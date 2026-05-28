"""LightGBM shadow scorer — observe-only P(win) inference.

Drop-in shadow scorer for V3 scan_pipeline. Loads trained model + feature
schema, extracts the same 14-bucket signature used by ml_router, runs
inference per candidate, logs prediction alongside actual outcome.

NEVER blocks or alters routing. Pure observation layer for evaluating
LightGBM's pick vs scrooge's current best-by-score selection.

Wire-up in scan_pipeline.scan_symbol:
    # after best-by-score selection
    if shadow_scorer is not None and best is not None:
        shadow_scorer.observe(symbol, ctx, best, all_candidates=approved)

Output: /home/ubuntu/mr-scrooge-v3/data/lightgbm_shadow.jsonl
  One line per candidate scored. Fields:
    ts             — UTC ISO timestamp
    symbol         — pair
    strategy       — candidate.strategy
    direction      — long/short
    session        — session_bucket
    regime         — regime label
    buckets        — 14-bucket signature dict
    p_win          — LightGBM P(win) prediction
    was_picked     — bool: did current pipeline select this candidate?
    candidate_score — the score from best-by-score (for delta comparison)
    n_candidates_this_scan — how many candidates were in the pool
"""
from __future__ import annotations

import json
import logging
import threading
import time
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.shadow.lightgbm")

# Singleton — loaded lazily on first observe()
_MODEL: Any = None
_META: dict | None = None
_LOG_PATH: Path | None = None
_LOCK = threading.Lock()


def load(model_dir: str = "/home/ubuntu/mr-scrooge-v3/data/lab_training/v0",
         log_path: str = "/home/ubuntu/mr-scrooge-v3/data/lightgbm_shadow.jsonl") -> bool:
    """Load model + meta. Returns True on success, False if shadow disabled."""
    global _MODEL, _META, _LOG_PATH
    p = Path(model_dir)
    if not (p / "model.txt").exists():
        log.warning("[SHADOW] no model at %s — shadow disabled", model_dir)
        return False
    try:
        import lightgbm as lgb  # noqa
        _MODEL = lgb.Booster(model_file=str(p / "model.txt"))
        _META = json.loads((p / "feature_meta.json").read_text())
        _LOG_PATH = Path(log_path)
        _LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        log.info("[SHADOW] LightGBM v%s loaded — holdout AUC %.4f — log %s",
                 _META.get("version", "?"), _META.get("holdout_auc", -1), log_path)
        return True
    except Exception as e:
        log.exception("[SHADOW] load failed: %s", e)
        _MODEL = None
        return False


def _extract_buckets(ctx) -> dict | None:
    """Pull the 14 categorical buckets from ml_router's helper.

    Re-uses ml_router._compute_buckets to guarantee training/inference
    parity. If ml_router can't bucket this ctx, shadow scoring is skipped.
    """
    try:
        from scrooge_v3.strategies import ml_router  # type: ignore
        row = ml_router._extract_row_for_buckets(ctx)
        if row is None:
            return None
        return ml_router._compute_buckets(row)
    except Exception as e:
        log.debug("[SHADOW] bucket extract failed: %s", e)
        return None


def observe(symbol: str, ctx, best, all_candidates: list | None = None) -> None:
    """Log one line per scan for the picked candidate.

    Called from scan_pipeline AFTER best-by-score selection. Never raises —
    shadow logging must not affect live trading.
    """
    if _MODEL is None or _META is None or _LOG_PATH is None:
        return
    try:
        buckets = _extract_buckets(ctx)
        if buckets is None:
            return  # ctx can't be bucketed — skip silently

        # Session label
        from scrooge_v3.strategies import ml_router  # type: ignore
        session = ml_router._session(ctx) or "unknown"

        # Build feature row in the exact order the model expects
        row = {
            "pair":            symbol,
            "strategy_id":     best.strategy,
            "direction_exec":  best.direction.value if hasattr(best.direction, "value") else str(best.direction),
            "session_bucket":  session,
            **buckets,
        }

        # Convert to DataFrame with categorical dtypes matching training
        import pandas as pd  # noqa
        feat_order = _META["feature_order"]
        df = pd.DataFrame([[row.get(c, "NA") for c in feat_order]], columns=feat_order)
        cat_levels = _META["categorical_levels"]
        for col in feat_order:
            df[col] = df[col].astype(str).astype("category")
            df[col] = df[col].cat.set_categories(cat_levels.get(col, []))

        p_win = float(_MODEL.predict(df)[0])

        entry = {
            "ts":         time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "symbol":     symbol,
            "strategy":   row["strategy_id"],
            "direction":  row["direction_exec"],
            "session":    session,
            "regime":     str(buckets.get("regime", "")),
            "buckets":    buckets,
            "p_win":      round(p_win, 4),
            "candidate_score": float(getattr(best, "score", 0.0)),
            "was_picked": True,
            "n_candidates_this_scan": (len(all_candidates) if all_candidates else 1),
        }

        with _LOCK:
            with _LOG_PATH.open("a") as f:
                f.write(json.dumps(entry) + "\n")
    except Exception as e:
        log.debug("[SHADOW] observe failed: %s", e)
        # Swallow — must never affect live trading


def is_loaded() -> bool:
    return _MODEL is not None
