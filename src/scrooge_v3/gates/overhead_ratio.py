"""Overhead ratio gate -- spread cost vs potential profit check."""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class OverheadRatioGate(BaseGate):
    # WARNING: OTR <8% = 17% WR (worst bracket). Low OTR = wide unfocused box = DANGER.
    """Gate 6 -- Overhead-to-range ratio (OTR).

    Blocks trades where spread costs consume too much of the potential profit.
    OTR = total_round_trip_spread / range_half
    """

    name = "overhead_ratio"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.otr_excellent: float = self.config.get("otr_excellent", 0.05)
        self.otr_acceptable: float = self.config.get("otr_acceptable", 0.12)
        self.otr_marginal: float = self.config.get("otr_marginal", 0.25)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        total_overhead: float = ctx.metadata.get("total_overhead", 0.0)
        range_half: float = ctx.metadata.get("range_half", 0.0)
        zone_tier: int = ctx.metadata.get("zone_tier", 3)
        pressure_strength: str = ctx.metadata.get(
            "pressure_strength", "weak"
        )
        confirmation_type: str = ctx.metadata.get("confirmation_type", "")

        if range_half <= 0:
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason="Range half is zero -- invalid range",
                metrics={"score": 0.0},
            )

        otr = total_overhead / range_half

        if otr < 0.08:
            # OTR <8% = wide unfocused box, 17% WR in V1 live data
            category = "too_low"
            score = 0.0
            passed = False
        elif otr <= 0.18:
            # Sweet spot: 63-68% WR in V1 live data
            category = "sweet_spot"
            score = 1.0
            passed = True
        elif otr < self.otr_marginal:
            category = "marginal"
            # Marginal OTR: only allow if setup quality compensates
            high_quality = zone_tier <= 2 and (
                pressure_strength == "strong"
                or confirmation_type
                in ("wick_rejection", "engulfing_reversal")
            )
            passed = high_quality
            score = 0.4 if passed else 0.0
        else:
            category = "skip"
            score = 0.0
            passed = False

        reason = f"OTR {otr:.1%} ({category})"
        if not passed and category == "too_low":
            reason = f"OTR {otr:.1%} -- OTR too low -- wide box trap (17% WR)"
        elif not passed and category == "marginal":
            reason += (
                f" -- marginal requires Tier<=2 + strong signal"
                f" (tier={zone_tier}"
                f" pressure={pressure_strength}"
                f" confirm={confirmation_type})"
            )

        if passed:
            self._log.debug(
                "[GATE:%s] PASSED symbol=%s reason=%s",
                self.name, candidate.symbol, reason,
            )
        else:
            self._log.debug(
                "[GATE:%s] FAILED symbol=%s reason=%s",
                self.name, candidate.symbol, reason,
            )

        return GateResult(
            gate_name=self.name,
            passed=passed,
            reason=reason,
            metrics={
                "score": score,
                "otr_ratio": otr,
                "otr_category": category,
            },
        )
