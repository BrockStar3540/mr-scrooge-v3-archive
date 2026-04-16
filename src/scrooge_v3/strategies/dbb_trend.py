"""DBB Trend Engine — breakout/pullback continuation strategy.

Uses Double Bollinger Band framework to identify genuine breakouts
and trade pullback continuations. Two entry modes:

  Mode A (BREAKOUT): Fresh directional expansion through Band A + prior
    structural high/low. Requires strong body, close beyond structure.

  Mode B (PULLBACK): Valid retest after confirmed breakout. Pullback
    holds above reclaimed zone, continuation candle confirms.

Follows Platform Doctrine:
  - Only activates with router permission (TREND/BREAKOUT states)
  - Tags management_profile="trend_runner" for shared PositionPipeline
  - No private exit logic

See docs/DOUBLE_BB_STRATEGY.md for the full rulebook.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import (
    SymbolContext,
    TradeCandidate,
    TradeDirection,
)

log = logging.getLogger("scrooge_v3.strategy.dbb_trend")

_BULLISH_STATES = ("TREND_UP", "BREAKOUT_UP")
_BEARISH_STATES = ("TREND_DOWN", "BREAKOUT_DOWN")
_ALL_TREND = _BULLISH_STATES + _BEARISH_STATES + ("STRETCH_DOWN",)


class DBBTrendStrategy:
    """Double BB breakout/pullback continuation engine.

    Implements StrategyModule Protocol.
    """

    name = "dbb_trend"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.lookback_bars = config.get("lookback_bars", 12)
        self.pullback_max_retrace_pct = config.get("pullback_max_retrace_pct", 0.55)
        self.min_breakout_body_pct = config.get("min_breakout_body_pct", 0.55)
        self.min_rr = config.get("min_rr", 1.1)
        self.stop_buffer_pips = config.get("stop_buffer_pips", 2)
        self.fixed_score = config.get("fixed_score", 32)
        self.structure_lookback = config.get("structure_lookback", 10)

    # ------------------------------------------------------------------
    # Protocol
    # ------------------------------------------------------------------

    def eligible(self, ctx: SymbolContext) -> bool:
        """Allow only in trend/breakout BB states, regime not BLOCKED."""
        if not self.enabled:
            return False

        bb = ctx.classifications.get("bb_state")
        if bb is None:
            return False
        if bb.label not in _ALL_TREND:
            return False

        reg = ctx.classifications.get("regime")
        if reg and reg.label == "BLOCKED":
            return False

        boll = ctx.features.get("bollinger")
        if boll is None:
            return False

        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < 25:
            return False

        return True

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        """Evaluate for breakout or pullback continuation entry."""
        bb = ctx.classifications.get("bb_state")
        boll = ctx.features.get("bollinger")
        bars = ctx.snapshot.candles.get("5M")

        if bb is None or boll is None or bars is None or len(bars) < 25:
            return None

        bb_state = bb.label
        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        buffer = self.stop_buffer_pips * pip

        # Extract band values
        v = boll.values
        upper_a = v.get("upper_a", 0.0)
        lower_a = v.get("lower_a", 0.0)
        sma20 = v.get("sma_a", 0.0)

        closes = bars["close"].astype(float).values
        opens = bars["open"].astype(float).values
        highs = bars["high"].astype(float).values
        lows = bars["low"].astype(float).values

        # Determine direction from BB state
        if bb_state in _BULLISH_STATES:
            direction = TradeDirection.LONG
        elif bb_state in _BEARISH_STATES or bb_state == "STRETCH_DOWN":
            direction = TradeDirection.SHORT
        else:
            return None

        # Try pullback first (more common, better R:R), then breakout
        candidate = self._try_pullback(
            ctx, direction, closes, opens, highs, lows,
            upper_a, lower_a, sma20, bb_state, pip, buffer,
        )
        if candidate:
            return candidate

        candidate = self._try_breakout(
            ctx, direction, closes, opens, highs, lows,
            upper_a, lower_a, sma20, bb_state, pip, buffer,
        )
        return candidate

    # ------------------------------------------------------------------
    # Mode A: Breakout Confirmation Entry
    # ------------------------------------------------------------------

    def _try_breakout(
        self,
        ctx: SymbolContext,
        direction: TradeDirection,
        closes, opens, highs, lows,
        upper_a: float, lower_a: float, sma20: float,
        bb_state: str, pip: float, buffer: float,
    ) -> TradeCandidate | None:
        """Fresh breakout: band break + structure break + close confirmation."""

        current_close = closes[-1]
        current_high = highs[-1]
        current_low = lows[-1]
        current_open = opens[-1]
        candle_range = current_high - current_low

        if candle_range <= 0:
            return None

        # Body quality check
        body = abs(current_close - current_open)
        body_pct = body / candle_range
        if body_pct < self.min_breakout_body_pct:
            return None

        # Structure: prior swing high/low over lookback
        lb = self.structure_lookback
        if direction == TradeDirection.LONG:
            # Must close above Band A upper AND prior structural high
            prior_high = float(highs[-lb - 1:-1].max())
            if current_close <= upper_a or current_close <= prior_high:
                return None
            # Close must be bullish
            if current_close <= current_open:
                return None

            stop_price = current_low - buffer
            breakout_level = prior_high
            # TP1: measured move (breakout distance from structure projected up)
            impulse = current_close - prior_high
            tp1 = current_close + impulse
            # TP2: session boundary
            tp2 = self._session_target(ctx, direction, current_close, impulse * 2)

        else:  # SHORT
            prior_low = float(lows[-lb - 1:-1].min())
            if current_close >= lower_a or current_close >= prior_low:
                return None
            if current_close >= current_open:
                return None

            stop_price = current_high + buffer
            breakout_level = prior_low
            impulse = prior_low - current_close
            tp1 = current_close - impulse
            tp2 = self._session_target(ctx, direction, current_close, impulse * 2)

        risk = abs(current_close - stop_price)
        reward = abs(tp2 - current_close) if tp2 else abs(tp1 - current_close)
        if risk <= 0:
            return None
        rr = reward / risk
        if rr < self.min_rr:
            return None

        log.info(
            "[STRATEGY:dbb_trend] BREAKOUT symbol=%s dir=%s bb=%s "
            "close=%.5f structure=%.5f body=%.0f%% rr=%.2f",
            ctx.symbol, direction.value, bb_state,
            current_close, breakout_level, body_pct * 100, rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=self.name,
            entry_price=current_close,
            stop_price=stop_price,
            take_profit=tp2 or tp1,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "DBB_BREAKOUT",
                "strategy_family": "trend",
                "management_profile": "trend_runner",
                "bb_state": bb_state,
                "structure_break_confirmed": True,
                "breakout_level": breakout_level,
                "breakout_bar_idx": len(closes) - 1,
                "pullback_depth_pct": 0.0,
                "dbb_upper_a": upper_a,
                "dbb_lower_a": lower_a,
                "sma20": sma20,
                "tp1": tp1,
                "tp2": tp2,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )

    # ------------------------------------------------------------------
    # Mode B: Pullback Continuation Entry
    # ------------------------------------------------------------------

    def _try_pullback(
        self,
        ctx: SymbolContext,
        direction: TradeDirection,
        closes, opens, highs, lows,
        upper_a: float, lower_a: float, sma20: float,
        bb_state: str, pip: float, buffer: float,
    ) -> TradeCandidate | None:
        """Pullback after confirmed breakout: retest + continuation candle."""

        lb = self.lookback_bars
        sl = self.structure_lookback

        # Find the breakout bar in recent history
        breakout_idx = None
        breakout_level = 0.0

        if direction == TradeDirection.LONG:
            for i in range(-lb, -1):
                bar_close = closes[i]
                bar_open = opens[i]
                bar_high = highs[i]
                bar_low = lows[i]
                bar_range = bar_high - bar_low
                if bar_range <= 0:
                    continue
                body_pct = abs(bar_close - bar_open) / bar_range

                # Structure high before this bar
                start = max(0, len(closes) + i - sl)
                end = len(closes) + i
                if start >= end:
                    continue
                prior_high = float(highs[start:end].max())

                # Breakout: close above Band A upper AND prior high, strong body
                if (bar_close > upper_a and bar_close > prior_high
                        and bar_close > bar_open
                        and body_pct >= self.min_breakout_body_pct):
                    # Check not immediately negated
                    next_idx = i + 1
                    if next_idx < 0 and closes[next_idx] < prior_high:
                        continue  # Negated — breakout failed
                    breakout_idx = len(closes) + i
                    breakout_level = prior_high
                    break
        else:  # SHORT
            for i in range(-lb, -1):
                bar_close = closes[i]
                bar_open = opens[i]
                bar_high = highs[i]
                bar_low = lows[i]
                bar_range = bar_high - bar_low
                if bar_range <= 0:
                    continue
                body_pct = abs(bar_close - bar_open) / bar_range

                start = max(0, len(closes) + i - sl)
                end = len(closes) + i
                if start >= end:
                    continue
                prior_low = float(lows[start:end].min())

                if (bar_close < lower_a and bar_close < prior_low
                        and bar_close < bar_open
                        and body_pct >= self.min_breakout_body_pct):
                    next_idx = i + 1
                    if next_idx < 0 and closes[next_idx] > prior_low:
                        continue
                    breakout_idx = len(closes) + i
                    breakout_level = prior_low
                    break

        if breakout_idx is None:
            return None

        # Measure pullback depth
        current_close = closes[-1]
        current_open = opens[-1]

        if direction == TradeDirection.LONG:
            breakout_peak = float(highs[breakout_idx:].max())
            pullback_low = float(lows[breakout_idx:].min())
            breakout_move = breakout_peak - breakout_level
            if breakout_move <= 0:
                return None
            retrace = (breakout_peak - pullback_low) / breakout_move
            if retrace > self.pullback_max_retrace_pct:
                return None

            # Continuation confirmation: current candle bullish
            if current_close <= current_open:
                return None

            # Price should be near support zone (breakout level, SMA20, or inner band)
            support_zone = max(breakout_level, sma20)
            if current_close < support_zone - (breakout_move * 0.1):
                return None  # Too far below support

            # Stop below pullback swing low
            pullback_swing_low = float(lows[-min(lb, len(lows)):].min())
            stop_price = pullback_swing_low - buffer

            # Targets
            tp1 = breakout_peak  # Retest the breakout peak
            impulse = breakout_peak - breakout_level
            tp2 = self._session_target(ctx, direction, current_close, impulse)

        else:  # SHORT
            breakout_trough = float(lows[breakout_idx:].min())
            pullback_high = float(highs[breakout_idx:].max())
            breakout_move = breakout_level - breakout_trough
            if breakout_move <= 0:
                return None
            retrace = (pullback_high - breakout_trough) / breakout_move
            if retrace > self.pullback_max_retrace_pct:
                return None

            if current_close >= current_open:
                return None

            resistance_zone = min(breakout_level, sma20)
            if current_close > resistance_zone + (breakout_move * 0.1):
                return None

            pullback_swing_high = float(highs[-min(lb, len(highs)):].max())
            stop_price = pullback_swing_high + buffer

            tp1 = breakout_trough
            impulse = breakout_level - breakout_trough
            tp2 = self._session_target(ctx, direction, current_close, impulse)

        risk = abs(current_close - stop_price)
        reward = abs(tp2 - current_close) if tp2 else abs(tp1 - current_close)
        if risk <= 0:
            return None
        rr = reward / risk
        if rr < self.min_rr:
            return None

        pullback_depth = retrace

        log.info(
            "[STRATEGY:dbb_trend] PULLBACK symbol=%s dir=%s bb=%s "
            "close=%.5f breakout_lvl=%.5f retrace=%.0f%% rr=%.2f",
            ctx.symbol, direction.value, bb_state,
            current_close, breakout_level, pullback_depth * 100, rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=self.name,
            entry_price=current_close,
            stop_price=stop_price,
            take_profit=tp2 or tp1,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "DBB_PULLBACK",
                "strategy_family": "trend",
                "management_profile": "trend_runner",
                "bb_state": bb_state,
                "structure_break_confirmed": True,
                "breakout_bar_idx": breakout_idx,
                "breakout_level": breakout_level,
                "pullback_depth_pct": round(pullback_depth, 3),
                "dbb_upper_a": upper_a,
                "dbb_lower_a": lower_a,
                "sma20": sma20,
                "tp1": tp1,
                "tp2": tp2,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _session_target(
        self,
        ctx: SymbolContext,
        direction: TradeDirection,
        entry: float,
        fallback_distance: float,
    ) -> float:
        """Get session boundary as TP2, or use fallback measured move."""
        zone_feature = ctx.features.get("zone_detector")
        if zone_feature:
            zm = zone_feature.values.get("zone_map")
            if zm:
                sr = getattr(zm, "session_range", None) or (zm.get("session_range") if isinstance(zm, dict) else None)
                if sr:
                    pdh = getattr(sr, "PDH", None) or (sr.get("PDH") if isinstance(sr, dict) else None)
                    pdl = getattr(sr, "PDL", None) or (sr.get("PDL") if isinstance(sr, dict) else None)
                    if direction == TradeDirection.LONG and pdh and pdh > entry:
                        return pdh
                    elif direction == TradeDirection.SHORT and pdl and pdl < entry:
                        return pdl

        # Fallback: measured move projection
        if direction == TradeDirection.LONG:
            return entry + fallback_distance
        else:
            return entry - fallback_distance
