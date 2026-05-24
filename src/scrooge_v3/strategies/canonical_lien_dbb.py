"""Canonical Lien Double Bollinger Band — zone-entry trend continuation probe.

Per Kathy Lien, the Double Bollinger Band continuation signal fires when price
has broken outside the 2σ outer band, then pulls back but holds above (long) /
below (short) the BB midline, and prints a confirmation candle.

Emits TradeCandidate with:
  family = 'dbb_trend'
  strategy_id (probe_name) = 'canonical_lien_dbb_long' or 'canonical_lien_dbb_short'

Both probes default DISABLED. Enable via:
  strategies.probes_v2.canonical_lien_dbb_long.enabled = true
  strategies.probes_v2.canonical_lien_dbb_short.enabled = true

Registers into the shared PROBE_REGISTRY from probes_v2 at import time.
Bootstrap must import this module before calling build_all_probe_strategies
if you want these included in the main probe sweep; OR use
build_all_lien_dbb_probes() for a separate registration block.
"""
from __future__ import annotations

import logging

from scrooge_v3.strategies.probes_v2 import (
    PROBE_REGISTRY,
    ProbeContext,
    ProbeStrategy,
    _build_candidate_multi,
    _is_bull_bar,
)

log = logging.getLogger("scrooge_v3.strategy.canonical_lien_dbb")


# ---------------------------------------------------------------------------
# Probe functions
# ---------------------------------------------------------------------------

def probe_canonical_lien_dbb_long(ctx: ProbeContext):
    """Long: price broke above upper_a (2σ), pulled back, holds above midline."""
    f = ctx.features
    bb_pos   = f.get("bb_position")
    bb_upper = f.get("bb_upper")
    bb_lower = f.get("bb_lower")
    atr_pips = f.get("atr_pips")
    rsi      = f.get("rsi")
    if None in (bb_pos, bb_upper, bb_lower, atr_pips, rsi):
        return None
    if len(ctx.m5_high) < 5:
        return None
    # Prior 3 bars (excluding current) must have touched/broken the upper 2σ band
    if max(ctx.m5_high[-4:-1]) <= bb_upper:
        return None
    # Current close: pulled back but still above midline (bb_position 0.5–1.0)
    if not (0.5 < bb_pos < 1.0):
        return None
    # Continuation candle: bullish bar
    if not _is_bull_bar(ctx):
        return None
    # RSI must not be overbought
    if rsi >= 68:
        return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-5:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "canonical_lien_dbb_long",
        {"rsi": rsi, "bb_position": bb_pos},
    )


def probe_canonical_lien_dbb_short(ctx: ProbeContext):
    """Short: price broke below lower_a (2σ), pulled back, holds below midline."""
    f = ctx.features
    bb_pos   = f.get("bb_position")
    bb_upper = f.get("bb_upper")
    bb_lower = f.get("bb_lower")
    atr_pips = f.get("atr_pips")
    rsi      = f.get("rsi")
    if None in (bb_pos, bb_upper, bb_lower, atr_pips, rsi):
        return None
    if len(ctx.m5_low) < 5:
        return None
    # Prior 3 bars must have touched/broken the lower 2σ band
    if min(ctx.m5_low[-4:-1]) >= bb_lower:
        return None
    # Current close: pulled back but still below midline (bb_position 0.0–0.5)
    if not (0.0 < bb_pos < 0.5):
        return None
    # Continuation candle: bearish bar
    if _is_bull_bar(ctx):
        return None
    # RSI must not be oversold
    if rsi <= 32:
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-5:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "canonical_lien_dbb_short",
        {"rsi": rsi, "bb_position": bb_pos},
    )


# ---------------------------------------------------------------------------
# Register into shared PROBE_REGISTRY (side-effectful at import time)
# ---------------------------------------------------------------------------

PROBE_REGISTRY["canonical_lien_dbb_long"] = {
    "fn":       probe_canonical_lien_dbb_long,
    "family":   "dbb_trend",
    "sentinel": "Charlie",
    "target":   2.0,
}
PROBE_REGISTRY["canonical_lien_dbb_short"] = {
    "fn":       probe_canonical_lien_dbb_short,
    "family":   "dbb_trend",
    "sentinel": "Charlie",
    "target":   2.0,
}

