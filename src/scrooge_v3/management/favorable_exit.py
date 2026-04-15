"""Favorable exit — limit-order exit when conditions justify closing.

Extracted from V2 coordinator._handle_green_exit() (lines 758-853).
Places a limit order inside the spread for a better fill, with
market-close fallback in fast markets.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from scrooge_v3.core.types import TradeDirection

log = logging.getLogger("scrooge_v3.management.favorable_exit")


@dataclass
class FavorableExitPlan:
    """Plan for a favorable exit."""

    position_id: str
    method: str  # "limit" or "market"
    limit_price: float = 0.0
    reason: str = ""
    expiry_seconds: int = 600  # 10 minutes


class FavorableExitManager:
    """Plans favorable exits with limit-order preference.

    In normal conditions: places a limit order inside the spread.
    In fast markets: closes at market immediately.
    """

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.offset_pips = config.get("favorable_exit_offset_pips", 0.5)
        self.expiry_seconds = config.get("favorable_exit_expiry_seconds", 600)

    def plan_exit(
        self,
        position_id: str,
        direction: TradeDirection,
        bid: float,
        ask: float,
        is_fast_market: bool = False,
        reason: str = "conditions_reversed",
    ) -> FavorableExitPlan:
        """Plan a favorable exit.

        Fast market → market close (no limit).
        Normal → limit inside spread for better fill.
        """
        pip = 0.01 if bid > 10 else 0.0001
        offset = self.offset_pips * pip

        if is_fast_market:
            return FavorableExitPlan(
                position_id=position_id,
                method="market",
                reason=f"fast_market: {reason}",
            )

        # Place limit inside spread for favorable fill
        if direction == TradeDirection.LONG:
            # Closing a long = selling → want to sell at higher price
            limit_price = ask - offset
        else:
            # Closing a short = buying → want to buy at lower price
            limit_price = bid + offset

        return FavorableExitPlan(
            position_id=position_id,
            method="limit",
            limit_price=limit_price,
            reason=reason,
            expiry_seconds=self.expiry_seconds,
        )
