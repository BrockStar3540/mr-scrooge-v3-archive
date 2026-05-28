"""MatrixRouterGate v3.5 — winner-allow / loser-veto via shared bucket tuples.

Brock 2026-05-28: "14 factors in a serial number. We find which ones determine
losers and block them, and which ones the winners share and allow them."

Architecture (replaces the per-cell formula optimizer of v3):
  - Source: winner_loser_formulas.csv (lab-mined, 21,402 rows)
    Each row = (combo, factor, bucket) -> classification.
    combo = "pair|strategy|direction|session"
    classification in {WINNER, NEUTRAL, LOSER, INSUFFICIENT}
      WINNER: WR >= 0.65 with n >= 15 in this combo for this bucket
      LOSER:  WR <= 0.45 with n >= 15
  - At scan: compute candidate's 14-factor bucket signature.
  - For each (factor, bucket) tuple, look up its classification in this combo.
  - Decision:
      ANY loser hit                       -> BLOCK (loser veto)
      >=1 winner hit AND zero loser hits  -> PASS  (positive signal)
      else (all NEUTRAL/INSUFFICIENT)     -> BLOCK (no_signal)

Every PASS/BLOCK logs the specific (factor, bucket, wr, n) tuples that drove
the decision so the audit trail is one grep away in journalctl.

Falls back to v3 cell-formula matrix if winner_loser_formulas.csv is missing;
falls back further to legacy F-code matrix if neither v3 file is available.

Universal HTF20 pre-filter retained: H20 in {H20d, H20e} blocks regardless of
combo-specific lookup. Empirically the strongest universal veto in the lab.
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Optional

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate

LAB_DIR = Path("/home/ubuntu/mr-scrooge-v3/data/lab_matrix")
WLF_CSV = LAB_DIR / "winner_loser_formulas.csv"
V3_CSV = LAB_DIR / "optimized_matrix_v3.csv"
LEGACY_CSV = LAB_DIR / "optimized_matrix_by_session.csv"

if str(LAB_DIR) not in sys.path:
    sys.path.insert(0, str(LAB_DIR))

log = logging.getLogger("scrooge_v3.gate.matrix_router")

HTF20_MISMATCH_BUCKETS = {"H20d", "H20e"}


class MatrixRouterGate(BaseGate):
    """Winner-allow / loser-veto router on shared bucket tuples (v3.5)."""

    name = "matrix_router"

    def __init__(self, config: dict | None = None, mode: GateMode = GateMode.HARD):
        super().__init__(config or {}, mode)
        self._stop_pips = float(self.config.get("stop_pips", 7.0))
        # Tunables for the winner_loser engine.
        # min_winner_hits: how many WINNER (factor,bucket) tuples must match
        # before we allow PASS. 1 is permissive; raise to 2+ to require
        # multi-factor agreement.
        self._min_winner_hits = int(self.config.get("min_winner_hits", 1))
        # Allow PASS even when zero winners hit, if no losers either.
        self._allow_no_signal = bool(self.config.get("allow_no_signal", False))

        self._FACTORS = None
        self._factor_predicate = None
        self._wlf_index: dict = {}          # combo -> {factor -> {bucket -> (cls, wr, n)}}
        self._opt: Optional[pd.DataFrame] = None
        self._cell_index: dict = {}         # fallback v3 cell index
        self._schema = "none"
        self._loaded = False
        self._load_source()

    # ------------------------------------------------------------------
    # Boot-time source load
    # ------------------------------------------------------------------
    def _load_source(self) -> None:
        if WLF_CSV.exists():
            try:
                self._load_wlf()
                return
            except Exception:
                log.exception("[MATRIX_ROUTER] winner_loser load failed, trying v3 cell matrix")
        if V3_CSV.exists():
            try:
                self._load_v3_cells()
                return
            except Exception:
                log.exception("[MATRIX_ROUTER] v3 cells load failed, trying legacy")
        if LEGACY_CSV.exists():
            try:
                self._load_legacy()
                return
            except Exception:
                log.exception("[MATRIX_ROUTER] legacy load failed — gate will fail-open")
        self._loaded = False

    def _load_wlf(self) -> None:
        from factor_buckets import FACTORS  # type: ignore  # noqa
        self._FACTORS = FACTORS
        df = pd.read_csv(WLF_CSV)
        winners = losers = neutrals = insufficient = 0
        for r in df.itertuples(index=False):
            cls = str(r.classification)
            if cls == "WINNER":
                winners += 1
            elif cls == "LOSER":
                losers += 1
            elif cls == "NEUTRAL":
                neutrals += 1
            else:
                insufficient += 1
            combo = str(r.combo)
            factor = str(r.factor)
            bucket = str(r.bucket)
            try:
                wr = float(r.wr)
                n = int(r.n)
            except Exception:
                wr, n = 0.0, 0
            self._wlf_index.setdefault(combo, {}).setdefault(factor, {})[bucket] = (cls, wr, n)
        self._loaded = True
        self._schema = "wlf"
        log.info(
            "[MATRIX_ROUTER] loaded winner_loser_formulas: %d rows, %d unique combos, "
            "%d WINNER / %d LOSER / %d NEUTRAL / %d INSUFFICIENT, %d factors, "
            "min_winner_hits=%d allow_no_signal=%s",
            len(df), len(self._wlf_index), winners, losers, neutrals, insufficient,
            len(FACTORS), self._min_winner_hits, self._allow_no_signal,
        )

    def _load_v3_cells(self) -> None:
        from factor_buckets import FACTORS  # type: ignore  # noqa
        self._FACTORS = FACTORS
        opt = pd.read_csv(V3_CSV)
        for _, r in opt.iterrows():
            try:
                formula = json.loads(r["formula_json"]) if isinstance(r["formula_json"], str) else {}
            except Exception:
                formula = {}
            d = r.to_dict()
            d["_formula"] = {k: set(v) for k, v in formula.items()}
            key = (str(d["pair"]), str(d["strategy"]),
                   str(d["direction"]), str(d.get("session", "")))
            self._cell_index.setdefault(key, []).append(d)
        self._opt = opt
        self._loaded = True
        self._schema = "v3_cells"
        log.warning(
            "[MATRIX_ROUTER] winner_loser CSV missing, fell back to v3 cell matrix: %d cells",
            len(opt),
        )

    def _load_legacy(self) -> None:
        from factor_catalog import FACTORS, factor_predicate  # type: ignore  # noqa
        self._FACTORS = FACTORS
        self._factor_predicate = factor_predicate
        opt = pd.read_csv(LEGACY_CSV)
        for _, r in opt.iterrows():
            key = (str(r["pair"]), str(r["strategy"]),
                   str(r["direction"]), str(r.get("session", "")))
            self._cell_index.setdefault(key, []).append(r.to_dict())
        self._opt = opt
        self._loaded = True
        self._schema = "legacy"
        log.warning("[MATRIX_ROUTER] both v3 files missing, falling back to legacy F-codes")

    # ------------------------------------------------------------------
    # Per-candidate context row + bucket computation
    # ------------------------------------------------------------------
    @staticmethod
    def _row_from_ctx(candidate: TradeCandidate, ctx: SymbolContext) -> dict:
        feat = ctx.features or {}
        cls_ = ctx.classifications or {}

        def fv(name):
            f = feat.get(name)
            if f is None:
                return {}
            return getattr(f, "values", {}) if hasattr(f, "values") else (f if isinstance(f, dict) else {})

        mx = fv("matrix_features")
        bb = fv("bollinger"); atr = fv("atr"); rsi = fv("rsi")
        st = fv("structure"); rng = fv("range")
        bb_state = getattr(cls_.get("bb_state"), "label", "") if cls_.get("bb_state") else ""
        session = getattr(cls_.get("session_bucket"), "label", "") if cls_.get("session_bucket") else ""

        sym = candidate.symbol or ""
        spread_raw = float(getattr(ctx.snapshot, "spread", 0.0) or 0.0)
        pip = 0.01 if any(j in sym for j in ("JPY", "MXN")) else 0.0001
        spread_pips = spread_raw / pip if pip > 0 else 0.0
        direction = (getattr(candidate.direction, "value", str(candidate.direction)) or "")

        bb_width_live = None
        ua, la = bb.get("upper_a"), bb.get("lower_a")
        if ua is not None and la is not None and pip > 0:
            try:
                bb_width_live = (float(ua) - float(la)) / pip
            except Exception:
                bb_width_live = None

        return {
            "pair": sym,
            "strategy_id": candidate.strategy or "",
            "direction_exec": direction,
            "session_bucket": session,
            "spread_pips": spread_pips,
            "rsi14": mx.get("rsi14") or rsi.get("rsi") or rsi.get("rsi14") or rsi.get("value"),
            "rsi": rsi.get("rsi"),
            "zscore": mx.get("zscore") or bb.get("z_score"),
            "z_score": bb.get("z_score"),
            "bb_position": bb.get("bb_position") or bb.get("position"),
            "bb_width_pips": mx.get("bb_width_pips") or bb_width_live,
            "atr_5m_pips": mx.get("atr_5m_pips"),
            "atr_1h_pips": mx.get("atr_1h_pips"),
            "realized_vol": atr.get("realized_vol"),
            "adr_consumed": atr.get("adr_consumed"),
            "ema20_slope": mx.get("ema20_slope"),
            "ema50_slope": mx.get("ema50_slope"),
            "htf_pct_20": mx.get("htf_pct_20"),
            "htf_pct_60": mx.get("htf_pct_60"),
            "htf_bias_20": mx.get("htf_bias_20"),
            "htf_bias_60": mx.get("htf_bias_60"),
            "trend_1h": mx.get("trend_1h"),
            "trend_4h": mx.get("trend_4h"),
            "bb_state": bb_state,
            "range_percentile": rng.get("range_percentile"),
            "pullback_depth_pct": st.get("pullback_depth_pct"),
            "dist_to_swing_high_pips": st.get("dist_to_swing_high_pips"),
            "dist_to_swing_low_pips": st.get("dist_to_swing_low_pips"),
            "distance_to_structure_pips": st.get("distance_to_structure_pips"),
            "_matrix_features_degraded": mx.get("_degraded", []),
        }

    def _compute_buckets(self, row: dict) -> dict[str, str]:
        sym = row.get("pair", "") or ""
        pip = 0.01 if any(j in sym for j in ("JPY", "MXN")) else 0.0001
        ctx = {
            "stop_pips": self._stop_pips,
            "pip_size": pip,
            "rv_baseline": 0.002,
            "direction": row.get("direction_exec"),
        }
        out: dict[str, str] = {}
        for f in self._FACTORS:
            try:
                out[f.code] = f.bucket_for(row, ctx)
            except Exception:
                out[f.code] = f"{f.code}x"
        return out

    def _candidate_family(self, candidate: TradeCandidate) -> str:
        md_fam = (candidate.metadata or {}).get("strategy_family", "")
        if md_fam:
            return str(md_fam)
        strat = (candidate.strategy or "").lower()
        if strat.startswith("dbb"): return "canonical_lien_dbb"
        if strat.startswith("mtb"): return "box_master_theory"
        if strat.startswith("drv"): return "canonical_darvas"
        if strat.startswith("rg"): return "reversal"
        if strat.startswith("itp_"): return "trend_pullback"
        if strat.startswith("cma_"): return "chaikin_macd_atr"
        if strat.startswith("cmr_"): return "compression_reversion"
        if strat.startswith("ce_"): return "compression_expansion"
        if strat.startswith("sb_"): return "session_breakout"
        if strat.startswith("ifvg"): return "ifvg"
        return candidate.strategy or ""

    # ------------------------------------------------------------------
    # Top-level evaluator
    # ------------------------------------------------------------------
    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        if not self._loaded:
            return GateResult(
                gate_name=self.name, passed=True,
                reason="matrix_unavailable_fail_open",
                metrics={"schema": self._schema},
            )

        row = self._row_from_ctx(candidate, ctx)
        family = self._candidate_family(candidate)
        session = row.get("session_bucket", "") or ""
        direction = row["direction_exec"]

        # Universal HTF20 mismatch pre-filter — runs regardless of schema.
        buckets = self._compute_buckets(row)
        sig = "|".join(f"{f.code}={buckets.get(f.code, '?')}" for f in self._FACTORS)
        degraded = row.get("_matrix_features_degraded") or []
        log.info(
            "[MATRIX_ROUTER] candidate %s strat=%s fam=%s dir=%s sess=%s sig=[%s]%s",
            row["pair"], candidate.strategy or "?", family, direction, session, sig,
            f" degraded=[{','.join(degraded)}]" if degraded else "",
        )

        h20 = buckets.get("H20", "")
        if h20 in HTF20_MISMATCH_BUCKETS:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"htf20_mismatch:h20_bucket={h20},dir={direction}",
                metrics={"blocked_by": "htf20_universal_pre_filter",
                         "h20_bucket": h20, "schema": self._schema},
            )

        combo = f"{row['pair']}|{family}|{direction}|{session}"
        candidate.metadata["matrix_combo"] = combo
        candidate.metadata["matrix_candidate_buckets"] = buckets

        if self._schema == "wlf":
            return self._evaluate_wlf(candidate, row, family, session, direction, combo, buckets)
        if self._schema == "v3_cells":
            return self._evaluate_v3_cells(candidate, row, family, session, direction, buckets)
        return self._evaluate_legacy(candidate, row, family, session, direction)

    # ------------------------------------------------------------------
    # WLF — winner_loser_formulas-driven decision (primary path)
    # ------------------------------------------------------------------
    def _evaluate_wlf(self, candidate, row, family, session, direction, combo, buckets) -> GateResult:
        rules = self._wlf_index.get(combo)
        if not rules:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_combo_in_matrix:{combo}",
                metrics={"schema": "wlf", "combo": combo},
            )

        winners_hit: list[tuple] = []   # (factor, bucket, wr, n)
        losers_hit: list[tuple] = []
        for f in self._FACTORS:
            bucket = buckets.get(f.code, "")
            tier = rules.get(f.code, {}).get(bucket)
            if not tier:
                continue
            cls, wr, n = tier
            if cls == "WINNER":
                winners_hit.append((f.code, bucket, wr, n))
            elif cls == "LOSER":
                losers_hit.append((f.code, bucket, wr, n))

        candidate.metadata["matrix_winners_hit"] = [
            {"factor": f, "bucket": b, "wr": w, "n": n} for f, b, w, n in winners_hit
        ]
        candidate.metadata["matrix_losers_hit"] = [
            {"factor": f, "bucket": b, "wr": w, "n": n} for f, b, w, n in losers_hit
        ]

        # Loser veto — any LOSER tuple kills the trade
        if losers_hit:
            detail = ",".join(
                f"{f}={b}(wr={w:.0%},n={n})" for f, b, w, n in losers_hit
            )
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"loser_veto:{combo}:{detail}",
                metrics={
                    "schema": "wlf",
                    "blocked_by": "loser_veto",
                    "combo": combo,
                    "losers_hit": len(losers_hit),
                    "winners_hit": len(winners_hit),
                },
            )

        # Winner allow path
        if len(winners_hit) >= self._min_winner_hits:
            detail = ",".join(
                f"{f}={b}(wr={w:.0%},n={n})" for f, b, w, n in winners_hit
            )
            # Construct a v3-style serial for ML observer + ledger.
            serial = "|".join(
                [combo] + [buckets.get(f.code, "?") for f in self._FACTORS]
            )
            candidate.metadata["matrix_cluster_serial"] = serial
            candidate.metadata["matrix_schema"] = "wlf"
            # Best-WR winner becomes the score / tie-breaker.
            best_wr = max(w for _, _, w, _ in winners_hit)
            return GateResult(
                gate_name=self.name, passed=True,
                reason=f"winner_allow:{combo}:winners={len(winners_hit)}:best_wr={best_wr:.0%}:{detail}",
                metrics={
                    "schema": "wlf",
                    "combo": combo,
                    "winners_hit": len(winners_hit),
                    "best_wr": best_wr,
                    "score": float(best_wr),
                },
            )

        # No winners, no losers — empty signal
        if self._allow_no_signal:
            serial = "|".join(
                [combo] + [buckets.get(f.code, "?") for f in self._FACTORS]
            )
            candidate.metadata["matrix_cluster_serial"] = serial
            candidate.metadata["matrix_schema"] = "wlf_no_signal_allowed"
            return GateResult(
                gate_name=self.name, passed=True,
                reason=f"no_signal_allowed:{combo}",
                metrics={"schema": "wlf", "winners_hit": 0, "losers_hit": 0},
            )

        return GateResult(
            gate_name=self.name, passed=False,
            reason=f"no_signal:{combo}:winners={len(winners_hit)}<min{self._min_winner_hits},losers=0",
            metrics={
                "schema": "wlf",
                "combo": combo,
                "winners_hit": len(winners_hit),
                "losers_hit": 0,
            },
        )

    # ------------------------------------------------------------------
    # v3 cell-formula evaluator (fallback if WLF unavailable)
    # ------------------------------------------------------------------
    def _evaluate_v3_cells(self, candidate, row, family, session, direction, buckets) -> GateResult:
        key = (row["pair"], family, direction, session)
        clusters = self._cell_index.get(key, [])
        if not clusters:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_cluster_in_matrix:pair={row['pair']},family={family},dir={direction},session={session}",
                metrics={"family_resolved": family, "session": session, "schema": "v3_cells"},
            )
        active = []
        for c in clusters:
            formula: dict = c.get("_formula", {})
            missed = False
            for fcode, allowed in formula.items():
                if not allowed:
                    continue
                if buckets.get(fcode, "") not in allowed:
                    missed = True
                    break
            if missed:
                continue
            opt_exp = float(c.get("exp_optimized_pips", 0) or 0)
            if opt_exp < 1.5:
                continue
            active.append((opt_exp, c))
        if not active:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_active_cluster_v3:{family}/{session}",
                metrics={"clusters_evaluated": len(clusters), "schema": "v3_cells"},
            )
        active.sort(key=lambda kv: -kv[0])
        best_exp, best = active[0]
        candidate.metadata["matrix_cluster_serial"] = best.get("serial", "")
        candidate.metadata["matrix_schema"] = "v3_cells"
        return GateResult(
            gate_name=self.name, passed=True,
            reason=f"cluster_active_v3:{best.get('serial','')}:exp={best_exp:.2f}p",
            metrics={"schema": "v3_cells", "score": float(best_exp)},
        )

    # ------------------------------------------------------------------
    # Legacy F-code fallback
    # ------------------------------------------------------------------
    def _evaluate_legacy(self, candidate, row, family, session, direction) -> GateResult:
        try:
            if self._factor_predicate("F40")(row):
                return GateResult(
                    gate_name=self.name, passed=False,
                    reason=f"F40_universal_htf20_mismatch:dir={direction}",
                    metrics={"blocked_by": "F40_universal", "schema": "legacy"},
                )
        except Exception:
            pass
        key = (row["pair"], family, direction, session)
        clusters = self._cell_index.get(key, [])
        if not clusters:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_cluster_in_matrix:{key}",
                metrics={"schema": "legacy"},
            )
        active = []
        for c in clusters:
            factor_ids_raw = str(c.get("factor_ids", "") or "")
            formula = [f.strip() for f in factor_ids_raw.split(",") if f.strip()]
            blocked = False
            for fid in formula:
                try:
                    if bool(self._factor_predicate(fid)(row) or False):
                        blocked = True
                        break
                except Exception:
                    pass
            if blocked:
                continue
            opt_exp = float(c.get("exp_optimized_pips", 0) or 0)
            if opt_exp < 1.5:
                continue
            active.append((opt_exp, c))
        if not active:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_active_cluster:{key}",
                metrics={"schema": "legacy"},
            )
        active.sort(key=lambda kv: -kv[0])
        best_exp, best_cluster = active[0]
        candidate.metadata["matrix_cluster_serial"] = best_cluster.get("serial", "")
        candidate.metadata["matrix_schema"] = "legacy"
        return GateResult(
            gate_name=self.name, passed=True,
            reason=f"cluster_active_legacy:{best_cluster.get('serial','')}",
            metrics={"schema": "legacy", "score": float(best_exp)},
        )
