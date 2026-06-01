"""pip_eater_gate.py v2 — DUAL-SOURCE pip-EV gate.

Mode C (max) blend: takes the more optimistic signal from either pair-module
baseline OR matrix-refined cell. Per Brock 2026-05-31: each source has cells
the other lacks, missing real harvests is worse than disagreement noise.

Lookups:
    pair_lookup:   (pair, strategy, direction, session, regime) -> mean_pip
    matrix_lookup: (pair, strategy, direction, session)         -> exp_optimized_pips

Tiers (floor=4.0p configurable):
    < 0          -> pip_trick    BLOCK
    0 to 4.0     -> empty_plate  BLOCK
    4.0 to 10.0  -> good_plate   PASS
    10.0 to 20.0 -> tasty        PASS
    >= 20.0      -> optimized_meal PASS
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate

ML_OBSERVER_DIR = Path("/home/ubuntu/mr-scrooge-v3/src/scrooge_v3/advisors/ml_observer")
if str(ML_OBSERVER_DIR) not in sys.path:
    sys.path.insert(0, str(ML_OBSERVER_DIR))
import per_pair_modules as ppm  # type: ignore  # noqa: E402

FACTOR_BUCKETS_PATH = Path("/home/ubuntu/mr-scrooge-v3/data/per_pair_modules/EUR_USD/lib")
if str(FACTOR_BUCKETS_PATH) not in sys.path:
    sys.path.insert(0, str(FACTOR_BUCKETS_PATH))
import factor_buckets as fb  # type: ignore  # noqa: E402

PAIR_LOOKUP_CSV = Path("/home/ubuntu/mr-scrooge-v3/data/pip_meal_lookup.csv")
MATRIX_LOOKUP_CSV = Path("/home/ubuntu/mr-scrooge-v3/data/matrix_meal_lookup.csv")


def _tag(exp_pips: float, floor: float = 4.0) -> str:
    if exp_pips < 0:        return "pip_trick"
    if exp_pips < floor:    return "empty_plate"
    if exp_pips < 10.0:     return "good_plate"
    if exp_pips < 20.0:     return "tasty"
    return "optimized_meal"


def _normalize_direction(d: Any) -> str:
    s = str(d).lower().replace("tradedirection.", "").strip()
    return "long" if s.startswith("l") else "short" if s.startswith("s") else s


class PipEaterGate(BaseGate):
    """Dual-source pip-EV gate. Mode C (max) blend of pair-module + matrix."""

    name = "pip_eater"

    def __init__(self, config: dict[str, Any] | None = None,
                 mode: GateMode = GateMode.HARD) -> None:
        super().__init__(config or {}, mode)
        self.floor_pips = float(self.config.get("floor_pips", 4.0))
        self.min_n = int(self.config.get("min_n", 30))
        self.blend_mode = str(self.config.get("blend_mode", "max")).lower()  # max | min | avg
        self._pair_lookup: dict[tuple, dict] = {}
        self._matrix_lookup: dict[tuple, dict] = {}
        self._missing_logged: set[tuple] = set()
        self._load()

    def _load(self) -> None:
        # Pair-module baseline lookup
        if PAIR_LOOKUP_CSV.exists():
            df = pd.read_csv(PAIR_LOOKUP_CSV)
            df = df[df["n"] >= self.min_n].copy()
            self._pair_lookup = {
                (r["pair"], r["strategy_id"], r["direction_exec"],
                 r["session_bucket"], r["regime_id"]): {
                    "n": int(r["n"]), "mean_pip": float(r["mean_pip"]),
                    "wr": float(r["wr"]), "cohort": str(r["cohort"]),
                }
                for _, r in df.iterrows()
            }
        # Matrix-refined lookup
        if MATRIX_LOOKUP_CSV.exists():
            mf = pd.read_csv(MATRIX_LOOKUP_CSV)
            self._matrix_lookup = {
                (r["pair"], r["strategy"], r["direction"], r["session"]): {
                    "n_optimized": int(r["n_optimized"]),
                    "exp_optimized_pips": float(r["exp_optimized_pips"]),
                    "exp_baseline_pips": float(r["exp_baseline_pips"]),
                    "lift_pips": float(r["lift_pips"]),
                    "factor_count": int(r.get("factor_count", 0)) if pd.notna(r.get("factor_count")) else 0,
                }
                for _, r in mf.iterrows()
            }
        pair_n = len(self._pair_lookup)
        mat_n = len(self._matrix_lookup)
        self._log.info(
            "[PIP_EATER] loaded %d pair cells + %d matrix cells. Floor=%.1fp blend=%s",
            pair_n, mat_n, self.floor_pips, self.blend_mode,
        )

    def _compute_buckets(self, candidate: TradeCandidate, ctx: SymbolContext) -> dict[str, str]:
        feat = {}
        try:
            feat = ctx.features_dict() if hasattr(ctx, "features_dict") else {}
        except Exception:
            pass
        try:
            stop_pips = abs(candidate.entry_price - candidate.stop_price)
            pip_size = 0.01 if any(j in candidate.symbol for j in ("JPY", "MXN")) else 0.0001
            feat["stop_pips"] = stop_pips / pip_size if pip_size else 0.0
        except Exception:
            feat["stop_pips"] = 7.0
        row = {**feat, "pair": candidate.symbol}
        out = {}
        for f in fb.FACTORS:
            try:
                out[f.code] = f.bucket_for(row, {})
            except Exception:
                out[f.code] = f"{f.code}x"
        return out

    def _get_session(self, ctx: SymbolContext) -> str:
        cls = getattr(ctx, "classifications", {}) or {}
        sb = cls.get("session_bucket")
        return getattr(sb, "label", "") if sb else ""

    def _blend(self, pair_ev: Optional[float], matrix_ev: Optional[float]) -> Optional[float]:
        if pair_ev is None and matrix_ev is None:
            return None
        if pair_ev is None:
            return matrix_ev
        if matrix_ev is None:
            return pair_ev
        if self.blend_mode == "max":
            return max(pair_ev, matrix_ev)
        if self.blend_mode == "min":
            return min(pair_ev, matrix_ev)
        return (pair_ev + matrix_ev) / 2.0  # avg

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        try:
            pair = candidate.symbol
            strategy = candidate.strategy or ""
            direction = _normalize_direction(candidate.direction)
            session = self._get_session(ctx)

            mod = ppm.get(pair, strategy)
            if mod is None:
                return GateResult(
                    gate_name=self.name, passed=False, mode=self.mode,
                    reason=f"no per-pair module for {pair}/{strategy}",
                    metrics={"verdict": "no_module"},
                )
            buckets = self._compute_buckets(candidate, ctx)
            regime = mod.assign_regime(buckets)

            pair_key = (pair, strategy, direction, session, regime)
            mat_key = (pair, strategy, direction, session)
            pair_cell = self._pair_lookup.get(pair_key)
            mat_cell = self._matrix_lookup.get(mat_key)

            pair_ev = pair_cell["mean_pip"] if pair_cell else None
            # Brock 2026-06-01: HONEST EV. Was exp_optimized_pips (mean of the
            # cherry-picked winning-signature subset, kept ~8-16%, NOT achievable
            # live since the signature filter is not enforced -> systemic +6-8p
            # over-promise). exp_baseline_pips is the honest full-sample mean.
            matrix_ev = mat_cell["exp_baseline_pips"] if mat_cell else None
            final_ev = self._blend(pair_ev, matrix_ev)

            if final_ev is None:
                if pair_key not in self._missing_logged:
                    self._missing_logged.add(pair_key)
                return GateResult(
                    gate_name=self.name, passed=False, mode=self.mode,
                    reason=f"no cell evidence (pair={pair} strat={strategy} reg={regime})",
                    metrics={"verdict": "no_cell", "regime": regime,
                             "pair": pair, "strategy": strategy,
                             "direction": direction, "session": session},
                )

            tag = _tag(final_ev, floor=self.floor_pips)
            passed = tag in ("good_plate", "tasty", "optimized_meal")
            chose = (
                "max" if (pair_ev is not None and matrix_ev is not None and self.blend_mode == "max")
                else "pair_only" if matrix_ev is None
                else "matrix_only" if pair_ev is None
                else self.blend_mode
            )
            metrics = {
                "verdict": tag,
                "final_exp_pips": round(final_ev, 2),
                "pair_exp_pips": round(pair_ev, 2) if pair_ev is not None else None,
                "matrix_exp_pips": round(matrix_ev, 2) if matrix_ev is not None else None,
                "blend": chose,
                "regime": regime,
                "pair_n": pair_cell["n"] if pair_cell else 0,
                "matrix_n": mat_cell["n_optimized"] if mat_cell else 0,
                "cohort": pair_cell["cohort"] if pair_cell else "n/a",
            }
            # Safe-None formatters for log lines
            pe_s = f"{pair_ev:+.2f}p" if pair_ev is not None else "n/a"
            me_s = f"{matrix_ev:+.2f}p" if matrix_ev is not None else "n/a"
            pn = pair_cell["n"] if pair_cell else 0
            mn = mat_cell["n_optimized"] if mat_cell else 0
            if passed:
                reason = (f"HARVEST {tag} exp_pips={final_ev:+.2f}p "
                          f"(pair={pe_s}[n={pn}] matrix={me_s}[n={mn}] "
                          f"chose={chose} regime={regime})")
            elif tag == "pip_trick":
                reason = (f"PIP TRICK detected exp_pips={final_ev:+.2f}p — danger "
                          f"(pair={pe_s} matrix={me_s} regime={regime})")
            else:
                reason = (f"empty plate exp_pips={final_ev:+.2f}p < floor={self.floor_pips}p "
                          f"(pair={pe_s} matrix={me_s} regime={regime})")
            return GateResult(
                gate_name=self.name, passed=passed, mode=self.mode,
                reason=reason, metrics=metrics,
            )
        except Exception as e:
            self._log.warning("[PIP_EATER] eval error %s/%s: %s",
                              candidate.symbol, candidate.strategy, e)
            return GateResult(
                gate_name=self.name, passed=False, mode=self.mode,
                reason=f"eval error: {type(e).__name__}: {e}",
                metrics={"verdict": "error"},
            )
