# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — XGBoost Trainer.

Joins scans.jsonl + outcomes.jsonl by (symbol + nearest-in-time linkage)
to build a supervised (X, y) training set, runs CV, saves model, reports
feature importance.

Two data sources supported for backwards compat during backfill:
  1. NEW: scans.jsonl + outcomes.jsonl (five-file schema)
  2. LEGACY: observations.jsonl with inline `outcome` key (archive)
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
import xgboost as xgb

from features import FEATURE_NAMES
from config import (
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING, XGB_CV_FOLDS,
    MODEL_FILE, SCANS_FILE, OUTCOMES_FILE, OBSERVATIONS_FILE,
    PHASE2_MIN_TRADES, PHASE3_MIN_CV_ACCURACY,
    TRADE_ASSOCIATION_WINDOW_SEC,
)

log = logging.getLogger("ml-observer.trainer")


def _load_legacy(min_rows: int) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], int]:
    """Load from legacy observations.jsonl (inline outcome)."""
    if not OBSERVATIONS_FILE.exists():
        return None, None, 0
    rows_X, rows_y = [], []
    with open(OBSERVATIONS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obs = json.loads(line)
            except json.JSONDecodeError:
                continue
            outcome = obs.get("outcome")
            if outcome is None:
                continue
            feats = obs.get("features", {})
            rows_X.append([feats.get(n, 0.0) for n in FEATURE_NAMES])
            rows_y.append(float(outcome))
    if len(rows_X) < min_rows:
        return None, None, len(rows_X)
    return np.array(rows_X), np.array(rows_y), len(rows_X)


def _load_scans_outcomes(min_rows: int) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], int]:
    """Join scans.jsonl + outcomes.jsonl.

    For each closed outcome, walk scans.jsonl back from the close ts
    within TRADE_ASSOCIATION_WINDOW_SEC to find the matching TAKE_*
    scan of that symbol.
    """
    if not (SCANS_FILE.exists() and OUTCOMES_FILE.exists()):
        return None, None, 0

    from datetime import datetime

    closes = []
    opens_by_trade: dict[str, dict] = {}
    with open(OUTCOMES_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("kind") == "trade_close":
                closes.append(row)
            elif row.get("kind") == "trade_open":
                opens_by_trade[row.get("trade_id", "")] = row

    if not closes:
        return None, None, 0

    # Build an index of scans keyed by symbol -> list of (ts_epoch, row)
    by_symbol: dict[str, list] = {}
    with open(SCANS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            sym = row.get("symbol")
            ts_s = row.get("ts")
            if not sym or not ts_s:
                continue
            try:
                ts_e = datetime.fromisoformat(ts_s.replace("Z", "+00:00")).timestamp()
            except ValueError:
                continue
            by_symbol.setdefault(sym, []).append((ts_e, row))
    for lst in by_symbol.values():
        lst.sort()

    def _pick_scan(symbol: str, close_ts: float) -> Optional[dict]:
        # Prefer the matched-on-open scan if we saved it.
        lst = by_symbol.get(symbol) or []
        # Scan rows with TAKE_* verdict, most recent before close_ts, within window.
        cutoff = close_ts - TRADE_ASSOCIATION_WINDOW_SEC * 48  # permissive: trade can live hours
        best = None
        for ts_e, row in lst:
            if ts_e > close_ts:
                break
            if not str(row.get("verdict", "")).startswith("TAKE_"):
                continue
            if ts_e < cutoff:
                continue
            best = row
        return best

    rows_X, rows_y = [], []
    for close in closes:
        sym = close.get("symbol")
        try:
            close_ts_e = datetime.fromisoformat(close["ts"].replace("Z", "+00:00")).timestamp()
        except (KeyError, ValueError, AttributeError):
            continue
        trade_id = close.get("trade_id", "")
        # Prefer the matched-scan cycle recorded on the open row.
        open_row = opens_by_trade.get(trade_id, {})
        matched_scan = None
        if open_row.get("matched_scan_ts"):
            # Look up exact scan
            target_ts = open_row["matched_scan_ts"]
            for ts_e, row in by_symbol.get(sym, []):
                if row.get("ts") == target_ts and str(row.get("verdict", "")).startswith("TAKE_"):
                    matched_scan = row
                    break
        if matched_scan is None:
            matched_scan = _pick_scan(sym, close_ts_e)
        if matched_scan is None:
            continue
        feats = matched_scan.get("ml_features") or matched_scan.get("features") or {}
        rows_X.append([float(feats.get(n, 0.0)) for n in FEATURE_NAMES])
        rows_y.append(float(close.get("outcome", 0)))
    if len(rows_X) < min_rows:
        return None, None, len(rows_X)
    return np.array(rows_X), np.array(rows_y), len(rows_X)


def load_training_data() -> Tuple[Optional[np.ndarray], Optional[np.ndarray], int]:
    """Load labeled training set from either source."""
    X, y, n = _load_scans_outcomes(PHASE2_MIN_TRADES)
    if X is not None:
        return X, y, n
    # Fallback to legacy
    X2, y2, n2 = _load_legacy(PHASE2_MIN_TRADES)
    if X2 is not None:
        return X2, y2, n2
    return None, None, max(n, n2)


def train_model() -> dict:
    X, y, n = load_training_data()
    if X is None:
        return {"status": "insufficient_data", "n_samples": n,
                "required": PHASE2_MIN_TRADES}

    wins = int(y.sum())
    losses = n - wins
    log.info("Training on %d trades (%d wins, %d losses)", n, wins, losses)

    dtrain = xgb.DMatrix(X, label=y, feature_names=FEATURE_NAMES)
    cv_results = xgb.cv(
        XGB_PARAMS, dtrain,
        num_boost_round=XGB_NUM_ROUNDS,
        nfold=XGB_CV_FOLDS,
        early_stopping_rounds=XGB_EARLY_STOPPING,
        seed=42,
        verbose_eval=False,
    )
    best_round = len(cv_results)
    best_logloss = cv_results["test-logloss-mean"].iloc[-1]
    best_logloss_std = cv_results["test-logloss-std"].iloc[-1]
    model = xgb.train(XGB_PARAMS, dtrain, num_boost_round=best_round)
    preds = model.predict(dtrain)
    pred_labels = (preds > 0.5).astype(int)
    accuracy = (pred_labels == y).mean()
    importance = model.get_score(importance_type="gain")
    sorted_imp = sorted(importance.items(), key=lambda x: x[1], reverse=True)
    model.save_model(str(MODEL_FILE))
    log.info("Model saved to %s", MODEL_FILE)
    report = {
        "status": "trained",
        "n_samples": n, "wins": wins, "losses": losses,
        "cv_best_round": best_round,
        "cv_logloss": round(best_logloss, 4),
        "cv_logloss_std": round(best_logloss_std, 4),
        "insample_accuracy": round(accuracy, 4),
        "feature_importance_top10": [
            {"feature": name, "gain": round(gain, 2)}
            for name, gain in sorted_imp[:10]
        ],
        "phase3_ready": accuracy >= PHASE3_MIN_CV_ACCURACY,
    }
    log.info("Training: logloss=%s acc=%s phase3=%s",
             report["cv_logloss"], report["insample_accuracy"],
             report["phase3_ready"])
    for i, item in enumerate(report["feature_importance_top10"]):
        log.info("  Feature #%d: %s (gain=%s)", i+1, item["feature"], item["gain"])
    return report


def predict(features_dict: dict) -> Tuple[float, int]:
    if not MODEL_FILE.exists():
        return 0.5, -1
    model = xgb.Booster()
    model.load_model(str(MODEL_FILE))
    row = [features_dict.get(n, 0.0) for n in FEATURE_NAMES]
    dmat = xgb.DMatrix(np.array([row]), feature_names=FEATURE_NAMES)
    prob = float(model.predict(dmat)[0])
    label = 1 if prob > 0.5 else 0
    return prob, label
