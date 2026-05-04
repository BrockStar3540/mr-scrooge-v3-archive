"""Patch A regression — strategy attribution in AuditEvent.

B-1 Cause #2: AuditEvent had no top-level `strategy`, so live execution-audit
events were strategy-less. Fix: add `strategy` to dataclass, thread
`tracked.strategy` through position_coordinator, normalize state_recovery
harvest audit to top-level.

Tests assert the contract: any audit event from a tracked-position context
carries non-empty `strategy` at top level (not buried in `extra`).
"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from scrooge_v3.telemetry.execution_audit import AuditEvent
from scrooge_v3.services.state_recovery import StateRecovery


def test_audit_event_has_strategy_field():
    """Dataclass must expose `strategy` at top level with a default of ''."""
    e = AuditEvent(type="hold", reason="no_action", strategy="dbb_trend")
    assert e.strategy == "dbb_trend"
    d = e.to_dict()
    assert d.get("strategy") == "dbb_trend", \
        f"strategy must be top-level in to_dict; got {d}"


def test_audit_event_strategy_default_empty():
    e = AuditEvent(type="hold", reason="no_action")
    assert e.strategy == ""
    assert e.to_dict().get("strategy") == ""


def test_state_recovery_audit_harvest_promotes_strategy_to_top_level():
    """_audit_harvest used to stuff strategy into `extra`. After Patch A it
    must put it at top level so downstream consumers don't have to dig."""
    captured: list[AuditEvent] = []

    class _FakeAudit:
        def record(self, ev):
            captured.append(ev)

    ctx = SimpleNamespace(execution_audit=_FakeAudit())
    sr = StateRecovery(ctx)
    sr._audit_harvest(
        "harvest_limit_created", "tp1_preplaced",
        trade_id="T1", order_id="O1", symbol="USD_JPY",
        strategy="dbb_trend",
        gtd_time="2026-12-31T00:00:00.000000000Z",
        created_at="2026-05-04T00:00:00+00:00",
    )
    assert len(captured) == 1
    ev = captured[0]
    assert ev.strategy == "dbb_trend", \
        f"strategy must be top-level; got strategy={ev.strategy!r} extra={ev.extra}"
    # And not duplicated in extra
    assert "strategy" not in (ev.extra or {}), \
        f"strategy should not be in extra anymore; got extra={ev.extra}"
    # Other extras still flow through
    assert ev.extra.get("order_id") == "O1"
    assert ev.extra.get("gtd_time")


def test_state_recovery_audit_harvest_empty_strategy_ok():
    """If caller doesn't pass a strategy, top-level must be '' — no crash,
    no spurious 'unknown' string."""
    captured: list[AuditEvent] = []

    class _FakeAudit:
        def record(self, ev):
            captured.append(ev)

    sr = StateRecovery(SimpleNamespace(execution_audit=_FakeAudit()))
    sr._audit_harvest(
        "orphan_harvest_limit_cancelled", "ok",
        trade_id="T2", order_id="O2", symbol="EUR_USD",
    )
    assert captured[0].strategy == ""


def test_position_coordinator_audit_base_includes_strategy():
    """Smoke check: the dict spread into AuditEvent in position_coordinator
    must include `strategy`. This is the live management-event path that was
    100% strategy-less pre-patch."""
    # We don't construct the full coordinator (too much surface). Instead
    # we replay the audit_base shape against AuditEvent to lock the contract.
    tracked = SimpleNamespace(
        trade_id="T1", symbol="USD_JPY", direction="long", strategy="direct",
    )
    audit_base = dict(
        trade_id=tracked.trade_id, symbol=tracked.symbol,
        direction=tracked.direction,
        strategy=getattr(tracked, "strategy", "") or "",
        profit_r=0.5, spread=0.0002, action="ratchet",
    )
    e = AuditEvent(type="sl_moved", reason="ratchet", **audit_base)
    assert e.strategy == "direct"
    assert e.to_dict().get("strategy") == "direct"


def test_position_coordinator_audit_base_handles_missing_strategy():
    """Defensive: tracked objects without a strategy attr (or with None)
    must produce empty string, not crash."""
    tracked = SimpleNamespace(trade_id="T9", symbol="X", direction="long")
    base = dict(
        trade_id=tracked.trade_id, symbol=tracked.symbol,
        direction=tracked.direction,
        strategy=getattr(tracked, "strategy", "") or "",
        profit_r=0.0, spread=0.0, action="hold",
    )
    e = AuditEvent(type="hold", reason="no_action", **base)
    assert e.strategy == ""
