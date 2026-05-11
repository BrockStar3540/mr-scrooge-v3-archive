"""Walk-forward stability test on 1,577 simulated dbb_trend trades.

5 chronological folds. Each fold: train on data before fold start, test
on the fold window. Compute AUC + filter sumR per fold. Consistency
across folds = signal is stable, not a temporal artifact."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import roc_auc_score

REPO = Path.home() / "mr-scrooge-v3"
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))
from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES
from scrooge_v3.advisors.ml_observer.config import XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING
from train_v2 import backfill_extras, parse, to_vec
from calibrate_dbb import load_corpus, vectorize


def main():
    j = load_corpus()
    dbb = j[j["strategy"] == "dbb_trend"].copy().reset_index(drop=True)
    dbb = dbb.sort_values("ts").reset_index(drop=True)
    print(f"dbb_trend trades: {len(dbb)}")

    X = vectorize(dbb)
    y = dbb["is_win"].astype(np.float32).values
    r = dbb["realized_r"].astype(np.float32).values

    # 5 folds: cumulative training, fixed-size rolling test
    n = len(dbb)
    n_folds = 5
    fold_size = n // (n_folds + 1)  # leave first fold for initial training
    print(f"fold_size={fold_size}, initial train size={fold_size}")

    rows = []
    for k in range(n_folds):
        train_end = fold_size * (k + 1)
        test_end = min(train_end + fold_size, n)
        Xtr, ytr = X[:train_end], y[:train_end]
        Xte, yte = X[train_end:test_end], y[train_end:test_end]
        rte = r[train_end:test_end]
        if pd.Series(yte).nunique() < 2 or len(yte) < 10: continue

        # Use last ~20% of training as val for early stop + calibration
        v_split = int(0.8 * train_end)
        Xtr_only, Xtv = Xtr[:v_split], Xtr[v_split:]
        ytr_only, ytv = ytr[:v_split], ytr[v_split:]

        dtr = xgb.DMatrix(Xtr_only, label=ytr_only, feature_names=FEATURE_NAMES)
        dtv = xgb.DMatrix(Xtv, label=ytv, feature_names=FEATURE_NAMES)
        dte = xgb.DMatrix(Xte, label=yte, feature_names=FEATURE_NAMES)

        booster = xgb.train(
            params={**XGB_PARAMS, "eval_metric": ["logloss","auc"]},
            dtrain=dtr, num_boost_round=XGB_NUM_ROUNDS,
            evals=[(dtr,"tr"), (dtv,"val")],
            early_stopping_rounds=XGB_EARLY_STOPPING, verbose_eval=False,
        )
        # Calibrate on val
        p_val = booster.predict(dtv)
        iso = IsotonicRegression(out_of_bounds="clip")
        iso.fit(p_val, ytv)

        # Predict on test
        p_raw = booster.predict(dte)
        p_cal = iso.predict(p_raw)
        try:
            auc_raw = roc_auc_score(yte, p_raw)
            auc_cal = roc_auc_score(yte, p_cal)
        except ValueError:
            auc_raw = auc_cal = float("nan")

        # Filter scenarios at p>=0.5
        sel = p_cal >= 0.5
        wr_filt = float(yte[sel].mean()) if sel.sum() else float("nan")
        sumR_filt = float(rte[sel].sum())

        ts_start = dbb.iloc[train_end]["ts"]
        ts_end = dbb.iloc[test_end-1]["ts"]
        rows.append({
            "fold": k+1, "train_n": train_end, "test_n": len(yte),
            "test_start": ts_start, "test_end": ts_end,
            "test_baseline_WR": float(yte.mean()),
            "test_baseline_sumR": float(rte.sum()),
            "AUC_raw": auc_raw, "AUC_cal": auc_cal,
            "n_p>=0.5": int(sel.sum()),
            "WR_p>=0.5": wr_filt, "sumR_p>=0.5": sumR_filt,
        })

    df = pd.DataFrame(rows)
    print()
    print(df.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    print()
    print("=== Fold averages ===")
    print(f"  AUC_cal mean={df['AUC_cal'].mean():.3f}  std={df['AUC_cal'].std():.3f}")
    print(f"  WR_p>=0.5 mean={df['WR_p>=0.5'].mean():.3f}  std={df['WR_p>=0.5'].std():.3f}")
    print(f"  sumR_p>=0.5 mean={df['sumR_p>=0.5'].mean():+.2f}  std={df['sumR_p>=0.5'].std():.2f}")
    print(f"  baseline sumR mean={df['test_baseline_sumR'].mean():+.2f}")


if __name__ == "__main__":
    main()
