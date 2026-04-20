"""Bug 2 regression — double-harvest race between pre-placed limit and pipeline."""

from types import SimpleNamespace

import pytest

from scrooge_v3.core.position_pipeline import PositionPipeline
from scrooge_v3.execution.position_tracker import PositionTracker


class FakeHarvestManager:
    def check_harvest(self, pos_id, direction, current_price, tp1, tp1_taken):
        if tp1_taken:
            return None
        return SimpleNamespace(close_fraction=0.5, target_label="TP1")


def _tracker():
    return PositionTracker(persist_path=None)


def test_harvest_guard_skips_when_broker_shows_reduction():
    """8273 units opened, limit for 4136 filled at broker (4137 remaining).
    Pipeline must NOT emit harvest; must mark tp1_taken via tracker."""
    tracker = _tracker()
    tracker.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="short",
        units=8273, entry_price=159.181, stop_price=159.367,
        tp1_price=159.08,
    )
    pos = tracker.get("T1")
    assert pos.original_units == 8273

    pipeline = PositionPipeline(harvest_manager=FakeHarvestManager())
    action = pipeline.manage_position(
        pos, current_price=159.08, bid=159.08, ask=159.082, spread=0.002,
        live_units=4137, tracker=tracker,
    )
    assert action.action != "harvest"
    assert pos.tp1_taken is True


def test_harvest_skipped_when_limit_pending():
    tracker = _tracker()
    tracker.register_entry(
        trade_id="T2", symbol="USD_JPY", direction="short",
        units=8273, entry_price=159.181, stop_price=159.367,
        tp1_price=159.08,
    )
    tracker.set_harvest_order("T2", "ORDER_ABC")
    pos = tracker.get("T2")

    pipeline = PositionPipeline(harvest_manager=FakeHarvestManager())
    action = pipeline.manage_position(
        pos, current_price=159.08, bid=159.08, ask=159.082, spread=0.002,
        live_units=8273, tracker=tracker,
    )
    assert action.action != "harvest"
    assert pos.tp1_taken is False


def test_harvest_fires_when_no_limit_and_no_reduction():
    tracker = _tracker()
    tracker.register_entry(
        trade_id="T3", symbol="USD_JPY", direction="short",
        units=8273, entry_price=159.181, stop_price=159.367,
        tp1_price=159.08,
    )
    pos = tracker.get("T3")

    pipeline = PositionPipeline(harvest_manager=FakeHarvestManager())
    action = pipeline.manage_position(
        pos, current_price=159.08, bid=159.08, ask=159.082, spread=0.002,
        live_units=8273, tracker=tracker,
    )
    assert action.action == "harvest"
