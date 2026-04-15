"""Bollinger Bands feature calculator — dual-band computation.

Computes two Bollinger Band sets from 5m bar data:
  Band A: 20-period SMA +/- 2 std on close  (normal price range)
  Band B:  4-period SMA +/- 4 std on open   (extreme outliers / breakouts)

This module only COMPUTES the bands. Classification (BBState enum)
is handled by classifiers/bb_state.py.
"""

from __future__ import annotations

import logging
from datetime import datetime

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.bollinger")

_MIN_BARS_A = 20  # minimum bars to compute Band A
_MIN_BARS_B = 4   # minimum bars to compute Band B


class BollingerCalculator:
    """
    Computes dual Bollinger Bands from 5-minute candles.

    Config:
        band_a_period: SMA period for Band A (default 20)
        band_a_std:    Standard deviation multiplier for Band A (default 2)
        band_b_period: SMA period for Band B (default 4)
        band_b_std:    Standard deviation multiplier for Band B (default 4)
        timeframe:     Candle timeframe key in snapshot.candles (default "5m")

    Returns FeatureResult with values:
        upper_a       — Band A upper
        lower_a       — Band A lower
        sma_a         — Band A SMA
        upper_b       — Band B upper
        lower_b       — Band B lower
        sma_b         — Band B SMA
        current_close — latest close
        prior_close_1 — one candle back close
        prior_close_2 — two candles back close
    """

    name: str = "bollinger"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.band_a_period = config.get("band_a_period", 20)
        self.band_a_std = config.get("band_a_std", 2)
        self.band_b_period = config.get("band_b_period", 4)
        self.band_b_std = config.get("band_b_std", 4)
        self.timeframe = config.get("timeframe", "5m")

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        bars: pd.DataFrame | None = snapshot.candles.get(self.timeframe)

        if bars is None or len(bars) < _MIN_BARS_A:
            log.warning(f"{symbol}: Insufficient {self.timeframe} bars for Bollinger calculation")
            return FeatureResult(name=self.name, values={}, computed_at=datetime.now())

        closes = bars["close"].astype(float)
        opens = bars["open"].astype(float)

        # Band A -- 20-period on close
        sma_a = float(closes.iloc[-self.band_a_period:].mean())
        std_a = float(closes.iloc[-self.band_a_period:].std(ddof=1))
        upper_a = sma_a + self.band_a_std * std_a
        lower_a = sma_a - self.band_a_std * std_a

        # Band B -- 4-period on open
        n_b = min(self.band_b_period, len(opens))
        sma_b = float(opens.iloc[-n_b:].mean())
        std_b = float(opens.iloc[-n_b:].std(ddof=1)) if n_b >= 2 else 0.0
        upper_b = sma_b + self.band_b_std * std_b
        lower_b = sma_b - self.band_b_std * std_b

        c = float(closes.iloc[-1])
        c1 = float(closes.iloc[-2]) if len(closes) >= 2 else c
        c2 = float(closes.iloc[-3]) if len(closes) >= 3 else c1

        # Z-score: how many std devs from Band A mean
        z_score = (c - sma_a) / std_a if std_a > 0 else 0.0

        # BB position: where price sits in 0-1 range (0=lower, 1=upper)
        band_width = upper_a - lower_a
        bb_position = (c - lower_a) / band_width if band_width > 0 else 0.5

        return FeatureResult(
            name=self.name,
            values={
                "upper_a": upper_a,
                "lower_a": lower_a,
                "sma_a": sma_a,
                "upper_b": upper_b,
                "lower_b": lower_b,
                "sma_b": sma_b,
                "current_close": c,
                "prior_close_1": c1,
                "prior_close_2": c2,
                "z_score": round(z_score, 4),
                "bb_position": round(bb_position, 4),
            },
            computed_at=datetime.now(),
        )
