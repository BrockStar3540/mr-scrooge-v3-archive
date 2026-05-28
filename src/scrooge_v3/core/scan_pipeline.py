"""Scan pipeline — the entry evaluation orchestrator.

Replaces V2 coordinator.process_instrument() (lines 291-693) and
the ranking logic (lines 1456-1535).

Flow:
  Market Data → Feature Engine → Context Builder → Classifiers
  → Strategy Router → Strategy Modules → Gate Pipeline
  → V3 Scorer → approved candidate or None
"""

from __future__ import annotations

import json
import logging
import os
import random
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
# 2026-05-28 (Brock): ML router replaces strategy_router for allowed-set selection
from scrooge_v3.strategies import ml_router  # noqa: E402
from scrooge_v3.advisors import lightgbm_shadow  # noqa: E402
from .types import (
    FeatureResult,
    MarketSnapshot,
    SymbolContext,
    TradeCandidate,
)

log = logging.getLogger("scrooge_v3.core.scan_pipeline")


# Soft-deprioritize cache (Brock 2026-05-20): tuples with no bank coverage
# get a 20% sampling rate to save scan effort while preserving telemetry.
# File is reloaded automatically when mtime changes.
_DEPRIO_CACHE: dict = {"mtime": 0.0, "tuples": set(), "sample_rate": 1.0,
                       "logged_skips": 0}


def _load_deprioritize() -> tuple[set, float]:
    """Return (deprioritize_tuples, sample_rate). Empty on missing/error."""
    path = "data/router_deprioritize.json"
    try:
        mt = os.path.getmtime(path)
    except OSError:
        return set(), 1.0
    if _DEPRIO_CACHE["mtime"] != mt:
        try:
            with open(path) as f:
                cfg = json.load(f)
            tuples = {(t["regime53"], t["pair"], t["direction"])
                      for t in cfg.get("tuples", [])}
            rate = float(cfg.get("sample_rate", 0.20))
            _DEPRIO_CACHE["tuples"] = tuples
            _DEPRIO_CACHE["sample_rate"] = rate
            _DEPRIO_CACHE["mtime"] = mt
            log.info(
                "[ROUTER] deprioritize list loaded: %d tuples, sample_rate=%.2f",
                len(tuples), rate,
            )
        except Exception as exc:
            log.exception("[ROUTER] failed to load deprioritize list: %s", exc)
            return set(), 1.0
    return _DEPRIO_CACHE["tuples"], _DEPRIO_CACHE["sample_rate"]



