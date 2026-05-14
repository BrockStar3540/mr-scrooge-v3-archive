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
                basis={
                    "n": int(r.get("n", 0)),
                    "wins": int(r.get("wins", 0)),
                    "sum_R": float(r.get("sum_R", 0.0)),
                    "mean_R": float(r.get("mean_R", 0.0)),
                    "wr": float(r.get("wr", 0.0)),
                    "source": str(r.get("source", "")),
                },
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
