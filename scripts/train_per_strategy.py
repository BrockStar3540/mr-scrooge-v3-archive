"""Strategy-conditional + R-weighted XGBoost models.

Two changes vs train_v2.py:
  1. Train one model per strategy family (direct / dbb_trend / reversal / trend)
  2. Add a regression head predicting realized_r (continuous) so threshold
     tuning can target expected R, not just probability.

Reports OOS AUC + sumR per strategy + R-regression performance.
"""
from __future__ import annotations
import json, sys, logging
from pathlib import Path
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import roc_auc_score, mean_absolute_error

REPO = Path.home() / "mr-scrooge-v3"
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))
from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES
from scrooge_v3.advisors.ml_observer.config import (
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING,
)
from train_v2 import backfill_extras, parse, safe, to_vec

REPLAY = Path.home() / "Oanda-Bot-Trainer" / "data" / "replay"
OUT = REPO / "data" / "ml-observer-offline"

log = logging.getLogger("per-strat")


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    sc = pd.read_parquet(REPLAY / "oanda_180d_scans_accepted.parquet")
    tr = pd.read_parquet(REPLAY / "oanda_180d_training_set.parquet")
    sc["ts"] = pd.to_datetime(sc["ts"], utc=True)
    tr["ts"] = pd.to_datetime(tr["ts"], utc=True)
    j = sc.merge(tr[["ts", "symbol", "is_win", "realized_r"]],
                 on=["symbol", "ts"], how="inner")

    # Pull strategy from candidate dict
    j["strategy"] = j["candidate"].apply(
        lambda c: (parse(c) or {}).get("strategy", "unknown") if c else "unknown"
    )
    log.info("trades by strategy: %s", j["strategy"].value_counts().to_dict())

    # Vectorize all rows
    X = []
    for _, r in j.iterrows():
        mf = parse(r["ml_features"])
        mf = backfill_extras(r, mf)
        X.append(to_vec(mf))
    X = np.asarray(X, dtype=np.float32)
    y_win = j["is_win"].astype(np.float32).values
    y_r = j["realized_r"].astype(np.float32).values

    split = pd.Timestamp("2026-03-01T00:00:00Z").to_numpy()
    tr_mask_global = j["ts"].values < split
    te_mask_global = ~tr_mask_global

    # === GLOBAL baseline (all strategies) ===
    log.info("\n=== GLOBAL baseline ===")
    Xtr, Xte = X[tr_mask_global], X[te_mask_global]
    ytr, yte = y_win[tr_mask_global], y_win[te_mask_global]
    rte = y_r[te_mask_global]
    dtr = xgb.DMatrix(Xtr, label=ytr, feature_names=FEATURE_NAMES)
    dte = xgb.DMatrix(Xte, label=yte, feature_names=FEATURE_NAMES)
    booster_global = xgb.train(
        params={**XGB_PARAMS, "eval_metric": ["logloss", "auc"]},
        dtrain=dtr, num_boost_round=XGB_NUM_ROUNDS,
        evals=[(dtr, "train"), (dte, "test")],
        early_stopping_rounds=XGB_EARLY_STOPPING, verbose_eval=False,
    )
    p_global = booster_global.predict(dte)
    log.info("  global AUC=%.4f", roc_auc_score(yte, p_global))

    # === PER-STRATEGY models ===
    log.info("\n=== PER-STRATEGY ===")
    per_strat_results = {}
    for strat in j["strategy"].unique():
        if pd.isna(strat) or strat == "unknown": continue
        sm = (j["strategy"] == strat).values
        n = sm.sum()
        if n < 200: continue
        s_tr = sm & tr_mask_global
        s_te = sm & te_mask_global
        if s_te.sum() < 30: continue
        Xtr_s = X[s_tr]; ytr_s = y_win[s_tr]
        Xte_s = X[s_te]; yte_s = y_win[s_te]; rte_s = y_r[s_te]

        dtr_s = xgb.DMatrix(Xtr_s, label=ytr_s, feature_names=FEATURE_NAMES)
        dte_s = xgb.DMatrix(Xte_s, label=yte_s, feature_names=FEATURE_NAMES)
        m = xgb.train(
            params={**XGB_PARAMS, "eval_metric": ["logloss", "auc"]},
            dtrain=dtr_s, num_boost_round=XGB_NUM_ROUNDS,
            evals=[(dtr_s, "tr"), (dte_s, "te")],
            early_stopping_rounds=XGB_EARLY_STOPPING, verbose_eval=False,
        )
        p_s = m.predict(dte_s)
        auc = roc_auc_score(yte_s, p_s) if pd.Series(yte_s).nunique() > 1 else float("nan")

        # Compare to global model on this slice
        p_g_on_s = p_global[s_te[te_mask_global]]
        auc_g = roc_auc_score(yte_s, p_g_on_s) if pd.Series(yte_s).nunique() > 1 else float("nan")

        log.info("  %-12s n=%d (te=%d) AUC_per=%.4f  AUC_global_on_slice=%.4f  lift=%+.4f",
                 strat, n, s_te.sum(), auc, auc_g, auc - auc_g)

        # Filter sims with R
        log.info("    base: sumR=%+.2f over %d trades, WR=%.3f",
                 rte_s.sum(), len(rte_s), yte_s.mean())
        for thr in [0.3, 0.4, 0.5, 0.6]:
            sel = p_s >= thr
            if sel.sum() == 0: continue
            log.info("    p>=%.1f n=%d (%.1f%%)  sumR=%+.2f  WR=%.3f",
                     thr, sel.sum(), 100 * sel.sum() / len(yte_s),
                     rte_s[sel].sum(), yte_s[sel].mean())

        m.save_model(str(OUT / f"model_strategy_{strat}.xgb"))
        per_strat_results[strat] = {"auc": auc, "n": n, "model": m}

    # === R-WEIGHTED regression head ===
    log.info("\n=== R-REGRESSION head (predict realized_r) ===")
    rtr = y_r[tr_mask_global]
    dtr_r = xgb.DMatrix(Xtr, label=rtr, feature_names=FEATURE_NAMES)
    dte_r = xgb.DMatrix(Xte, label=rte, feature_names=FEATURE_NAMES)
    booster_r = xgb.train(
        params={**XGB_PARAMS, "objective": "reg:squarederror", "eval_metric": "mae"},
        dtrain=dtr_r, num_boost_round=XGB_NUM_ROUNDS,
        evals=[(dtr_r, "tr"), (dte_r, "te")],
        early_stopping_rounds=XGB_EARLY_STOPPING, verbose_eval=False,
    )
    pred_r = booster_r.predict(dte_r)
    log.info("  R-MAE=%.3f  R-corr=%.3f",
             mean_absolute_error(rte, pred_r),
             float(np.corrcoef(rte, pred_r)[0, 1]))

    # Filter by predicted R
    log.info("\n=== Filter by predicted_R (out-of-sample) ===")
    log.info("  baseline take all: sumR=%+.2f", rte.sum())
    for thr_r in [0.0, 0.1, 0.2, 0.3, 0.5]:
        sel = pred_r >= thr_r
        if sel.sum() == 0: continue
        log.info("  pred_r>=%.1f  n=%d (%.1f%%)  sumR=%+.2f  WR=%.3f  avg_actual_R=%+.3f",
                 thr_r, sel.sum(), 100 * sel.sum() / len(rte),
                 rte[sel].sum(), yte[sel].mean(), rte[sel].mean())

    booster_r.save_model(str(OUT / "model_r_regression.xgb"))


if __name__ == "__main__":
    main()
