"""Base gate class and pipeline result container."""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate


@dataclass
class GatePipelineResult:
    """Aggregated result from running all gates in sequence."""

    symbol: str
    all_passed: bool = True
    gates: list[GateResult] = field(default_factory=list)
    rejection_reason: str = ""
    aggregate_score: float = 0.0

    def append(self, result: GateResult) -> None:
        self.gates.append(result)
        if not result.passed and result.mode == GateMode.HARD and self.all_passed:
            self.all_passed = False
            self.rejection_reason = f"[{result.gate_name}] {result.reason}"
        # Recompute aggregate score from passing gates
        passing = [g for g in self.gates if g.passed]
        self.aggregate_score = (
            sum(g.metrics.get("score", 0.0) for g in passing) / len(passing)
            if passing
            else 0.0
        )

    def gate(self, name: str) -> GateResult | None:
        """Retrieve a specific gate result by name."""
        return next((g for g in self.gates if g.gate_name == name), None)


class BaseGate(ABC):
    """Abstract base for all gate implementations.

    Implements the ``GateModule`` protocol from ``core.contracts``.
    Subclasses must set ``name`` and implement ``evaluate()``.
    """

    name: str = "unnamed"
    mode: GateMode = GateMode.HARD

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        self.config = config or {}
        self.mode = mode
        self._log = logging.getLogger(f"scrooge_v3.gate.{self.name}")

    @abstractmethod
    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        """Evaluate the gate for a candidate trade.

        Must never raise -- catch all exceptions and return a failed GateResult.
        """
        ...

    def safe_evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        """Wraps evaluate() with timing, error capture, and mode tagging."""
        start = time.monotonic()
        try:
            result = self.evaluate(candidate, ctx)
            elapsed_ms = (time.monotonic() - start) * 1000
            result.mode = self.mode
            result.metrics["latency_ms"] = elapsed_ms
            return result
        except Exception as exc:
            elapsed_ms = (time.monotonic() - start) * 1000
            reason = f"Gate exception: {exc}"
            self._log.exception(
                "[GATE:%s] FAILED symbol=%s reason=%s",
                self.name,
                candidate.symbol,
                reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                mode=self.mode,
                reason=reason,
                metrics={"latency_ms": elapsed_ms},
            )
