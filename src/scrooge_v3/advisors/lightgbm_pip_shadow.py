"""LightGBM v1 PIP-prediction shadow scorer — observe-only regression.

v1 (Brock 2026-05-31): regressor predicting pnl_pips (continuous) instead of
P(win). Native pip-eater architecture: "how many pips will this trade collect?"
not "what's the probability it wins?"

Trained on 2.4M trades (legacy 838K + Phase 3 1.55M).
Holdout MAE: 8.01p (15.5% improvement over naive-mean baseline 9.48p).

Output: /home/ubuntu/mr-scrooge-v3/data/lightgbm_pip_shadow.jsonl
Fields: ts, symbol, strategy, direction, session, regime, pred_pips,
        candidate_score, was_picked, n_candidates_this_scan, buckets

Never blocks or alters routing — pure observation. Eventually may promote
to a gate (e.g., require pred_pips >= 4.0p) or join the pip_eater_gate as
a third source alongside pair-module + matrix.
"""
from __future__ import annotations

import json
import logging
import threading
import time
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.shadow.lightgbm_pip")

_MODEL: Any = None
_META: dict | None = None
_LOG_PATH: Path | None = None
_LOCK = threading.Lock()


def load(model_dir: str = "/home/ubuntu/mr-scrooge-v3/data/lab_training/v1",
         log_path: str = "/home/ubuntu/mr-scrooge-v3/data/lightgbm_pip_shadow.jsonl") -> bool:
    """Load v1 regressor model + meta. Returns True on success."""
    global _MODEL, _META, _LOG_PATH
    p = Path(model_dir)
    if not (p / "model.txt").exists():
        log.warning("[SHADOW_PIP] no model at %s — pip-shadow disabled", model_dir)
        return False
    try:
        import lightgbm as lgb  # noqa
        _MODEL = lgb.Booster(model_file=str(p / "model.txt"))
        _META = json.loads((p / "feature_meta.json").read_text())
        _LOG_PATH = Path(log_path)
        _LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        log.info("[SHADOW_PIP] v1 regressor loaded — version=%s, target=%s",
                 _META.get("version", "?"), _META.get("target", "?"))
        return True
    except Exception as e:
        log.error("[SHADOW_PIP] load failed: %s", e)
        _MODEL = None
        return False


def _extract_buckets(ctx) -> dict | None:
    try:
        from scrooge_v3.strategies import ml_router  # type: ignore
        row = ml_router._extract_row_for_buckets(getattr(ctx, "symbol", ""), ctx)
        if row is None:
            return None
        return ml_router._compute_buckets(getattr(ctx, "symbol", ""), row)
    except Exception as e:
        log.debug("[SHADOW_PIP] bucket extract failed: %s", e)
        return None


def predict_pips(symbol: str, ctx, candidate) -> float | None:
    """Predict pnl_pips for a candidate. Returns float or None if not scorable."""
    if _MODEL is None or _META is None:
        return None
    try:
        buckets = _extract_buckets(ctx)
        if buckets is None:
            return None
        from scrooge_v3.strategies import ml_router  # type: ignore
        session = ml_router._session(ctx) or "unknown"
        row = {
            "pair": symbol,
            "strategy_id": candidate.strategy,
            "direction_exec": candidate.direction.value if hasattr(candidate.direction, "value") else str(candidate.direction),
            "session_bucket": session,
            **buckets,
        }
        import pandas as pd  # noqa
        feat_order = _META["feature_order"]
        df = pd.DataFrame([[row.get(c, "NA") for c in feat_order]], columns=feat_order)
        for col in feat_order:
            df[col] = df[col].astype(str).astype("category")
        return float(_MODEL.predict(df)[0])
    except Exception as e:
        log.debug("[SHADOW_PIP] predict_pips failed: %s", e)
        return None


def observe(symbol: str, ctx, best, all_candidates: list | None = None) -> None:
    """Log one line per scan for the picked candidate."""
    if _MODEL is None or _META is None or _LOG_PATH is None:
        return
    try:
        buckets = _extract_buckets(ctx)
        if buckets is None:
            return
        from scrooge_v3.strategies import ml_router  # type: ignore
        session = ml_router._session(ctx) or "unknown"
        row = {
            "pair":           symbol,
            "strategy_id":    best.strategy,
            "direction_exec": best.direction.value if hasattr(best.direction, "value") else str(best.direction),
            "session_bucket": session,
            **buckets,
        }
        import pandas as pd  # noqa
        feat_order = _META["feature_order"]
        df = pd.DataFrame([[row.get(c, "NA") for c in feat_order]], columns=feat_order)
        for col in feat_order:
            df[col] = df[col].astype(str).astype("category")
        pred_pips = float(_MODEL.predict(df)[0])

        # Meal tag — same tiers as pip_eater_gate
        if pred_pips < 0:
            tag = "pip_trick"
        elif pred_pips < 4.0:
            tag = "empty_plate"
        elif pred_pips < 10.0:
            tag = "good_plate"
        elif pred_pips < 20.0:
            tag = "tasty"
        else:
            tag = "optimized_meal"

        entry = {
            "ts":         time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "symbol":     symbol,
            "strategy":   row["strategy_id"],
            "direction":  row["direction_exec"],
            "session":    session,
            "buckets":    buckets,
            "pred_pips":  round(pred_pips, 2),
            "verdict":    tag,
            "candidate_score": float(getattr(best, "score", 0.0)),
            "was_picked": True,
            "n_candidates_this_scan": (len(all_candidates) if all_candidates else 1),
        }
        with _LOCK:
            with _LOG_PATH.open("a") as f:
                f.write(json.dumps(entry) + "\n")
    except Exception as e:
        log.debug("[SHADOW_PIP] observe failed: %s", e)


def is_loaded() -> bool:
    return _MODEL is not None
