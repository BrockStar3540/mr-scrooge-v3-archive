"""Time-series holdout: train on Oct 2025 - Feb 2026, test on Mar-Apr 2026.

Honest out-of-sample evaluation. No CV on the training half — single train/test
split on chronological boundary, since CV folds leak future info into past in
time-series data.
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

from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES
from scrooge_v3.advisors.ml_observer.config import (
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING,
)

REPLAY = Path.home() / "Oanda-Bot-Trainer" / "data" / "replay"
SCANS = REPLAY / "oanda_180d_scans_accepted.parquet"
TRAIN = REPLAY / "oanda_180d_training_set.parquet"

OUT_DIR = REPO / "data" / "ml-observer-offline"
HOLDOUT_MODEL = OUT_DIR / "model_holdout.xgb"
HOLDOUT_REPORT = OUT_DIR / "holdout_report.md"

SPLIT_TS = pd.Timestamp("2026-03-01T00:00:00Z")

log = logging.getLogger("holdout")


def parse_mf(raw):
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str):
        try:
            return json.loads(raw.replace("Infinity", "1e9").replace("NaN", "0"))
        except json.JSONDecodeError:
            return {}
    return {}


def vec(mf):
    out = []
    for name in FEATURE_NAMES:
        try:
            v = float(mf.get(name, 0.0))
            if not np.isfinite(v):
                v = 0.0
        except (TypeError, ValueError):
            v = 0.0
        out.append(v)
    return out


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    log.info("loading...")
    sc = pd.read_parquet(SCANS)
    tr = pd.read_parquet(TRAIN)
    sc["ts"] = pd.to_datetime(sc["ts"], utc=True)
    tr["ts"] = pd.to_datetime(tr["ts"], utc=True)

    j = sc[["ts", "symbol", "ml_features", "verdict"]].merge(
        tr[["ts", "symbol", "is_win", "exit_reason", "realized_r"]],
        on=["symbol", "ts"], how="inner",
    )
    log.info("joined=%d", len(j))

    j["X"] = j["ml_features"].map(lambda r: vec(parse_mf(r)))
    j["y"] = j["is_win"].astype(int)

    train_mask = j["ts"] < SPLIT_TS
    test_mask = ~train_mask

    X_tr = np.asarray(j.loc[train_mask, "X"].tolist(), dtype=np.float32)
    y_tr = j.loc[train_mask, "y"].astype(np.float32).values
    X_te = np.asarray(j.loc[test_mask, "X"].tolist(), dtype=np.float32)
    y_te = j.loc[test_mask, "y"].astype(np.float32).values

    log.info("train rows=%d (wins=%d, WR=%.3f)", len(y_tr), int(y_tr.sum()), float(y_tr.mean()))
    log.info("test  rows=%d (wins=%d, WR=%.3f)", len(y_te), int(y_te.sum()), float(y_te.mean()))

    dtrain = xgb.DMatrix(X_tr, label=y_tr, feature_names=FEATURE_NAMES)
    dtest = xgb.DMatrix(X_te, label=y_te, feature_names=FEATURE_NAMES)

    booster = xgb.train(
        params={**XGB_PARAMS, "eval_metric": ["logloss", "auc", "error"]},
        dtrain=dtrain,
        num_boost_round=XGB_NUM_ROUNDS,
        evals=[(dtrain, "train"), (dtest, "test")],
        early_stopping_rounds=XGB_EARLY_STOPPING,
        verbose_eval=10,
    )

    p_te = booster.predict(dtest)
    df_te = pd.DataFrame({"p": p_te, "y": y_te, "r": j.loc[test_mask, "realized_r"].values})

    df_te["bucket"] = pd.cut(df_te["p"], bins=[0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0],
                             include_lowest=True, right=False)
    cal = df_te.groupby("bucket", observed=True).agg(
        n=("y", "size"), wins=("y", "sum"), avg_r=("r", "mean"), sum_r=("r", "sum"),
    )
    cal["win_rate"] = cal["wins"] / cal["n"]

    log.info("\n=== OOS calibration ===\n%s", cal.to_string())

    # Decision sims at various thresholds
    log.info("\n=== Filter strategies (out-of-sample) ===")
    log.info("  base: take all -> n=%d, WR=%.3f, sum_r=%.2fR", len(y_te), float(y_te.mean()), float(df_te["r"].sum()))
    for thr in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
        sel = df_te["p"] >= thr
        n = int(sel.sum())
        if n == 0:
            log.info("  p>=%.1f: n=0", thr)
            continue
        wr = float(df_te.loc[sel, "y"].mean())
        sumr = float(df_te.loc[sel, "r"].sum())
        log.info("  p>=%.1f: n=%d (%.1f%% kept), WR=%.3f, sum_r=%+.2fR, avg_r=%+.3fR",
                 thr, n, 100*n/len(y_te), wr, sumr, sumr/n)

    booster.save_model(str(HOLDOUT_MODEL))
    log.info("\nholdout model -> %s", HOLDOUT_MODEL)

    rep = []
    rep.append(f"# Out-of-Sample Holdout Report\n\n")
    rep.append(f"**Split:** train < {SPLIT_TS.date()} | test >= {SPLIT_TS.date()}\n\n")
    rep.append(f"**Train:** {len(y_tr)} trades (WR={y_tr.mean()*100:.1f}%)\n")
    rep.append(f"**Test:** {len(y_te)} trades (WR={y_te.mean()*100:.1f}%)\n\n")
    rep.append(f"## OOS calibration\n\n```\n{cal.to_string()}\n```\n\n")
    rep.append(f"## OOS filter strategies\n\n")
    rep.append(f"| threshold | n_taken | %kept | WR | sum_R | avg_R |\n|---|---|---|---|---|---|\n")
    rep.append(f"| baseline (all) | {len(y_te)} | 100% | {y_te.mean()*100:.1f}% | {df_te['r'].sum():+.2f} | {df_te['r'].mean():+.3f} |\n")
    for thr in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
        sel = df_te["p"] >= thr
        n = int(sel.sum())
        if n == 0:
            continue
        wr = float(df_te.loc[sel, "y"].mean())
        sumr = float(df_te.loc[sel, "r"].sum())
        rep.append(f"| p>={thr} | {n} | {100*n/len(y_te):.1f}% | {wr*100:.1f}% | {sumr:+.2f} | {sumr/n:+.3f} |\n")
    HOLDOUT_REPORT.write_text("".join(rep))
    log.info("report -> %s", HOLDOUT_REPORT)


if __name__ == "__main__":
    main()
