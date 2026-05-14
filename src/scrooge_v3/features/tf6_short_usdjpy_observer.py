"""TF6_short / USD_JPY shadow micro-bot observer.

Research origin
---------------
Discovered 2026-05-13 as the sole survivor of the strategy-library regime
discovery pipeline after all integrity gates were applied:

  - look-ahead corrected M15/H1 labels
  - rollover hour (UTC 21-23) excluded
  - hour_utc removed as decision-tree feature
  - vol-conditional spread stress (3x when vol_ratio<0.2)
  - random slippage Monte Carlo (0-2 pips)
  - fire-time concentration audit (max 40% per hour OR weekday)
  - walk-forward positive in >=3/4 holdout windows
  - recent 6mo CI lower bound > 0

Reference performance (research holdout, post all stress):
  n_h=100  mean_R_h=+0.32  CI_lo=+0.01
  n_recent=23  mean_R_recent=+1.19  CI_lo=+0.67

Statistical caveat: permutation test on the broader pipeline produced
p ≈ 0.2 — economically promising but not statistically significant.
This bot is OBSERVE-ONLY. No live order placement.

What this module does
---------------------
At each scan cycle for USD_JPY:
  1. Evaluate the discovered trigger + regime gate on the latest M5 close
  2. If conditions fire, write a JSONL signal to `data/observe-tf6-usdjpy.jsonl`
  3. Deduplicate by M5 bar timestamp (one signal per close)
  4. Return a FeatureResult so dashboards / ML observer can see the state

It does NOT call the broker. It does NOT influence V3's strategy decisions.

Signal rule (the only TF6_short USDJPY rule that survived all gates)
-------------------------------------------------------------------
Trigger:
  - EMA9 < EMA21 < EMA50 (descending order, computed on M5 closes)
  - All three EMAs falling vs prior bar
  - EMA50 5-bar slope < -0.05% (downtrend confirmation)
Discovered regime gate:
  - weekday in {Wed, Thu, Fri, Sun (UTC)} — weekday > 1 in pandas weekday
  - ema50_dist <= -0.48% (price well below EMA50)
  - bb_width_rank_288 <= 0.998 (effectively any compression)
Hour exclusion (rollover artifact band):
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

log = logging.getLogger("scrooge_v3.observe.tf6_short_usdjpy")


class TF6ShortUSDJPYObserver:
    """Shadow observer for the TF6_short / USD_JPY micro-bot."""

    name: str = "tf6_short_usdjpy_observer"
    SYMBOL: str = "USD_JPY"

    # Numeric thresholds from the discovered rule
    EMA50_DIST_MAX: float = -0.00477   # price >= 0.477% below EMA50 (negative)
    BB_WIDTH_RANK_MAX: float = 0.998   # near-no-op upper bound from tree
    EMA50_SLOPE_5B_MAX: float = -0.0005  # 5-bar slope must be < -0.05%
    BB_WIDTH_RANK_WINDOW: int = 288     # rolling window for bb_width percentile rank
    WEEKDAY_MIN: int = 2                # pandas: Mon=0; >1.5 means weekday in {2..6}
    ROLLOVER_BAND_START_UTC: int = 21
    ROLLOVER_BAND_END_UTC: int = 23     # exclude [21, 23)

    def __init__(self, config: dict | None = None):
        config = config or {}
        self._output_path = Path(config.get("output_path", "data/observe-tf6-usdjpy.jsonl"))
        self._output_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = Lock()
        self._last_emitted_bar_ts: str | None = None  # dedup against same M5 bar

    # ------------------------------------------------------------------
    # Standard feature contract
    # ------------------------------------------------------------------
    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        values: dict[str, Any] = {
            "applies": symbol == self.SYMBOL,
            "fired": False,
            "reason": "",
            "entry": 0.0,
            "stop": 0.0,
            "tp_2r": 0.0,
            "ema9": 0.0,
            "ema21": 0.0,
            "ema50": 0.0,
            "ema50_dist": 0.0,
            "ema50_slope_5b": 0.0,
            "bb_width_rank_288": 0.0,
            "weekday": -1,
            "hour_utc": -1,
            "bar_ts": "",
        }
        if symbol != self.SYMBOL:
            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

        m5 = snapshot.candles.get("5M")
        if m5 is None or len(m5) < max(50, self.BB_WIDTH_RANK_WINDOW + 25):
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

            # Use the LAST CLOSED M5 bar — the snapshot's latest row IS the
            # most recent closed bar (V3 fetches finished candles).
            close = bars["close"].astype(float)
            high  = bars["high"].astype(float)

            ema9  = close.ewm(span=9,  adjust=False).mean()
            ema21 = close.ewm(span=21, adjust=False).mean()
            ema50 = close.ewm(span=50, adjust=False).mean()

            c_now = float(close.iloc[-1])
            e9, e21, e50 = float(ema9.iloc[-1]), float(ema21.iloc[-1]), float(ema50.iloc[-1])
            values.update({"ema9": e9, "ema21": e21, "ema50": e50})

            # bar_ts as iso string for dedup
            bar_ts_idx = bars.index[-1]
            bar_ts_iso = (
                bar_ts_idx.tz_convert("UTC").isoformat()
                if getattr(bar_ts_idx, "tzinfo", None) is not None
                else pd.Timestamp(bar_ts_idx).tz_localize("UTC").isoformat()
            )
            now_dt = pd.Timestamp(bar_ts_idx)
            if now_dt.tzinfo is None:
                now_dt = now_dt.tz_localize("UTC")
            else:
                now_dt = now_dt.tz_convert("UTC")
            values["bar_ts"] = bar_ts_iso
            values["weekday"] = int(now_dt.weekday())
            values["hour_utc"] = int(now_dt.hour)

            # === GATE 1: rollover artifact-band exclusion ===
            if self.ROLLOVER_BAND_START_UTC <= now_dt.hour < self.ROLLOVER_BAND_END_UTC:
                values["reason"] = "rollover_band_excluded"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # === GATE 2: weekday filter (Wed-Sun) ===
            if now_dt.weekday() < self.WEEKDAY_MIN:
                values["reason"] = "weekday_excluded"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # === GATE 3: trigger — descending EMA ribbon ===
            if not (e9 < e21 < e50):
                values["reason"] = "ema_ribbon_not_descending"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # === GATE 4: all three EMAs falling ===
            if not (e9 < float(ema9.iloc[-2]) and
                    e21 < float(ema21.iloc[-2]) and
                    e50 < float(ema50.iloc[-2])):
                values["reason"] = "emas_not_all_falling"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # === GATE 5: EMA50 5-bar slope ===
            slope_50 = (e50 - float(ema50.iloc[-6])) / float(ema50.iloc[-6])
            values["ema50_slope_5b"] = float(slope_50)
            if slope_50 >= self.EMA50_SLOPE_5B_MAX:
                values["reason"] = f"ema50_slope_{slope_50:.5f}_above_threshold"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # === GATE 6: discovered regime — ema50_dist ===
            ema50_dist = (c_now - e50) / e50
            values["ema50_dist"] = float(ema50_dist)
            if ema50_dist > self.EMA50_DIST_MAX:
                values["reason"] = f"ema50_dist_{ema50_dist:.5f}_above_threshold"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # === GATE 7: discovered regime — bb_width_rank ===
            sma20 = close.rolling(20).mean()
            std20 = close.rolling(20).std(ddof=0)
            bb_upper = sma20 + 2 * std20
            bb_lower = sma20 - 2 * std20
            bb_width = (bb_upper - bb_lower) / sma20
            bbw_rank = bb_width.rolling(self.BB_WIDTH_RANK_WINDOW).rank(pct=True).iloc[-1]
            values["bb_width_rank_288"] = float(bbw_rank) if pd.notna(bbw_rank) else 0.0
            if pd.isna(bbw_rank) or bbw_rank > self.BB_WIDTH_RANK_MAX:
                values["reason"] = "bb_width_rank_above_threshold_or_nan"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

            # === ALL GATES PASSED — bot fires ===
            stop = float(high.iloc[-10:].max())  # max(high[-10:]) — 10-bar swing high
            if stop <= c_now:
                values["reason"] = "swing_high_not_above_entry"
                return FeatureResult(name=self.name, values=values, computed_at=datetime.now())
            risk = stop - c_now
            tp_2r = c_now - 2 * risk
            values.update({
                "fired": True,
                "reason": "all_gates_passed",
                "entry": c_now,
                "stop": stop,
                "tp_2r": tp_2r,
            })

            # === Emit shadow signal (dedup per M5 bar) ===
            with self._lock:
                if self._last_emitted_bar_ts != bar_ts_iso:
                    try:
                        self._output_path.parent.mkdir(parents=True, exist_ok=True)
                        with open(self._output_path, "a") as f:
                            payload = {
                                "event": "observe_micro_bot_signal",
                                "bot": "TF6_short_USD_JPY",
                                "symbol": self.SYMBOL,
                                "direction": "short",
                                "logged_at": datetime.now(timezone.utc).isoformat(),
                                "bar_ts": bar_ts_iso,
                                "entry": c_now, "stop": stop, "tp_2r": tp_2r,
                                "risk_px": risk,
                                "context": {
                                    "ema9": e9, "ema21": e21, "ema50": e50,
                                    "ema50_dist": float(ema50_dist),
                                    "ema50_slope_5b": float(slope_50),
                                    "bb_width_rank_288": float(bbw_rank),
                                    "weekday": int(now_dt.weekday()),
                                    "hour_utc": int(now_dt.hour),
                                },
                                "spread_at_fire_px": float(getattr(snapshot, "spread", 0.0) or 0.0),
                                "spread_at_fire_pips": float((getattr(snapshot, "spread", 0.0) or 0.0) / (0.01 if self.SYMBOL.endswith("JPY") else 0.0001)),
                            }
                            f.write(json.dumps(payload) + "\n")
                        self._last_emitted_bar_ts = bar_ts_iso
                        log.info(
                            "%s TF6_short USDJPY shadow fire: entry=%.5f stop=%.5f tp=%.5f",
                            bar_ts_iso, c_now, stop, tp_2r,
                        )
                    except Exception:
                        log.exception("TF6_short observer: shadow write failed")

            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())

        except Exception:
            log.exception("%s: tf6_short_usdjpy_observer compute failed", symbol)
            values["reason"] = "exception"
            return FeatureResult(name=self.name, values=values, computed_at=datetime.now())
