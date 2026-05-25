"""Natural target floor gate — block candidates whose strategy projection
is below a minimum scalp size.

Strategy emissions write metadata["projected_tp_pips"] as the raw distance
to the strategy's natural target (e.g., upper 2σ band for DBB, PDH for MTB
long-pitchfork). This gate rejects when the projection is below the
configured floor — before scalper_clamp overrides TP with its fixed value.

Brock 2026-05-25: motivated by USD_CHF 4014 and CHF_JPY 4021. Both were
textbook-valid DBB setups but the BB compression was so tight that the
natural TP target was only 3-6 pips, while scalper_clamp demanded 12.
Result: trade entered at strategy's "almost-done" zone, scalper_clamp's
TP was unreachable, ran to stop.

Candidates without projected_tp_pips metadata PASS (gate fails open) so
strategies that haven't been instrumented yet aren't blanket-blocked.
"""
from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class NaturalTargetFloorGate(BaseGate):
    """Reject candidates whose strategy projects a target below min_pips."""

    name = "natural_target_floor"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.min_pips: float = float(self.config.get("min_pips", 7.0))

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        md = candidate.metadata or {}
        projected = md.get("projected_tp_pips")
        if projected is None:
            # Strategy didn't emit a natural target — pass (fail-open)
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason=f"no_projection_in_metadata:strategy={candidate.strategy}",
                metrics={"min_pips": self.min_pips, "projected_pips": -1.0},
            )
        try:
            projected_pips = float(projected)
        except (TypeError, ValueError):
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason=f"projection_unparseable:{projected!r}",
                metrics={"min_pips": self.min_pips, "projected_pips": -1.0},
            )

        if projected_pips < self.min_pips:
            reason = (
                f"projected_target_{projected_pips:.1f}p_below_floor_{self.min_pips:.1f}p"
            )
            self._log.info(
                "[GATE:%s] FAILED symbol=%s strategy=%s reason=%s",
                self.name, candidate.symbol, candidate.strategy, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={
                    "min_pips": self.min_pips,
                    "projected_pips": projected_pips,
                },
            )

        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=f"projected_{projected_pips:.1f}p_above_floor_{self.min_pips:.1f}p",
            metrics={
                "score": min(1.0, projected_pips / 24.0),
                "min_pips": self.min_pips,
                "projected_pips": projected_pips,
            },
        )
