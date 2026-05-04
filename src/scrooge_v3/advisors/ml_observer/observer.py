#!/usr/bin/env python3
# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Main Loop (V3, expanded scope).

Each 5-minute cycle:
  1. Fetch V3 /api/data (signals + account + system).
  2. Drain journald via persisted cursor → categorize every line:
     - V3_SCORER log lines are buffered and merged per (cycle, symbol)
       into the scan rows.
     - Gate/exec/tracker/recovery/circuit/cooldown → actions.jsonl.
     - WARNING/ERROR/other → bot-logs.jsonl.
  3. Build one scan row per (cycle, symbol, scored) → scans.jsonl.
  4. Snapshot account + risk-tracker JSONs → account.jsonl.
  5. Poll OANDA ORDER_FILL transactions via cursor → outcomes.jsonl.
  6. If enough labeled trades, train XGBoost; if accurate enough, advise.

Read-only with respect to V3 state. The only files written are under
`data/ml-observer/`.

2026-04-20: Rewritten for five-file schema + journald ingestion.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

# Flat-import style for systemd drop-in launch convenience.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import (  # noqa: E402
    V3_API_URL, V3_AUTH, OANDA_ENV_PATH,
    CYCLE_SECONDS, V3_DATA_DIR,
    SCANS_FILE, ACTIONS_FILE, ACCOUNT_FILE, OUTCOMES_FILE, BOT_LOGS_FILE,
    STATE_FILE, MODEL_FILE, PROTESTS_FILE,
    JOURNAL_CURSOR_FILE, JOURNAL_UNIT, JOURNAL_MAX_ENTRIES_PER_CYCLE,
    LOG_DIR, DATA_DIR,
    PHASE2_MIN_TRADES, RETRAIN_INTERVAL_TRADES, PROTEST_CONFIDENCE,
    TRADE_ASSOCIATION_WINDOW_SEC,
)
# Patch B.right: order_id → strategy attribution lookup. Reads the bot's
# data/order-attribution.jsonl deterministically; no time-window walk.
ATTRIBUTION_FILE = V3_DATA_DIR / "order-attribution.jsonl"
from scrooge_v3.telemetry.order_attribution import lookup_attribution  # noqa: E402
from features import build_scan_row, extract_features, FEATURE_NAMES  # noqa: E402
from v3_scorer_parser import parse_v3_scorer_line  # noqa: E402
from journal_reader import iter_journal_events  # noqa: E402
from account_snapshot import build_snapshot  # noqa: E402
from oanda_poll import OandaPoller, classify_fill, load_env  # noqa: E402
from trainer import train_model, predict  # noqa: E402


# --- Logging setup ---
LOG_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "ml-observer.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("ml-observer")


# ----------------------------- State -----------------------------

class ObserverState:
    """Persistent state across restarts."""

    def __init__(self):
        self.phase = 1
        self.total_scans = 0
        self.total_actions = 0
        self.total_account_snapshots = 0
        self.total_outcomes = 0
        self.total_bot_logs = 0
        self.last_train_outcomes = 0
        self.cv_accuracy = 0.0
        self.last_cycle_seen: Optional[int] = None
        self.last_transaction_id_seen: Optional[str] = None
        self.known_trade_ids: set = set()

    def save(self):
        STATE_FILE.write_text(json.dumps({
            "phase": self.phase,
            "total_scans": self.total_scans,
            "total_actions": self.total_actions,
            "total_account_snapshots": self.total_account_snapshots,
            "total_outcomes": self.total_outcomes,
            "total_bot_logs": self.total_bot_logs,
            "last_train_outcomes": self.last_train_outcomes,
            "cv_accuracy": self.cv_accuracy,
            "last_cycle_seen": self.last_cycle_seen,
            "last_transaction_id_seen": self.last_transaction_id_seen,
            "known_trade_ids": list(self.known_trade_ids),
        }, indent=2))

    def load(self):
        if not STATE_FILE.exists():
            return
        try:
            data = json.loads(STATE_FILE.read_text())
        except (OSError, json.JSONDecodeError):
            log.warning("Corrupt state file, starting fresh")
            return
        self.phase = data.get("phase", 1)
        self.total_scans = data.get("total_scans", data.get("total_observations", 0))
        self.total_actions = data.get("total_actions", 0)
        self.total_account_snapshots = data.get("total_account_snapshots", 0)
        self.total_outcomes = data.get("total_outcomes", 0)
        self.total_bot_logs = data.get("total_bot_logs", 0)
        self.last_train_outcomes = data.get("last_train_outcomes", 0)
        self.cv_accuracy = data.get("cv_accuracy", 0.0)
        self.last_cycle_seen = data.get("last_cycle_seen")
        self.last_transaction_id_seen = data.get("last_transaction_id_seen")
        self.known_trade_ids = set(data.get("known_trade_ids", []))


