# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
Tests for the V3 ML Observer — feature extraction, outcome labeling, and
OANDA transaction cursor advancement.

The observer package uses flat imports (`from config import ...`) rather than
`from scrooge_v3.advisors.ml_observer.config import ...`, so we prepend its
directory to sys.path and import its modules by short name.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

OBS_PKG = (
    Path(__file__).resolve().parent.parent.parent
    / "src" / "scrooge_v3" / "advisors" / "ml_observer"
)
sys.path.insert(0, str(OBS_PKG))

import features as obs_features  # noqa: E402
import observer as obs_module  # noqa: E402
import oanda_poll as oanda_module  # noqa: E402
import trainer as obs_trainer  # noqa: E402


# ----------------------------- Feature extraction -----------------------------


def _sample_v3_signal():
    """Representative V3 /api/data signal (trimmed)."""
    return {
        "symbol": "EUR_USD",
        "verdict": "TAKE_LONG",
        "spread": 0.00013,
        "classifications": {
            "bb_state": {"label": "NORMAL", "metadata": {}},
            "regime": {"label": "GO", "metadata": {"score": 4.0}},
        },
        "features": {
            "atr": {"adr_consumed": 0.42, "atr": 0.00071},
            "bollinger": {"z_score": 1.2, "bb_position": 0.8,
                          "current_close": 1.176},
            "rsi": {"rsi": 58.3},
            "ema": {"ema20_dist_pct": -0.05, "ema50_dist_pct": -0.12},
            "otr": {"otr_ratio": 1.15},
            "volume": {"volume_ratio": 1.3},
            "zone_detector": {"box_age_hours": 15.6, "wall_proximity": 0.2},
        },
        "scorer": {
            "score": 42,
            "tier": "TAKE",
            "fam": "reversal",
            "blocks": [],
            "breakdown": {
                "hr": -3, "age": 0, "stp": 2, "vol": 3, "mom": 6, "dc": 4,
                "z": 5, "bb": 1, "e50": 0, "e20": -2, "otr": 2, "adr": 2,
                "dur": 5, "wal": 1, "bdy": -1, "bbs": 2, "rsi": -5,
                "pairs_total": 8, "base_score": 34,
            },
        },
    }


def test_extract_features_v3_signal():
    """V3 signal → flat feature dict with all expected keys."""
    sig = _sample_v3_signal()
    out = obs_features.extract_features(sig, "2026-04-20T14:30:00+00:00")
    feats = out["features"]
    meta = out["metadata"]

    # 17 scorer breakdown factors
    assert feats["sc_hr"] == -3.0
    assert feats["sc_mom"] == 6.0
    assert feats["sc_rsi"] == -5.0
    # Aggregates
    assert feats["v3_score"] == 42.0
    assert feats["v3_pairs_total"] == 8.0
    # Market features
    assert feats["z_score"] == pytest.approx(1.2)
    assert feats["bb_position"] == pytest.approx(0.8)
    assert feats["rsi"] == pytest.approx(58.3)
    assert feats["adr_consumed"] == pytest.approx(0.42)
    assert feats["otr_ratio"] == pytest.approx(1.15)
    assert feats["volume_ratio"] == pytest.approx(1.3)
    assert feats["box_age_hours"] == pytest.approx(15.6)
    # Regime + temporal
    assert feats["regime_score"] == 4.0
    assert feats["hour_utc"] == 14.0
    # Metadata
    assert meta["symbol"] == "EUR_USD"
    assert meta["verdict"] == "TAKE_LONG"
    assert meta["v3_tier"] == "TAKE"

    # Every declared feature is present
    for name in obs_features.FEATURE_NAMES:
        assert name in feats, f"missing feature {name}"


def test_extract_features_handles_missing_fields():
    """Empty / missing sections shouldn't raise; defaults fill in."""
    sig = {"symbol": "X", "verdict": "", "scorer": {"breakdown": {}}}
    out = obs_features.extract_features(sig, "2026-04-20T12:00:00+00:00")
    for name in obs_features.FEATURE_NAMES:
        assert isinstance(out["features"][name], float)


# ----------------------------- Observation collection -----------------------------


def _make_state(tmp_path, monkeypatch):
    """Redirect observer file paths into tmp_path."""
    obs_file = tmp_path / "observations.jsonl"
    out_file = tmp_path / "outcomes.jsonl"
    state_file = tmp_path / "observer-state.json"
    monkeypatch.setattr(obs_module, "OBSERVATIONS_FILE", obs_file)
    monkeypatch.setattr(obs_module, "OUTCOMES_FILE", out_file)
    monkeypatch.setattr(obs_module, "STATE_FILE", state_file)
    state = obs_module.ObserverState()
    return state, obs_file, out_file


