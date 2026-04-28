"""Train ML observer model on the 18k sim corpus with the NEW unified
79-feature schema (after features.py was updated 2026-04-28).

The corpus rows were generated before the schema bump, so their
`ml_features` dicts don't have the 18 enriched keys. We backfill them at
load time from the same source dicts the live extractor will use:
features.bollinger, classifications, scorer, candidate.
"""
from __future__ import annotations
import json, sys, logging
from pathlib import Path
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import roc_auc_score

REPO = Path.home() / "mr-scrooge-v3"
sys.path.insert(0, str(REPO / "src"))

from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES
from scrooge_v3.advisors.ml_observer.config import (
    XGB_PARAMS, XGB_NUM_ROUNDS, XGB_EARLY_STOPPING,
)

REPLAY = Path.home() / "Oanda-Bot-Trainer" / "data" / "replay"
OUT = REPO / "data" / "ml-observer-offline"

_BB_STATE_MAP = {"NORMAL": 0, "REJECTION_LONG": 1, "REJECTION_SHORT": 2,
                 "STRETCH_UP": 3, "STRETCH_DOWN": 4, "TREND_UP": 5, "TREND_DOWN": 6}
_REGIME_MAP = {"NORMAL": 0, "CAUTION": 1, "RESTRICTED": 2}
_STRATEGY_MAP = {"reversal": 0, "direct": 1, "dbb_trend": 2, "trend": 3}

log = logging.getLogger("train-v2")


def parse(raw):
    if isinstance(raw, dict): return raw
    if isinstance(raw, str):
        try: return json.loads(raw.replace("Infinity", "1e9").replace("NaN", "0"))
        except: return {}
    return {}


def safe(v, d=0.0):
    try:
        f = float(v)
        return f if np.isfinite(f) else d
    except (TypeError, ValueError):
        return d


def backfill_extras(row, mf):
    """Populate the 18 enriched keys in ml_features from row's other dicts.
    Mirrors the logic in features.py (build_scan_row enriched block)."""
    if "natural_stop_pips" in mf:
        return mf  # already present
    feat = parse(row.get("features", {}))
    cls = parse(row.get("classifications", {}))
    sc = parse(row.get("scorer", {}))
    cand = parse(row.get("candidate", {})) if row.get("candidate") is not None else {}
    boll = parse(feat.get("bollinger", {}))

    sma_a = safe(boll.get("sma_a"))
    upper_a = safe(boll.get("upper_a"))
    lower_a = safe(boll.get("lower_a"))
    upper_b = safe(boll.get("upper_b"))
    lower_b = safe(boll.get("lower_b"))
    cur = safe(boll.get("current_close"))
    pct_b_a = safe(boll.get("percent_b_a", boll.get("percent_b")))
    pct_b_b = safe(boll.get("percent_b_b"))

    sma_dist_bps = ((cur - sma_a) / sma_a * 1e4) if sma_a > 0 else 0.0
    bw_a = ((upper_a - lower_a) / sma_a * 1e4) if sma_a > 0 else 0.0
    bw_b = ((upper_b - lower_b) / sma_a * 1e4) if sma_a > 0 else 0.0

    bb_label = (cls.get("bb_state") or {}).get("label", "NORMAL") if isinstance(cls.get("bb_state"), dict) else "NORMAL"
    regime_label = (cls.get("regime") or {}).get("label", "NORMAL") if isinstance(cls.get("regime"), dict) else "NORMAL"

    cand_dir = str(cand.get("direction") or "")
    cand_strat = str(cand.get("strategy") or "")
    entry = safe(cand.get("entry_price"))
    stop = safe(cand.get("stop_price"))
    tp = safe(cand.get("take_profit"))

    sym = str(row.get("symbol") or "")
    pip = 0.01 if any(j in sym for j in ("JPY", "MXN")) else 0.0001
    nat_stop = abs(entry - stop) / pip if (entry and stop) else 0.0
    tp_dist = abs(entry - tp) / pip if (entry and tp) else 0.0
    rr = (tp_dist / nat_stop) if nat_stop > 0 else 0.0
    spread = safe(row.get("spread"))
    spread_pips = (spread * 1e4) if pip == 0.0001 else (spread * 1e2)
    sp_to_stop = (spread_pips / nat_stop) if nat_stop > 0 else 0.0

    score = safe(sc.get("score"))
    floor = safe(sc.get("floor"))
    b_thr = safe(sc.get("b"))
    a_thr = safe(sc.get("a"))

    mf.update({
        "sma20_dist_signed_bps": sma_dist_bps,
        "bb_band_width_a_bps": bw_a,
        "bb_band_width_b_bps": bw_b,
        "bb_percent_b_a": pct_b_a,
        "bb_percent_b_b": pct_b_b,
        "bb_state_id": float(_BB_STATE_MAP.get(bb_label, 0)),
        "regime_id": float(_REGIME_MAP.get(regime_label, 0)),
        "strategy_id": float(_STRATEGY_MAP.get(cand_strat, 0)),
        "direction_long": 1.0 if cand_dir == "long" else 0.0,
        "tier_b_flag": 1.0 if (b_thr and score >= b_thr) else 0.0,
        "tier_a_flag": 1.0 if (a_thr and score >= a_thr) else 0.0,
        "score_minus_floor": score - floor,
        "score_above_b": score - b_thr,
        "natural_stop_pips": nat_stop,
        "tp_distance_pips": tp_dist,
        "rr_ratio": rr,
        "spread_pips": spread_pips,
        "spread_to_stop_ratio": sp_to_stop,
    })
    return mf


