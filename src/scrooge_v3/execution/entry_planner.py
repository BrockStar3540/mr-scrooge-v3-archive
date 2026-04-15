"""Entry planner — plans and validates entry orders.

Extracted from V2 coordinator fire_entry() (lines 1109-1257).
Handles sizing adjustments, staleness checks, and order plan creation.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import OrderPlan, SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.execution.entry_planner")


class EntryPlanner:
    """Plans entry orders from approved trade candidates.

    Applies:
      - Position sizing
      - Off-peak session reduction
      - Regime-based size adjustment
      - Range confidence multiplier
      - Trend entry size reduction
      - Staleness validation (price already past entry)
      - TP2 market guard
    """

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.off_peak_reduction = config.get("off_peak_reduction", 0.50)
        self.restricted_reduction = config.get("restricted_reduction", 0.50)
        self.trend_full_fraction = config.get("trend_full_size_fraction", 0.50)
        self.trend_stretch_fraction = config.get("trend_stretch_size_fraction", 0.30)

    def plan(
        self,
        candidate: TradeCandidate,
        ctx: SymbolContext,
        base_units: int,
        regime_state: str = "NORMAL",
        is_off_peak: bool = False,
        range_confidence: float = 1.0,
    ) -> OrderPlan | None:
        """Create an order plan from an approved candidate.

        Returns None if validation fails (stale, TP2 guard, etc.)
        """
        units = float(base_units)

        # Off-peak reduction (Sydney/Tokyo sessions)
        if is_off_peak:
            units *= self.off_peak_reduction
            log.debug("[ENTRY_PLANNER] Off-peak reduction: %.0f units", units)

        # Regime-based reduction
        if regime_state == "RESTRICTED":
            units *= self.restricted_reduction
            log.debug("[ENTRY_PLANNER] Regime restricted reduction: %.0f units", units)

        # Range confidence multiplier
        if range_confidence < 1.0:
            units *= range_confidence
            log.debug("[ENTRY_PLANNER] Range confidence %.2f: %.0f units", range_confidence, units)

        # Trend entry reduction
        entry_type = candidate.metadata.get("entry_type", "")
        if entry_type == "TREND_FULL":
            units *= self.trend_full_fraction
        elif entry_type == "TREND_STRETCH":
            units *= self.trend_stretch_fraction

        units = max(1, round(units))

        # Staleness check — price already past entry
        pip = 0.01 if "JPY" in candidate.symbol else 0.0001
        if candidate.direction == TradeDirection.LONG:
            if ctx.snapshot.ask > candidate.entry_price + pip * 5:
                log.info(
                    "[ENTRY_PLANNER] STALE symbol=%s ask=%.5f > entry=%.5f",
                    candidate.symbol, ctx.snapshot.ask, candidate.entry_price,
                )
                return None
        else:
            if ctx.snapshot.bid < candidate.entry_price - pip * 5:
                log.info(
                    "[ENTRY_PLANNER] STALE symbol=%s bid=%.5f < entry=%.5f",
                    candidate.symbol, ctx.snapshot.bid, candidate.entry_price,
                )
                return None

        # TP2 market guard
        tp2 = candidate.take_profit
        if tp2 is not None:
            buf = pip * 2
            if candidate.direction == TradeDirection.LONG and tp2 <= ctx.snapshot.mid + buf:
                log.info("[ENTRY_PLANNER] TP2 guard: tp2=%.5f <= mid+buf", tp2)
                return None
            if candidate.direction == TradeDirection.SHORT and tp2 >= ctx.snapshot.mid - buf:
                log.info("[ENTRY_PLANNER] TP2 guard: tp2=%.5f >= mid-buf", tp2)
                return None

        return OrderPlan(
            symbol=candidate.symbol,
            direction=candidate.direction,
            entry_price=candidate.entry_price,
            stop_price=candidate.stop_price,
            take_profit=candidate.take_profit,
            size=units,
            order_type="MARKET",
            metadata={
                "strategy": candidate.strategy,
                "score": candidate.score,
                "risk_reward": candidate.risk_reward,
                "entry_type": entry_type,
                "regime_state": regime_state,
                "range_confidence": range_confidence,
            },
        )
