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
    BUCKET_META_FILE, SCAN_OPEN_WINDOW_SEC,
)

log = logging.getLogger("ml-observer.trainer")

# Sidecar describing the feature space the saved model.xgb was trained on, so
# predict() rebuilds an identical (categorical) input frame.
MODEL_FEATURES_FILE = MODEL_FILE.parent / "model-features.json"

# Hardcoded fallback if feature_meta.json is unreadable: 14 pip_eater buckets
# plus the 4 identity columns, in the live LightGBM shadow order.
_FALLBACK_BUCKET_ORDER = [
    "BB", "BBP", "A5", "A1", "RSI", "E20", "E50", "ZS", "SPR", "ADR",
    "H20", "H60", "T1", "T4", "pair", "strategy_id", "direction_exec",
    "session_bucket",
]


def _bucket_schema() -> Tuple[list, dict]:
    """(feature_order, categorical_levels) for the pip_eater bucket feature
    space — sourced from the live LightGBM shadow meta for train/inference
    parity with the bot."""
    try:
        meta = json.loads(BUCKET_META_FILE.read_text())
        order = list(meta.get("feature_order") or [])
        levels = dict(meta.get("categorical_levels") or {})
        if order:
            return order, levels
    except Exception as e:  # noqa: BLE001
        log.warning("bucket schema load failed (%s) — using fallback order", e)
    return list(_FALLBACK_BUCKET_ORDER), {}


def _scan_to_feature_row(scan: dict) -> Optional[dict]:
    """Flatten a bucketed scan row into the {col: categorical_value} feature
    row the model consumes. Returns None if the row carries no buckets."""
    buckets = scan.get("buckets")
    if not isinstance(buckets, dict) or not buckets:
        return None
    ident = scan.get("identity") or {}
    cand = scan.get("candidate") or {}
    row = dict(buckets)
    row["pair"] = scan.get("symbol", "")
    row["strategy_id"] = ident.get("strategy") or cand.get("strategy") or ""
    row["direction_exec"] = ident.get("direction") or cand.get("direction") or ""
    row["session_bucket"] = ident.get("session_bucket") or ""
    return row


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


def _build_categorical_frame(feat_rows: list):
    """Build a category-dtyped DataFrame from feature rows using the canonical
    bucket schema. Returns (df, feature_order, categorical_levels)."""
    import pandas as pd
    order, levels = _bucket_schema()
    df = pd.DataFrame(
        [[str(fr.get(c, "NA")) for c in order] for fr in feat_rows],
        columns=order,
    )
    used_levels: dict = {}
    for c in order:
        base = list(levels.get(c) or [])
        # Extend with any observed value not in the meta (e.g. a new strategy)
        # so set_categories never drops a row to NaN.
        observed = sorted(df[c].astype(str).unique().tolist())
        cats = list(dict.fromkeys(base + observed))
        df[c] = df[c].astype(str).astype("category").cat.set_categories(cats)
        used_levels[c] = cats
    return df, order, used_levels