def to_vec(mf):
    return [safe(mf.get(n, 0.0)) for n in FEATURE_NAMES]


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    log.info("FEATURE_NAMES count = %d", len(FEATURE_NAMES))

    sc = pd.read_parquet(REPLAY / "oanda_180d_scans_accepted.parquet")
    tr = pd.read_parquet(REPLAY / "oanda_180d_training_set.parquet")
    sc["ts"] = pd.to_datetime(sc["ts"], utc=True)
    tr["ts"] = pd.to_datetime(tr["ts"], utc=True)
    j = sc.merge(tr[["ts", "symbol", "is_win", "realized_r"]],
                 on=["symbol", "ts"], how="inner")
    log.info("joined=%d", len(j))

    log.info("vectorizing...")
    X = []
    for _, r in j.iterrows():
        mf = parse(r["ml_features"])
        mf = backfill_extras(r, mf)
        X.append(to_vec(mf))
    X = np.asarray(X, dtype=np.float32)
    y = j["is_win"].astype(np.float32).values
    log.info("X=%s y=%s", X.shape, y.shape)

    # Time-series holdout
    split = pd.Timestamp("2026-03-01T00:00:00Z")
    tr_mask = j["ts"].values < split.to_numpy()
    te_mask = ~tr_mask

    Xtr, Xte = X[tr_mask], X[te_mask]
    ytr, yte = y[tr_mask], y[te_mask]
    rte = j.loc[te_mask, "realized_r"].values

    dtr = xgb.DMatrix(Xtr, label=ytr, feature_names=FEATURE_NAMES)
    dte = xgb.DMatrix(Xte, label=yte, feature_names=FEATURE_NAMES)
    booster = xgb.train(
        params={**XGB_PARAMS, "eval_metric": ["logloss", "auc", "error"]},
        dtrain=dtr, num_boost_round=XGB_NUM_ROUNDS,
        evals=[(dtr, "train"), (dte, "test")],
        early_stopping_rounds=50,
        verbose_eval=20,
    )
    pte = booster.predict(dte)
    log.info("best_round=%d  TEST_AUC=%.4f  test_err=%.4f",
             booster.best_iteration + 1,
             roc_auc_score(yte, pte),
             float(((pte > 0.5) != yte.astype(bool)).mean()))

    # Save: replace LIVE model file
    booster.save_model(str(OUT / "model.xgb"))
    booster.save_model(str(OUT / "model_v2_79f.xgb"))
    log.info("saved -> %s and %s", OUT / "model.xgb", OUT / "model_v2_79f.xgb")

    # Feature importance for the new 18
    fi = booster.get_score(importance_type="gain")
    new_feats = FEATURE_NAMES[-18:]
    log.info("\n=== Importance — enriched 18 ===")
    for f in new_feats:
        if f in fi:
            log.info("  %-30s gain=%.2f", f, fi[f])

    log.info("\n=== OOS filter scenarios ===")
    log.info("  baseline-take-all WR=%.3f sumR=%+.2f", yte.mean(), rte.sum())
    for thr in [0.3, 0.4, 0.5, 0.6, 0.7]:
        sel = pte >= thr
        n = int(sel.sum())
        if n == 0: continue
        wr = yte[sel].mean(); sr = rte[sel].sum()
        log.info("  p>=%.1f  n=%d (%.1f%%)  WR=%.3f  sumR=%+.2f  avgR=%+.3f",
                 thr, n, 100 * n / len(yte), wr, sr, sr / n)


if __name__ == "__main__":
    main()