# ---------------------------------------------------------------------------
# Public exports
# ---------------------------------------------------------------------------

_LIEN_DBB_NAMES = ["canonical_lien_dbb_long", "canonical_lien_dbb_short"]

# Pre-built list (disabled by default) — used by boot test and bootstrap.
LIEN_DBB_PROBES: list[ProbeStrategy] = [
    ProbeStrategy(name, {}) for name in _LIEN_DBB_NAMES
]


def build_all_lien_dbb_probes(config: dict | None = None) -> list[ProbeStrategy]:
    """Return ProbeStrategy instances for both Lien DBB probes.

    config shape (same section as probes_v2):
      config["canonical_lien_dbb_long"]  = {"enabled": bool, "r_target": float}
      config["canonical_lien_dbb_short"] = {"enabled": bool, "r_target": float}
    Missing entries → disabled.
    """
    cfg = config or {}
    return [ProbeStrategy(name, cfg.get(name, {})) for name in _LIEN_DBB_NAMES]


__all__ = ["LIEN_DBB_PROBES", "build_all_lien_dbb_probes"]

# ============================================================================
# CanonicalLienDBBStrategy — class-based router-reachable module
# ============================================================================
# Added 2026-05-24 to fix v1.12_FULL DBB cells being unreachable.
#
# Three-layer naming break that this module fixes:
#   1. router (strategy_router.py) allows family "canonical_lien_dbb"
#   2. probe-based version above registers as "canonical_lien_dbb_long/_short"
#      → scan_pipeline gate `entry.name not in allowed` filters them out
#   3. v1.12_FULL routing-table rows use strategy={DBB1,DBB2,DBB3}_*
#      → 2 probes can't represent 6 variants
#
# This class registers with name="canonical_lien_dbb" (matches router allowed),
# iterates 6 variants strictest-first, emits candidate.strategy=variant_name
# (matches parquet DBB1/DBB2/DBB3 strategy field), and lets entry_filter_gate
# resolve the routing-table row via exact (pair × regime × dir × session ×
# strategy) match. The probe-based code above is left in place (enabled=0,
# harmless coexistence).

from datetime import datetime, timezone

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection


_ELIGIBLE_STATES = ("NORMAL", "COMPRESSION", "STRETCH_UP", "STRETCH_DOWN")

# Variants list (strictest-first iteration). Each variant: name, direction, mode.
# mode ∈ {basic, confirmed, sustained}
DEFAULT_DBB_VARIANTS = [
    # DBB3: most-restrictive (sustained 2-bar zone hold)
    {"name": "DBB3_buy_zone_sustained_long",   "direction": "long",  "mode": "sustained"},
    {"name": "DBB3_sell_zone_sustained_short", "direction": "short", "mode": "sustained"},
    # DBB2: zone + EMA20 slope confirmation
    {"name": "DBB2_buy_zone_confirmed_long",   "direction": "long",  "mode": "confirmed"},
    {"name": "DBB2_sell_zone_confirmed_short", "direction": "short", "mode": "confirmed"},
    # DBB1: basic zone entry (loosest)
    {"name": "DBB1_buy_zone_long",             "direction": "long",  "mode": "basic"},
    {"name": "DBB1_sell_zone_short",           "direction": "short", "mode": "basic"},
]


