"""session_filter_gate — Gate #1 of the 4-layer matrix cascade.

Cheapest, broadest check. Confirms the current scan landed in a known
session bucket (asia/asia_late/london_open/london/ny_open/ny_mid/ny_close/
off_hours). If the session classifier didn't tag the candidate or tagged
it as something unrecognized, we have no statistical basis for trading
and we block.

Stamps candidate.metadata["matrix_session"] on PASS so downstream gates
don't have to recompute.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate
from . import matrix_engine as me

log = logging.getLogger("scrooge_v3.gate.session_filter")


class SessionFilterGate(BaseGate):
    name = "session_filter"

    def __init__(self, config: dict | None = None, mode: GateMode = GateMode.HARD):
        super().__init__(config or {}, mode)
        # Touch engine to validate factor_buckets is importable at boot.
        try:
            me.load()
            log.info("[SESSION_FILTER] ready — %d known session buckets",
                     len(me.KNOWN_SESSIONS))
        except Exception:
            log.exception("[SESSION_FILTER] matrix_engine load failed; gate fails-open")

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        session = me.candidate_session(ctx)
        sym = candidate.symbol or "?"
        log.info("[SESSION_FILTER] sym=%s session=%r", sym, session)

        if not session:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"no_session_classification:sym={sym}",
                metrics={"session": ""},
            )
        if session not in me.KNOWN_SESSIONS:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"unknown_session:{session}",
                metrics={"session": session, "known": sorted(me.KNOWN_SESSIONS)},
            )
        candidate.metadata["matrix_session"] = session
        return GateResult(
            gate_name=self.name, passed=True,
            reason=f"session_known:{session}",
            metrics={"session": session},
        )
