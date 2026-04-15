"""Module contracts — the formal interfaces every plug-in must satisfy."""

from __future__ import annotations

from typing import Protocol

from .types import (
    AdvisorResult,
    ClassificationResult,
    FeatureResult,
    GateResult,
    HealthStatus,
    MarketSnapshot,
    OrderPlan,
    PositionState,
    StopPlan,
    SymbolContext,
    TradeCandidate,
)


class FeatureModule(Protocol):
    """Computes reusable facts from market data. Does not trade."""

    name: str

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult: ...


class ClassifierModule(Protocol):
    """Classifies market state (regime, BB, opening, structure, volatility)."""

    name: str

    def classify(self, ctx: SymbolContext) -> ClassificationResult: ...


class StrategyModule(Protocol):
    """Pluggable trading engine."""

    name: str

    def eligible(self, ctx: SymbolContext) -> bool: ...

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None: ...


class GateModule(Protocol):
    """Ordered filter in the gate pipeline. Each is optional and removable."""

    name: str

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult: ...


class ExecutionPolicy(Protocol):
    """Plans entries and stop updates."""

    name: str

    def plan_entry(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> OrderPlan: ...

    def plan_stop_update(
        self, position: PositionState, ctx: SymbolContext
    ) -> StopPlan: ...


class AdvisorModule(Protocol):
    """Optional ML/LLM/heuristic advisor. Never bypasses hard risk controls."""

    name: str

    def advise(
        self, ctx: SymbolContext, candidate: TradeCandidate | None
    ) -> AdvisorResult: ...


class HealthCheckModule(Protocol):
    """Health probe for any module."""

    name: str

    def probe(self) -> HealthStatus: ...