def _append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(record, default=str) + "\n")


# ----------------------------- V3 API -----------------------------

def fetch_v3_data() -> Optional[dict]:
    try:
        r = requests.get(V3_API_URL, auth=V3_AUTH, timeout=10)
        if r.status_code == 200:
            return r.json()
        log.warning("V3 API returned %s", r.status_code)
    except requests.RequestException as e:
        log.warning("V3 API fetch failed: %s", e)
    return None


# ----------------------------- Journal drain -----------------------------

# Regex to extract a symbol from gate/sizing/exec lines so we can key
# per-symbol scorer-log merges.
_SYMBOL_RX = re.compile(r"symbol=([A-Z]{3}_[A-Z]{3})\b|\b([A-Z]{3}_[A-Z]{3})[:\s]")


def _extract_symbol(msg: str) -> Optional[str]:
    m = _SYMBOL_RX.search(msg)
    if not m:
        return None
    return m.group(1) or m.group(2)


def drain_journal(state: ObserverState) -> tuple[dict, int, int]:
    """Pull every new journald line; route by category.

    Returns (scorer_lines_by_symbol, action_count_written, bot_log_count_written).

    `scorer_lines_by_symbol` maps symbol -> most recent parsed V3_SCORER
    dict. The observer uses this to enrich the scan row built from the API.
    """
    scorer_by_symbol: dict[str, dict] = {}
    actions_written = 0
    bot_logs_written = 0

    for category, rec in iter_journal_events(
        JOURNAL_UNIT,
        JOURNAL_CURSOR_FILE,
        max_entries=JOURNAL_MAX_ENTRIES_PER_CYCLE,
    ):
        msg = rec["message"]

        if category == "scorer_line":
            parsed = parse_v3_scorer_line(msg)
            if parsed:
                # We don't know the symbol from the scorer line itself (V3
                # doesn't include it). The observer resolves this per-cycle
                # by correlating order within a cycle; for now we stash by
                # context fingerprint so later we can recover the pairing.
                # Simplest viable key: timestamp + px (unique per symbol/cycle).
                key = f"px={parsed['context'].get('px')}_ts={rec['ts']}"
                scorer_by_symbol[key] = {**parsed, "_log_ts": rec["ts"]}
            continue

        if category in ("gate", "sizing", "exec", "tracker", "recovery",
                        "circuit", "cooldown", "positions", "scan"):
            symbol = _extract_symbol(msg)
            action_rec = {
                "ts": rec["ts"],
                "category": category,
                "symbol": symbol,
                "level": rec["level"],
                "logger": rec["logger"],
                "message": msg,
            }
            # Enrich gate lines with parsed gate_name + passed/reason.
            if category == "gate":
                gm = re.search(
                    r"\[GATE:([A-Za-z_]+)\]\s+(PASSED|FAILED)\s+"
                    r"(?:symbol=\S+\s+)?reason=(.+)$",
                    msg,
                )
                if gm:
                    action_rec["gate_name"] = gm.group(1)
                    action_rec["passed"] = gm.group(2) == "PASSED"
                    action_rec["reason"] = gm.group(3).strip()
            _append_jsonl(ACTIONS_FILE, action_rec)
            actions_written += 1
            continue

        if category in ("warning", "error", "other"):
            _append_jsonl(BOT_LOGS_FILE, {
                "ts": rec["ts"],
                "level": rec["level"],
                "logger": rec["logger"],
                "message": msg,
            })
            bot_logs_written += 1

    state.total_actions += actions_written
    state.total_bot_logs += bot_logs_written
    return scorer_by_symbol, actions_written, bot_logs_written


# ----------------------------- Scans -----------------------------

