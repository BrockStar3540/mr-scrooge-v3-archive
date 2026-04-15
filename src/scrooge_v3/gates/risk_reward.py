"""Risk-reward gate -- checks minimum RR ratio by strategy type."""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class RiskRewardGate(BaseGate):
    """Checks that the candidate meets minimum risk-reward ratio.

    Reversal strategies require higher RR (1.35 default) than trend
    strategies (1.10 default) because reversals have lower base-rate
    win probability.
    """

    name = "risk_reward"

    # Strategy prefixes that map to trend thresholds
    TREND_STRATEGIES = ("trend_full", "trend_stretch", "sma20_pullback")

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.reversal_min_rr: float = self.config.get(
            "reversal_min_rr", 1.35
        )
        self.trend_min_rr: float = self.config.get("trend_min_rr", 1.10)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        rr = candidate.risk_reward
        strategy = candidate.strategy.lower() if candidate.strategy else ""

        is_trend = any(
            strategy.startswith(prefix) for prefix in self.TREND_STRATEGIES
        )
        min_rr = self.trend_min_rr if is_trend else self.reversal_min_rr
        strategy_label = "trend" if is_trend else "reversal"

        if rr < min_rr:
            reason = (
                f"RR {rr:.2f} below {strategy_label}"
                f" minimum {min_rr:.2f}"
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
                    "risk_reward": rr,
                    "min_rr": min_rr,
                    "strategy_type": strategy_label,
                },
            )

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=RR %.2f >= %.2f (%s)",
            self.name, candidate.symbol, rr, min_rr, strategy_label,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=(
                f"RR {rr:.2f} meets {strategy_label}"
                f" minimum {min_rr:.2f}"
            ),
            metrics={
                "score": min(1.0, rr / 2.0),
                "risk_reward": rr,
                "min_rr": min_rr,
                "strategy_type": strategy_label,
            },
        )
