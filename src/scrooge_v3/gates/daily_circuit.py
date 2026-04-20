"""Daily circuit breaker gate - halts new entries once daily loss cap is hit.

Cheapest, highest-priority veto: runs FIRST in the gate pipeline. Reads
``ctx.state['daily_circuit']`` which is maintained by the CooldownTracker
in state recovery. On UTC day rollover the tracker resets the trip flag.
"""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class DailyCircuitGate(BaseGate):
    """Hard-block all new entries for the rest of the UTC day once tripped."""

    name = "daily_circuit"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        circuit: dict = ctx.state.get("daily_circuit", {}) or {}
        tripped = bool(circuit.get("tripped"))
        pnl = float(circuit.get("realized_pnl", 0.0))
        eq = float(circuit.get("equity_start", 0.0))
        pct = (pnl / eq * 100.0) if eq > 0 else 0.0

        if tripped:
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=(
                    f"Daily circuit tripped: {pct:.2f}% "
                    f"({pnl:+.2f}) - halting new entries"
                ),
                metrics={
                    "realized_pnl": pnl,
                    "equity_start": eq,
                    "daily_pct": pct,
                    "tripped_at": circuit.get("tripped_at"),
                },
            )

        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=f"Daily P/L {pct:+.2f}% within limits",
            metrics={
                "score": 1.0,
                "realized_pnl": pnl,
                "daily_pct": pct,
            },
        )
