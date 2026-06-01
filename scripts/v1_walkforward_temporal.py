#!/usr/bin/env python3
"""True temporal walk-forward for the v1 pip-regressor question.

Runs on the time-stamped phase3 corpus (raw features that feed v1's buckets).
The headline is NOT absolute MAE (continuous != v1's bucketed features) but the
GAP between a RANDOM split and a CHRONOLOGICAL split on the SAME data — that
gap is the temporal-leakage estimate that the timeless v1 corpus couldn't give.
"""
import json, time
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import KFold

CORPUS = "/tmp/corpus_timed_phase3.csv.gz"
OUT = "data/lab_training/v1/walkforward_temporal.json"

CAT = ["pair", "strategy_id", "direction_exec", "session_bucket", "variant"]
PARAMS = {"objective": "regression_l1", "metric": ["mae", "rmse"],
          "learning_rate": 0.05, "num_leaves": 127, "min_data_in_leaf": 200,
          "feature_fraction": 0.85, "bagging_fraction": 0.85, "bagging_freq": 5,
          "verbose": -1}
N_ROUNDS = 500

def log(m): print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)

log(f"loading {CORPUS}")
df = pd.read_csv(CORPUS)
df["entry_time"] = pd.to_datetime(df["entry_time"], utc=True, errors="coerce")
df = df.dropna(subset=["entry_time", "pnl_pips"]).sort_values("entry_time").reset_index(drop=True)
NUM = [c for c in df.columns if c not in CAT + ["entry_time", "pnl_pips"]]
FEATS = CAT + NUM
for c in CAT:
    df[c] = df[c].astype("category")
for c in NUM:
    df[c] = pd.to_numeric(df[c], errors="coerce")
y = df["pnl_pips"].astype(float).values
log(f"rows={len(df):,} feats={len(FEATS)} ({len(CAT)} cat / {len(NUM)} num) "
    f"span {df['entry_time'].min().date()}->{df['entry_time'].max().date()}")

def fit_eval(tr, te, tag):
    dtr = lgb.Dataset(df.iloc[tr][FEATS], label=y[tr],
                      categorical_feature=CAT, free_raw_data=False)
    b = lgb.train(PARAMS, dtr, num_boost_round=N_ROUNDS)
    pred = b.predict(df.iloc[te][FEATS])
    mae = float(np.mean(np.abs(pred - y[te])))
    naive = float(np.mean(np.abs(y[te] - y[tr].mean())))
    r = {"tag": tag, "n_train": int(len(tr)), "n_test": int(len(te)),
         "mae": round(mae, 4), "naive_mae": round(naive, 4),
         "improvement_pct": round(100*(naive-mae)/naive, 2)}
    log(f"  {tag}: MAE={mae:.3f} naive={naive:.3f} impr={r['improvement_pct']}%")
    return r

res = {"corpus_rows": int(len(df)), "n_features": len(FEATS),
       "note": "raw features (continuous) on phase3 cohort; compare RANDOM vs CHRONO gap"}

# 1. random 80/20
log("=== random 80/20 ===")
idx = np.arange(len(df))
rng = np.random.RandomState(42); perm = rng.permutation(idx)
cut = int(0.8*len(df))
res["random_8020"] = fit_eval(perm[:cut], perm[cut:], "random_8020")

# 2. CHRONOLOGICAL 80/20 — the true walk-forward (train past, test future)
log("=== chronological 80/20 (TRUE walk-forward) ===")
res["chrono_8020"] = fit_eval(idx[:cut], idx[cut:], "chrono_8020")

# 3. expanding-window walk-forward (4 folds, growing train, next slice test)
log("=== expanding-window walk-forward (4 folds) ===")
folds = []
for k in range(4):
    tr_end = int(len(df)*(0.4 + 0.15*k))
    te_end = int(len(df)*(0.4 + 0.15*(k+1)))
    if te_end <= tr_end: continue
    folds.append(fit_eval(idx[:tr_end], idx[tr_end:te_end], f"expand_fold{k}"))
res["expanding_wf"] = {"folds": folds,
                       "mean_mae": round(float(np.mean([f["mae"] for f in folds])), 4),
                       "mean_improvement_pct": round(float(np.mean([f["improvement_pct"] for f in folds])), 2)}

gap = res["chrono_8020"]["mae"] - res["random_8020"]["mae"]
res["leakage_gap_pips"] = round(gap, 4)
res["leakage_gap_pct_of_random"] = round(100*gap/res["random_8020"]["mae"], 2)

json.dump(res, open(OUT, "w"), indent=2)
log("=== SUMMARY ===")
log(f"random_8020      MAE = {res['random_8020']['mae']}")
log(f"chrono_8020 (WF) MAE = {res['chrono_8020']['mae']}")
log(f"expanding-WF mean MAE = {res['expanding_wf']['mean_mae']}")
log(f"LEAKAGE GAP = {res['leakage_gap_pips']}p ({res['leakage_gap_pct_of_random']}% of random)")
log(f"WROTE {OUT}")
