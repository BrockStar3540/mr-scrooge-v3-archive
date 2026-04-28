"""Branch-routing advisor — fail-safe scaffolding.

When the trainer ships a router model, this loads it and emits routing
decisions. While models are still being trained, the advisor runs in a
"observe-no-model" mode where it just records which branch a candidate
belongs to, with no probability or veto.

Modes:
  - observe (default): never blocks. Annotates each candidate with the
    router's branch verdict + probabilities (when model loaded).
  - hard: drops candidates from non-selected branches when probabilities
    are confident. Conservative thresholds:
      FREEZE_THRESHOLD = 0.55
      MIN_BRANCH_CONFIDENCE = 0.58
      MIN_BRANCH_MARGIN = 0.08

Hooked into scan_pipeline AFTER strategies emit candidates but BEFORE
the gate pipeline (so routing happens before stateful filtering).

Loads:
  data/ml-observer-offline/models/branch_router_T0.xgb
  (optional) data/ml-observer-offline/models/branch_router_T0.iso
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.advisors.branch_router")

# Map V3 strategy names to canonical router branches.
STRATEGY_BRANCH = {
    "direct": "box",
    "reversal": "box",
    "dbb_trend": "dbb",
    "trend": "dbb",
}

# Router class indices match train_branch_router.py label_map
CLASS_LABELS = ["box", "dbb", "freeze", "unclear"]

# Conservative live policy thresholds (per consultancy spec)
DEFAULT_FREEZE_THRESHOLD = 0.55
DEFAULT_MIN_BRANCH_CONFIDENCE = 0.58
DEFAULT_MIN_BRANCH_MARGIN = 0.08


class BranchRouter:
    """Per-scan branch router. Fail-safe: if the model isn't present,
    falls through with no routing opinion."""

    name = "branch_router"

    def __init__(
        self,
        repo_root: Path,
        mode: str = "observe",
        model_path: str = "data/ml-observer-offline/models/branch_router_T0.xgb",
        thresholds: dict | None = None,
    ) -> None:
        self.repo_root = Path(repo_root)
        self.mode = mode  # observe | hard
        self.model_path = self.repo_root / model_path
        thresholds = thresholds or {}
        self.freeze_threshold = thresholds.get("freeze", DEFAULT_FREEZE_THRESHOLD)
        self.min_confidence = thresholds.get("min_confidence", DEFAULT_MIN_BRANCH_CONFIDENCE)
        self.min_margin = thresholds.get("min_margin", DEFAULT_MIN_BRANCH_MARGIN)
        self._model = None
        self._features = None
        self._tried_load = False

    def _load(self) -> Any:
        if self._tried_load:
            return self._model
        self._tried_load = True
        if not self.model_path.exists():
            log.info("[BRANCH_ROUTER] no model at %s — running advisory-only",
                     self.model_path)
            return None
        try:
            import xgboost as xgb
            m = xgb.Booster()
            m.load_model(str(self.model_path))
            self._model = m
            log.info("[BRANCH_ROUTER] loaded %s", self.model_path)
            return m
        except Exception as exc:
            log.exception("[BRANCH_ROUTER] failed to load model: %s", exc)
            return None

    def _feature_names(self):
        if self._features is None:
            from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES
            self._features = FEATURE_NAMES
        return self._features

    def _build_features(self, ctx, candidates: list) -> list[float]:
        """Reuse the existing features.py infrastructure."""
        from scrooge_v3.advisors.ml_observer.features import build_scan_row
        # Build a stub signal dict similar to ml-observer capture
        feat_dict = {}
        for name, fr in (ctx.features or {}).items():
            feat_dict[name] = dict(fr.values) if hasattr(fr, "values") else fr
        cls_dict = {}
        for name, cr in (ctx.classifications or {}).items():
            cls_dict[name] = {
                "label": getattr(cr, "label", ""),
                "confidence": getattr(cr, "confidence", 0.0),
                "metadata": getattr(cr, "metadata", {}) or {},
            }
        signal = {
            "symbol": ctx.symbol,
            "verdict": "ROUTER_PROBE",
            "spread": getattr(ctx.snapshot, "spread", 0.0),
            "features": feat_dict,
            "classifications": cls_dict,
            "scorer": {},
            "candidate": None,
            "gates": {},
        }
        row = build_scan_row(signal, timestamp=None)
        mf = row.get("ml_features", {}) or {}
        return [float(mf.get(n, 0.0) or 0.0) for n in self._feature_names()]

    def decide(self, ctx, candidates: list) -> dict:
        """Returns dict:
          {
            available_branches: [...],
            router_probs: {box, dbb, freeze, unclear} | None,
            preferred_branch: str | None,
            decision: 'allow_all' | 'route_to_<branch>' | 'freeze',
            decision_reason: str,
            mode: self.mode,
          }
        """
        result = {
            "available_branches": sorted(set(
                STRATEGY_BRANCH.get(getattr(c, "strategy", "") or "", "other")
                for c in candidates
            )),
            "router_probs": None,
            "preferred_branch": None,
            "decision": "allow_all",
            "decision_reason": "no_model",
            "mode": self.mode,
        }
        model = self._load()
        if model is None:
            return result
        try:
            import numpy as np
            import xgboost as xgb
            X = np.asarray([self._build_features(ctx, candidates)], dtype=np.float32)
            probs = model.predict(xgb.DMatrix(X, feature_names=self._feature_names()))[0]
            # probs is shape (n_classes,)
            probs_dict = {CLASS_LABELS[i]: float(probs[i]) for i in range(len(CLASS_LABELS))}
            result["router_probs"] = probs_dict

            p_freeze = probs_dict.get("freeze", 0.0)
            p_box = probs_dict.get("box", 0.0)
            p_dbb = probs_dict.get("dbb", 0.0)

            if p_freeze >= self.freeze_threshold:
                result["preferred_branch"] = "freeze"
                result["decision"] = "freeze"
                result["decision_reason"] = f"p_freeze={p_freeze:.2f} >= {self.freeze_threshold}"
                return result

            best_branch = "box" if p_box >= p_dbb else "dbb"
            best_prob = max(p_box, p_dbb)
            second_prob = min(p_box, p_dbb)
            margin = best_prob - second_prob

            if best_prob < self.min_confidence:
                result["decision"] = "allow_all"
                result["decision_reason"] = (
                    f"max(p_box,p_dbb)={best_prob:.2f} < min_conf={self.min_confidence}"
                )
                return result
            if margin < self.min_margin:
                result["decision"] = "allow_all"
                result["decision_reason"] = (
                    f"margin={margin:.2f} < min_margin={self.min_margin}"
                )
                return result

            result["preferred_branch"] = best_branch
            result["decision"] = f"route_to_{best_branch}"
            result["decision_reason"] = (
                f"p_{best_branch}={best_prob:.2f}, margin={margin:.2f}"
            )
        except Exception as exc:
            log.exception("[BRANCH_ROUTER] decide failed: %s", exc)
            result["decision_reason"] = f"error: {exc}"
        return result

    def filter_candidates(self, candidates: list, decision: dict) -> list:
        """Apply the decision in `hard` mode. Observe mode always returns
        the input candidates unchanged."""
        if self.mode != "hard":
            return candidates
        d = decision.get("decision", "allow_all")
        if d == "freeze":
            log.info("[BRANCH_ROUTER] FREEZE — dropping %d candidates", len(candidates))
            return []
        if d.startswith("route_to_"):
            target = d[len("route_to_"):]
            kept = [c for c in candidates
                    if STRATEGY_BRANCH.get(getattr(c, "strategy", "") or "", "other") == target]
            if len(kept) < len(candidates):
                log.info("[BRANCH_ROUTER] routed to %s — kept %d/%d candidates",
                         target, len(kept), len(candidates))
            return kept
        return candidates
