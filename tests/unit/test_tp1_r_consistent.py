"""Phase 3 — Bug G: TP1 at the same R-multiple across all pair families."""

from __future__ import annotations

import pytest

from scrooge_v3.core.trade_geometry import (
    compute_tp1,
    initial_risk,
    price_distance_to_r,
)


# (symbol, entry, stop, direction) — covers JPY base / JPY cross / USD quote / cross
PAIR_SETUPS = [
    ("USD_JPY", 152.340, 152.526, "short"),   # R = 18.6 pips
    ("AUD_JPY", 113.651, 113.912, "short"),   # R = 26.1 pips
    ("NZD_JPY", 93.264, 92.936, "long"),      # R = 32.8 pips
    ("AUD_USD", 0.71546, 0.71510, "long"),    # R = 3.6 pips
    ("EUR_USD", 1.08200, 1.08150, "long"),    # R = 5.0 pips
    ("GBP_CHF", 1.12000, 1.12500, "short"),   # R = 50 pips (non-JPY cross)
]


@pytest.mark.parametrize("symbol,entry,stop,direction", PAIR_SETUPS)
def test_tp1_r_is_exactly_one_by_default(symbol, entry, stop, direction):
    """Unified TP1 formula always places TP1 at exactly 1R regardless of pair."""
    tp1 = compute_tp1(entry, stop, direction, tp1_r=1.0)
    r_dist = initial_risk(entry, stop)
    tp1_dist = abs(tp1 - entry)
    r_mult = price_distance_to_r(tp1_dist, r_dist)
    assert r_mult == pytest.approx(1.0, abs=1e-6), (
        f"{symbol}: TP1 at {r_mult:.4f}R, expected 1.0"
    )


@pytest.mark.parametrize("symbol,entry,stop,direction", PAIR_SETUPS)
@pytest.mark.parametrize("tp1_r", [0.5, 1.0, 1.5, 2.0])
def test_tp1_r_consistent_across_pairs(symbol, entry, stop, direction, tp1_r):
    """For any tp1_r, every pair gets TP1 at that exact R-multiple."""
    tp1 = compute_tp1(entry, stop, direction, tp1_r=tp1_r)
    r_dist = initial_risk(entry, stop)
    tp1_dist = abs(tp1 - entry)
    r_mult = price_distance_to_r(tp1_dist, r_dist)
    assert r_mult == pytest.approx(tp1_r, abs=1e-6)


def test_tp1_direction_correct():
    """Long TP1 above entry, short TP1 below entry."""
    tp1_long = compute_tp1(1.1000, 1.0950, "long", tp1_r=1.0)
    assert tp1_long > 1.1000
    tp1_short = compute_tp1(113.651, 113.912, "short", tp1_r=1.0)
    assert tp1_short < 113.651
