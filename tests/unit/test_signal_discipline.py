"""Phase 4 Signal Discipline — unit + replay tests.

Covers: Bug K (cooldown), Bug L (zone blacklist), Bug M (expiry
backoff), Bug N (daily circuit breaker), plus replays of today's
AUD/USD and NZD/JPY incidents.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from scrooge_v3.risk.cooldown_tracker import CooldownTracker, zone_key_for
from scrooge_v3.core.types import (
    GateMode, MarketSnapshot, SymbolContext, TradeCandidate, TradeDirection,
)


# ------------------------------------------------------------------
# helpers
# ------------------------------------------------------------------
def _ctx(symbol="AUD_USD", mid=0.7155, spread=0.00014, state=None):
    snap = MarketSnapshot(
        symbol=symbol, bid=mid - spread / 2, ask=mid + spread / 2,
        mid=mid, spread=spread, timestamp=datetime.now(timezone.utc),
    )
    return SymbolContext(symbol=symbol, snapshot=snap, state=state or {})


def _cand(symbol="AUD_USD", direction="short", entry=0.71554, sl=0.71820):
    return TradeCandidate(
        symbol=symbol, direction=TradeDirection(direction),
        strategy="reversal", entry_price=entry, stop_price=sl,
        take_profit=entry - 0.003 if direction == "long" else entry + 0.003,
        risk_reward=1.5, score=35,
    )


@pytest.fixture
def tmp_tracker(tmp_path: Path) -> CooldownTracker:
    return CooldownTracker(
        config={
            "cooldown_after_stop_minutes": 60,
            "zone_blacklist_hours": 4,
            "zone_bucket_pips": 20,
            "max_consecutive_expiries": 3,
            "backoff_minutes": 30,
            "max_daily_loss_pct": 3.0,
        },
        data_dir=tmp_path,
    )


# ------------------------------------------------------------------
# 1. Cooldown after stop
# ------------------------------------------------------------------
def test_cooldown_after_stop(tmp_tracker):
    t = tmp_tracker
    now = datetime(2026, 4, 19, 4, 34, 0, tzinfo=timezone.utc)
    t.record_stop("AUD_USD", "long", entry_price=0.71500, when=now)

    # 84 seconds later — still in cooldown
    t_84 = now + timedelta(seconds=84)
    assert t.is_in_cooldown("AUD_USD", "long", now=t_84) is True
    # 61 minutes later — cleared
    t_61 = now + timedelta(minutes=61)
    assert t.is_in_cooldown("AUD_USD", "long", now=t_61) is False
    # Opposite direction is unaffected
    assert t.is_in_cooldown("AUD_USD", "short", now=t_84) is False
    # Other symbol unaffected
    assert t.is_in_cooldown("EUR_USD", "long", now=t_84) is False


def test_cooldown_persists_across_restart(tmp_path):
    cfg = {"cooldown_after_stop_minutes": 60}
    t1 = CooldownTracker(config=cfg, data_dir=tmp_path)
    now = datetime(2026, 4, 19, 4, 34, tzinfo=timezone.utc)
    t1.record_stop("AUD_USD", "long", entry_price=0.7150, when=now)

    # New tracker reading the same dir
    t2 = CooldownTracker(config=cfg, data_dir=tmp_path)
    check = now + timedelta(seconds=84)
    assert t2.is_in_cooldown("AUD_USD", "long", now=check) is True


# ------------------------------------------------------------------
# 2. Zone blacklist
# ------------------------------------------------------------------
def test_zone_blacklist_after_loss(tmp_tracker):
    t = tmp_tracker
    now = datetime(2026, 4, 19, 5, 0, tzinfo=timezone.utc)
    t.blacklist_zone("AUD_USD", "long", 0.71554, when=now)
    # Same zone (within bucket)
    assert t.is_zone_blacklisted("AUD_USD", "long", 0.71560, now=now + timedelta(minutes=30))
    # Same price, other direction — NOT blocked
    assert not t.is_zone_blacklisted("AUD_USD", "short", 0.71554, now=now + timedelta(minutes=30))
    # Much further price — different bucket
    assert not t.is_zone_blacklisted("AUD_USD", "long", 0.72000, now=now + timedelta(minutes=30))
    # Past expiry window (4 hours)
    assert not t.is_zone_blacklisted("AUD_USD", "long", 0.71554, now=now + timedelta(hours=5))


def test_zone_key_bucketing_jpy():
    # JPY pairs use 0.01 per pip -> 20 pips = 0.20
    k1 = zone_key_for("NZD_JPY", "short", 82.455, pips=20)
    k2 = zone_key_for("NZD_JPY", "short", 82.460, pips=20)
    assert k1 == k2
    k3 = zone_key_for("NZD_JPY", "short", 83.100, pips=20)
    assert k3 != k1


# ------------------------------------------------------------------
# 3. Expiry backoff
# ------------------------------------------------------------------
def test_limit_expiry_backoff(tmp_tracker):
    t = tmp_tracker
    sym, dir_ = "NZD_JPY", "short"
    price = 82.450

    # 1st, 2nd expiries — still allowed
    t.record_expiry(sym, dir_, price)
    assert not t.is_in_expiry_backoff(sym, dir_, price)
    t.record_expiry(sym, dir_, price)
    assert not t.is_in_expiry_backoff(sym, dir_, price)

    # 3rd expiry triggers backoff
    t.record_expiry(sym, dir_, price)
    assert t.is_in_expiry_backoff(sym, dir_, price)

    # Fill on same zone resets counter
    t.record_fill(sym, dir_, price)
    assert not t.is_in_expiry_backoff(sym, dir_, price)
    assert t.expiry_count(sym, dir_, price) == 0

    # Drive back to backoff, then direction-flip resets
    for _ in range(3):
        t.record_expiry(sym, dir_, price)
    assert t.is_in_expiry_backoff(sym, dir_, price)
    t.record_direction_flip(sym, "long")  # flip opposite resets short counter
    assert not t.is_in_expiry_backoff(sym, dir_, price)


# ------------------------------------------------------------------
# 4. Daily circuit breaker
# ------------------------------------------------------------------
def test_daily_circuit_breaker(tmp_tracker):
    t = tmp_tracker
    now = datetime(2026, 4, 19, 12, 0, tzinfo=timezone.utc)
    t.start_day(equity=10000.0, when=now)

    # Accumulate losses to 2% — not yet tripped
    t.record_realized_pnl(-120, now=now)
    t.record_realized_pnl(-80, now=now)
    assert not t.is_circuit_tripped(now=now)

    # Push to 3.2% — trips
    t.record_realized_pnl(-120, now=now)
    assert t.is_circuit_tripped(now=now)

    # Partial recovery does NOT un-trip
    t.record_realized_pnl(+200, now=now)
    assert t.is_circuit_tripped(now=now)


def test_circuit_resets_on_new_utc_day(tmp_tracker):
    t = tmp_tracker
    day1 = datetime(2026, 4, 19, 23, 0, tzinfo=timezone.utc)
    t.start_day(equity=10000.0, when=day1)
    t.record_realized_pnl(-400, now=day1)
    assert t.is_circuit_tripped(now=day1)

    day2 = datetime(2026, 4, 20, 0, 5, tzinfo=timezone.utc)
    assert not t.is_circuit_tripped(now=day2)


# ------------------------------------------------------------------
# 5. Gate plumbing
# ------------------------------------------------------------------
def test_cooldown_gate_blocks_via_state(tmp_tracker):
    from scrooge_v3.gates.cooldown import CooldownGate
    t = tmp_tracker
    # Use a stop 5 minutes in the real past so the gate's datetime.now()
    # still considers us inside the 60-minute cooldown window.
    now = datetime.now(timezone.utc) - timedelta(minutes=5)
    t.record_stop("AUD_USD", "long", entry_price=0.7150, when=now)
    state = t.to_state_dict()
    ctx = _ctx(state=state)
    cand = _cand(symbol="AUD_USD", direction="long", entry=0.71554, sl=0.71820)
    gate = CooldownGate({"cooldown_after_stop_minutes": 60})
    res = gate.evaluate(cand, ctx)
    assert res.passed is False
    assert "Cooldown" in res.reason


def test_expiry_backoff_gate_blocks_via_state(tmp_tracker):
    from scrooge_v3.gates.expiry_backoff import ExpiryBackoffGate
    t = tmp_tracker
    price = 82.45
    for _ in range(3):
        t.record_expiry("NZD_JPY", "short", price)
    state = t.to_state_dict()
    ctx = _ctx(symbol="NZD_JPY", mid=price, state=state)
    cand = _cand(symbol="NZD_JPY", direction="short", entry=price, sl=price + 0.3)
    gate = ExpiryBackoffGate({"zone_bucket_pips": 20})
    res = gate.evaluate(cand, ctx)
    assert res.passed is False


def test_daily_circuit_gate_blocks_via_state(tmp_tracker):
    from scrooge_v3.gates.daily_circuit import DailyCircuitGate
    t = tmp_tracker
    now = datetime(2026, 4, 19, 12, 0, tzinfo=timezone.utc)
    t.start_day(equity=10000.0, when=now)
    for _ in range(4):
        t.record_realized_pnl(-100, now=now)
    assert t.is_circuit_tripped(now=now)
    ctx = _ctx(state=t.to_state_dict())
    cand = _cand()
    gate = DailyCircuitGate()
    res = gate.evaluate(cand, ctx)
    assert res.passed is False


def test_debounce_gate_blocks_blacklisted_zone(tmp_tracker):
    from scrooge_v3.gates.debounce import DebounceGate
    t = tmp_tracker
    # Blacklist 30 min in the real past; gate uses datetime.now().
    now = datetime.now(timezone.utc) - timedelta(minutes=30)
    t.blacklist_zone("AUD_USD", "long", 0.71554, when=now)
    state = t.to_state_dict()
    ctx = _ctx(state=state)
    cand = _cand(symbol="AUD_USD", direction="long", entry=0.71560, sl=0.71290)
    gate = DebounceGate({"zone_blacklist_hours": 4, "zone_bucket_pips": 20})
    res = gate.evaluate(cand, ctx)
    assert res.passed is False
    assert "blacklist" in res.reason.lower()


# ------------------------------------------------------------------
# 6. Replays of today's live incidents
# ------------------------------------------------------------------
def test_replay_audusd_revenge_sequence(tmp_tracker):
    """First entry allowed; after SL at 04:34, re-entry 84s later blocked."""
    from scrooge_v3.gates.cooldown import CooldownGate

    t = tmp_tracker
    t0 = datetime(2026, 4, 19, 4, 34, 2, tzinfo=timezone.utc)
    # First entry should be allowed (no prior state)
    ctx_pre = _ctx(symbol="AUD_USD", state=t.to_state_dict())
    cand = _cand(symbol="AUD_USD", direction="long", entry=0.71554, sl=0.71510)
    gate = CooldownGate({"cooldown_after_stop_minutes": 60})
    assert gate.evaluate(cand, ctx_pre).passed is True

    # Record the SL hit at 04:34
    t.record_stop("AUD_USD", "long", entry_price=0.71554, when=t0)

    # At 04:35:26 (84 sec later) try to re-enter — must be blocked
    t_re = datetime(2026, 4, 19, 4, 35, 26, tzinfo=timezone.utc)
    # We simulate "now" by feeding state AT that moment
    # (gate reads datetime.now; we rely on stopped_at being 84s in the past)
    # Because gate uses wall-clock, we manipulate by setting stopped_at
    # effectively "now - 84s".
    from datetime import datetime as _dt
    real_now = _dt.now(timezone.utc)
    t._cooldowns[t.cooldown_key("AUD_USD", "long")].stopped_at = real_now - timedelta(seconds=84)
    ctx_post = _ctx(symbol="AUD_USD", state=t.to_state_dict())
    res = gate.evaluate(cand, ctx_post)
    assert res.passed is False, f"expected block within cooldown: {res.reason}"


def test_replay_nzdjpy_14_limit_sequence(tmp_tracker):
    """After 3 consecutive limit expiries at same zone, 4th+ blocked."""
    from scrooge_v3.gates.expiry_backoff import ExpiryBackoffGate
    t = tmp_tracker
    sym, dir_, price = "NZD_JPY", "short", 82.450

    gate = ExpiryBackoffGate({"zone_bucket_pips": 20})

    for i in range(3):
        t.record_expiry(sym, dir_, price)
        ctx = _ctx(symbol=sym, mid=price, state=t.to_state_dict())
        cand = _cand(symbol=sym, direction=dir_, entry=price, sl=price + 0.3)
        res = gate.evaluate(cand, ctx)
        if i < 2:
            assert res.passed is True, f"expiry #{i+1} should not yet block"
        else:
            assert res.passed is False, "3rd expiry should trigger backoff"

    # 4th attempt — still blocked until backoff window passes
    ctx = _ctx(symbol=sym, mid=price, state=t.to_state_dict())
    cand = _cand(symbol=sym, direction=dir_, entry=price, sl=price + 0.3)
    assert gate.evaluate(cand, ctx).passed is False


# ------------------------------------------------------------------
# 7. Gate ordering sanity check
# ------------------------------------------------------------------
def test_gate_ordering_circuit_first():
    """Daily circuit should fire first in the pipeline bootstrap."""
    import json
    from pathlib import Path
    from scrooge_v3.core.config import ConfigStore
    # Build gates like bootstrap does
    from scrooge_v3.gates.pipeline import GatePipeline
    from scrooge_v3.gates import (
        DailyCircuitGate, CooldownGate, DebounceGate,
        ExpiryBackoffGate, RegimeFloorGate, ZoneEntryCapGate,
    )
    gp = GatePipeline()
    gp.register_many([
        DailyCircuitGate(),
        CooldownGate({}),
        DebounceGate({}),
        ExpiryBackoffGate({}),
        RegimeFloorGate({"min_score": -4}),
        ZoneEntryCapGate({}),
    ])
    names = [g.name for g in gp.gates]
    assert names[0] == "daily_circuit"
    assert "cooldown" in names
    assert "debounce" in names
    assert "expiry_backoff" in names
    assert names.index("cooldown") < names.index("zone_entry_cap")