def collect_scans(
    state: ObserverState,
    data: dict,
    scorer_by_symbol: dict,
) -> int:
    """Build one scan row per scored candidate in the current cycle.

    Skips if the cycle hasn't advanced (dedup).
    """
    system = data.get("system", {})
    cycle = system.get("cycle_count", 0)

    if state.last_cycle_seen is not None and cycle == state.last_cycle_seen:
        return 0
    state.last_cycle_seen = cycle

    signals = data.get("signals", [])
    if not signals:
        return 0

    ts = datetime.now(timezone.utc).isoformat()
    # Order scorer-log entries by timestamp so we can align to API
    # signal order (both are scanned in the same pair order within a
    # cycle). Fallback: iterate entries as we go.
    ordered_parsed = sorted(scorer_by_symbol.values(),
                            key=lambda p: p.get("_log_ts", ""))
    parsed_iter = iter(ordered_parsed)

    recorded = 0
    for signal in signals:
        scorer = signal.get("scorer", {})
        if not scorer.get("breakdown"):
            continue
        # Best-effort pair with the next unconsumed parsed log line.
        # Enrichment is additive — if pairing is wrong, the API-side
        # fields still make the row usable. context.px can be checked
        # offline for alignment.
        parsed = next(parsed_iter, None)
        row = build_scan_row(
            signal,
            cycle=cycle,
            timestamp=ts,
            scorer_log_parsed=parsed,
        )
        _append_jsonl(SCANS_FILE, row)
        recorded += 1

    state.total_scans += recorded
    if recorded:
        log.info("[scans] cycle=%s recorded=%d", cycle, recorded)
    return recorded


# ----------------------------- Account snapshot -----------------------------

def snapshot_account(state: ObserverState, data: Optional[dict]) -> int:
    """Append one account.jsonl row per cycle."""
    env = load_env(OANDA_ENV_PATH)
    row = build_snapshot(
        v3_data=data,
        v3_data_root=V3_DATA_DIR,
        oanda_api_url=env.get("OANDA_API_URL") or os.environ.get("OANDA_API_URL"),
        oanda_account_id=env.get("OANDA_ACCOUNT_ID") or os.environ.get("OANDA_ACCOUNT_ID"),
        oanda_token=env.get("OANDA_API_TOKEN") or os.environ.get("OANDA_API_TOKEN"),
    )
    _append_jsonl(ACCOUNT_FILE, row)
    state.total_account_snapshots += 1
    return 1


# ----------------------------- Outcomes (unchanged logic, different source file) -----------------------------

def _find_scan_for_trade(symbol: str, window_sec: int) -> Optional[dict]:
    """Find most recent TAKE_* scan row for this symbol within the window."""
    path = SCANS_FILE
    if not path.exists():
        # Fall back to legacy observations.jsonl for backfill continuity
        legacy = DATA_DIR / "observations.jsonl"
        path = legacy if legacy.exists() else path
    if not path.exists():
        return None
    cutoff = datetime.now(timezone.utc).timestamp() - window_sec
    try:
        lines = path.read_text().splitlines()
    except OSError:
        return None
    for line in reversed(lines[-800:]):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("symbol") != symbol:
            continue
        if not str(row.get("verdict", "")).startswith("TAKE_"):
            continue
        try:
            ts = datetime.fromisoformat((row.get("ts") or "").replace("Z", "+00:00")).timestamp()
        except (KeyError, ValueError, AttributeError):
            continue
        if ts < cutoff:
            break
        return row
    return None


