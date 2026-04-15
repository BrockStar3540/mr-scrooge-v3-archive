"""Ratchet manager — locks percentage of unrealized gains.

Engineering extension from Part II Section 32.
Provides mechanical discipline beyond the source theory's qualitative trailing rules.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import StopPlan, TradeDirection

log = logging.getLogger("scrooge_v3.management.ratchet")


class RatchetManager:
    """Locks a percentage of unrealized gains at periodic intervals."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.lock_pct = config.get("ratchet_lock_pct", 0.50)
        self.min_profit_pips = config.get("ratchet_min_profit_pips", 10.0)

    def compute_ratchet_stop(
        self,
        direction: TradeDirection,
        entry_price: float,
        current_price: float,
        current_stop: float,
        pip_size: float = 0.0001,
    ) -> StopPlan | None:
        """Compute ratcheted stop that locks a fraction of unrealized profit.

        Only activates when profit exceeds min_profit_pips.
        Never loosens the stop — only tightens.
        """
        if direction == TradeDirection.LONG:
            profit_pips = (current_price - entry_price) / pip_size
        else:
            profit_pips = (entry_price - current_price) / pip_size

        if profit_pips < self.min_profit_pips:
            return None

        # Lock lock_pct of the move from entry
        locked_distance = abs(current_price - entry_price) * self.lock_pct

        if direction == TradeDirection.LONG:
            new_stop = entry_price + locked_distance
            if new_stop <= current_stop:
                return None  # Would loosen
        else:
            new_stop = entry_price - locked_distance
            if new_stop >= current_stop:
                return None

        return StopPlan(
            position_id="",
            new_stop=new_stop,
            reason=f"ratchet lock {self.lock_pct:.0%} of {profit_pips:.1f} pips",
        )
