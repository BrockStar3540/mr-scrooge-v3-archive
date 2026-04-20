"""Phase 3 — Bug H: R-relative BE and ratchet thresholds with pip floors.

The old fixed-pip thresholds fired at wildly different R-multiples
depending on stop width. Live trades:

  AUD/USD R=3.6 pips: be_trigger_pips=5 never fires (needs 1.4R profit).
  USD/JPY R=18 pips: be_trigger_pips=5 fires at 0.27R — clips ratchets.

New behavior: threshold = max(r * R, min_pips * pip_size).
"""

from __future__ import annotations

import pytest

from scrooge_v3.core.types import TradeDirection
from scrooge_v3.management.be_manager import BreakEvenManager
from scrooge_v3.management.ratchet import RatchetManager


@pytest.fixture
def be_default():
    """Defaults mirror config/default.json post-Phase-3."""
    return BreakEvenManager({
        "be_trigger_r": 0.5,
        "be_trigger_min_pips": 2.0,
        "be_offset_r": 0.1,
        "be_offset_min_pips": 1.0,
    })


@pytest.fixture
def ratchet_default():
    return RatchetManager({
        "ratchet_trigger_r": 1.0,
        "ratchet_trigger_min_pips": 3.0,
        "ratchet_lock_pct": 0.5,
    })


class TestBreakEvenRRelative:
    def test_be_fires_at_half_R_on_wide_stop_usdjpy(self, be_default):
        """USD/JPY R=18.6 pips. 0.5R = 9.3 pips. Max(9.3, 2) = 9.3 pips."""
        entry, sl = 152.340, 152.526  # short; R=0.186
        R = 0.186
        # At 0.49R favorable: should NOT fire
        current = entry - (0.49 * R)
        plan = be_default.should_move_to_be(
            TradeDirection.SHORT, entry, current, sl, pip_size=0.01,
            initial_risk_distance=R,
        )
        assert plan is None, "should not fire below 0.5R"

        # At 0.51R favorable: should fire
        current = entry - (0.51 * R)
        plan = be_default.should_move_to_be(
            TradeDirection.SHORT, entry, current, sl, pip_size=0.01,
            initial_risk_distance=R,
        )
        assert plan is not None
        # Offset = max(0.1R, 1 pip) = max(1.86, 1.0) = 1.86 pips = 0.0186
        # BE stop = 152.340 - 0.0186 = 152.3214
        assert plan.new_stop == pytest.approx(entry - 0.0186, abs=1e-6)

    def test_be_fires_on_tight_audusd_via_pip_floor(self, be_default):
        """AUD/USD R=3.6 pips. 0.5R=1.8 pips, floor=2.0 pips. Effective=2.0 pips."""
        entry, sl = 0.71546, 0.71510  # long; R=0.00036
        R = 0.00036
        # At 1.5 pips favorable — below 2.0 pip floor
        current = entry + 1.5 * 0.0001
        plan = be_default.should_move_to_be(
            TradeDirection.LONG, entry, current, sl, pip_size=0.0001,
            initial_risk_distance=R,
        )
        assert plan is None

        # At 2.5 pips favorable — above floor
        current = entry + 2.5 * 0.0001
        plan = be_default.should_move_to_be(
            TradeDirection.LONG, entry, current, sl, pip_size=0.0001,
            initial_risk_distance=R,
        )
        assert plan is not None
        # Offset = max(0.1R, 1 pip) = max(0.036 pip, 1 pip) = 1 pip
        # BE = 0.71546 + 0.0001 = 0.71556
        assert plan.new_stop == pytest.approx(0.71556, abs=1e-6)

    def test_be_offset_respects_min_pip_floor_jpy(self, be_default):
        """AUD/JPY R=26.1 pips short. 0.1R = 2.61 pips, floor=1 pip => 2.61 pips."""
        entry, sl = 113.651, 113.912
        R = 0.261
        # Far into profit — guaranteed fire
        current = 113.000
        plan = be_default.should_move_to_be(
            TradeDirection.SHORT, entry, current, sl, pip_size=0.01,
            initial_risk_distance=R,
        )
        assert plan is not None
        # Offset = max(0.1 * 0.261, 1.0 * 0.01) = max(0.0261, 0.01) = 0.0261
        # BE = 113.651 - 0.0261 = 113.6249
        assert plan.new_stop == pytest.approx(113.6249, abs=1e-6)

    def test_be_partial_taken_fires_at_any_profit(self, be_default):
        """Partial-taken bypasses the trigger threshold."""
        entry, sl = 1.1000, 1.0950
        R = 0.005
        # Only 0.1R favorable — below 0.5R trigger
        current = entry + 0.1 * R
        plan = be_default.should_move_to_be(
            TradeDirection.LONG, entry, current, sl, pip_size=0.0001,
            partial_taken=True, initial_risk_distance=R,
        )
        assert plan is not None

    def test_be_never_loosens(self, be_default):
        """If current_stop already at/above BE, return None."""
        entry, sl = 1.1000, 1.0950
        R = 0.005
        current = entry + 1.0 * R  # well past trigger
        # Current stop already above BE target
        current_stop = entry + 0.0005
        plan = be_default.should_move_to_be(
            TradeDirection.LONG, entry, current, current_stop, pip_size=0.0001,
            initial_risk_distance=R,
        )
        assert plan is None

    def test_legacy_config_migrated(self):
        """Legacy be_trigger_pips still honored as min-pips floor."""
        be = BreakEvenManager({"be_trigger_pips": 10.0, "be_offset_pips": 2.0})
        assert be.trigger_min_pips == 10.0
        assert be.offset_min_pips == 2.0


class TestRatchetRRelative:
    def test_ratchet_fires_at_1R_on_wide_jpy(self, ratchet_default):
        """USD/JPY R=18.6 pips. 1R = 18.6 pips, floor=3 pips. Effective=18.6."""
        entry, sl = 152.340, 152.526  # short; R=0.186
        R = 0.186
        current_stop = 152.340
        # 0.9R favorable — below trigger
        current = entry - 0.9 * R
        plan = ratchet_default.compute_ratchet_stop(
            TradeDirection.SHORT, entry, current, current_stop, pip_size=0.01,
            initial_risk_distance=R,
        )
        assert plan is None
        # 1.1R favorable — above trigger
        current = entry - 1.1 * R
        plan = ratchet_default.compute_ratchet_stop(
            TradeDirection.SHORT, entry, current, current_stop, pip_size=0.01,
            initial_risk_distance=R,
        )
        assert plan is not None

    def test_ratchet_fires_on_tight_audusd_via_floor(self, ratchet_default):
        """AUD/USD R=3.6 pips. 1R=3.6 pips, floor=3 pips. Effective=3.6 pips."""
        entry, sl = 0.71546, 0.71510  # long; R=0.00036
        R = 0.00036
        current_stop = entry
        # 3 pips favorable — below 3.6 (1R)
        current = entry + 3.0 * 0.0001
        plan = ratchet_default.compute_ratchet_stop(
            TradeDirection.LONG, entry, current, current_stop, pip_size=0.0001,
            initial_risk_distance=R,
        )
        assert plan is None
        # 4 pips favorable — above
        current = entry + 4.0 * 0.0001
        plan = ratchet_default.compute_ratchet_stop(
            TradeDirection.LONG, entry, current, current_stop, pip_size=0.0001,
            initial_risk_distance=R,
        )
        assert plan is not None
