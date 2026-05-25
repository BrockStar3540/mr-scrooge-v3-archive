# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
Tests for the V3 ML Observer — five-file schema.

Covers:
    - V3_SCORER log-line parser (head + factors + pair_adjustments + context)
    - build_scan_row → 47+ ml_features, all standard sections
    - OANDA fill classification (open / close / win / loss)
    - OANDA transactions cursor advancement
    - Outcome reconciliation end-to-end (scan → fill → close → outcomes row)
    - Each output file has stable schema (no required field missing)
    - Journal reader classifier categorizes gate / sizing / exec correctly
    - Account snapshot row shape (with and without OANDA summary)
    - Trainer loader handles both scans+outcomes and legacy observations
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

import features as obs_features   # noqa: E402
import observer as obs_module     # noqa: E402
import oanda_poll as oanda_module # noqa: E402
import shadow as obs_shadow       # noqa: E402
import trainer as obs_trainer     # noqa: E402
import v3_scorer_parser as spar   # noqa: E402
import journal_reader as jrdr     # noqa: E402
import account_snapshot as acct   # noqa: E402


# =============================================================================
# V3_SCORER log-line parser
# =============================================================================

_SCORER_LINE = (
    "2026-04-20 14:46:08 [INFO] scrooge_v3.strategies.v3_scorer — "
    "[V3_SCORER] base=14 final=13 tier=REJECT fam=direct session=ny_active "
    "(floor=30 b=42 a=50 cap=12) pairs_raw=-1 capped=-1 | "
    "hr=-3 age=+0 stp=-2 vol=-3 mom=+1 dc=+4 z=+4 bb=-1 e50=+0 e20=+4 "
    "otr=+0 adr=-1 dur=+5 wal=+1 bdy=+1 bbs=+2 rsi=+2 "
    "p_z_norm=+5 n_hr_adr=-6 || "
    "px=0.55880 ema20=0.55950 ema50=0.56020 box=0.00354 age=17.8h"
)


def test_scorer_parser_full_line_populates_all_sections():
    r = spar.parse_v3_scorer_line(_SCORER_LINE)
    assert r is not None
    # Head
    assert r["base"] == 14 and r["final"] == 13
    assert r["tier"] == "REJECT" and r["fam"] == "direct"
    assert r["session"] == "ny_active"
    assert r["floor"] == 30 and r["b"] == 42 and r["a"] == 50 and r["cap"] == 12
    assert r["pairs_raw"] == -1 and r["capped"] == -1
    # 17 factors
    assert set(r["factors"].keys()) == {
        "hr", "age", "stp", "vol", "mom", "dc", "z", "bb", "e50", "e20",
        "otr", "adr", "dur", "wal", "bdy", "bbs", "rsi"
    }
    assert r["factors"]["hr"] == -3
    assert r["factors"]["rsi"] == 2
    # Pair adjustments
    assert r["pair_adjustments"] == {"p_z_norm": 5, "n_hr_adr": -6}
    # Context
    assert r["context"]["px"] == pytest.approx(0.55880)
    assert r["context"]["ema20"] == pytest.approx(0.55950)
    assert r["context"]["age"] == pytest.approx(17.8)
    # No unknown tokens
    assert r["raw_extra"] == {}


def test_scorer_parser_returns_none_on_unrelated_line():
    assert spar.parse_v3_scorer_line("2026-04-20 14:46:08 [INFO] hello world") is None


def test_scorer_parser_preserves_unknown_factor_in_raw_extra():
    line = ("[V3_SCORER] base=1 final=1 tier=TAKE fam=reversal session=asia_active "
            "(floor=30 b=44 a=54 cap=16) pairs_raw=+0 capped=+0 | "
            "hr=+0 age=+0 stp=+0 vol=+0 mom=+0 dc=+0 z=+0 bb=+0 e50=+0 e20=+0 "
            "otr=+0 adr=+0 dur=+0 wal=+0 bdy=+0 bbs=+0 rsi=+0 "
            "something_new=+7 || px=1.0 ema20=1.0 ema50=1.0 box=0.1 age=1.0h")
    r = spar.parse_v3_scorer_line(line)
    assert r is not None
    # "something_new" is not a core factor and doesn't start with p_ or n_
    assert r["raw_extra"] == {"something_new": 7}


# =============================================================================
# Scan row builder
# =============================================================================

