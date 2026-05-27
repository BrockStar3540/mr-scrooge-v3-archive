"""Matrix-driven shadow advisor.

For each live scan with a candidate, look up the matching lab cluster, apply
the optimized formula's factor exclusions, and emit a MATRIX_TAKE / MATRIX_BLOCK
decision with the explanation.

Inputs:
  - data/lab_matrix/optimized_matrix.csv          (unified view)
  - data/lab_matrix/optimized_matrix_by_session.csv (session view)
  - data/lab_matrix/factor_catalog.py            (factor predicate definitions)

The bot scan_row provides features in ml_features + classifications. We map
those to the same field names the factor predicates expect (rsi14, bb_position,
spread_pips, atr_5m_pips, atr_1h_pips, htf_bias_20, etc.) and ask the predicate
whether each factor would exclude the trade.

Returns a dict the shadow recorder writes alongside the existing decision:
  {
    "matrix_decision": "TAKE" | "BLOCK" | "NO_MATCH",
    "matrix_serial": "AUD_JPY-RNA-Sdirect-Dlong-F21-F29-F43-F44-F60-F61",
    "matrix_baseline_exp_pips": 3.11,
    "matrix_optimized_exp_pips": 8.19,
    "matrix_formula_factors": ["F21", "F29", "F43", "F44", "F60", "F61"],
    "matrix_blocking_factors": ["F44"],   # which formula factors fired
    "matrix_blocking_names": ["cand_vs_trend4h_mismatch"],
    "matrix_view": "unified" | "by_session",
  }
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any, Optional

import pandas as pd

log = logging.getLogger("scrooge_v3.matrix_advisor")

# Path to the lab matrix data shipped to this host
LAB_DIR = Path("/home/ubuntu/mr-scrooge-v3/data/lab_matrix")

# Make the factor catalog importable
if str(LAB_DIR) not in sys.path:
    sys.path.insert(0, str(LAB_DIR))


class MatrixAdvisor:
    """Loads the matrix once at boot, advises on every live candidate."""

    def __init__(self, lab_dir: Path = LAB_DIR):
        self.lab_dir = lab_dir
        self._opt_unified: Optional[pd.DataFrame] = None
        self._opt_by_session: Optional[pd.DataFrame] = None
        self._factor_predicate = None
        self._factor_names = None
        self.loaded = False
        self._load()

    def _load(self) -> None:
        try:
            self._opt_unified = pd.read_csv(self.lab_dir / "optimized_matrix.csv")
            self._opt_by_session = pd.read_csv(self.lab_dir / "optimized_matrix_by_session.csv")
            from factor_catalog import FACTORS, factor_predicate
            self._FACTORS = FACTORS
            self._factor_predicate = factor_predicate
            self.loaded = True
            log.info(
                "[MATRIX] loaded unified=%d clusters, by_session=%d clusters, factors=%d",
                len(self._opt_unified), len(self._opt_by_session), len(FACTORS),
            )
        except Exception:
            log.exception("[MATRIX] load failed — advisor disabled")

    # ---------------------------------------------------------------
    # Build a "row" the factor predicates can consume.
    #
    # Factor predicates were written against the lab's per-trade CSV schema.
    # We need to translate scan_row fields → those keys.
    # ---------------------------------------------------------------
    @staticmethod
    def _row_from_scan(scan_row: dict[str, Any]) -> dict[str, Any]:
        """Translate a live scan_row into the field shape factor predicates expect."""
        feat = scan_row.get("features", {}) or {}
        cls = scan_row.get("classifications", {}) or {}
        candidate = scan_row.get("candidate", {}) or {}

        def f(name, default=None):
            obj = feat.get(name)
            if not isinstance(obj, dict): return default
            return obj

        bollinger = f("bollinger", {}) or {}
        atr = f("atr", {}) or {}
        rsi = f("rsi", {}) or {}
        zscore = f("zscore", {}) or {}
        bb_state = (cls.get("bb_state") or {})
        regime53 = (cls.get("regime53") or {})
        session = (cls.get("session_bucket") or {})

        # Try multiple sources for each value
        row = {
            "pair": scan_row.get("symbol", ""),
            "strategy_id": candidate.get("strategy", ""),
            "direction_exec": candidate.get("direction", ""),
            "spread_pips": float(scan_row.get("spread", 0) or 0) * 10000  # rough; need pip-aware
                if scan_row.get("symbol", "")[-3:] != "JPY"
                else float(scan_row.get("spread", 0) or 0) * 100,
            # core factors expected by factor_catalog.py:
            "rsi14": rsi.get("rsi14") or rsi.get("value"),
            "bb_position": bollinger.get("bb_position") or bollinger.get("position"),
            "bb_width_pips": bollinger.get("bb_width_pips") or bollinger.get("width_pips"),
            "zscore": zscore.get("zscore") or zscore.get("value"),
            "atr_5m_pips": atr.get("atr_5m_pips") or atr.get("atr_5m"),
            "atr_1h_pips": atr.get("atr_1h_pips") or atr.get("atr_1h"),
            "realized_vol": atr.get("realized_vol"),
            "adr_consumed": atr.get("adr_consumed"),
            "ema20_slope": (feat.get("ema") or {}).get("ema20_slope"),
            "ema50_slope": (feat.get("ema") or {}).get("ema50_slope"),
            # HTF biases — read from features.htf or classifications
            "htf_bias_5":   (feat.get("htf") or {}).get("htf_bias_5"),
            "htf_bias_20":  (feat.get("htf") or {}).get("htf_bias_20"),
            "htf_bias_60":  (feat.get("htf") or {}).get("htf_bias_60"),
            "htf_bias_120": (feat.get("htf") or {}).get("htf_bias_120"),
            "trend_1h":     (feat.get("trend") or {}).get("trend_1h"),
            "trend_4h":     (feat.get("trend") or {}).get("trend_4h"),
            "bb_state":     bb_state.get("label", ""),
            "regime53":     regime53.get("label", "") or "NA",
            "session_bucket": session.get("label", "") or scan_row.get("identity", {}).get("session_bucket", ""),
            "range_percentile":  (feat.get("range") or {}).get("range_percentile"),
            "pullback_depth_pct": (feat.get("structure") or {}).get("pullback_depth_pct"),
            "dist_to_swing_high_pips": (feat.get("structure") or {}).get("dist_to_swing_high_pips"),
            "dist_to_swing_low_pips":  (feat.get("structure") or {}).get("dist_to_swing_low_pips"),
            "distance_to_structure_pips": (feat.get("structure") or {}).get("distance_to_structure_pips"),
        }
        return row

    def _lookup_cluster(self, row: dict[str, Any]) -> Optional[dict[str, Any]]:
        """Find the most specific matching cluster row in the matrix.

        Try session-stratified first; fall back to unified.
        """
        pair = row["pair"]; direction = row["direction_exec"]
        strat = row["strategy_id"]; session = row.get("session_bucket")
        if not (pair and direction and strat):
            return None

        # Session-specific match
        if self._opt_by_session is not None and session:
            mask = (
                (self._opt_by_session["pair"] == pair) &
                (self._opt_by_session["direction"] == direction) &
                (self._opt_by_session["strategy"] == strat) &
                (self._opt_by_session["session"] == session)
            )
            sub = self._opt_by_session[mask]
            if not sub.empty:
                return {"view": "by_session", "row": sub.iloc[0].to_dict()}

        # Unified fallback
        if self._opt_unified is not None:
            mask = (
                (self._opt_unified["pair"] == pair) &
                (self._opt_unified["direction"] == direction) &
                (self._opt_unified["strategy"] == strat)
            )
            sub = self._opt_unified[mask]
            if not sub.empty:
                return {"view": "unified", "row": sub.iloc[0].to_dict()}
        return None

    def advise(self, scan_row: dict[str, Any]) -> dict[str, Any]:
        """Return the matrix decision for a single live scan."""
        if not self.loaded:
            return {"matrix_decision": "DISABLED"}

        row = self._row_from_scan(scan_row)
        if not row["strategy_id"] or not row["direction_exec"]:
            return {"matrix_decision": "NO_CANDIDATE"}

        match = self._lookup_cluster(row)
        if match is None:
            return {
                "matrix_decision": "NO_MATCH",
                "matrix_serial": None,
                "matrix_reason": "no_cluster_in_matrix",
            }

        m = match["row"]
        formula = (str(m.get("factor_ids", "") or "")).split(",") if m.get("factor_ids") else []
        formula = [f.strip() for f in formula if f.strip()]

        # Apply each factor predicate
        blocking = []
        blocking_names = []
        for fid in formula:
            pred = self._factor_predicate(fid)
            try:
                v = pred(row)
                excludes = bool(v) if v is not None else False
            except Exception:
                excludes = False
            if excludes:
                blocking.append(fid)
                blocking_names.append(self._FACTORS.get(fid, {}).get("name", fid))

        if blocking:
            decision = "BLOCK"
            reason = f"formula_factor_excludes:{','.join(blocking)}"
        else:
            # No formula factor fires — passes the optimized formula
            # Still respect baseline expectancy
            base_exp = float(m.get("exp_baseline_pips", 0) or 0)
            opt_exp  = float(m.get("exp_optimized_pips", 0) or 0)
            decision = "TAKE" if opt_exp > 0 else "BLOCK"
            reason = "formula_passed" if decision == "TAKE" else "cluster_negative_expectancy"

        return {
            "matrix_decision": decision,
            "matrix_serial": str(m.get("serial", "")),
            "matrix_view": match["view"],
            "matrix_reason": reason,
            "matrix_formula_factors": formula,
            "matrix_blocking_factors": blocking,
            "matrix_blocking_names": blocking_names,
            "matrix_baseline_exp_pips": float(m.get("exp_baseline_pips", 0) or 0),
            "matrix_optimized_exp_pips": float(m.get("exp_optimized_pips", 0) or 0),
            "matrix_baseline_wr": float(m.get("wr_baseline", 0) or 0),
            "matrix_optimized_wr": float(m.get("wr_optimized", 0) or 0),
            "matrix_kept_pct": float(m.get("kept_pct", 0) or 0),
            "matrix_n_baseline": int(m.get("n_baseline", 0) or 0),
        }


_singleton: Optional[MatrixAdvisor] = None

def get_advisor() -> MatrixAdvisor:
    global _singleton
    if _singleton is None:
        _singleton = MatrixAdvisor()
    return _singleton
