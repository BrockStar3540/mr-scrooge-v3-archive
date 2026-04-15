"""ATR feature calculator — standard True Range with EWM smoothing."""

from __future__ import annotations

import logging
from datetime import datetime

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.atr")


class ATRCalculator:
    """
    Computes Average True Range from daily candles.

    Config:
        period: EWM span for smoothing (default 14)

    Returns FeatureResult with values:
        atr       — raw ATR value
        atr_60pct — 60% of ATR (directional pressure threshold)
        atr_80pct — 80% of ATR (strong reversal threshold)
        atr_20pct — 20% of ATR (minimum threshold)
    """

    name: str = "atr"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.period = config.get("period", 14)

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        daily_bars: pd.DataFrame | None = snapshot.candles.get("D")

        if daily_bars is None or len(daily_bars) < self.period + 1:
            log.warning(f"{symbol}: Insufficient daily bars for ATR calculation")
            return FeatureResult(
                name=self.name,
                values={"atr": 0.0, "atr_60pct": 0.0, "atr_80pct": 0.0, "atr_20pct": 0.0},
                computed_at=datetime.now(),
            )

        atr = self._calculate_atr(daily_bars, self.period)

        # ADR consumed: today's range / ATR (how much of daily range is used)
        today = daily_bars.iloc[-1]
        today_range = float(today["high"]) - float(today["low"])
        adr_consumed = today_range / atr if atr > 0 else 0.0

        return FeatureResult(
            name=self.name,
            values={
                "atr": atr,
                "atr_60pct": atr * 0.60,
                "atr_80pct": atr * 0.80,
                "atr_20pct": atr * 0.20,
                "adr_consumed": round(adr_consumed, 4),
            },
            computed_at=datetime.now(),
        )

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    @staticmethod
    def _calculate_atr(bars: pd.DataFrame, period: int) -> float:
        """Standard ATR calculation using True Range with EWM smoothing."""
        highs = bars["high"].values
        lows = bars["low"].values
        closes = bars["close"].values

        tr_list = []
        for i in range(1, len(bars)):
            tr = max(
                highs[i] - lows[i],
                abs(highs[i] - closes[i - 1]),
                abs(lows[i] - closes[i - 1]),
            )
            tr_list.append(tr)

        tr_series = pd.Series(tr_list)
        atr = tr_series.ewm(span=period, adjust=False).mean().iloc[-1]
        return float(atr)
