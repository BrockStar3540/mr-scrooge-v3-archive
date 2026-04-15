"""Scan pipeline — the entry evaluation orchestrator.

Replaces V2 coordinator.process_instrument() (lines 291-693) and
the ranking logic (lines 1456-1535).

Flow:
  Market Data → Feature Engine → Context Builder → Classifiers
  → Strategy Router → Strategy Modules → Gate Pipeline
  → V3 Scorer → approved candidate or None
"""

from __future__ import annotations

import logging
from typing import Any

from .events import (
    CANDIDATE_APPROVED,
    CANDIDATE_CREATED,
    CANDIDATE_REJECTED,
    CONTEXT_BUILT,
    FEATURES_COMPUTED,
    STRATEGY_EVALUATED,
    Event,
    EventBus,
)
from .registry import ModuleRegistry
from .strategy_router import StrategyRouter
from .types import (
    FeatureResult,
    MarketSnapshot,
    SymbolContext,
    TradeCandidate,
)

log = logging.getLogger("scrooge_v3.core.scan_pipeline")


class ScanPipeline:
    """Orchestrates the full scan cycle for one symbol.

    Wires together: features → context → classifiers → router → strategies → gates.
    """

    def __init__(
        self,
        registry: ModuleRegistry,
        router: StrategyRouter,
        event_bus: EventBus | None = None,
        gate_pipeline: Any = None,
        scorer: Any = None,
    ):
        self.registry = registry
        self.router = router
        self.event_bus = event_bus
        self.gate_pipeline = gate_pipeline
        self.scorer = scorer

    def scan_symbol(
        self,
        symbol: str,
        snapshot: MarketSnapshot,
        state: dict | None = None,
    ) -> TradeCandidate | None:
        """Run the full scan pipeline for one symbol.

        Returns the best approved candidate, or None.
        """
        state = state or {}

        # 1. Run all active feature modules
        features: dict[str, FeatureResult] = {}
        for entry in self.registry.get_active("features"):
            try:
                result = entry.instance.compute(symbol, snapshot, state)
                features[entry.name] = result
            except Exception:
                log.exception("[SCAN] Feature %s failed for %s", entry.name, symbol)

        self._emit(FEATURES_COMPUTED, symbol=symbol, features=list(features.keys()))

        # 2. Build context
        ctx = SymbolContext(
            symbol=symbol,
            snapshot=snapshot,
            features=features,
            state=state,
        )

        # 3. Run all active classifiers
        for entry in self.registry.get_active("classifiers"):
            try:
                result = entry.instance.classify(ctx)
                ctx.classifications[entry.name] = result
            except Exception:
                log.exception("[SCAN] Classifier %s failed for %s", entry.name, symbol)

        self._emit(CONTEXT_BUILT, symbol=symbol, classifications=list(ctx.classifications.keys()))

        # 4. Route to eligible strategies
        allowed = self.router.get_allowed(ctx)
        if not allowed:
            log.debug("[SCAN] No strategies allowed for %s", symbol)
            return None

        # 5. Evaluate eligible strategies
        candidates: list[TradeCandidate] = []
        for entry in self.registry.get_active("strategies"):
            if entry.name not in allowed:
                continue
            try:
                if entry.instance.eligible(ctx):
                    candidate = entry.instance.evaluate(ctx)
                    if candidate is not None:
                        candidates.append(candidate)
                        self._emit(
                            CANDIDATE_CREATED,
                            symbol=symbol,
                            strategy=entry.name,
                            score=candidate.score,
                        )
            except Exception:
                log.exception("[SCAN] Strategy %s failed for %s", entry.name, symbol)

        self._emit(STRATEGY_EVALUATED, symbol=symbol, candidates=len(candidates))

        if not candidates:
            return None

        # 6. Run gate pipeline on each candidate
        approved: list[TradeCandidate] = []
        for candidate in candidates:
            if self.gate_pipeline is not None:
                gate_result = self.gate_pipeline.evaluate(candidate, ctx)
                if gate_result.all_passed:
                    approved.append(candidate)
                    self._emit(
                        CANDIDATE_APPROVED,
                        symbol=symbol,
                        strategy=candidate.strategy,
                        score=candidate.score,
                    )
                else:
                    self._emit(
                        CANDIDATE_REJECTED,
                        symbol=symbol,
                        strategy=candidate.strategy,
                        reason=gate_result.rejection_reason,
                    )
            else:
                # No gate pipeline registered — pass through
                approved.append(candidate)

        if not approved:
            return None

        # 7. V3 Scorer — re-score gate-approved candidates
        if self.scorer is not None:
            scored: list[TradeCandidate] = []
            for candidate in approved:
                result = self.scorer.score(ctx, candidate)
                if result.tier == "BLOCKED":
                    self._emit(
                        CANDIDATE_REJECTED,
                        symbol=symbol,
                        strategy=candidate.strategy,
                        reason=f"V3_BLOCKED:{','.join(result.blocks)}",
                    )
                    continue
                if result.tier == "REJECT":
                    self._emit(
                        CANDIDATE_REJECTED,
                        symbol=symbol,
                        strategy=candidate.strategy,
                        reason=f"V3_REJECT:score={result.score}",
                    )
                    continue
                # Replace strategy's fixed score with V3 score
                candidate.score = float(result.score)
                candidate.metadata["v3_tier"] = result.tier
                candidate.metadata["v3_breakdown"] = result.breakdown
                candidate.metadata["v3_pairs"] = result.pairs_total
                scored.append(candidate)
            approved = scored

        if not approved:
            return None

        # 8. Select best candidate by score
        best = max(approved, key=lambda c: c.score)
        log.info(
            "[SCAN] APPROVED symbol=%s strategy=%s v3_score=%.0f tier=%s rr=%.2f",
            symbol, best.strategy, best.score,
            best.metadata.get("v3_tier", "?"), best.risk_reward,
        )
        return best

    def scan_universe(
        self,
        symbols: list[str],
        snapshots: dict[str, MarketSnapshot],
        state: dict | None = None,
    ) -> list[TradeCandidate]:
        """Scan all symbols and return ranked candidates."""
        candidates = []
        for symbol in symbols:
            snapshot = snapshots.get(symbol)
            if snapshot is None:
                continue
            candidate = self.scan_symbol(symbol, snapshot, state)
            if candidate is not None:
                candidates.append(candidate)

        # Rank by score descending
        candidates.sort(key=lambda c: c.score, reverse=True)
        return candidates

    def _emit(self, event_type: str, **payload: Any) -> None:
        if self.event_bus:
            self.event_bus.emit(Event(type=event_type, payload=payload))