def _sample_v3_signal():
    return {
        "symbol": "EUR_USD",
        "verdict": "TAKE_LONG",
        "strategy_allowed": "reversal",
        "spread": 0.00013,
        "classifications": {
            "bb_state": {"label": "NORMAL", "confidence": 1.0, "metadata": {}},
            "regime": {"label": "GO", "confidence": 2.0, "metadata": {"score": 4.0}},
            "opening_state": {"label": "NORMAL_OPEN", "confidence": 1.0, "metadata": {}},
            "structure": {"label": "UNKNOWN", "confidence": 0.0, "metadata": {}},
        },
        "features": {
            "atr": {"adr_consumed": 0.42, "atr": 0.00071, "atr_20pct": 0.00014,
                    "atr_60pct": 0.0004, "atr_80pct": 0.0005},
            "bollinger": {"z_score": 1.2, "bb_position": 0.8, "current_close": 1.176},
            "rsi": {"rsi": 58.3},
            "ema": {"ema20": 1.175, "ema50": 1.174,
                    "ema20_dist_pct": -0.05, "ema50_dist_pct": -0.12},
            "otr": {"otr_ratio": 1.15, "range_half": 0.002, "total_overhead": 0.001},
            "volume": {"volume_ratio": 1.3, "current_volume": 6500, "avg_volume": 5000},
            "zone_detector": {"box_age_hours": 15.6, "wall_proximity": 0.2,
                              "box_range": 0.007},
        },
        "gates": {
            "debounce": {"passed": True, "reason": "no prior entry"},
            "regime_floor": {"passed": True, "reason": "score above floor"},
        },
        "scorer": {
            "score": 42, "tier": "TAKE", "pairs_total": 8, "blocks": [],
            "breakdown": {
                "hr": -3, "age": 0, "stp": 2, "vol": 3, "mom": 6, "dc": 4,
                "z": 5, "bb": 1, "e50": 0, "e20": -2, "otr": 2, "adr": 2,
                "dur": 5, "wal": 1, "bdy": -1, "bbs": 2, "rsi": -5,
                "pairs_total": 8, "base_score": 34,
            },
        },
        "candidate": {
            "strategy": "DBB3_sell_zone_sustained_short",
            "direction": "short",
            "family": "canonical_lien_dbb",
            "entry_price": 1.1760,
            "stop_price": 1.1770,
            "take_profit": 1.1748,
            "size": 100000,
            "risk_reward": 1.2,
            "score": 42,
            "metadata": {
                "routing_cell_strategy": "DBB3_sell_zone_sustained_short",
                "routing_cell_family": "canonical_lien_dbb",
                "routing_cell_tier": "Pro",
                "routing_match_kind": "exact_strategy",
                "tp1": 1.1754,
            },
        },
    }


def test_build_scan_row_merges_api_and_parsed_log():
    sig = _sample_v3_signal()
    parsed = spar.parse_v3_scorer_line(_SCORER_LINE)
    row = obs_features.build_scan_row(
        sig, cycle=42, timestamp="2026-04-20T14:46:08+00:00",
        scorer_log_parsed=parsed,
    )
    # Scan-row shape
    for key in ("ts", "cycle", "symbol", "verdict", "spread",
                "scorer", "candidate", "identity", "features", "classifications", "gates",
                "ml_features", "metadata", "trade_id"):
        assert key in row, f"missing top-level key {key}"
    assert row["trade_id"] is None
    assert row["cycle"] == 42
    # Scorer section has BOTH API + log fields
    assert row["scorer"]["score"] == 42            # API
    assert row["scorer"]["final"] == 13            # log
    assert row["scorer"]["fam"] == "direct"        # log
    assert row["scorer"]["session"] == "ny_active" # log
    assert row["scorer"]["floor"] == 30
    assert row["scorer"]["pair_adjustments"] == {"p_z_norm": 5, "n_hr_adr": -6}
    assert row["candidate"]["strategy"] == "DBB3_sell_zone_sustained_short"
    assert row["identity"]["routing_match_kind"] == "exact_strategy"
    assert row["identity"]["family"] == "canonical_lien_dbb"
    # Gates
    assert row["gates"]["debounce"]["passed"] is True
    assert row["gates"]["debounce"]["reason"] == "no prior entry"
    # ML features count
    assert len(row["ml_features"]) == len(obs_features.FEATURE_NAMES)
    assert len(row["ml_features"]) >= 47