class CanonicalLienDBBStrategy:
    """Canonical Kathy Lien Double Bollinger Band — zone-entry continuation.

    Implements StrategyModule Protocol. Router allows family
    "canonical_lien_dbb"; this class registers under that name. Iterates
    DEFAULT_DBB_VARIANTS strictest-first; first match wins. Emits
    candidate.strategy=variant_name so entry_filter_gate can match the
    specific DBB1/DBB2/DBB3 routing-table row.
    """

    name = "canonical_lien_dbb"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.min_rr = config.get("min_rr", 1.1)
        self.stop_buffer_pips = config.get("stop_buffer_pips", 2)
        self.fixed_score = config.get("fixed_score", 32)
        self.ema_slope_lookback = config.get("ema_slope_lookback", 5)
        self.variants = config.get("variants", DEFAULT_DBB_VARIANTS)
        log.info(
            "[STRATEGY:canonical_lien_dbb] init enabled=%s variants=%d",
            self.enabled, len(self.variants),
        )

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        bb = ctx.classifications.get("bb_state")
        if bb is None or bb.label not in _ELIGIBLE_STATES:
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
        boll = ctx.features.get("bollinger")
        bars = ctx.snapshot.candles.get("5M")
        if boll is None or bars is None or len(bars) < 25:
            return None

        v = boll.values
        upper_a = v.get("upper_a", 0.0)
        lower_a = v.get("lower_a", 0.0)
        sma_a   = v.get("sma_a",   0.0)

        # Derive 1σ bands from existing 2σ bands (sma_a + 1*std == midpoint of
        # sma_a and 2σ band)
        upper_1sd = sma_a + (upper_a - sma_a) / 2.0
        lower_1sd = sma_a - (sma_a - lower_a) / 2.0

        closes = bars["close"].astype(float).values
        highs  = bars["high"].astype(float).values
        lows   = bars["low"].astype(float).values

        if len(closes) < 25:
            return None

        current_close = closes[-1]
        prev_close    = closes[-2]
        current_high  = highs[-1]
        current_low   = lows[-1]
        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        buffer = self.stop_buffer_pips * pip

        for variant in self.variants:
            direction_str = variant["direction"]
            mode = variant["mode"]
            direction = TradeDirection.LONG if direction_str == "long" else TradeDirection.SHORT

            # Zone check (1σ to midline)
            if direction == TradeDirection.LONG:
                in_zone_now  = (sma_a <= current_close <= upper_1sd)
                in_zone_prev = (sma_a <= prev_close   <= upper_1sd)
            else:
                in_zone_now  = (lower_1sd <= current_close <= sma_a)
                in_zone_prev = (lower_1sd <= prev_close   <= sma_a)

            if not in_zone_now:
                continue

            # Mode-specific gates
            if mode == "sustained":
                if not in_zone_prev:
                    continue
            elif mode == "confirmed":
                if not self._ema20_slope_ok(closes, direction):
                    continue

            # Build candidate
            if direction == TradeDirection.LONG:
                stop_price = min(current_low, lower_1sd) - buffer
                target_distance = upper_a - current_close
                tp1 = current_close + max(target_distance * 0.5, 12 * pip)
                tp2 = current_close + max(target_distance, 24 * pip)
            else:
                stop_price = max(current_high, upper_1sd) + buffer
                target_distance = current_close - lower_a
                tp1 = current_close - max(target_distance * 0.5, 12 * pip)
                tp2 = current_close - max(target_distance, 24 * pip)

            risk = abs(current_close - stop_price)
            reward = abs(tp2 - current_close)
            if risk <= 0:
                continue
            rr = reward / risk
            if rr < self.min_rr:
                continue

            log.info(
                "[STRATEGY:canonical_lien_dbb] %s symbol=%s dir=%s close=%.5f rr=%.2f",
                variant["name"], ctx.symbol, direction.value, current_close, rr,
            )

            return TradeCandidate(
                symbol=ctx.symbol,
                direction=direction,
                strategy=variant["name"],   # ← key: emits DBB1/DBB2/DBB3 name for parquet match
                entry_price=current_close,
                stop_price=stop_price,
                take_profit=tp2,
                size=0.0,
                risk_reward=rr,
                score=self.fixed_score,
                metadata={
                    "entry_type": "CANONICAL_LIEN_DBB",
                    "strategy_family": "canonical_lien_dbb",
                    "management_profile": "trend_runner",
                    "variant_name": variant["name"],
                    "mode": mode,
                    "zone_upper": upper_1sd if direction == TradeDirection.LONG else sma_a,
                    "zone_lower": sma_a     if direction == TradeDirection.LONG else lower_1sd,
                    "sma_a": sma_a,
                    "upper_a": upper_a,
                    "lower_a": lower_a,
                    "tp1": tp1,
                    "tp2": tp2,
                    "risk_points": risk,
                    "reward_points": reward,
                },
                created_at=datetime.now(timezone.utc),
            )

        return None

    def _ema20_slope_ok(self, closes, direction: TradeDirection) -> bool:
        import pandas as pd
        if len(closes) < 20 + self.ema_slope_lookback:
            return False
        s = pd.Series(closes).ewm(span=20, adjust=False).mean().values
        slope = s[-1] - s[-self.ema_slope_lookback]
        if direction == TradeDirection.LONG:
            return slope > 0
        return slope < 0
