"""Intraday Trend Pullback — HTF-aligned LTF pullback continuation.

Strategy logic
--------------
1. HTF Bias (Daily): sign of (daily_close_now - daily_close_20_bars_ago).
   - Positive -> uptrend -> LONG-only
   - Negative -> downtrend -> SHORT-only
   - Near-zero (below `bias_min_pips` threshold) -> no trade
2. Pullback retest (M5/H1): during the trend, wait for M5 price to retrace
   to whichever of the following references is closest to the current close
   (within `retest_tolerance_pips`):
     - EMA20 on H1 (from `ctx.features['ema'].values`)
     - Prior swing low (long) / prior swing high (short) within the last
       30 M5 bars (excluding the current bar)
   A "VWAP-like" anchor falls back to M5 EMA20 if needed.
3. Entry trigger: on the retest bar, require a rejection candle in the trend
   direction:
     - LONG: lower-wick fraction of total range > 50% AND close > open
     - SHORT: upper-wick fraction of total range > 50% AND close < open
4. Stop: just beyond the retest level (`sl_buffer_pips` past the retest
   reference; below for long, above for short).
5. Take profit: project to recent swing high (long) or low (short) over the
   last `swing_lookback` M5 bars, with a `min_tp_pips` floor (default 12).
6. HTF alignment is hard — never counter-trend.

Emits TradeCandidate with:
  strategy = 'ITP_pullback_long' or 'ITP_pullback_short'
  family   = 'trend_pullback'

Required metadata fields (per spec):
  projected_tp_pips, strategy_family, htf_bias, retest_level, retest_type.

Research-grade module — class-based, registers via name string.
Gracefully returns None on any missing/malformed feature, never crashes.
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategy.intraday_trend_pullback")


def _pip_size(symbol: str) -> float:
    return 0.01 if "JPY" in symbol else 0.0001


def _safe_float(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    # NaN check
    if v != v:
        return None
    return v


def _ema(series, span: int):
    """Plain EMA over a numeric iterable; returns last value or None."""
    try:
        import pandas as pd
        s = pd.Series([float(x) for x in series])
        if len(s) < span:
            return None
        return float(s.ewm(span=span, adjust=False).mean().iloc[-1])
    except Exception:
        return None


class IntradayTrendPullbackStrategy:
    """HTF-aligned intraday pullback continuation.

    Implements the V3 StrategyModule Protocol (eligible/evaluate).
    """

    name = "intraday_trend_pullback"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)

        # HTF bias controls
        self.bias_lookback_d = int(config.get("bias_lookback_d", 20))
        self.bias_min_pips = float(config.get("bias_min_pips", 30.0))

        # Pullback / retest tolerances
        self.retest_tolerance_pips = float(config.get("retest_tolerance_pips", 8.0))
        self.swing_lookback = int(config.get("swing_lookback", 30))

        # Stop + TP geometry
        self.sl_buffer_pips = float(config.get("sl_buffer_pips", 3.0))
        self.min_tp_pips = float(config.get("min_tp_pips", 12.0))
        self.min_rr = float(config.get("min_rr", 1.0))

        # Rejection-wick threshold
        self.wick_frac_min = float(config.get("wick_frac_min", 0.50))

        # Score
        self.fixed_score = float(config.get("fixed_score", 28.0))

        log.info(
            "[STRATEGY:intraday_trend_pullback] init enabled=%s "
            "bias_lookback=%d bias_min_pips=%.1f tol_pips=%.1f sl_buf=%.1f "
            "min_tp=%.1f min_rr=%.2f",
            self.enabled, self.bias_lookback_d, self.bias_min_pips,
            self.retest_tolerance_pips, self.sl_buffer_pips,
            self.min_tp_pips, self.min_rr,
        )

    # ------------------------------------------------------------------ #
    # Protocol                                                           #
    # ------------------------------------------------------------------ #

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        try:
            candles = ctx.snapshot.candles or {}
            m5 = candles.get("5M")
            daily = candles.get("D")
            if m5 is None or daily is None:
                return False
            if len(m5) < max(self.swing_lookback + 2, 25):
                return False
            if len(daily) < self.bias_lookback_d + 1:
                return False
            return True
        except Exception:
            return False

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        try:
            return self._evaluate_inner(ctx)
        except Exception as e:  # never crash the scan pipeline
            log.debug(
                "[STRATEGY:intraday_trend_pullback] evaluate exception symbol=%s err=%s",
                getattr(ctx, "symbol", "?"), e,
            )
            return None

    # ------------------------------------------------------------------ #
    # Core                                                               #
    # ------------------------------------------------------------------ #

    def _evaluate_inner(self, ctx: SymbolContext) -> TradeCandidate | None:
        candles = ctx.snapshot.candles or {}
        m5 = candles.get("5M")
        daily = candles.get("D")
        h1 = candles.get("1H")
        if m5 is None or daily is None:
            return None

        symbol = ctx.symbol
        pip = _pip_size(symbol)

        # --- HTF bias from daily closes ---------------------------------
        try:
            d_closes = daily["close"].astype(float).values
        except Exception:
            return None
        if len(d_closes) < self.bias_lookback_d + 1:
            return None
        d_now = _safe_float(d_closes[-1])
        d_then = _safe_float(d_closes[-1 - self.bias_lookback_d])
        if d_now is None or d_then is None:
            return None
        bias_delta_pips = (d_now - d_then) / pip
        if abs(bias_delta_pips) < self.bias_min_pips:
            return None  # flat -> no trade
        htf_bias = "long" if bias_delta_pips > 0 else "short"
        direction = TradeDirection.LONG if htf_bias == "long" else TradeDirection.SHORT

        # --- M5 candle vectors ------------------------------------------
        try:
            m5_close = m5["close"].astype(float).values
            m5_open = m5["open"].astype(float).values
            m5_high = m5["high"].astype(float).values
            m5_low = m5["low"].astype(float).values
        except Exception:
            return None
        if len(m5_close) < self.swing_lookback + 2:
            return None

        cur_close = _safe_float(m5_close[-1])
        cur_open = _safe_float(m5_open[-1])
        cur_high = _safe_float(m5_high[-1])
        cur_low = _safe_float(m5_low[-1])
        if None in (cur_close, cur_open, cur_high, cur_low):
            return None

        # --- Reference levels: H1 EMA20, swing levels, M5 EMA20 fallback -
        retest_candidates: list[tuple[str, float]] = []

        # 1) H1 EMA20 — prefer ctx.features['ema'].values['ema20'] if present
        ema20_h1 = None
        ema_feat = ctx.features.get("ema") if ctx.features else None
        if ema_feat is not None:
            vals = getattr(ema_feat, "values", None) or {}
            ema20_h1 = _safe_float(vals.get("ema20"))
        if ema20_h1 is None and h1 is not None:
            try:
                h1_closes = h1["close"].astype(float).values
                ema20_h1 = _ema(h1_closes, 20)
            except Exception:
                ema20_h1 = None
        if ema20_h1 is not None:
            retest_candidates.append(("ema20", float(ema20_h1)))

        # 2) Prior swing levels over the last `swing_lookback` M5 bars,
        # excluding the current (forming) bar.
        window_lo = m5_low[-(self.swing_lookback + 1):-1]
        window_hi = m5_high[-(self.swing_lookback + 1):-1]
        if len(window_lo) > 0 and len(window_hi) > 0:
            if direction == TradeDirection.LONG:
                swing_lvl = float(min(window_lo))
                retest_candidates.append(("swing", swing_lvl))
            else:
                swing_lvl = float(max(window_hi))
                retest_candidates.append(("swing", swing_lvl))

        # 3) Fallback: M5 EMA20 as VWAP-like anchor
        m5_ema20 = _ema(m5_close, 20)
        if m5_ema20 is not None:
            retest_candidates.append(("ema20", float(m5_ema20)))

        if not retest_candidates:
            return None

        # Pick closest retest level to current close
        retest_type, retest_level = min(
            retest_candidates, key=lambda kv: abs(cur_close - kv[1])
        )
        dist_pips = abs(cur_close - retest_level) / pip
        if dist_pips > self.retest_tolerance_pips:
            return None  # not at a retest level

        # --- Rejection-candle trigger -----------------------------------
        rng = cur_high - cur_low
        if rng <= 0:
            return None
        lower_wick = min(cur_open, cur_close) - cur_low
        upper_wick = cur_high - max(cur_open, cur_close)

        if direction == TradeDirection.LONG:
            wick_ok = (lower_wick / rng) > self.wick_frac_min
            body_ok = cur_close > cur_open
            if not (wick_ok and body_ok):
                return None
        else:
            wick_ok = (upper_wick / rng) > self.wick_frac_min
            body_ok = cur_close < cur_open
            if not (wick_ok and body_ok):
                return None

        # --- Stop placement just beyond retest level --------------------
        sl_buffer = self.sl_buffer_pips * pip
        if direction == TradeDirection.LONG:
            # Below retest level OR below current low, whichever is lower
            stop_price = min(retest_level, cur_low) - sl_buffer
        else:
            stop_price = max(retest_level, cur_high) + sl_buffer

        risk = abs(cur_close - stop_price)
        if risk <= 0:
            return None

        # --- Take profit: project to recent swing high / low ------------
        if direction == TradeDirection.LONG:
            recent_hi = float(max(m5_high[-self.swing_lookback:]))
            tp_proj = recent_hi
            tp_floor = cur_close + self.min_tp_pips * pip
            take_profit = max(tp_proj, tp_floor)
            reward = take_profit - cur_close
        else:
            recent_lo = float(min(m5_low[-self.swing_lookback:]))
            tp_proj = recent_lo
            tp_floor = cur_close - self.min_tp_pips * pip
            take_profit = min(tp_proj, tp_floor)
            reward = cur_close - take_profit

        if reward <= 0:
            return None
        rr = reward / risk
        if rr < self.min_rr:
            return None

        projected_tp_pips = reward / pip
        strategy_id = (
            "ITP_pullback_long" if direction == TradeDirection.LONG
            else "ITP_pullback_short"
        )

        log.info(
            "[STRATEGY:intraday_trend_pullback] %s symbol=%s bias=%s "
            "retest=%s lvl=%.5f close=%.5f rr=%.2f tp_pips=%.1f",
            strategy_id, symbol, htf_bias, retest_type, retest_level,
            cur_close, rr, projected_tp_pips,
        )

        return TradeCandidate(
            symbol=symbol,
            direction=direction,
            strategy=strategy_id,
            entry_price=cur_close,
            stop_price=stop_price,
            take_profit=take_profit,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "INTRADAY_TREND_PULLBACK",
                "strategy_family": "trend_pullback",
                "management_profile": "trend_runner",
                "htf_bias": htf_bias,
                "retest_level": float(retest_level),
                "retest_type": retest_type,
                "retest_distance_pips": float(dist_pips),
                "bias_delta_pips": float(bias_delta_pips),
                "lower_wick_frac": float(lower_wick / rng),
                "upper_wick_frac": float(upper_wick / rng),
                "projected_tp_pips": float(projected_tp_pips),
                "risk_points": float(risk),
                "reward_points": float(reward),
            },
            created_at=datetime.now(timezone.utc),
        )


__all__ = ["IntradayTrendPullbackStrategy"]
