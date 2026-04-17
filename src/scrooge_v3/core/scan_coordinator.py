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

        # Get active pairs for current session
        from scrooge_v3.market.screener import get_session_pairs
        pairs = get_session_pairs(now.hour)
        if not pairs:
            log.debug("[SCAN] No active pairs this session")
            return result

        # Fetch market snapshots from broker
        snapshots = self._fetch_snapshots(pairs, now)
        result.pairs_scanned = len(snapshots)

        # Run scan pipeline — returns candidates + full per-pair reports
        candidates, reports = ctx.scan_pipeline.scan_universe(pairs, snapshots)
        result.reports = reports

        # Filter out symbols we already have a position in or pending entry for
        held_symbols = {pos.symbol for pos in ctx.tracker.all_positions()}
        pending_symbols = set(ctx.tracker.all_pending_entries().keys())
        candidates = [c for c in candidates if c.symbol not in held_symbols and c.symbol not in pending_symbols]

        if not candidates or ctx.state.position_count >= ctx.state.max_positions:
            result.candidates = candidates
            return result

        # --- Throttle: max pending entries ---
        pending_count = len(ctx.tracker.all_pending_entries())
        max_pending = 2
        if pending_count >= max_pending:
            log.info("[SCAN] Throttled: %d pending entries >= max %d", pending_count, max_pending)
            result.candidates = []
            return result

        # --- Throttle: currency correlation gate ---
        # Don't stack trades on the same base or quote currency
        open_currencies = set()
        for pos in ctx.tracker.all_positions():
            parts = pos.symbol.split("_")
            if len(parts) == 2:
                open_currencies.add(parts[0])
                open_currencies.add(parts[1])
        for sym in ctx.tracker.all_pending_entries().keys():
            parts = sym.split("_")
            if len(parts) == 2:
                open_currencies.add(parts[0])
                open_currencies.add(parts[1])

        # Filter out candidates that share a currency with open/pending positions
        uncorrelated = []
        for c in candidates:
            parts = c.symbol.split("_")
            if len(parts) == 2:
                base, quote = parts
                if base in open_currencies or quote in open_currencies:
                    log.debug("[SCAN] Correlation filter: %s blocked (overlap with %s)",
                              c.symbol, open_currencies & {base, quote})
                    continue
            uncorrelated.append(c)

        if uncorrelated:
            candidates = uncorrelated
        else:
            # All candidates correlate — allow best one if no open positions at all
            if not ctx.tracker.all_positions() and not ctx.tracker.all_pending_entries():
                pass  # First trade of the session, allow it
            else:
                log.info("[SCAN] All candidates correlated with open/pending — skipping")
                result.candidates = []
                return result

        best = candidates[0]
        log.info("[SCAN] Best candidate: %s %s score=%.0f",
                 best.symbol, best.strategy, best.score)

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
