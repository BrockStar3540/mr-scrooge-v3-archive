"""Break-even manager — removes risk after confirmation.

Source theory Section 17: "Move the remainder of the stop-loss around break even.
This way I'm out of the risk."

Triggers after partial take profit or when price moves favorably by N pips.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import StopPlan, TradeDirection

log = logging.getLogger("scrooge_v3.management.break_even")


class BreakEvenManager:
    """Moves stop to break-even after conditions are met."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.trigger_pips = config.get("be_trigger_pips", 15.0)
        self.offset_pips = config.get("be_offset_pips", 1.0)  # small profit buffer

    def should_move_to_be(
        self,
        direction: TradeDirection,
        entry_price: float,
        current_price: float,
        current_stop: float,
        pip_size: float = 0.0001,
        partial_taken: bool = False,
    ) -> StopPlan | None:
        """Check if stop should be moved to break-even.

        Triggers when:
          - Partial profit has been taken, OR
          - Price has moved trigger_pips in our favor

        Never moves stop backwards from a better position.
        """
        if direction == TradeDirection.LONG:
            profit_pips = (current_price - entry_price) / pip_size
            be_stop = entry_price + self.offset_pips * pip_size
            # Only move if currently below BE
            if current_stop >= be_stop:
                return None
        else:
            profit_pips = (entry_price - current_price) / pip_size
            be_stop = entry_price - self.offset_pips * pip_size
            if current_stop <= be_stop:
                return None

        if not partial_taken and profit_pips < self.trigger_pips:
            return None

        return StopPlan(
            position_id="",
            new_stop=be_stop,
            reason=f"break_even at {be_stop:.5f} (profit={profit_pips:.1f} pips, partial={partial_taken})",
        )
