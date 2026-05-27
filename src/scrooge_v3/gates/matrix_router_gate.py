"""MatrixRouterGate — the single authoritative entry router.

Replaces:
  - regime_floor, regime_compat, regime_strategy_router (regime-based gates)
  - sub_regime_filter (sub-regime skiplist)
  - entry_filter, entry_filter_shadow (static-parquet routing)
  - htf_trend_filter (folded in as universal F40 pre-filter)

The matrix CSVs (baseline_matrix_by_session.csv, optimized_matrix_by_session.csv)
ARE the routing table. Each row = one cell. The cluster_serial encodes the
exact market signature (pair, family, direction, session, formula-factors).

On boot: load matrix into memory, build per-(pair,family,direction,session)
index.

On each candidate:
  1. F40 universal pre-filter — if candidate direction disagrees with htf20
     bias, reject (the matrix's #1 alpha across all 17 strategies).
  2. Lookup clusters by (pair, family, direction, session).
  3. For each matching cluster, apply its optimized formula factors as
     predicates against the live factor state. If a formula factor "would
     exclude" this trade (e.g. F40 fires for a long with htf20=short), the
     cluster is OFF.
  4. PASS if any cluster is ACTIVE with optimized_exp_pips >= min_exp_threshold
     (default 1.5p).
  5. FAIL otherwise with explanatory reason.

Threshold + tie-breaker (Brock 2026-05-27):
  - min_exp_threshold: 1.5p
  - tie-breaker (multiple active clusters): highest optimized_exp_pips wins
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate

LAB_DIR = Path("/home/ubuntu/mr-scrooge-v3/data/lab_matrix")

# Make factor_catalog importable
if str(LAB_DIR) not in sys.path:
    sys.path.insert(0, str(LAB_DIR))

log = logging.getLogger("scrooge_v3.gate.matrix_router")


class MatrixRouterGate(BaseGate):
    """Authoritative entry router based on lab matrix clusters."""

    name = "matrix_router"

    def __init__(self, config: dict | None = None, mode: GateMode = GateMode.HARD):
        super().__init__(config or {}, mode)
        self._min_exp = float(self.config.get("min_exp_threshold_pips", 1.5))
        self._opt: Optional[pd.DataFrame] = None
        self._factor_predicate = None
        self._FACTORS = None
        self._index: dict = {}
        self._loaded = False
        self._load_matrix()

    def _load_matrix(self) -> None:
        try:
            opt = pd.read_csv(LAB_DIR / "optimized_matrix_by_session.csv")
            from factor_catalog import FACTORS, factor_predicate
            self._FACTORS = FACTORS
            self._factor_predicate = factor_predicate
            self._opt = opt
            # Build (pair, strategy/family, direction, session) -> [cluster rows]
            for _, r in opt.iterrows():
                key = (str(r["pair"]), str(r["strategy"]), str(r["direction"]),
                       str(r.get("session", "")))
                self._index.setdefault(key, []).append(r.to_dict())
            self._loaded = True
            log.info(
                "[MATRIX_ROUTER] loaded %d clusters, %d unique cells, min_exp=%.1fp",
                len(opt), len(self._index), self._min_exp,
            )
        except Exception:
            log.exception("[MATRIX_ROUTER] load failed — gate will fail-open (PASS)")
            self._loaded = False

    @staticmethod
    def _row_from_ctx(candidate: TradeCandidate, ctx: SymbolContext) -> dict:
        """Build a factor-predicate-friendly row dict from candidate + context."""
        feat = ctx.features or {}
        cls_ = ctx.classifications or {}

        def fv(name):
            f = feat.get(name)
            if f is None: return {}
            return getattr(f, "values", {}) if hasattr(f, "values") else (f if isinstance(f, dict) else {})

        bb  = fv("bollinger"); atr = fv("atr"); rsi = fv("rsi")
        zs  = fv("zscore");    ema = fv("ema")
        htf = fv("htf");       tr  = fv("trend"); st = fv("structure")
        rng = fv("range");     vol = fv("volume")
        bb_state = getattr(cls_.get("bb_state"), "label", "") if cls_.get("bb_state") else ""
        session  = getattr(cls_.get("session_bucket"), "label", "") if cls_.get("session_bucket") else ""

        sym = candidate.symbol or ""
        spread_raw = float(getattr(ctx.snapshot, "spread", 0.0) or 0.0)
        pip = 0.01 if any(j in sym for j in ("JPY", "MXN")) else 0.0001
        spread_pips = spread_raw / pip if pip > 0 else 0.0
        direction = (getattr(candidate.direction, "value", str(candidate.direction)) or "")

        return {
            "pair": sym,
            "strategy_id": candidate.strategy or "",
            "direction_exec": direction,
            "session_bucket": session,
            "spread_pips": spread_pips,
            "rsi14": rsi.get("rsi14") or rsi.get("value"),
            "bb_position": bb.get("bb_position") or bb.get("position"),
            "bb_width_pips": bb.get("bb_width_pips") or bb.get("width_pips"),
            "zscore": zs.get("zscore") or zs.get("value"),
            "atr_5m_pips": atr.get("atr_5m_pips") or atr.get("atr_5m"),
            "atr_1h_pips": atr.get("atr_1h_pips") or atr.get("atr_1h"),
            "realized_vol": atr.get("realized_vol"),
            "adr_consumed": atr.get("adr_consumed"),
            "ema20_slope": ema.get("ema20_slope"),
            "ema50_slope": ema.get("ema50_slope"),
            "htf_bias_5":   htf.get("htf_bias_5"),
            "htf_bias_20":  htf.get("htf_bias_20"),
            "htf_bias_60":  htf.get("htf_bias_60"),
            "htf_bias_120": htf.get("htf_bias_120"),
            "trend_1h": tr.get("trend_1h"),
            "trend_4h": tr.get("trend_4h"),
            "bb_state": bb_state,
            "range_percentile":  rng.get("range_percentile"),
            "pullback_depth_pct": st.get("pullback_depth_pct"),
            "dist_to_swing_high_pips": st.get("dist_to_swing_high_pips"),
            "dist_to_swing_low_pips":  st.get("dist_to_swing_low_pips"),
            "distance_to_structure_pips": st.get("distance_to_structure_pips"),
        }

    def _candidate_family(self, candidate: TradeCandidate) -> str:
        """Resolve the matrix-family name for a candidate.

        Matrix uses family-level names (canonical_lien_dbb, ifvg, trend, etc.).
        Candidates emit variant names (DBB1_buy_zone_long, CMA_long, etc.).
        Sources, in order: metadata.strategy_family, candidate's strategy when
        it matches a family name, mapping table.
        """
        md_fam = (candidate.metadata or {}).get("strategy_family", "")
        if md_fam:
            return str(md_fam)
        strat = (candidate.strategy or "").lower()
        # Variant → family heuristics
        if strat.startswith("dbb"): return "canonical_lien_dbb"
        if strat.startswith("mtb"): return "box_master_theory"
        if strat.startswith("drv"): return "canonical_darvas"
        if strat.startswith("rg"):  return "reversal"
        if strat.startswith("itp_"): return "trend_pullback"
        if strat.startswith("cma_"): return "chaikin_macd_atr"
        if strat.startswith("cmr_"): return "compression_reversion"
        if strat.startswith("ce_"):  return "compression_expansion"
        if strat.startswith("sb_"):  return "session_breakout"
        if strat.startswith("ifvg"): return "ifvg"
        return candidate.strategy or ""

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        if not self._loaded:
            return GateResult(gate_name=self.name, passed=True,
                              reason="matrix_unavailable_fail_open",
                              metrics={})

        row = self._row_from_ctx(candidate, ctx)
        # === 1. F40 universal pre-filter (folded HTF gate) ===
        # F40 = cand_vs_htf20_mismatch. If candidate direction disagrees with
        # htf20, reject — matrix's #1 universal alpha across all 17 strategies.
        try:
            f40_pred = self._factor_predicate("F40")
            if bool(f40_pred(row)):
                return GateResult(
                    gate_name=self.name, passed=False,
                    reason=f"F40_universal_htf20_mismatch:dir={row['direction_exec']},htf20={row.get('htf_bias_20')}",
                    metrics={"blocked_by": "F40_universal_pre_filter"},
                )
        except Exception:
            pass  # if predicate errors, don't block on it

        # === 2. Cluster lookup ===
        family = self._candidate_family(candidate)
        session = row.get("session_bucket", "") or ""
        direction = row["direction_exec"]
        key = (row["pair"], family, direction, session)
        clusters = self._index.get(key, [])
        if not clusters:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_cluster_in_matrix:pair={row['pair']},family={family},dir={direction},session={session}",
                metrics={"family_resolved": family, "session": session},
            )

        # === 3. Evaluate each cluster's formula ===
        active = []
        for c in clusters:
            factor_ids_raw = str(c.get("factor_ids", "") or "")
            formula = [f.strip() for f in factor_ids_raw.split(",") if f.strip()]
            blocked_by = []
            for fid in formula:
                try:
                    pred = self._factor_predicate(fid)
                    if pred is None: continue
                    v = pred(row)
                    if bool(v) if v is not None else False:
                        blocked_by.append(fid)
                except Exception:
                    pass
            if blocked_by:
                continue  # cluster OFF
            opt_exp = float(c.get("exp_optimized_pips", 0) or 0)
            if opt_exp < self._min_exp:
                continue  # cluster too weak
            active.append((opt_exp, c))

        if not active:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_active_cluster:family={family},session={session},clusters_evaluated={len(clusters)}",
                metrics={"clusters_evaluated": len(clusters)},
            )

        # === 4. Tie-breaker: highest optimized_exp_pips wins ===
        active.sort(key=lambda kv: -kv[0])
        best_exp, best_cluster = active[0]
        candidate.metadata["matrix_cluster_serial"] = best_cluster.get("serial", "")
        candidate.metadata["matrix_optimized_exp_pips"] = best_exp
        candidate.metadata["matrix_baseline_exp_pips"] = float(best_cluster.get("exp_baseline_pips", 0) or 0)
        candidate.metadata["matrix_wr_optimized"] = float(best_cluster.get("wr_optimized", 0) or 0)
        candidate.metadata["matrix_kept_pct"] = float(best_cluster.get("kept_pct", 0) or 0)
        candidate.metadata["matrix_formula_factors"] = str(best_cluster.get("factor_ids", "") or "")

        return GateResult(
            gate_name=self.name, passed=True,
            reason=f"cluster_active:{best_cluster.get('serial','')}:exp={best_exp:.2f}p:active_count={len(active)}",
            metrics={
                "score": float(best_exp),
                "active_clusters": len(active),
                "best_exp_pips": best_exp,
            },
        )
