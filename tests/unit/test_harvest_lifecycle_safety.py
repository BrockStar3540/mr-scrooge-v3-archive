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
            order_id="ORD_GHOST", symbol="GBP_USD", order_type="LIMIT_ORDER",
            units=5000, price=1.25, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
            parent_trade_id="T_LOST", position_fill="REDUCE_ONLY",
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
            order_id="ORD_LIVE", symbol="USD_JPY", order_type="LIMIT_ORDER",
            units=5000, price=150.5, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
            parent_trade_id="T_LIVE", position_fill="REDUCE_ONLY",
        )],
    )
    recovery = StateRecovery(_ctx(broker, tracker, audit=_FakeAudit()))
    recovery.reconcile_orphan_harvests()
    assert broker.cancelled == []


# ---------- Hotfix/orphan-sweep-broker-walk: 5 new tests ----------

def test_broker_walk_catches_orphan_with_empty_ledger():
    """Pre-deploy orphan: broker reports a REDUCE_ONLY LIMIT with parent
    trade dead on broker AND ledger empty AND tracker empty. The new
    broker-first walk MUST cancel + emit both audit events even though the
    ledger has no record of this order."""
    tracker = PositionTracker(persist_path=None)
    # Ledger is empty (autouse fixture _isolated_ledger gives us a fresh one).
    assert sr_mod._HARVEST_LEDGER.all() == {}
    broker = _FakeBroker(
        open_trades=[],
        pending=[PendingOrderInfo(
            order_id="ORD_PRE", symbol="EUR_USD", order_type="LIMIT_ORDER",
            units=5000, price=1.10, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
            parent_trade_id="T_DEAD", position_fill="REDUCE_ONLY",
        )],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_orphan_harvests()

    assert "ORD_PRE" in broker.cancelled, \
        f"expected ORD_PRE cancelled, got {broker.cancelled}"
    types = [e["type"] for e in audit.events]
    assert "orphan_harvest_limit_found" in types
    assert "orphan_harvest_limit_cancelled" in types


def test_broker_walk_does_not_cancel_entry_limit():
    """CRITICAL SAFETY: an entry LIMIT (positionFill=DEFAULT, no parent
    trade) must never be cancelled by the orphan sweep, even if it looks
    'unparented'."""
    tracker = PositionTracker(persist_path=None)
    broker = _FakeBroker(
        open_trades=[],
        pending=[PendingOrderInfo(
            order_id="ORD_ENTRY", symbol="USD_CAD", order_type="LIMIT_ORDER",
            units=10000, price=1.35, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
            parent_trade_id="",  # entry LIMITs have no parent
            position_fill="DEFAULT",
        )],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_orphan_harvests()

    assert broker.cancelled == [], \
        f"entry LIMIT must NEVER be cancelled by orphan sweep; got {broker.cancelled}"
    types = [e["type"] for e in audit.events]
    assert "orphan_harvest_limit_cancelled" not in types


def test_broker_walk_does_not_cancel_sl_or_tp_orders():
    """CRITICAL SAFETY: STOP_LOSS_ORDER and TAKE_PROFIT_ORDER types must be
    skipped even if their parent trade looks gone."""
    tracker = PositionTracker(persist_path=None)
    broker = _FakeBroker(
        open_trades=[],
        pending=[
            PendingOrderInfo(
                order_id="ORD_SL", symbol="AUD_USD", order_type="STOP_LOSS_ORDER",
                units=10000, price=0.65, state="PENDING",
                time_in_force="GTC",
                parent_trade_id="T_GONE", position_fill="REDUCE_ONLY",
            ),
            PendingOrderInfo(
                order_id="ORD_TP", symbol="AUD_USD", order_type="TAKE_PROFIT_ORDER",
                units=10000, price=0.70, state="PENDING",
                time_in_force="GTC",
                parent_trade_id="T_GONE", position_fill="REDUCE_ONLY",
            ),
        ],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_orphan_harvests()

    assert broker.cancelled == [], \
        f"SL/TP orders must NEVER be cancelled by orphan sweep; got {broker.cancelled}"


def test_broker_walk_respects_live_parent_on_broker():
    """Parent trade is alive on broker (not in tracker). Sweep must skip
    -- the harvest is legitimate."""
    tracker = PositionTracker(persist_path=None)
    broker = _FakeBroker(
        open_trades=[TradeInfo(
            trade_id="T_BROKER_LIVE", symbol="GBP_JPY",
            direction="long", units=10000, entry_price=190.0,
        )],
        pending=[PendingOrderInfo(
            order_id="ORD_HARV", symbol="GBP_JPY", order_type="LIMIT_ORDER",
            units=5000, price=191.0, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
            parent_trade_id="T_BROKER_LIVE", position_fill="REDUCE_ONLY",
        )],
    )
    recovery = StateRecovery(_ctx(broker, tracker, audit=_FakeAudit()))

    recovery.reconcile_orphan_harvests()

    assert broker.cancelled == []


def test_broker_walk_respects_live_tracker_entry():
    """Parent absent from broker open trades but present in tracker. Sweep
    must skip -- tracker is the V3 source of truth for in-flight trades."""
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T_TRACKED", symbol="NZD_USD", direction="short",
        units=10000, entry_price=0.60, stop_price=0.605,
        tp1_price=0.595, strategy="direct",
    )
    broker = _FakeBroker(
        open_trades=[],  # not on broker yet (race / lag)
        pending=[PendingOrderInfo(
            order_id="ORD_TRACKED", symbol="NZD_USD", order_type="LIMIT_ORDER",
            units=5000, price=0.595, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
            parent_trade_id="T_TRACKED", position_fill="REDUCE_ONLY",
        )],
    )
    recovery = StateRecovery(_ctx(broker, tracker, audit=_FakeAudit()))

    recovery.reconcile_orphan_harvests()

    assert broker.cancelled == []


# ---------- Hotfix/harvest-same-cycle-race (2026-04-30): 3 new tests ----------

def test_same_cycle_placement_survives_reconcile():
    """A harvest LIMIT placed during the entry-fill loop of
    reconcile_pending_orders MUST NOT be cancelled by the harvest-reconcile
    loop in the same call. The pre-fix race emitted broker_side_gone within
    ~250ms of every placement because pending_on_broker was snapshotted
    BEFORE the placement.
    """
    tracker = PositionTracker(persist_path=None)
    tracker.register_pending_entry("USD_JPY", "ORD_ENTRY")
    tracker.set_pending_entry_meta("USD_JPY", {
        "tp1_price": 150.5,
        "strategy": "direct",
        "direction": "long",
        "entry_price": 150.0,
    })
    broker = _FakeBroker(
        open_trades=[TradeInfo(
            trade_id="T_NEW", symbol="USD_JPY", direction="long",
            units=10000, entry_price=150.0, current_stop=149.5,
            current_tp=151.0,
        )],
        pending=[],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_pending_orders()

    assert len(broker.placed) == 1
    assert broker.placed[0]["position_fill"] == "REDUCE_ONLY"
    new_pos = tracker.get("T_NEW")
    assert new_pos is not None
    assert new_pos.harvest_order_id == "ORD_1", \
        f"harvest_order_id wiped by same-cycle race; got {new_pos.harvest_order_id}"
    assert "ORD_1" in sr_mod._HARVEST_LEDGER.all(), \
        "ledger entry wiped by same-cycle race"
    cancelled_events = [e for e in audit.events
                        if e["type"] == "harvest_limit_cancelled"]
    assert cancelled_events == [], \
        f"unexpected harvest_limit_cancelled in same cycle: {cancelled_events}"
    created_events = [e for e in audit.events
                      if e["type"] == "harvest_limit_created"]
    assert len(created_events) == 1
    assert broker.cancelled == []


def test_next_cycle_leaves_live_harvest_intact():
    """Cycle 2: the harvest LIMIT placed in cycle 1 is still alive on the
    broker. reconcile_pending_orders MUST treat it as 'still pending' and
    not touch tracker/ledger or emit any cancel event.
    """
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T_LIVE", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5, strategy="direct",
    )
    tracker.set_harvest_order("T_LIVE", "ORD_HARV")
    sr_mod._HARVEST_LEDGER.add(
        order_id="ORD_HARV", trade_id="T_LIVE", symbol="USD_JPY",
        strategy="direct",
        gtd_time="2026-12-31T00:00:00.000000000Z",
    )
    broker = _FakeBroker(
        open_trades=[TradeInfo(
            trade_id="T_LIVE", symbol="USD_JPY", direction="long",
            units=10000, entry_price=150.0,
        )],
        pending=[PendingOrderInfo(
            order_id="ORD_HARV", symbol="USD_JPY", order_type="LIMIT",
            units=5000, price=150.5, state="PENDING",
            time_in_force="GTD", gtd_time="2026-12-31T00:00:00.000000000Z",
        )],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_pending_orders()

    pos = tracker.get("T_LIVE")
    assert pos is not None
    assert pos.harvest_order_id == "ORD_HARV"
    assert "ORD_HARV" in sr_mod._HARVEST_LEDGER.all()
    assert broker.cancelled == []
    cancelled_events = [e for e in audit.events
                        if e["type"] == "harvest_limit_cancelled"]
    assert cancelled_events == []


def test_real_broker_side_gone_still_clears_local_state():
    """Counter-test: if a harvest LIMIT genuinely vanishes from the broker
    (e.g. GTD-expired between cycles, pre-existing tracker pointer, NOT
    placed in this same call), the existing broker_side_gone path MUST
    still fire to keep local state consistent. Guards against the fix
    being too permissive.
    """
    tracker = PositionTracker(persist_path=None)
    tracker.register_entry(
        trade_id="T_STALE", symbol="USD_JPY", direction="long",
        units=10000, entry_price=150.0, stop_price=149.5,
        tp1_price=150.5, strategy="direct",
    )
    tracker.set_harvest_order("T_STALE", "ORD_STALE")
    sr_mod._HARVEST_LEDGER.add(
        order_id="ORD_STALE", trade_id="T_STALE", symbol="USD_JPY",
        strategy="direct",
        gtd_time="2026-04-30T00:00:00.000000000Z",
    )
    broker = _FakeBroker(
        open_trades=[TradeInfo(
            trade_id="T_STALE", symbol="USD_JPY", direction="long",
            units=10000, entry_price=150.0,
        )],
        pending=[],
    )
    audit = _FakeAudit()
    recovery = StateRecovery(_ctx(broker, tracker, audit=audit))

    recovery.reconcile_pending_orders()

    pos = tracker.get("T_STALE")
    assert pos.harvest_order_id == ""
    assert "ORD_STALE" not in sr_mod._HARVEST_LEDGER.all()
    cancelled_events = [e for e in audit.events
                        if e["type"] == "harvest_limit_cancelled"
                        and e.get("reason") == "broker_side_gone"]
    assert len(cancelled_events) == 1
