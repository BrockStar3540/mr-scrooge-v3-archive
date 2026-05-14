"""TF6_long / USD_MXN shadow micro-bot observer.

Research origin
---------------
Discovered 2026-05-13 in the LOOSENED regime-discovery pass (after the strict
unbiased pipeline produced 0 survivors and the TF6_short USD_JPY observer was
shipped).

Methodology difference vs the TF6_short USDJPY observer (shipped earlier):
- Strict pipeline (TF6_short USDJPY): DecisionTreeClassifier on is_winner,
  min_samples_leaf=60, win_rate >= 0.40 gate, then triple-gate validation.
- Loosened pipeline (TF6_long USDMXN, this bot): DecisionTreeRegressor on
  realized_R, min_samples_leaf=30, NO win_rate gate, then stress stack.

This bot survived: holdout CI > 0, recent 6mo CI > 0, walk-forward 3/4,
vol-conditional spread (3x when vol_ratio<0.2, 2x when <0.4), random slippage
Monte Carlo (1000 draws, 100% positive), hour concentration audit
(max 23.3% at hour 7 UTC), Sunday concentration 0.4%.

Reference performance (post all stress, vol-conditional spread):
  n_d=510  mean_R_d=+0.24
  n_h=60   mean_R_h=+0.38   CI_lo=+0.06
  n_recent=36 (Oct 2025+)   mean_R_recent=+0.56   CI_lo=+0.06
  slippage MC 5th-pctile recent = +0.55, 100% draws positive
  hour-7 UTC concentration = 23.3% (London pre-open, USD_MXN main session start)

Statistical caveat: permutation test NOT YET RUN on the loosened pipeline.
This bot has weaker statistical backing than the TF6_short USDJPY bot.
OBSERVE-ONLY. No order placement.

Sample size caveat: ~36 fires per 6mo = ~1.5/week. Shadow data accumulates
slowly.

USD_MXN cost caveat: dukascopy mid-price approximation used 12 pip base spread.
OANDA live spread varies — can balloon during US data releases. Spread monitor
data over the shadow window will reveal whether the 12-pip assumption holds.

Signal rule
-----------
Trigger (TF6 long ribbon):
  - EMA9 > EMA21 > EMA50 (ascending, computed on M5 closes)
  - All three EMAs rising vs prior bar
  - EMA50 5-bar slope > +0.05% (uptrend confirmation)
Discovered regime gate:
  - rsi14 > 80.83 (overbought — fading the top, mean-reversion-flavored long)
  - atr_ratio <= 1.355 (modest volatility, NOT in an outsized expansion)
  - ema50_dist <= 0.94% (price not too stretched above EMA50)
Hour exclusion (proven artifact band from prior research):
  - hour_utc NOT in [21, 22, 23) UTC
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Any

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.observe.tf6_long_usdmxn")


class TF6LongUSDMXNObserver:
    """Shadow observer for the TF6_long / USD_MXN micro-bot."""

    name: str = "tf6_long_usdmxn_observer"
    SYMBOL: str = "USD_MXN"

    RSI_MIN: float = 80.83
    ATR_RATIO_MAX: float = 1.355
    EMA50_DIST_MAX: float = 0.00941  # positive cap — price <= 0.94% above EMA50
    EMA50_SLOPE_5B_MIN: float = 0.0005
    ATR_RATIO_WINDOW: int = 288
    ROLLOVER_BAND_START_UTC: int = 21
    ROLLOVER_BAND_END_UTC: int = 23

    def __init__(self, config: dict | None = None):
        config = config or {}
        self._output_path = Path(config.get("output_path", "data/observe-tf6-long-usdmxn.jsonl"))
        self._output_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = Lock()
        self._last_emitted_bar_ts: str | None = None

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        values: dict[str, Any] = {
            "applies": symbol == self.SYMBOL,
            "fired": False,
            "reason": "",
            "entry": 0.0, "stop": 0.0, "tp_2r": 0.0,
            "ema9": 0.0, "ema21": 0.0, "ema50": 0.0,
            "ema50_dist": 0.0, "ema50_slope_5b": 0.0,
            "rsi14": 0.0, "atr_ratio": 0.0,
            "weekday": -1, "hour_utc": -1, "bar_ts": "",
        }
        if symbol != self.SYMBOL:
            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

        m5 = snapshot.candles.get("5M")
        if m5 is None or len(m5) < max(60, self.ATR_RATIO_WINDOW + 25):
            values["reason"] = "insufficient_m5_bars"
            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

        try:
            bars = m5[["open", "high", "low", "close"]].copy()
            if not isinstance(bars.index, pd.DatetimeIndex):
                if "time" in bars.columns:
                    bars.index = pd.to_datetime(bars["time"], utc=True)
                else:
                    values["reason"] = "no_time_index"
                    return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            close = bars["close"].astype(float)
            high  = bars["high"].astype(float)
            low   = bars["low"].astype(float)

            ema9  = close.ewm(span=9,  adjust=False).mean()
            ema21 = close.ewm(span=21, adjust=False).mean()
            ema50 = close.ewm(span=50, adjust=False).mean()

            c_now = float(close.iloc[-1])
            e9, e21, e50 = float(ema9.iloc[-1]), float(ema21.iloc[-1]), float(ema50.iloc[-1])
            values.update({"ema9": e9, "ema21": e21, "ema50": e50})

            bar_ts_idx = bars.index[-1]
            now_dt = pd.Timestamp(bar_ts_idx)
            if now_dt.tzinfo is None:
                now_dt = now_dt.tz_localize("UTC")
            else:
                now_dt = now_dt.tz_convert("UTC")
            bar_ts_iso = now_dt.isoformat()
            values["bar_ts"] = bar_ts_iso
            values["weekday"] = int(now_dt.weekday())
            values["hour_utc"] = int(now_dt.hour)

            # GATE 1: rollover artifact-band exclusion
            if self.ROLLOVER_BAND_START_UTC <= now_dt.hour < self.ROLLOVER_BAND_END_UTC:
                values["reason"] = "rollover_band_excluded"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # GATE 2: TF6 long ribbon — ASCENDING
            if not (e9 > e21 > e50):
                values["reason"] = "ema_ribbon_not_ascending"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # GATE 3: all three EMAs rising
            if not (e9 > float(ema9.iloc[-2]) and
                    e21 > float(ema21.iloc[-2]) and
                    e50 > float(ema50.iloc[-2])):
                values["reason"] = "emas_not_all_rising"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # GATE 4: EMA50 5-bar slope
            slope_50 = (e50 - float(ema50.iloc[-6])) / float(ema50.iloc[-6])
            values["ema50_slope_5b"] = float(slope_50)
            if slope_50 <= self.EMA50_SLOPE_5B_MIN:
                values["reason"] = f"ema50_slope_{slope_50:.5f}_below_threshold"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # GATE 5: discovered regime — ema50_dist <= 0.94%
            ema50_dist = (c_now - e50) / e50
            values["ema50_dist"] = float(ema50_dist)
            if ema50_dist > self.EMA50_DIST_MAX:
                values["reason"] = f"ema50_dist_{ema50_dist:.5f}_above_max"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # GATE 6: discovered regime — RSI > 80.83
            delta = close.diff()
            gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
            loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
            rsi = (100 - 100 / (1 + gain / loss)).iloc[-1]
            values["rsi14"] = float(rsi)
            if pd.isna(rsi) or rsi <= self.RSI_MIN:
                values["reason"] = f"rsi_{rsi:.2f}_below_threshold"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # GATE 7: discovered regime — atr_ratio <= 1.355
            tr = pd.concat(
                [high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()],
                axis=1
            ).max(axis=1)
            atr14 = tr.ewm(alpha=1/14, adjust=False).mean()
            atr_ratio_series = atr14 / atr14.rolling(self.ATR_RATIO_WINDOW).mean()
            atr_ratio = float(atr_ratio_series.iloc[-1])
            values["atr_ratio"] = atr_ratio
            if pd.isna(atr_ratio) or atr_ratio > self.ATR_RATIO_MAX:
                values["reason"] = f"atr_ratio_{atr_ratio:.3f}_above_max"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # ALL GATES PASSED — bot fires (long)
            # Stop: min(low[-5:]) per TF2-style baseline, then compare 10-bar to be conservative
            stop = float(low.iloc[-10:].min())
            if stop >= c_now:
                values["reason"] = "swing_low_not_below_entry"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())
            risk = c_now - stop
            tp_2r = c_now + 2 * risk
            values.update({
                "fired": True, "reason": "all_gates_passed",
                "entry": c_now, "stop": stop, "tp_2r": tp_2r,
            })

            with self._lock:
                if self._last_emitted_bar_ts != bar_ts_iso:
                    try:
                        self._output_path.parent.mkdir(parents=True, exist_ok=True)
                        with open(self._output_path, "a") as f:
                            payload = {
                                "event": "observe_micro_bot_signal",
                                "bot": "TF6_long_USD_MXN",
                                "symbol": self.SYMBOL,
                                "direction": "long",
                                "logged_at": datetime.now(timezone.utc).isoformat(),
                                "bar_ts": bar_ts_iso,
                                "entry": c_now, "stop": stop, "tp_2r": tp_2r,
                                "risk_px": risk,
                                "context": {
                                    "ema9": e9, "ema21": e21, "ema50": e50,
                                    "ema50_dist": float(ema50_dist),
                                    "ema50_slope_5b": float(slope_50),
                                    "rsi14": float(rsi),
                                    "atr_ratio": atr_ratio,
                                    "weekday": int(now_dt.weekday()),
                                    "hour_utc": int(now_dt.hour),
                                },
                                "spread_at_fire_px": float(getattr(snapshot, "spread", 0.0) or 0.0),
                                "spread_at_fire_pips": float((getattr(snapshot, "spread", 0.0) or 0.0) / (0.01 if self.SYMBOL.endswith("JPY") else 0.0001)),
                                "research_methodology": "loosened_regressor_min_leaf_30",
                                "permutation_p_value": None,
                            }
                            f.write(json.dumps(payload) + "\n")
                        self._last_emitted_bar_ts = bar_ts_iso
                        log.info(
                            "%s TF6_long USDMXN shadow fire: entry=%.5f stop=%.5f tp=%.5f",
                            bar_ts_iso, c_now, stop, tp_2r,
                        )
                    except Exception:
                        log.exception("TF6_long observer: shadow write failed")

            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

        except Exception:
            log.exception("%s: tf6_long_usdmxn_observer compute failed", symbol)
            values["reason"] = "exception"
            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())
