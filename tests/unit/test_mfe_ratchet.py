"""Phase 3 — Bug I: peak-tracked ratchet keeps locks across retracement."""

from __future__ import annotations

from scrooge_v3.core.types import TradeDirection
from scrooge_v3.management.ratchet import RatchetManager


def test_peak_anchored_lock_survives_retracement_long():
    """Spike to +3R, retrace to +1.5R. Peak-anchored lock > entry-anchored."""
    ratchet = RatchetManager({
        "ratchet_trigger_r": 1.0,
        "ratchet_trigger_min_pips": 3.0,
        "ratchet_lock_pct": 0.5,
    })
    entry, sl = 1.1000, 1.0950
    R = 0.005
    peak = 1.1150  # +3R
    retrace = 1.1075  # +1.5R
    current_stop = entry

    plan_peak = ratchet.compute_ratchet_stop(
        TradeDirection.LONG, entry, retrace, current_stop, pip_size=0.0001,
        initial_risk_distance=R, peak_price=peak,
    )
    plan_entry = ratchet.compute_ratchet_stop(
        TradeDirection.LONG, entry, retrace, current_stop, pip_size=0.0001,
        initial_risk_distance=R, peak_price=0.0,
    )

    assert plan_peak is not None
    assert plan_entry is not None
    # Peak-anchored: lock 50% of 0.015 = 0.0075 -> stop 1.1075
    # Entry-anchored: lock 50% of 0.0075 = 0.00375 -> stop 1.10375
    assert plan_peak.new_stop > plan_entry.new_stop
    assert plan_peak.new_stop == pytest.approx(1.1075, abs=1e-6)
    assert plan_entry.new_stop == pytest.approx(1.10375, abs=1e-6)


def test_peak_anchored_lock_short():
    """Short: peak is lowest price. Spike to -3R, retrace to -1.5R."""
    ratchet = RatchetManager({
        "ratchet_trigger_r": 1.0,
        "ratchet_trigger_min_pips": 3.0,
        "ratchet_lock_pct": 0.5,
    })
    entry, sl = 113.651, 113.912
    R = 0.261
    peak = 112.868  # -3R from entry
    retrace = 113.260  # ~-1.5R
    current_stop = 113.912

    plan_peak = ratchet.compute_ratchet_stop(
        TradeDirection.SHORT, entry, retrace, current_stop, pip_size=0.01,
        initial_risk_distance=R, peak_price=peak,
    )
    plan_entry = ratchet.compute_ratchet_stop(
        TradeDirection.SHORT, entry, retrace, current_stop, pip_size=0.01,
        initial_risk_distance=R, peak_price=0.0,
    )

    assert plan_peak is not None
    assert plan_entry is not None
    # For a short, tighter = smaller number (lower stop price).
    assert plan_peak.new_stop < plan_entry.new_stop


def test_peak_tracker_updates_on_new_high():
    """PositionTracker.update_peak moves monotonically in favorable direction."""
    from pathlib import Path
    import tempfile

    from scrooge_v3.execution.position_tracker import PositionTracker

    with tempfile.TemporaryDirectory() as tmp:
        tracker = PositionTracker(persist_path=Path(tmp) / "state.json")
        tracker.register_entry(
            trade_id="T1", symbol="EUR_USD", direction="long",
            units=1000, entry_price=1.1000, stop_price=1.0950,
        )
        pos = tracker.get("T1")
        assert pos.peak_price == 1.1000  # bootstraps to entry

        # Move up
        assert tracker.update_peak("T1", 1.1030) is True
        assert tracker.get("T1").peak_price == 1.1030

        # Retrace — no update
        assert tracker.update_peak("T1", 1.1020) is False
        assert tracker.get("T1").peak_price == 1.1030

        # New high
        assert tracker.update_peak("T1", 1.1050) is True
        assert tracker.get("T1").peak_price == 1.1050


def test_peak_tracker_short_direction():
    """For shorts, peak is the LOWEST price reached."""
    from pathlib import Path
    import tempfile

    from scrooge_v3.execution.position_tracker import PositionTracker

    with tempfile.TemporaryDirectory() as tmp:
        tracker = PositionTracker(persist_path=Path(tmp) / "s.json")
        tracker.register_entry(
            trade_id="T1", symbol="AUD_JPY", direction="short",
            units=1000, entry_price=113.651, stop_price=113.912,
        )
        # Initial peak is entry
        assert tracker.get("T1").peak_price == 113.651

        # Move down (favorable for short)
        assert tracker.update_peak("T1", 113.500) is True
        assert tracker.get("T1").peak_price == 113.500

        # Rally (unfavorable) — no update
        assert tracker.update_peak("T1", 113.600) is False
        assert tracker.get("T1").peak_price == 113.500


import pytest  # noqa: E402
