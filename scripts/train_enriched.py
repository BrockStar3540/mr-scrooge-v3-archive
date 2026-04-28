"""Train ML observer with ENRICHED features from raw scan dicts.

Adds factors recoverable from existing scan parquets (no re-sweep needed):
  - SMA20 distance (signed bps) -- from bollinger.sma_a + current_close
  - BB band geometry -- band width, percent_b, position in band
  - BB state categorical -- REJECTION/STRETCH/NORMAL encoded
  - Regime categorical -- NORMAL/CAUTION/RESTRICTED encoded
  - Strategy categorical -- reversal/direct/dbb_trend/trend
  - Direction (long/short)
  - Score-tier flags
  - Pip-scale natural stop and overhead (from candidate)

Compares AUC vs the baseline 61-feature model.
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import xgboost as xgb

REPO = Path.home() / "mr-scrooge-v3"
sys.path.insert(0, str(REPO / "src"))
from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES as BASE_FEATURES
from scrooge_v3.advisors.ml_observer.config import (
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING,
)

REPLAY = Path.home() / "Oanda-Bot-Trainer" / "data" / "replay"
OUT_DIR = REPO / "data" / "ml-observer-offline"

BB_STATE_MAP = {
    "NORMAL": 0, "REJECTION_LONG": 1, "REJECTION_SHORT": 2,
    "STRETCH_UP": 3, "STRETCH_DOWN": 4, "TREND_UP": 5, "TREND_DOWN": 6,
}
REGIME_MAP = {"NORMAL": 0, "CAUTION": 1, "RESTRICTED": 2}
STRATEGY_MAP = {"reversal": 0, "direct": 1, "dbb_trend": 2, "trend": 3}

EXTRA_FEATURES = [
    "sma20_dist_signed_bps", "bb_band_width_a_bps", "bb_band_width_b_bps",
    "bb_percent_b_a", "bb_percent_b_b",
    "bb_state_id", "regime_id",
    "strategy_id", "direction_long",
    "tier_b_flag", "tier_a_flag", "score_minus_floor", "score_above_b",
    "natural_stop_pips", "tp_distance_pips", "rr_ratio",
    "spread_pips", "spread_to_stop_ratio",
]
ENRICHED_FEATURES = list(BASE_FEATURES) + EXTRA_FEATURES

log = logging.getLogger("train-enriched")


def safe_float(v, default=0.0):
    try:
        f = float(v)
        return f if np.isfinite(f) else default
    except (TypeError, ValueError):
        return default


def parse_dict(raw):
    if isinstance(raw, dict): return raw
    if isinstance(raw, str):
        try: return json.loads(raw.replace("Infinity", "1e9").replace("NaN", "0"))
        except: return {}
    return {}


def base_vec(mf):
    out = []
    for n in BASE_FEATURES:
        out.append(safe_float(mf.get(n, 0.0)))
    return out


def extra_vec(row):
    """Extract EXTRA_FEATURES from one scan_accepted row."""
    feats = parse_dict(row.get("features", {}))
    cls = parse_dict(row.get("classifications", {}))
    scorer = parse_dict(row.get("scorer", {}))
    cand = parse_dict(row.get("candidate", {}))

    boll = parse_dict(feats.get("bollinger", {}))
    sma_a = safe_float(boll.get("sma_a"))
    upper_a = safe_float(boll.get("upper_a"))
    lower_a = safe_float(boll.get("lower_a"))
    upper_b = safe_float(boll.get("upper_b"))
    lower_b = safe_float(boll.get("lower_b"))
    close = safe_float(boll.get("current_close"))
    pct_b_a = safe_float(boll.get("percent_b_a", boll.get("percent_b")))
    pct_b_b = safe_float(boll.get("percent_b_b"))

    sma_dist_bps = ((close - sma_a) / sma_a * 10000) if sma_a > 0 else 0.0
    bw_a_bps = ((upper_a - lower_a) / sma_a * 10000) if sma_a > 0 else 0.0
    bw_b_bps = ((upper_b - lower_b) / sma_a * 10000) if sma_a > 0 else 0.0

    bb_state = (cls.get("bb_state") or {}).get("label", "NORMAL") if isinstance(cls.get("bb_state"), dict) else "NORMAL"
    regime = (cls.get("regime") or {}).get("label", "NORMAL") if isinstance(cls.get("regime"), dict) else "NORMAL"

    strat = cand.get("strategy", "")
    direction = cand.get("direction", "")
    entry = safe_float(cand.get("entry_price"))
    stop = safe_float(cand.get("stop_price"))
    tp = safe_float(cand.get("take_profit"))

    pip_size = 0.01 if any(j in str(row.get("symbol", "")) for j in ("JPY", "MXN")) else 0.0001
    nat_stop_pips = abs(entry - stop) / pip_size if (entry and stop and pip_size) else 0.0
    tp_dist_pips = abs(entry - tp) / pip_size if (entry and tp and pip_size) else 0.0
    rr = (tp_dist_pips / nat_stop_pips) if nat_stop_pips > 0 else 0.0

    spread = safe_float(row.get("spread"))
    spread_pips = spread * 10 if pip_size == 0.0001 else spread  # rough
    sp_to_stop = (spread_pips / nat_stop_pips) if nat_stop_pips > 0 else 0.0

    score = safe_float(scorer.get("score"))
    floor = safe_float(scorer.get("floor"))
    b_thr = safe_float(scorer.get("b"))
    a_thr = safe_float(scorer.get("a"))

    return [
        sma_dist_bps, bw_a_bps, bw_b_bps,
        pct_b_a, pct_b_b,
        float(BB_STATE_MAP.get(bb_state, 0)),
        float(REGIME_MAP.get(regime, 0)),
        float(STRATEGY_MAP.get(strat, 0)),
        1.0 if direction == "long" else 0.0,
        1.0 if score >= b_thr else 0.0,
        1.0 if score >= a_thr else 0.0,
        score - floor,
        score - b_thr,
        nat_stop_pips, tp_dist_pips, rr,
        spread_pips, sp_to_stop,
    ]


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    log.info("loading corpus...")
    sc = pd.read_parquet(REPLAY / "oanda_180d_scans_accepted.parquet")
    tr = pd.read_parquet(REPLAY / "oanda_180d_training_set.parquet")
    sc["ts"] = pd.to_datetime(sc["ts"], utc=True)
    tr["ts"] = pd.to_datetime(tr["ts"], utc=True)

    j = sc.merge(
        tr[["ts", "symbol", "is_win", "realized_r"]],
        on=["symbol", "ts"], how="inner",
    )
    log.info("joined=%d", len(j))

    log.info("vectorizing base + extra features...")
    base_X = []
    extra_X = []
    for _, r in j.iterrows():
        mf = parse_dict(r["ml_features"])
        base_X.append(base_vec(mf))
        extra_X.append(extra_vec(r))
    base_X = np.asarray(base_X, dtype=np.float32)
    extra_X = np.asarray(extra_X, dtype=np.float32)
    full_X = np.concatenate([base_X, extra_X], axis=1)
    y = j["is_win"].astype(np.float32).values
    log.info("base=%s extra=%s full=%s y=%s", base_X.shape, extra_X.shape, full_X.shape, y.shape)

    # Time-series split (same as holdout_eval)
    split_ts = pd.Timestamp("2026-03-01T00:00:00Z")
    train_mask = j["ts"].values < split_ts.to_numpy()
    test_mask = ~train_mask

    def fit_eval(X, names, label):
        Xtr, Xte = X[train_mask], X[test_mask]
        ytr, yte = y[train_mask], y[test_mask]
        dtr = xgb.DMatrix(Xtr, label=ytr, feature_names=names)
        dte = xgb.DMatrix(Xte, label=yte, feature_names=names)
        booster = xgb.train(
            params={**XGB_PARAMS, "eval_metric": ["logloss", "auc", "error"]},
            dtrain=dtr, num_boost_round=XGB_NUM_ROUNDS,
            evals=[(dtr, "train"), (dte, "test")],
            early_stopping_rounds=XGB_EARLY_STOPPING,
            verbose_eval=False,
        )
        ptr = booster.predict(dtr); pte = booster.predict(dte)
        from sklearn.metrics import roc_auc_score
        log.info("%-10s base_round=%d  train_AUC=%.4f  TEST_AUC=%.4f  test_err=%.4f",
                 label, booster.best_iteration + 1,
                 roc_auc_score(ytr, ptr), roc_auc_score(yte, pte),
                 float(((pte > 0.5) != yte.astype(bool)).mean()))
        return booster, pte

    log.info("\n=== BASELINE: 61-feature model ===")
    b1, p1 = fit_eval(base_X, BASE_FEATURES, "baseline")

    log.info("\n=== ENRICHED: 79-feature model ===")
    b2, p2 = fit_eval(full_X, ENRICHED_FEATURES, "enriched")

    # Feature importance for the new features
    fi = b2.get_score(importance_type="gain")
    log.info("\n=== Feature importance — extras only ===")
    for f in EXTRA_FEATURES:
        if f in fi:
            log.info("  %-30s gain=%.2f", f, fi[f])

    # Save enriched model
    b2.save_model(str(OUT_DIR / "model_enriched.xgb"))
    log.info("model -> %s", OUT_DIR / "model_enriched.xgb")

    # Filter scenarios on test set
    yte = y[test_mask]
    rte = j.loc[test_mask, "realized_r"].values
    log.info("\n=== OOS filter scenarios — enriched ===")
    log.info("  baseline-take-all WR=%.3f sumR=%+.2f", yte.mean(), rte.sum())
    for thr in [0.3, 0.4, 0.5, 0.6, 0.7]:
        sel = p2 >= thr
        n = int(sel.sum())
        if n == 0: continue
        wr = yte[sel].mean(); sr = rte[sel].sum()
        log.info("  p>=%.1f  n=%d (%.1f%%)  WR=%.3f  sumR=%+.2f  avgR=%+.3f",
                 thr, n, 100*n/len(yte), wr, sr, sr/n)


if __name__ == "__main__":
    main()
