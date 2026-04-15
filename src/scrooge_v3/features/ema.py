"""EMA distance feature calculator — EMA20 and EMA50 from hourly bars.

Returns distance from current price to each EMA as a percentage of range,
which the V3 scorer uses for factor scoring:
  EMA50 < 20% of range → -10 pts (battle zone, 20% WR)
  EMA20 < 15% of range → -7 pts (too close, 47% WR)
"""

from __future__ import annotations

import logging
from datetime import datetime

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.ema")


class EMACalculator:
    """Computes EMA20 and EMA50 from hourly bars with range-relative distances.

    Implements FeatureModule protocol.
    """

    name: str = "ema"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.short_period = config.get("short_period", 20)
        self.long_period = config.get("long_period", 50)

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        hourly_bars: pd.DataFrame | None = snapshot.candles.get("1H")

        if hourly_bars is None or len(hourly_bars) < self.long_period:
            log.warning(f"{symbol}: Insufficient hourly bars for EMA calculation")
            return FeatureResult(
                name=self.name,
                values={
                    "ema20": 0.0, "ema50": 0.0,
                    "ema20_dist_pct": 0.0, "ema50_dist_pct": 0.0,
                },
                computed_at=datetime.now(),
            )

        closes = hourly_bars["close"].astype(float)
        ema20 = float(closes.ewm(span=self.short_period, adjust=False).mean().iloc[-1])
        ema50 = float(closes.ewm(span=self.long_period, adjust=False).mean().iloc[-1])

        current_price = snapshot.mid
        box_range = state.get("box_range", 0.0)

        if box_range > 0:
            ema20_dist_pct = abs(current_price - ema20) / box_range * 100
            ema50_dist_pct = abs(current_price - ema50) / box_range * 100
        else:
            ema20_dist_pct = abs(current_price - ema20) / current_price * 100 if current_price > 0 else 0.0
            ema50_dist_pct = abs(current_price - ema50) / current_price * 100 if current_price > 0 else 0.0

        return FeatureResult(
            name=self.name,
            values={
                "ema20": ema20,
                "ema50": ema50,
                "ema20_dist_pct": round(ema20_dist_pct, 2),
                "ema50_dist_pct": round(ema50_dist_pct, 2),
            },
            computed_at=datetime.now(),
        )