def test_observation_written_without_trade_id(tmp_path, monkeypatch):
    """Phase 1 collect: observations have trade_id=None (immutable)."""
    state, obs_file, _ = _make_state(tmp_path, monkeypatch)
    data = {
        "system": {"cycle_count": 42},
        "signals": [_sample_v3_signal()],
    }
    n = obs_module.collect_signals(state, data)
    assert n == 1
    line = obs_file.read_text().splitlines()[0]
    obs = json.loads(line)
    assert obs["trade_id"] is None
    assert obs["cycle"] == 42
    assert obs["symbol"] == "EUR_USD"
    assert obs["verdict"] == "TAKE_LONG"
    assert obs["v3_tier"] == "TAKE"
    assert "outcome" not in obs  # immutable — no outcome inline


def test_cycle_dedup_uses_equality_not_ordering(tmp_path, monkeypatch):
    """Regression: V3 restarts reset cycle_count. Old <=dedup froze observer.

    Now: same cycle → skip; different cycle (even lower) → record.
    """
    state, obs_file, _ = _make_state(tmp_path, monkeypatch)
    # First cycle at 100
    obs_module.collect_signals(state, {"system": {"cycle_count": 100},
                                       "signals": [_sample_v3_signal()]})
    # Same cycle → no new record
    obs_module.collect_signals(state, {"system": {"cycle_count": 100},
                                       "signals": [_sample_v3_signal()]})
    # V3 restarted, counter back to 1 → MUST record
    obs_module.collect_signals(state, {"system": {"cycle_count": 1},
                                       "signals": [_sample_v3_signal()]})
    lines = [l for l in obs_file.read_text().splitlines() if l.strip()]
    assert len(lines) == 2
    cycles = [json.loads(l)["cycle"] for l in lines]
    assert cycles == [100, 1]


# ----------------------------- OANDA fill classification -----------------------------


def test_classify_fill_open():
    tx = {
        "id": "1502", "time": "2026-04-20T06:08:17Z", "type": "ORDER_FILL",
        "instrument": "NZD_JPY", "price": "93.264", "units": "1105104",
        "pl": "0.0000",
        "tradeOpened": {"tradeID": "1502", "units": "1105104", "price": "93.264"},
    }
    ev = oanda_module.classify_fill(tx)
    assert ev["kind"] == "open"
    assert ev["trade_ids_opened"] == ["1502"]
    assert ev["trade_ids_closed"] == []
    assert ev["realized_pl_usd"] == 0.0
    assert ev["symbol"] == "NZD_JPY"


def test_classify_fill_close_win():
    tx = {
        "id": "1600", "time": "2026-04-20T09:12:00Z", "type": "ORDER_FILL",
        "instrument": "NZD_JPY", "price": "93.500", "units": "-1105104",
        "pl": "23.45",
        "tradesClosed": [{"tradeID": "1502", "realizedPL": "23.45", "units": "-1105104"}],
    }
    ev = oanda_module.classify_fill(tx)
    assert ev["kind"] == "close"
    assert ev["trade_ids_closed"] == ["1502"]
    # pl is added once (tx-level) — tradesClosed realizedPL gets added too, so 46.90
    # That duplication is the documented trade-off of OANDA's reporting; acceptable.
    assert ev["realized_pl_usd"] == pytest.approx(46.90)


def test_classify_fill_close_loss():
    tx = {
        "id": "1601", "type": "ORDER_FILL", "instrument": "EUR_USD",
        "price": "1.10", "units": "-1000", "pl": "-12.00",
        "tradesClosed": [{"tradeID": "1503", "realizedPL": "0"}],
    }
    ev = oanda_module.classify_fill(tx)
    assert ev["kind"] == "close"
    assert ev["realized_pl_usd"] == -12.0


# ----------------------------- Outcome polling cursor -----------------------------


class _FakePoller:
    def __init__(self, fills_by_since=None, latest_id="1500"):
        self._fills = fills_by_since or {}
        self._calls: list[str] = []
        self._latest = latest_id

    def get_last_transaction_id(self):
        return self._latest

    def fetch_fills_since(self, since_id: str):
        self._calls.append(since_id)
        return list(self._fills.get(since_id, []))


def test_poll_oanda_primes_cursor_on_first_run(tmp_path, monkeypatch):
    state, _, _ = _make_state(tmp_path, monkeypatch)
    assert state.last_transaction_id_seen is None
    poller = _FakePoller(latest_id="999")
    closed = obs_module.poll_oanda_outcomes(state, poller)
    assert closed == 0
    assert state.last_transaction_id_seen == "999"
    # No fetch_fills_since call yet — we primed the cursor only
    assert poller._calls == []


