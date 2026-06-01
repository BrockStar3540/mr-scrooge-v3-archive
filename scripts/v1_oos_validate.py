#!/usr/bin/env python3
"""v1 LightGBM out-of-sample validation.

The v1 pip-regressor reported holdout MAE 8.01p from a RANDOM 80/20 split.
Lab trades are autocorrelated (same setup repeated across nearby bars), so a
random split leaks structure between train/test and flatters MAE. The corpus
has NO time column, so a true chronological walk-forward is impossible here.

This runs the honest checks that ARE possible:
  1. random_5fold      — control; should reproduce ~8.01p (optimistic bound)
  2. cohort_holdout    — train legacy -> test phase3, and vice versa
                         (distribution-shift robustness)
  3. group_by_pair     — GroupKFold over pairs; generalize to UNSEEN pairs
                         (pessimistic bound; note: also strips 'pair', the #1
                          feature, so expect a legitimate penalty too)

Aggregate MAE is compared to the naive baseline (predict y_train_mean).
"""
import json, time, sys
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import KFold, GroupKFold

CORPUS = "data/lab_training/training_corpus_v1.csv.gz"
META = "data/lab_training/v1/feature_meta.json"
OUT = "data/lab_training/v1/oos_validation.json"

meta = json.load(open(META))
FEATS = meta["feature_order"]
PARAMS = dict(meta["params"])
N_ROUNDS = meta.get("best_iteration", 500)

def log(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)

log(f"loading {CORPUS} ...")
df = pd.read_csv(CORPUS)
log(f"loaded {len(df):,} rows, cols={list(df.columns)}")
for c in FEATS:
    df[c] = df[c].astype("category")
y = df["pnl_pips"].astype(float).values

def fit_eval(tr_idx, te_idx, tag):
    Xtr, ytr = df.iloc[tr_idx][FEATS], y[tr_idx]
    Xte, yte = df.iloc[te_idx][FEATS], y[te_idx]
    dtr = lgb.Dataset(Xtr, label=ytr, categorical_feature=FEATS, free_raw_data=False)
    booster = lgb.train(PARAMS, dtr, num_boost_round=N_ROUNDS)
    pred = booster.predict(Xte)
    mae = float(np.mean(np.abs(pred - yte)))
    rmse = float(np.sqrt(np.mean((pred - yte) ** 2)))
    naive = float(np.mean(np.abs(yte - ytr.mean())))
    res = {"tag": tag, "n_train": int(len(tr_idx)), "n_test": int(len(te_idx)),
           "mae": round(mae, 4), "rmse": round(rmse, 4),
           "naive_mae": round(naive, 4),
           "improvement_pct": round(100 * (naive - mae) / naive, 2)}
    log(f"  {tag}: MAE={mae:.3f} naive={naive:.3f} impr={res['improvement_pct']}% "
        f"(train={len(tr_idx):,} test={len(te_idx):,})")
    return res

results = {"corpus_rows": int(len(df)), "n_rounds": N_ROUNDS,
           "random_split_reported_mae": meta.get("holdout_mae", 8.01),
           "checks": {}}

# 1. random 5-fold control
log("=== random_5fold ===")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
folds = []
for i, (tr, te) in enumerate(kf.split(df)):
    folds.append(fit_eval(tr, te, f"random_fold{i}"))
results["checks"]["random_5fold"] = {
    "folds": folds,
    "mean_mae": round(np.mean([f["mae"] for f in folds]), 4),
    "mean_improvement_pct": round(np.mean([f["improvement_pct"] for f in folds]), 2)}

# 2. cohort holdout (both directions)
log("=== cohort_holdout ===")
if "cohort" in df.columns:
    cohorts = list(df["cohort"].astype(str).unique())
    log(f"cohorts: {cohorts}")
    ch = []
    idx_all = np.arange(len(df))
    cohort_str = df["cohort"].astype(str).values
    for test_cohort in cohorts:
        te = idx_all[cohort_str == test_cohort]
        tr = idx_all[cohort_str != test_cohort]
        if len(te) and len(tr):
            ch.append(fit_eval(tr, te, f"train_rest->test_{test_cohort}"))
    results["checks"]["cohort_holdout"] = ch
else:
    results["checks"]["cohort_holdout"] = "no_cohort_column"

# 3. group by pair
log("=== group_by_pair (5-fold) ===")
gkf = GroupKFold(n_splits=5)
groups = df["pair"].astype(str).values
gfolds = []
for i, (tr, te) in enumerate(gkf.split(df, y, groups)):
    n_test_pairs = len(set(groups[te]))
    r = fit_eval(tr, te, f"pairgroup_fold{i}")
    r["n_test_pairs"] = n_test_pairs
    gfolds.append(r)
results["checks"]["group_by_pair"] = {
    "folds": gfolds,
    "mean_mae": round(np.mean([f["mae"] for f in gfolds]), 4),
    "mean_improvement_pct": round(np.mean([f["improvement_pct"] for f in gfolds]), 2),
    "note": "strips 'pair' (the #1 feature) -> includes a legitimate penalty, not pure leakage"}

json.dump(results, open(OUT, "w"), indent=2)
log(f"WROTE {OUT}")
log("=== SUMMARY ===")
log(f"random_5fold mean MAE     : {results['checks']['random_5fold']['mean_mae']}")
if isinstance(results["checks"]["cohort_holdout"], list):
    for c in results["checks"]["cohort_holdout"]:
        log(f"cohort {c['tag']:32s}: {c['mae']}")
log(f"group_by_pair mean MAE    : {results['checks']['group_by_pair']['mean_mae']}")
