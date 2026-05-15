"""Technical Regime 53 — live V3 feature.

Ports the bar-true 53-regime classifier from
research/technical-regime-53-atlas-v1/build_regime_atlas_v1.py into V3's
feature pipeline.

Required inputs (from snapshot.candles):
  - 5M bars: M5 closes/highs/lows for indicators + last-bar regime input
  - D bars: daily OHLC for daily ATR20 avg + daily BB-width 20 avg baselines

Output (FeatureResult.values):
  - technical_regime_53     (str: M01..S06 + Z01)
  - technical_regime_desc   (str: human label)
  - ATR14, BB_width, ADX14, EMA_slope, RSI14, close_pos, ATR_ratio, BB_compress

Deterministic. No look-ahead — uses only completed bars.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.technical_regime_53")


REGIME_DESC = {
    "M01": "stop_hunt_up_high_adx", "M02": "stop_hunt_up_low_adx",
    "M03": "stop_hunt_dn_high_adx", "M04": "stop_hunt_dn_low_adx",
    "F01": "false_break_up_strong_trend", "F02": "false_break_up",
    "F03": "false_break_dn_strong_trend", "F04": "false_break_dn",
    "B01": "breakout_up_high_vol_trend", "B02": "breakout_up_strong_adx_low_vol",
    "B03": "breakout_up_moderate_adx", "B04": "breakout_up_weak",
    "B05": "breakout_dn_high_vol_trend", "B06": "breakout_dn_strong_adx_low_vol",
    "B07": "breakout_dn_moderate_adx", "B08": "breakout_dn_weak",
    "C01": "tight_coil_low_adx", "C02": "tight_coil_adx",
    "C03": "compressed_bb_active_atr_low_adx", "C04": "compressed_bb_active_atr_adx",
    "X01": "expansion_strong_uptrend", "X02": "expansion_strong_downtrend",
    "X03": "expansion_strong_adx_flat", "X04": "expansion_moderate_trend", "X05": "expansion_no_trend",
    "T01": "strong_uptrend_extended", "T02": "strong_uptrend_room",
    "T03": "strong_downtrend_extended", "T04": "strong_downtrend_room",
    "T05": "moderate_uptrend", "T06": "moderate_downtrend", "T07": "directional_drift_flat",
    "O01": "overbought_range", "O02": "overbought_trend_caution",
    "O03": "oversold_range", "O04": "oversold_trend_caution",
    "O05": "moderately_overbought", "O06": "moderately_oversold",
    "R01": "wide_volatile_range", "R02": "wide_quiet_range", "R03": "normal_range", "R04": "tight_range",
    "S01": "quiet_asia", "S02": "active_asia", "S03": "volatile_asia",
    "S04": "london_midrange_drift", "S05": "quiet_ny", "S06": "active_ny",
    "Z01": "catch_all",
}


def _compute_atr(high, low, close, alpha=1/14):
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=alpha, adjust=False).mean()


def _compute_rsi(close):
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    return 100 - 100 / (1 + gain / loss.replace(0, np.nan))


def _compute_adx(high, low, close):
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm  = pd.Series(np.where((up_move > down_move) & (up_move > 0), up_move, 0.0), index=high.index)
    minus_dm = pd.Series(np.where((down_move > up_move) & (down_move > 0), down_move, 0.0), index=high.index)
    atr = _compute_atr(high, low, close)
    plus_di  = 100 * plus_dm.ewm(alpha=1/14, adjust=False).mean() / atr.replace(0, np.nan)
    minus_di = 100 * minus_dm.ewm(alpha=1/14, adjust=False).mean() / atr.replace(0, np.nan)
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return dx.ewm(alpha=1/14, adjust=False).mean()


def _empty_values() -> dict[str, Any]:
    return {
        "technical_regime_53": "unknown",
        "technical_regime_desc": "insufficient_data",
        "ATR14": None, "BB_width": None, "ADX14": None,
        "EMA_slope": None, "RSI14": None, "close_pos": None,
        "ATR_ratio": None, "BB_compress": None,
    }


class TechnicalRegime53Calculator:
    """Live V3 classifier for the 53-regime bar-true taxonomy."""

    name: str = "technical_regime_53"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.min_m5_bars = int(config.get("min_m5_bars", 50))   # need warmup
        self.min_daily_bars = int(config.get("min_daily_bars", 25))

    def compute(self, symbol: str, snapshot: MarketSnapshot, state: dict) -> FeatureResult:
        m5 = snapshot.candles.get("5M")
        daily = snapshot.candles.get("D")

        if m5 is None or len(m5) < self.min_m5_bars or daily is None or len(daily) < self.min_daily_bars:
            return FeatureResult(name=self.name, values=_empty_values(), computed_at=datetime.now())

        try:
            # M5 indicators
            high = m5["high"].astype(float).reset_index(drop=True)
            low  = m5["low"].astype(float).reset_index(drop=True)
            close = m5["close"].astype(float).reset_index(drop=True)
            atr14 = _compute_atr(high, low, close)
            sma20 = close.rolling(20).mean()
            std20 = close.rolling(20).std(ddof=0)
            upper = sma20 + 2*std20
            lower = sma20 - 2*std20
            bb_width = (upper - lower) / sma20
            adx14 = _compute_adx(high, low, close)
            ema50 = close.ewm(span=50, adjust=False).mean()
            ema_slope = (ema50.iloc[-1] - ema50.iloc[-11]) / ema50.iloc[-11] if len(ema50) >= 11 else 0.0
            rsi14 = _compute_rsi(close)
            max_20 = high.shift(1).rolling(20).max()
            min_20 = low.shift(1).rolling(20).min()
            rng = (max_20 - min_20).replace(0, np.nan)
            close_pos = (close - min_20) / rng

            # Daily baselines
            dh = daily["high"].astype(float)
            dl = daily["low"].astype(float)
            dc = daily["close"].astype(float)
            d_atr14 = _compute_atr(dh, dl, dc)
            d_mid = dc.rolling(20).mean()
            d_std = dc.rolling(20).std(ddof=0)
            d_bbw = ((d_mid + 2*d_std) - (d_mid - 2*d_std)) / d_mid
            # Use prior day's 20-day rolling avg (.shift(1) makes it look-ahead-safe)
            d_atr20_avg = d_atr14.rolling(20).mean().shift(1).iloc[-1]
            d_bbw20_avg = d_bbw.rolling(20).mean().shift(1).iloc[-1]

            # Current-bar values
            atr14_now = float(atr14.iloc[-1])
            bb_width_now = float(bb_width.iloc[-1])
            adx14_now = float(adx14.iloc[-1])
            rsi14_now = float(rsi14.iloc[-1])
            cp_now = float(close_pos.iloc[-1]) if not pd.isna(close_pos.iloc[-1]) else 0.5
            ema_slope_now = float(ema_slope) if not pd.isna(ema_slope) else 0.0

            atr_ratio = atr14_now / d_atr20_avg if d_atr20_avg and d_atr20_avg > 0 else None
            bb_compress = bb_width_now / d_bbw20_avg if d_bbw20_avg and d_bbw20_avg > 0 else None

            # Pattern flags (current bar)
            close_now = float(close.iloc[-1])
            high_now = float(high.iloc[-1])
            low_now = float(low.iloc[-1])
            max_20_now = float(max_20.iloc[-1]) if not pd.isna(max_20.iloc[-1]) else close_now
            min_20_now = float(min_20.iloc[-1]) if not pd.isna(min_20.iloc[-1]) else close_now
            max_20_prev = float(max_20.iloc[-2]) if len(max_20) >= 2 and not pd.isna(max_20.iloc[-2]) else max_20_now
            min_20_prev = float(min_20.iloc[-2]) if len(min_20) >= 2 and not pd.isna(min_20.iloc[-2]) else min_20_now

            breakout_up = close_now > max_20_now * 1.002
            breakout_dn = close_now < min_20_now * 0.998
            bo_up_prev = float(close.iloc[-2]) > max_20_prev * 1.002 if len(close) >= 2 else False
            bo_dn_prev = float(close.iloc[-2]) < min_20_prev * 0.998 if len(close) >= 2 else False
            false_break_up = bo_up_prev and (close_now <= max_20_now)
            false_break_dn = bo_dn_prev and (close_now >= min_20_now)
            sweep_up_prev = float(low.iloc[-2]) < min_20_prev * 0.998 if len(low) >= 2 else False
            sweep_dn_prev = float(high.iloc[-2]) > max_20_prev * 1.002 if len(high) >= 2 else False
            stop_hunt_up = sweep_up_prev and (close_now > min_20_now)
            stop_hunt_dn = sweep_dn_prev and (close_now < max_20_now)

            # Session bucket
            ts = m5.index[-1] if hasattr(m5.index[-1], "hour") else snapshot.timestamp
            h_utc = ts.hour if hasattr(ts, "hour") else 0
            session_asia = 0 <= h_utc < 8
            session_london = 8 <= h_utc < 16
            session_ny = 16 <= h_utc < 24

            # Classify (priority tree from build_regime_atlas_v1.py)
            code = "Z01"
            abs_slope = abs(ema_slope_now)

            def _check(name, cond):
                nonlocal code
                if code != "Z01": return
                if cond: code = name

            _check("M01", stop_hunt_up and adx14_now >= 20)
            _check("M02", stop_hunt_up and adx14_now < 20)
            _check("M03", stop_hunt_dn and adx14_now >= 20)
            _check("M04", stop_hunt_dn and adx14_now < 20)
            _check("F01", false_break_up and adx14_now >= 30)
            _check("F02", false_break_up and adx14_now < 30)
            _check("F03", false_break_dn and adx14_now >= 30)
            _check("F04", false_break_dn and adx14_now < 30)
            if atr_ratio is not None:
                _check("B01", breakout_up and adx14_now >= 40 and atr_ratio >= 1.2)
                _check("B02", breakout_up and adx14_now >= 40 and atr_ratio < 1.2)
            _check("B03", breakout_up and adx14_now < 40 and adx14_now >= 25)
            _check("B04", breakout_up and adx14_now < 25)
            if atr_ratio is not None:
                _check("B05", breakout_dn and adx14_now >= 40 and atr_ratio >= 1.2)
                _check("B06", breakout_dn and adx14_now >= 40 and atr_ratio < 1.2)
            _check("B07", breakout_dn and adx14_now < 40 and adx14_now >= 25)
            _check("B08", breakout_dn and adx14_now < 25)
            if bb_compress is not None and atr_ratio is not None:
                _check("C01", bb_compress <= 0.75 and atr_ratio <= 0.8 and adx14_now < 20)
                _check("C02", bb_compress <= 0.75 and atr_ratio <= 0.8 and adx14_now >= 20)
                _check("C03", bb_compress <= 0.75 and atr_ratio > 0.8 and adx14_now < 20)
                _check("C04", bb_compress <= 0.75 and atr_ratio > 0.8 and adx14_now >= 20)
                _check("X01", atr_ratio >= 1.5 and adx14_now >= 40 and ema_slope_now > 0.002)
                _check("X02", atr_ratio >= 1.5 and adx14_now >= 40 and ema_slope_now < -0.002)
                _check("X03", atr_ratio >= 1.5 and adx14_now >= 40 and abs_slope <= 0.002)
                _check("X04", atr_ratio >= 1.5 and adx14_now < 40 and adx14_now >= 25)
                _check("X05", atr_ratio >= 1.5 and adx14_now < 25)
            _check("T01", adx14_now >= 40 and ema_slope_now > 0.002 and cp_now >= 0.8)
            _check("T02", adx14_now >= 40 and ema_slope_now > 0.002 and cp_now < 0.8)
            _check("T03", adx14_now >= 40 and ema_slope_now < -0.002 and cp_now <= 0.2)
            _check("T04", adx14_now >= 40 and ema_slope_now < -0.002 and cp_now > 0.2)
            _check("T05", adx14_now >= 25 and adx14_now < 40 and ema_slope_now > 0.001)
            _check("T06", adx14_now >= 25 and adx14_now < 40 and ema_slope_now < -0.001)
            _check("T07", adx14_now >= 25 and adx14_now < 40 and abs_slope <= 0.001)
            _check("O01", rsi14_now > 80 and cp_now > 0.9 and adx14_now < 25)
            _check("O02", rsi14_now > 80 and cp_now > 0.9 and adx14_now >= 25)
            _check("O03", rsi14_now < 20 and cp_now < 0.1 and adx14_now < 25)
            _check("O04", rsi14_now < 20 and cp_now < 0.1 and adx14_now >= 25)
            _check("O05", rsi14_now > 70 and rsi14_now <= 80 and cp_now > 0.85)
            _check("O06", rsi14_now < 30 and rsi14_now >= 20 and cp_now < 0.15)
            if atr_ratio is not None:
                _check("R01", adx14_now < 20 and bb_width_now >= 0.05 and atr_ratio >= 1.0)
                _check("R02", adx14_now < 20 and bb_width_now >= 0.05 and atr_ratio < 1.0)
            _check("R03", adx14_now < 20 and bb_width_now < 0.05 and bb_width_now >= 0.02)
            _check("R04", adx14_now < 20 and bb_width_now < 0.02)
            if atr_ratio is not None:
                _check("S01", session_asia and atr_ratio < 0.6 and adx14_now < 20)
                _check("S02", session_asia and atr_ratio >= 0.6 and atr_ratio < 1.0)
                _check("S03", session_asia and atr_ratio >= 1.0)
                _check("S04", session_london and 0.45 <= cp_now <= 0.55 and adx14_now < 20)
                _check("S05", session_ny and atr_ratio < 0.7)
                _check("S06", session_ny and atr_ratio >= 0.7)

            return FeatureResult(
                name=self.name,
                values={
                    "technical_regime_53": code,
                    "technical_regime_desc": REGIME_DESC.get(code, "unknown"),
                    "ATR14": round(atr14_now, 6),
                    "BB_width": round(bb_width_now, 6),
                    "ADX14": round(adx14_now, 2),
                    "EMA_slope": round(ema_slope_now, 6),
                    "RSI14": round(rsi14_now, 2),
                    "close_pos": round(cp_now, 4),
                    "ATR_ratio": round(atr_ratio, 4) if atr_ratio else None,
                    "BB_compress": round(bb_compress, 4) if bb_compress else None,
                    "regime_thresholds_version": "bartrue_2026-05-14",
                },
                computed_at=datetime.now(),
            )
        except Exception:
            log.exception("%s: technical_regime_53 compute failed", symbol)
            return FeatureResult(name=self.name, values=_empty_values(), computed_at=datetime.now())
