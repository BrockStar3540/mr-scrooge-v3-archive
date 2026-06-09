"""MatrixFeaturesCalculator — supplies the lab-format inputs the v3 matrix needs.

Background: the lab spec-sweep produced trade rows with 95 columns including
pip-scaled ATRs per timeframe, EMA slopes, HTF % positions, and trend per
timeframe. The default live feature stack only publishes daily ATR, EMA
values (not slopes), and a single RSI. The v3 MatrixRouterGate needs the
lab-compatible inputs at scan time or every formula match degrades to the
no-data sentinel buckets (RSIx, A1_x, E20x, ...) and the gate blocks everything.

This module reads the same OANDA candles the rest of the live pipeline uses
and computes the missing lab-format keys in one place, so the lab and live
feature contracts converge.

Outputs (FeatureResult.values keys):
    atr_5m_pips      — ATR(14) on 5M bars, in pips
    atr_1h_pips      — ATR(14) on 1H bars, in pips
    bb_width_pips    — Bollinger band width (20-period 1H) in pips
    ema20_slope      — (ema20_t - ema20_{t-1}) on 1H bars, in pips
    ema50_slope      — same for ema50 on 1H bars
    htf_pct_20       — close position within last 20 1H bars [0..1]
    htf_pct_60       — close position within last 60 1H bars [0..1]
    htf_bias_20      — "long"/"short"/"flat" derived from htf_pct_20
    htf_bias_60      — same for htf_pct_60
    trend_1h         — "long"/"short"/"flat" from close vs ema20 on 1H
    trend_4h         — "long"/"short"/"flat" from close vs ema20 on resampled 4H
    rsi14            — alias of live `rsi` feature for lab-key compatibility
    zscore           — alias of live `z_score` feature for lab-key compatibility
    _degraded        — list of keys that fell back to safe defaults

Every degraded computation is logged with the cause so the live behavior is
auditable from journalctl.
"""

from __future__ import annotations

import logging
from datetime import datetime

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.matrix_features")


def _pip_size(symbol: str) -> float:
    return 0.01 if any(j in (symbol or "") for j in ("JPY", "MXN")) else 0.0001


def _atr14_pips(bars: pd.DataFrame, pip: float) -> float | None:
    if bars is None or len(bars) < 15:
        return None
    df = bars.iloc[-30:].copy()
    high = df["high"].astype(float)
    low = df["low"].astype(float)
    close_prev = df["close"].astype(float).shift(1)
    tr = pd.concat(
        [
            (high - low).abs(),
            (high - close_prev).abs(),
            (low - close_prev).abs(),
        ],
        axis=1,
    ).max(axis=1)
    tr = tr.dropna()
    if len(tr) < 14:
        return None
    atr = float(tr.ewm(alpha=1.0 / 14, adjust=False).mean().iloc[-1])
    return atr / pip if pip > 0 else None


def _ema_slope_pips(bars: pd.DataFrame, period: int, pip: float) -> float | None:
    # EWMA(adjust=False) returns a value from bar 0 onward, so the slope
    # only needs `period` bars for the EMA to be meaningfully seeded and
    # 2 EMA values to diff. With exactly `period` bars we get both.
    if bars is None or len(bars) < period:
        return None
    closes = bars["close"].astype(float)
    ema = closes.ewm(span=period, adjust=False).mean()
    if len(ema) < 2:
        return None
    slope = float(ema.iloc[-1] - ema.iloc[-2])
    return slope / pip if pip > 0 else None


def _bb_width_pips(bars: pd.DataFrame, period: int, k: float, pip: float) -> float | None:
    if bars is None or len(bars) < period:
        return None
    closes = bars["close"].astype(float).iloc[-period:]
    if len(closes) < 2:
        return None
    mean = float(closes.mean())
    std = float(closes.std(ddof=1))
    if std <= 0:
        return None
    return (2 * k * std) / pip if pip > 0 else None


def _pct_position(bars: pd.DataFrame, window: int) -> float | None:
    if bars is None or len(bars) < window:
        return None
    df = bars.iloc[-window:]
    hi = float(df["high"].astype(float).max())
    lo = float(df["low"].astype(float).min())
    if hi <= lo:
        return None
    close = float(df["close"].astype(float).iloc[-1])
    return (close - lo) / (hi - lo)


def _bias_from_pct(pct: float | None) -> str:
    if pct is None:
        return ""
    if pct >= 0.60:
        return "long"
    if pct <= 0.40:
        return "short"
    return "flat"