def _synthesize_session_thresholds(scorer, family: str) -> dict:
    """Return {session, fam, floor, b, a, cap} for the current scan moment.
    Uses scorer's clock when available; falls back to UTC-now."""
    try:
        from scrooge_v3.core.clock import compat_threshold_profile, session_label_from_utc
        from datetime import datetime, timezone
        clock = getattr(scorer, "clock", None) if scorer is not None else None
        if clock is not None and hasattr(clock, "session_label"):
            label = clock.session_label()
        else:
            label = session_label_from_utc(datetime.now(timezone.utc))
        profile = compat_threshold_profile(label, family=family or "default")
        return {
            "session": label.value if hasattr(label, "value") else str(label),
            "fam": family or "default",
            "floor": profile.base_floor,
            "b": profile.b_tier,
            "a": profile.a_tier,
            "cap": profile.pair_cap,
        }
    except Exception:
        return {}


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
        branch_router: Any = None,
    ):
        self.registry = registry
        self.router = router
        self.event_bus = event_bus
        self.gate_pipeline = gate_pipeline
        self.scorer = scorer
        # Post-scorer per-strategy ML gate. None = disabled (no-op).
        self.ml_filter = ml_filter
        # Pre-gate branch router (box/dbb/freeze/unclear). None = disabled.
        self.branch_router = branch_router

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
        # 2026-05-28 (Brock): ML pre-router (per-pair WIN rules) replaces
        # strategy_router. Returns set of strategy names whose rules say
        # they can fire in the current (regime, session, bucket) state.
        _all_strats = {e.name for e in self.registry.get_active('strategies')}
        allowed = ml_router.get_allowed_or_all(symbol, ctx, _all_strats)
        if not allowed:
            log.debug("[SCAN] No strategies allowed for %s", symbol)
            return None

        # 5. Evaluate eligible strategies
        candidates: list[TradeCandidate] = []
        for entry in self.registry.get_active("strategies"):
            entry_family = getattr(entry.instance, "_family", None)
            if entry.name not in allowed and entry_family not in allowed:
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

        # 5b. Branch router (pre-gate). Decides which family should own this
        # timestamp. Observe-mode logs only; hard-mode filters out candidates
        # from non-routed branches.
        if self.branch_router is not None:
            try:
                rr_decision = self.branch_router.decide(ctx, candidates)
                for c in candidates:
                    c.metadata["branch_router"] = rr_decision
                kept = self.branch_router.filter_candidates(candidates, rr_decision)
                if len(kept) < len(candidates):
                    log.info("[ROUTER] %s: filtered %d -> %d (decision=%s)",
                             symbol, len(candidates), len(kept), rr_decision.get("decision"))
                candidates = kept
                if not candidates:
                    return None
            except Exception:
                log.exception("[ROUTER] branch_router.decide raised; ignoring")

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

        # 7. V3 Scorer — archived 2026-05-28 (see archived/v3_scorer_2026-05-28/).
        # ML routing is the sole admit decision; strategies emit their own
        # scores; best-by-score selection at step 8 ranks among approved
        # candidates. No re-scoring layer.

        if not approved:
            return None

        # 8. Select best candidate by score
        best = max(approved, key=lambda c: c.score)
        log.info(
            "[SCAN] APPROVED symbol=%s strategy=%s v3_score=%.0f tier=%s rr=%.2f",
            symbol, best.strategy, best.score,
            best.metadata.get("v3_tier", "?"), best.risk_reward,
        )
        # LightGBM shadow scorer (Brock 2026-05-28): observe-only logging
        # of P(win) for the selected candidate. Never blocks, never alters
        # routing. Reads `data/lightgbm_shadow.jsonl` for offline eval.
        try:
            lightgbm_shadow.observe(symbol, ctx, best, all_candidates=approved)
        except Exception:
            pass
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
        # 2026-05-28 (Brock): ML pre-router (per-pair WIN rules) replaces
        # strategy_router. Returns set of strategy names whose rules say
        # they can fire in the current (regime, session, bucket) state.
        _all_strats = {e.name for e in self.registry.get_active('strategies')}
        allowed = ml_router.get_allowed_or_all(symbol, ctx, _all_strats)
        report["strategy_allowed"] = allowed
        if not allowed:
            report["verdict"] = "NO_STRATEGY"
            # Still run scorer for display even without a candidate
            if self.scorer:
                dummy_candidate = TradeCandidate(symbol=symbol, direction="long", strategy="none", entry_price=snapshot.mid, stop_price=snapshot.mid, score=0)
                try:
                    sr = self.scorer.score(ctx, dummy_candidate)
                    _st = _synthesize_session_thresholds(self.scorer, "default")
                    report["scorer"] = {
                        "score": sr.score, "tier": sr.tier,
                        "blocks": sr.blocks, "breakdown": sr.breakdown,
                        "pairs_total": sr.pairs_total,
                        "base_score": getattr(sr, "base_score", 0),
                        "fam": _st.get("fam", ""), "session": _st.get("session", ""),
                        "floor": _st.get("floor", 0), "b": _st.get("b", 0),
                        "a": _st.get("a", 0), "cap": _st.get("cap", 0),
                    }
                except Exception:
                    pass
            return report

        # 4. Strategies
        candidates = []
        for entry in self.registry.get_active("strategies"):
            entry_family = getattr(entry.instance, "_family", None)
            if entry.name not in allowed and entry_family not in allowed:
                continue
            try:
                if entry.instance.eligible(ctx):
                    candidate = entry.instance.evaluate(ctx)
                    if candidate is not None:
                        candidates.append(candidate)
            except Exception:
                pass

        # 4.5 Soft-deprioritize (Brock 2026-05-20): drop candidates whose
        # (regime53, pair, direction) tuple has no bank coverage at any
        # tier. Sample at 20% so telemetry continues to detect regime
        # drift / new evidence. Cuts ~half the scan effort on tuples
        # the validated bank says are dead.
        if candidates:
            dep_tuples, dep_rate = _load_deprioritize()
            if dep_tuples:
                rc = ctx.classifications.get("technical_regime_53")
                regime_label = rc.label if rc else None
                if regime_label is None:
                    rfeat = ctx.features.get("technical_regime_53")
                    if rfeat is not None:
                        vals = getattr(rfeat, "values", {}) or {}
                        regime_label = vals.get("technical_regime_53")
                if regime_label:
                    kept = []
                    for c in candidates:
                        d = c.direction.value if hasattr(c.direction, "value") else str(c.direction)
                        if (regime_label, symbol, d) in dep_tuples and random.random() >= dep_rate:
                            _DEPRIO_CACHE["logged_skips"] += 1
                            if _DEPRIO_CACHE["logged_skips"] % 50 == 1:
                                log.info(
                                    "[ROUTER] deprioritized_sampled_out symbol=%s regime=%s direction=%s (logged 1/50)",
                                    symbol, regime_label, d,
                                )
                            continue
                        kept.append(c)
                    candidates = kept

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
                    _st = _synthesize_session_thresholds(self.scorer, "default")
                    report["scorer"] = {
                        "score": sr.score, "tier": sr.tier,
                        "blocks": sr.blocks, "breakdown": sr.breakdown,
                        "pairs_total": sr.pairs_total,
                        "base_score": getattr(sr, "base_score", 0),
                        "fam": _st.get("fam", ""), "session": _st.get("session", ""),
                        "floor": _st.get("floor", 0), "b": _st.get("b", 0),
                        "a": _st.get("a", 0), "cap": _st.get("cap", 0),
                    }
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
                    _st = _synthesize_session_thresholds(self.scorer, "default")
                    report["scorer"] = {
                        "score": sr.score, "tier": sr.tier,
                        "blocks": sr.blocks, "breakdown": sr.breakdown,
                        "pairs_total": sr.pairs_total,
                        "base_score": getattr(sr, "base_score", 0),
                        "fam": _st.get("fam", ""), "session": _st.get("session", ""),
                        "floor": _st.get("floor", 0), "b": _st.get("b", 0),
                        "a": _st.get("a", 0), "cap": _st.get("cap", 0),
                    }
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
                        _st = _synthesize_session_thresholds(self.scorer, "default")
                    report["scorer"] = {
                        "score": sr.score, "tier": sr.tier,
                        "blocks": sr.blocks, "breakdown": sr.breakdown,
                        "pairs_total": sr.pairs_total,
                        "base_score": getattr(sr, "base_score", 0),
                        "fam": _st.get("fam", ""), "session": _st.get("session", ""),
                        "floor": _st.get("floor", 0), "b": _st.get("b", 0),
                        "a": _st.get("a", 0), "cap": _st.get("cap", 0),
                    }
                    # SCORER VETO REMOVED 2026-05-27 (Brock'"'"'s call).
                    # The v3_scorer is now PURELY a ranker — BLOCKED + REJECT
                    # tiers no longer veto candidates. Score still attaches
                    # so max(approved, key=c.score) selection works.
                    if sr.tier in ("BLOCKED", "REJECT"):
                        log.info(
                            "[V3_SCORER] scorer_bypassed_brock_2026_05_27 "
                            "symbol=%s strategy=%s tier=%s score=%d "
                            "(would_have_killed_old_floor)",
                            candidate.symbol, candidate.strategy, sr.tier, sr.score,
                        )
                        candidate.metadata["v3_bypassed_by_brock_override"] = True
                        candidate.metadata["v3_would_have_rejected_at"] = sr.score
                    candidate.score = float(sr.score)
                    candidate.metadata["v3_tier"] = sr.tier
                    candidate.metadata["v3_breakdown"] = sr.breakdown
                    scored.append(candidate)
                except Exception:
                    log.exception("[SCAN_FULL] scorer step failed for %s", candidate.symbol)

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
