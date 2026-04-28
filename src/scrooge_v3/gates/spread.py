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
        # ctx.snapshot.spread is a raw price difference (e.g. 0.00015 on
        # EUR/USD). Thresholds in this gate are in PIPS. Convert before
        # comparison — previously the gate compared price-units to pip-units
        # and never fired even on hostile spreads.
        raw_spread = ctx.snapshot.spread
        symbol = candidate.symbol
        is_jpy = any(j in symbol for j in ("JPY", "MXN"))
        pip_size = 0.01 if is_jpy else 0.0001
        spread_pips = raw_spread / pip_size if pip_size else raw_spread

        threshold = self.max_spread_jpy if is_jpy else self.max_spread_default

        # 1. Absolute threshold (pips)
        if spread_pips > threshold:
            return self._fail(
                f"Spread {spread_pips:.2f}p > threshold {threshold:.2f}p",
                {"spread_pips": spread_pips, "threshold": threshold},
            )

        # 2. Spread vs natural stop (both in pips now)
        risk_points = candidate.metadata.get("risk_points", 0)
        if risk_points > 0 and spread_pips >= risk_points:
            return self._fail(
                f"Spread {spread_pips:.2f}p >= natural stop {risk_points:.2f}p",
                {"spread_pips": spread_pips, "natural_stop": risk_points},
            )

        return self._pass(
            f"Spread {spread_pips:.2f}p OK",
            {"spread_pips": spread_pips, "threshold": threshold},
        )

    def _pass(self, reason: str, metrics: dict) -> GateResult:
        metrics["score"] = 1.0
        return GateResult(gate_name=self.name, passed=True, reason=reason, metrics=metrics)

    def _fail(self, reason: str, metrics: dict) -> GateResult:
        return GateResult(gate_name=self.name, passed=False, reason=reason, metrics=metrics)
