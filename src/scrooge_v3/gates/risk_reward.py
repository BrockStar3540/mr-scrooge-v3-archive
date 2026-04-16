"""Risk-reward gate -- checks minimum RR ratio by strategy family."""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


def _candidate_family(candidate: TradeCandidate) -> str:
    """Extract strategy family from candidate metadata or strategy name."""
    md = getattr(candidate, "metadata", {}) or {}
    fam = md.get("strategy_family")
    if fam:
        return str(fam)
    strat = (candidate.strategy or "").lower()
    if strat in ("dbb_trend", "trend", "trend_full", "trend_stretch"):
        return "trend"
    if strat in ("reversal", "box_reversal"):
        return "reversal"
    return "default"


class RiskRewardGate(BaseGate):
    """Checks that the candidate meets minimum risk-reward ratio.

    Uses strategy family to select the correct RR threshold.
    """

    name = "risk_reward"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.reversal_min_rr: float = self.config.get("reversal_min_rr", 1.0)
        self.trend_min_rr: float = self.config.get("trend_min_rr", 1.10)
        self.default_min_rr: float = self.config.get("default_min_rr", 1.0)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        rr = candidate.risk_reward
        family = _candidate_family(candidate)

        if family == "trend":
            min_rr = self.trend_min_rr
        elif family == "reversal":
            min_rr = self.reversal_min_rr
        else:
            min_rr = self.default_min_rr

        if rr < min_rr:
            reason = f"RR {rr:.2f} below {family} minimum {min_rr:.2f}"
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={"risk_reward": rr, "min_rr": min_rr, "strategy_family": family},
            )

        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=f"RR {rr:.2f} meets {family} minimum {min_rr:.2f}",
            metrics={"score": min(1.0, rr / 2.0), "risk_reward": rr, "min_rr": min_rr, "strategy_family": family},
        )
