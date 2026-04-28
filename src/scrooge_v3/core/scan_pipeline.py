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
        ml_filter: Any = None,
    ):
        self.registry = registry
        self.router = router
        self.event_bus = event_bus
        self.gate_pipeline = gate_pipeline
        self.scorer = scorer
        # Post-scorer per-strategy ML gate. None = disabled (no-op).
        self.ml_filter = ml_filter

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

                # ML strategy filter (post-scorer). Predicts P(win) for
                # opt-in strategies. Mode=observe logs only; mode=hard
                # actually drops candidates below threshold.
                if self.ml_filter is not None:
                    ml = self.ml_filter.evaluate(symbol, candidate, ctx, result)
                    candidate.metadata["ml_filter"] = ml
                    if ml.get("vetoed"):
                        self._emit(
                            CANDIDATE_REJECTED,
                            symbol=symbol,
                            strategy=candidate.strategy,
                            reason=f"ML_FILTER:{ml.get('reason','low_p')}",
                        )
                        continue
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

        # Build per-candidate records that we'll enrich as we walk the
        # pipeline (gates -> scorer). The trainer persists this so it can
        # reason about winners AND losers from the same scan.
        candidate_records: list[dict] = []
        for c in candidates:
            candidate_records.append({
                "strategy": c.strategy,
                "strategy_family": (c.metadata or {}).get("strategy_family", ""),
                "direction": c.direction.value if hasattr(c.direction, 'value') else str(c.direction),
                "entry_price": float(c.entry_price or 0.0),
                "stop_price": float(c.stop_price or 0.0),
                "take_profit": float(c.take_profit) if c.take_profit else None,
                "risk_reward": round(float(c.risk_reward or 0.0), 3),
                "metadata": dict(c.metadata or {}),
                "gates": {},
                "gate_passed": None,
                "gate_rejection_reason": None,
                "scorer": None,
                "scorer_tier": None,
                "score": None,
                "selected_by_runtime": False,  # filled in at the very end
            })
        # Backward-compat lightweight view (existing dashboard uses this).
        report["candidates_by_strategy"] = [
            {"strategy": r["strategy"], "direction": r["direction"],
             "entry": r["entry_price"], "stop": r["stop_price"], "rr": r["risk_reward"],
             "family": r["strategy_family"]}
            for r in candidate_records
        ]

        if not candidates:
            report["verdict"] = "NO_CANDIDATE"
            if self.scorer:
                dummy_candidate = TradeCandidate(symbol=symbol, direction="long", strategy="none", entry_price=snapshot.mid, stop_price=snapshot.mid, score=0)
                try:
                    sr = self.scorer.score(ctx, dummy_candidate)
                    report["scorer"] = {"score": sr.score, "tier": sr.tier, "blocks": sr.blocks, "breakdown": sr.breakdown, "pairs_total": sr.pairs_total}
                except Exception:
                    pass
            report["all_candidates"] = candidate_records
            return report

        # 5. Gates — run on ALL candidates (mirrors live scan_symbol path)
        gate_approved = []
        gate_rejected = []
        for i, candidate in enumerate(candidates):
            rec = candidate_records[i]
            if self.gate_pipeline:
                gate_result = self.gate_pipeline.run(candidate, ctx)
                # Per-candidate gate results into the record
                if hasattr(gate_result, "gates"):
                    rec["gates"] = {
                        gr.gate_name: {
                            "passed": gr.passed, "reason": gr.reason,
                            "mode": gr.mode.value if hasattr(gr.mode, "value") else str(gr.mode),
                            "metrics": dict(gr.metrics or {}),
                        }
                        for gr in gate_result.gates
                    }
                rec["gate_passed"] = bool(gate_result.all_passed)
                rec["gate_rejection_reason"] = (
                    gate_result.rejection_reason if not gate_result.all_passed else None
                )
                # Display report keeps first-candidate snapshot for backward compat
                if not report["gates"] and rec["gates"]:
                    report["gates"] = dict(rec["gates"])
                if gate_result.all_passed:
                    gate_approved.append(candidate)
                else:
                    gate_rejected.append({"strategy": candidate.strategy, "reason": gate_result.rejection_reason})
            else:
                rec["gate_passed"] = True
                gate_approved.append(candidate)

        if not gate_approved:
            report["verdict"] = "GATE_REJECTED"
            report["gates"]["_rejection"] = gate_rejected[0]["reason"] if gate_rejected else "unknown"
            # Still run scorer on first candidate for display
            if self.scorer and candidates:
                try:
                    sr = self.scorer.score(ctx, candidates[0])
                    report["scorer"] = {"score": sr.score, "tier": sr.tier, "blocks": sr.blocks, "breakdown": sr.breakdown, "pairs_total": sr.pairs_total}
                except Exception:
                    pass
            return report

        # Index for writing per-candidate scorer result back into records
        idx_by_obj = {id(c): i for i, c in enumerate(candidates)}

        # 6. Scorer — score ALL gate-approved candidates, pick best
        if self.scorer:
            scored = []
            best_score_result = None
            for candidate in gate_approved:
                try:
                    sr = self.scorer.score(ctx, candidate)
                    rec = candidate_records[idx_by_obj[id(candidate)]]
                    rec["scorer"] = {
                        "score": float(sr.score), "tier": str(sr.tier),
                        "blocks": list(sr.blocks or []),
                        "breakdown": dict(sr.breakdown or {}),
                        "pairs_total": getattr(sr, "pairs_total", None),
                        "base_score": getattr(sr, "base_score", None),
                    }
                    rec["scorer_tier"] = str(sr.tier)
                    rec["score"] = float(sr.score)
                    # Track scorer result for the best candidate (for report display)
                    if best_score_result is None or sr.score > best_score_result.score:
                        best_score_result = sr
                        report["scorer"] = {"score": sr.score, "tier": sr.tier, "blocks": sr.blocks, "breakdown": sr.breakdown, "pairs_total": sr.pairs_total}
                    if sr.tier in ("A", "B"):
                        candidate.score = float(sr.score)
                        candidate.metadata["v3_tier"] = sr.tier
                        candidate.metadata["v3_breakdown"] = sr.breakdown
                        scored.append(candidate)
                except Exception:
                    pass

            if not scored:
                # All candidates blocked/rejected by scorer
                if best_score_result:
                    if best_score_result.tier == "BLOCKED":
                        report["verdict"] = "V3_BLOCKED"
                    else:
                        report["verdict"] = "V3_REJECT"
                report["all_candidates"] = candidate_records
                return report

            # Pick actual winner (same as live path)
            winner = max(scored, key=lambda c: c.score)
            report["verdict"] = f"TAKE_{winner.metadata.get('v3_tier', 'B')}"
            report["candidate"] = winner
            # Mark selected_by_runtime on the winning record
            wi = idx_by_obj.get(id(winner))
            if wi is not None:
                candidate_records[wi]["selected_by_runtime"] = True
        else:
            # No scorer — pick by strategy score
            winner = max(gate_approved, key=lambda c: c.score)
            report["verdict"] = "TAKE_UNSCORED"
            report["candidate"] = winner
            wi = idx_by_obj.get(id(winner))
            if wi is not None:
                candidate_records[wi]["selected_by_runtime"] = True

        report["all_candidates"] = candidate_records
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