def test_build_scan_row_without_log_still_works():
    sig = _sample_v3_signal()
    row = obs_features.build_scan_row(sig, cycle=1,
                                      timestamp="2026-04-20T10:00:00+00:00")
    # Log-only fields default gracefully
    assert row["scorer"]["fam"] == ""
    assert row["scorer"]["session"] == ""
    assert row["scorer"]["pair_adjustments"] == {}
    # ML feature vector is still complete
    assert set(row["ml_features"].keys()) == set(obs_features.FEATURE_NAMES)


def test_build_scan_row_handles_empty_signal():
    row = obs_features.build_scan_row({"symbol": "X", "verdict": "",
                                       "scorer": {"breakdown": {}}},
                                      cycle=0,
                                      timestamp="2026-04-20T00:00:00+00:00")
    for name in obs_features.FEATURE_NAMES:
        assert isinstance(row["ml_features"][name], float)


# =============================================================================
# Observer wiring — five-file output
# =============================================================================

def _redirect_paths(tmp_path, monkeypatch):
    monkeypatch.setattr(obs_module, "SCANS_FILE", tmp_path / "scans.jsonl")
    monkeypatch.setattr(obs_module, "ACTIONS_FILE", tmp_path / "actions.jsonl")
    monkeypatch.setattr(obs_module, "ACCOUNT_FILE", tmp_path / "account.jsonl")
    monkeypatch.setattr(obs_module, "OUTCOMES_FILE", tmp_path / "outcomes.jsonl")
    monkeypatch.setattr(obs_module, "BOT_LOGS_FILE", tmp_path / "bot-logs.jsonl")
    monkeypatch.setattr(obs_module, "STATE_FILE", tmp_path / "state.json")
    monkeypatch.setattr(obs_module, "SHADOW_BANK_FILE", tmp_path / "shadow-bank.json")
    monkeypatch.setattr(obs_module, "SHADOW_DECISIONS_FILE", tmp_path / "shadow-decisions.jsonl")
    monkeypatch.setattr(obs_module, "SHADOW_TRADES_FILE", tmp_path / "shadow-trades.jsonl")
    return obs_module.ObserverState()


def test_collect_scans_writes_one_row_per_scored_candidate(tmp_path, monkeypatch):
    state = _redirect_paths(tmp_path, monkeypatch)
    data = {"system": {"cycle_count": 7}, "signals": [_sample_v3_signal()]}
    n, rows = obs_module.collect_scans(state, data, scorer_by_symbol={})
    assert n == 1
    assert len(rows) == 1
    row = json.loads((tmp_path / "scans.jsonl").read_text().splitlines()[0])
    assert row["cycle"] == 7
    assert row["symbol"] == "EUR_USD"
    assert row["trade_id"] is None


def test_collect_scans_cycle_dedup_uses_equality(tmp_path, monkeypatch):
    state = _redirect_paths(tmp_path, monkeypatch)
    sig = _sample_v3_signal()
    obs_module.collect_scans(state, {"system": {"cycle_count": 100}, "signals": [sig]}, {})
    obs_module.collect_scans(state, {"system": {"cycle_count": 100}, "signals": [sig]}, {})
    # V3 restarted, counter reset
    obs_module.collect_scans(state, {"system": {"cycle_count": 1}, "signals": [sig]}, {})
    cycles = [json.loads(l)["cycle"]
              for l in (tmp_path / "scans.jsonl").read_text().splitlines() if l.strip()]
    assert cycles == [100, 1]


def test_shadow_bank_builds_exact_strategy_bucket(tmp_path):
    scans_file = tmp_path / "scans.jsonl"
    outcomes_file = tmp_path / "outcomes.jsonl"
    scan = obs_features.build_scan_row(
        _sample_v3_signal(),
        cycle=11,
        timestamp="2026-04-20T10:00:00+00:00",
    )
    scans_file.write_text(json.dumps(scan) + "\n")
    outcomes_file.write_text("\n".join([
        json.dumps({
            "kind": "trade_open",
            "ts": "2026-04-20T10:01:00+00:00",
            "trade_id": "T1",
            "symbol": "EUR_USD",
            "matched_scan_ts": "2026-04-20T10:00:00+00:00",
        }),
        json.dumps({
            "kind": "trade_close",
            "ts": "2026-04-20T10:30:00+00:00",
            "trade_id": "T1",
            "symbol": "EUR_USD",
            "label": "win",
            "outcome": 1,
            "realized_pnl_usd": 125.0,
        }),
    ]) + "\n")

    bank = obs_shadow.build_shadow_bank(scans_file, outcomes_file)
    assert bank["source_counts"]["labeled_examples"] == 1
    assert len(bank["exact"]) == 1
    bucket = next(iter(bank["exact"].values()))
    assert bucket["n"] == 1
    assert bucket["wins"] == 1
    assert bucket["win_rate"] == 1.0


