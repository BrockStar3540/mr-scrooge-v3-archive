"""Hotfix regression — harvest LIMIT lifecycle safety.

60-day OANDA broker-truth audit (2026-04-29) found 8 cases of harvest LIMIT
orders surviving parent close and later firing as naked positions with no
SL/TP. Three guards land in this hotfix:

  1. Every harvest LIMIT placed with a strategy-bounded GTD (4h direct/box,
     12h dbb_trend) — last-resort broker-side ceiling.
  2. Cancellation on every parent-close path via reconcile_tracker (vanish).
  3. Periodic orphan sweep using a persisted harvest ledger so that any
     pending REDUCE_ONLY LIMIT whose parent trade is gone gets cancelled
     even if the tracker pointer was lost.

These tests cover the three guards using the same fake-broker style as
test_state_truth.py.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from scrooge_v3.execution.position_tracker import PositionTracker
from scrooge_v3.market.broker import PendingOrderInfo, TradeInfo
from scrooge_v3.services import state_recovery as sr_mod
from scrooge_v3.services.state_recovery import StateRecovery


# ---------- Fakes ----------

class _FakeBroker:
    def __init__(self, open_trades=None, pending=None):
        self._open = list(open_trades or [])
        self._pending = list(pending or [])
        self.cancelled: list[str] = []
        self.placed: list[dict] = []

    def get_open_trades(self):
        return list(self._open)

    def get_pending_orders(self):
        return list(self._pending)

    def cancel_order(self, order_id):
        self.cancelled.append(order_id)
        self._pending = [o for o in self._pending if o.order_id != order_id]
        return True

    def place_limit_order(self, **kw):
        self.placed.append(kw)
        order_id = f"ORD_{len(self.placed)}"
        self._pending.append(PendingOrderInfo(
            order_id=order_id, symbol=kw["symbol"], order_type="LIMIT",
            units=abs(kw["units"]), price=kw["price"],
            state="PENDING", time_in_force="GTD",
            gtd_time=kw.get("gtd_time", ""),
        ))
        return SimpleNamespace(success=True, order_id=order_id,
                               trade_id=None, error="")

    def close_trade(self, trade_id, units=None):
        return SimpleNamespace(success=False, error="not_used_in_test")


class _FakeAudit:
    def __init__(self):
        self.events: list[dict] = []

    def record(self, ev):
        self.events.append(ev.to_dict())


class _FakeConfig:
    def section(self, name):
        return {}


def _ctx(broker, tracker, audit=None):
    return SimpleNamespace(
        broker=broker,
        tracker=tracker,
        execution_audit=audit,
        config=_FakeConfig(),
        state=SimpleNamespace(
            decrement_positions=lambda: None,
            position_count=0,
            record_zone_entry=lambda *a, **kw: None,
        ),
        known_trade_ids=set(),
    )


@pytest.fixture(autouse=True)
def _isolated_ledger(tmp_path, monkeypatch):
    """Each test gets its own ledger file; reset module-global instance."""
    ledger_path = tmp_path / "harvest-order-ledger.json"
    monkeypatch.setattr(sr_mod, "_HARVEST_LEDGER_PATH", ledger_path)
    monkeypatch.setattr(sr_mod, "_HARVEST_LEDGER", sr_mod.HarvestLedger(ledger_path))
    yield


# ---------- Test 1: parent close cancels harvest LIMIT ----------

def test_parent_close_cancels_harvest_limit(tmp_path):
    """Parent vanishes from broker (SL hit / manual close / full TP) ->
    reconcile_tracker MUST cancel the outstanding harvest LIMIT."""
    pp = tmp_path / "tracker.json"
    tracker = PositionTracker(persist_path=pp)
    tracker.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5, strategy="direct",
    )
    tracker.set_harvest_order("T1", "ORD_HARVEST")

    # Broker reports zero open trades (parent closed externally) but the
    # harvest LIMIT is still sitting there pending.
    broker = _FakeBroker(
        open_trades=[],
        pending=[PendingOrderInfo(
            order_id="ORD_HARVEST", symbol="USD_JPY", order_type="LIMIT",
            units=5000, price=150.5, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
        )],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_tracker()

    assert "ORD_HARVEST" in broker.cancelled, \
        f"expected harvest cancel, got cancelled={broker.cancelled}"
    assert tracker.get("T1") is None  # vanished
    types = [e["type"] for e in audit.events]
    assert "harvest_limit_cancelled" in types


# ---------- Test 2: harvest LIMIT carries strategy-bounded GTD ----------

def test_harvest_limit_carries_gtd(tmp_path):
    """_place_harvest_limit MUST include a non-empty GTD timestamp on the
    outbound order request, with hours bounded by strategy holding profile.
    """
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T1", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5, strategy="dbb_trend",
    )
    broker = _FakeBroker()
    recovery = StateRecovery(_ctx(broker, tracker, audit=_FakeAudit()))

    recovery._place_harvest_limit(tracker.get("T1"))

    assert broker.placed, "expected place_limit_order call"
    call = broker.placed[0]
    assert call["position_fill"] == "REDUCE_ONLY"
    assert call["gtd_time"], "harvest LIMIT must carry a GTD"
    # dbb_trend gets 12h, direct/box get 4h. Spot-check by switching strategy.
    assert call["gtd_time"].endswith("Z")  # OANDA RFC3339

    tracker2 = PositionTracker(persist_path=None)
    tracker2.register_entry(
        trade_id="T2", symbol="EUR_USD", direction="short",
        units=10000, entry_price=1.10, stop_price=1.105,
        tp1_price=1.095, strategy="direct",
    )
    broker2 = _FakeBroker()
    recovery2 = StateRecovery(_ctx(broker2, tracker2, audit=_FakeAudit()))
    recovery2._place_harvest_limit(tracker2.get("T2"))
    direct_gtd = broker2.placed[0]["gtd_time"]
    dbb_gtd = call["gtd_time"]
    # dbb_trend window (12h) is strictly later than direct (4h).
    assert dbb_gtd > direct_gtd, \
        f"expected dbb_trend GTD > direct GTD; got dbb={dbb_gtd} direct={direct_gtd}"


# ---------- Test 3: orphan sweep cancels stale harvest LIMITs ----------

def test_orphan_sweep_cancels_harvest_with_no_parent(tmp_path):
    """Broker reports a pending harvest LIMIT whose parent trade is absent
    from both the broker's open trades AND the tracker. The orphan sweep
    MUST cancel it and emit the expected audit events."""
    tracker = PositionTracker(persist_path=None)
    # Seed the persisted ledger directly to simulate a harvest placed in
    # a previous run/cycle whose tracker entry has since been lost.
    sr_mod._HARVEST_LEDGER.add(
        order_id="ORD_GHOST", trade_id="T_LOST", symbol="GBP_USD",
        strategy="direct",
        gtd_time="2026-12-31T00:00:00.000000000Z",
    )
    broker = _FakeBroker(
        open_trades=[],
        pending=[PendingOrderInfo(
            order_id="ORD_GHOST", symbol="GBP_USD", order_type="LIMIT",
            units=5000, price=1.25, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
        )],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_orphan_harvests()

    assert "ORD_GHOST" in broker.cancelled
    types = [e["type"] for e in audit.events]
    assert "orphan_harvest_limit_found" in types
    assert "orphan_harvest_limit_cancelled" in types
    # Ledger cleaned up.
    assert "ORD_GHOST" not in sr_mod._HARVEST_LEDGER.all()


def test_orphan_sweep_leaves_live_harvest_alone(tmp_path):
    """Sanity counter-test: a harvest LIMIT whose parent trade is still
    alive on the broker MUST NOT be touched by the orphan sweep."""
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T_LIVE", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5, strategy="direct",
    )
    tracker.set_harvest_order("T_LIVE", "ORD_LIVE")
    sr_mod._HARVEST_LEDGER.add(
        order_id="ORD_LIVE", trade_id="T_LIVE", symbol="USD_JPY",
        strategy="direct",
        gtd_time="2026-12-31T00:00:00.000000000Z",
    )
    broker = _FakeBroker(
        open_trades=[TradeInfo(
            trade_id="T_LIVE", symbol="USD_JPY", direction="long",
            units=10000, entry_price=150.0,
        )],
        pending=[PendingOrderInfo(
            order_id="ORD_LIVE", symbol="USD_JPY", order_type="LIMIT",
            units=5000, price=150.5, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
        )],
    )
    recovery = StateRecovery(_ctx(broker, tracker, audit=_FakeAudit()))
    recovery.reconcile_orphan_harvests()
    assert broker.cancelled == []
