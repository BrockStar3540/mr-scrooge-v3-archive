"""Exhaustion filter gate -- requires BB exhaustion for reversals."""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class ExhaustionFilterGate(BaseGate):
    """For reversal strategies: requires Bollinger Band state to indicate
    exhaustion (EXTREME or REJECTION).

    Trend strategies bypass this gate automatically.
    """

    name = "exhaustion_filter"

    # Strategy prefixes that skip the exhaustion check
    TREND_STRATEGIES = ("trend_full", "trend_stretch", "sma20_pullback")

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.required_bb_states: list[str] = self.config.get(
            "required_bb_states", ["EXTREME", "REJECTION"]
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        strategy = candidate.strategy.lower() if candidate.strategy else ""

        # Trend strategies bypass this gate
        is_trend = any(
            strategy.startswith(prefix) for prefix in self.TREND_STRATEGIES
        )
        if is_trend:
            self._log.debug(
                "[GATE:%s] PASSED symbol=%s reason=trend strategy bypass",
                self.name, candidate.symbol,
            )
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="Trend strategy -- exhaustion check bypassed",
                metrics={"score": 1.0, "bypassed": True},
            )

        # Get BB classification
        bb_cls = ctx.classifications.get("bollinger_band")
        bb_state = bb_cls.label if bb_cls else "UNKNOWN"

        if bb_state.upper() in [s.upper() for s in self.required_bb_states]:
            self._log.debug(
                "[GATE:%s] PASSED symbol=%s reason=BB state %s",
                self.name, candidate.symbol, bb_state,
            )
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason=f"BB exhaustion confirmed: {bb_state}",
                metrics={
                    "score": 1.0,
                    "bb_state": bb_state,
                    "required_states": self.required_bb_states,
                },
            )

        reason = (
            f"BB state {bb_state} not in required"
            f" {self.required_bb_states}"
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
                "bb_state": bb_state,
                "required_states": self.required_bb_states,
            },
        )
