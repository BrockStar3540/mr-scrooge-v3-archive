"""Compression Mean Reversion — band-fade scalper for tight, low-vol regimes.

Fires ONLY when the market is in compression: narrow Bollinger bands, ATR
contracted versus its 50-bar median, and price hugging the midline. When all
three compression conditions hold, fade Bollinger-band touches back to the
SMA midline using rejection-wick confirmation.

This is intentionally a small-target, high-WR style. Natural targets sit in
the 4-8 pip range; the strategy is gated hard to never fire outside
compression.

Emits TradeCandidate with:
  strategy_family = 'compression_reversion'
  strategy (probe_name) = 'CMR_fade_long' | 'CMR_fade_short'
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from statistics import median
from typing import Any

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategy.compression_mean_reversion")


# ---------------------------------------------------------------------------
# Tunables (compression thresholds)
# ---------------------------------------------------------------------------

# Bollinger band width as % of SMA midline. Compression requires bands to be
# tighter than this fraction.
BB_WIDTH_PCT_MAX = 0.003

# Price distance from SMA midline as % of SMA. Compression requires price
# riding near the midline (weak directional structure).
MIDLINE_DIST_PCT_MAX = 0.001

# Window for the ATR contraction comparison.
ATR_MEDIAN_LOOKBACK = 50

# Bars needed for a stable computation (ATR_14 + 50-bar median + some slack).
MIN_BARS = 70

# Rejection wick threshold — long bar needs lower wick > 50% of bar range
# (and analogous for short / upper wick).
WICK_PCT_MIN = 0.50

# Stop placement past the BB extreme, in pips.
STOP_BUFFER_PIPS = 2.5

# Minimum TP distance from entry, in pips (floor if midline-distance is tiny).
MIN_TP_PIPS = 8.0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _pip(symbol: str) -> float:
    return 0.01 if "JPY" in symbol else 0.0001


def _atr_pips_series(highs, lows, closes, period: int, pip: float) -> list[float]:
    """Compute simple rolling ATR (Wilder-style SMA of true range) in pips.

    Returns a list of length len(closes); positions before enough data are
    filled with 0.0. Lightweight — we only need recent values for a median.
    """
    n = len(closes)
    if n == 0:
        return []
    trs: list[float] = [0.0] * n
    for i in range(1, n):
        h = float(highs[i])
        l = float(lows[i])
        prev_c = float(closes[i - 1])
        tr = max(h - l, abs(h - prev_c), abs(l - prev_c))
        trs[i] = tr
    atrs: list[float] = [0.0] * n
    if n < period + 1:
        return atrs
    # First ATR = simple average of first `period` TRs (skipping index 0).
    first = sum(trs[1 : period + 1]) / period
    atrs[period] = first / pip
    prev = first
    for i in range(period + 1, n):
        cur = (prev * (period - 1) + trs[i]) / period
        atrs[i] = cur / pip
        prev = cur
    return atrs


# ---------------------------------------------------------------------------
# Strategy
# ---------------------------------------------------------------------------

class CompressionMeanReversionStrategy:
    """Mean-reversion band fade gated by hard compression criteria.

    Implements the V3 StrategyModule shape (eligible / evaluate). Returns
    None outside compression — never trades trend.
    """

    _family = "compression_reversion"  # routing-table family (matches lab matrix)
    name = "compression_mean_reversion"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.bb_width_pct_max = config.get("bb_width_pct_max", BB_WIDTH_PCT_MAX)
        self.midline_dist_pct_max = config.get(
            "midline_dist_pct_max", MIDLINE_DIST_PCT_MAX
        )
        self.atr_median_lookback = int(
            config.get("atr_median_lookback", ATR_MEDIAN_LOOKBACK)
        )
        self.wick_pct_min = config.get("wick_pct_min", WICK_PCT_MIN)
        self.stop_buffer_pips = config.get("stop_buffer_pips", STOP_BUFFER_PIPS)
        self.min_tp_pips = config.get("min_tp_pips", MIN_TP_PIPS)
        self.fixed_score = config.get("fixed_score", 28)
        self.min_rr = config.get("min_rr", 0.5)  # mean-reversion: low RR is OK
        log.info(
            "[STRATEGY:compression_mean_reversion] init enabled=%s "
            "bb_width_max=%.4f midline_max=%.4f wick_min=%.2f",
            self.enabled,
            self.bb_width_pct_max,
            self.midline_dist_pct_max,
            self.wick_pct_min,
        )

    # ------------------------------------------------------------------
    # Eligibility — cheap pre-flight gate
    # ------------------------------------------------------------------
    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        boll = ctx.features.get("bollinger")
        if boll is None:
            return False
        bars = ctx.snapshot.candles.get("5M")
        if bars is None:
            return False
        try:
            n = len(bars)
        except TypeError:
            return False
        if n < MIN_BARS:
            return False
        return True

    # ------------------------------------------------------------------
    # Evaluate — full compression check + entry trigger
    # ------------------------------------------------------------------
    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        boll = ctx.features.get("bollinger")
        bars = ctx.snapshot.candles.get("5M")
        if boll is None or bars is None:
            return None
        try:
            n = len(bars)
        except TypeError:
            return None
        if n < MIN_BARS:
            return None

        v = boll.values or {}
        upper_a = float(v.get("upper_a", 0.0) or 0.0)
        lower_a = float(v.get("lower_a", 0.0) or 0.0)
        sma_a = float(v.get("sma_a", 0.0) or 0.0)
        if sma_a <= 0.0 or upper_a <= 0.0 or lower_a <= 0.0:
            return None
        if upper_a <= lower_a:
            return None

        # Pull OHLC arrays (DataFrame, lowercase cols).
        try:
            closes = bars["close"].astype(float).values
            highs = bars["high"].astype(float).values
            lows = bars["low"].astype(float).values
            opens = bars["open"].astype(float).values
        except Exception as exc:  # pragma: no cover - defensive
            log.debug(
                "[STRATEGY:compression_mean_reversion] OHLC pull failed: %s", exc
            )
            return None

        if len(closes) < MIN_BARS:
            return None

        pip = _pip(ctx.symbol)
        current_close = float(closes[-1])
        current_high = float(highs[-1])
        current_low = float(lows[-1])
        current_open = float(opens[-1])

        # --------------------------------------------------------------
        # COMPRESSION GATE — ALL conditions must hold.
        # --------------------------------------------------------------
        bb_width_pct = (upper_a - lower_a) / sma_a
        if bb_width_pct >= self.bb_width_pct_max:
            return None

        midline_dist_pct = abs(current_close - sma_a) / sma_a
        if midline_dist_pct >= self.midline_dist_pct_max:
            return None

        # ATR contraction: current ATR_14 below median of last `lookback` ATRs.
        atr_series = _atr_pips_series(highs, lows, closes, 14, pip)
        # Trim leading zeros (warm-up) before taking median.
        recent_atrs = [
            a for a in atr_series[-self.atr_median_lookback :] if a > 0.0
        ]
        if len(recent_atrs) < max(10, self.atr_median_lookback // 2):
            return None
        atr_current = atr_series[-1]
        if atr_current <= 0.0:
            return None
        atr_median = median(recent_atrs)
        if atr_current >= atr_median:
            return None

        # --------------------------------------------------------------
        # ENTRY TRIGGER — pick a side based on which band was touched.
        # --------------------------------------------------------------
        bar_range = current_high - current_low
        if bar_range <= 0.0:
            return None

        direction: TradeDirection | None = None
        strategy_name: str = ""
        body_high = max(current_open, current_close)
        body_low = min(current_open, current_close)

        # LONG fade: close touches/crosses lower band, lower wick dominates.
        if current_close <= lower_a:
            lower_wick = body_low - current_low
            lower_wick_pct = lower_wick / bar_range
            if lower_wick_pct > self.wick_pct_min:
                direction = TradeDirection.LONG
                strategy_name = "CMR_fade_long"

        # SHORT fade: close touches/crosses upper band, upper wick dominates.
        if direction is None and current_close >= upper_a:
            upper_wick = current_high - body_high
            upper_wick_pct = upper_wick / bar_range
            if upper_wick_pct > self.wick_pct_min:
                direction = TradeDirection.SHORT
                strategy_name = "CMR_fade_short"

        if direction is None:
            return None

        # --------------------------------------------------------------
        # Stop, TP, RR
        # --------------------------------------------------------------
        buffer = self.stop_buffer_pips * pip
        min_tp_dist = self.min_tp_pips * pip

        if direction == TradeDirection.LONG:
            stop_price = lower_a - buffer
            midline_dist = sma_a - current_close
            tp_dist = max(midline_dist, min_tp_dist)
            take_profit = current_close + tp_dist
        else:
            stop_price = upper_a + buffer
            midline_dist = current_close - sma_a
            tp_dist = max(midline_dist, min_tp_dist)
            take_profit = current_close - tp_dist

        risk = abs(current_close - stop_price)
        reward = abs(take_profit - current_close)
        if risk <= 0.0 or reward <= 0.0:
            return None
        rr = reward / risk
        if rr < self.min_rr:
            return None

        projected_tp_pips = reward / pip
        midline_distance_pips = abs(current_close - sma_a) / pip

        metadata: dict[str, Any] = {
            "entry_type": "COMPRESSION_MEAN_REVERSION",
            "strategy_family": "compression_reversion",
            "management_profile": "scalper_fade",
            "projected_tp_pips": projected_tp_pips,
            "compression_bb_width": bb_width_pct,
            "compression_atr": atr_current,
            "compression_atr_median": atr_median,
            "midline_distance_pips": midline_distance_pips,
            "sma_a": sma_a,
            "upper_a": upper_a,
            "lower_a": lower_a,
            "wick_pct": (
                (body_low - current_low) / bar_range
                if direction == TradeDirection.LONG
                else (current_high - body_high) / bar_range
            ),
            "risk_points": risk,
            "reward_points": reward,
        }

        log.info(
            "[STRATEGY:compression_mean_reversion] %s symbol=%s dir=%s "
            "close=%.5f bb_w=%.5f atr=%.2f atr_med=%.2f midline_pips=%.2f "
            "tp_pips=%.2f rr=%.2f",
            strategy_name,
            ctx.symbol,
            direction.value,
            current_close,
            bb_width_pct,
            atr_current,
            atr_median,
            midline_distance_pips,
            projected_tp_pips,
            rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=strategy_name,
            entry_price=current_close,
            stop_price=stop_price,
            take_profit=take_profit,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata=metadata,
            created_at=datetime.now(timezone.utc),
        )


__all__ = ["CompressionMeanReversionStrategy"]
