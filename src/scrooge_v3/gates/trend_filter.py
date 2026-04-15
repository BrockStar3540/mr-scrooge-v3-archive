"""Trend filter gate -- higher-timeframe trend regime check."""

from __future__ import annotations

from typing import Any

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class TrendFilterGate(BaseGate):
    """Gate 2 -- Trend regime filter.

    Uses 50H EMA slope to classify uptrend / downtrend / ranging.
    Blocks counter-trend trades at low-quality zones (Tier 3+).
    """

    name = "trend_filter"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        direction = candidate.direction.value  # "long" / "short"
        bars_1h: pd.DataFrame = ctx.metadata.get("bars_1h", pd.DataFrame())
        zone_tier: int = ctx.metadata.get("zone_tier", 3)

        regime = self._get_regime(bars_1h)

        counter_trend = (
            (direction == "short" and regime == "uptrend")
            or (direction == "long" and regime == "downtrend")
        )

        if counter_trend and zone_tier >= 3:
            reason = (
                f"Counter-trend: {direction} blocked at Tier {zone_tier}"
                f" in {regime}"
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
                    "score": 0.0,
                    "regime": regime,
                    "direction": direction,
                    "zone_tier": zone_tier,
                    "is_ranging": False,
                    "is_counter_trend": True,
                },
            )

        score = 1.0
        note = f"{regime} -> {direction} allowed"
        if counter_trend:
            score = 0.6
            note = (
                f"Counter-trend {direction} allowed -- Tier {zone_tier}"
                f" overrides {regime}"
            )

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=%s",
            self.name, candidate.symbol, note,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=note,
            metrics={
                "score": score,
                "regime": regime,
                "direction": direction,
                "zone_tier": zone_tier,
                "is_ranging": regime == "ranging",
                "is_counter_trend": counter_trend,
            },
        )

    @staticmethod
    def _get_regime(bars_1h: pd.DataFrame) -> str:
        """50H EMA slope over last 10 bars.

        Returns ``'uptrend'``, ``'downtrend'``, or ``'ranging'``.
        """
        if len(bars_1h) < 62:
            return "ranging"
        closes = bars_1h["close"].values
        ema50 = pd.Series(closes).ewm(span=50, adjust=False).mean().values
        base = ema50[-11]
        if base == 0:
            return "ranging"
        slope = (ema50[-1] - base) / base
        if slope > 0.0005:
            return "uptrend"
        elif slope < -0.0005:
            return "downtrend"
        return "ranging"
