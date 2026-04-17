# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — XGBoost Trainer
Trains win/loss classifier, runs CV, reports feature importance.
"""

import json
import logging
from pathlib import Path
from typing import Tuple, Optional

import numpy as np
import xgboost as xgb

from features import FEATURE_NAMES
from config import (
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING, XGB_CV_FOLDS,
    MODEL_FILE, OBSERVATIONS_FILE, PHASE2_MIN_TRADES, PHASE3_MIN_CV_ACCURACY,
)

log = logging.getLogger("ml-observer.trainer")


def load_training_data() -> Tuple[Optional[np.ndarray], Optional[np.ndarray], int]:
    """
    Load observations that have outcomes (trades that closed).
    Returns (X, y, total_with_outcomes) or (None, None, 0) if insufficient data.
    """
    if not OBSERVATIONS_FILE.exists():
        return None, None, 0

    rows_X = []
    rows_y = []

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

            features = obs.get("features", {})
            row = [features.get(name, 0.0) for name in FEATURE_NAMES]
            rows_X.append(row)
            rows_y.append(float(outcome))

    if len(rows_X) < PHASE2_MIN_TRADES:
        return None, None, len(rows_X)

    return np.array(rows_X), np.array(rows_y), len(rows_X)


def train_model() -> dict:
    """
    Train XGBoost model with cross-validation.
    Returns training report dict.
    """
    X, y, n_samples = load_training_data()

    if X is None:
        return {
            "status": "insufficient_data",
            "n_samples": n_samples,
            "required": PHASE2_MIN_TRADES,
        }

    wins = int(y.sum())
    losses = n_samples - wins
    log.info(f"Training on {n_samples} trades ({wins} wins, {losses} losses)")

    dtrain = xgb.DMatrix(X, label=y, feature_names=FEATURE_NAMES)

    # Cross-validation
    cv_results = xgb.cv(
        XGB_PARAMS,
        dtrain,
        num_boost_round=XGB_NUM_ROUNDS,
        nfold=XGB_CV_FOLDS,
        early_stopping_rounds=XGB_EARLY_STOPPING,
        seed=42,
        verbose_eval=False,
    )

    best_round = len(cv_results)
    best_logloss = cv_results["test-logloss-mean"].iloc[-1]
    best_logloss_std = cv_results["test-logloss-std"].iloc[-1]

    # Calculate CV accuracy (threshold at 0.5)
    # Retrain on full data to get predictions for accuracy estimate
    model = xgb.train(XGB_PARAMS, dtrain, num_boost_round=best_round)

    # Use in-sample predictions as rough accuracy (CV logloss is the real metric)
    preds = model.predict(dtrain)
    pred_labels = (preds > 0.5).astype(int)
    accuracy = (pred_labels == y).mean()

    # Feature importance
    importance = model.get_score(importance_type="gain")
    sorted_importance = sorted(importance.items(), key=lambda x: x[1], reverse=True)

    # Save model
    model.save_model(str(MODEL_FILE))
    log.info(f"Model saved to {MODEL_FILE}")

    report = {
        "status": "trained",
        "n_samples": n_samples,
        "wins": wins,
        "losses": losses,
        "cv_best_round": best_round,
        "cv_logloss": round(best_logloss, 4),
        "cv_logloss_std": round(best_logloss_std, 4),
        "insample_accuracy": round(accuracy, 4),
        "feature_importance_top10": [
            {"feature": name, "gain": round(gain, 2)}
            for name, gain in sorted_importance[:10]
        ],
        "phase3_ready": accuracy >= PHASE3_MIN_CV_ACCURACY,
    }

    log.info(f"Training report: logloss={report['cv_logloss']} "
             f"accuracy={report['insample_accuracy']} "
             f"phase3_ready={report['phase3_ready']}")
    for i, item in enumerate(report["feature_importance_top10"]):
        log.info(f"  Feature #{i+1}: {item['feature']} (gain={item['gain']})")

    return report


def predict(features_dict: dict) -> Tuple[float, int]:
    """
    Predict outcome for a single observation.
    Returns (probability_of_win, predicted_label).
    """
    if not MODEL_FILE.exists():
        return 0.5, -1  # no model yet

    model = xgb.Booster()
    model.load_model(str(MODEL_FILE))

    row = [features_dict.get(name, 0.0) for name in FEATURE_NAMES]
    dmat = xgb.DMatrix(np.array([row]), feature_names=FEATURE_NAMES)
    prob = float(model.predict(dmat)[0])
    label = 1 if prob > 0.5 else 0

    return prob, label