def _load_shadow_outcomes(min_rows: int):
    """Join pip_eater bucketed scans (scans.jsonl) + outcomes.jsonl into a
    categorical (X, y) training set.

    For each closed trade: trade_close -> trade_open (by trade_id) gives the
    fill ts + symbol; we take the most recent bucketed scan for that symbol
    within SCAN_OPEN_WINDOW_SEC before the fill. X = the 18-column categorical
    bucket frame; y = win(1)/loss(0).
    """
    if not (SCANS_FILE.exists() and OUTCOMES_FILE.exists()):
        return None, None, 0

    from datetime import datetime

    def _ep(s):
        try:
            return datetime.fromisoformat(str(s).replace("Z", "+00:00")).timestamp()
        except Exception:  # noqa: BLE001
            return None

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
            if not isinstance(row.get("buckets"), dict) or not row["buckets"]:
                continue  # only PIP-EATER bucketed rows are trainable
            sym = row.get("symbol")
            te = _ep(row.get("ts"))
            if not sym or te is None:
                continue
            by_symbol.setdefault(sym, []).append((te, row))
    for lst in by_symbol.values():
        lst.sort(key=lambda x: x[0])
    if not by_symbol:
        return None, None, 0

    opens_by_trade: dict[str, dict] = {}
    closes: list[dict] = []
    with open(OUTCOMES_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            k = r.get("kind")
            if k == "trade_open":
                opens_by_trade[r.get("trade_id", "")] = r
            elif k == "trade_close":
                closes.append(r)
    if not closes:
        return None, None, 0

    def _nearest(symbol: str, t: float) -> Optional[dict]:
        best = None
        for te, row in by_symbol.get(symbol, []):
            if te > t:
                break
            if t - te <= SCAN_OPEN_WINDOW_SEC:
                best = row
        return best

    feat_rows: list[dict] = []
    ys: list[float] = []
    for close in closes:
        trade_id = close.get("trade_id", "")
        open_row = opens_by_trade.get(trade_id)
        if not open_row:
            continue
        t = _ep(open_row.get("ts"))
        sym = open_row.get("symbol")
        if t is None or not sym:
            continue
        scan = _nearest(sym, t)
        if scan is None:
            continue
        fr = _scan_to_feature_row(scan)
        if fr is None:
            continue
        feat_rows.append(fr)
        ys.append(float(close.get("outcome", 0)))

    if len(feat_rows) < min_rows:
        return None, None, len(feat_rows)

    df, _order, _levels = _build_categorical_frame(feat_rows)
    return df, np.array(ys), len(feat_rows)


def load_training_data() -> Tuple[Optional[object], Optional[np.ndarray], int]:
    """Load the labeled training set.

    PIP-EATER era: the live feature source is the categorical bucket frame
    joined from scans.jsonl (mirrored from lightgbm_shadow.jsonl) + outcomes.
    The legacy numeric V3-scorer paths (_load_scans_outcomes via ml_features,
    _load_legacy) are retired — those features are no longer emitted — and are
    kept only for archival reference. We therefore do NOT fall back to them, to
    avoid training on all-zero vectors.
    """
    X, y, n = _load_shadow_outcomes(PHASE2_MIN_TRADES)
    if X is not None:
        return X, y, n
    return None, None, n


def train_model() -> dict:
    X, y, n = load_training_data()
    if X is None:
        return {"status": "insufficient_data", "n_samples": n,
                "required": PHASE2_MIN_TRADES}

    wins = int(y.sum())
    losses = n - wins
    log.info("Training on %d trades (%d wins, %d losses)", n, wins, losses)

    import pandas as pd
    is_categorical = isinstance(X, pd.DataFrame)
    params = dict(XGB_PARAMS)
    if is_categorical:
        # XGBoost categorical splits require the hist tree method.
        params["tree_method"] = "hist"
        dtrain = xgb.DMatrix(X, label=y, enable_categorical=True)
        feat_names = list(X.columns)
    else:
        dtrain = xgb.DMatrix(X, label=y, feature_names=FEATURE_NAMES)
        feat_names = FEATURE_NAMES

    # Guard CV folds against tiny / imbalanced sets.
    nfold = max(2, min(XGB_CV_FOLDS, wins, losses)) if min(wins, losses) else 2
    cv_results = xgb.cv(
        params, dtrain,
        num_boost_round=XGB_NUM_ROUNDS,
        nfold=nfold,
        early_stopping_rounds=XGB_EARLY_STOPPING,
        seed=42,
        verbose_eval=False,
    )
    best_round = len(cv_results)
    best_logloss = cv_results["test-logloss-mean"].iloc[-1]
    best_logloss_std = cv_results["test-logloss-std"].iloc[-1]
    model = xgb.train(params, dtrain, num_boost_round=best_round)
    preds = model.predict(dtrain)
    pred_labels = (preds > 0.5).astype(int)
    accuracy = (pred_labels == y).mean()
    importance = model.get_score(importance_type="gain")
    sorted_imp = sorted(importance.items(), key=lambda x: x[1], reverse=True)
    model.save_model(str(MODEL_FILE))
    # Persist the feature schema so predict() rebuilds an identical input frame.
    if is_categorical:
        schema = {
            "mode": "categorical",
            "feature_order": feat_names,
            "categorical_levels": {
                c: list(map(str, X[c].cat.categories)) for c in feat_names
            },
        }
    else:
        schema = {"mode": "numeric", "feature_order": list(feat_names)}
    try:
        MODEL_FEATURES_FILE.write_text(json.dumps(schema))
    except OSError as e:  # noqa: BLE001
        log.warning("could not write model feature schema: %s", e)
    log.info("Model saved to %s (mode=%s)", MODEL_FILE,
             "categorical" if is_categorical else "numeric")
    report = {
        "status": "trained",
        "n_samples": n, "wins": wins, "losses": losses,
        "cv_best_round": best_round,
        "cv_logloss": round(best_logloss, 4),
        "cv_logloss_std": round(best_logloss_std, 4),
        "insample_accuracy": round(float(accuracy), 4),
        "feature_importance_top10": [
            {"feature": name, "gain": round(float(gain), 2)}
            for name, gain in sorted_imp[:10]
        ],
        "phase3_ready": bool(accuracy >= PHASE3_MIN_CV_ACCURACY),
    }
    log.info("Training: logloss=%s acc=%s phase3=%s",
             report["cv_logloss"], report["insample_accuracy"],
             report["phase3_ready"])
    for i, item in enumerate(report["feature_importance_top10"]):
        log.info("  Feature #%d: %s (gain=%s)", i+1, item["feature"], item["gain"])
    return report


def predict(features_dict: dict) -> Tuple[float, int]:
    """Score one feature row. Returns (p_win, label).

    (0.5, -1) is the neutral/abstain sentinel: returned when no model exists or
    the caller could not supply the bucket features this model needs (e.g. the
    V3 API signal path, which no longer carries them).
    """
    if not MODEL_FILE.exists():
        return 0.5, -1
    import json as _json
    import pandas as _pd

    schema = {}
    if MODEL_FEATURES_FILE.exists():
        try:
            schema = _json.loads(MODEL_FEATURES_FILE.read_text())
        except Exception:  # noqa: BLE001
            schema = {}

    model = xgb.Booster()
    model.load_model(str(MODEL_FILE))

    if schema.get("mode") == "categorical":
        order = schema.get("feature_order") or []
        levels = schema.get("categorical_levels") or {}
        # Abstain if the caller gave us none of the bucket features.
        if not any(k in features_dict for k in order):
            return 0.5, -1
        df = _pd.DataFrame(
            [[str(features_dict.get(c, "NA")) for c in order]], columns=order
        )
        for c in order:
            cats = levels.get(c) or sorted(df[c].astype(str).unique().tolist())
            df[c] = df[c].astype(str).astype("category").cat.set_categories(cats)
        dmat = xgb.DMatrix(df, enable_categorical=True)
        prob = float(model.predict(dmat)[0])
        return prob, (1 if prob > 0.5 else 0)

    # Legacy numeric path (retired V3-scorer feature vector).
    _row = {n: features_dict.get(n, 0.0) for n in FEATURE_NAMES}
    _df = _pd.DataFrame([_row], columns=FEATURE_NAMES)
    dmat = xgb.DMatrix(_df)
    prob = float(model.predict(dmat)[0])
    return prob, (1 if prob > 0.5 else 0)
