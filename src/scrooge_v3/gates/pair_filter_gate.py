"""pair_filter_gate — Gate #2 of the 4-layer matrix cascade.

Confirms the (pair, session) tuple has at least one combo in the WLF index.
If the lab never produced data for this pair at this session, we have no
basis for any combo evaluation and we block early before bucket calc.

Reads matrix_session from candidate.metadata (set by session_filter_gate).
Stamps matrix_pair_session_combos_count on PASS.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate
from . import matrix_engine as me

log = logging.getLogger("scrooge_v3.gate.pair_filter")


class PairFilterGate(BaseGate):
    name = "pair_filter"

    def __init__(self, config: dict | None = None, mode: GateMode = GateMode.HARD):
        super().__init__(config or {}, mode)
        try:
            me.load()
            ps = me.pair_session_combos()
            log.info("[PAIR_FILTER] ready — %d (pair,session) tuples in matrix", len(ps))
        except Exception:
            log.exception("[PAIR_FILTER] matrix_engine load failed; gate fails-open")

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        sym = candidate.symbol or "?"
        session = (candidate.metadata or {}).get("matrix_session") or me.candidate_session(ctx)

        ps = me.pair_session_combos()
        combos_here = ps.get((sym, session), set())
        log.info("[PAIR_FILTER] sym=%s session=%s combos_in_matrix=%d",
                 sym, session, len(combos_here))

        if not combos_here:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"pair_session_not_in_matrix:{sym}|{session}",
                metrics={"pair": sym, "session": session, "combos_count": 0},
            )

        candidate.metadata["matrix_pair_session_combos_count"] = len(combos_here)
        return GateResult(
            gate_name=self.name, passed=True,
            reason=f"pair_session_known:{sym}|{session}:{len(combos_here)}_combos",
            metrics={"pair": sym, "session": session, "combos_count": len(combos_here)},
        )
