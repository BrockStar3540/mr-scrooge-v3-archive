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