def test_shadow_decision_prefers_exact_bucket_when_profitable(tmp_path):
    scan = obs_features.build_scan_row(
        _sample_v3_signal(),
        cycle=12,
        timestamp="2026-04-20T11:00:00+00:00",
    )
    identity = scan["identity"]
    ex_key = obs_shadow._exact_key(identity)
    st_key = obs_shadow._strategy_key(identity)
    fam_key = obs_shadow._family_key(identity)
    bank = {
        "exact": {
            ex_key: {
                "identity": identity,
                "n": 2,
                "wins": 2,
                "losses": 0,
                "scratches": 0,
                "sum_pnl_usd": 220.0,
                "avg_pnl_usd": 110.0,
                "win_rate": 1.0,
            }
        },
        "strategy": {st_key: {"identity": identity, "n": 4, "wins": 1, "losses": 3, "scratches": 0, "sum_pnl_usd": -40.0, "avg_pnl_usd": -10.0, "win_rate": 0.25}},
        "family": {fam_key: {"identity": identity, "n": 6, "wins": 2, "losses": 4, "scratches": 0, "sum_pnl_usd": -60.0, "avg_pnl_usd": -10.0, "win_rate": 0.3333}},
    }
    decision = obs_shadow.decide_shadow(scan, bank)
    assert decision["decision"] == "TAKE"
    assert decision["bank_level"] == "exact"


# =============================================================================
# Journal reader classifier
# =============================================================================

def test_journal_classify_gate_line():
    cat = jrdr._classify(
        "[GATE:debounce] PASSED symbol=EUR_USD reason=No prior entry",
        "6")
    assert cat == "gate"


def test_journal_classify_scorer_line():
    cat = jrdr._classify("[V3_SCORER] base=1 final=2 tier=TAKE", "6")
    assert cat == "scorer_line"


def test_journal_classify_sizing_line():
    cat = jrdr._classify(
        "[SIZING] EUR_USD: 5000 units | equity $10000", "6")
    assert cat == "sizing"


def test_journal_classify_exec_line():
    cat = jrdr._classify("ORDER_FILL tradeID=123 price=1.10", "6")
    assert cat == "exec"


def test_journal_classify_error_routes_to_error():
    cat = jrdr._classify("some random boring error", "3")
    assert cat == "error"


def test_journal_classify_warning_routes_to_warning():
    cat = jrdr._classify("some random warning", "4")
    assert cat == "warning"


def test_journal_noise_is_dropped():
    assert jrdr._is_noise("Percentile filter applied to XXX")
    assert jrdr._is_noise("Insufficient bars for AUD_CHF")
    assert jrdr._is_noise("HTTP 502 Bad Gateway from broker")
    assert not jrdr._is_noise("[V3_SCORER] base=1 final=1")


def test_gate_line_enrichment_parses_fields(tmp_path, monkeypatch):
    """Observer.drain_journal enriches gate lines with name/passed/reason."""
    # Patch iter_journal_events to yield a canned gate entry
    state = _redirect_paths(tmp_path, monkeypatch)

    def fake_iter(*_args, **_kwargs):
        yield ("gate", {
            "ts": "2026-04-20T14:00:00+00:00",
            "priority": "6",
            "level": "INFO",
            "logger": "scrooge_v3.gate.pipeline",
            "message": ("2026-04-20 14:00:00 [INFO] scrooge_v3.gate.pipeline — "
                        "[GATE:cooldown] PASSED symbol=EUR_USD reason=No active cooldown"),
        })
    monkeypatch.setattr(obs_module, "iter_journal_events", fake_iter)
    obs_module.drain_journal(state)
    lines = [l for l in (tmp_path / "actions.jsonl").read_text().splitlines() if l.strip()]
    assert len(lines) == 1
    rec = json.loads(lines[0])
    assert rec["category"] == "gate"
    assert rec["gate_name"] == "cooldown"
    assert rec["passed"] is True
    assert rec["symbol"] == "EUR_USD"
    assert rec["reason"] == "No active cooldown"


