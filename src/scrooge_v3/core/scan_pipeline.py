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
        #    After each feature, propagate key values into state so
        #    downstream features can access them (e.g. OTR needs zone_detector's range_half).
        features: dict[str, FeatureResult] = {}
        for entry in self.registry.get_active("features"):
            try:
                result = entry.instance.compute(symbol, snapshot, state)
                features[entry.name] = result
                # Propagate zone_detector outputs into state for OTR and others
                if entry.name == "zone_detector" and result.values:
                    zm = result.values.get("zone_map")
                    if zm and hasattr(zm, "session_range") and zm.session_range:
                        sr = zm.session_range
                        box_range = sr.PDH - sr.PDL
                        state["range_half"] = box_range / 2
                        state["box_range"] = box_range
                        state["total_overhead"] = snapshot.spread * 2
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
                gate_result = self.gate_pipeline.run(candidate, ctx)
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

                # DBB candidate audit — log every dbb_trend candidate for calibration
                if candidate.strategy == "dbb_trend":
                    self._emit(
                        "DBBCandidateScored",
                        symbol=symbol,
                        strategy=candidate.strategy,
                        direction=candidate.direction.value if hasattr(candidate.direction, 'value') else str(candidate.direction),
                        entry_type=candidate.metadata.get("entry_type", ""),
                        bb_state=candidate.metadata.get("bb_state", ""),
                        base_score=result.base_score,
                        final_score=result.score,
                        tier=result.tier,
                        breakout_level=candidate.metadata.get("breakout_level", 0),
                        pullback_depth_pct=candidate.metadata.get("pullback_depth_pct", 0),
                        rr=round(candidate.risk_reward, 2),
                        management_profile=candidate.metadata.get("management_profile", ""),
                    )
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

    def scan_symbol_full(
        self,
        symbol: str,
        snapshot: MarketSnapshot,
        state: dict | None = None,
    ) -> dict:
        """Run full scan and return ALL intermediate data for dashboard display.

        Returns a dict with features, classifications, gates, scorer, and verdict
        regardless of whether the pair produces a candidate.
        """
        state = state or {}
        report: dict = {
            "symbol": symbol,
            "spread": snapshot.spread,
            "features": {},
            "classifications": {},
            "strategy_allowed": [],
            "gates": {},
            "scorer": {},
            "verdict": "NO_SETUP",
            "candidate": None,
        }

        # 1. Features
        for entry in self.registry.get_active("features"):
            try:
                result = entry.instance.compute(symbol, snapshot, state)
                report["features"][entry.name] = result.values
                if entry.name == "zone_detector" and result.values:
                    zm = result.values.get("zone_map")
                    if zm and hasattr(zm, "session_range") and zm.session_range:
                        sr = zm.session_range
                        box_range = sr.PDH - sr.PDL
                        state["range_half"] = box_range / 2
                        state["box_range"] = box_range
                        state["total_overhead"] = snapshot.spread * 2
            except Exception:
                report["features"][entry.name] = {"error": True}

        # 2. Context + classifiers
        features_typed = {}
        for name, vals in report["features"].items():
            features_typed[name] = FeatureResult(name=name, values=vals if isinstance(vals, dict) else {})
        ctx = SymbolContext(symbol=symbol, snapshot=snapshot, features=features_typed, state=state)
        for entry in self.registry.get_active("classifiers"):
            try:
                result = entry.instance.classify(ctx)
                ctx.classifications[entry.name] = result
                report["classifications"][entry.name] = {"label": result.label, "confidence": result.confidence, "metadata": result.metadata}
            except Exception:
                report["classifications"][entry.name] = {"label": "ERROR", "error": True}

        # 3. Strategy routing
        allowed = self.router.get_allowed(ctx)
        report["strategy_allowed"] = allowed
        if not allowed:
            report["verdict"] = "NO_STRATEGY"
            # Still run scorer for display even without a candidate
            if self.scorer:
                dummy_candidate = TradeCandidate(symbol=symbol, direction="long", strategy="none", entry_price=snapshot.mid, stop_price=snapshot.mid, score=0)
                try:
                    sr = self.scorer.score(ctx, dummy_candidate)
                    report["scorer"] = {"score": sr.score, "tier": sr.tier, "blocks": sr.blocks, "breakdown": sr.breakdown, "pairs_total": sr.pairs_total}
                except Exception:
                    pass
            return report

        # 4. Strategies
        candidates = []
        for entry in self.registry.get_active("strategies"):
            if entry.name not in allowed:
                continue
            try:
                if entry.instance.eligible(ctx):
                    candidate = entry.instance.evaluate(ctx)
                    if candidate is not None:
                        candidates.append(candidate)
            except Exception:
                pass

        if not candidates:
            report["verdict"] = "NO_CANDIDATE"
            if self.scorer:
                dummy_candidate = TradeCandidate(symbol=symbol, direction="long", strategy="none", entry_price=snapshot.mid, stop_price=snapshot.mid, score=0)
                try:
                    sr = self.scorer.score(ctx, dummy_candidate)
                    report["scorer"] = {"score": sr.score, "tier": sr.tier, "blocks": sr.blocks, "breakdown": sr.breakdown, "pairs_total": sr.pairs_total}
                except Exception:
                    pass
            return report

        # 5. Gates
        best_candidate = candidates[0]
        if self.gate_pipeline:
            gate_result = self.gate_pipeline.run(best_candidate, ctx)
            if hasattr(gate_result, "results"):
                for gr in gate_result.results:
                    report["gates"][gr.gate_name] = {"passed": gr.passed, "reason": gr.reason, "metrics": gr.metrics}
            if not gate_result.all_passed:
                report["verdict"] = "GATE_REJECTED"
                report["gates"]["_rejection"] = gate_result.rejection_reason
                # Still run scorer for display
                if self.scorer:
                    try:
                        sr = self.scorer.score(ctx, best_candidate)
                        report["scorer"] = {"score": sr.score, "tier": sr.tier, "blocks": sr.blocks, "breakdown": sr.breakdown, "pairs_total": sr.pairs_total}
                    except Exception:
                        pass
                return report

        # 6. Scorer
        if self.scorer:
            try:
                sr = self.scorer.score(ctx, best_candidate)
                report["scorer"] = {"score": sr.score, "tier": sr.tier, "blocks": sr.blocks, "breakdown": sr.breakdown, "pairs_total": sr.pairs_total}
                if sr.tier == "BLOCKED":
                    report["verdict"] = f"V3_BLOCKED"
                elif sr.tier == "REJECT":
                    report["verdict"] = f"V3_REJECT"
                elif sr.tier in ("A", "B"):
                    report["verdict"] = f"TAKE_{sr.tier}"
                    best_candidate.score = float(sr.score)
                    best_candidate.metadata["v3_tier"] = sr.tier
                    best_candidate.metadata["v3_breakdown"] = sr.breakdown
                    report["candidate"] = best_candidate
            except Exception:
                pass

        return report

    def scan_universe(
        self,
        symbols: list[str],
        snapshots: dict[str, MarketSnapshot],
        state: dict | None = None,
    ) -> tuple[list[TradeCandidate], list[dict]]:
        """Scan all symbols. Returns (ranked candidates, all pair reports)."""
        candidates = []
        reports = []
        for symbol in symbols:
            snapshot = snapshots.get(symbol)
            if snapshot is None:
                continue
            report = self.scan_symbol_full(symbol, snapshot, state.copy() if state else None)
            reports.append(report)
            if report.get("candidate") is not None:
                candidates.append(report["candidate"])

        candidates.sort(key=lambda c: c.score, reverse=True)
        return candidates, reports

    def _emit(self, event_type: str, **payload: Any) -> None:
        if self.event_bus:
            self.event_bus.emit(Event(type=event_type, payload=payload))
