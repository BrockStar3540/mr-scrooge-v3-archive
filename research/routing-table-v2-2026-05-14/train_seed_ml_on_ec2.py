"""Train the seed-bank ML model on EC2.

Reads /tmp/ml_training_corpus.parquet (54,829 rows / 6,779W / 48,050L)
prepared on Mini. Trains XGBoost. Saves model + encodings + metrics.
"""
import pandas as pd
import numpy as np
import json
import xgboost as xgb
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score, log_loss
)

CORPUS = Path("/tmp/ml_training_corpus.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/data/ml-observer")

# Feature schema — must be computable at V3 inference time.
# All 6 market features come from the technical_regime_53 V3 feature.
# Categorical IDs derived at inference from regime/symbol/session_bucket/direction.
SEED_FEATURE_NAMES = [
    # Market (from technical_regime_53 feature values)
    "ATR14", "BB_width", "ADX14", "EMA_slope", "RSI14", "close_pos",
    # Categorical IDs
    "regime53_id", "pair_id", "session_id", "direction_long",
    # Temporal
    "hour_utc", "day_of_week",
]


def session_bucket(h):
    if 0 <= h < 4:   return "asia"
    if 4 <= h < 6:   return "asia_late"
    if 6 <= h < 9:   return "london_open"
    if 9 <= h < 13:  return "ny_open"
    if 13 <= h < 17: return "ny_mid"
    if 17 <= h < 21: return "ny_close"
    return "off_hours"


print("loading corpus ...", flush=True)
df = pd.read_parquet(CORPUS)
print(f"  rows: {len(df):,}  W={int(df.is_win.sum())}  L={int((~df.is_win).sum())}  WR={df.is_win.mean():.1%}")

# Add categorical / temporal columns
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
df["hour_utc"] = df["entry_ts"].dt.hour.astype(int)
df["day_of_week"] = df["entry_ts"].dt.weekday.astype(int)
df["session_bucket"] = df["hour_utc"].apply(session_bucket)

REGIME_CODES = sorted(df.technical_regime_53.unique().tolist())
PAIR_CODES   = sorted(df.pair.unique().tolist())
SESSION_CODES= ["asia","asia_late","london_open","ny_open","ny_mid","ny_close","off_hours"]

regime_id  = {c:i for i,c in enumerate(REGIME_CODES)}
pair_id    = {c:i for i,c in enumerate(PAIR_CODES)}
session_id = {c:i for i,c in enumerate(SESSION_CODES)}

df["regime53_id"]    = df["technical_regime_53"].map(regime_id).astype(int)
df["pair_id"]        = df["pair"].map(pair_id).astype(int)
df["session_id"]     = df["session_bucket"].map(session_id).astype(int)
df["direction_long"] = (df["direction"].astype(str).str.lower() == "long").astype(int)

print(f"\n  regimes: {len(REGIME_CODES)}  pairs: {len(PAIR_CODES)}  sessions: {len(SESSION_CODES)}")

# Build (X, y)
X = df[SEED_FEATURE_NAMES].astype(float).values
y = df["is_win"].astype(int).values

# Stratified split
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print(f"  train: {len(X_train):,}  val: {len(X_val):,}")
pos_weight = (y_train == 0).sum() / max(1, (y_train == 1).sum())
print(f"  scale_pos_weight: {pos_weight:.2f}")

dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=SEED_FEATURE_NAMES)
dval   = xgb.DMatrix(X_val,   label=y_val,   feature_names=SEED_FEATURE_NAMES)

params = {
    "objective": "binary:logistic",
    "eval_metric": ["auc", "logloss"],
    "max_depth": 5,
    "eta": 0.05,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "scale_pos_weight": float(pos_weight),
    "tree_method": "hist",
    "seed": 42,
}

print("\ntraining XGBoost (600 rounds, ES=30) ...", flush=True)
model = xgb.train(
    params, dtrain, num_boost_round=600,
    evals=[(dtrain,"train"), (dval,"val")],
    early_stopping_rounds=30, verbose_eval=100,
)

# Predictions
preds_train = model.predict(dtrain)
preds_val   = model.predict(dval)


