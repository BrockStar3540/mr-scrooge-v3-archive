"""Spread gate -- blocks when spread exceeds safety threshold."""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class SpreadGate(BaseGate):
    """Hard blocks when current spread exceeds the per-symbol threshold.

    JPY pairs use a wider threshold (5.0 pips default) because their
    price scale is ~100x larger than majors.
    """

    name = "spread"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.max_spread_jpy: float = self.config.get(
            "max_spread_jpy", 5.0
        )
        self.max_spread_default: float = self.config.get(
            "max_spread_default", 2.0
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        spread = ctx.snapshot.spread
        symbol = candidate.symbol

        threshold = (
            self.max_spread_jpy
            if "JPY" in symbol
            else self.max_spread_default
        )

        if spread > threshold:
            reason = (
                f"Spread {spread:.2f} exceeds threshold {threshold:.2f}"
            )
            self._log.debug(
                "[GATE:%s] FAILED symbol=%s reason=%s",
                self.name, symbol, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={
                    "spread": spread,
                    "threshold": threshold,
                },
            )

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=spread %.2f <= %.2f",
            self.name, symbol, spread, threshold,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=f"Spread {spread:.2f} within threshold {threshold:.2f}",
            metrics={
                "score": 1.0,
                "spread": spread,
                "threshold": threshold,
            },
        )