def test_drain_journal_routes_warning_to_bot_logs(tmp_path, monkeypatch):
    state = _redirect_paths(tmp_path, monkeypatch)
    def fake_iter(*_a, **_k):
        yield ("warning", {"ts": "2026-04-20T00:00:00+00:00", "priority": "4",
                           "level": "WARNING", "logger": "foo",
                           "message": "something went sideways"})
    monkeypatch.setattr(obs_module, "iter_journal_events", fake_iter)
    obs_module.drain_journal(state)
    assert (tmp_path / "bot-logs.jsonl").exists()
    assert not (tmp_path / "actions.jsonl").exists()


# =============================================================================
# OANDA fill classifier
# =============================================================================

def test_classify_fill_open():
    tx = {"id": "1502", "time": "2026-04-20T06:08:17Z", "type": "ORDER_FILL",
          "instrument": "NZD_JPY", "price": "93.264", "units": "1105104",
          "pl": "0.0000",
          "tradeOpened": {"tradeID": "1502", "units": "1105104", "price": "93.264"}}
    ev = oanda_module.classify_fill(tx)
    assert ev["kind"] == "open"
    assert ev["trade_ids_opened"] == ["1502"]
    assert ev["realized_pl_usd"] == 0.0


def test_classify_fill_close_loss():
    tx = {"id": "1601", "type": "ORDER_FILL", "instrument": "EUR_USD",
          "price": "1.10", "units": "-1000", "pl": "-12.00",
          "tradesClosed": [{"tradeID": "1503", "realizedPL": "0"}]}
    ev = oanda_module.classify_fill(tx)
    assert ev["kind"] == "close"
    assert ev["realized_pl_usd"] == -12.0


# =============================================================================
# Outcome reconciliation (end-to-end)
# =============================================================================

class _FakePoller:
    def __init__(self, fills_by_since=None, latest_id="1500"):
        self._fills = fills_by_since or {}
        self._calls: list[str] = []
        self._latest = latest_id

    def get_last_transaction_id(self):
        return self._latest

    def fetch_fills_since(self, since_id):
        self._calls.append(since_id)
        return list(self._fills.get(since_id, []))


def test_poll_oanda_primes_cursor_on_first_run(tmp_path, monkeypatch):
    state = _redirect_paths(tmp_path, monkeypatch)
    poller = _FakePoller(latest_id="999")
    closed = obs_module.poll_oanda_outcomes(state, poller)
    assert closed == 0
    assert state.last_transaction_id_seen == "999"
    assert poller._calls == []


def test_trade_open_links_to_scan_row(tmp_path, monkeypatch):
    state = _redirect_paths(tmp_path, monkeypatch)
    state.last_transaction_id_seen = "1000"
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).isoformat()
    (tmp_path / "scans.jsonl").write_text(json.dumps({
        "ts": now, "cycle": 42, "symbol": "EUR_USD", "verdict": "TAKE_LONG",
        "ml_features": {n: 0.0 for n in obs_features.FEATURE_NAMES},
    }) + "\n")
    open_tx = {"id": "1001", "type": "ORDER_FILL", "instrument": "EUR_USD",
               "price": "1.10", "units": "1000", "pl": "0",
               "tradeOpened": {"tradeID": "1001", "units": "1000", "price": "1.10"}}
    poller = _FakePoller(fills_by_since={"1000": [open_tx]})
    obs_module.poll_oanda_outcomes(state, poller)
    rows = [json.loads(l) for l in (tmp_path / "outcomes.jsonl").read_text().splitlines()
            if l.strip()]
    assert len(rows) == 1
    assert rows[0]["kind"] == "trade_open"
    assert rows[0]["matched_scan_cycle"] == 42
    assert rows[0]["matched_scan_verdict"] == "TAKE_LONG"