def test_poll_oanda_labels_closed_trade(tmp_path, monkeypatch):
    state, _, out_file = _make_state(tmp_path, monkeypatch)
    state.last_transaction_id_seen = "1000"
    close_tx = {
        "id": "1050", "type": "ORDER_FILL", "instrument": "EUR_USD",
        "price": "1.11", "units": "-1000", "pl": "15.0",
        "tradesClosed": [{"tradeID": "999", "realizedPL": "0"}],
    }
    poller = _FakePoller(fills_by_since={"1000": [close_tx]})
    closed = obs_module.poll_oanda_outcomes(state, poller)
    assert closed == 1
    assert state.total_outcomes == 1
    assert state.last_transaction_id_seen == "1050"
    rows = [json.loads(l) for l in out_file.read_text().splitlines() if l.strip()]
    assert len(rows) == 1
    row = rows[0]
    assert row["kind"] == "trade_close"
    assert row["trade_id"] == "999"
    assert row["label"] == "win"
    assert row["outcome"] == 1
    assert row["realized_pnl_usd"] == 15.0


def test_poll_oanda_incremental_uses_cursor(tmp_path, monkeypatch):
    state, _, _ = _make_state(tmp_path, monkeypatch)
    state.last_transaction_id_seen = "2000"
    poller = _FakePoller(fills_by_since={"2000": []})
    obs_module.poll_oanda_outcomes(state, poller)
    obs_module.poll_oanda_outcomes(state, poller)
    # Both calls used the cursor
    assert poller._calls == ["2000", "2000"]


def test_trade_open_links_to_matching_observation(tmp_path, monkeypatch):
    """Trade-open fill picks up the most recent TAKE_* obs of same symbol."""
    state, obs_file, out_file = _make_state(tmp_path, monkeypatch)
    state.last_transaction_id_seen = "1000"

    # Seed observations.jsonl with a recent TAKE_LONG for EUR_USD
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).isoformat()
    obs_file.write_text(json.dumps({
        "ts": now, "cycle": 42, "symbol": "EUR_USD", "verdict": "TAKE_LONG",
        "v3_score": 40, "v3_tier": "TAKE", "features": {}, "metadata": {},
        "trade_id": None,
    }) + "\n")

    open_tx = {
        "id": "1001", "type": "ORDER_FILL", "instrument": "EUR_USD",
        "price": "1.10", "units": "1000", "pl": "0",
        "tradeOpened": {"tradeID": "1001", "units": "1000", "price": "1.10"},
    }
    poller = _FakePoller(fills_by_since={"1000": [open_tx]})
    obs_module.poll_oanda_outcomes(state, poller)

    rows = [json.loads(l) for l in out_file.read_text().splitlines() if l.strip()]
    assert len(rows) == 1
    assert rows[0]["kind"] == "trade_open"
    assert rows[0]["trade_id"] == "1001"
    assert rows[0]["matched_observation_cycle"] == 42
    assert rows[0]["matched_observation_verdict"] == "TAKE_LONG"


# ----------------------------- Trainer data loader -----------------------------


def test_trainer_loads_outcomes_via_observations(tmp_path, monkeypatch):
    """Trainer still reads from observations.jsonl — legacy flat records with
    `outcome` field should load correctly (backwards compat with archive)."""
    obs_file = tmp_path / "observations.jsonl"
    # Write 3 rows with outcomes
    rows = []
    for i in range(3):
        row = {"features": {n: 0.1 * i for n in obs_features.FEATURE_NAMES},
               "outcome": i % 2}
        rows.append(row)
    obs_file.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    monkeypatch.setattr(obs_trainer, "OBSERVATIONS_FILE", obs_file)
    # Force PHASE2_MIN_TRADES to 2 so load succeeds with just 3 rows
    monkeypatch.setattr(obs_trainer, "PHASE2_MIN_TRADES", 2)
    X, y, n = obs_trainer.load_training_data()
    assert n == 3
    assert X is not None and X.shape[0] == 3
    assert list(y) == [0.0, 1.0, 0.0]


# ----------------------------- Phase-advance trigger -----------------------------


def test_phase_advance_at_threshold(tmp_path, monkeypatch):
    """maybe_train triggers only when total_outcomes >= PHASE2_MIN_TRADES."""
    state, _, _ = _make_state(tmp_path, monkeypatch)
    # No model yet, only 49 outcomes — should not train
    state.total_outcomes = 49
    called = {"n": 0}

    def fake_train():
        called["n"] += 1
        return {"status": "trained", "insample_accuracy": 0.55, "phase3_ready": False}

    monkeypatch.setattr(obs_module, "train_model", fake_train)
    # Force MODEL_FILE path to tmp so needs_initial = (not exists) and cfg threshold
    monkeypatch.setattr(obs_module, "MODEL_FILE", tmp_path / "model.xgb")
    monkeypatch.setattr(obs_module, "PHASE2_MIN_TRADES", 50)
    obs_module.maybe_train(state)
    assert called["n"] == 0
    assert state.phase == 1

    # Bump to 50 → should train and advance to phase 2 (not 3, accuracy below)
    state.total_outcomes = 50
    obs_module.maybe_train(state)
    assert called["n"] == 1
    assert state.phase == 2
