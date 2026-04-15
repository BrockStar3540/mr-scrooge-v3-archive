"""Regime floor gate -- blocks if regime score below threshold."""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class RegimeFloorGate(BaseGate):
    """Blocks trades when the regime composite score is below a minimum floor.

    The regime score is a signed value where negative scores indicate
    unfavorable conditions. The default floor of -1 allows mildly
    negative regimes but blocks deeply adverse ones.
    """

    name = "regime_floor"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.min_score: float = self.config.get("min_score", -1)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        regime_cls = ctx.classifications.get("regime")
        regime_score = (
            regime_cls.metadata.get("score", 0) if regime_cls else 0
        )

        if regime_score < self.min_score:
            reason = (
                f"Regime score {regime_score} below floor"
                f" {self.min_score}"
            )
            self._log.debug(
                "[GATE:%s] FAILED symbol=%s reason=%s",
                self.name, candidate.symbol, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={
                    "regime_score": regime_score,
                    "min_score": self.min_score,
                },
            )

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=regime score %s >= %s",
            self.name, candidate.symbol, regime_score, self.min_score,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=(
                f"Regime score {regime_score} above floor"
                f" {self.min_score}"
            ),
            metrics={
                "score": max(0.0, min(1.0, (regime_score + 5) / 10.0)),
                "regime_score": regime_score,
                "min_score": self.min_score,
            },
        )
