"""Scan coordinator — orchestrates the per-cycle market scan.

Owns: pair universe, market data fetching, scan pipeline invocation,
candidate filtering (held/pending symbols), spread quality gating.

Does NOT own: order placement, position management, dashboard publishing.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .types import MarketSnapshot, TradeCandidate

log = logging.getLogger("scrooge_v3.core.scan_coordinator")


@dataclass
class ScanResult:
    """Result of one scan cycle."""
    candidates: list[TradeCandidate] = field(default_factory=list)
    reports: list[dict[str, Any]] = field(default_factory=list)
    pairs_scanned: int = 0
    best_candidate: TradeCandidate | None = None
    spread_skip: bool = False
    spread_skip_symbol: str = ""
    spread_skip_ratio: float = 0.0


class ScanCoordinator:
    """Orchestrates the market scan phase of each cycle.

    Fetches market data, runs the scan pipeline across all active pairs,
    filters out held/pending symbols, and applies the spread quality gate.
    Returns a ScanResult for the runtime to act on.
    """

    def __init__(self, ctx: Any):
        self.ctx = ctx

    def scan_cycle(self, now: datetime) -> ScanResult:
        """Run one complete scan cycle.

        Returns ScanResult with candidates, reports, and best candidate.
        """
        ctx = self.ctx
        result = ScanResult()

        # screener-disconnected (Brock 2026-05-28): ML library encodes
        # (pair, session, regime) edge already — let ml_router decide
        # admit, not a hardcoded hour filter. Was returning a 6-pair
        # subset at Sydney-only hours, blocking EUR_USD/GBP_USD/USD_JPY.
        from scrooge_v3.market.screener import CANDIDATE_PAIRS
        from scrooge_v3.advisors import lightgbm_shadow
        pairs = list(CANDIDATE_PAIRS)
        if not getattr(self.__class__, "_screener_disconnect_logged", False):
            log.info(
                "[SCAN] Session filter DISABLED — scanning all %d pairs "
                "every cycle (ML decides admit per pair).",
                len(pairs),
            )
            self.__class__._screener_disconnect_logged = True

        # Fetch market snapshots from broker
        snapshots = self._fetch_snapshots(pairs, now)
        result.pairs_scanned = len(snapshots)

        # Phase 4: build the state dict handed into every gate.
        gate_state: dict[str, Any] = {
            "zone_last_entry": {
                k: v.isoformat() for k, v in
                getattr(ctx.state, "zone_debounce", {}).items()
            },
            "zone_entries_today": dict(
                getattr(ctx.state, "zone_entry_counts", {})
            ),
        }
        tracker_obj = getattr(ctx, "cooldown_tracker", None)
        if tracker_obj is not None:
            try:
                gate_state.update(tracker_obj.to_state_dict())
            except Exception:
                log.exception("[SCAN] cooldown_tracker.to_state_dict failed")

        # Run scan pipeline — returns candidates + full per-pair reports
        candidates, reports = ctx.scan_pipeline.scan_universe(
            pairs, snapshots, state=gate_state,
        )
        result.reports = reports

        # ----- LightGBM primary gate (lightgbm_gate_live) -----
        # Brock 2026-05-28: LightGBM scores every gate-approved candidate;
        # drop those below p_win threshold; re-sort surviving candidates by
        # p_win so candidates[0] is the highest-confidence pick.
        try:
            from scrooge_v3.advisors import lightgbm_shadow as _lgbm
            from scrooge_v3.core.types import SymbolContext, FeatureResult
            _scored = []
            for _c in candidates:
                _rep = next((r for r in reports if r.get("symbol") == _c.symbol), None)
                if _rep is None:
                    continue
                _ctx = SymbolContext(
                    symbol=_c.symbol,
                    snapshot=snapshots.get(_c.symbol),
                    features={
                        k: FeatureResult(name=k, values=v if isinstance(v, dict) else {})
                        for k, v in _rep.get("features", {}).items()
                    },
                    state={"session_bucket": _rep.get("classifications", {})
                              .get("session_bucket", {}).get("label", "unknown")},
                )
                _pw = _lgbm.predict_p_win(_c.symbol, _ctx, _c)
                if _pw is None:
                    # Couldn't score — skip rather than admit blind.
                    log.info("[LIGHTGBM] UNSCORABLE %s %s — dropped",
                             _c.symbol, _c.strategy)
                    continue
                _c.metadata["lightgbm_p_win"] = round(_pw, 4)
                _c.metadata["pre_lgbm_score"] = float(_c.score)
                if _pw < _lgbm.THRESHOLD:
                    log.info("[LIGHTGBM] BLOCKED %s %s p_win=%.3f<%.2f",
                             _c.symbol, _c.strategy, _pw, _lgbm.THRESHOLD)
                    continue
                log.info("[LIGHTGBM] PASS    %s %s p_win=%.3f",
                         _c.symbol, _c.strategy, _pw)
                _c.score = float(_pw)  # rank downstream by p_win
                _scored.append(_c)
            # Re-rank survivors by p_win descending
            _scored.sort(key=lambda c: c.score, reverse=True)
            candidates = _scored
        except Exception:
            log.exception("[LIGHTGBM] live gate failed — falling back to score ranking")

        # Brock 2026-06-04: SAME-PAIR STACKING ALLOWED. A fresh signal fires
        # regardless of what's already open on that symbol. Only dedup in-flight
        # pending entries. Global max_positions (8) remains the hard total cap.
        pending_symbols = set(ctx.tracker.all_pending_entries().keys())
        candidates = [c for c in candidates if c.symbol not in pending_symbols]

        if not candidates or ctx.state.position_count >= ctx.state.max_positions:
            result.candidates = candidates
            return result

        # --- Throttle: max pending entries ---
        pending_count = len(ctx.tracker.all_pending_entries())
        max_pending = 6   # Brock 2026-05-25: loosened from 2 for 452-cell broad-coverage bank
        if pending_count >= max_pending:
            log.info("[SCAN] Throttled: %d pending entries >= max %d", pending_count, max_pending)
            result.candidates = []
            return result

        # --- Throttle: currency exposure cap (loosened 2026-05-25) ---
        # OLD rule was: block ANY pair sharing base OR quote with open/pending.
        # That starved the 452-cell bank — one AUD_JPY open killed 10+ pairs.
        # NEW rule: cap exposure at MAX_PER_CURRENCY positions per currency.
        # Also block exact-pair stacking (same symbol already open or pending).
        MAX_PER_CURRENCY = 8  # Brock 2026-06-04: non-binding (== max_positions) — pair/currency stacking allowed
        currency_counts: dict[str, int] = {}
        open_symbols: set[str] = set()
        for pos in ctx.tracker.all_positions():
            open_symbols.add(pos.symbol)
            parts = pos.symbol.split("_")
            if len(parts) == 2:
                currency_counts[parts[0]] = currency_counts.get(parts[0], 0) + 1
                currency_counts[parts[1]] = currency_counts.get(parts[1], 0) + 1
        for sym in ctx.tracker.all_pending_entries().keys():
            open_symbols.add(sym)
            parts = sym.split("_")
            if len(parts) == 2:
                currency_counts[parts[0]] = currency_counts.get(parts[0], 0) + 1
                currency_counts[parts[1]] = currency_counts.get(parts[1], 0) + 1

        uncorrelated = []
        for c in candidates:
            # Brock 2026-06-04: same-pair stacking allowed — no exact-pair block.
            parts = c.symbol.split("_")
            if len(parts) == 2:
                base, quote = parts
                # Block only if adding this would push currency exposure past cap
                if (currency_counts.get(base, 0) >= MAX_PER_CURRENCY or
                    currency_counts.get(quote, 0) >= MAX_PER_CURRENCY):
                    log.debug("[SCAN] Currency cap: %s blocked (base=%d quote=%d, cap=%d)",
                              c.symbol, currency_counts.get(base,0),
                              currency_counts.get(quote,0), MAX_PER_CURRENCY)
                    continue
            uncorrelated.append(c)

        if uncorrelated:
            candidates = uncorrelated
        else:
            log.info("[SCAN] All candidates blocked by currency cap or exact-pair stacking — skipping")
            result.candidates = []
            return result

        best = candidates[0]
        log.info("[SCAN] Best candidate: %s %s score=%.0f",
                 best.symbol, best.strategy, best.score)

        # LightGBM shadow scorer (Brock 2026-05-28): observe-only P(win)
        # logging for the selected candidate. Look up the pair's report
        # to recover ctx-derived buckets via ml_router. Never blocks.
        try:
            best_report = next((r for r in reports if r.get("symbol") == best.symbol), None)
            if best_report is not None:
                # Reconstruct minimal ctx from report — ml_router._compute_buckets
                # works off feature values which are in the report.
                from scrooge_v3.core.types import SymbolContext, FeatureResult
                ctx_for_shadow = SymbolContext(
                    symbol=best.symbol,
                    snapshot=snapshots.get(best.symbol),
                    features={
                        k: FeatureResult(name=k, values=v if isinstance(v, dict) else {})
                        for k, v in best_report.get("features", {}).items()
                    },
                    state={"session_bucket": best_report.get("classifications", {})
                              .get("session_bucket", {}).get("label", "unknown")},
                )
                lightgbm_shadow.observe(best.symbol, ctx_for_shadow, best,
                                         all_candidates=candidates)
                # LightGBM v1 pip-shadow observe UNPLUGGED 2026-06-04 (moved to ML Lab)
                # Matrix shadow advisor observe UNPLUGGED 2026-06-04 (moved to ML Lab)
        except Exception:
            log.debug("[SHADOW] observe failed", exc_info=True)

        # Spread quality gate: skip entry if spread is elevated vs rolling mean
        spread_stats = ctx.spread_monitor.get_stats(best.symbol)
        if spread_stats["mean"] > 0:
            spread_ratio = spread_stats["current"] / spread_stats["mean"]
            if spread_ratio > 1.5:
                log.warning("[SCAN] ENTRY SKIPPED: %s spread elevated (%.1fx mean: "
                            "current=%.5f mean=%.5f)",
                            best.symbol, spread_ratio,
                            spread_stats["current"], spread_stats["mean"])
                result.spread_skip = True
                result.spread_skip_symbol = best.symbol
                result.spread_skip_ratio = spread_ratio
                result.candidates = []
                return result

        result.candidates = candidates
        result.best_candidate = best
        return result

    def _fetch_snapshots(
        self, pairs: list[str], now: datetime,
    ) -> dict[str, MarketSnapshot]:
        """Fetch market data for all pairs from broker."""
        ctx = self.ctx
        prices = ctx.broker.get_prices(pairs)
        snapshots: dict[str, MarketSnapshot] = {}

        for symbol, quote in prices.items():
            candles = {}
            for oanda_tf, internal_key in (("D", "D"), ("H1", "1H"), ("M5", "5M")):
                df = ctx.broker.get_candles(symbol, oanda_tf)
                if df is not None:
                    candles[internal_key] = df

            snapshots[symbol] = MarketSnapshot(
                symbol=symbol,
                bid=quote.bid,
                ask=quote.ask,
                mid=quote.mid,
                spread=quote.spread,
                timestamp=quote.timestamp or now,
                candles=candles,
            )
            ctx.spread_monitor.record(symbol, quote.spread)

        return snapshots