def poll_oanda_outcomes(state: ObserverState, poller: OandaPoller) -> int:
    """Poll OANDA transactions, emit trade_open / trade_close rows."""
    if state.last_transaction_id_seen is None:
        latest = poller.get_last_transaction_id()
        if latest:
            state.last_transaction_id_seen = latest
            log.info("OANDA cursor primed at lastTransactionID=%s", latest)
        return 0

    fills = poller.fetch_fills_since(state.last_transaction_id_seen)
    if not fills:
        return 0

    closed_count = 0
    max_id_seen = state.last_transaction_id_seen
    for tx in fills:
        ev = classify_fill(tx)
        tx_id = ev["tx_id"]
        try:
            if int(tx_id) > int(max_id_seen or "0"):
                max_id_seen = tx_id
        except (TypeError, ValueError):
            pass

        if ev["kind"] == "open":
            for trade_id in ev["trade_ids_opened"]:
                # Patch B.right: order_id → strategy lookup is the primary
                # attribution path. The bot writes one row per placed order
                # to data/order-attribution.jsonl; we resolve strategy +
                # scan_cycle deterministically from the OANDA orderID. Falls
                # back to the legacy scan window walk only when attribution
                # is missing (pre-patch backfill / externally placed orders).
                attribution = None
                source = "none"
                ord_id = ev.get("order_id") or ""
                if ord_id:
                    attribution = lookup_attribution(ATTRIBUTION_FILE, ord_id)
                    if attribution:
                        source = "order_id_lookup"
                if attribution is None and trade_id:
                    attribution = lookup_attribution(ATTRIBUTION_FILE, trade_id)
                    if attribution:
                        source = "order_id_lookup"
                matched = None
                if attribution is None:
                    matched = _find_scan_for_trade(
                        ev["symbol"], TRADE_ASSOCIATION_WINDOW_SEC,
                    )
                    if matched:
                        source = "scan_window_fallback"
                strategy = (
                    (attribution or {}).get("strategy", "") if attribution
                    else ((matched or {}).get("strategy", "") if matched else "")
                )
                scan_cycle = (
                    (attribution or {}).get("scan_cycle") if attribution
                    else ((matched or {}).get("cycle") if matched else None)
                )
                _append_jsonl(OUTCOMES_FILE, {
                    "kind": "trade_open",
                    "ts": ev["time"],
                    "trade_id": trade_id,
                    "symbol": ev["symbol"],
                    "price": ev["price"],
                    "units": ev["units"],
                    "order_id": ord_id,
                    "strategy": strategy,
                    "scan_cycle": scan_cycle,
                    "tier": (attribution or {}).get("tier", "") if attribution else "",
                    "score": (attribution or {}).get("score", 0) if attribution else 0,
                    "attribution_source": source,
                    # Legacy fields preserved for backward compat.
                    "matched_scan_ts": (
                        matched.get("ts") if matched
                        else ((attribution or {}).get("placed_at")
                              if attribution else None)
                    ),
                    "matched_scan_cycle": scan_cycle,
                    "matched_scan_verdict": matched.get("verdict") if matched else None,
                })
                state.known_trade_ids.add(trade_id)
                log.info("[oanda] trade_open %s %s strategy=%s source=%s",
                         trade_id, ev["symbol"], strategy or "?", source)
        elif ev["kind"] == "close":
            for trade_id in ev["trade_ids_closed"]:
                pl = ev["realized_pl_usd"]
                if pl > 0:
                    label, outcome_bin = "win", 1
                elif pl < 0:
                    label, outcome_bin = "loss", 0
                else:
                    label, outcome_bin = "scratch", 0
                _append_jsonl(OUTCOMES_FILE, {
                    "kind": "trade_close",
                    "ts": ev["time"],
                    "trade_id": trade_id,
                    "symbol": ev["symbol"],
                    "label": label,
                    "outcome": outcome_bin,
                    "realized_pnl_usd": pl,
                    "exit_price": ev["price"],
                })
                state.total_outcomes += 1
                closed_count += 1
                log.info("[oanda] trade_close %s %s pl=%.2f label=%s",
                         trade_id, ev["symbol"], pl, label)

    state.last_transaction_id_seen = max_id_seen
    return closed_count


# ----------------------------- Train/advise -----------------------------

def maybe_train(state: ObserverState) -> bool:
    new_outcomes = state.total_outcomes - state.last_train_outcomes
    needs_initial = not MODEL_FILE.exists() and state.total_outcomes >= PHASE2_MIN_TRADES
    needs_retrain = MODEL_FILE.exists() and new_outcomes >= RETRAIN_INTERVAL_TRADES
    if not (needs_initial or needs_retrain):
        return MODEL_FILE.exists()

    log.info("Training triggered: outcomes=%d new_since_last=%d",
             state.total_outcomes, new_outcomes)
    report = train_model()
    if report["status"] == "trained":
        state.last_train_outcomes = state.total_outcomes
        state.cv_accuracy = report.get("insample_accuracy", 0.0)
        state.phase = max(state.phase, 2)
        if report.get("phase3_ready"):
            state.phase = 3
            log.info("Phase 3 ACTIVATED — advisor mode engaged")
        return True
    return False


