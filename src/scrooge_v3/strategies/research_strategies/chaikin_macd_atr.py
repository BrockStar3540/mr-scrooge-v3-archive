"""Chaikin + MACD + ATR momentum strategy — M5 forex scalper.

Research strategy for Mr. Scrooge V3. Combines a Chaikin Money Flow (CMF)
directional bias with a MACD signal-line crossover trigger and an ATR-based
stop/target geometry.

Logic:
  - BIAS: CMF(20) on M5 bars. >0 -> long-only, <0 -> short-only.
  - TRIGGER: MACD(12,26,9) crossover on the current bar.
      * Bullish cross: (MACD - Signal) > 0 this bar AND <= 0 previous bar.
      * Bearish cross: (MACD - Signal) < 0 this bar AND >= 0 previous bar.
  - ENTRY: LONG = CMF > 0 AND bullish cross. SHORT = CMF < 0 AND bearish cross.
  - GEOMETRY:
      SL = entry +/- 1.5 * ATR(14)   (min 10 pips)
      TP = entry +/- 2.5 * ATR(14)   (min 12 pips)

Emits TradeCandidate with strategy = "CMA_long" or "CMA_short" and
strategy_family = "chaikin_macd_atr". Returns None gracefully when data is
insufficient (needs >=26 bars for MACD, >=20 for CMF, >=14 for ATR).
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone

import pandas as pd

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection


log = logging.getLogger("scrooge_v3.strategy.chaikin_macd_atr")


# ---------------------------------------------------------------------------
# Indicator helpers
# ---------------------------------------------------------------------------

def _chaikin_money_flow(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series,
    window: int = 20,
) -> float | None:
    """Return latest CMF value over the last `window` bars, or None.

    MFM = ((close - low) - (high - close)) / (high - low). If high == low, MFM = 0.
    CMF = sum(MFM * volume) / sum(volume) over the window.
    """
    if len(close) < window:
        return None
    hl = (high - low).astype(float)
    # Per-bar MFM with safe divide (high == low -> 0)
    mfm = pd.Series(0.0, index=close.index)
    nonflat = hl > 0
    mfm.loc[nonflat] = (
        ((close[nonflat] - low[nonflat]) - (high[nonflat] - close[nonflat]))
        / hl[nonflat]
    )
    mfv = mfm * volume.astype(float)
    win_mfv = mfv.iloc[-window:].sum()
    win_vol = volume.iloc[-window:].astype(float).sum()
    if win_vol <= 0:
        return None
    return float(win_mfv / win_vol)


def _macd_lines(close: pd.Series) -> tuple[pd.Series, pd.Series] | None:
    """Return (macd, signal) full Series, or None if not enough data."""
    if len(close) < 26:
        return None
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14) -> float | None:
    """Latest Wilder-style ATR (RMA via EWM alpha=1/window)."""
    if len(close) < window + 1:
        return None
    prev_close = close.shift(1)
    tr = pd.concat(
        [
            (high - low).abs(),
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    # Wilder smoothing: EWM with alpha = 1/window, adjust=False
    atr = tr.ewm(alpha=1.0 / window, adjust=False).mean()
    val = atr.iloc[-1]
    if pd.isna(val):
        return None
    return float(val)


# ---------------------------------------------------------------------------
# Strategy class
# ---------------------------------------------------------------------------

class ChaikinMACDATRStrategy:
    """Chaikin Money Flow bias + MACD cross trigger + ATR geometry."""

    _family = "chaikin_macd_atr"  # routing-table family
    name = "chaikin_macd_atr"

    # Geometry / indicator defaults
    CMF_WINDOW = 20
    ATR_WINDOW = 14
    SL_ATR_MULT = 1.5
    TP_ATR_MULT = 2.5
    MIN_SL_PIPS = 10.0
    MIN_TP_PIPS = 12.0

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.cmf_window = int(config.get("cmf_window", self.CMF_WINDOW))
        self.atr_window = int(config.get("atr_window", self.ATR_WINDOW))
        self.sl_atr_mult = float(config.get("sl_atr_mult", self.SL_ATR_MULT))
        self.tp_atr_mult = float(config.get("tp_atr_mult", self.TP_ATR_MULT))
        self.min_sl_pips = float(config.get("min_sl_pips", self.MIN_SL_PIPS))
        self.min_tp_pips = float(config.get("min_tp_pips", self.MIN_TP_PIPS))
        self.fixed_score = float(config.get("fixed_score", 30))
        log.info(
            "[STRATEGY:chaikin_macd_atr] init enabled=%s cmf_w=%d atr_w=%d "
            "sl_mult=%.2f tp_mult=%.2f",
            self.enabled, self.cmf_window, self.atr_window,
            self.sl_atr_mult, self.tp_atr_mult,
        )

    # ------------------------------------------------------------------
    # StrategyModule Protocol
    # ------------------------------------------------------------------

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        bars = ctx.snapshot.candles.get("5M")
        if bars is None:
            return False
        # MACD needs >=26 bars + 1 for prior-bar diff -> require >=27
        # CMF needs >=20, ATR needs >=15. MACD is the binding constraint.
        min_bars = max(27, self.cmf_window, self.atr_window + 1)
        if len(bars) < min_bars:
            return False
        # Require expected columns
        for col in ("open", "high", "low", "close", "volume"):
            if col not in bars.columns:
                return False
        return True

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        bars = ctx.snapshot.candles.get("5M")
        if bars is None:
            return None

        # Defensive length check (mirror eligible)
        min_bars = max(27, self.cmf_window, self.atr_window + 1)
        if len(bars) < min_bars:
            return None

        try:
            high = bars["high"].astype(float)
            low = bars["low"].astype(float)
            close = bars["close"].astype(float)
            volume = bars["volume"].astype(float)
        except (KeyError, ValueError):
            return None

        # --- CMF bias --------------------------------------------------
        cmf = _chaikin_money_flow(high, low, close, volume, window=self.cmf_window)
        if cmf is None or cmf == 0.0:
            return None

        # --- MACD trigger ---------------------------------------------
        macd_pair = _macd_lines(close)
        if macd_pair is None:
            return None
        macd, signal = macd_pair
        if len(macd) < 2 or pd.isna(macd.iloc[-1]) or pd.isna(signal.iloc[-1]):
            return None
        diff_now = float(macd.iloc[-1] - signal.iloc[-1])
        diff_prev = float(macd.iloc[-2] - signal.iloc[-2])

        bullish_cross = diff_now > 0.0 and diff_prev <= 0.0
        bearish_cross = diff_now < 0.0 and diff_prev >= 0.0

        long_signal = cmf > 0.0 and bullish_cross
        short_signal = cmf < 0.0 and bearish_cross
        if not (long_signal or short_signal):
            return None

        # --- ATR geometry ---------------------------------------------
        atr_val = _atr(high, low, close, window=self.atr_window)
        if atr_val is None or atr_val <= 0:
            return None

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        atr_pips = atr_val / pip

        sl_distance = max(self.sl_atr_mult * atr_val, self.min_sl_pips * pip)
        tp_distance = max(self.tp_atr_mult * atr_val, self.min_tp_pips * pip)

        entry_price = float(close.iloc[-1])

        if long_signal:
            direction = TradeDirection.LONG
            stop_price = entry_price - sl_distance
            take_profit = entry_price + tp_distance
            strategy_name = "CMA_long"
        else:
            direction = TradeDirection.SHORT
            stop_price = entry_price + sl_distance
            take_profit = entry_price - tp_distance
            strategy_name = "CMA_short"

        risk = abs(entry_price - stop_price)
        reward = abs(take_profit - entry_price)
        if risk <= 0:
            return None
        rr = reward / risk

        projected_tp_pips = tp_distance / pip

        log.info(
            "[STRATEGY:chaikin_macd_atr] %s symbol=%s entry=%.5f cmf=%.4f "
            "macd_diff=%.6f atr_pips=%.1f rr=%.2f",
            strategy_name, ctx.symbol, entry_price, cmf,
            diff_now, atr_pips, rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=strategy_name,
            entry_price=entry_price,
            stop_price=stop_price,
            take_profit=take_profit,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "CHAIKIN_MACD_ATR",
                "strategy_family": "chaikin_macd_atr",
                "cmf": cmf,
                "macd_diff": diff_now,
                "macd_diff_prev": diff_prev,
                "atr_pips": atr_pips,
                "atr_value": atr_val,
                "sl_distance": sl_distance,
                "tp_distance": tp_distance,
                "projected_tp_pips": projected_tp_pips,
                "risk_points": risk,
                "reward_points": reward,
                "cmf_window": self.cmf_window,
                "atr_window": self.atr_window,
            },
            created_at=datetime.now(timezone.utc),
        )


__all__ = ["ChaikinMACDATRStrategy"]
