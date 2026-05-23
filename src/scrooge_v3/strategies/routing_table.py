"""Routing Table — per-(regime53, pair, session) strategy attachment.

Brock's 2026-05-14 architecture (the parser tree):

  tick -> regime parser  (label: technical_regime_53)
       -> pair parser    (label: symbol)
       -> session parser (label: session_bucket)
       -> RoutingTable lookup
          -> list of attached strategies + per-cell params
          -> empty list = nothing fires = death recorded

The table is data, not code. It carries:
  - which strategies are attached at each leaf
  - per-cell parameter overrides (r_target, score_boost, direction_constraint)
  - basis evidence (n, wins, sum_R, mean_R, wr) for audit

It is hot-loadable from a parquet file at boot. Hand overrides via YAML can
layer on top (future).

Cell key:  (regime53, pair, session_bucket, direction)
Cell value: list[RoutingDecision]
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.strategies.routing_table")


@dataclass
class RoutingDecision:
    """One attached strategy for one cell."""
    strategy: str
    family: str
    direction: str | None        # "long" / "short" / None (both)
    r_target: float
    score_boost: float
    basis: dict[str, Any] = field(default_factory=dict)


def _build_basis(r) -> dict:
    """Construct the basis dict from a parquet row.

    Carries audit metadata (n/wins/sum_R/mean_R/wr/source) plus optional
    per-cell rules introduced in routing_table_v4:
      - shave_rule      : winner-side entry filter (string, AND-conjunction)
      - loser_skip_rule : death-by-presence rule (string, AND-conjunction)
    Missing/null values are skipped so v2/v3 parquets continue to load.
    """
    basis = {
        "n": int(r.get("n", 0)),
        "wins": int(r.get("wins", 0)),
        "sum_R": float(r.get("sum_R", 0.0)),
        "mean_R": float(r.get("mean_R", 0.0)),
        "wr": float(r.get("wr", 0.0)),
        "source": str(r.get("source", "")),
    }
    # v8: include tier alongside the rule
    if 'tier' in (r.index if hasattr(r, 'index') else r):
        try:
            tval = r.get('tier') if hasattr(r, 'get') else r['tier']
            if tval is not None and (not isinstance(tval, float) or tval == tval):
                basis['tier'] = str(tval)
        except Exception:
            pass
    for key in ("shave_rule", "loser_skip_rule"):
        val = r.get(key) if hasattr(r, "get") else (r[key] if key in r else None)
        if val is None or (isinstance(val, float) and val != val):  # skip NaN
            continue
        sval = str(val).strip()
        if sval and sval.lower() not in ("nan", "none"):
            basis[key] = sval
    # Brock 2026-05-22: family_lock support. When True, entry_filter loose-family
    # override will SKIP this cell — only candidates with matching family approve.
    # Prevents cross-family cell absorption for new families at fresh leaves (e.g.
    # MTB at C01 EUR_CHF where reversal/direct candidates could otherwise loose-match).
    if 'family_locked' in (r.index if hasattr(r, 'index') else r):
        try:
            lval = r.get('family_locked') if hasattr(r, 'get') else r['family_locked']
            # Accept True, "true", 1 — reject NaN/None/False/empty
            if lval is True:
                basis['family_locked'] = True
            elif isinstance(lval, str) and lval.strip().lower() == "true":
                basis['family_locked'] = True
            elif isinstance(lval, (int, float)) and lval == lval and lval == 1:
                basis['family_locked'] = True
        except Exception:
            pass
    # 2026-05-23 Layer 2: sub_regime support. Cell can require a specific MTB sub_regime
    # (e.g. "MTB_C01_3"). When set, lookup() prefers cells whose basis['sub_regime'] matches
    # the candidate's classified mtb_sub_regime. Backward-compatible: cells without
    # sub_regime continue to match at parent-regime level (existing behavior).
    if 'sub_regime' in (r.index if hasattr(r, 'index') else r):
        try:
            sval = r.get('sub_regime') if hasattr(r, 'get') else r['sub_regime']
            if sval is not None and not (isinstance(sval, float) and sval != sval):
                s = str(sval).strip()
                # 2026-05-23: only set basis['sub_regime'] if it's a TRUE sub-regime ID
                # (contains underscore — e.g., "MTB_C02_4", "C02_3"). Legacy v1.9/v1.10/v1.11
                # cells set sub_regime=parent_regime (e.g., "C02") as a placeholder; those
                # should be treated as "no sub_regime requirement" so lookup() preference
                # logic works correctly.
                if s and s.lower() not in ('nan', 'none', '') and '_' in s:
                    basis['sub_regime'] = s
        except Exception:
            pass
    return basis


class RoutingTable:
    """In-memory routing table loaded from parquet.

    Lookup signature:
        decisions = table.lookup(regime53, pair, session_bucket, direction=None)
        # -> list[RoutingDecision]

    Empty list = death-by-absence at this leaf.
    """

    def __init__(self, parquet_path: str | Path | None = None):
        self._table: dict[tuple[str, str, str], list[RoutingDecision]] = {}
        self._loaded_path: str | None = None
        self._rows = 0
        self._unique_leaves = 0
        if parquet_path:
            self.load(parquet_path)

    def load(self, parquet_path: str | Path) -> None:
        try:
            import pandas as pd  # local import to avoid hard dep at module-load
        except ImportError:
            log.warning("[ROUTING_TABLE] pandas not available; table empty")
            return
        p = Path(parquet_path)
        if not p.exists():
            log.warning("[ROUTING_TABLE] parquet not found: %s — table empty", p)
            return
        df = pd.read_parquet(p)
        self._table.clear()
        for _, r in df.iterrows():
            key = (
                str(r["technical_regime_53"]),
                str(r["pair"]),
                str(r["session_bucket"]),
            )
            self._table.setdefault(key, []).append(RoutingDecision(
                strategy=str(r["strategy"]),
                family=str(r["family"]),
                direction=str(r["direction"]) if r.get("direction") else None,
                r_target=float(r.get("r_target", 1.5)),
                score_boost=float(r.get("score_boost", 0.0)),
                basis=_build_basis(r),
            ))
        self._loaded_path = str(p)
        self._rows = int(len(df))
        self._unique_leaves = len(self._table)
        log.info(
            "[ROUTING_TABLE] loaded %s — rows=%d leaves=%d",
            p.name, self._rows, self._unique_leaves,
        )

    def lookup(
        self,
        regime53: str | None,
        pair: str,
        session_bucket: str,
        direction: str | None = None,
        sub_regime: str | None = None,
    ) -> list[RoutingDecision]:
        """Return attached strategies for this leaf. Empty list = death."""
        if not regime53:
            return []
        key = (str(regime53), str(pair), str(session_bucket))
        decisions = self._table.get(key, [])
        if direction is None:
            return list(decisions)
        # Filter by direction constraint
        out = []
        for d in decisions:
            if d.direction is None or d.direction == direction:
                out.append(d)
        # 2026-05-23 Layer 2: sub_regime preference. If caller passed sub_regime (from
        # mtb_sub_regime classifier), prefer cells with matching basis['sub_regime'].
        # If no matching sub_regime cells exist at this leaf, fall back to non-sub_regime
        # cells (backward compatible — v1.9/v1.10/v1.11 cells don't set sub_regime).
        # When sub_regime is None (non-C01/C02 regime or classifier failed), sub_regime-tagged
        # cells MUST be excluded — their sub_regime requirement isn't satisfied.
        if out:
            sub_tagged = [d for d in out if (d.basis or {}).get('sub_regime') is not None]
            non_sub = [d for d in out if (d.basis or {}).get('sub_regime') is None]
            if sub_regime is None:
                # No sub_regime classification — only non_sub cells are valid
                return non_sub
            # sub_regime provided — prefer matching cells, include non_sub as fallback
            sub_matched = [d for d in sub_tagged if (d.basis or {}).get('sub_regime') == sub_regime]
            if sub_matched:
                return sub_matched + non_sub
            return non_sub
        return out

    def strategy_names_for(
        self, regime53: str | None, pair: str, session_bucket: str,
        direction: str | None = None,
    ) -> list[str]:
        """Just the attached strategy names — for callers that only need names."""
        return [d.strategy for d in self.lookup(regime53, pair, session_bucket, direction)]

    def families_for(
        self, regime53: str | None, pair: str, session_bucket: str,
        direction: str | None = None,
    ) -> list[str]:
        """Distinct families attached at this leaf."""
        return sorted({d.family for d in self.lookup(regime53, pair, session_bucket, direction)})

    @property
    def stats(self) -> dict[str, Any]:
        return {
            "loaded_path": self._loaded_path,
            "rows": self._rows,
            "leaves": self._unique_leaves,
        }