def advise(state: ObserverState, data: dict):
    if state.phase < 3 or not MODEL_FILE.exists():
        return
    signals = data.get("signals", [])
    ts = datetime.now(timezone.utc).isoformat()
    for signal in signals:
        symbol = signal.get("symbol", "")
        verdict = signal.get("verdict", "")
        scorer = signal.get("scorer", {})
        if not symbol or not scorer.get("breakdown"):
            continue
        extracted = extract_features(signal, ts)
        prob, pred_label = predict(extracted["features"])

        bot_entering = verdict.startswith("TAKE")
        bot_skipping = verdict in ("NO_CANDIDATE", "V3_REJECT", "V3_BLOCKED")
        ml_says_win = prob > PROTEST_CONFIDENCE
        ml_says_loss = prob < (1 - PROTEST_CONFIDENCE)

        protest = None
        if bot_entering and ml_says_loss:
            protest = {"type": "DISAGREE_ENTRY",
                       "detail": f"Bot entering ({verdict}) but ML predicts LOSS "
                                 f"(P(win)={prob:.2f})"}
        elif bot_skipping and ml_says_win:
            protest = {"type": "MISSED_OPPORTUNITY",
                       "detail": f"Bot skipped ({verdict}) but ML predicts WIN "
                                 f"(P(win)={prob:.2f})"}
        if protest:
            _append_jsonl(PROTESTS_FILE, {
                "ts": ts, "bot": "v3", "symbol": symbol,
                "bot_verdict": verdict,
                "ml_prediction": "WIN" if pred_label == 1 else "LOSS",
                "ml_confidence": round(prob, 4),
                "protest_type": protest["type"], "detail": protest["detail"],
                "v3_score": scorer.get("score", 0),
                "features": extracted["features"],
            })
            log.info("[v3] PROTEST %s: %s — %s",
                     protest["type"], symbol, protest["detail"])


# ----------------------------- Main loop -----------------------------

def run():
    log.info("=" * 60)
    log.info("ML Observer starting — V3 (five-file schema)")
    log.info("V3 API: %s", V3_API_URL)
    log.info("OANDA env: %s", OANDA_ENV_PATH)
    log.info("Cycle: %ss", CYCLE_SECONDS)
    log.info("Feature count: %d", len(FEATURE_NAMES))
    log.info("=" * 60)

    state = ObserverState()
    state.load()
    log.info("Resumed phase=%s scans=%d actions=%d acct=%d outcomes=%d bot_logs=%d "
             "cursor=%s last_cycle=%s",
             state.phase, state.total_scans, state.total_actions,
             state.total_account_snapshots, state.total_outcomes,
             state.total_bot_logs,
             state.last_transaction_id_seen, state.last_cycle_seen)

    poller = OandaPoller.from_env(OANDA_ENV_PATH)
    if poller is None:
        log.warning("OANDA poller disabled — outcomes will NOT be labeled")

    while True:
        try:
            cycle_start = time.time()

            data = fetch_v3_data()

            # Journal drain first so scorer lines are available to enrich scans.
            scorer_map, n_actions, n_logs = drain_journal(state)
            if n_actions or n_logs:
                log.info("[journal] actions=%d logs=%d scorer=%d",
                         n_actions, n_logs, len(scorer_map))

            if data:
                collect_scans(state, data, scorer_map)
                snapshot_account(state, data)
                if poller:
                    poll_oanda_outcomes(state, poller)

                model_ready = maybe_train(state)
                if model_ready and state.phase >= 3:
                    advise(state, data)

            state.save()

            log.info("Cycle: phase=%s scans=%d act=%d acct=%d out=%d logs=%d acc=%.2f",
                     state.phase, state.total_scans, state.total_actions,
                     state.total_account_snapshots, state.total_outcomes,
                     state.total_bot_logs, state.cv_accuracy)

            elapsed = time.time() - cycle_start
            time.sleep(max(0, CYCLE_SECONDS - elapsed))

        except KeyboardInterrupt:
            log.info("Shutting down (keyboard interrupt)")
            state.save()
            break
        except Exception as e:  # noqa: BLE001
            log.error("Cycle error: %s", e, exc_info=True)
            state.save()
            time.sleep(30)


if __name__ == "__main__":
    run()
