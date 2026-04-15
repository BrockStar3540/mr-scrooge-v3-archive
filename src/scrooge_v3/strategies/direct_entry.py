"""Direct entry strategy — zone-based entry when V3 scorer qualifies.

Unlike reversal/trend strategies that require specific BB states,
this strategy is always eligible. It uses zone detector data to set
entry at current price, SL at nearest zone boundary + buffer, and
TP at opposite boundary. Quality gating is handled entirely by the
V3 scorer downstream.

This exists because the V3 scoring data shows profitable trades
at BB NORMAL state (e.g. 00-07 UTC + BB NORM = 9W/0L, +14 pts).
The old BB-state routing blocks these setups.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from scrooge_v3.core.types import (
    SymbolContext,
    TradeCandidate,
    TradeDirection,
)

log = logging.getLogger("scrooge_v3.strategy.direct_entry")

DIRECT_FIXED_SCORE = 1  # Placeholder — V3 scorer replaces this


class DirectEntryStrategy:
    """Zone-based entry, quality deferred to V3 scorer.

    Implements StrategyModule Protocol.
    """

    name = "direct"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)

    def eligible(self, ctx: SymbolContext) -> bool:
        """Always eligible — the scorer decides quality."""
        if not self.enabled:
            return False
        # Need zone detector data for entry mechanics
        zd = ctx.features.get("zone_detector")
        if not zd or not zd.values.get("zone_map"):
            return False
        return True

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        """Build candidate from zone structure + price location."""
        zd = ctx.features.get("zone_detector")
        if not zd:
            return None
        zone_map = zd.values.get("zone_map")
        if zone_map is None:
            return None

        sr = getattr(zone_map, "session_range", None)
        if sr is None:
            return None

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        price = ctx.snapshot.mid
        pdh = sr.PDH
        pdl = sr.PDL
        center = (pdh + pdl) / 2
        box_range = pdh - pdl

        if box_range < pip * 5:
            return None  # Box too tight

        # Direction: if price in lower half → LONG, upper half → SHORT
        if price < center:
            direction = TradeDirection.LONG
            sl = pdl - pip * 3
            tp = pdh
        else:
            direction = TradeDirection.SHORT
            sl = pdh + pip * 3
            tp = pdl

        risk = abs(price - sl)
        reward = abs(tp - price)
        if risk <= 0:
            return None
        rr = reward / risk

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=self.name,
            entry_price=price,
            stop_price=sl,
            take_profit=tp,
            size=0.0,
            risk_reward=rr,
            score=DIRECT_FIXED_SCORE,
            metadata={
                "entry_type": "DIRECT",
                "risk_points": risk,
                "reward_points": reward,
                "tp1": center,
                "tp2": tp,
            },
            created_at=datetime.now(timezone.utc),
        )
