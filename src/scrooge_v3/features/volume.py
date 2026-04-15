"""Volume ratio feature calculator.

Computes current volume relative to recent average.
V3 scorer uses this: calm (0.9-1.1) = 82% WR (+9 pts),
volatile (>1.3) = 43% WR (-3 pts).
"""

from __future__ import annotations

import logging
from datetime import datetime

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.volume")


class VolumeCalculator:
    """Computes volume ratio (current / average) from hourly bars.

    Implements FeatureModule protocol.
    """

    name: str = "volume"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.avg_period = config.get("avg_period", 20)

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        hourly_bars: pd.DataFrame | None = snapshot.candles.get("1H")

        if hourly_bars is None or "volume" not in hourly_bars.columns or len(hourly_bars) < self.avg_period + 1:
            log.debug(f"{symbol}: Insufficient data for volume ratio")
            return FeatureResult(
                name=self.name,
                values={"volume_ratio": 1.0, "avg_volume": 0.0, "current_volume": 0.0},
                computed_at=datetime.now(),
            )

        volumes = hourly_bars["volume"].astype(float)
        current_vol = float(volumes.iloc[-1])
        avg_vol = float(volumes.iloc[-(self.avg_period + 1):-1].mean())

        ratio = current_vol / avg_vol if avg_vol > 0 else 1.0

        return FeatureResult(
            name=self.name,
            values={
                "volume_ratio": round(ratio, 4),
                "avg_volume": round(avg_vol, 2),
                "current_volume": round(current_vol, 2),
            },
            computed_at=datetime.now(),
        )
