"""V4HybridScorer -- the rebuilt ranker that will replace V3HybridScorer.

Per Brock 2026-05-18 spec:
  - routing/island layer decides eligibility
  - this scorer ranks among eligible options + optionally feeds size/confidence
  - does NOT veto

Heads:
  A. should_trade  -- P(is_win=True) binary classifier
  B. expected_r    -- realized R-multiple regressor

Currently loaded model is v0 (2026-05-18): AUC 0.497 on holdout
(below promotion bar of 0.60). Class is staged for shadow-mode wiring
once a passing model is trained. Mode = `shadow` by default; never
emits a BLOCKED or REJECT result.
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

try:
    import xgboost as xgb
    HAS_XGB = True
except ImportError:
    HAS_XGB = False

log = logging.getLogger("scrooge_v3.strategies.v4_scorer")


@dataclass
class V4ScorerResult:
    """Output of V4HybridScorer.score().

    p_win        Head A probability (0-1)
    expected_r   Head B expected R-multiple
    rank_score   composite ranking signal: p_win * max(0.1, expected_r)
    mode         "shadow" | "live"
    tier         informational only -- mirrors v3's tier vocab for compat
                 ("A"/"B"/"REJECT") with thresholds at p_win.
    """
    p_win: float = 0.0
    expected_r: float = 0.0
    rank_score: float = 0.0
    mode: str = "shadow"
    tier: str = "B"
    blocks: list = field(default_factory=list)
    breakdown: dict = field(default_factory=dict)
    pairs_total: int = 0
    base_score: int = 0
    score: int = 0  # kept for v3 compat; this is rank_score * 100


class V4HybridScorer:
    """v4 scorer. Loads two XGBoost models + a features manifest.

    Usage:
        v4 = V4HybridScorer(model_dir="research/.../v4_scorer", mode="shadow")
        result = v4.score(ctx, candidate)

    In shadow mode (default), logs predictions but does not affect
    pipeline decisions. The wire-in to scan_pipeline is gated by config.
    """

    name = "v4_scorer"

    def __init__(self, model_dir: str | Path, mode: str = "shadow"):
        self.mode = mode
        self.model_dir = Path(model_dir)
        self._loaded = False
        self._features: list[str] = []
        self._categorical_maps: dict[str, dict[str, int]] = {}
        self._numeric_cols: list[str] = []
        self._model_a: Any = None
        self._model_b: Any = None
        self._metrics: dict = {}
        self._load()

    def _load(self):
        if not HAS_XGB:
            log.warning("[V4_SCORER] xgboost not installed -- scorer disabled")
            return
        try:
            meta_path = self.model_dir / "v4_scorer_features.json"
            if not meta_path.exists():
                log.warning("[V4_SCORER] features manifest missing at %s", meta_path)
                return
            meta = json.loads(meta_path.read_text())
            self._features = meta["feature_cols"]
            self._categorical_maps = meta["categorical_maps"]
            self._numeric_cols = meta["numeric_cols"]
            self._model_a = xgb.XGBClassifier()
            self._model_a.load_model(str(self.model_dir / "v4_scorer_model_A.json"))
            self._model_b = xgb.XGBRegressor()
            self._model_b.load_model(str(self.model_dir / "v4_scorer_model_B.json"))
            mpath = self.model_dir / "v4_scorer_metrics.json"
            if mpath.exists():
                self._metrics = json.loads(mpath.read_text())
            self._loaded = True
            auc = (self._metrics.get("head_a") or {}).get("auc_test", float("nan"))
            log.info("[V4_SCORER] loaded mode=%s features=%d AUC(A)=%.3f",
                     self.mode, len(self._features), auc)
        except Exception as exc:
            log.exception("[V4_SCORER] load failed: %s", exc)
            self._loaded = False

    def _features_from_ctx(self, ctx, candidate) -> dict:
        """Pull v4 feature row from (ctx, candidate)."""
        out: dict = {}
        # regime / pair / direction / session
        regime53 = self._classify(ctx, "technical_regime_53")
        out["technical_regime_53"] = regime53 or "unknown"
        out["parent_regime"] = (regime53 or "")[:3]
        out["pair"] = ctx.symbol
        out["direction"] = getattr(candidate.direction, "value", str(candidate.direction))
        out["session_bucket"] = self._classify(ctx, "session_bucket") or "unknown"
        ts = getattr(ctx.snapshot, "timestamp", None)
        out["hour_utc"] = float(ts.hour) if ts is not None else 0.0
        out["day_of_week"] = float(ts.weekday()) if ts is not None else 0.0
        # factors -- pull from technical_regime_53 feature (where they live)
        feat = ctx.features.get("technical_regime_53")
        vals = (getattr(feat, "values", {}) or {}) if feat else {}
        for k in ("ATR_ratio","BB_compress","ADX14","RSI14","close_pos"):
            v = vals.get(k)
            out[k] = float(v) if isinstance(v, (int, float)) else 0.0
        # bb_position / z_score live on bollinger
        bb = ctx.features.get("bollinger")
        bb_vals = (getattr(bb, "values", {}) or {}) if bb else {}
        out["bb_position"] = float(bb_vals.get("bb_position") or 0.0)
        out["z_score"] = float(bb_vals.get("z_score") or 0.0)
        # volume_ratio
        vol = ctx.features.get("volume")
        vol_vals = (getattr(vol, "values", {}) or {}) if vol else {}
        out["volume_ratio"] = float(vol_vals.get("volume_ratio") or 0.0)
        # ema dist
        ema = ctx.features.get("ema")
        ema_vals = (getattr(ema, "values", {}) or {}) if ema else {}
        out["ema20_dist_pct"] = float(ema_vals.get("ema20_dist_pct") or 0.0)
        out["ema50_dist_pct"] = float(ema_vals.get("ema50_dist_pct") or 0.0)
        out["sma20_dist_signed_bps"] = float(ema_vals.get("sma20_dist_signed_bps") or 0.0)
        # cell features (carried via entry_filter stamps)
        meta = candidate.metadata or {}
        cell_tier = meta.get("routing_cell_tier") or "none"
        out["cell_tier"] = cell_tier
        out["cell_tier_rank"] = float({"Probationary":0,"Seed":1,"Standard":2,
                                       "Seed-Pro":3,"Pro":4,"Elite":5}.get(cell_tier, 0))
        out["cell_n_unique"] = float(meta.get("routing_cell_n_unique") or 0)
        out["cell_wr"] = float(meta.get("routing_cell_wr") or 0)
        out["cell_wilson_lb"] = float(meta.get("routing_cell_wilson_lb") or 0)
        out["cell_source_bank"] = str(meta.get("routing_cell_source_bank") or "unknown")
        return out

    def _classify(self, ctx, key: str):
        c = ctx.classifications.get(key)
        if c is not None:
            return c.label
        feat = ctx.features.get(key)
        if feat is None:
            return None
        vals = getattr(feat, "values", {}) or {}
        v = vals.get(key)
        return str(v) if v is not None else None

    def _encode_row(self, row: dict) -> np.ndarray:
        x = []
        for c in self._features:
            if c in self._categorical_maps:
                v = str(row.get(c, ""))
                x.append(self._categorical_maps[c].get(v, -1))
            else:
                v = row.get(c, 0.0)
                try: x.append(float(v))
                except (TypeError, ValueError): x.append(0.0)
        return np.asarray([x], dtype=np.float32)

    def score(self, ctx, candidate) -> V4ScorerResult:
        if not self._loaded:
            return V4ScorerResult(p_win=0.0, expected_r=0.0, rank_score=0.0,
                                  mode=self.mode, tier="B")
        try:
            row = self._features_from_ctx(ctx, candidate)
            X = self._encode_row(row)
            p_win = float(self._model_a.predict_proba(X)[0, 1])
            expected_r = float(self._model_b.predict(X)[0])
            rank_score = p_win * max(0.1, expected_r)
            tier = "A" if p_win >= 0.55 else "B" if p_win >= 0.45 else "REJECT"
            return V4ScorerResult(
                p_win=p_win, expected_r=expected_r,
                rank_score=rank_score, mode=self.mode, tier=tier,
                score=int(rank_score * 100),
                base_score=int(p_win * 100),
                breakdown={"p_win": p_win, "expected_r": expected_r,
                           "cell_tier": row.get("cell_tier"),
                           "cell_wilson_lb": row.get("cell_wilson_lb")},
            )
        except Exception as exc:
            log.exception("[V4_SCORER] score failed: %s", exc)
            return V4ScorerResult(p_win=0.0, expected_r=0.0, rank_score=0.0,
                                  mode=self.mode, tier="B")
