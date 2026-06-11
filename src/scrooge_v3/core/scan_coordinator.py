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
            # Re-rank survivors by (cell_hits, p_win) descending — a candidate
            # with more validated cell-sides vouching for it outranks a
            # single-hit one; p_win breaks ties (Brock 2026-06-11).
            _scored.sort(
                key=lambda c: (
                    int((getattr(c, "metadata", None) or {}).get("cell_hits", 0) or 0),
                    c.score,
                ),
                reverse=True,
            )
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
        # Brock 2026-06-08: hard per-pair cap — at most N concurrent trades per symbol.
        try:
            MAX_PER_PAIR = int((ctx.config.section("risk") or {}).get("max_per_pair", 2))
        except Exception:
            MAX_PER_PAIR = 2
        currency_counts: dict[str, int] = {}
        symbol_counts: dict[str, int] = {}
        open_symbols: set[str] = set()
        for pos in ctx.tracker.all_positions():
            open_symbols.add(pos.symbol)
            symbol_counts[pos.symbol] = symbol_counts.get(pos.symbol, 0) + 1
            parts = pos.symbol.split("_")
            if len(parts) == 2:
                currency_counts[parts[0]] = currency_counts.get(parts[0], 0) + 1
                currency_counts[parts[1]] = currency_counts.get(parts[1], 0) + 1
        for sym in ctx.tracker.all_pending_entries().keys():
            open_symbols.add(sym)
            symbol_counts[sym] = symbol_counts.get(sym, 0) + 1
            parts = sym.split("_")
            if len(parts) == 2:
                currency_counts[parts[0]] = currency_counts.get(parts[0], 0) + 1
                currency_counts[parts[1]] = currency_counts.get(parts[1], 0) + 1

        # Brock 2026-06-10: DUP GUARD — one concurrent position per
        # (pair, strategy, direction). The per-pair cap=2 is meant to allow two
        # IDEAS on a pair, but a persisting signal was getting approved again on
        # the next 60s scan at full size (8073/8083, 8091/8099, 8115/8123,
        # 8155/8163 — each twin pair stopped in the same second, doubling the
        # loss for zero information gain). Different strategy or direction on
        # the same pair still stacks freely (2026-06-04 stacking intent).
        try:
            _dedup_same_signal = bool(
                (ctx.config.section("risk") or {}).get("dedup_same_signal", True))
        except Exception:
            _dedup_same_signal = True
        open_signal_keys: set = set()
        if _dedup_same_signal:
            for pos in ctx.tracker.all_positions():
                open_signal_keys.add((pos.symbol, pos.strategy, pos.direction))
        # Brock 2026-06-11 STATE-DEDUP v1 (full cell book era): one position
        # per (pair, direction) across ALL strategy names. 45% of signals are
        # shared states wearing different names; the name-keyed guard above
        # missed cross-name twins (8201/8217). Within-scan ownership of a
        # shared state stays with the p_win ranking (best candidate wins).
        try:
            _dedup_state = bool(
                (ctx.config.section("risk") or {}).get("dedup_same_state", True))
        except Exception:
            _dedup_state = True
        open_state_keys: set = set()
        if _dedup_state:
            for pos in ctx.tracker.all_positions():
                open_state_keys.add((pos.symbol, pos.direction))

        uncorrelated = []
        for c in candidates:
            _dirv = getattr(c.direction, "value", str(c.direction))
            if (c.symbol, _dirv) in open_state_keys:
                # ROTATION-ON-BLOCKED-SIGNAL (Brock 2026-06-11): a fresh
                # validated signal is knocking on an occupied slot. If the
                # sitting position is pre-TP1, >min_age old, and RED (corpus
                # conditional hold-value below a fresh cell's EV minus swap
                # cost -- 7,240-path OOS table, slot_econ.py), close it NOW;
                # the slot frees and the signal re-enters next scan if still
                # valid. Green/young/runner positions are never rotated
                # (hold-value beats rotation in every green bucket).
                try:
                    _rot = (ctx.config.section("risk") or {}).get("rotation", {})
                except Exception:
                    _rot = {}
                if _rot.get("enabled", True):
                    try:
                        from datetime import datetime as _dt, timezone as _tz
                        _min_age = float(_rot.get("min_age_minutes", 60))
                        _max_profit = float(_rot.get("max_profit_pips", 0.0))
                        for pos in ctx.tracker.all_positions():
                            if pos.symbol != c.symbol or pos.direction != _dirv:
                                continue
                            if getattr(pos, "tp1_taken", False):
                                break
                            try:
                                _age = (_dt.now(_tz.utc) - _dt.fromisoformat(
                                    str(pos.opened_at).replace("Z", "+00:00"))
                                    ).total_seconds() / 60.0
                            except Exception:
                                break
                            if _age < _min_age:
                                break
                            _snap = snapshots.get(c.symbol)
                            if _snap is None:
                                break
                            _pipsz = 0.01 if "JPY" in c.symbol else 0.0001
                            _sgn = 1 if pos.direction == "long" else -1
                            _profit = (_snap.mid - pos.entry_price) * _sgn / _pipsz
                            if _profit >= _max_profit:
                                break
                            log.warning("[SCAN] ROTATION: closing %s %s %s "
                                        "(age %.0fm, %+.1fp, pre-TP1) — fresh "
                                        "%s signal blocked on the slot",
                                        pos.trade_id, pos.symbol, pos.direction,
                                        _age, _profit, c.strategy)
                            try:
                                from scrooge_v3.management.green_exit import _xlog
                                _xlog(kind="rotation_close", trade_id=str(pos.trade_id),
                                      symbol=pos.symbol, age_min=round(_age),
                                      profit_pips=round(_profit, 1),
                                      blocked_strategy=c.strategy)
                            except Exception:
                                pass
                            try:
                                ctx.broker.close_trade(pos.trade_id)
                            except Exception:
                                log.exception("[SCAN] rotation close failed")
                            break
                    except Exception:
                        log.debug("[SCAN] rotation eval failed", exc_info=True)
                log.info("[SCAN] State dedup: %s %s blocked — position already "
                         "open on this pair+direction (any strategy)",
                         c.symbol, _dirv)
                continue
            _key = (c.symbol, c.strategy, _dirv)
            if _key in open_signal_keys:
                log.info("[SCAN] Dup guard: %s %s %s blocked — same signal "
                         "already has an open position", c.symbol, c.strategy,
                         _key[2])
                continue
            # Brock 2026-06-08: per-pair cap — at most MAX_PER_PAIR concurrent per symbol.
            if symbol_counts.get(c.symbol, 0) >= MAX_PER_PAIR:
                log.info("[SCAN] Per-pair cap: %s blocked (%d open/pending >= %d)",
                         c.symbol, symbol_counts.get(c.symbol, 0), MAX_PER_PAIR)
                continue
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
                df = ctx.broker.get_candles(symbol, oanda_tf, count=(130 if oanda_tf == "D" else 50))
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
