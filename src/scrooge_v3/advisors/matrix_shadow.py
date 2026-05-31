"""Matrix shadow advisor — parallel cross-validation layer for LightGBM.

Per Brock 2026-05-29: wire matrix data alongside per-pair modules so the
ML has both signals available. The two were independently mined from the
same 838k corpus and agree on the king factor (HTF alignment). Disagreements
between them on specific candidates are high-information signal.

Loads:
  data/matrix/optimized_matrix_by_session.csv  (3,880 curated cells)
  data/matrix/factor_lift_table.csv            (44k factor-per-cell lifts)

At scan time, for each picked candidate:
  1. Lookup cell for (pair × strategy_family × direction × session)
     → if cell exists, that combo has lab-validated edge with given factor formula
  2. Aggregate factor lifts for (pair × strategy_family × direction)
     → matrix_factor_score = mean lift across all factors for this cell

Output: data/matrix_shadow.jsonl, one line per candidate the bot selected.
Never gates, never alters routing. Pure observability.
"""
from __future__ import annotations

import json
import logging
import threading
import time
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.shadow.matrix")

_OPT_MATRIX: dict[tuple, list[dict]] | None = None
_FACTOR_LIFT: dict[tuple, dict[str, float]] | None = None
_LOG_PATH: Path | None = None
_LOCK = threading.Lock()


def load(
    matrix_dir: str = "/home/ubuntu/mr-scrooge-v3/data/matrix",
    log_path: str = "/home/ubuntu/mr-scrooge-v3/data/matrix_shadow.jsonl",
) -> bool:
    """Load matrix CSVs. Returns True on success, False if files missing."""
    global _OPT_MATRIX, _FACTOR_LIFT, _LOG_PATH
    d = Path(matrix_dir)
    opt_p = d / "optimized_matrix_by_session.csv"
    lift_p = d / "factor_lift_table.csv"
    if not opt_p.exists() or not lift_p.exists():
        log.warning("[MATRIX_SHADOW] missing files at %s — disabled", matrix_dir)
        return False
    try:
        import pandas as pd

        # Optimized matrix: key by (pair, strategy, direction, session)
        opt = pd.read_csv(opt_p)
        opt = opt.dropna(subset=["pair", "strategy", "direction", "session"])
        idx: dict[tuple, list[dict]] = {}
        for _, row in opt.iterrows():
            key = (row["pair"], row["strategy"], row["direction"], row["session"])
            idx.setdefault(key, []).append({
                "serial":             row.get("serial"),
                "factor_ids":         row.get("factor_ids"),
                "n_optimized":        int(row.get("n_optimized", 0)),
                "wr_optimized":       float(row.get("wr_optimized", 0)),
                "exp_optimized_pips": float(row.get("exp_optimized_pips", 0)),
                "lift_pips":          float(row.get("lift_pips", 0)),
                "kept_pct":           float(row.get("kept_pct", 0)),
            })
        _OPT_MATRIX = idx
        log.info(
            "[MATRIX_SHADOW] optimized_matrix: %d cells, %d (pair,strat,dir,session) keys",
            len(opt), len(idx),
        )

        # Factor lift table: key by (pair, strategy, direction)
        lift = pd.read_csv(lift_p)
        lift = lift.dropna(subset=["pair", "strategy", "direction", "factor_name", "lift_exp"])
        lift = lift[lift["n_kept"] > 0]
        lift_idx: dict[tuple, dict[str, float]] = {}
        for (pair, strat, direction), grp in lift.groupby(["pair", "strategy", "direction"]):
            lift_idx[(pair, strat, direction)] = {
                row["factor_name"]: float(row["lift_exp"])
                for _, row in grp.iterrows()
            }
        _FACTOR_LIFT = lift_idx
        log.info(
            "[MATRIX_SHADOW] factor_lift_table: %d (pair,strat,dir) keys",
            len(lift_idx),
        )

        _LOG_PATH = Path(log_path)
        _LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        log.info("[MATRIX_SHADOW] log path: %s", log_path)
        return True
    except Exception as e:
        log.exception("[MATRIX_SHADOW] load failed: %s", e)
        return False


def observe(symbol: str, ctx, candidate, all_candidates: list | None = None) -> None:
    """Log matrix verdict for the picked candidate. Never raises."""
    if _OPT_MATRIX is None or _FACTOR_LIFT is None or _LOG_PATH is None:
        return
    try:
        direction = (
            candidate.direction.value
            if hasattr(candidate.direction, "value")
            else str(candidate.direction)
        )

        # Session + family mapping via ml_router
        from scrooge_v3.strategies import ml_router
        session = ml_router._session(ctx) or "unknown"
        family = ml_router.variant_to_family(candidate.strategy) or candidate.strategy

        # Optimized matrix cell lookup
        cell_key = (symbol, family, direction, session)
        cells = _OPT_MATRIX.get(cell_key, [])
        best_cell = (
            max(cells, key=lambda c: c["exp_optimized_pips"])
            if cells else None
        )

        # Factor lift aggregate
        lift_key = (symbol, family, direction)
        lift_map = _FACTOR_LIFT.get(lift_key, {})
        if lift_map:
            values = list(lift_map.values())
            matrix_factor_score = sum(values) / len(values)
            sorted_factors = sorted(lift_map.items(), key=lambda x: x[1], reverse=True)
            top_pos = [(n, round(v, 4)) for n, v in sorted_factors[:3]]
            top_neg = [(n, round(v, 4)) for n, v in sorted_factors[-3:][::-1]]
        else:
            matrix_factor_score = None
            top_pos, top_neg = [], []

        # Verdict roll-up
        if best_cell is not None and best_cell["exp_optimized_pips"] > 0:
            verdict = "MATRIX_PASS"
        elif best_cell is not None:
            verdict = "MATRIX_NEG_CELL"
        elif lift_map:
            verdict = "NO_CELL_FACTOR_ONLY"
        else:
            verdict = "MATRIX_BLIND"

        entry = {
            "ts":             time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "symbol":         symbol,
            "strategy":       candidate.strategy,
            "family":         family,
            "direction":      direction,
            "session":        session,
            "lightgbm_p_win": candidate.metadata.get("lightgbm_p_win"),
            "candidate_score": float(getattr(candidate, "score", 0.0)),
            "verdict":        verdict,
            "matrix_cell_exists":   best_cell is not None,
            "matrix_n_cells":       len(cells),
            "matrix_best_cell":     best_cell,
            "matrix_factor_score":  (
                round(matrix_factor_score, 4)
                if matrix_factor_score is not None else None
            ),
            "matrix_top_pos":       top_pos,
            "matrix_top_neg":       top_neg,
        }

        with _LOCK:
            with _LOG_PATH.open("a") as f:
                f.write(json.dumps(entry, default=str) + "\n")
    except Exception:
        log.debug("[MATRIX_SHADOW] observe failed", exc_info=True)


def is_loaded() -> bool:
    return _OPT_MATRIX is not None and _FACTOR_LIFT is not None
