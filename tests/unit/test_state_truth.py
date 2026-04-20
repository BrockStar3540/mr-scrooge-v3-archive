"""Phase 2 — State Truth regression tests.

Covers:
  Bug A: tracker flag persistence across restarts
  Bug B: tracker units synced to broker truth after partial closes
  Bug C: dust residuals flattened after partial
  Bug D: pending-entry dicts are per-instance, not class-scoped
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from scrooge_v3.core.position_pipeline import PositionPipeline
from scrooge_v3.execution.position_tracker import PositionTracker
from scrooge_v3.market.broker import TradeInfo
from scrooge_v3.services.state_recovery import StateRecovery


# ---------- Fakes ----------

class _FakeHarvestManager:
    def check_harvest(self, pos_id, direction, current_price, tp1, tp1_taken):
        if tp1_taken:
            return None
        return SimpleNamespace(close_fraction=0.5, target_label="TP1")


class _FakeBroker:
    def __init__(self, open_trades=None, pending=None):
        self._open = list(open_trades or [])
        self._pending = list(pending or [])
        self.closed: list[tuple[str, float | None]] = []

    def get_open_trades(self):
        return list(self._open)

    def get_pending_orders(self):
        return list(self._pending)

    def close_trade(self, trade_id, units=None):
        self.closed.append((trade_id, units))
        for t in list(self._open):
            if t.trade_id == trade_id:
                if units is None or units >= t.units:
                    self._open.remove(t)
                else:
                    t.units -= units
                return SimpleNamespace(success=True, fill_price=1.0,
                                        realized_pl=0.0, trade_id=trade_id, error="")
        return SimpleNamespace(success=False, fill_price=0.0,
                               realized_pl=0.0, trade_id="", error="not_found")

    def cancel_order(self, order_id):
        return True

    def place_limit_order(self, **kw):
        return SimpleNamespace(success=True, order_id="ORD1", trade_id=None, error="")


class _FakeConfig:
    def __init__(self, mgmt=None):
        self._mgmt = mgmt or {}

    def section(self, name):
        if name == "management":
            return dict(self._mgmt)
        return {}


def _ctx(broker, tracker, mgmt=None):
    return SimpleNamespace(
        broker=broker,
        tracker=tracker,
        config=_FakeConfig(mgmt),
        state=SimpleNamespace(
            decrement_positions=lambda: None,
            position_count=0,
            record_zone_entry=lambda *a, **kw: None,
        ),
        known_trade_ids=set(),
    )


# ---------- Bug A: flag persistence ----------

def test_mark_tp1_taken_persists(tmp_path):
    pp = tmp_path / "tracker.json"
    t1 = PositionTracker(persist_path=pp)
    t1.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
    )
    t1.mark_tp1_taken("T1")

    t2 = PositionTracker(persist_path=pp)
    t2.restore()
    assert t2.get("T1").tp1_taken is True


def test_mark_break_even_persists(tmp_path):
    pp = tmp_path / "tracker.json"
    t1 = PositionTracker(persist_path=pp)
    t1.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
    )
    t1.mark_break_even("T1")

    t2 = PositionTracker(persist_path=pp)
    t2.restore()
    assert t2.get("T1").break_even_achieved is True


# ---------- Bug B: tracker units sync ----------

def test_update_units(tmp_path):
    pp = tmp_path / "tracker.json"
    t1 = PositionTracker(persist_path=pp)
    t1.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
    )
    t1.update_units("T1", 5000)

    t2 = PositionTracker(persist_path=pp)
    t2.restore()
    assert t2.get("T1").units == 5000
    # original_units snapshot must remain for profit_r math
    assert t2.get("T1").original_units == 10000


def test_partial_harvest_updates_units(tmp_path):
    """Limit harvest fills -> reconcile must sync units AND mark tp1_taken."""
    pp = tmp_path / "tracker.json"
    tracker = PositionTracker(persist_path=pp)
    tracker.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5,
    )
    tracker.set_harvest_order("T1", "ORD_HARVEST")

    broker_trade = TradeInfo(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=5000, entry_price=150.0,
    )
    broker = _FakeBroker(open_trades=[broker_trade], pending=[])
    recovery = StateRecovery(_ctx(broker, tracker))
    recovery.reconcile_pending_orders()

    assert tracker.get("T1").units == 5000
    assert tracker.get("T1").tp1_taken is True
    assert tracker.get("T1").harvest_order_id == ""


def test_no_double_harvest_after_partial_fill():
    """Phase 1 harvest-guard must still hold with Phase 2 units-truth changes."""
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="short",
        units=10000, entry_price=150.0, stop_price=150.5,
        tp1_price=149.5,
    )
    pos = tracker.get("T1")

    pipeline = PositionPipeline(harvest_manager=_FakeHarvestManager())
    action = pipeline.manage_position(
        pos, current_price=149.5, bid=149.5, ask=149.502, spread=0.002,
        live_units=5000, tracker=tracker,
    )
    assert action.action != "harvest"
    assert pos.tp1_taken is True


# ---------- Bug D: per-instance pending dicts ----------

def test_pending_entries_not_class_scope():
    t1 = PositionTracker(persist_path=None)
    t2 = PositionTracker(persist_path=None)
    t1.register_pending_entry("USD_JPY", "ORD_A")
    t1.set_pending_entry_meta("USD_JPY", {"tp1_price": 150.5})

    assert t1.get_pending_entry("USD_JPY") == "ORD_A"
    assert t2.get_pending_entry("USD_JPY") is None
    assert t2.get_pending_entry_meta("USD_JPY") == {}


# ---------- Bug C: dust flatten ----------

def test_dust_flatten():
    """After partial harvest, residual <= threshold triggers market flatten."""
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=3, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5,
    )
    tracker.set_harvest_order("T1", "ORD_HARVEST")

    broker_trade = TradeInfo(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=1, entry_price=150.0,
    )
    broker = _FakeBroker(open_trades=[broker_trade], pending=[])
    recovery = StateRecovery(_ctx(broker, tracker, mgmt={"dust_unit_threshold": 2}))
    recovery.reconcile_pending_orders()

    dust_closes = [c for c in broker.closed if c[0] == "T1" and c[1] is None]
    assert dust_closes, f"expected dust flatten, got closes={broker.closed}"
    assert tracker.get("T1").tp1_taken is True


def test_dust_threshold_not_triggered_above_limit():
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5,
    )
    tracker.set_harvest_order("T1", "ORD_HARVEST")

    broker_trade = TradeInfo(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=5000, entry_price=150.0,
    )
    broker = _FakeBroker(open_trades=[broker_trade], pending=[])
    recovery = StateRecovery(_ctx(broker, tracker, mgmt={"dust_unit_threshold": 2}))
    recovery.reconcile_pending_orders()

    assert broker.closed == []
    assert tracker.get("T1").units == 5000
    assert tracker.get("T1").tp1_taken is True
