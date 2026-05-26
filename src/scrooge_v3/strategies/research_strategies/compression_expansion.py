"""Compression-to-Expansion Breakout — research strategy.

Identifies periods of low volatility (compression) using a composite score
of BB width percentile, ATR percentile, and recent range percentile over
a rolling window of M5 bars. Fires only when the *current* bar shows
clear expansion (range >> recent median range) AND the *prior* window was
in compression. Direction follows the expansion bar.

Strategy family: ``compression_expansion``
Strategy names emitted:
  - ``CE_break_long``
  - ``CE_break_short``

Default DISABLED. Intended for research / shadow scoring only — register
manually via the strategy router config when enabling.

Author: Mr Scrooge V3 research strategies
Created: 2026-05-26
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategy.compression_expansion")


# ---------------------------------------------------------------------------
# Tunables
# ---------------------------------------------------------------------------

DEFAULTS = {
    "enabled": False,
    # Window over which we measure the "compression" distribution.
    "compression_window": 30,
    # Number of recent bars (excluding current) that must score as compressed.
    "compression_lookback": 15,
    # A bar is "compressed" when its composite score is at/above this percentile
    # rank within the rolling compression_window.
    "compression_percentile": 0.80,
    # Expansion trigger: current bar range >= expansion_mult * median(range, N).
    "expansion_lookback": 10,
    "expansion_mult": 1.5,
    # Stop placement buffer (in pips).
    "stop_buffer_pips": 2.0,
    # Floor on take-profit distance, in pips.
    "min_tp_pips": 12.0,
    # Minimum risk:reward.
    "min_rr": 1.0,
    # Static score; real ranking is via the v3/v4 scorer downstream.
    "fixed_score": 28.0,
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _percentile_rank(value: float, series) -> float:
    """Return percentile rank of ``value`` within ``series`` in [0.0, 1.0].

    Low rank => value is small relative to the series. Used so the raw
    metric (bb_width / atr / range) maps to "compression score" via 1-rank.
    """
    n = len(series)
    if n == 0:
        return 0.5
    count_le = 0
    for v in series:
        if v <= value:
            count_le += 1
    return count_le / n


def _median(values) -> float:
    n = len(values)
    if n == 0:
        return 0.0
    s = sorted(values)
    mid = n // 2
    if n % 2 == 1:
        return float(s[mid])
    return float((s[mid - 1] + s[mid]) / 2.0)


# ---------------------------------------------------------------------------
# Strategy
# ---------------------------------------------------------------------------

class CompressionExpansionStrategy:
    """Compression-to-Expansion Breakout.

    Implements StrategyModule protocol:
      - ``eligible(ctx) -> bool``
      - ``evaluate(ctx) -> TradeCandidate | None``
    """

    name = "compression_expansion"

    def __init__(self, config: dict | None = None):
        cfg = {**DEFAULTS, **(config or {})}
        self.enabled = bool(cfg["enabled"])
        self.compression_window = int(cfg["compression_window"])
        self.compression_lookback = int(cfg["compression_lookback"])
        self.compression_percentile = float(cfg["compression_percentile"])
        self.expansion_lookback = int(cfg["expansion_lookback"])
        self.expansion_mult = float(cfg["expansion_mult"])
        self.stop_buffer_pips = float(cfg["stop_buffer_pips"])
        self.min_tp_pips = float(cfg["min_tp_pips"])
        self.min_rr = float(cfg["min_rr"])
        self.fixed_score = float(cfg["fixed_score"])
        # Minimum total bars: bb_period (20) + window + small headroom.
        self._min_bars = 20 + self.compression_window + 2
        log.info(
            "[STRATEGY:compression_expansion] init enabled=%s window=%d "
            "lookback=%d pct=%.2f exp_mult=%.2f",
            self.enabled, self.compression_window, self.compression_lookback,
            self.compression_percentile, self.expansion_mult,
        )

    # ------------------------------------------------------------------ eligibility

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        # Need a regime that is not explicitly blocked.
        reg = ctx.classifications.get("regime")
        if reg is not None and reg.label == "BLOCKED":
            return False
        # Need Bollinger feature (sanity check; we recompute per-bar).
        if ctx.features.get("bollinger") is None:
            return False
        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < self._min_bars:
            return False
        return True

    # ------------------------------------------------------------------ evaluate

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < self._min_bars:
            return None

        try:
            opens = bars["open"].astype(float).values
            highs = bars["high"].astype(float).values
            lows = bars["low"].astype(float).values
            closes = bars["close"].astype(float).values
        except Exception as exc:  # noqa: BLE001
            log.debug("[compression_expansion] bars unpack failed: %s", exc)
            return None

        n = len(closes)
        if n < self._min_bars:
            return None

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001

        # ------------------------------------------------------------------
        # Build per-bar metrics for the rolling compression_window.
        # ------------------------------------------------------------------
        win = self.compression_window
        bb_period = 20
        if n < bb_period + win:
            return None

        bar_metrics = []  # list[(bb_width, atr_proxy, bar_range)]
        for i in range(n - win, n):
            window_closes = closes[i - bb_period + 1: i + 1]
            mean = float(window_closes.mean())
            var = float(((window_closes - mean) ** 2).mean())  # population std
            std = var ** 0.5
            bb_width = 4.0 * std  # upper(+2 sigma) - lower(-2 sigma)
            tr = float(highs[i] - lows[i])
            bar_metrics.append((bb_width, tr, tr))

        if len(bar_metrics) < win:
            return None

        bb_widths = [m[0] for m in bar_metrics]
        atrs = [m[1] for m in bar_metrics]
        ranges_w = [m[2] for m in bar_metrics]

        # Per-bar composite compression score: average of (1 - percentile_rank)
        # for each of the three metrics. Higher => more compressed.
        compression_scores = []
        for i in range(win):
            bbw = bar_metrics[i][0]
            atr = bar_metrics[i][1]
            rng = bar_metrics[i][2]
            r_bb = _percentile_rank(bbw, bb_widths)
            r_atr = _percentile_rank(atr, atrs)
            r_rng = _percentile_rank(rng, ranges_w)
            score = ((1.0 - r_bb) + (1.0 - r_atr) + (1.0 - r_rng)) / 3.0
            compression_scores.append(score)

        # ------------------------------------------------------------------
        # Compression check: prior `compression_lookback` bars (excluding the
        # current bar) should mostly score >= compression_percentile.
        # ------------------------------------------------------------------
        lb = self.compression_lookback
        if lb > win - 1:
            lb = win - 1
        prior_scores = compression_scores[-1 - lb:-1]  # exclude current
        if len(prior_scores) == 0:
            return None
        compressed_count = sum(
            1 for s in prior_scores if s >= self.compression_percentile
        )
        compressed_frac = compressed_count / len(prior_scores)
        if compressed_frac < 0.60:
            return None

        # ------------------------------------------------------------------
        # Expansion trigger: current bar range >= mult * median(range, N).
        # ------------------------------------------------------------------
        exp_lb = self.expansion_lookback
        if exp_lb >= n:
            exp_lb = n - 1
        recent_ranges = [
            float(highs[i] - lows[i]) for i in range(n - 1 - exp_lb, n - 1)
        ]
        if len(recent_ranges) == 0:
            return None
        med_range = _median(recent_ranges)
        cur_range = float(highs[-1] - lows[-1])
        if med_range <= 0 or cur_range < self.expansion_mult * med_range:
            return None

        # ------------------------------------------------------------------
        # Direction: align across body sign AND vs prior close.
        # ------------------------------------------------------------------
        cur_open = float(opens[-1])
        cur_close = float(closes[-1])
        prev_close = float(closes[-2])

        is_bull = (cur_close > cur_open) and (cur_close > prev_close)
        is_bear = (cur_close < cur_open) and (cur_close < prev_close)
        if not (is_bull or is_bear):
            return None

        direction = TradeDirection.LONG if is_bull else TradeDirection.SHORT

        # Compression range = envelope of prior compressed bars (excl. current)
        comp_high = float(max(highs[n - 1 - lb: n - 1]))
        comp_low = float(min(lows[n - 1 - lb: n - 1]))
        comp_range = comp_high - comp_low
        if comp_range <= 0:
            return None

        # ------------------------------------------------------------------
        # Entry / stop / target. Default = signal entry at current close.
        # ------------------------------------------------------------------
        entry_price = cur_close
        buffer = self.stop_buffer_pips * pip
        min_tp_dist = self.min_tp_pips * pip

        if direction == TradeDirection.LONG:
            stop_price = comp_low - buffer
            tp_dist = max(comp_range, min_tp_dist)
            take_profit = entry_price + tp_dist
        else:
            stop_price = comp_high + buffer
            tp_dist = max(comp_range, min_tp_dist)
            take_profit = entry_price - tp_dist

        risk = abs(entry_price - stop_price)
        reward = abs(take_profit - entry_price)
        if risk <= 0:
            return None
        rr = reward / risk
        if rr < self.min_rr:
            return None

        # ------------------------------------------------------------------
        # Current-bar percentile metrics — required metadata for factor work.
        # ------------------------------------------------------------------
        cur_bbw = bar_metrics[-1][0]
        cur_atr = bar_metrics[-1][1]
        cur_rng = bar_metrics[-1][2]
        bb_width_pct = _percentile_rank(cur_bbw, bb_widths)
        atr_pct = _percentile_rank(cur_atr, atrs)
        range_pct = _percentile_rank(cur_rng, ranges_w)

        strategy_name = (
            "CE_break_long" if direction == TradeDirection.LONG else "CE_break_short"
        )

        log.info(
            "[STRATEGY:compression_expansion] FIRE %s symbol=%s dir=%s entry=%.5f "
            "stop=%.5f tp=%.5f rr=%.2f comp_frac=%.2f exp_ratio=%.2f",
            strategy_name, ctx.symbol, direction.value,
            entry_price, stop_price, take_profit, rr,
            compressed_frac, (cur_range / med_range if med_range > 0 else 0.0),
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
                "entry_type": "COMPRESSION_EXPANSION_BREAK",
                "strategy_family": "compression_expansion",
                "management_profile": "breakout_runner",
                # Required factor-analysis fields:
                "projected_tp_pips": tp_dist / pip,
                "bb_width_pct": bb_width_pct,
                "atr_pct": atr_pct,
                "range_pct": range_pct,
                # Diagnostics:
                "compressed_frac": compressed_frac,
                "compression_percentile_threshold": self.compression_percentile,
                "compression_window": self.compression_window,
                "compression_lookback": lb,
                "expansion_mult_used": (
                    (cur_range / med_range) if med_range > 0 else 0.0
                ),
                "expansion_mult_required": self.expansion_mult,
                "comp_high": comp_high,
                "comp_low": comp_low,
                "comp_range_pips": comp_range / pip,
                "current_range_pips": cur_range / pip,
                "median_range_pips": med_range / pip,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )


__all__ = ["CompressionExpansionStrategy", "DEFAULTS"]
