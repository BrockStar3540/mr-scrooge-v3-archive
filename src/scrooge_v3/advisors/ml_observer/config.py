# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Configuration
Paths, thresholds, and phase triggers.

2026-04-19: Added OANDA transaction polling + separate outcomes.jsonl.
2026-04-16: Rewired for V3 only. V1 and V2 are decommissioned.
"""

from pathlib import Path

# --- V3 API (read-only) ---
V3_API_URL = "http://127.0.0.1:8084/api/data"
V3_AUTH = ("admin", "scrooge2026")

# --- OANDA credentials (loaded from V3 .env at runtime, read-only) ---
OANDA_ENV_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent / ".env"

# --- Observer data directory ---
OBS_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent  # mr-scrooge-v3/
DATA_DIR = OBS_DIR / "data" / "ml-observer"
LOG_DIR = OBS_DIR / "logs"  # shared V3 logs dir

OBSERVATIONS_FILE = DATA_DIR / "observations.jsonl"
OUTCOMES_FILE = DATA_DIR / "outcomes.jsonl"  # separate file — observations stay immutable
PROTESTS_FILE = DATA_DIR / "ml-protests.jsonl"
MODEL_FILE = DATA_DIR / "model.xgb"
STATE_FILE = DATA_DIR / "observer-state.json"

# --- Cycle timing ---
CYCLE_SECONDS = 300  # 5 minutes, matches bot cycle

# --- Phase thresholds ---
PHASE2_MIN_TRADES = 50       # trades with outcomes before training
PHASE3_MIN_CV_ACCURACY = 0.60  # minimum CV accuracy to start advising
RETRAIN_INTERVAL_TRADES = 25   # retrain after this many new closed trades

# --- Advisor thresholds ---
PROTEST_CONFIDENCE = 0.70  # minimum ML confidence to log a protest

# --- Trade association window ---
# When an OANDA tradeOpened fill lands, associate with the most recent
# observation of same symbol + TAKE_* verdict within this window.
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
