"""Trend participation strategy — BB20 pullback entries.

Fires when BB state = TREND or STRETCH. Enters with the trend on
pullbacks to the BB20 midline (SMA20). Intentionally simple — no
entry confirmation gate, no directional pressure, no complex scoring.

Regime mapping:
  EXTREME → reversal strategy
  TREND   → this strategy (full size)
  STRETCH → this strategy (reduced size, 2-candle confirmation)
  RANGE   → idle
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from scrooge_v3.core.types import (
    SymbolContext,
    TradeCandidate,
    TradeDirection,
)

log = logging.getLogger("scrooge_v3.strategy.trend")

_TREND_STATES = ("TREND_UP", "TREND_DOWN")
_STRETCH_STATES = ("STRETCH_UP", "STRETCH_DOWN")
_ALL_TREND = _TREND_STATES + _STRETCH_STATES

TREND_FIXED_SCORE = 30


class TrendStrategy:
    """BB20 pullback entries with the trend.

    Implements StrategyModule Protocol.
    """

    name = "trend"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.sma_proximity_pct = config.get("sma_proximity_pct", 0.0015)
        self.atr_stop_multiple = config.get("atr_stop_multiple", 1.0)
        self.fixed_score = config.get("fixed_score", TREND_FIXED_SCORE)

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        bb = ctx.classifications.get("bb_state")
        if bb is None:
            return False
        return bb.label in _ALL_TREND

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        """Evaluate trend pullback entry.

        Requires:
          ctx.features["zone_detector"] — zone map with session range
          ctx.features["bollinger"] — BB band values
          ctx.classifications["bb_state"] — current BB classification
          ctx.snapshot — current market data with 5M candles
        """
        bb = ctx.classifications.get("bb_state")
        if bb is None:
            return None

        bb_state = bb.label
        if bb_state not in _ALL_TREND:
            return None

        bars_5m = ctx.snapshot.candles.get("5M")
        if bars_5m is None or len(bars_5m) < 22:
            return None

        # Compute SMA20
        closes = bars_5m["close"].astype(float)
        sma20 = float(closes.iloc[-20:].mean())
        current_close = float(closes.iloc[-1])
        current_open = float(bars_5m["open"].astype(float).iloc[-1])

        # Direction from BB state
        if bb_state in ("TREND_UP", "STRETCH_UP"):
            direction = TradeDirection.LONG
        else:
            direction = TradeDirection.SHORT

        # Proximity check: price near SMA20
        atr_5m = float((bars_5m["high"] - bars_5m["low"]).iloc[-14:].mean())
        proximity_pct = abs(current_close - sma20) / sma20 if sma20 > 0 else 1.0
        proximity_atr = abs(current_close - sma20) / atr_5m if atr_5m > 0 else 1.0

        max_pct = self.sma_proximity_pct
        max_atr = 0.3

        if proximity_pct > max_pct and proximity_atr > max_atr:
            return None

        # Bounce confirmation
        if direction == TradeDirection.LONG:
            if current_close <= current_open:
                return None
            if current_close > sma20 * (1 + max_pct * 2):
                return None
        else:
            if current_close >= current_open:
                return None
            if current_close < sma20 * (1 - max_pct * 2):
                return None

        # STRETCH requires 2-candle confirmation
        if bb_state in _STRETCH_STATES:
            prev_close = float(closes.iloc[-2])
            prev_open = float(bars_5m["open"].astype(float).iloc[-2])
            if direction == TradeDirection.LONG:
                if prev_close > sma20 * (1 + max_pct * 3):
                    return None
                if prev_close > prev_open and abs(prev_close - sma20) / sma20 > max_pct * 2:
                    return None
            else:
                if prev_close < sma20 * (1 - max_pct * 3):
                    return None
                if prev_close < prev_open and abs(prev_close - sma20) / sma20 > max_pct * 2:
                    return None

        # Spread check
        zone_feature = ctx.features.get("zone_detector")
        session_range = None
        if zone_feature:
            zm = zone_feature.values.get("zone_map")
            if zm:
                session_range = zm.get("session_range") or zm.get("daily_box")

        range_half = 0.0
        if session_range:
            range_half = _get(session_range, "range_half", "half_box", default=0.0)

        if range_half > 0 and ctx.snapshot.spread > 0:
            spread_ratio = ctx.snapshot.spread / range_half
            if spread_ratio > 0.30:
                return None

        # Calculate SL and TP
        sl_distance = atr_5m * self.atr_stop_multiple

        bb_values = ctx.features.get("bollinger", None)
        upper_a = bb.metadata.get("upper_A", current_close + sl_distance * 2) if bb else current_close + sl_distance * 2
        lower_a = bb.metadata.get("lower_A", current_close - sl_distance * 2) if bb else current_close - sl_distance * 2

        if direction == TradeDirection.LONG:
            stop_price = current_close - sl_distance
            tp1 = upper_a
            tp2 = _get(session_range, "PDH", "high", default=current_close + sl_distance * 2) if session_range else current_close + sl_distance * 2
        else:
            stop_price = current_close + sl_distance
            tp1 = lower_a
            tp2 = _get(session_range, "PDL", "low", default=current_close - sl_distance * 2) if session_range else current_close - sl_distance * 2

        risk = abs(current_close - stop_price)
        reward = abs(tp2 - current_close)
        rr = reward / risk if risk > 0 else 0.0

        entry_type = "TREND_FULL" if bb_state in _TREND_STATES else "TREND_STRETCH"

        log.info(
            "[STRATEGY:trend] CANDIDATE symbol=%s type=%s direction=%s "
            "bb=%s sma20=%.5f price=%.5f sl=%.5f tp2=%.5f rr=%.2f",
            ctx.symbol, entry_type, direction.value,
            bb_state, sma20, current_close, stop_price, tp2, rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=self.name,
            entry_price=current_close,
            stop_price=stop_price,
            take_profit=tp2,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": entry_type,
                "bb_state": bb_state,
                "sma20": sma20,
                "tp1": tp1,
                "tp2": tp2,
                "proximity_pct": proximity_pct,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )


def _get(obj, *keys, default=None):
    """Get attribute or dict key, trying multiple names."""
    for key in keys:
        if isinstance(obj, dict) and key in obj:
            return obj[key]
        elif hasattr(obj, key):
            return getattr(obj, key)
    return default
