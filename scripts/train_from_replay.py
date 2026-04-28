"""Offline ML observer training from Oanda-Bot-Trainer replay corpus.

Reads the 18,858-trade 180-day replay set, joins scans+outcomes, fits an
XGBoost win/loss classifier with the same hyperparameters and CV setup
the live trainer uses. Writes the candidate model to a SEPARATE directory
(data/ml-observer-offline/) so live observer state is untouched.

This script does NOT modify any ml_observer source. It only imports
FEATURE_NAMES and XGB_PARAMS read-only.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import xgboost as xgb

REPO = Path.home() / "mr-scrooge-v3"
sys.path.insert(0, str(REPO / "src"))

from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES  # noqa: E402
from scrooge_v3.advisors.ml_observer.config import (  # noqa: E402
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING, XGB_CV_FOLDS,
)

REPLAY = Path.home() / "Oanda-Bot-Trainer" / "data" / "replay"
SCANS_PARQUET = REPLAY / "oanda_180d_scans_accepted.parquet"
TRAINING_PARQUET = REPLAY / "oanda_180d_training_set.parquet"

OUT_DIR = REPO / "data" / "ml-observer-offline"
MODEL_OUT = OUT_DIR / "model.xgb"
REPORT_OUT = OUT_DIR / "training_report.md"

REGIME_SETS = [
    ("covid_shock_2020-03-09", "covid"),
    ("invasion_2022-02-21", "invasion"),
    ("regime_yen_intervention_2024-04-29", "yen_intv"),
    ("us_dst_2024-03-10", "us_dst"),
    ("chop_2023-08-07", "chop"),
    ("trend_2023-07-03", "trend"),
]

log = logging.getLogger("offline-trainer")


def _parse_ml_features(raw) -> dict:
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str):
        try:
            return json.loads(raw.replace("Infinity", "1e9").replace("NaN", "0"))
        except json.JSONDecodeError:
            return {}
    return {}


def _row_to_vector(mf: dict) -> list[float]:
    out = []
    for name in FEATURE_NAMES:
        v = mf.get(name, 0.0)
        try:
            f = float(v)
            if not np.isfinite(f):
                f = 0.0
        except (TypeError, ValueError):
            f = 0.0
        out.append(f)
    return out


def build_dataset(scans_path: Path, outcomes_path: Path) -> tuple[np.ndarray, np.ndarray, pd.DataFrame]:
    scans = pd.read_parquet(scans_path)
    outcomes = pd.read_parquet(outcomes_path)

    log.info("scans=%d outcomes=%d", len(scans), len(outcomes))

    # scans_accepted has trade_id=None (replay artifact). Link via (symbol, ts).
    scans_slim = scans[["ml_features", "verdict", "symbol", "ts"]].copy()
    scans_slim["ts"] = pd.to_datetime(scans_slim["ts"], utc=True)
    outcomes_slim = outcomes[["ts", "symbol", "is_win", "exit_reason", "realized_r"]].copy()
    outcomes_slim["ts"] = pd.to_datetime(outcomes_slim["ts"], utc=True)

    merged = scans_slim.merge(outcomes_slim, on=["symbol", "ts"], how="inner")
    log.info("joined rows=%d", len(merged))

    rows_X, rows_y, kept = [], [], []
    for _, r in merged.iterrows():
        mf = _parse_ml_features(r["ml_features"])
        if not mf:
            continue
        rows_X.append(_row_to_vector(mf))
        rows_y.append(1 if bool(r["is_win"]) else 0)
        kept.append(r)

    X = np.asarray(rows_X, dtype=np.float32)
    y = np.asarray(rows_y, dtype=np.float32)
    kept_df = pd.DataFrame(kept).reset_index(drop=True)
    log.info("vectorized X=%s y_win=%d y_loss=%d", X.shape, int(y.sum()), int(len(y) - y.sum()))
    return X, y, kept_df


def train(X: np.ndarray, y: np.ndarray) -> tuple[xgb.Booster, dict]:
    dtrain = xgb.DMatrix(X, label=y, feature_names=FEATURE_NAMES)
    log.info("running %d-fold CV (rounds=%d)", XGB_CV_FOLDS, XGB_NUM_ROUNDS)
    cv = xgb.cv(
        params={**XGB_PARAMS, "eval_metric": ["logloss", "auc", "error"]},
        dtrain=dtrain,
        num_boost_round=XGB_NUM_ROUNDS,
        nfold=XGB_CV_FOLDS,
        early_stopping_rounds=XGB_EARLY_STOPPING,
        seed=XGB_PARAMS["seed"],
        stratified=True,
        as_pandas=True,
    )
    best_round = len(cv)
    final = cv.iloc[-1].to_dict()
    log.info("CV done at round=%d", best_round)
    log.info("CV final: logloss=%.4f auc=%.4f error=%.4f",
             final["test-logloss-mean"], final["test-auc-mean"], final["test-error-mean"])

    booster = xgb.train(
        params=XGB_PARAMS,
        dtrain=dtrain,
        num_boost_round=best_round,
    )
    metrics = {
        "best_round": best_round,
        "cv_logloss": final["test-logloss-mean"],
        "cv_logloss_std": final["test-logloss-std"],
        "cv_auc": final["test-auc-mean"],
        "cv_auc_std": final["test-auc-std"],
        "cv_accuracy": 1.0 - final["test-error-mean"],
        "cv_accuracy_std": final["test-error-std"],
    }
    return booster, metrics


def feature_importance(booster: xgb.Booster, top: int = 25) -> list[tuple[str, float]]:
    score = booster.get_score(importance_type="gain")
    items = sorted(score.items(), key=lambda kv: kv[1], reverse=True)
    return items[:top]


def score_buckets(booster: xgb.Booster, X: np.ndarray, y: np.ndarray) -> pd.DataFrame:
    p = booster.predict(xgb.DMatrix(X, feature_names=FEATURE_NAMES))
    df = pd.DataFrame({"p": p, "y": y})
    df["bucket"] = pd.cut(df["p"], bins=[0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0],
                          include_lowest=True, right=False)
    g = df.groupby("bucket", observed=True).agg(n=("y", "size"), wins=("y", "sum"))
    g["win_rate"] = g["wins"] / g["n"]
    return g


def evaluate_regime_sets(booster: xgb.Booster) -> list[dict]:
    results = []
    for stem, label in REGIME_SETS:
        scans_p = REPLAY / f"{stem}.parquet"
        opens_p = REPLAY / f"{stem}.opens.parquet"
        closes_p = REPLAY / f"{stem}.closes.parquet"
        if not (scans_p.exists() and opens_p.exists() and closes_p.exists()):
            log.info("skip regime set %s — missing files", label)
            continue
        try:
            scans = pd.read_parquet(scans_p)
            closes = pd.read_parquet(closes_p)
            keep = scans[scans["verdict"].isin(["TAKE_A", "TAKE_B"])][["trade_id", "ml_features"]]
            j = keep.merge(closes[["trade_id", "exit_reason"]], on="trade_id", how="inner")
            if j.empty:
                continue
            j["is_win"] = j["exit_reason"].eq("TP")
            X = np.asarray([_row_to_vector(_parse_ml_features(r)) for r in j["ml_features"]], dtype=np.float32)
            y = j["is_win"].astype(np.float32).values
            if len(y) == 0:
                continue
            p = booster.predict(xgb.DMatrix(X, feature_names=FEATURE_NAMES))
            base_wr = float(y.mean())
            taken = (p >= 0.5)
            ml_wr = float(y[taken].mean()) if taken.any() else float("nan")
            results.append({
                "regime": label, "n_trades": int(len(y)),
                "base_win_rate": base_wr, "ml_taken": int(taken.sum()),
                "ml_win_rate": ml_wr, "lift": ml_wr - base_wr if taken.any() else float("nan"),
            })
        except Exception as e:  # noqa: BLE001
            log.warning("regime %s failed: %s", label, e)
    return results


def write_report(metrics: dict, fi: list, buckets: pd.DataFrame, regime: list, X: np.ndarray, y: np.ndarray) -> str:
    lines = []
    lines.append(f"# Offline ML Observer — Training Report\n")
    lines.append(f"**Source:** `oanda_180d_training_set.parquet` (180d replay corpus)\n")
    lines.append(f"**Rows trained:** {len(y)} (wins={int(y.sum())} / losses={int(len(y)-y.sum())}, base WR={y.mean()*100:.1f}%)\n")
    lines.append(f"**Features:** {len(FEATURE_NAMES)}\n")
    lines.append(f"## CV ({XGB_CV_FOLDS}-fold)\n")
    lines.append(f"- accuracy: **{metrics['cv_accuracy']*100:.2f}%** ± {metrics['cv_accuracy_std']*100:.2f}\n")
    lines.append(f"- AUC: **{metrics['cv_auc']:.4f}** ± {metrics['cv_auc_std']:.4f}\n")
    lines.append(f"- logloss: {metrics['cv_logloss']:.4f} ± {metrics['cv_logloss_std']:.4f}\n")
    lines.append(f"- best round: {metrics['best_round']}\n")
    lines.append(f"\n## Top feature importance (gain)\n\n| feature | gain |\n|---|---|\n")
    for name, val in fi:
        lines.append(f"| `{name}` | {val:.2f} |\n")
    lines.append(f"\n## Win rate by predicted score bucket (in-sample)\n\n")
    lines.append(buckets.to_string())
    lines.append("\n")
    if regime:
        lines.append("\n## Regime stress tests (out-of-sample)\n\n")
        rdf = pd.DataFrame(regime)
        lines.append(rdf.to_string(index=False))
        lines.append("\n")
    return "".join(lines)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--no-regime", action="store_true", help="skip regime stress eval")
    p.add_argument("--top-features", type=int, default=25)
    args = p.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    log.info("loading corpus...")
    X, y, kept = build_dataset(SCANS_PARQUET, TRAINING_PARQUET)
    if len(y) == 0:
        sys.exit("no usable rows after vectorize")

    booster, metrics = train(X, y)
    fi = feature_importance(booster, args.top_features)
    buckets = score_buckets(booster, X, y)
    regime = [] if args.no_regime else evaluate_regime_sets(booster)

    booster.save_model(str(MODEL_OUT))
    log.info("model -> %s", MODEL_OUT)

    report = write_report(metrics, fi, buckets, regime, X, y)
    REPORT_OUT.write_text(report)
    log.info("report -> %s", REPORT_OUT)

    print()
    print(report)


if __name__ == "__main__":
    main()
