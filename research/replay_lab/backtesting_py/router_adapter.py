"""Routing-table replay — mirror live entry_filter_gate semantics.

Wraps the real RoutingTable so the same parquet that runs live runs in
replay. Implements the three routing modes:
  - exact_strategy_only
  - exact_plus_family
  - exact_plus_loose_override
"""
from __future__ import annotations
import sys
from pathlib import Path

_SRC = Path("/home/ubuntu/mr-scrooge-v3/src")
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from scrooge_v3.strategies.routing_table import RoutingTable


_TIER_RANK = {
    "Probationary": 0, "Seed": 1, "Seed-Pro": 2,
    "Pro": 3, "Elite": 4,
}


def load_routing_table(parquet_path: str | None = None) -> RoutingTable:
    """Load the live routing table or a specified path."""
    if parquet_path is None:
        parquet_path = "data/routing_table_v10_fast_v1_13_full_mirror.parquet"
    if not Path(parquet_path).is_absolute():
        parquet_path = str(Path("/home/ubuntu/mr-scrooge-v3") / parquet_path)
    return RoutingTable(parquet_path)


def resolve_cell_match(
    table: RoutingTable,
    regime53_label: str,
    symbol: str,
    session: str,
    direction: str,
    strategy: str,
    sub_regime: str | None = None,
    routing_mode: str = "exact_strategy_only",
    min_tier: str = "Seed-Pro",
) -> tuple[bool, dict]:
    """Replicates entry_filter_gate.evaluate() match logic.

    Returns (passed: bool, info: dict).
    """
    if routing_mode == "bypass":
        # Skip slate entirely — useful for testing raw strategy edge
        # independent of routing-table coverage.
        return True, {"match_kind": "bypass", "cell_strategy": strategy,
                      "cell_family": None, "cell_tier": "bypass",
                      "cell_score_boost": 0.0, "decisions_count": 0}
    if not regime53_label or not session:
        return False, {"reason": "cell_key_unavailable", "match_kind": None}

    decisions = table.lookup(
        regime53_label, symbol, session,
        direction=direction, sub_regime=sub_regime,
    )

    # Exact strategy
    match = next((d for d in decisions if d.strategy == strategy), None)
    match_kind = "exact_strategy" if match else None

    # Exact family
    if match is None and routing_mode in ("exact_plus_family", "exact_plus_loose_override"):
        family_matches = [d for d in decisions if d.family == strategy]
        if family_matches:
            family_matches.sort(
                key=lambda d: (
                    _TIER_RANK.get((d.basis or {}).get("tier", "Probationary"), 0),
                    d.score_boost,
                ),
                reverse=True,
            )
            match = family_matches[0]
            match_kind = "exact_family"

    # Family-loose override
    if (
        match is None
        and routing_mode == "exact_plus_loose_override"
        and decisions
        and _TIER_RANK.get(min_tier, 0) >= _TIER_RANK["Seed-Pro"]
    ):
        trade_tier = [
            d for d in decisions
            if _TIER_RANK.get((d.basis or {}).get("tier", "Probationary"), 0) >= _TIER_RANK["Seed-Pro"]
            and not (d.basis or {}).get("family_locked", False)
        ]
        if trade_tier:
            trade_tier.sort(
                key=lambda d: (
                    _TIER_RANK.get((d.basis or {}).get("tier", "Probationary"), 0),
                    d.score_boost,
                ),
                reverse=True,
            )
            match = trade_tier[0]
            match_kind = "family_loose_override"

    if match is None:
        return False, {"reason": "no_routing_match", "match_kind": None,
                       "decisions_count": len(decisions)}

    basis = match.basis or {}
    return True, {
        "match_kind": match_kind,
        "cell_strategy": match.strategy,
        "cell_family": match.family,
        "cell_tier": basis.get("tier"),
        "cell_score_boost": match.score_boost,
        "decisions_count": len(decisions),
    }
