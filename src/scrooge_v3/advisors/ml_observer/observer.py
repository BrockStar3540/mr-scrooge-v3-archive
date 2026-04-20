#!/usr/bin/env python3
# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Main Loop (V3)
Watches Scrooge V3 passively via its /api/data endpoint and OANDA transactions.
Collects signal data, associates live trades by symbol+time, polls OANDA for
closed-trade outcomes, trains XGBoost after enough labeled trades, logs protests
when ML disagrees with bot decisions. Never takes action — read-only forever.

2026-04-19: Split outcomes into outcomes.jsonl (observations immutable).
            OANDA transactions polled via sinceid cursor for incremental labeling.
            Fixed cycle-dedup bug that froze the observer after a V3 restart.
2026-04-16: Rewired from V1/V2 status.json to V3 REST API.

Phases:
  1. Collector  — record every evaluated signal + outcomes
  2. Learner    — train model after 50+ closed trades
  3. Advisor    — log protests when ML confidence > 70%
"""

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Set

import requests

from config import (
    V3_API_URL, V3_AUTH, OANDA_ENV_PATH,
    CYCLE_SECONDS, OBSERVATIONS_FILE, OUTCOMES_FILE, PROTESTS_FILE,
    STATE_FILE, MODEL_FILE, LOG_DIR,
    PHASE2_MIN_TRADES, RETRAIN_INTERVAL_TRADES, PROTEST_CONFIDENCE,
    TRADE_ASSOCIATION_WINDOW_SEC,
)
from features import extract_features
from trainer import train_model, predict
from oanda_poll import OandaPoller, classify_fill

# --- Logging setup ---
LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "ml-observer.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("ml-observer")


class ObserverState:
    """Persistent state across restarts."""

    def __init__(self):
        self.phase = 1
        self.total_observations = 0
        self.total_outcomes = 0
        self.last_train_outcomes = 0
        self.cv_accuracy = 0.0
        # Per-cycle dedup — track exact last cycle we've RECORDED.
        # Using equality, not ordering, so V3 restarts (cycle counter reset)
        # don't freeze us forever.
        self.last_cycle_seen: Optional[int] = None
        # OANDA transactions cursor (string id).
        self.last_transaction_id_seen: Optional[str] = None
        self.known_trade_ids: Set[str] = set()

    def save(self):
        data = {
            "phase": self.phase,
            "total_observations": self.total_observations,
            "total_outcomes": self.total_outcomes,
            "last_train_outcomes": self.last_train_outcomes,
            "cv_accuracy": self.cv_accuracy,
            "last_cycle_seen": self.last_cycle_seen,
            "last_transaction_id_seen": self.last_transaction_id_seen,
            "known_trade_ids": list(self.known_trade_ids),
        }
        STATE_FILE.write_text(json.dumps(data, indent=2))

    def load(self):
        if STATE_FILE.exists():
            try:
                data = json.loads(STATE_FILE.read_text())
                self.phase = data.get("phase", 1)
                self.total_observations = data.get("total_observations", 0)
                self.total_outcomes = data.get("total_outcomes", 0)
                self.last_train_outcomes = data.get("last_train_outcomes", 0)
                self.cv_accuracy = data.get("cv_accuracy", 0.0)
                self.last_cycle_seen = data.get("last_cycle_seen")
                self.last_transaction_id_seen = data.get("last_transaction_id_seen")
                self.known_trade_ids = set(data.get("known_trade_ids", []))
            except (json.JSONDecodeError, KeyError):
                log.warning("Corrupt state file, starting fresh")


def _append_jsonl(path: Path, record: dict):
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")


def fetch_v3_data() -> dict | None:
    """Fetch current state from V3 dashboard API."""
    try:
        r = requests.get(V3_API_URL, auth=V3_AUTH, timeout=10)
        if r.status_code == 200:
            return r.json()
        log.warning("V3 API returned %s", r.status_code)
    except requests.RequestException as e:
        log.warning("V3 API fetch failed: %s", e)
    return None


def collect_signals(state: ObserverState, data: dict) -> int:
    """Phase 1: Extract signals from V3 API response and store features.

    Returns count of observations written this cycle.
    """
    system = data.get("system", {})
    cycle = system.get("cycle_count", 0)

    # Dedup: only record if cycle changed. Using != (not <=) so V3 restarts
    # don't freeze us.
    if state.last_cycle_seen is not None and cycle == state.last_cycle_seen:
        return 0
    state.last_cycle_seen = cycle

    signals = data.get("signals", [])
    if not signals:
        return 0

    timestamp = datetime.now(timezone.utc).isoformat()
    recorded = 0

    for signal in signals:
        symbol = signal.get("symbol", "")
        if not symbol:
            continue

        verdict = signal.get("verdict", "")
        scorer = signal.get("scorer", {})

        # Only record signals that were actually scored.
        if not scorer.get("breakdown"):
            continue

        extracted = extract_features(signal, timestamp)

        observation = {
            "ts": timestamp,
            "cycle": cycle,
            "symbol": symbol,
            "verdict": verdict,
            "v3_score": scorer.get("score", 0),
            "v3_tier": scorer.get("tier", ""),
            "fam": scorer.get("fam", scorer.get("family", "")),
            "features": extracted["features"],
            "metadata": extracted["metadata"],
            # Observations are immutable — trade_id / outcome live in outcomes.jsonl.
            "trade_id": None,
        }

        _append_jsonl(OBSERVATIONS_FILE, observation)
        recorded += 1

    state.total_observations += recorded
    if recorded > 0:
        log.info("[v3] Recorded %d signals (cycle %s)", recorded, cycle)
    return recorded


def _find_obs_for_trade(symbol: str, window_sec: int,
                        observations_path: Optional[Path] = None) -> Optional[dict]:
    """
    Look backwards through observations.jsonl for the most recent TAKE_* signal
    of this symbol within the window. Returns the raw observation dict, or None.
    """
    path = observations_path or OBSERVATIONS_FILE
    if not path.exists():
        return None
    cutoff = datetime.now(timezone.utc).timestamp() - window_sec
    try:
        lines = path.read_text().splitlines()
    except OSError:
        return None
    # Walk bottom-up, capped at a few cycles worth.
    for line in reversed(lines[-400:]):
        if not line.strip():
            continue
        try:
            obs = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obs.get("symbol") != symbol:
            continue
        if not str(obs.get("verdict", "")).startswith("TAKE_"):
            continue
        try:
            ts = datetime.fromisoformat(obs["ts"]).timestamp()
        except (KeyError, ValueError):
            continue
        if ts < cutoff:
            break
        return obs
    return None


def poll_oanda_outcomes(state: ObserverState, poller: OandaPoller) -> int:
    """Poll OANDA transactions since last cursor.

    Returns count of closed-trade outcomes recorded this call.
    """
    if state.last_transaction_id_seen is None:
        # Prime cursor to current latest so we don't re-process history.
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
                matched = _find_obs_for_trade(ev["symbol"], TRADE_ASSOCIATION_WINDOW_SEC)
                link = {
                    "kind": "trade_open",
                    "ts": ev["time"],
                    "trade_id": trade_id,
                    "symbol": ev["symbol"],
                    "price": ev["price"],
                    "units": ev["units"],
                    "matched_observation_ts": matched["ts"] if matched else None,
                    "matched_observation_cycle": matched["cycle"] if matched else None,
                    "matched_observation_verdict": matched["verdict"] if matched else None,
                }
                _append_jsonl(OUTCOMES_FILE, link)
                state.known_trade_ids.add(trade_id)
                log.info("[oanda] trade_open %s %s matched=%s",
                         trade_id, ev["symbol"], bool(matched))
        elif ev["kind"] == "close":
            for trade_id in ev["trade_ids_closed"]:
                pl = ev["realized_pl_usd"]
                if pl > 0:
                    label = "win"
                    outcome_bin = 1
                elif pl < 0:
                    label = "loss"
                    outcome_bin = 0
                else:
                    label = "scratch"
                    outcome_bin = 0
                record = {
                    "kind": "trade_close",
                    "ts": ev["time"],
                    "trade_id": trade_id,
                    "symbol": ev["symbol"],
                    "label": label,
                    "outcome": outcome_bin,
                    "realized_pnl_usd": pl,
                    "exit_price": ev["price"],
                }
                _append_jsonl(OUTCOMES_FILE, record)
                state.total_outcomes += 1
                closed_count += 1
                log.info("[oanda] trade_close %s %s pl=%.2f label=%s",
                         trade_id, ev["symbol"], pl, label)

    state.last_transaction_id_seen = max_id_seen
    return closed_count


def maybe_train(state: ObserverState) -> bool:
    """Phase 2: Train model if we have enough data. Returns True if model is ready."""
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
    """Phase 3: Run predictions on current signals, log protests."""
    if state.phase < 3:
        return
    if not MODEL_FILE.exists():
        return

    signals = data.get("signals", [])
    timestamp = datetime.now(timezone.utc).isoformat()

    for signal in signals:
        symbol = signal.get("symbol", "")
        verdict = signal.get("verdict", "")
        scorer = signal.get("scorer", {})
        if not symbol or not scorer.get("breakdown"):
            continue

        extracted = extract_features(signal, timestamp)
        prob, pred_label = predict(extracted["features"])

        bot_entering = verdict.startswith("TAKE")
        bot_skipping = verdict in ("NO_CANDIDATE", "V3_REJECT", "V3_BLOCKED")
        ml_says_win = prob > PROTEST_CONFIDENCE
        ml_says_loss = prob < (1 - PROTEST_CONFIDENCE)

        protest = None
        if bot_entering and ml_says_loss:
            protest = {
                "type": "DISAGREE_ENTRY",
                "detail": f"Bot entering ({verdict}) but ML predicts LOSS "
                          f"(P(win)={prob:.2f}, threshold={1-PROTEST_CONFIDENCE:.2f})",
            }
        elif bot_skipping and ml_says_win:
            protest = {
                "type": "MISSED_OPPORTUNITY",
                "detail": f"Bot skipped ({verdict}) but ML predicts WIN "
                          f"(P(win)={prob:.2f}, threshold={PROTEST_CONFIDENCE:.2f})",
            }

        if protest:
            record = {
                "ts": timestamp,
                "bot": "v3",
                "symbol": symbol,
                "bot_verdict": verdict,
                "ml_prediction": "WIN" if pred_label == 1 else "LOSS",
                "ml_confidence": round(prob, 4),
                "protest_type": protest["type"],
                "detail": protest["detail"],
                "v3_score": scorer.get("score", 0),
                "regime_score": extracted["features"].get("regime_score", 0),
                "features": extracted["features"],
            }
            _append_jsonl(PROTESTS_FILE, record)
            log.info("[v3] PROTEST %s: %s — %s",
                     protest["type"], symbol, protest["detail"])


def run():
    log.info("=" * 60)
    log.info("ML Observer starting — V3 mode")
    log.info("V3 API: %s", V3_API_URL)
    log.info("OANDA env: %s", OANDA_ENV_PATH)
    log.info("Cycle: %ss", CYCLE_SECONDS)
    log.info("=" * 60)

    state = ObserverState()
    state.load()
    log.info("Resumed at phase=%s observations=%d outcomes=%d cursor=%s last_cycle_seen=%s",
             state.phase, state.total_observations, state.total_outcomes,
             state.last_transaction_id_seen, state.last_cycle_seen)

    poller = OandaPoller.from_env(OANDA_ENV_PATH)
    if poller is None:
        log.warning("OANDA poller disabled — outcomes will NOT be labeled")

    while True:
        try:
            cycle_start = time.time()

            data = fetch_v3_data()
            if data:
                collect_signals(state, data)

                if poller:
                    poll_oanda_outcomes(state, poller)

                model_ready = maybe_train(state)

                if model_ready and state.phase >= 3:
                    advise(state, data)

            state.save()

            log.info("Cycle complete: phase=%s obs=%d outcomes=%d accuracy=%.2f cursor=%s",
                     state.phase, state.total_observations, state.total_outcomes,
                     state.cv_accuracy, state.last_transaction_id_seen)

            elapsed = time.time() - cycle_start
            sleep_time = max(0, CYCLE_SECONDS - elapsed)
            time.sleep(sleep_time)

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
