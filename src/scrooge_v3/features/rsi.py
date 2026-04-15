"""RSI feature calculator — standard RSI(14) from hourly bars.

Reuses the proven RSI computation from telemetry/quality_indicators.py.
V3 scorer uses this: RSI 45-55 = HARD BLOCK (29-50% WR),
RSI < 30 = +7 pts (oversold reversal edge).
"""

from __future__ import annotations

import logging
from datetime import datetime

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.rsi")


class RSICalculator:
    """Computes RSI from hourly close prices.

    Implements FeatureModule protocol.
    """

    name: str = "rsi"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.period = config.get("period", 14)

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        hourly_bars: pd.DataFrame | None = snapshot.candles.get("1H")

        if hourly_bars is None or len(hourly_bars) < self.period + 1:
            log.warning(f"{symbol}: Insufficient hourly bars for RSI calculation")
            return FeatureResult(
                name=self.name,
                values={"rsi": 50.0},
                computed_at=datetime.now(),
            )

        closes = hourly_bars["close"].astype(float)
        delta = closes.diff().dropna()
        gains = delta.clip(lower=0)
        losses = -delta.clip(upper=0)

        avg_gain = float(gains.ewm(alpha=1 / self.period, adjust=False).mean().iloc[-1])
        avg_loss = float(losses.ewm(alpha=1 / self.period, adjust=False).mean().iloc[-1])

        if avg_loss == 0:
            rsi = 100.0
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        return FeatureResult(
            name=self.name,
            values={"rsi": round(rsi, 2)},
            computed_at=datetime.now(),
        )
