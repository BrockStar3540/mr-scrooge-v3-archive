# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Configuration.

Paths, thresholds, and phase triggers. The observer writes to FIVE JSONL
files in `data/ml-observer/` that downstream training joins by
(ts, symbol, trade_id, cycle_id):

    scans.jsonl     — one row per scored candidate per cycle (the full
                      47+ ML-feature vector + context + gates)
    actions.jsonl   — bot actions (orders, fills, SL moves, harvests,
                      gate blocks, circuit trips, cooldowns)
    account.jsonl   — periodic account + risk-tracker snapshots
    outcomes.jsonl  — trade_open / trade_close rows from OANDA poller
    bot-logs.jsonl  — filtered WARNING/ERROR and uncategorized info
                      from journald

2026-04-20: Scope expansion — production-grade data pipeline, 5 output
            files, full-fidelity V3 scorer capture, journald tailer,
            OANDA summary snapshots, risk-tracker JSON ingestion.
2026-04-19: Added OANDA transaction polling + separate outcomes.jsonl.
2026-04-16: Rewired for V3 only. V1 and V2 are decommissioned.
"""

from pathlib import Path

# --- V3 API (read-only) ---
V3_API_URL = "http://127.0.0.1:8084/api/data"
V3_AUTH = ("admin", "scrooge2026")

# --- Paths ---
OBS_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent  # mr-scrooge-v3/
DATA_DIR = OBS_DIR / "data" / "ml-observer"
V3_DATA_DIR = OBS_DIR / "data"          # mr-scrooge-v3/data/ (risk tracker JSONs)
LOG_DIR = OBS_DIR / "logs"              # shared V3 logs dir

# --- OANDA credentials (loaded from V3 .env at runtime, read-only) ---
OANDA_ENV_PATH = OBS_DIR / ".env"

# --- Output files (five-file schema) ---
SCANS_FILE        = DATA_DIR / "scans.jsonl"
ACTIONS_FILE      = DATA_DIR / "actions.jsonl"
ACCOUNT_FILE      = DATA_DIR / "account.jsonl"
OUTCOMES_FILE     = DATA_DIR / "outcomes.jsonl"
BOT_LOGS_FILE     = DATA_DIR / "bot-logs.jsonl"

# --- Observer state + model ---
STATE_FILE        = DATA_DIR / "observer-state.json"
MODEL_FILE        = DATA_DIR / "model.xgb"
PROTESTS_FILE     = DATA_DIR / "ml-protests.jsonl"
SHADOW_DECISIONS_FILE = DATA_DIR / "shadow-decisions.jsonl"
SHADOW_TRADES_FILE    = DATA_DIR / "shadow-trades.jsonl"
SHADOW_BANK_FILE      = DATA_DIR / "shadow-bank.json"
SHADOW_COMPARISON_FILE = DATA_DIR / "shadow-comparison.json"

# --- journald cursor (resume reads across observer restarts) ---
JOURNAL_CURSOR_FILE = DATA_DIR / "journal.cursor"
JOURNAL_UNIT = "mr-scrooge-v3.service"
JOURNAL_MAX_ENTRIES_PER_CYCLE = 10000

# --- Legacy (still used for reads during backfill) ---
OBSERVATIONS_FILE = DATA_DIR / "observations.jsonl"  # legacy — no new writes

# --- Cycle timing ---
CYCLE_SECONDS = 300  # 5 min, matches bot cycle

# --- Phase thresholds ---
PHASE2_MIN_TRADES = 50          # trades with outcomes before training
PHASE3_MIN_CV_ACCURACY = 0.60   # min CV accuracy before advising
RETRAIN_INTERVAL_TRADES = 25    # retrain after this many new closed trades

# --- Advisor thresholds ---
PROTEST_CONFIDENCE = 0.70

# --- Current-corpus shadow observer thresholds ---
SHADOW_MIN_TRADES_EXACT = 2
SHADOW_MIN_TRADES_STRATEGY = 3
SHADOW_MIN_TRADES_FAMILY = 5
SHADOW_MIN_WIN_RATE = 0.45
SHADOW_MIN_AVG_PNL_USD = 0.0

# --- Trade association window ---
TRADE_ASSOCIATION_WINDOW_SEC = 600  # 10 min

# --- XGBoost parameters ---
XGB_PARAMS = {
    "max_depth": 4,
    "eta": 0.1,
    "objective": "binary:logistic",
    "eval_metric": "logloss",
    "nthread": 2,
    "seed": 42,
}
XGB_NUM_ROUNDS = 100
XGB_EARLY_STOPPING = 10
XGB_CV_FOLDS = 5
