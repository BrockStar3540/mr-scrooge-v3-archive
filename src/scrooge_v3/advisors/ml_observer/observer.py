#!/usr/bin/env python3
# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Main Loop (V3)
Watches Scrooge V3 passively via its /api/data endpoint.
Collects signal data, trains XGBoost after enough trades,
logs protests when ML disagrees with bot decisions.
Never takes action — read-only forever.

2026-04-16: Rewired from V1/V2 status.json to V3 REST API.
V1 and V2 are decommissioned. Old observations are archived.

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
from typing import Dict, Set

import requests

from config import (
    V3_API_URL, V3_AUTH,
    CYCLE_SECONDS, OBSERVATIONS_FILE, PROTESTS_FILE,
    STATE_FILE, MODEL_FILE, LOG_DIR,
    PHASE2_MIN_TRADES, RETRAIN_INTERVAL_TRADES, PROTEST_CONFIDENCE,
)
from features import extract_features
from trainer import load_training_data, train_model, predict

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
        self.last_cycle_count = 0  # V3 cycle dedup
        self.known_trade_ids: Set[str] = set()  # track closed trades

    def save(self):
        data = {
            "phase": self.phase,
            "total_observations": self.total_observations,
            "total_outcomes": self.total_outcomes,
            "last_train_outcomes": self.last_train_outcomes,
            "cv_accuracy": self.cv_accuracy,
            "last_cycle_count": self.last_cycle_count,
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
                self.last_cycle_count = data.get("last_cycle_count", 0)
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
        log.warning(f"V3 API returned {r.status_code}")
    except requests.RequestException as e:
        log.warning(f"V3 API fetch failed: {e}")
    return None


def collect_signals(state: ObserverState, data: dict):
    """Phase 1: Extract signals from V3 API response and store features."""
    system = data.get("system", {})
    cycle = system.get("cycle_count", 0)

    # Dedup by cycle count
    if cycle <= state.last_cycle_count:
        return
    state.last_cycle_count = cycle

    signals = data.get("signals", [])
    if not signals:
        return

    timestamp = datetime.now(timezone.utc).isoformat()
    recorded = 0

    for signal in signals:
        symbol = signal.get("symbol", "")
        if not symbol:
            continue

        verdict = signal.get("verdict", "")
        scorer = signal.get("scorer", {})

        # Only record signals that were actually scored
        if not scorer.get("score") and not scorer.get("breakdown"):
            continue

        extracted = extract_features(signal, timestamp)

        observation = {
            "ts": timestamp,
            "bot": "v3",
            "cycle": cycle,
            "symbol": symbol,
            "verdict": verdict,
            "v3_score": scorer.get("score", 0),
            "v3_tier": scorer.get("tier", ""),
            "features": extracted["features"],
            "metadata": extracted["metadata"],
            "trade_id": None,
            "outcome": None,
            "outcome_pnl": None,
        }

        _append_jsonl(OBSERVATIONS_FILE, observation)
        recorded += 1

    state.total_observations += recorded
    if recorded > 0:
        log.info(f"[v3] Recorded {recorded} signals (cycle {cycle})")


def check_outcomes(state: ObserverState, data: dict):
    """Check V3 recent_closes for new trade outcomes."""
    recent_closes = data.get("recent_closes", [])

    for close in recent_closes:
        trade_id = close.get("trade_id", "")
        if not trade_id or trade_id in state.known_trade_ids:
            continue

        state.known_trade_ids.add(trade_id)

        pnl = close.get("realized_pl", 0.0)
        outcome = 1 if pnl > 0 else 0

        outcome_record = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "bot": "v3",
            "cycle": -1,
            "symbol": close.get("symbol", ""),
            "verdict": "TRADE_CLOSED",
            "v3_score": 0,
            "v3_tier": "",
            "features": {k: 0.0 for k in __import__("features").FEATURE_NAMES},
            "metadata": {
                "symbol": close.get("symbol", ""),
                "verdict": "TRADE_CLOSED",
                "trade_id": trade_id,
            },
            "trade_id": trade_id,
            "outcome": outcome,
            "outcome_pnl": pnl,
        }

        _append_jsonl(OBSERVATIONS_FILE, outcome_record)
        state.total_outcomes += 1
        log.info(f"[v3] Trade outcome: {close.get('symbol')} "
                 f"pnl={pnl:.2f} outcome={'WIN' if outcome else 'LOSS'}")


def maybe_train(state: ObserverState) -> bool:
    """Phase 2: Train model if we have enough data. Returns True if model is ready."""
    new_outcomes = state.total_outcomes - state.last_train_outcomes

    needs_initial = not MODEL_FILE.exists() and state.total_outcomes >= PHASE2_MIN_TRADES
    needs_retrain = MODEL_FILE.exists() and new_outcomes >= RETRAIN_INTERVAL_TRADES

    if not (needs_initial or needs_retrain):
        return MODEL_FILE.exists()

    log.info(f"Training triggered: outcomes={state.total_outcomes} "
             f"new_since_last={new_outcomes}")

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
        if not symbol or not scorer.get("score"):
            continue

        extracted = extract_features(signal, timestamp)
        prob, pred_label = predict(extracted["features"])

        # Determine if ML disagrees with bot
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
            log.info(f"[v3] PROTEST {protest['type']}: "
                     f"{symbol} — {protest['detail']}")


def run():
    log.info("=" * 60)
    log.info("ML Observer starting — V3 mode")
    log.info(f"V3 API: {V3_API_URL}")
    log.info(f"Cycle: {CYCLE_SECONDS}s")
    log.info("V1 and V2 are decommissioned. Watching V3 only.")
    log.info("=" * 60)

    state = ObserverState()
    state.load()
    log.info(f"Resumed at phase={state.phase} "
             f"observations={state.total_observations} "
             f"outcomes={state.total_outcomes}")

    while True:
        try:
            cycle_start = time.time()

            # Fetch V3 data
            data = fetch_v3_data()
            if data:
                # Phase 1: Always collect
                collect_signals(state, data)

                # Check for trade outcomes
                check_outcomes(state, data)

                # Phase 2: Train if ready
                model_ready = maybe_train(state)

                # Phase 3: Advise if model is ready and accurate enough
                if model_ready and state.phase >= 3:
                    advise(state, data)

            # Save state
            state.save()

            # Log phase status
            log.info(f"Cycle complete: phase={state.phase} "
                     f"obs={state.total_observations} "
                     f"outcomes={state.total_outcomes} "
                     f"accuracy={state.cv_accuracy:.2f}")

            elapsed = time.time() - cycle_start
            sleep_time = max(0, CYCLE_SECONDS - elapsed)
            time.sleep(sleep_time)

        except KeyboardInterrupt:
            log.info("Shutting down (keyboard interrupt)")
            state.save()
            break
        except Exception as e:
            log.error(f"Cycle error: {e}", exc_info=True)
            state.save()
            time.sleep(30)


if __name__ == "__main__":
    run()
