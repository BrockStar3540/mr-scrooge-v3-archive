"""ML-based strategy filter — observe-only by default.

Loads a per-strategy XGBoost model and predicts P(win) for each candidate.
Initially active only for `dbb_trend` strategy where offline analysis showed
OOS AUC 0.774 / 71.8% WR at p>=0.5 (vs 23.5% baseline). For other strategies,
the filter is a no-op.

Operates POST-scorer — needs the full scorer breakdown (sc_hr, sc_age, ...)
that the model was trained on. Called from scan_pipeline after V3 scoring,
before "best candidate" selection.

Modes:
  - "observe": predicts and logs, never blocks. Default.
  - "hard": blocks dbb_trend candidates with p < threshold.

Telemetry: every prediction is logged + emitted into report["gates"]
under name="ml_strategy_filter" so ml-observer captures it.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.gate.ml_strategy_filter")


class MLStrategyFilter:
    """Per-strategy ML gate. Lazy-loads XGBoost models per strategy."""

    name = "ml_strategy_filter"

    # Strategies and their associated model files. Add entries here as new
    # per-strategy models prove out. Strategy names without an entry are
    # passed through unconditionally.
    DEFAULT_MODEL_MAP = {
        "dbb_trend": "data/ml-observer-offline/model_strategy_dbb_trend.xgb",
    }

    # Optional isotonic-regression calibrator per strategy. Maps raw XGBoost
    # probabilities to honest probabilities. Set to None to use raw scores.
    DEFAULT_CALIB_MAP = {
        "dbb_trend": "data/ml-observer-offline/model_strategy_dbb_trend.iso",
    }

    # Per-strategy probability threshold (applied to CALIBRATED prob if calibrator
    # exists, else raw). Below this, "would_veto" / actual veto.
    DEFAULT_THRESHOLDS = {
        "dbb_trend": 0.50,
    }

    def __init__(
        self,
        repo_root: Path,
        mode: str = "observe",
        model_map: dict[str, str] | None = None,
        thresholds: dict[str, float] | None = None,
        calib_map: dict[str, str] | None = None,
    ) -> None:
        self.repo_root = Path(repo_root)
        self.mode = mode  # "observe" | "hard"
        self.model_map = model_map or self.DEFAULT_MODEL_MAP
        self.thresholds = thresholds or self.DEFAULT_THRESHOLDS
        self.calib_map = calib_map or self.DEFAULT_CALIB_MAP
        self._models: dict[str, Any] = {}
        self._calibs: dict[str, Any] = {}
        self._features = None  # FEATURE_NAMES, lazy-imported

    def _load_calib(self, strategy: str):
        if strategy in self._calibs:
            return self._calibs[strategy]
        rel = self.calib_map.get(strategy)
        if not rel:
            self._calibs[strategy] = None
            return None
        path = self.repo_root / rel
        if not path.exists():
            log.info("[ML_FILTER] no calibrator for %s (using raw prob)", strategy)
            self._calibs[strategy] = None
            return None
        try:
            import joblib
            iso = joblib.load(str(path))
            self._calibs[strategy] = iso
            log.info("[ML_FILTER] loaded calibrator for %s", strategy)
            return iso
        except Exception as exc:
            log.exception("[ML_FILTER] failed to load calibrator for %s: %s", strategy, exc)
            self._calibs[strategy] = None
            return None

    def _load_model(self, strategy: str):
        if strategy in self._models:
            return self._models[strategy]
        path = self.repo_root / self.model_map.get(strategy, "")
        if not path.exists():
            log.warning("[ML_FILTER] model file missing for %s: %s", strategy, path)
            self._models[strategy] = None
            return None
        try:
            import xgboost as xgb
            m = xgb.Booster()
            m.load_model(str(path))
            self._models[strategy] = m
            log.info("[ML_FILTER] loaded model for %s from %s", strategy, path.name)
            return m
        except Exception as exc:
            log.exception("[ML_FILTER] failed to load model for %s: %s", strategy, exc)
            self._models[strategy] = None
            return None

    def _ml_features(self):
        if self._features is None:
            from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES
            self._features = FEATURE_NAMES
        return self._features

    def _build_scan_row(self, symbol: str, candidate, ctx, scorer_result) -> dict:
        """Reconstruct the same `signal` dict shape build_scan_row expects."""
        from scrooge_v3.advisors.ml_observer.features import build_scan_row

        feat_dict: dict[str, Any] = {}
        for name, fr in (ctx.features or {}).items():
            feat_dict[name] = dict(fr.values) if hasattr(fr, "values") else fr

        cls_dict: dict[str, Any] = {}
        for name, cr in (ctx.classifications or {}).items():
            cls_dict[name] = {
                "label": getattr(cr, "label", ""),
                "confidence": getattr(cr, "confidence", 0.0),
                "metadata": getattr(cr, "metadata", {}) or {},
            }

        signal = {
            "symbol": symbol,
            "verdict": "TAKE_PROBE",  # ML gate runs on candidates, not blocks
            "spread": getattr(ctx.snapshot, "spread", 0.0) if ctx.snapshot else 0.0,
            "features": feat_dict,
            "classifications": cls_dict,
            "scorer": {
                "score": float(scorer_result.score),
                "tier": str(scorer_result.tier),
                "blocks": list(scorer_result.blocks or []),
                "breakdown": dict(scorer_result.breakdown or {}),
            },
            "candidate": {
                "symbol": symbol,
                "direction": (candidate.direction.value
                              if hasattr(candidate.direction, "value")
                              else str(candidate.direction)),
                "entry_price": float(candidate.entry_price or 0.0),
                "stop_price": float(candidate.stop_price or 0.0),
                "take_profit": float(candidate.take_profit or 0.0)
                               if candidate.take_profit else 0.0,
                "strategy": candidate.strategy,
                "score": float(candidate.score or 0.0),
            },
            "gates": {},
        }
        return build_scan_row(signal, timestamp=None)

    def evaluate(self, symbol: str, candidate, ctx, scorer_result) -> dict:
        """Returns a dict {applicable, p_win, threshold, would_veto, vetoed,
        reason}. Caller decides whether to drop the candidate based on
        `vetoed` (which respects mode)."""
        strat = (candidate.strategy or "").lower()
        if strat not in self.model_map:
            return {
                "applicable": False,
                "p_win": None,
                "threshold": None,
                "would_veto": False,
                "vetoed": False,
                "reason": f"strategy_{strat}_not_filtered",
            }
        model = self._load_model(strat)
        if model is None:
            return {
                "applicable": True,
                "p_win": None,
                "threshold": None,
                "would_veto": False,
                "vetoed": False,
                "reason": "model_unavailable",
            }
        try:
            row = self._build_scan_row(symbol, candidate, ctx, scorer_result)
            mf = row.get("ml_features", {}) or {}
            feature_names = self._ml_features()
            import numpy as np
            import xgboost as xgb
            vec = np.asarray(
                [[float(mf.get(n, 0.0) or 0.0) for n in feature_names]],
                dtype=np.float32,
            )
            p_raw = float(model.predict(xgb.DMatrix(vec, feature_names=feature_names))[0])
            iso = self._load_calib(strat)
            p = float(iso.predict([p_raw])[0]) if iso is not None else p_raw
        except Exception as exc:
            log.exception("[ML_FILTER] predict failed for %s/%s: %s",
                          symbol, strat, exc)
            return {
                "applicable": True,
                "p_win": None,
                "threshold": None,
                "would_veto": False,
                "vetoed": False,
                "reason": f"predict_error: {exc}",
            }

        thr = float(self.thresholds.get(strat, 0.5))
        would_veto = p < thr
        vetoed = would_veto and self.mode == "hard"
        result = {
            "applicable": True,
            "p_win": p,
            "p_win_raw": p_raw,
            "calibrated": iso is not None,
            "threshold": thr,
            "would_veto": would_veto,
            "vetoed": vetoed,
            "reason": (
                f"p_win={p:.3f} threshold={thr:.2f} "
                f"{'VETO' if would_veto else 'PASS'}"
                f"{' (observe only)' if would_veto and self.mode == 'observe' else ''}"
            ),
        }
        log.info(
            "[ML_FILTER] %s strategy=%s p_win=%.3f thr=%.2f mode=%s -> %s",
            symbol, strat, p, thr, self.mode,
            "VETO" if vetoed else ("WOULD_VETO" if would_veto else "PASS"),
        )
        return result
