"""Feature-quality floor — block candidates on symbols with missing
critical features (insufficient bars, zone-map empty, etc.).

When a feature calculator hits insufficient data it returns degraded
defaults (EMA=0, RSI=50, zone_map={}) and now flags values["_degraded"]
= True. Without this gate those defaults flow into the v3_scorer and
strategy emissions as if they were real, producing junk scores and
falsely-confident emissions on under-warmed-up symbols.

Brock 2026-05-25.
"""
from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class FeatureQualityFloorGate(BaseGate):
    """Block candidates when any critical feature reports _degraded."""

    name = "feature_quality_floor"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        # Critical features that, if degraded, mean the symbol shouldn\'t trade
        # this cycle. Scorer + strategies depend on these.
        default_critical = ["ema", "rsi", "zone_detector"]
        self.critical_features: list[str] = list(
            self.config.get("critical_features", default_critical)
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        degraded = []
        for name in self.critical_features:
            fr = ctx.features.get(name)
            if fr is None:
                degraded.append(f"{name}:missing")
                continue
            vals = getattr(fr, "values", None) or {}
            if vals.get("_degraded"):
                degraded.append(f"{name}:degraded")

        if degraded:
            reason = "degraded_features:" + ",".join(degraded)
            self._log.info(
                "[GATE:%s] FAILED symbol=%s strategy=%s reason=%s",
                self.name, candidate.symbol, candidate.strategy, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={"degraded_count": len(degraded)},
            )

        return GateResult(
            gate_name=self.name,
            passed=True,
            reason="features_ok",
            metrics={"score": 1.0, "degraded_count": 0},
        )
