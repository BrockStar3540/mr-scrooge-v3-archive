"""v4 scorer trainer -- XGBoost on the assembled training set.

Produces three outputs per Brock v4 spec heads:
  Head A: should_trade  -- binary classifier, P(is_win=True)
  Head B: expected_r    -- regressor, realized_R
  (Head C: rank — deferred until we have multi-candidate-per-tick data)

Saves:
  v4_scorer_model_A.json     XGBoost binary classifier
  v4_scorer_model_B.json     XGBoost regressor
  v4_scorer_features.json    feature name list + categorical maps
  v4_scorer_metrics.json     AUC, Brier, calibration, RMSE per split
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import xgboost as xgb
except ImportError:
    print("xgboost not installed. Install with: pip install xgboost")
    raise

from sklearn.metrics import (
    roc_auc_score, brier_score_loss, mean_squared_error,
)


CATEGORICAL_COLS = [
    "technical_regime_53", "parent_regime", "pair", "direction",
    "session_bucket", "cell_tier", "cell_source_bank",
]
NUMERIC_COLS = [
    "hour_utc", "day_of_week",
    "ATR_ratio", "BB_compress", "ADX14", "RSI14", "close_pos", "bb_position",
    "volume_ratio", "z_score", "ema20_dist_pct", "ema50_dist_pct",
    "sma20_dist_signed_bps",
    "cell_tier_rank", "cell_n_unique", "cell_wr", "cell_wilson_lb",
]


def build_categorical_maps(df):
    """Stable categorical encoding for inference."""
    maps = {}
    for c in CATEGORICAL_COLS:
        if c not in df.columns: continue
        vals = sorted(df[c].dropna().astype(str).unique().tolist())
        maps[c] = {v: i for i, v in enumerate(vals)}
    return maps


def encode(df, maps):
    out = df.copy()
    for c, m in maps.items():
        out[c] = out[c].astype(str).map(m).fillna(-1).astype(int)
    for c in NUMERIC_COLS:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce").fillna(0.0)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--training-set", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--n-estimators", type=int, default=400)
    ap.add_argument("--max-depth", type=int, default=6)
    ap.add_argument("--learning-rate", type=float, default=0.05)
    args = ap.parse_args()

    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)

    print(f"Loading training set: {args.training_set}")
    df = pd.read_parquet(args.training_set)
    print(f"  rows: {len(df):,}")
    print(f"  split: {df.v4_split.value_counts().to_dict()}")
    print(f"  overall WR: {df.is_win.mean():.4f}")

    maps = build_categorical_maps(df)
    print(f"  categorical maps: {[(k, len(v)) for k, v in maps.items()]}")

    enc = encode(df, maps)
    train = enc[enc.v4_split == "train"]
    test = enc[enc.v4_split == "test"]
    print(f"  train rows: {len(train):,}  test rows: {len(test):,}")

    feature_cols = [c for c in (CATEGORICAL_COLS + NUMERIC_COLS) if c in enc.columns]
    print(f"  features: {len(feature_cols)}")

    X_train = train[feature_cols].values
    X_test = test[feature_cols].values

    metrics = {"train_rows": len(train), "test_rows": len(test),
               "feature_cols": feature_cols, "train_wr": float(train.is_win.mean()),
               "test_wr": float(test.is_win.mean())}

    # ---- Head A: should_trade (binary classifier) ----
    print("\n=== Head A: should_trade (binary classifier) ===")
    y_train_a = train.is_win.astype(int).values
    y_test_a = test.is_win.astype(int).values
    pos_rate = y_train_a.mean()
    scale_pos = (1 - pos_rate) / max(pos_rate, 1e-6)
    print(f"  class balance (train pos rate): {pos_rate:.4f}  scale_pos_weight={scale_pos:.2f}")

    model_a = xgb.XGBClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        learning_rate=args.learning_rate,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="binary:logistic",
        eval_metric="auc",
        scale_pos_weight=scale_pos,
        tree_method="hist",
        random_state=42,
    )
    model_a.fit(X_train, y_train_a,
                eval_set=[(X_test, y_test_a)], verbose=False)
    p_test_a = model_a.predict_proba(X_test)[:, 1]
    auc_a = roc_auc_score(y_test_a, p_test_a)
    brier_a = brier_score_loss(y_test_a, p_test_a)
    print(f"  test AUC: {auc_a:.4f}  Brier: {brier_a:.4f}")

    # Calibration by decile
    cal_rows = []
    deciles = pd.qcut(p_test_a, q=10, labels=False, duplicates="drop")
    for d in sorted(np.unique(deciles)):
        mask = deciles == d
        cal_rows.append({
            "decile": int(d),
            "n": int(mask.sum()),
            "mean_pred": float(p_test_a[mask].mean()),
            "actual_wr": float(y_test_a[mask].mean()),
        })
    print("  calibration (decile, pred, actual):")
    for r in cal_rows:
        print(f"    d={r['decile']}: n={r['n']:>5d} pred={r['mean_pred']:.3f} act={r['actual_wr']:.3f}")
    metrics["head_a"] = {
        "auc_test": auc_a, "brier_test": brier_a,
        "calibration": cal_rows,
    }
    model_a.save_model(str(out / "v4_scorer_model_A.json"))

    # ---- Head B: expected_r (regressor) ----
    print("\n=== Head B: expected_r (regressor on realized_R) ===")
    y_train_b = train.realized_R.fillna(0).astype(float).values
    y_test_b = test.realized_R.fillna(0).astype(float).values
    model_b = xgb.XGBRegressor(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        learning_rate=args.learning_rate,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        eval_metric="rmse",
        tree_method="hist",
        random_state=42,
    )
    model_b.fit(X_train, y_train_b,
                eval_set=[(X_test, y_test_b)], verbose=False)
    pred_b = model_b.predict(X_test)
    rmse_b = float(np.sqrt(mean_squared_error(y_test_b, pred_b)))
    pearson_b = float(np.corrcoef(y_test_b, pred_b)[0, 1])
    print(f"  test RMSE: {rmse_b:.4f}  Pearson r: {pearson_b:.4f}")
    print(f"  predicted R distribution: mean={pred_b.mean():.3f} std={pred_b.std():.3f}")
    print(f"  actual R distribution:    mean={y_test_b.mean():.3f} std={y_test_b.std():.3f}")
    metrics["head_b"] = {"rmse_test": rmse_b, "pearson_test": pearson_b}
    model_b.save_model(str(out / "v4_scorer_model_B.json"))

    # Features + maps
    feature_meta = {
        "feature_cols": feature_cols,
        "categorical_maps": maps,
        "numeric_cols": [c for c in NUMERIC_COLS if c in enc.columns],
        "trained_at": pd.Timestamp.now(tz="UTC").isoformat(),
    }
    (out / "v4_scorer_features.json").write_text(json.dumps(feature_meta, indent=2))
    (out / "v4_scorer_metrics.json").write_text(json.dumps(metrics, indent=2))

    print(f"\n-> {out}/v4_scorer_model_A.json")
    print(f"-> {out}/v4_scorer_model_B.json")
    print(f"-> {out}/v4_scorer_features.json")
    print(f"-> {out}/v4_scorer_metrics.json")

    # Promotion gate summary
    print("\n=== Promotion gates (per spec) ===")
    pass_a = "PASS" if auc_a >= 0.60 else "BELOW_BAR"
    print(f"  Head A AUC >= 0.60: {auc_a:.3f} -> {pass_a}")
    pass_b = "PASS" if abs(pearson_b) >= 0.10 else "BELOW_BAR"
    print(f"  Head B Pearson >= 0.10: {pearson_b:.3f} -> {pass_b}")
    if pass_a == "PASS":
        print("\n  Phase 2 (shadow alongside v3) is GREEN-LIT.")
    else:
        print("\n  Phase 2 NOT YET green-lit. Retrain with more data or features.")


if __name__ == "__main__":
    main()
