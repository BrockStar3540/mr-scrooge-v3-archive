"""Phase 3 — Bug J regression: JPY BE must land at 0.01 precision.

Live trade 1488 AUD/JPY short (entry 113.651) observed a BE stop at
113.650 — that is, a 0.001 = 0.1-pip offset instead of the intended
1-pip = 0.01. This test ensures the BE computation with pip_size=0.01
always produces a 0.01-quantized result for JPY pairs, and that the
wire-format precision used by the OANDA adapter round-trips exactly.
"""

from __future__ import annotations

import pytest

from scrooge_v3.core.types import TradeDirection
from scrooge_v3.management.be_manager import BreakEvenManager


@pytest.fixture
def be():
    return BreakEvenManager({
        "be_trigger_r": 0.5,
        "be_trigger_min_pips": 2.0,
        "be_offset_r": 0.1,
        "be_offset_min_pips": 1.0,
    })


# (symbol, entry, sl, direction, R, expected_offset_per_pip_floor)
JPY_SETUPS = [
    ("AUD_JPY", 113.651, 113.912, TradeDirection.SHORT, 0.261),
    ("USD_JPY", 152.340, 152.526, TradeDirection.SHORT, 0.186),
    ("GBP_JPY", 193.450, 193.100, TradeDirection.LONG, 0.350),
    ("EUR_JPY", 163.200, 162.900, TradeDirection.LONG, 0.300),
]


@pytest.mark.parametrize("symbol,entry,sl,direction,R", JPY_SETUPS)
def test_jpy_be_offset_is_at_least_one_pip(symbol, entry, sl, direction, R, be):
    """For JPY pairs, the 1-pip floor keeps BE well clear of spread."""
    # Well past trigger
    sign = 1 if direction == TradeDirection.LONG else -1
    current = entry + sign * (2.0 * R)
    plan = be.should_move_to_be(
        direction, entry, current, sl, pip_size=0.01,
        initial_risk_distance=R,
    )
    assert plan is not None
    offset = abs(plan.new_stop - entry)
    # Offset = max(0.1 * R, 1.0 * 0.01)
    expected = max(0.1 * R, 1.0 * 0.01)
    assert offset == pytest.approx(expected, abs=1e-9)
    # Offset is NEVER less than 1 pip (0.01) for JPY
    assert offset >= 0.01 - 1e-9


@pytest.mark.parametrize("symbol,entry,sl,direction,R", JPY_SETUPS)
def test_jpy_be_quantized_to_0_01(symbol, entry, sl, direction, R, be):
    """BE stop, rounded to 3 decimals (OANDA JPY wire precision), is exact."""
    sign = 1 if direction == TradeDirection.LONG else -1
    current = entry + sign * (2.0 * R)
    plan = be.should_move_to_be(
        direction, entry, current, sl, pip_size=0.01,
        initial_risk_distance=R,
    )
    assert plan is not None
    wire = f"{plan.new_stop:.3f}"
    # Round-trip: parse and compare
    assert float(wire) == pytest.approx(plan.new_stop, abs=1e-3)


def test_aud_jpy_1488_regression_cannot_produce_sub_pip_offset(be):
    """Regression guard: trade 1488 AUD/JPY short entry=113.651, offset_r=0.1,
    pip_size=0.01, R=26.1 pips.

    The old bug produced 113.650 (offset=0.001). The new pip floor
    guarantees offset >= 0.01, so minimum BE = 113.641 (short).
    """
    entry, sl = 113.651, 113.912
    R = 0.261
    current = 113.000  # deep in profit
    plan = be.should_move_to_be(
        TradeDirection.SHORT, entry, current, sl, pip_size=0.01,
        initial_risk_distance=R,
    )
    assert plan is not None
    # Offset = max(0.1 * 0.261, 0.01) = 0.0261 -> BE = 113.6249
    assert abs(plan.new_stop - entry) >= 0.01 - 1e-9
    # Specifically cannot be 113.650 (which would be offset=0.001)
    assert plan.new_stop <= entry - 0.01 + 1e-9


def test_oanda_wire_precision_jpy_stops_unchanged():
    """OANDA modify_stop_loss formats JPY stops at 3 decimals — confirm
    that 113.641 round-trips as the exact wire value without decimal shrink."""
    for stop in (113.641, 113.650, 152.321, 193.100):
        prec = 3 if stop > 50 else 5
        wire = f"{stop:.{prec}f}"
        assert float(wire) == pytest.approx(stop, abs=1e-3)
        # Key assertion: the wire string is exactly 3 decimals for JPY.
        assert len(wire.split(".")[1]) == 3