def metrics(y_true, p, thr=0.5):
    yhat = (p >= thr).astype(int)
    return {
        "n": int(len(y_true)),
        "wr_in_data": float(y_true.mean()),
        "auc": float(roc_auc_score(y_true, p)),
        "accuracy_thr0.5": float(accuracy_score(y_true, yhat)),
        "precision_thr0.5": float(precision_score(y_true, yhat, zero_division=0)),
        "recall_thr0.5": float(recall_score(y_true, yhat, zero_division=0)),
        "logloss": float(log_loss(y_true, p)),
        "mean_p_when_win": float(p[y_true == 1].mean()) if (y_true == 1).sum() else None,
        "mean_p_when_loss": float(p[y_true == 0].mean()) if (y_true == 0).sum() else None,
    }


m_train = metrics(y_train, preds_train)
m_val   = metrics(y_val, preds_val)

print("\n=== METRICS ===")
print(f"  TRAIN: AUC={m_train['auc']:.3f}  acc={m_train['accuracy_thr0.5']:.3f}  prec={m_train['precision_thr0.5']:.3f}  recall={m_train['recall_thr0.5']:.3f}")
print(f"  VAL:   AUC={m_val['auc']:.3f}  acc={m_val['accuracy_thr0.5']:.3f}  prec={m_val['precision_thr0.5']:.3f}  recall={m_val['recall_thr0.5']:.3f}")
print(f"         mean p(win) on actual wins:   {m_val['mean_p_when_win']:.3f}")
print(f"         mean p(win) on actual losses: {m_val['mean_p_when_loss']:.3f}")

# Calibration buckets
print("\n=== VAL CALIBRATION (held-out) ===")
print(f"  {'bucket':<12} {'n':>6} {'wins':>6} {'WR_actual':>11} {'mean_p_pred':>12}")
for lo, hi, label in [(0.0,0.3,"<0.3"), (0.3,0.5,"0.3-0.5"),
                       (0.5,0.7,"0.5-0.7"), (0.7,0.85,"0.7-0.85"), (0.85,1.01,">=0.85")]:
    mask = (preds_val >= lo) & (preds_val < hi)
    n = int(mask.sum())
    if n == 0: continue
    w = int(y_val[mask].sum())
    print(f"  {label:<12} {n:>6} {w:>6} {w/n:>11.1%} {preds_val[mask].mean():>12.3f}")

# Feature importance
imp = model.get_score(importance_type="gain")
imp_sorted = sorted(imp.items(), key=lambda x: -x[1])
print(f"\n=== FEATURE IMPORTANCE (gain) ===")
for n, g in imp_sorted:
    print(f"  {n:<22}  {g:>10.1f}")

# Save artifacts in observer dir
OUT.mkdir(parents=True, exist_ok=True)
# XGBoost native JSON format
model.save_model(str(OUT / "model.json"))
# Also save in legacy .xgb path (some loaders look for it; we'll point to .json)
model.save_model(str(OUT / "model.xgb"))

with (OUT / "seed_ml_encodings.json").open("w") as fh:
    json.dump({
        "feature_names": SEED_FEATURE_NAMES,
        "regime53_to_id": regime_id,
        "pair_to_id": pair_id,
        "session_to_id": session_id,
        "direction_to_id": {"short": 0, "long": 1},
        "trained_at": pd.Timestamp.utcnow().isoformat(),
        "corpus_size": int(len(df)),
        "training_corpus": "moving-regime 54,829 trades (textbook + trainer probes), last 6mo, dense regime53",
    }, fh, indent=2)

with (OUT / "seed_ml_metrics.json").open("w") as fh:
    json.dump({
        "trained_at": pd.Timestamp.utcnow().isoformat(),
        "train_rows": len(X_train),
        "val_rows": len(X_val),
        "n_features": len(SEED_FEATURE_NAMES),
        "scale_pos_weight": float(pos_weight),
        "best_iteration": int(model.best_iteration) if hasattr(model, "best_iteration") else None,
        "train_metrics": m_train,
        "val_metrics": m_val,
        "feature_importance": [{"feature": n, "gain": round(g, 2)} for n, g in imp_sorted],
    }, fh, indent=2)

print(f"\nsaved -> {OUT}/")
for f in ["model.json", "model.xgb", "seed_ml_encodings.json", "seed_ml_metrics.json"]:
    p = OUT / f
    print(f"  {f}  ({p.stat().st_size/1024:.1f} KB)")
