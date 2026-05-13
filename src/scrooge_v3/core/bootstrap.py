"""Bootstrap — initializes all engines and returns a RuntimeContext.

Extracted from Runtime.boot() to keep runtime.py as a thin conductor.
All module registration, config validation, broker init, state restore,
and reconciliation happens here.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

from .config import ConfigStore
from .events import EventBus
from .registry import ModuleRegistry
from .runtime_context import RuntimeContext
from .scan_pipeline import ScanPipeline
from .state_controller import StateController
from .strategy_router import StrategyRouter

log = logging.getLogger("scrooge_v3.core.bootstrap")


class BootFailure(Exception):
    """Raised when boot cannot complete."""
    pass


def build_runtime(config: ConfigStore, live_state: Any = None) -> RuntimeContext:
    """Boot all engines, validate config, return a fully wired RuntimeContext.

    Raises BootFailure if any critical step fails.
    """
    log.info("[BOOT] Starting V3 bootstrap...")

    event_bus = EventBus()
    registry = ModuleRegistry()
    persist_path = Path(config.get("runtime.state_file", "data/state.json"))
    state = StateController(
        config=config.section("risk") | config.section("runtime"),
        persist_path=persist_path,
    )
    router = StrategyRouter()
    scan_pipeline = ScanPipeline(
        registry=registry,
        router=router,
        event_bus=event_bus,
    )

    # --- Validate config ---
    config.apply_env_overrides()
    errors = config.validate()
    if errors:
        for e in errors:
            log.error("[BOOT] Config error: %s", e)
        raise BootFailure(f"Config validation failed: {errors}")
    log.info("[BOOT] Config validated OK")

    # --- Wire config hot reload ---
    config.start_watcher()

    # --- Broker adapter ---
    broker = _init_broker(config)
    if broker is None:
        raise BootFailure("Broker init failed")

    # --- Register features ---
    from scrooge_v3.features import (
        ATRCalculator, BollingerCalculator, EMACalculator,
        OverheadRatioCalculator, RSICalculator, TechnicalContextCalculator,
        VolumeCalculator, ZoneDetector,
    )
    feat_cfg = config.section("features")
    registry.register("features", "atr", ATRCalculator(feat_cfg.get("atr", {})))
    registry.register("features", "bollinger", BollingerCalculator(feat_cfg.get("bollinger", {})))
    registry.register("features", "zone_detector", ZoneDetector(feat_cfg.get("zone_detector", {})))
    registry.register("features", "otr", OverheadRatioCalculator())
    registry.register("features", "ema", EMACalculator(feat_cfg.get("ema", {})))
    registry.register("features", "rsi", RSICalculator(feat_cfg.get("rsi", {})))
    registry.register("features", "volume", VolumeCalculator(feat_cfg.get("volume", {})))
    registry.register(
        "features",
        "technical_context",
        TechnicalContextCalculator(feat_cfg.get("technical_context", {})),
    )

    # --- Register classifiers ---
    from scrooge_v3.classifiers.bb_state import BollingerStateClassifier
    from scrooge_v3.classifiers.regime import RegimeClassifier
    from scrooge_v3.classifiers.opening import OpeningStateClassifier
    from scrooge_v3.classifiers.structure import StructureClassifier

    registry.register("classifiers", "bb_state", BollingerStateClassifier())
    registry.register("classifiers", "regime", RegimeClassifier())
    registry.register("classifiers", "opening_state", OpeningStateClassifier())
    registry.register("classifiers", "structure", StructureClassifier())

    # --- Register strategies ---
    from scrooge_v3.strategies import ReversalStrategy, TrendStrategy, DBBTrendStrategy, V3HybridScorer
    from scrooge_v3.strategies.direct_entry import DirectEntryStrategy

    strat_cfg = config.section("strategies")
    registry.register("strategies", "reversal", ReversalStrategy(strat_cfg.get("reversal", {})))
    registry.register("strategies", "trend", TrendStrategy(strat_cfg.get("trend", {})))
    registry.register("strategies", "direct", DirectEntryStrategy(strat_cfg.get("direct", {})))
    registry.register("strategies", "dbb_trend", DBBTrendStrategy(strat_cfg.get("dbb_trend", {})))

    # --- Build cooldown tracker (Phase 4 Signal Discipline) ---
    from scrooge_v3.risk.cooldown_tracker import CooldownTracker

    risk_cfg = config.section("risk") or {}
    cooldown_tracker = CooldownTracker(
        config=risk_cfg,
        data_dir=Path("data"),
    )

    # --- Register gates ---
    # Order matters: daily_circuit FIRST (cheapest, hardest veto), then
    # cooldown / debounce / expiry_backoff (risk-discipline vetoes), then
    # regime_floor and the rest.
    from scrooge_v3.gates import (
        BoxV3ShadowGate, CooldownGate, DailyCircuitGate, DebounceGate,
        ExpiryBackoffGate, RegimeCompatGate, RegimeFloorGate, ZoneEntryCapGate,
    )
    from scrooge_v3.core.types import GateMode
    from scrooge_v3.gates.pipeline import GatePipeline

    gate_cfg = config.section("gates")
    gate_pipeline = GatePipeline()
    gate_pipeline.register_many([
        DailyCircuitGate(),
        CooldownGate(risk_cfg),
        DebounceGate({
            **gate_cfg.get("debounce", {}),
            "zone_blacklist_hours": risk_cfg.get("zone_blacklist_hours", 4),
            "zone_bucket_pips": risk_cfg.get("zone_bucket_pips", 20),
        }),
        ExpiryBackoffGate({
            "zone_bucket_pips": risk_cfg.get("zone_bucket_pips", 20),
        }),
        RegimeFloorGate({"min_score": -4}),
        ZoneEntryCapGate(gate_cfg.get("zone_entry_cap", {})),
        # Observe-only regime compatibility classifier. Never blocks; emits
        # (regime × family × dir_vs_hint) recommendation for audit-trail
        # analysis. Promote to HARD only after held-out validation.
        RegimeCompatGate(mode=GateMode.OBSERVE),
        # Observe-only shadow of frozen box v3 gate tree (from trainer repo
        # 19ada0e: docs/box_gate_tree.md + data/regimes/box_gate_v3.yaml).
        # Emits would_allow / ranking_score / tier per candidate; never rejects.
        BoxV3ShadowGate(mode=GateMode.OBSERVE),
    ])

    # --- Wire scorer and gate pipeline into scan pipeline ---
    scorer = V3HybridScorer(config.section("scoring"))
    scan_pipeline.gate_pipeline = gate_pipeline
    scan_pipeline.scorer = scorer

    # --- ML strategy filter (post-scorer, per-strategy XGBoost) ---
    # Off by default. Enable via config.scoring.ml_filter = {mode: "observe" | "hard"}
    ml_cfg = config.section("scoring").get("ml_filter") if config.get("scoring") else None
    if ml_cfg and ml_cfg.get("enabled"):
        from scrooge_v3.gates.ml_strategy_filter import MLStrategyFilter
        repo_root = Path(__file__).resolve().parent.parent.parent.parent
        scan_pipeline.ml_filter = MLStrategyFilter(
            repo_root=repo_root,
            mode=ml_cfg.get("mode", "observe"),
            model_map=ml_cfg.get("model_map"),
            thresholds=ml_cfg.get("thresholds"),
        )
        log.info("[BOOT] ML strategy filter ENABLED (mode=%s)", ml_cfg.get("mode", "observe"))
    else:
        log.info("[BOOT] ML strategy filter disabled")

    # --- Branch router (pre-gate; box/dbb/freeze/unclear) ---
    br_cfg = config.section("scoring").get("branch_router") if config.get("scoring") else None
    if br_cfg and br_cfg.get("enabled"):
        from scrooge_v3.advisors.branch_router import BranchRouter
        repo_root = Path(__file__).resolve().parent.parent.parent.parent
        scan_pipeline.branch_router = BranchRouter(
            repo_root=repo_root,
            mode=br_cfg.get("mode", "observe"),
            model_path=br_cfg.get("model_path", "data/ml-observer-offline/models/branch_router_T0.xgb"),
            thresholds=br_cfg.get("thresholds"),
        )
        log.info("[BOOT] Branch router ENABLED (mode=%s)", br_cfg.get("mode", "observe"))
    else:
        log.info("[BOOT] Branch router disabled")

    # --- Position pipeline ---
    from scrooge_v3.core.position_pipeline import PositionPipeline
    from scrooge_v3.management.trail import TrailManager
    from scrooge_v3.management.ratchet import RatchetManager
    from scrooge_v3.management.be_manager import BreakEvenManager
    from scrooge_v3.management.partial_harvest import PartialHarvestManager
    from scrooge_v3.management.emergency_close import EmergencyCloseManager
    from scrooge_v3.execution.stop_planner import StopPlanner
    from scrooge_v3.telemetry.execution_audit import ExecutionAudit
    from scrooge_v3.telemetry.dbb_candidate_audit import DBBCandidateAudit
    from scrooge_v3.telemetry.order_attribution import OrderAttributionWriter

    mgmt_cfg = config.section("management") if config.get("management") else {}
    exit_cfg = mgmt_cfg.get("exit_manager", {})
    execution_audit = ExecutionAudit(filepath="data/execution-audit.jsonl")
    dbb_audit = DBBCandidateAudit(filepath="data/dbb-candidate-audit.jsonl")
    # Patch B.right: order_id → strategy attribution map
    order_attribution = OrderAttributionWriter(
        filepath="data/order-attribution.jsonl",
    )

    # Subscribe to DBB candidate events
    def _on_dbb_scored(event):
        from datetime import datetime, timezone
        p = event.payload
        h = datetime.now(timezone.utc).hour
        if h >= 20: session = 'dead_late'
        elif h >= 18: session = 'late_ny'
        elif h >= 12: session = 'ny_active'
        elif h >= 8: session = 'london'
        else: session = 'asia_london_open'
        p['session'] = session
        dbb_audit.record(p)
    event_bus.subscribe('DBBCandidateScored', _on_dbb_scored)

    position_pipeline = PositionPipeline(
        trail_manager=TrailManager(mgmt_cfg.get("trail", {})),
        ratchet_manager=RatchetManager(mgmt_cfg.get("ratchet", {})),
        be_manager=BreakEvenManager(mgmt_cfg.get("break_even", {})),
        harvest_manager=PartialHarvestManager(mgmt_cfg.get("harvest", {})),
        emergency_manager=EmergencyCloseManager(mgmt_cfg.get("emergency", {})),
        stop_planner=StopPlanner(config.section("execution")),
        event_bus=event_bus,
        exit_config=exit_cfg,
    )
    log.info("[BOOT] Position pipeline initialized (trail, ratchet, BE, harvest, emergency, exit_manager)")

    # --- Spread monitor ---
    from scrooge_v3.market.spread_monitor import SpreadMonitor
    spread_monitor = SpreadMonitor()

    # --- Position tracker ---
    from scrooge_v3.execution.position_tracker import PositionTracker
    tracker = PositionTracker(persist_path=Path("data/positions.json"))
    tracker.restore()

    # --- Universe screener ---
    from scrooge_v3.market.screener import get_session_pairs
    screener = get_session_pairs

    # --- Load instruments ---
    instruments = broker.get_instruments()
    log.info("[BOOT] Loaded %d instruments from broker", len(instruments))

    # --- Restore state ---
    if state.restore():
        log.info("[BOOT] State restored from disk")
    else:
        log.info("[BOOT] No prior state — fresh start")

    # --- Equity baseline ---
    acct = broker.get_account()
    if acct:
        state.equity_start = acct.equity
        log.info("[BOOT] Equity baseline: $%.2f", acct.equity)
        # Phase 4: seed the daily circuit if first boot today.
        from datetime import datetime as _dt, timezone as _tz
        circuit_snap = cooldown_tracker.circuit_snapshot()
        today_utc = _dt.now(_tz.utc).strftime("%Y-%m-%d")
        if (
            circuit_snap.get("utc_date") != today_utc
            or circuit_snap.get("equity_start", 0) <= 0
        ):
            cooldown_tracker.start_day(acct.equity)

    # --- Reconcile open positions with tracker ---
    open_trades = broker.get_open_trades()
    state.position_count = len(open_trades)
    known_trade_ids = {t.trade_id for t in open_trades}

    for trade in open_trades:
        if not tracker.get(trade.trade_id):
            tracker.register_entry(
                trade_id=trade.trade_id,
                symbol=trade.symbol,
                direction=trade.direction,
                units=trade.units,
                entry_price=trade.entry_price,
                stop_price=trade.current_stop,
                tp_price=trade.current_tp,
                strategy="recovered",
            )
            log.warning("[BOOT] Recovered orphaned position: %s %s %s %.0f units",
                        trade.trade_id, trade.symbol, trade.direction, trade.units)
    log.info("[BOOT] %d positions tracked (%d from broker)",
             len(tracker.all_positions()), len(open_trades))

    # --- Smoke test ---
    if not broker.ping():
        raise BootFailure("Broker ping failed")

    dry_run = config.get("runtime.dry_run", True)
    scan_interval = config.get("runtime.scan_interval_seconds", 300)

    log.info("[BOOT] Complete — dry_run=%s, %d features, %d gates",
             dry_run, len(list(registry.get_active("features"))),
             len(gate_pipeline.gates) if hasattr(gate_pipeline, 'gates') else 0)

    return RuntimeContext(
        config=config,
        broker=broker,
        event_bus=event_bus,
        registry=registry,
        state=state,
        router=router,
        scan_pipeline=scan_pipeline,
        position_pipeline=position_pipeline,
        tracker=tracker,
        spread_monitor=spread_monitor,
        execution_audit=execution_audit,
        dbb_audit=dbb_audit,
        order_attribution=order_attribution,
        live_state=live_state,
        screener=screener,
        cooldown_tracker=cooldown_tracker,
        known_trade_ids=known_trade_ids,
        scan_interval=scan_interval,
        dry_run=dry_run,
    )


def _init_broker(config: ConfigStore) -> Any:
    """Initialize the appropriate broker adapter."""
    from scrooge_v3.market.oanda_adapter import OANDAAdapter
    from scrooge_v3.market.dry_run_adapter import DryRunAdapter

    broker_cfg = config.section("broker")
    oanda = OANDAAdapter({
        "api_url": os.environ.get("OANDA_API_URL", broker_cfg.get("api_url", "https://api-fxpractice.oanda.com")),
        "account_id": os.environ.get("OANDA_ACCOUNT_ID", broker_cfg.get("account_id", "")),
        "api_token": os.environ.get("OANDA_API_TOKEN", broker_cfg.get("api_token", "")),
    })

    dry_run = config.get("runtime.dry_run", True)
    if dry_run:
        log.info("[BOOT] Using dry-run adapter (shadow trading)")
        return DryRunAdapter(oanda)
    return oanda
