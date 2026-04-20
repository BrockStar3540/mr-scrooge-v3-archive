"""Bug 4 regression — profit_r uses initial_risk_distance, not dynamic SL."""

import pytest

from scrooge_v3.core.position_pipeline import PositionPipeline
from scrooge_v3.execution.position_tracker import PositionTracker


def test_initial_risk_distance_snapshotted_at_register():
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T5", symbol="EUR_USD", direction="long",
        units=100000, entry_price=1.0800, stop_price=1.0750,
    )
    pos = tracker.get("T5")
    assert pos.initial_risk_distance == pytest.approx(0.005, rel=1e-4)
    tracker.update_stop("T5", 1.0790)
    assert pos.initial_risk_distance == pytest.approx(0.005, rel=1e-4)


def test_profit_r_uses_initial_risk_after_be_move():
    """Scenario from production log: entry=159.181, SL=159.367 (risk=0.186).
    After BE moves SL to 159.171 and price is at 159.10:
      OLD bug: profit_r = (159.181-159.10) / (159.181-159.171) = 8.1 (wrong)
      FIX:    profit_r = (159.181-159.10) / 0.186 ≈ 0.435."""
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T4", symbol="USD_JPY", direction="short",
        units=8273, entry_price=159.181, stop_price=159.367,
        tp1_price=159.08,
    )
    pos = tracker.get("T4")
    tracker.update_stop("T4", 159.171)  # BE move

    pipeline = PositionPipeline(
        exit_config={"early_hold_threshold_r": 0.5, "lock_threshold_r": 0.8}
    )
    action = pipeline.manage_position(
        pos, current_price=159.10, bid=159.10, ask=159.102, spread=0.002,
        live_units=8273, tracker=tracker,
    )
    profit_r = action.details["profit_r"]
    assert profit_r == pytest.approx(0.435, abs=0.02), f"profit_r={profit_r}"
    assert action.details["phase"] != "HARVEST"


def test_profit_r_correct_before_any_stop_move():
    """Before any stop move, initial_risk == current risk; profit_r identical."""
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T6", symbol="USD_JPY", direction="short",
        units=1000, entry_price=159.181, stop_price=159.367,
    )
    pos = tracker.get("T6")
    pipeline = PositionPipeline(exit_config={})
    action = pipeline.manage_position(
        pos, current_price=159.088, bid=159.088, ask=159.09, spread=0.002,
        live_units=1000, tracker=tracker,
    )
    # profit_distance = 0.093, risk = 0.186 -> 0.5
    assert action.details["profit_r"] == pytest.approx(0.5, abs=0.01)