def test_end_to_end_scan_open_close_produces_outcome_row(tmp_path, monkeypatch):
    """Full flow: scan row → open fill → close fill → two outcome rows."""
    state = _redirect_paths(tmp_path, monkeypatch)
    state.last_transaction_id_seen = "1000"
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).isoformat()
    (tmp_path / "scans.jsonl").write_text(json.dumps({
        "ts": now, "cycle": 42, "symbol": "EUR_USD", "verdict": "TAKE_LONG",
        "ml_features": {n: 0.0 for n in obs_features.FEATURE_NAMES},
    }) + "\n")
    open_tx = {"id": "1001", "type": "ORDER_FILL", "instrument": "EUR_USD",
               "price": "1.10", "units": "1000", "pl": "0",
               "tradeOpened": {"tradeID": "9001", "units": "1000", "price": "1.10"}}
    close_tx = {"id": "1002", "type": "ORDER_FILL", "instrument": "EUR_USD",
                "price": "1.11", "units": "-1000", "pl": "10.0",
                "tradesClosed": [{"tradeID": "9001", "realizedPL": "0"}]}
    poller = _FakePoller(fills_by_since={"1000": [open_tx, close_tx]})
    obs_module.poll_oanda_outcomes(state, poller)
    rows = [json.loads(l) for l in (tmp_path / "outcomes.jsonl").read_text().splitlines()
            if l.strip()]
    kinds = [r["kind"] for r in rows]
    assert kinds == ["trade_open", "trade_close"]
    close_row = rows[1]
    assert close_row["label"] == "win"
    assert close_row["outcome"] == 1
    assert close_row["realized_pnl_usd"] == 10.0
    assert state.total_outcomes == 1


def test_incremental_cursor_does_not_reprocess(tmp_path, monkeypatch):
    state = _redirect_paths(tmp_path, monkeypatch)
    state.last_transaction_id_seen = "2000"
    poller = _FakePoller(fills_by_since={"2000": []})
    obs_module.poll_oanda_outcomes(state, poller)
    obs_module.poll_oanda_outcomes(state, poller)
    assert poller._calls == ["2000", "2000"]


# =============================================================================
# Account snapshot
# =============================================================================

def test_account_snapshot_without_oanda(tmp_path):
    v3_data = {
        "system": {"cycle_count": 5},
        "account": {"balance": 80987.65, "equity": 80987.65,
                    "daily_pnl": -13.7, "position_count": 0},
    }
    row = acct.build_snapshot(v3_data, tmp_path)
    assert row["cycle"] == 5
    assert row["v3_account"]["balance"] == 80987.65
    # Tracker files missing → null
    assert row["cooldowns"] is None
    assert row["daily_circuit"] is None
    assert row["oanda"]["balance"] is None
    assert "ts" in row


def test_account_snapshot_reads_tracker_files(tmp_path):
    (tmp_path / "cooldowns.json").write_text('{"EUR_USD": 1717200000}')
    (tmp_path / "daily_circuit.json").write_text(
        '{"date": "2026-04-20", "tripped": false, "equity_start": 80000}'
    )
    row = acct.build_snapshot({"system": {"cycle_count": 1}, "account": {}}, tmp_path)
    assert row["cooldowns"] == {"EUR_USD": 1717200000}
    assert row["daily_circuit"]["tripped"] is False


# =============================================================================
# Trainer
# =============================================================================

def test_trainer_legacy_loader_still_works(tmp_path, monkeypatch):
    obs_file = tmp_path / "observations.jsonl"
    rows = [
        {"features": {n: 0.1 * i for n in obs_features.FEATURE_NAMES},
         "outcome": i % 2}
        for i in range(3)
    ]
    obs_file.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    monkeypatch.setattr(obs_trainer, "OBSERVATIONS_FILE", obs_file)
    monkeypatch.setattr(obs_trainer, "SCANS_FILE", tmp_path / "scans.jsonl")
    monkeypatch.setattr(obs_trainer, "OUTCOMES_FILE", tmp_path / "outcomes.jsonl")
    monkeypatch.setattr(obs_trainer, "PHASE2_MIN_TRADES", 2)
    X, y, n = obs_trainer.load_training_data()
    assert n == 3
    assert X is not None and X.shape[0] == 3
    assert list(y) == [0.0, 1.0, 0.0]


