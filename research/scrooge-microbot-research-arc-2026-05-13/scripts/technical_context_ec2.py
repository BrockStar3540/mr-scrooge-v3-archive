"""Technical context feature for raw-M5 survivor shadow detection.

Computes the exact higher-timeframe labels used by the raw-M5 winner
factory v2:

- M15 trend from M5-resampled close vs EMA20 with a +/-5 bps dead zone.
- H1 range regime from a rolling 48-hour percentile rank of hourly range.

This module is shadow telemetry only. It does not approve, reject, size, or
manage trades.
"""

from __future__ import annotations

import logging
from datetime import datetime

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.technical_context")


class TechnicalContextCalculator:
    """Computes live labels needed to shadow raw-M5 v2 survivor cells."""

    name: str = "technical_context"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.m15_ema_period = int(config.get("m15_ema_period", 20))
        self.m15_deadzone_bps = float(config.get("m15_deadzone_bps", 5.0))
        self.h1_rank_window = int(config.get("h1_rank_window", 48))
        self.h1_breakout_rank = float(config.get("h1_breakout_rank", 0.75))
        self.h1_consolidation_rank = float(config.get("h1_consolidation_rank", 0.25))

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        m5: pd.DataFrame | None = snapshot.candles.get("5M")
        h1: pd.DataFrame | None = snapshot.candles.get("1H")

        values = {
            "m15_trend": "unknown",
            "m15_trend_id": 0,
            "m15_ema20": 0.0,
            "m15_close": 0.0,
            "h1_regime": "unknown",
            "h1_regime_id": 0,
            "h1_range_rank_48": 0.0,
            "raw_m5_structural_gate_long": False,
            "raw_m5_structural_gate_short": False,
        }

        try:
            m15_trend, m15_close, m15_ema20 = self._m15_trend(m5)
            h1_regime, h1_rank = self._h1_regime(h1)
        except Exception:
            log.exception("%s: technical_context calculation failed", symbol)
            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

        values["m15_trend"] = m15_trend
        values["m15_trend_id"] = {"down": -1, "unknown": 0, "flat": 0, "up": 1}.get(m15_trend, 0)
        values["m15_ema20"] = round(float(m15_ema20), 8)
        values["m15_close"] = round(float(m15_close), 8)
        values["h1_regime"] = h1_regime
        values["h1_regime_id"] = {"unknown": 0, "consolidation": 1, "in_range": 2, "breakout": 3}.get(h1_regime, 0)
        values["h1_range_rank_48"] = round(float(h1_rank), 4)
        values["raw_m5_structural_gate_long"] = bool(h1_regime == "breakout" and m15_trend == "up")
        values["raw_m5_structural_gate_short"] = bool(h1_regime == "breakout" and m15_trend == "down")

        return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

    def _m15_trend(self, m5: pd.DataFrame | None) -> tuple[str, float, float]:
        if m5 is None or len(m5) < self.m15_ema_period * 3:
            return "unknown", 0.0, 0.0

        bars = m5[["open", "high", "low", "close"]].copy()
        if not isinstance(bars.index, pd.DatetimeIndex):
            if "time" not in bars.columns:
                return "unknown", 0.0, 0.0
            bars.index = pd.to_datetime(bars["time"], utc=True)

        m15 = bars.resample("15min").agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last",
        }).dropna()
        if len(m15) < self.m15_ema_period:
            return "unknown", 0.0, 0.0

        closes = m15["close"].astype(float)
        ema20 = closes.ewm(span=self.m15_ema_period, adjust=False).mean()
        close = float(closes.iloc[-1])
        ema = float(ema20.iloc[-1])
        band = self.m15_deadzone_bps / 10000.0

        if ema <= 0:
            return "unknown", close, ema
        if close > ema * (1.0 + band):
            return "up", close, ema
        if close < ema * (1.0 - band):
            return "down", close, ema
        return "flat", close, ema

    def _h1_regime(self, h1: pd.DataFrame | None) -> tuple[str, float]:
        if h1 is None or len(h1) < self.h1_rank_window:
            return "unknown", 0.0

        highs = h1["high"].astype(float)
        lows = h1["low"].astype(float)
        ranges = highs - lows
        ranks = ranges.rolling(self.h1_rank_window).rank(pct=True)
        rank = float(ranks.iloc[-1]) if pd.notna(ranks.iloc[-1]) else 0.0

        if rank < self.h1_consolidation_rank:
            return "consolidation", rank
        if rank > self.h1_breakout_rank:
            return "breakout", rank
        return "in_range", rank
