"""ATR budget gate -- measures directional ATR consumption (advisory)."""

from __future__ import annotations

from typing import Any

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class ATRBudgetGate(BaseGate):
    """Gate 3 -- ATR consumption. Advisory only (always passes).

    Measures how much of the daily ATR the directional leg consumed.
    """

    name = "atr_budget"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.OBSERVE,
    ) -> None:
        super().__init__(config, mode)
        self.atr_min_pct: float = self.config.get("atr_minimum_pct", 0.15)
        self.atr_valid_pct: float = self.config.get("atr_valid_pct", 0.60)
        self.atr_strong_pct: float = self.config.get(
            "atr_high_confidence_pct", 0.80
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        direction = candidate.direction.value
        bars_5m: pd.DataFrame = ctx.metadata.get("bars_5m", pd.DataFrame())
        session_range = ctx.metadata.get("session_range")
        atr = session_range.ATR if session_range else 0

        if len(bars_5m) < 2 or atr == 0:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="Insufficient data -- advisory pass",
                metrics={"score": 0.3, "atr_pct": 0.0, "strength": "weak"},
            )

        current_price = float(bars_5m["close"].iloc[-1])
        if direction == "short":
            directional_move = float(bars_5m["high"].max()) - current_price
        else:
            directional_move = current_price - float(bars_5m["low"].min())

        consumed_pct = max(directional_move, 0.0) / atr

        if consumed_pct >= self.atr_strong_pct:
            strength = "strong"
            score = 1.0
        elif consumed_pct >= self.atr_valid_pct:
            strength = "valid"
            score = 0.7
        else:
            strength = "weak"
            score = 0.3

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=ATR %.1f%% consumed (%s)",
            self.name, candidate.symbol, consumed_pct * 100, strength,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,  # Advisory -- always passes
            reason=f"ATR {consumed_pct:.1%} consumed ({strength})",
            metrics={
                "score": score,
                "atr_pct": consumed_pct,
                "strength": strength,
            },
        )