def test_trainer_scans_outcomes_loader(tmp_path, monkeypatch):
    """Trainer joins scans.jsonl + outcomes.jsonl by symbol + time."""
    from datetime import datetime, timezone, timedelta
    scans_file = tmp_path / "scans.jsonl"
    out_file = tmp_path / "outcomes.jsonl"

    base = datetime.now(timezone.utc)
    scan_rows = []
    close_rows = []
    open_rows = []
    for i in range(3):
        ts = (base - timedelta(minutes=60 - i * 10)).isoformat()
        scan_rows.append({
            "ts": ts, "cycle": i, "symbol": "EUR_USD", "verdict": "TAKE_LONG",
            "ml_features": {n: 0.1 * i for n in obs_features.FEATURE_NAMES},
        })
        open_rows.append({
            "kind": "trade_open", "ts": ts, "trade_id": f"T{i}", "symbol": "EUR_USD",
            "matched_scan_ts": ts,
        })
        close_rows.append({
            "kind": "trade_close", "ts": (base + timedelta(minutes=i)).isoformat(),
            "trade_id": f"T{i}", "symbol": "EUR_USD",
            "label": "win" if i % 2 == 0 else "loss",
            "outcome": 1 if i % 2 == 0 else 0, "realized_pnl_usd": 5 if i % 2 == 0 else -5,
        })

    scans_file.write_text("\n".join(json.dumps(r) for r in scan_rows) + "\n")
    out_file.write_text("\n".join(json.dumps(r) for r in open_rows + close_rows) + "\n")

    monkeypatch.setattr(obs_trainer, "SCANS_FILE", scans_file)
    monkeypatch.setattr(obs_trainer, "OUTCOMES_FILE", out_file)
    monkeypatch.setattr(obs_trainer, "OBSERVATIONS_FILE", tmp_path / "none.jsonl")
    monkeypatch.setattr(obs_trainer, "PHASE2_MIN_TRADES", 2)

    X, y, n = obs_trainer.load_training_data()
    assert n == 3
    assert X is not None
    assert list(y) == [1.0, 0.0, 1.0]


# =============================================================================
# Schema invariants
# =============================================================================

def test_scans_row_has_47_plus_ml_features():
    sig = _sample_v3_signal()
    parsed = spar.parse_v3_scorer_line(_SCORER_LINE)
    row = obs_features.build_scan_row(sig, cycle=1,
                                      timestamp="2026-04-20T00:00:00+00:00",
                                      scorer_log_parsed=parsed)
    assert len(row["ml_features"]) >= 47


def test_scans_row_every_feature_name_is_a_float():
    sig = _sample_v3_signal()
    row = obs_features.build_scan_row(sig, cycle=1,
                                      timestamp="2026-04-20T00:00:00+00:00")
    for name in obs_features.FEATURE_NAMES:
        assert isinstance(row["ml_features"][name], float)


def test_actions_row_schema_required_keys(tmp_path, monkeypatch):
    """Any action row written by drain_journal has {ts, category, level,
    logger, message} at minimum."""
    state = _redirect_paths(tmp_path, monkeypatch)
    def fake_iter(*_a, **_k):
        yield ("sizing", {"ts": "2026-04-20T01:02:03+00:00", "priority": "6",
                          "level": "INFO", "logger": "scrooge_v3.execution.sizing",
                          "message": "[SIZING] EUR_USD: 123 units"})
    monkeypatch.setattr(obs_module, "iter_journal_events", fake_iter)
    obs_module.drain_journal(state)
    rec = json.loads((tmp_path / "actions.jsonl").read_text().splitlines()[0])
    for k in ("ts", "category", "level", "logger", "message"):
        assert k in rec


def test_outcomes_row_schema_required_keys(tmp_path, monkeypatch):
    state = _redirect_paths(tmp_path, monkeypatch)
    state.last_transaction_id_seen = "1"
    tx = {"id": "2", "type": "ORDER_FILL", "instrument": "USD_JPY",
          "price": "150.0", "units": "-100", "pl": "7.5",
          "tradesClosed": [{"tradeID": "X1", "realizedPL": "0"}]}
    poller = _FakePoller(fills_by_since={"1": [tx]})
    obs_module.poll_oanda_outcomes(state, poller)
    rec = json.loads((tmp_path / "outcomes.jsonl").read_text().splitlines()[0])
    for k in ("kind", "ts", "trade_id", "symbol", "label", "outcome",
              "realized_pnl_usd", "exit_price"):
        assert k in rec
