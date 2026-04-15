"""Spread gate — mechanical spread safety checks.

Blocks when spread exceeds:
  1. Absolute threshold (2.0 pip default, 5.0 JPY)
  2. 10% of half-box range (spreads eating into profit)
  3. Natural stop distance (mechanically broken trade)

Reads from ctx.features and ctx.snapshot (V3 pattern).
"""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class SpreadGate(BaseGate):
    name = "spread"

    def __init__(self, config: dict[str, Any] | None = None, mode: GateMode = GateMode.HARD) -> None:
        super().__init__(config, mode)
        self.max_spread_jpy = self.config.get("max_spread_jpy", 5.0)
        self.max_spread_default = self.config.get("max_spread_default", 2.0)
        self.spread_pct_of_half = self.config.get("spread_pct_of_half", 0.10)

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        spread = ctx.snapshot.spread
        symbol = candidate.symbol
        threshold = self.max_spread_jpy if "JPY" in symbol else self.max_spread_default

        # 1. Absolute threshold
        if spread > threshold:
            return self._fail(f"Spread {spread:.4f} > threshold {threshold:.2f}",
                              {"spread": spread, "threshold": threshold})

        # 2. Spread as % of half-box (from zone_detector feature)
        zd = ctx.features.get("zone_detector")
        if zd and zd.values:
            zm = zd.values.get("zone_map")
            if zm and hasattr(zm, "session_range") and zm.session_range:
                half_box = (zm.session_range.PDH - zm.session_range.PDL) / 2
                if half_box > 0:
                    spread_pct = spread / half_box
                    if spread_pct > self.spread_pct_of_half:
                        return self._fail(
                            f"Spread {spread:.4f} = {spread_pct:.1%} of half-box (max {self.spread_pct_of_half:.0%})",
                            {"spread": spread, "half_box": half_box, "spread_pct": spread_pct})

        # 3. Spread vs natural stop (from candidate metadata)
        risk_points = candidate.metadata.get("risk_points", 0)
        if risk_points > 0 and spread >= risk_points:
            return self._fail(
                f"Spread {spread:.4f} >= natural stop {risk_points:.4f}",
                {"spread": spread, "natural_stop": risk_points})

        return self._pass(f"Spread {spread:.4f} OK", {"spread": spread, "threshold": threshold})

    def _pass(self, reason: str, metrics: dict) -> GateResult:
        metrics["score"] = 1.0
        return GateResult(gate_name=self.name, passed=True, reason=reason, metrics=metrics)

    def _fail(self, reason: str, metrics: dict) -> GateResult:
        return GateResult(gate_name=self.name, passed=False, reason=reason, metrics=metrics)
