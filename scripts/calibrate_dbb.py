"""Train calibrated dbb_trend XGBoost. Validate on real V3 trades + live captures."""
from __future__ import annotations
import json, sys
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
from scrooge_v3.advisors.ml_observer.config import (
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING,
)
from train_v2 import backfill_extras, parse, safe, to_vec

REPLAY = Path.home() / "Oanda-Bot-Trainer" / "data" / "replay"
OUT = REPO / "data" / "ml-observer-offline"


def load_corpus():
    sc = pd.read_parquet(REPLAY / "oanda_180d_scans_accepted.parquet")
    tr = pd.read_parquet(REPLAY / "oanda_180d_training_set.parquet")
    sc["ts"] = pd.to_datetime(sc["ts"], utc=True)
    tr["ts"] = pd.to_datetime(tr["ts"], utc=True)
    j = sc.merge(tr[["ts","symbol","is_win","realized_r"]], on=["symbol","ts"], how="inner")
    j["strategy"] = j["candidate"].apply(
        lambda c: (parse(c) or {}).get("strategy", "unknown") if c else "unknown"
    )
    return j


def vectorize(j):
    X = []
    for _, r in j.iterrows():
        mf = parse(r["ml_features"]); mf = backfill_extras(r, mf)
        X.append(to_vec(mf))
    return np.asarray(X, dtype=np.float32)


