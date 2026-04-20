"""Break-even manager — removes risk after confirmation.

Source theory Section 17: "Move the remainder of the stop-loss around break even.
This way I'm out of the risk."

Phase 3 (fix/mgmt-r-unified): trigger and offset are expressed in R with
pip floors, so the same config works for tight (AUD/USD R=3.6 pips) and
wide (USD/JPY R=18 pips) stops.

  effective_trigger_dist = max(trigger_r * R, trigger_min_pips * pip_size)
  effective_offset_dist  = max(offset_r  * R,  offset_min_pips * pip_size)

The offset floor specifically guards against sub-pip BE placement on JPY
pairs inside broker spread (the AUD/JPY trade 1488 family of bugs).
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import StopPlan, TradeDirection

log = logging.getLogger("scrooge_v3.management.break_even")


class BreakEvenManager:
    """Moves stop to break-even after conditions are met."""

    def __init__(self, config: dict | None = None):
        config = config or {}

        # Legacy fixed-pip keys (deprecated, still readable).
        legacy_trigger = config.get("be_trigger_pips")
        legacy_offset = config.get("be_offset_pips")
        if legacy_trigger is not None or legacy_offset is not None:
            log.warning(
                "[BE_MANAGER] DEPRECATED config keys be_trigger_pips/be_offset_pips "
                "detected — migrate to be_trigger_r/be_offset_r with "
                "be_trigger_min_pips/be_offset_min_pips floors."
            )

        # New R-relative keys with pip floors.
        self.trigger_r = float(config.get("be_trigger_r", 0.5))
        self.trigger_min_pips = float(
            config.get("be_trigger_min_pips", legacy_trigger if legacy_trigger is not None else 2.0)
        )
        self.offset_r = float(config.get("be_offset_r", 0.1))
        self.offset_min_pips = float(
            config.get("be_offset_min_pips", legacy_offset if legacy_offset is not None else 1.0)
        )

    def should_move_to_be(
        self,
        direction: TradeDirection,
        entry_price: float,
        current_price: float,
        current_stop: float,
        pip_size: float = 0.0001,
        partial_taken: bool = False,
        initial_risk_distance: float = 0.0,
    ) -> StopPlan | None:
        """Check if stop should be moved to break-even.

        Triggers when:
          - Partial profit has been taken, OR
          - Price has moved `effective_trigger_dist` in our favor

        Never moves stop backwards from a better position.
        """
        # Effective trigger = max(r * R, min_pips * pip_size). If we don't know
        # R (legacy call-site), fall back to pure pip floor.
        if initial_risk_distance > 0:
            trigger_dist = max(
                self.trigger_r * initial_risk_distance,
                self.trigger_min_pips * pip_size,
            )
            offset_dist = max(
                self.offset_r * initial_risk_distance,
                self.offset_min_pips * pip_size,
            )
        else:
            trigger_dist = self.trigger_min_pips * pip_size
            offset_dist = self.offset_min_pips * pip_size

        if direction == TradeDirection.LONG:
            profit_dist = current_price - entry_price
            be_stop = entry_price + offset_dist
            if current_stop >= be_stop:
                return None
        else:
            profit_dist = entry_price - current_price
            be_stop = entry_price - offset_dist
            if current_stop <= be_stop:
                return None

        if not partial_taken and profit_dist < trigger_dist:
            return None

        profit_pips = profit_dist / pip_size if pip_size > 0 else 0.0
        log.info(
            "[BE_MANAGER] compute_be: dir=%s entry=%.5f offset_dist=%.6f "
            "pip_size=%.5f be_stop=%.5f profit_pips=%.2f partial=%s",
            direction.value, entry_price, offset_dist, pip_size,
            be_stop, profit_pips, partial_taken,
        )
        return StopPlan(
            position_id="",
            new_stop=be_stop,
            reason=f"break_even at {be_stop:.5f} (profit={profit_pips:.1f} pips, partial={partial_taken})",
        )
