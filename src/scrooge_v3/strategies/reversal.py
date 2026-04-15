"""Reversal strategy — enters at session range boundaries on exhaustion rejection.

Source theory: Sections 3 (sucker move), 4 (levels first), 11 (pitchfork entry),
12 (wick rejection candle quality).

Pattern:
  1. Price at session range boundary (high or low)
  2. BB state is EXTREME or REJECTION (exhaustion confirmed)
  3. Prior candle shows qualifying wick rejection
  4. Current candle confirms re-entry direction
  5. Price is inside the range (not a breakout)
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import (
    ClassificationResult,
    FeatureResult,
    SymbolContext,
    TradeCandidate,
    TradeDirection,
)

log = logging.getLogger("scrooge_v3.strategy.reversal")

# Wick must be >= body * this ratio to qualify as a rejection candle
WICK_RATIO = 1.5

# Fixed score for ranking against other candidates
REVERSAL_FIXED_SCORE = 35

# BB states that qualify for reversal entries
_REVERSAL_BB_STATES = (
    "EXTREME_UP", "EXTREME_DOWN",
    "REJECTION_SHORT", "REJECTION_LONG",
)


class ReversalStrategy:
    """Reversal entries at session range boundaries on exhaustion rejection.

    Implements StrategyModule Protocol.
    """

    name = "reversal"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.zone_proximity_pct = config.get("zone_proximity_pct", 0.0025)
        self.min_risk_reward = config.get("min_risk_reward", 1.60)

    def eligible(self, ctx: SymbolContext) -> bool:
        """Reversal is eligible when BB state indicates exhaustion or rejection."""
        bb = ctx.classifications.get("bb_state")
        if bb is None:
            return False
        return bb.label in _REVERSAL_BB_STATES

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        """Evaluate reversal entry conditions.

        Requires:
          ctx.features["zone_detector"] — zone map with session range
          ctx.features["bollinger"] — BB band values
          ctx.classifications["bb_state"] — current BB classification
          ctx.snapshot — current market data
        """
        bb = ctx.classifications.get("bb_state")
        if bb is None:
            return None

        zone_feature = ctx.features.get("zone_detector")
        if zone_feature is None:
            return None
        zone_map = zone_feature.values.get("zone_map")
        if zone_map is None:
            return None

        session_range = zone_map.get("session_range") or zone_map.get("daily_box")
        if session_range is None:
            return None

        bars_5m = ctx.snapshot.candles.get("5M")
        if bars_5m is None or len(bars_5m) < 4:
            return None

        # Regime check — block if regime score too low
        regime = ctx.classifications.get("regime")
        if regime and regime.metadata.get("score", 0) <= -3:
            return None

        # Determine direction from BB state
        if bb.label in ("REJECTION_LONG", "EXTREME_DOWN"):
            direction = TradeDirection.LONG
        else:
            direction = TradeDirection.SHORT

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        current_price = ctx.snapshot.mid

        # Get session range boundaries
        pdh = _get(session_range, "PDH", "high")
        pdl = _get(session_range, "PDL", "low")
        center = _get(session_range, "center", "center")

        # Price must be inside the range
        if current_price > pdh or current_price < pdl:
            return None

        # Proximity check
        box_range = max(pdh - pdl, pip)
        proximity = box_range * self.zone_proximity_pct

        # Candle analysis — current = confirmation, previous = rejection
        curr = bars_5m.iloc[-1]
        prev = bars_5m.iloc[-2]

        c_close = float(curr["close"])
        p_open = float(prev["open"])
        p_high = float(prev["high"])
        p_low = float(prev["low"])
        p_close = float(prev["close"])

        body = max(abs(p_close - p_open), pip * 0.5)

        if direction == TradeDirection.LONG:
            if c_close > pdl + proximity:
                return None
            lower_wick = min(p_open, p_close) - p_low
            upper_wick = p_high - max(p_open, p_close)
            if lower_wick < body * WICK_RATIO or lower_wick <= upper_wick:
                return None
            if c_close <= p_high:
                return None
            entry = c_close
            sl = p_low - 2 * pip
            tp1 = center
            tp2 = pdh
        else:
            if c_close < pdh - proximity:
                return None
            upper_wick = p_high - max(p_open, p_close)
            lower_wick = min(p_open, p_close) - p_low
            if upper_wick < body * WICK_RATIO or upper_wick <= lower_wick:
                return None
            if c_close >= p_low:
                return None
            entry = c_close
            sl = p_high + 2 * pip
            tp1 = center
            tp2 = pdl

        # TP sanity
        if direction == TradeDirection.LONG and (tp2 <= entry or tp1 <= entry):
            return None
        if direction == TradeDirection.SHORT and (tp2 >= entry or tp1 >= entry):
            return None

        buf = pip * 2
        if direction == TradeDirection.LONG and tp2 <= current_price + buf:
            return None
        if direction == TradeDirection.SHORT and tp2 >= current_price - buf:
            return None

        # RR check
        risk = abs(entry - sl)
        reward = abs(tp2 - entry)
        if risk <= 0:
            return None
        rr = reward / risk
        if rr < self.min_risk_reward:
            log.info(
                "[STRATEGY:reversal] SKIP symbol=%s direction=%s rr=%.2f < min=%.1f",
                ctx.symbol, direction.value, rr, self.min_risk_reward,
            )
            return None

        log.info(
            "[STRATEGY:reversal] CANDIDATE symbol=%s direction=%s bb=%s "
            "entry=%.5f sl=%.5f tp2=%.5f rr=%.2f",
            ctx.symbol, direction.value, bb.label, entry, sl, tp2, rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=self.name,
            entry_price=entry,
            stop_price=sl,
            take_profit=tp2,
            size=0.0,  # sized later by execution layer
            risk_reward=rr,
            score=REVERSAL_FIXED_SCORE,
            metadata={
                "bb_state": bb.label,
                "tp1": tp1,
                "tp2": tp2,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )


def _get(obj: Any, *keys: str) -> Any:
    """Get attribute or dict key, trying multiple names."""
    for key in keys:
        if isinstance(obj, dict):
            if key in obj:
                return obj[key]
        elif hasattr(obj, key):
            return getattr(obj, key)
    return None
