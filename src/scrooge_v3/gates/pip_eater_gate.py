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
        # Brock 2026-06-02: momentum filter. Require align_score (# of H20/H60/
        # T1/T4 aligned with candidate direction) >= align_min. Lab: aligned>=3
        # trades net +0.64p/64% WR vs counter<=1 at -0.30p/59%. 0 = disabled.
        self.align_min = int(self.config.get("align_min", 0))
        self.blend_mode = str(self.config.get("blend_mode", "max")).lower()  # max | min | avg
        self._pair_lookup: dict[tuple, dict] = {}
        self._coarse_pair_lookup: dict[tuple, dict] = {}  # regime-agnostic fallback
        self._matrix_lookup: dict[tuple, dict] = {}
        self._known_strategies: set[str] = set()  # any strategy present in lab data
        self._missing_logged: set[tuple] = set()
        self._load()

    def _load(self) -> None:
        # Pair-module baseline lookup
        if PAIR_LOOKUP_CSV.exists():
            df = pd.read_csv(PAIR_LOOKUP_CSV)
            full = df.copy()  # unfiltered, for the regime-agnostic aggregate
            df = df[df["n"] >= self.min_n].copy()
            self._pair_lookup = {
                (r["pair"], r["strategy_id"], r["direction_exec"],
                 r["session_bucket"], r["regime_id"]): {
                    "n": int(r["n"]), "mean_pip": float(r["mean_pip"]),
                    "wr": float(r["wr"]), "cohort": str(r["cohort"]),
                }
                for _, r in df.iterrows()
            }
            # Regime-agnostic fallback (Brock 2026-06-01): when neither the
            # regime-specific pair cell NOR the matrix cell exists, collapse the
            # pair-module across ALL regimes (sample-weighted) so we trade on the
            # broader average instead of rejecting. Built from the UNFILTERED rows
            # (thin regime cells combine) but kept only if the combined n>=min_n.
            try:
                full["_wp"] = full["n"] * full["mean_pip"]
                grp = full.groupby(
                    ["pair", "strategy_id", "direction_exec", "session_bucket"],
                    as_index=False,
                ).agg(n=("n", "sum"), _wp=("_wp", "sum"),
                      cohort=("cohort", "first"))
                grp = grp[grp["n"] >= self.min_n]
                self._coarse_pair_lookup = {
                    (r["pair"], r["strategy_id"], r["direction_exec"],
                     r["session_bucket"]): {
                        "n": int(r["n"]),
                        "mean_pip": float(r["_wp"] / r["n"]) if r["n"] else 0.0,
                        "cohort": str(r["cohort"]),
                    }
                    for _, r in grp.iterrows()
                }
                self._known_strategies.update(full["strategy_id"].astype(str).unique())
            except Exception as e:
                self._log.warning("[PIP_EATER] coarse fallback build failed: %s", e)
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
            self._known_strategies.update(mf["strategy"].astype(str).unique())
        pair_n = len(self._pair_lookup)
        mat_n = len(self._matrix_lookup)
        self._log.info(
            "[PIP_EATER] loaded %d pair cells + %d matrix cells + %d coarse(regime-agnostic) cells. Floor=%.1fp blend=%s",
            pair_n, mat_n, len(self._coarse_pair_lookup), self.floor_pips, self.blend_mode,
        )

    def _compute_buckets(self, candidate: TradeCandidate, ctx: SymbolContext) -> dict[str, str]:
        # Brock 2026-06-02 FIX: the old `ctx.features_dict()` never existed
        # (hasattr False -> feat={}), so ALL 14 factor buckets came back "x" and
        # regime/alignment ran on empty. The real features live in
        # ctx.features[<calc>].values (matrix_features/atr/bollinger/ema/rsi).
        # Merge them so the buckets compute on real data.
        feat = {}
        try:
            for _fr in (getattr(ctx, "features", {}) or {}).values():
                _v = getattr(_fr, "values", None)
                if isinstance(_v, dict):
                    feat.update(_v)
        except Exception:
            pass
        # direction is required by the alignment-aware buckets (H20/H60/T1/T4)
        try:
            feat["direction"] = candidate.direction.value
            feat["direction_exec"] = candidate.direction.value
        except Exception:
            pass
        pip_size = 0.01 if any(j in candidate.symbol for j in ("JPY", "MXN")) else 0.0001
        try:
            stop_pips = abs(candidate.entry_price - candidate.stop_price)
            feat["stop_pips"] = stop_pips / pip_size if pip_size else 0.0
        except Exception:
            feat["stop_pips"] = 7.0
        # SPR factor needs spread in pips; it lives on the snapshot, not a feature calc.
        try:
            if "spread_pips" not in feat:
                _sp = getattr(getattr(ctx, "snapshot", None), "spread", 0.0) or 0.0
                if _sp and pip_size:
                    feat["spread_pips"] = _sp / pip_size
        except Exception:
            pass
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

            # Brock 2026-06-02: MOMENTUM FILTER. Only trade WITH the trend.
            # align_score = # of {H20,H60,T1,T4} aligned with candidate dir.
            # Applies to EVERY candidate (incl. uncovered_bypass strategies) —
            # the lab showed strategy identity barely matters; trade-level
            # alignment is the whole edge (aligned>=3 +0.64p vs counter -0.30p).
            if self.align_min > 0:
                align_score = (
                    (1 if buckets.get("H20") in ("H20a", "H20b") else 0)
                    + (1 if buckets.get("H60") in ("H60a", "H60b") else 0)
                    + (1 if buckets.get("T1") == "T1a" else 0)
                    + (1 if buckets.get("T4") == "T4a" else 0)
                )
                if align_score < self.align_min:
                    return GateResult(
                        gate_name=self.name, passed=False, mode=self.mode,
                        reason=(f"MOMENTUM filter: align_score={align_score} < {self.align_min} "
                                f"(H20={buckets.get('H20')} H60={buckets.get('H60')} "
                                f"T1={buckets.get('T1')} T4={buckets.get('T4')} dir={direction})"),
                        metrics={"verdict": "low_align", "align_score": align_score,
                                 "align_min": self.align_min, "pair": pair,
                                 "strategy": strategy, "direction": direction},
                    )

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

            # Brock 2026-06-01: regime-agnostic fallback. If neither the
            # regime-specific pair cell nor the matrix cell has evidence, fall
            # back to the pair-module collapsed across regimes. Trades taken on
            # this fallback are STAMPED (metadata + reason + verdict) so their
            # realized PnL can be compared against full-evidence trades.
            nocell_fallback = False
            coarse_cell = None
            if final_ev is None:
                coarse_cell = self._coarse_pair_lookup.get(mat_key)
                if coarse_cell is not None:
                    final_ev = coarse_cell["mean_pip"]
                    nocell_fallback = True

            if final_ev is None:
                # Brock 2026-06-01: UNCOVERED-STRATEGY BYPASS. If the strategy is
                # entirely absent from the lab (never backtested -> no EV cell at
                # any granularity), pass pip_eater and rely on the HTF-hard
                # alignment gate + other gates for quality. STAMPED as unvalidated
                # so realized PnL is separable at close. NOTE: a *known* strategy
                # that merely lacks this specific cell still rejects below — a
                # missing slice for a tested strategy is meaningful.
                if strategy and strategy not in self._known_strategies:
                    try:
                        if candidate.metadata is None:
                            candidate.metadata = {}
                        candidate.metadata["pip_evidence"] = "uncovered_bypass"
                        candidate.metadata["pip_nocell"] = True
                    except Exception:
                        pass
                    return GateResult(
                        gate_name=self.name, passed=True, mode=self.mode,
                        reason=(f"BYPASS uncovered strategy={strategy} — no lab evidence; "
                                f"passing on HTF-alignment/other gates (pair={pair} reg={regime})"),
                        metrics={"verdict": "uncovered_bypass", "evidence": "uncovered_bypass",
                                 "nocell_fallback": False, "uncovered": True, "regime": regime,
                                 "pair": pair, "strategy": strategy,
                                 "direction": direction, "session": session},
                    )
                if pair_key not in self._missing_logged:
                    self._missing_logged.add(pair_key)
                return GateResult(
                    gate_name=self.name, passed=False, mode=self.mode,
                    reason=f"no cell evidence (pair={pair} strat={strategy} reg={regime})",
                    metrics={"verdict": "no_cell", "regime": regime,
                             "pair": pair, "strategy": strategy,
                             "direction": direction, "session": session},
                )

            # Brock 2026-06-01: NET-of-spread EV. Lab pnl_pips is GROSS; live we
            # pay ~1x round-trip spread (1.8p avg, up to 2.6p on crosses). Gate on
            # the cost-adjusted number so a +4p gross edge on a wide-spread cross
            # does not pass as net-marginal/negative.
            _sp = getattr(getattr(ctx, "snapshot", None), "spread", 0.0) or 0.0
            _pip = 0.01 if any(j in pair for j in ("JPY", "MXN")) else 0.0001
            spread_pips = (_sp / _pip) if _pip else 0.0
            net_ev = final_ev - spread_pips
            tag = _tag(net_ev, floor=self.floor_pips)
            passed = tag in ("good_plate", "tasty", "optimized_meal")
            chose = (
                "regime_agnostic_fallback" if nocell_fallback
                else "max" if (pair_ev is not None and matrix_ev is not None and self.blend_mode == "max")
                else "pair_only" if matrix_ev is None
                else "matrix_only" if pair_ev is None
                else self.blend_mode
            )
            # STAMP (Brock 2026-06-01): mark the trade's evidence source so the
            # regime-agnostic fallback ("No Cell") trades are identifiable at
            # close. Rides into the position via candidate.metadata.
            evidence = "regime_agnostic_fallback" if nocell_fallback else chose
            try:
                if candidate.metadata is None:
                    candidate.metadata = {}
                candidate.metadata["pip_evidence"] = evidence
                candidate.metadata["pip_net_ev"] = round(net_ev, 2)
                candidate.metadata["pip_nocell"] = bool(nocell_fallback)
            except Exception:
                pass
            metrics = {
                "verdict": tag,
                "final_exp_pips": round(final_ev, 2),
                "net_exp_pips": round(net_ev, 2),
                "spread_pips": round(spread_pips, 2),
                "pair_exp_pips": round(pair_ev, 2) if pair_ev is not None else None,
                "matrix_exp_pips": round(matrix_ev, 2) if matrix_ev is not None else None,
                "blend": chose,
                "evidence": evidence,
                "nocell_fallback": bool(nocell_fallback),
                "regime": regime,
                "pair_n": pair_cell["n"] if pair_cell else 0,
                "matrix_n": mat_cell["n_optimized"] if mat_cell else 0,
                "coarse_n": coarse_cell["n"] if coarse_cell else 0,
                "cohort": pair_cell["cohort"] if pair_cell else (coarse_cell["cohort"] if coarse_cell else "n/a"),
            }
            # Safe-None formatters for log lines
            pe_s = f"{pair_ev:+.2f}p" if pair_ev is not None else "n/a"
            me_s = f"{matrix_ev:+.2f}p" if matrix_ev is not None else "n/a"
            pn = pair_cell["n"] if pair_cell else 0
            mn = mat_cell["n_optimized"] if mat_cell else 0
            if passed and nocell_fallback:
                reason = (f"HARVEST {tag} [NOCELL-FALLBACK] net={net_ev:+.2f}p (gross={final_ev:+.2f}p-spr={spread_pips:.1f}p) "
                          f"(regime-agnostic coarse={final_ev:+.2f}p[n={coarse_cell['n']}] "
                          f"regime={regime} — no pair/matrix cell)")
            elif passed:
                reason = (f"HARVEST {tag} net={net_ev:+.2f}p (gross={final_ev:+.2f}p-spr={spread_pips:.1f}p) "
                          f"(pair={pe_s}[n={pn}] matrix={me_s}[n={mn}] "
                          f"chose={chose} regime={regime})")
            elif tag == "pip_trick":
                reason = (f"PIP TRICK detected exp_pips={final_ev:+.2f}p — danger "
                          f"(pair={pe_s} matrix={me_s} regime={regime})")
            else:
                reason = (f"empty plate net={net_ev:+.2f}p (gross={final_ev:+.2f}p-spr={spread_pips:.1f}p) < floor={self.floor_pips}p "
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