def _trend_from_ema(bars: pd.DataFrame, period: int, deadzone_bps: float) -> str:
    if bars is None or len(bars) < period + 1:
        return ""
    closes = bars["close"].astype(float)
    ema = closes.ewm(span=period, adjust=False).mean()
    c = float(closes.iloc[-1])
    e = float(ema.iloc[-1])
    if e <= 0:
        return ""
    band = deadzone_bps / 10000.0
    if c > e * (1.0 + band):
        return "long"
    if c < e * (1.0 - band):
        return "short"
    return "flat"


class MatrixFeaturesCalculator:
    """Lab-compatible feature publisher for the v3 MatrixRouter."""

    name: str = "matrix_features"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.ema_short = int(config.get("ema_short", 20))
        self.ema_long = int(config.get("ema_long", 50))
        self.bb_period = int(config.get("bb_period", 20))
        self.bb_k = float(config.get("bb_k", 2.0))
        # Default windows match technical_context.h1_rank_window=48
        # which is the V3 snapshot's 1H history depth.
        self.htf_short_window = int(config.get("htf_short_window", 20))
        self.htf_long_window = int(config.get("htf_long_window", 48))
        self.trend_4h_ema = int(config.get("trend_4h_ema", 5))   # ema5 on 4H resample
        self.trend_deadzone_bps = float(config.get("trend_deadzone_bps", 5.0))

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        pip = _pip_size(symbol)
        m5 = snapshot.candles.get("5M")
        h1 = snapshot.candles.get("1H")

        values: dict = {
            "atr_5m_pips": None,
            "atr_1h_pips": None,
            "bb_width_pips": None,
            "ema20_slope": None,
            "ema50_slope": None,
            "htf_pct_20": None,
            "htf_pct_60": None,
            "htf_bias_20": "",
            "htf_bias_60": "",
            "trend_1h": "",
            "trend_4h": "",
            "rsi14": None,
            "zscore": None,
        }
        degraded: list[str] = []

        # ATR per timeframe
        if m5 is not None and len(m5) >= 15:
            values["atr_5m_pips"] = round(_atr14_pips(m5, pip) or 0.0, 4) or None
        else:
            degraded.append("atr_5m_pips:no_5m_bars")

        if h1 is not None and len(h1) >= 15:
            values["atr_1h_pips"] = round(_atr14_pips(h1, pip) or 0.0, 4) or None
        else:
            degraded.append("atr_1h_pips:no_1h_bars")

        # BB width pips (1H, 20-period) — fallback if live bollinger is on a different timeframe
        if h1 is not None and len(h1) >= self.bb_period:
            values["bb_width_pips"] = round(_bb_width_pips(h1, self.bb_period, self.bb_k, pip) or 0.0, 4) or None
        else:
            degraded.append("bb_width_pips:insufficient_h1_bars")

        # EMA slopes — _ema_slope_pips itself needs only `period` bars
        if h1 is not None and len(h1) >= self.ema_short:
            values["ema20_slope"] = round(_ema_slope_pips(h1, self.ema_short, pip) or 0.0, 6)
        else:
            have = len(h1) if h1 is not None else 0
            degraded.append(f"ema20_slope:need{self.ema_short}_have{have}")

        if h1 is not None and len(h1) >= self.ema_long:
            values["ema50_slope"] = round(_ema_slope_pips(h1, self.ema_long, pip) or 0.0, 6)
        else:
            have = len(h1) if h1 is not None else 0
            degraded.append(f"ema50_slope:need{self.ema_long}_have{have}")

        # HTF directional buckets — DAILY N-day return (signed), matching the lab
        # corpus + factor_buckets. Prior impl used a 1H [0..1] range-position
        # (_pct_position) — a different quantity that froze H20/H60 at 'e' live.
        # Fix 2026-06-09: daily candles already in the snapshot; use 20d/60d return.
        _d = snapshot.candles.get("D")
        _dcl = _d["close"].astype(float) if (_d is not None and "close" in _d and len(_d)) else None
        def _daily_ret(lb):
            if _dcl is None or len(_dcl) <= lb:
                return None
            a = float(_dcl.iloc[-1]); b = float(_dcl.iloc[-1 - lb])
            return ((a - b) / b) if b else 0.0
        pct20 = _daily_ret(20)
        pct60 = _daily_ret(60)
        values["htf_pct_20"] = round(pct20, 6) if pct20 is not None else None
        values["htf_pct_60"] = round(pct60, 6) if pct60 is not None else None
        _sgn = lambda p: ("long" if p > 0 else "short" if p < 0 else "flat") if p is not None else ""
        values["htf_bias_20"] = _sgn(pct20)
        values["htf_bias_60"] = _sgn(pct60)
        _dhave = len(_dcl) if _dcl is not None else 0
        if pct20 is None:
            degraded.append(f"htf_pct_20:needD>20_have{_dhave}")
        if pct60 is None:
            degraded.append(f"htf_pct_60:needD>60_have{_dhave}")

        # Trend per timeframe
        trend_1h = _trend_from_ema(h1, self.ema_short, self.trend_deadzone_bps) if h1 is not None else ""
        values["trend_1h"] = trend_1h
        if not trend_1h:
            degraded.append("trend_1h:no_1h_bars")

        # 4H resample from 1H — needs trend_4h_ema*4+4 1H bars minimum
        # (4H bars after resample = h1_bars // 4, need trend_4h_ema+1 4H bars).
        trend_4h = ""
        min_h1_for_4h = (self.trend_4h_ema + 1) * 4 + 4   # safety margin for edge resample
        if h1 is not None and len(h1) >= min_h1_for_4h:
            try:
                h1c = h1.copy()
                if not isinstance(h1c.index, pd.DatetimeIndex):
                    if "time" in h1c.columns:
                        h1c.index = pd.to_datetime(h1c["time"], utc=True)
                if isinstance(h1c.index, pd.DatetimeIndex):
                    h4 = h1c.resample("4h").agg({
                        "open": "first",
                        "high": "max",
                        "low": "min",
                        "close": "last",
                    }).dropna()
                    if len(h4) >= self.trend_4h_ema + 1:
                        trend_4h = _trend_from_ema(h4, self.trend_4h_ema, self.trend_deadzone_bps)
                    else:
                        degraded.append(f"trend_4h:after_resample_only_{len(h4)}_4h_bars")
            except Exception as e:
                degraded.append(f"trend_4h:resample_failed:{type(e).__name__}")
        else:
            degraded.append(f"trend_4h:need{min_h1_for_4h}_have{len(h1) if h1 is not None else 0}")
        values["trend_4h"] = trend_4h

        # Lab key aliases — pull from sibling features if already computed
        rsi_feat = (state or {}).get("rsi_value")
        if rsi_feat is None:
            # Lazy compute RSI(14) on 1H closes ourselves
            if h1 is not None and len(h1) >= 15:
                closes = h1["close"].astype(float)
                delta = closes.diff().dropna()
                gains = delta.clip(lower=0)
                losses = -delta.clip(upper=0)
                ag = float(gains.ewm(alpha=1 / 14, adjust=False).mean().iloc[-1])
                al = float(losses.ewm(alpha=1 / 14, adjust=False).mean().iloc[-1])
                if al == 0:
                    rsi_feat = 100.0
                else:
                    rsi_feat = 100 - (100 / (1 + ag / al))
        if rsi_feat is None:
            degraded.append("rsi14:no_1h_bars")
        else:
            values["rsi14"] = round(float(rsi_feat), 2)

        # zscore from 1H closes vs 20-period mean
        if h1 is not None and len(h1) >= self.bb_period:
            closes = h1["close"].astype(float).iloc[-self.bb_period:]
            mean = float(closes.mean())
            std = float(closes.std(ddof=1))
            if std > 0:
                values["zscore"] = round((float(closes.iloc[-1]) - mean) / std, 4)
            else:
                degraded.append("zscore:zero_std")
        else:
            degraded.append("zscore:insufficient_h1_bars")

        values["_degraded"] = degraded

        # Per-call audit log so we can read the full picture from journalctl.
        # Keep it on one line to keep grep tractable.
        log.info(
            "[MATRIX_FEATURES] %s atr5m=%s atr1h=%s ema20s=%s ema50s=%s "
            "htf20=%s/%s htf60=%s/%s tr1h=%s tr4h=%s rsi14=%s zs=%s bbw=%s degraded=%s",
            symbol,
            f"{values['atr_5m_pips']:.2f}p" if values["atr_5m_pips"] is not None else "-",
            f"{values['atr_1h_pips']:.2f}p" if values["atr_1h_pips"] is not None else "-",
            f"{values['ema20_slope']:.3f}p" if values["ema20_slope"] is not None else "-",
            f"{values['ema50_slope']:.3f}p" if values["ema50_slope"] is not None else "-",
            f"{values['htf_pct_20']:.3f}" if values["htf_pct_20"] is not None else "-",
            values["htf_bias_20"] or "-",
            f"{values['htf_pct_60']:.3f}" if values["htf_pct_60"] is not None else "-",
            values["htf_bias_60"] or "-",
            values["trend_1h"] or "-",
            values["trend_4h"] or "-",
            values["rsi14"] if values["rsi14"] is not None else "-",
            values["zscore"] if values["zscore"] is not None else "-",
            f"{values['bb_width_pips']:.2f}p" if values["bb_width_pips"] is not None else "-",
            ",".join(degraded) or "none",
        )

        return FeatureResult(
            name=self.name,
            values=values,
            computed_at=datetime.now(),
        )