def main():
    j = load_corpus()
    dbb = j[j["strategy"] == "dbb_trend"].copy().reset_index(drop=True)
    print(f"dbb_trend trades: {len(dbb)}, base WR={dbb['is_win'].mean()*100:.1f}%")

    # Three-way split: train/val(for calibration)/test
    split1 = pd.Timestamp("2026-02-01", tz="UTC")
    split2 = pd.Timestamp("2026-03-01", tz="UTC")
    train_mask = dbb["ts"].values < split1.to_numpy()
    val_mask = (dbb["ts"].values >= split1.to_numpy()) & (dbb["ts"].values < split2.to_numpy())
    test_mask = dbb["ts"].values >= split2.to_numpy()

    print(f"split: train={train_mask.sum()}  val={val_mask.sum()}  test={test_mask.sum()}")

    X = vectorize(dbb)
    y = dbb["is_win"].astype(np.float32).values
    r = dbb["realized_r"].astype(np.float32).values

    dtrain = xgb.DMatrix(X[train_mask], label=y[train_mask], feature_names=FEATURE_NAMES)
    dval = xgb.DMatrix(X[val_mask], label=y[val_mask], feature_names=FEATURE_NAMES)
    dtest = xgb.DMatrix(X[test_mask], label=y[test_mask], feature_names=FEATURE_NAMES)

    booster = xgb.train(
        params={**XGB_PARAMS, "eval_metric": ["logloss", "auc"]},
        dtrain=dtrain, num_boost_round=XGB_NUM_ROUNDS,
        evals=[(dtrain, "tr"), (dval, "val")],
        early_stopping_rounds=XGB_EARLY_STOPPING, verbose_eval=False,
    )
    print(f"trained best_round={booster.best_iteration+1}")

    # Calibrate on val
    p_val = booster.predict(dval)
    iso = IsotonicRegression(out_of_bounds="clip")
    iso.fit(p_val, y[val_mask])

    # Test set
    p_test_raw = booster.predict(dtest)
    p_test_cal = iso.predict(p_test_raw)
    print(f"\nTEST raw: AUC={roc_auc_score(y[test_mask], p_test_raw):.4f}")
    print(f"TEST cal: AUC={roc_auc_score(y[test_mask], p_test_cal):.4f}")

    # Threshold sweep
    print("\nThreshold sweep on TEST (raw vs cal):")
    print(f"  baseline take all: n={test_mask.sum()} WR={y[test_mask].mean()*100:.1f}% sumR={r[test_mask].sum():+.2f}")
    for thr in [0.3, 0.4, 0.5, 0.6, 0.7]:
        sel_raw = p_test_raw >= thr
        sel_cal = p_test_cal >= thr
        if sel_raw.sum():
            print(f"  raw p>={thr}  n={sel_raw.sum()} WR={y[test_mask][sel_raw].mean()*100:.1f}% sumR={r[test_mask][sel_raw].sum():+.2f}")
        if sel_cal.sum():
            print(f"  cal p>={thr}  n={sel_cal.sum()} WR={y[test_mask][sel_cal].mean()*100:.1f}% sumR={r[test_mask][sel_cal].sum():+.2f}")

    # Retrain on train+val for final deployment model
    X_full = X[~test_mask]
    y_full = y[~test_mask]
    dfull = xgb.DMatrix(X_full, label=y_full, feature_names=FEATURE_NAMES)
    final = xgb.train(
        params={**XGB_PARAMS, "eval_metric": ["logloss", "auc"]},
        dtrain=dfull, num_boost_round=booster.best_iteration + 1,
        verbose_eval=False,
    )
    final.save_model(str(OUT / "model_strategy_dbb_trend.xgb"))

    # Save calibrator
    import joblib
    joblib.dump(iso, str(OUT / "model_strategy_dbb_trend.iso"))
    print(f"\nsaved deployable model -> {OUT/'model_strategy_dbb_trend.xgb'}")
    print(f"saved isotonic -> {OUT/'model_strategy_dbb_trend.iso'}")

    # === Validate on historic real V3 trades (via historic_replay.parquet) ===
    hist_path = REPO / "data/ml-observer-offline/historic_replay.parquet"
    if hist_path.exists():
        hist = pd.read_parquet(hist_path)
        # filter to V3 trades where the replay scan emitted a candidate
        v3_with_cand = hist[(hist["label"] == "V3") & hist["verdict"].isin(["TAKE_A", "TAKE_B"])].copy()
        print(f"\n=== Historic V3 trades with candidate at entry tick: {len(v3_with_cand)} ===")
        if len(v3_with_cand):
            # We don't have strategy in this parquet — re-replay would. For now, skip strategy filter.
            print("(strategy field not preserved in historic_replay.parquet; can't filter to dbb_trend only)")

    # === Validate on 11 live-aligned trades ===
    base = REPO / "data/ml-observer"
    opens = {}
    closes = {}
    with open(base / "outcomes.jsonl") as f:
        for line in f:
            try: rr = json.loads(line)
            except: continue
            tid = rr.get("trade_id")
            if rr.get("kind") == "trade_open": opens[tid] = rr
            elif rr.get("kind") == "trade_close": closes.setdefault(tid, []).append(rr)
    scans_by = {}
    with open(base / "scans.jsonl") as f:
        for line in f:
            try: rr = json.loads(line)
            except: continue
            if str(rr.get("verdict","")).startswith("TAKE_"):
                scans_by[(rr.get("cycle"), rr.get("symbol"))] = rr

    live_dbb = []
    for tid, o in opens.items():
        if tid not in closes: continue
        sc_close = closes[tid][-1]
        scan = scans_by.get((o.get("matched_scan_cycle"), o.get("symbol")))
        if scan is None: continue
        cand = scan.get("candidate") or {}
        if isinstance(cand, str):
            try: cand = json.loads(cand)
            except: cand = {}
        if cand.get("strategy") != "dbb_trend": continue
        mf = scan.get("ml_features", {}) or {}
        mf = backfill_extras(scan, mf)
        Xl = np.asarray([to_vec(mf)], dtype=np.float32)
        p_raw = float(final.predict(xgb.DMatrix(Xl, feature_names=FEATURE_NAMES))[0])
        p_cal = float(iso.predict([p_raw])[0])
        live_dbb.append({
            "trade_id": tid, "symbol": o.get("symbol"),
            "win": sc_close.get("label") == "win",
            "pnl": sc_close.get("realized_pnl_usd"),
            "p_raw": p_raw, "p_cal": p_cal,
        })

    print(f"\n=== Live-aligned dbb_trend trades: {len(live_dbb)} ===")
    if live_dbb:
        df_live = pd.DataFrame(live_dbb)
        print(df_live.to_string())


if __name__ == "__main__":
    main()
