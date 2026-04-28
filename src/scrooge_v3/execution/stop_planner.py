"""Stop planner — trigger-side aware stop loss management.

Implements the V3 execution doctrine:
  1. Trigger-side validation (short SL vs ASK, long SL vs BID)
  2. No-man's-zone guard (never place SL inside spread)
  3. Spread-aware trailing (pause in hostile spread)
  4. Hybrid SL: native SL backstop + proactive limit for better fill

Extracted from V2 coordinator._manage_sl_limit() (lines 868-1027).
"""

from __future__ import annotations

import logging
from typing import Any

from scrooge_v3.core.types import StopPlan, TradeDirection

log = logging.getLogger("scrooge_v3.execution.stop_planner")


class StopPlanner:
    """Plans stop loss updates with trigger-side and spread awareness.

    Implements ExecutionPolicy.plan_stop_update() interface.
    """

    name = "stop_planner"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.trigger_buffer_pips = config.get("trigger_buffer_pips", 3.0)
        self.limit_offset_pips = config.get("limit_offset_pips", 0.5)
        self.fallback_buffer_pips = config.get("fallback_buffer_pips", 10.0)
        self.fast_market_multiplier = config.get("fast_market_multiplier", 2.5)

    def validate_stop(
        self,
        direction: TradeDirection,
        proposed_stop: float,
        bid: float,
        ask: float,
        spread: float,
    ) -> tuple[float, str]:
        """Validate and adjust a stop price for trigger-side safety.

        Returns (adjusted_stop, reason).

        Execution doctrine:
          - Short SL triggers on ASK → validate vs ask
          - Long SL triggers on BID → validate vs bid
          - Never place inside spread (no-man's-zone)
        """
        pip = self._pip_size_from_price(proposed_stop)
        # Phase 3 / Bug J instrumentation — trace pip_size inference at this
        # layer so we can detect the JPY offset bug in the wild.
        log.debug(
            "[STOP_PLANNER][FORENSIC] validate_stop dir=%s proposed=%.6f "
            "inferred_pip=%.5f bid=%.5f ask=%.5f spread=%.6f",
            direction.value, proposed_stop, pip, bid, ask, spread,
        )

        if direction == TradeDirection.SHORT:
            # Short SL triggers when ASK >= SL
            # SL must be safely above current ASK + buffer
            min_safe = ask + spread + pip * 2
            if proposed_stop < min_safe:
                log.info(
                    "[STOP_PLANNER] NO_MANS_ZONE short: proposed=%.5f < min_safe=%.5f (ask=%.5f spread=%.5f)",
                    proposed_stop, min_safe, ask, spread,
                )
                return min_safe, "adjusted_above_spread"
        else:
            # Long SL triggers when BID <= SL
            # SL must be safely below current BID - buffer
            max_safe = bid - spread - pip * 2
            if proposed_stop > max_safe:
                log.info(
                    "[STOP_PLANNER] NO_MANS_ZONE long: proposed=%.5f > max_safe=%.5f (bid=%.5f spread=%.5f)",
                    proposed_stop, max_safe, bid, spread,
                )
                return max_safe, "adjusted_below_spread"

        return proposed_stop, "valid"

    def is_entry_spread_hostile(
        self,
        spread: float,
        mean_spread: float,
    ) -> tuple[bool, str]:
        """Dedicated entry-spread preflight. Returns (hostile, reason).

        Earlier versions reused should_trail() for entry-time spread vetoes,
        but that helper checks tightness first and returns
        new_stop_not_tighter on fresh entries (validated_sl == best.stop_price),
        which is NOT hostile_spread, so the entry kill-switch was bypassed.
        This method evaluates ONLY spread fastness, ignoring stop geometry.
        """
        if mean_spread > 0 and spread > mean_spread * self.fast_market_multiplier:
            return True, (
                f"hostile_spread ({spread:.5f} > {mean_spread * self.fast_market_multiplier:.5f})"
            )
        return False, "spread_normal"

    def should_trail(
        self,
        direction: TradeDirection,
        current_stop: float,
        new_stop: float,
        spread: float,
        mean_spread: float,
    ) -> tuple[bool, str]:
        """Determine if trailing should proceed given spread conditions.

        Spread-aware trailing: do not tighten stops in hostile spread.
        """
        # Only trail if new stop is tighter (better for us)
        if direction == TradeDirection.LONG:
            if new_stop <= current_stop:
                return False, "new_stop_not_tighter"
        else:
            if new_stop >= current_stop:
                return False, "new_stop_not_tighter"

        # Check for hostile spread
        if mean_spread > 0 and spread > mean_spread * self.fast_market_multiplier:
            return False, f"hostile_spread ({spread:.5f} > {mean_spread * self.fast_market_multiplier:.5f})"

        return True, "trail_approved"

    def plan_stop_update(
        self,
        position_id: str,
        direction: TradeDirection,
        proposed_stop: float,
        bid: float,
        ask: float,
        spread: float,
    ) -> StopPlan | None:
        """Create a validated stop update plan.

        Returns None if the stop placement is unsafe.
        """
        adjusted, reason = self.validate_stop(direction, proposed_stop, bid, ask, spread)

        if reason == "valid":
            return StopPlan(
                position_id=position_id,
                new_stop=adjusted,
                reason="validated",
            )

        # Stop was adjusted for safety
        return StopPlan(
            position_id=position_id,
            new_stop=adjusted,
            reason=reason,
            metadata={"original_proposed": proposed_stop, "adjustment": reason},
        )

    def is_fast_market(
        self,
        candle_range: float,
        avg_range: float,
    ) -> bool:
        """Detect fast market conditions from candle range vs average."""
        if avg_range <= 0:
            return False
        return candle_range >= avg_range * self.fast_market_multiplier

    @staticmethod
    def _pip_size_from_price(price: float) -> float:
        """Infer pip size from price magnitude.

        WARNING: this is a heuristic. For anything needing correctness (BE
        offset, TP1 placement), use `scrooge_v3.core.trade_geometry.pip_size`
        with the actual symbol. This heuristic exists only so `validate_stop`
        can compute a no-mans-zone buffer without knowing the symbol.
        """
        if price > 10:  # JPY pairs have quote magnitude ~100
            return 0.01
        return 0.0001
