"""Partial harvest — take partial profits at targets.

Source theory Section 17: "Sell half of my position, pay myself."
Standard pattern: take 1/2 off → move stop to BE → let the rest work.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from scrooge_v3.core.types import TradeDirection

log = logging.getLogger("scrooge_v3.management.partial_harvest")


@dataclass
class HarvestAction:
    """Describes a partial take-profit action."""

    position_id: str
    close_fraction: float  # e.g. 0.5 = close half
    reason: str
    target_label: str  # "tp1", "tp2"


class PartialHarvestManager:
    """Manages partial take-profit harvesting."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.tp1_fraction = config.get("tp1_fraction", 0.50)

    def check_harvest(
        self,
        position_id: str,
        direction: TradeDirection,
        current_price: float,
        tp1_price: float,
        tp1_taken: bool = False,
    ) -> HarvestAction | None:
        """Check if partial profit should be taken.

        Returns HarvestAction if TP1 hit and not yet taken.
        """
        if tp1_taken:
            return None

        if direction == TradeDirection.LONG:
            if current_price >= tp1_price:
                return HarvestAction(
                    position_id=position_id,
                    close_fraction=self.tp1_fraction,
                    reason=f"TP1 hit at {current_price:.5f} >= {tp1_price:.5f}",
                    target_label="tp1",
                )
        else:
            if current_price <= tp1_price:
                return HarvestAction(
                    position_id=position_id,
                    close_fraction=self.tp1_fraction,
                    reason=f"TP1 hit at {current_price:.5f} <= {tp1_price:.5f}",
                    target_label="tp1",
                )

        return None
