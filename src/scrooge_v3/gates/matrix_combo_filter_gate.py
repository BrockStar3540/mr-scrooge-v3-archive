"""matrix_combo_filter_gate — Gate #3 of the 4-layer matrix cascade.

Confirms the full combo (pair, family, direction, session) exists in the
WLF index. The pair_filter only checked (pair, session); this gate adds
strategy-family + direction.

Resolves family from candidate.strategy (e.g. DBB3_buy_zone_sustained_long
-> canonical_lien_dbb). On PASS, stamps combo + family on candidate.metadata.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate
from . import matrix_engine as me

log = logging.getLogger("scrooge_v3.gate.matrix_combo_filter")


class MatrixComboFilterGate(BaseGate):
    name = "matrix_combo_filter"

    def __init__(self, config: dict | None = None, mode: GateMode = GateMode.HARD):
        super().__init__(config or {}, mode)
        try:
            me.load()
            log.info("[MATRIX_COMBO_FILTER] ready — %d combos in WLF",
                     len(me.wlf_index()))
        except Exception:
            log.exception("[MATRIX_COMBO_FILTER] engine load failed; gate fails-open")

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        sym = candidate.symbol or "?"
        family = me.candidate_family(candidate)
        direction = me.candidate_direction(candidate)
        session = (candidate.metadata or {}).get("matrix_session") or me.candidate_session(ctx)
        combo = me.combo_key(sym, family, direction, session)

        idx = me.wlf_index()
        present = combo in idx
        log.info("[MATRIX_COMBO_FILTER] combo=%s present=%s", combo, present)

        if not present:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"combo_not_in_matrix:{combo}",
                metrics={"combo": combo},
            )
        candidate.metadata["matrix_combo"] = combo
        candidate.metadata["matrix_family"] = family
        candidate.metadata["matrix_direction"] = direction
        rules_for_combo = idx.get(combo, {})
        candidate.metadata["matrix_factors_with_data"] = len(rules_for_combo)
        return GateResult(
            gate_name=self.name, passed=True,
            reason=f"combo_known:{combo}:factors_with_data={len(rules_for_combo)}",
            metrics={"combo": combo, "factors_with_data": len(rules_for_combo)},
        )
