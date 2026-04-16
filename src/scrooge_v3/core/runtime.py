"""Runtime — thin orchestrator replacing the V2 coordinator.

Wires together: ScanPipeline, PositionPipeline, StateController.
Runs the main 5-minute loop and the 3-second fast loop.

This file should stay under 200 lines. If it grows beyond that,
something that should be a module is being embedded here.
"""

from __future__ import annotations

import logging
import signal
import time
from datetime import datetime, timezone
from typing import Any

from .config import ConfigStore
from .events import EventBus
from .registry import ModuleRegistry
from .scan_pipeline import ScanPipeline
from .state_controller import StateController
from .strategy_router import StrategyRouter
from .types import MarketSnapshot, ModuleMode, TradeDirection

log = logging.getLogger("scrooge_v3.core.runtime")


class Runtime:
    """Main runtime — boots the system and runs the trading loop.

    Responsibilities:
      - Boot all engines and register modules
      - Run 5-minute scan cycle
      - Delegate position management to PositionPipeline
      - Handle shutdown gracefully
    """

    def __init__(self, config: ConfigStore, live_state: Any = None):
        self.config = config
        self.event_bus = EventBus()
        self.registry = ModuleRegistry()
        from pathlib import Path
        persist_path = Path(config.get("runtime.state_file", "data/state.json"))
        self.state = StateController(
            config=config.section("risk") | config.section("runtime"),
            persist_path=persist_path,
        )
        self.router = StrategyRouter()
        self.broker: Any = None
        self.screener: Any = None
        self.live_state = live_state
        self.position_pipeline: Any = None
        self._known_trade_ids: set[str] = set()  # For vanished trade detection
        self.scan_pipeline = ScanPipeline(
            registry=self.registry,
            router=self.router,
            event_bus=self.event_bus,
        )
        self._shutdown_requested = False
        self._scan_interval = config.get("runtime.scan_interval_seconds", 300)
        self._dry_run = config.get("runtime.dry_run", True)

    def boot(self) -> bool:
        """Initialize all engines and register modules.

        Returns True if boot succeeds, False if smoke test fails.
        """
        log.info("[RUNTIME] Booting V3...")

        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

        # --- Validate config ---
        from .config import ConfigValidationError
        self.config.apply_env_overrides()
        errors = self.config.validate()
        if errors:
            for e in errors:
                log.error("[RUNTIME] Config error: %s", e)
            return False
        log.info("[RUNTIME] Config validated OK")

        # --- Wire config hot reload ---
        self.config.on_change(self._handle_config_change)
        self.config.start_watcher()

        # --- Broker adapter ---
        self.broker = self._init_broker()
        if self.broker is None:
            log.error("[RUNTIME] Broker init failed")
            return False

        # --- Register features ---
        from scrooge_v3.features import (
            ATRCalculator, BollingerCalculator, EMACalculator,
            OverheadRatioCalculator, RSICalculator, VolumeCalculator, ZoneDetector,
        )
        feat_cfg = self.config.section("features")
        self.registry.register("features", "atr", ATRCalculator(feat_cfg.get("atr", {})))
        self.registry.register("features", "bollinger", BollingerCalculator(feat_cfg.get("bollinger", {})))
        self.registry.register("features", "zone_detector", ZoneDetector(feat_cfg.get("zone_detector", {})))
        self.registry.register("features", "otr", OverheadRatioCalculator())
        self.registry.register("features", "ema", EMACalculator(feat_cfg.get("ema", {})))
        self.registry.register("features", "rsi", RSICalculator(feat_cfg.get("rsi", {})))
        self.registry.register("features", "volume", VolumeCalculator(feat_cfg.get("volume", {})))

        # --- Register classifiers ---
        from scrooge_v3.classifiers.bb_state import BollingerStateClassifier
        from scrooge_v3.classifiers.regime import RegimeClassifier
        from scrooge_v3.classifiers.opening import OpeningStateClassifier
        from scrooge_v3.classifiers.structure import StructureClassifier

        cls_cfg = self.config.section("classifiers")
        self.registry.register("classifiers", "bb_state", BollingerStateClassifier())
        self.registry.register("classifiers", "regime", RegimeClassifier())
        self.registry.register("classifiers", "opening_state", OpeningStateClassifier())
        self.registry.register("classifiers", "structure", StructureClassifier())

        # --- Register strategies ---
        from scrooge_v3.strategies import ReversalStrategy, TrendStrategy, DBBTrendStrategy, V3HybridScorer
        from scrooge_v3.strategies.direct_entry import DirectEntryStrategy

        strat_cfg = self.config.section("strategies")
        self.registry.register("strategies", "reversal", ReversalStrategy(strat_cfg.get("reversal", {})))
        self.registry.register("strategies", "trend", TrendStrategy(strat_cfg.get("trend", {})))
        self.registry.register("strategies", "direct", DirectEntryStrategy(strat_cfg.get("direct", {})))
        self.registry.register("strategies", "dbb_trend", DBBTrendStrategy(strat_cfg.get("dbb_trend", {})))

        # --- Register gates ---
        from scrooge_v3.gates import DebounceGate, ZoneEntryCapGate, RegimeFloorGate
        from scrooge_v3.gates.pipeline import GatePipeline

        gate_cfg = self.config.section("gates")
        gate_pipeline = GatePipeline()
        # V3 gate pipeline — 3 gates only:
        #   1. Regime BLOCKED (score < -4): macro circuit breaker, multiple
        #      failure signals stacking. No trade can work in this state.
        #   2. Debounce: prevents re-entry at same zone within 20 min.
        #      Scorer has no memory of recent entries.
        #   3. Zone cap: max 3 entries per zone+direction per day.
        #      Scorer evaluates each trade independently.
        # Everything else is handled by the V3 43-factor scorer.
        gate_pipeline.register_many([
            RegimeFloorGate({"min_score": -4}),
            DebounceGate(gate_cfg.get("debounce", {})),
            ZoneEntryCapGate(gate_cfg.get("zone_entry_cap", {})),
        ])

        # --- Wire scorer and gate pipeline into scan pipeline ---
        scorer = V3HybridScorer(self.config.section("scoring"))
        self.scan_pipeline.gate_pipeline = gate_pipeline
        self.scan_pipeline.scorer = scorer

        # --- Position pipeline (manages all open trades every cycle) ---
        from scrooge_v3.core.position_pipeline import PositionPipeline
        from scrooge_v3.management.trail import TrailManager
        from scrooge_v3.management.ratchet import RatchetManager
        from scrooge_v3.management.be_manager import BreakEvenManager
        from scrooge_v3.management.partial_harvest import PartialHarvestManager
        from scrooge_v3.management.emergency_close import EmergencyCloseManager
        from scrooge_v3.execution.stop_planner import StopPlanner
        from scrooge_v3.telemetry.execution_audit import ExecutionAudit

        mgmt_cfg = self.config.section("management") if self.config.get("management") else {}
        exit_cfg = mgmt_cfg.get("exit_manager", {})
        self.execution_audit = ExecutionAudit(filepath="data/execution-audit.jsonl")
        self.position_pipeline = PositionPipeline(
            trail_manager=TrailManager(mgmt_cfg.get("trail", {})),
            ratchet_manager=RatchetManager(mgmt_cfg.get("ratchet", {})),
            be_manager=BreakEvenManager(mgmt_cfg.get("break_even", {})),
            harvest_manager=PartialHarvestManager(mgmt_cfg.get("harvest", {})),
            emergency_manager=EmergencyCloseManager(mgmt_cfg.get("emergency", {})),
            stop_planner=StopPlanner(self.config.section("execution")),
            event_bus=self.event_bus,
            exit_config=exit_cfg,
        )
        log.info("[RUNTIME] Position pipeline initialized (trail, ratchet, BE, harvest, emergency, exit_manager)")

        # Pending entry metadata (stored in memory for fill reconciliation)
        self._pending_entry_meta: dict[str, dict] = {}

        # --- Spread monitor (rolling mean for hostile spread detection) ---
        from scrooge_v3.market.spread_monitor import SpreadMonitor
        self.spread_monitor = SpreadMonitor()

        # --- Position tracker (per-trade state across cycles) ---
        from pathlib import Path as _Path
        from scrooge_v3.execution.position_tracker import PositionTracker
        self.tracker = PositionTracker(
            persist_path=_Path("data/positions.json"),
        )
        self.tracker.restore()

        # --- Universe screener ---
        from scrooge_v3.market.screener import get_session_pairs
        self.screener = get_session_pairs

        # --- Load instruments ---
        instruments = self.broker.get_instruments()
        log.info("[RUNTIME] Loaded %d instruments from broker", len(instruments))

        # --- Restore state from disk (survives restarts) ---
        if self.state.restore():
            log.info("[RUNTIME] State restored from disk")
        else:
            log.info("[RUNTIME] No prior state — fresh start")

        # --- Set equity baseline for daily loss tracking ---
        acct = self.broker.get_account()
        if acct:
            self.state.equity_start = acct.equity
            log.info("[RUNTIME] Equity baseline: $%.2f", acct.equity)

        # --- Reconcile open positions with tracker ---
        open_trades = self.broker.get_open_trades()
        self.state.position_count = len(open_trades)
        self._known_trade_ids = {t.trade_id for t in open_trades}
        # Auto-register broker positions not in tracker (restart recovery)
        for trade in open_trades:
            if not self.tracker.get(trade.trade_id):
                self.tracker.register_entry(
                    trade_id=trade.trade_id,
                    symbol=trade.symbol,
                    direction=trade.direction,
                    units=trade.units,
                    entry_price=trade.entry_price,
                    stop_price=trade.current_stop,
                    tp_price=trade.current_tp,
                    strategy="recovered",
                )
                log.warning("[RUNTIME] Recovered orphaned position: %s %s %s %.0f units",
                            trade.trade_id, trade.symbol, trade.direction, trade.units)
        log.info("[RUNTIME] %d positions tracked (%d from broker)",
                 len(self.tracker.all_positions()), len(open_trades))

        # --- Smoke test ---
        if not self.broker.ping():
            log.error("[RUNTIME] Broker ping failed")
            return False

        log.info("[RUNTIME] Boot complete — dry_run=%s, %d features, %d gates",
                 self._dry_run, len(list(self.registry.get_active("features"))),
                 len(gate_pipeline.gates) if hasattr(gate_pipeline, 'gates') else 0)
        return True

    def _init_broker(self) -> Any:
        """Initialize the appropriate broker adapter."""
        from scrooge_v3.market.oanda_adapter import OANDAAdapter
        from scrooge_v3.market.dry_run_adapter import DryRunAdapter

        broker_cfg = self.config.section("broker")
        import os
        oanda = OANDAAdapter({
            "api_url": os.environ.get("OANDA_API_URL", broker_cfg.get("api_url", "https://api-fxpractice.oanda.com")),
            "account_id": os.environ.get("OANDA_ACCOUNT_ID", broker_cfg.get("account_id", "")),
            "api_token": os.environ.get("OANDA_API_TOKEN", broker_cfg.get("api_token", "")),
        })

        if self._dry_run:
            log.info("[RUNTIME] Using dry-run adapter (shadow trading)")
            return DryRunAdapter(oanda)
        return oanda

    @staticmethod
    def is_weekend() -> bool:
        """True during OANDA weekend close (Sat 00:00 - Sun 22:00 UTC)."""
        now = datetime.now(timezone.utc)
        wd = now.weekday()  # Mon=0, Sun=6
        if wd == 5:  # Saturday
            return True
        if wd == 6 and now.hour < 22:  # Sunday before 22:00
            return True
        return False

    def run(self) -> None:
        """Main 5-minute trading loop."""
        if not self.boot():
            log.error("[RUNTIME] Boot failed — not starting")
            return

        log.info("[RUNTIME] Starting main loop (interval=%ds)", self._scan_interval)

        while not self._shutdown_requested:
            cycle_start = time.monotonic()
            self.state.cycle_count += 1

            try:
                self._run_cycle()
            except Exception:
                log.exception("[RUNTIME] Cycle %d failed", self.state.cycle_count)

            self.state.persist()

            elapsed = time.monotonic() - cycle_start
            sleep_time = max(0, self._scan_interval - elapsed)
            if sleep_time > 0 and not self._shutdown_requested:
                self._interruptible_sleep(sleep_time)

        log.info("[RUNTIME] Shutdown complete after %d cycles", self.state.cycle_count)

    def _run_cycle(self) -> None:
        """Execute one scan cycle."""
        now = datetime.now(timezone.utc)

        # Weekend detection — OANDA is closed Sat 00:00 - Sun 22:00 UTC
        if self.is_weekend():
            log.debug("[RUNTIME] Weekend — market closed, skipping cycle")
            return

        # Daily reset at date boundary
        if self.state.session_start.date() != now.date():
            self.state.daily_reset()
            self.state.session_start = now
            # Reset equity baseline for new day
            acct = self.broker.get_account()
            if acct:
                self.state.equity_start = acct.equity
                log.info("[RUNTIME] New day — equity baseline: $%.2f", acct.equity)

        # Daily loss limit — halt ALL trading (scan + entry)
        if self.state.is_daily_loss_exceeded():
            log.warning("[RUNTIME] Daily loss limit reached (%.1f%% of $%.0f) — skipping cycle",
                        (self.state.daily_loss / self.state.equity_start * 100) if self.state.equity_start else 0,
                        self.state.equity_start)
            return

        # --- Vanished trade detection (broker closed between cycles) ---
        current_trades = self.broker.get_open_trades()
        current_ids = {t.trade_id for t in current_trades}
        vanished = self._known_trade_ids - current_ids
        if vanished:
            for tid in vanished:
                log.warning("[RUNTIME] Trade vanished (closed externally): %s", tid)
                self.state.decrement_positions()
            self._known_trade_ids = current_ids
        else:
            self._known_trade_ids = current_ids
        self.state.position_count = len(current_trades)

        # Get active pairs for current session
        from scrooge_v3.market.screener import get_session_pairs
        pairs = get_session_pairs(now.hour)

        if not pairs:
            log.debug("[RUNTIME] No active pairs this session")
            return

        # Fetch market snapshots from broker
        prices = self.broker.get_prices(pairs)
        snapshots: dict[str, MarketSnapshot] = {}
        for symbol, quote in prices.items():
            candles = {}
            # OANDA granularity names: D, H1, M5 (not 1H, 5M)
            for oanda_tf, internal_key in (("D", "D"), ("H1", "1H"), ("M5", "5M")):
                df = self.broker.get_candles(symbol, oanda_tf)
                if df is not None:
                    candles[internal_key] = df
            snapshots[symbol] = MarketSnapshot(
                symbol=symbol, bid=quote.bid, ask=quote.ask,
                mid=quote.mid, spread=quote.spread,
                timestamp=quote.timestamp or now, candles=candles,
            )
            self.spread_monitor.record(symbol, quote.spread)

        # Run scan pipeline — returns candidates + full per-pair reports
        candidates, reports = self.scan_pipeline.scan_universe(pairs, snapshots)

        # Fire best candidate if not at max positions
        # Filter out symbols we already have a position in or pending entry for
        held_symbols = {pos.symbol for pos in self.tracker.all_positions()}
        pending_symbols = set(self.tracker.all_pending_entries().keys())
        candidates = [c for c in candidates if c.symbol not in held_symbols and c.symbol not in pending_symbols]

        if candidates and self.state.position_count < self.state.max_positions:
            best = candidates[0]
            log.info("[RUNTIME] Best candidate: %s %s score=%.0f",
                     best.symbol, best.strategy, best.score)

            # --- Spread quality gate: skip entry if spread is elevated ---
            spread_stats = self.spread_monitor.get_stats(best.symbol)
            if spread_stats["mean"] > 0:
                spread_ratio = spread_stats["current"] / spread_stats["mean"]
                if spread_ratio > 1.5:
                    log.warning("[RUNTIME] ENTRY SKIPPED: %s spread elevated (%.1fx mean: "
                                "current=%.5f mean=%.5f) — waiting for tighter spread",
                                best.symbol, spread_ratio,
                                spread_stats["current"], spread_stats["mean"])
                    self.live_state.update(
                        spread_skips=self.live_state.spread_skips + 1,
                        last_spread_skip=f"{best.symbol} ({spread_ratio:.1f}x)",
                    )
                    candidates = []  # clear so we don't try the next candidate either

            from scrooge_v3.execution.sizing import SizingCalculator
            from scrooge_v3.execution.stop_planner import StopPlanner
            sizer = SizingCalculator()
            stop_planner = StopPlanner()
            acct = self.broker.get_account()
            equity = acct.equity if acct else 10000.0
            inst = self.broker.get_instruments().get(best.symbol, {})
            inst_info = {"pipLocation": inst.pip_location, "marginRate": inst.margin_rate} if hasattr(inst, "pip_location") else {}
            free_margin = acct.margin_available if acct else equity
            units = sizer.calculate(best.symbol, best.entry_price, equity, inst_info, free_margin=free_margin)
            if units and units > 0:
                # --- Execution Physics: validate SL before sending ---
                # Fetch live bid/ask for trigger-side validation
                quote = self.broker.get_price(best.symbol)
                if quote:
                    validated_sl, sl_reason = stop_planner.validate_stop(
                        best.direction, best.stop_price,
                        quote.bid, quote.ask, quote.spread,
                    )
                    if sl_reason != "valid":
                        log.warning("[RUNTIME] SL adjusted: %s %.5f → %.5f (%s)",
                                    best.symbol, best.stop_price, validated_sl, sl_reason)
                    # Check if trailing is safe (spread kill switch)
                    trail_ok, trail_reason = stop_planner.should_trail(
                        best.direction, best.stop_price, validated_sl,
                        quote.spread, self.spread_monitor.get_stats(best.symbol).get('mean', quote.spread),
                    )
                    if not trail_ok and "hostile_spread" in trail_reason:
                        log.warning("[RUNTIME] ENTRY SKIPPED: %s spread kill — %s",
                                    best.symbol, trail_reason)
                    else:
                        # Sign units: positive for LONG, negative for SHORT
                        signed_units = units if best.direction.value == "long" else -units

                        # Compute limit price: bid for longs (maker), ask for shorts (maker)
                        limit_price = quote.bid if best.direction.value == "long" else quote.ask

                        # GTD: expire after one cycle
                        from datetime import timedelta
                        gtd_time = (datetime.now(timezone.utc) + timedelta(minutes=5)).strftime(
                            "%Y-%m-%dT%H:%M:%S.000000000Z"
                        )

                        log.info("[RUNTIME] Placing LIMIT order: %s %s %d units @ %.5f SL=%.5f TP=%.5f GTD=%s",
                                 best.symbol, best.direction.value, signed_units,
                                 limit_price, validated_sl, best.take_profit or 0, gtd_time)
                        result = self.broker.place_limit_order(
                            symbol=best.symbol, units=signed_units,
                            price=limit_price,
                            stop_loss=validated_sl, take_profit=best.take_profit,
                            gtd_time=gtd_time,
                        )
                        if result.success and result.trade_id:
                            # Immediate fill (limit at-or-better than market)
                            self.state.position_count += 1
                            self.tracker.register_entry(
                                trade_id=result.trade_id,
                                symbol=best.symbol,
                                direction=best.direction.value,
                                units=abs(signed_units),
                                entry_price=result.fill_price,
                                stop_price=validated_sl,
                                tp_price=best.take_profit or 0,
                                tp1_price=best.metadata.get("tp1", 0),
                                tp2_price=best.take_profit or 0,
                                strategy=best.strategy,
                                v3_score=int(best.score),
                                metadata=best.metadata,
                            )
                            self.state.record_zone_entry(best.symbol, f"{validated_sl:.5f}")
                            log.info("[RUNTIME] LIMIT FILLED IMMEDIATELY: %s %s %d units @ %.5f",
                                     result.trade_id, best.symbol, signed_units, result.fill_price)
                            # Place harvest limit at TP1
                            self._place_harvest_limit(self.tracker.get(result.trade_id))
                        elif result.success and result.order_id:
                            # Pending — limit order placed, waiting for fill
                            self.tracker.register_pending_entry(best.symbol, result.order_id)
                            # Store entry metadata for when the fill comes
                            self._pending_entry_meta[best.symbol] = {
                                "direction": best.direction.value,
                                "stop_loss": validated_sl,
                                "take_profit": best.take_profit or 0,
                                "tp1_price": best.metadata.get("tp1", 0),
                                "strategy": best.strategy,
                                "v3_score": int(best.score),
                                "metadata": best.metadata,
                            }
                            log.info("[RUNTIME] LIMIT ENTRY PLACED: %s %s order=%s @ %.5f",
                                     best.symbol, best.direction.value, result.order_id, limit_price)
                        else:
                            log.error("[RUNTIME] LIMIT ORDER FAILED: %s %s error=%s",
                                      best.symbol, best.direction.value, result.error)
                else:
                    log.error("[RUNTIME] Cannot get price for %s — skipping entry", best.symbol)

        # --- Reconcile pending orders ---
        self._reconcile_pending_orders()

        # --- Manage open positions ---
        # Reconcile tracker with broker (detect vanished trades)
        open_trades = self.broker.get_open_trades()
        broker_ids = {t.trade_id for t in open_trades}
        vanished = self.tracker.reconcile_with_broker(broker_ids)
        for tid in vanished:
            # Cancel orphaned harvest limits for vanished trades
            tracked = self.tracker.get(tid)
            if tracked and tracked.harvest_order_id:
                self.broker.cancel_order(tracked.harvest_order_id)
                log.info("[RUNTIME] Cancelled harvest limit %s for vanished trade %s",
                         tracked.harvest_order_id, tid)
            self.state.decrement_positions()
        self.state.position_count = len(open_trades)

        # Run management pipeline on each tracked position
        from scrooge_v3.execution.stop_planner import StopPlanner
        from scrooge_v3.telemetry.execution_audit import AuditEvent
        sp = StopPlanner(self.config.section("execution"))
        audit = getattr(self, "execution_audit", None)

        def _audit(etype, reason, **kw):
            if audit:
                audit.record(AuditEvent(type=etype, reason=reason, **kw))

        for tracked in self.tracker.all_positions():
            # Get live price for execution physics
            quote = self.broker.get_price(tracked.symbol)
            if not quote:
                continue

            h1 = self.broker.get_candles(tracked.symbol, "H1", 24)
            pip = 0.01 if "JPY" in tracked.symbol else 0.0001
            direction = TradeDirection(tracked.direction)

            # Run position pipeline
            action = self.position_pipeline.manage_position(
                tracked,
                current_price=quote.mid,
                bid=quote.bid,
                ask=quote.ask,
                spread=quote.spread,
                mean_spread=self.spread_monitor.get_stats(tracked.symbol).get('mean', quote.spread),
                hourly_bars=h1,
                pip_size=pip,
            )

            details = action.details or {}
            profit_r = details.get("profit_r", 0.0)
            phase = details.get("phase", "")
            audit_base = dict(
                trade_id=tracked.trade_id, symbol=tracked.symbol,
                direction=tracked.direction, profit_r=profit_r,
                spread=quote.spread, action=action.action,
            )

            if action.action == "hold":
                hold_reason = details.get("reason", "no_action")
                _audit("hold", hold_reason, **audit_base)
                continue

            new_stop = details.get("new_stop")
            log.info("[RUNTIME] Position %s: action=%s phase=%s profit_r=%.3f details=%s",
                     tracked.trade_id, action.action, phase, profit_r, details)

            if action.action in ("trail", "ratchet", "break_even") and new_stop:
                # === EXECUTION PHYSICS: 4 guards before any SL submission ===
                # 1. Spread kill switch
                trail_ok, trail_reason = sp.should_trail(
                    direction, tracked.current_stop, new_stop,
                    quote.spread, quote.spread,
                )
                if not trail_ok:
                    log.warning("[RUNTIME] SL %s BLOCKED (%s): %s spread=%.5f — native SL stays",
                                action.action, trail_reason, tracked.trade_id, quote.spread)
                    _audit("sl_blocked", trail_reason, old_sl=tracked.current_stop,
                           new_sl=new_stop, **audit_base)
                    continue

                # 2-4. Trigger-side, no-man's-zone, buffer
                validated, reason = sp.validate_stop(
                    direction, new_stop, quote.bid, quote.ask, quote.spread,
                )

                if reason == "valid" or "adjusted" in reason:
                    # Final guard: never loosen the stop after spread adjustment
                    if direction == TradeDirection.LONG and validated < tracked.current_stop:
                        log.info("[RUNTIME] SL %s SKIPPED (spread adjustment would loosen): "
                                 "%s proposed=%.5f validated=%.5f current=%.5f",
                                 action.action, tracked.trade_id, new_stop, validated, tracked.current_stop)
                        _audit("sl_blocked", "would_loosen", old_sl=tracked.current_stop,
                               new_sl=validated, **audit_base)
                        continue
                    if direction == TradeDirection.SHORT and validated > tracked.current_stop:
                        log.info("[RUNTIME] SL %s SKIPPED (spread adjustment would loosen): "
                                 "%s proposed=%.5f validated=%.5f current=%.5f",
                                 action.action, tracked.trade_id, new_stop, validated, tracked.current_stop)
                        _audit("sl_blocked", "would_loosen", old_sl=tracked.current_stop,
                               new_sl=validated, **audit_base)
                        continue
                    success = self.broker.modify_stop_loss(tracked.trade_id, validated)
                    if success:
                        old_sl = tracked.current_stop
                        self.tracker.update_stop(tracked.trade_id, validated)
                        if action.action == "break_even":
                            self.tracker.mark_break_even(tracked.trade_id)
                        log.info("[RUNTIME] SL %s: %s %.5f → %.5f (%s)",
                                 action.action, tracked.trade_id, old_sl, validated, reason)
                        _audit("sl_moved", f"{action.action}_{reason}", old_sl=old_sl,
                               new_sl=validated, **audit_base)
                    else:
                        log.error("[RUNTIME] SL modify failed: %s", tracked.trade_id)
                        _audit("sl_blocked", "broker_reject", old_sl=tracked.current_stop,
                               new_sl=validated, **audit_base)
                else:
                    log.warning("[RUNTIME] SL %s BLOCKED (%s): %s — native SL stays",
                                action.action, reason, tracked.trade_id)
                    _audit("sl_blocked", reason, old_sl=tracked.current_stop,
                           new_sl=new_stop, **audit_base)

            elif action.action == "harvest":
                fraction = details.get("fraction", 0.5)
                close_units = int(tracked.units * fraction)
                if close_units > 0:
                    result = self.broker.close_trade(tracked.trade_id, close_units)
                    if result.success:
                        self.tracker.mark_tp1_taken(tracked.trade_id)
                        log.info("[RUNTIME] HARVEST: %s closed %d units @ %.5f",
                                 tracked.trade_id, close_units, result.fill_price)
                        _audit("harvest", "tp1_taken", **audit_base)

            elif action.action == "favorable_exit":
                trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
                if trade:
                    method = details.get("method", "market")
                    if method == "limit":
                        limit_price = details.get("limit_price", 0)
                        log.info("[RUNTIME] FAVORABLE EXIT (limit): %s @ %.5f",
                                 trade.trade_id, limit_price)
                        result = self.broker.close_trade(trade.trade_id)
                        if result.success:
                            log.info("[RUNTIME] FAVORABLE EXIT FILLED: %s @ %.5f",
                                     trade.trade_id, result.fill_price)
                            _audit("favorable_exit", f"limit_{details.get('reason', '')}", **audit_base)
                    else:
                        log.info("[RUNTIME] FAVORABLE EXIT (market): %s reason=%s",
                                 trade.trade_id, details.get("reason", ""))
                        result = self.broker.close_trade(trade.trade_id)
                        if result.success:
                            log.info("[RUNTIME] FAVORABLE EXIT FILLED: %s @ %.5f",
                                     trade.trade_id, result.fill_price)
                            _audit("favorable_exit", f"market_{details.get('reason', '')}", **audit_base)

            elif action.action == "emergency_close":
                trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
                if trade:
                    result = self.broker.close_trade(trade.trade_id)
                    if result.success:
                        self.state.record_loss(abs(result.realized_pl) if result.realized_pl < 0 else 0)
                        log.warning("[RUNTIME] EMERGENCY CLOSE: %s @ %.5f pl=%.2f reason=%s",
                                    trade.trade_id, result.fill_price,
                                    result.realized_pl, details.get("reason", ""))
                        _audit("emergency_close", details.get("reason", "unknown"), **audit_base)

        # --- Push execution audit to dashboard ---
        if audit and self.live_state:
            self.live_state.update(
                execution_summary=audit.summary(),
                execution_events=audit.recent_events(50),
            )

        # --- Daily P&L check ---
        daily_pl = self.broker.get_realized_pl_today()
        if self.live_state:
            self.live_state.update(daily_pnl=daily_pl)

        # Update dashboard live state with full per-pair reports
        if self.live_state:
            from scrooge_v3.market.screener import get_active_sessions
            acct = self.broker.get_account()
            sessions = get_active_sessions(now.hour)

            viable = [r for r in reports if r.get("verdict", "").startswith("TAKE")]

            self.live_state.update(
                cycle_count=self.state.cycle_count,
                equity=acct.equity if acct else 0,
                balance=acct.balance if acct else 0,
                unrealized_pl=acct.unrealized_pl if acct else 0,
                daily_pnl=self.broker.get_realized_pl_today() if acct else 0,
                position_count=self.state.position_count,
                pairs_scanned=len(reports),
                pairs_viable=len(viable),
                signals_evaluated=len(reports),
                active_sessions=[s["name"] for s in sessions],
                scan_reports=reports,
                valid_count=len(viable),
                rejected_count=len(reports) - len(viable),
                daily_loss_exceeded=self.state.is_daily_loss_exceeded(),
            )

        # Update pending orders count for dashboard
        self.live_state.update(
            pending_limit_orders=len(self.tracker.all_pending_entries()) + len(self.tracker.get_positions_with_harvest_orders()),
        )

        log.debug("[RUNTIME] Cycle %d complete — positions=%d, candidates=%d",
                  self.state.cycle_count, self.state.position_count, len(candidates))

    def shutdown(self) -> None:
        """Graceful shutdown."""
        log.info("[RUNTIME] Shutdown requested")
        self._shutdown_requested = True
        self.config.stop_watcher()
        self.state.persist()

    def _handle_signal(self, signum: int, frame: Any) -> None:
        log.info("[RUNTIME] Received signal %d", signum)
        self.shutdown()

    def _handle_config_change(self, change: dict) -> None:
        """Handle config hot-reload changes — update module modes, gate modes."""
        from .events import CONFIG_CHANGED, Event
        path = change.get("path", "")
        new_val = change.get("new")

        # Module mode switching: e.g. features.atr.mode = "disabled"
        parts = path.split(".")
        if len(parts) >= 3 and parts[2] == "mode":
            category = parts[0]  # features, classifiers, strategies, gates
            module_name = parts[1]
            new_mode = str(new_val)
            log.info("[RUNTIME] Config change: %s.%s mode → %s", category, module_name, new_mode)
            self.registry.set_mode(category, module_name, new_mode)

        # Gate mode switching: e.g. gates.spread.mode = "observe"
        if len(parts) >= 3 and parts[0] == "gates" and parts[2] == "mode":
            gate_name = parts[1]
            log.info("[RUNTIME] Gate mode change: %s → %s", gate_name, new_val)

        # Scan interval change
        if path == "runtime.scan_interval_seconds" and isinstance(new_val, (int, float)):
            self._scan_interval = int(new_val)
            log.info("[RUNTIME] Scan interval changed to %ds", self._scan_interval)

        # Emit event for other listeners
        self.event_bus.emit(Event(type=CONFIG_CHANGED, payload=change))

    def _interruptible_sleep(self, seconds: float) -> None:
        """Sleep that can be interrupted by shutdown."""
        end = time.monotonic() + seconds
        while time.monotonic() < end and not self._shutdown_requested:
            time.sleep(min(1.0, end - time.monotonic()))

    def _reconcile_pending_orders(self) -> None:
        """Reconcile pending entry and harvest limit orders with OANDA."""
        pending_on_broker = {o.order_id for o in self.broker.get_pending_orders()}

        # Check pending entries
        for symbol, order_id in list(self.tracker.all_pending_entries().items()):
            if order_id in pending_on_broker:
                continue  # Still pending, wait

            # Order gone — check if it filled (new trade appeared)
            open_trades = self.broker.get_open_trades()
            new_trade = None
            for t in open_trades:
                if t.symbol == symbol and not self.tracker.get(t.trade_id):
                    new_trade = t
                    break

            if new_trade:
                meta = self._pending_entry_meta.pop(symbol, {})
                self.tracker.register_entry(
                    trade_id=new_trade.trade_id,
                    symbol=new_trade.symbol,
                    direction=new_trade.direction,
                    units=new_trade.units,
                    entry_price=new_trade.entry_price,
                    stop_price=new_trade.current_stop,
                    tp_price=new_trade.current_tp,
                    tp1_price=meta.get("tp1_price", 0),
                    tp2_price=new_trade.current_tp,
                    strategy=meta.get("strategy", "limit_fill"),
                    v3_score=meta.get("v3_score", 0),
                    metadata=meta.get("metadata", {}),
                )
                self.state.position_count += 1
                self.state.record_zone_entry(symbol, f"{new_trade.current_stop:.5f}")
                log.info("[RUNTIME] LIMIT ENTRY FILLED: %s %s @ %.5f (order %s)",
                         new_trade.trade_id, symbol, new_trade.entry_price, order_id)
                self.tracker.clear_pending_entry(symbol)
                # Place harvest limit for the new trade
                self._place_harvest_limit(self.tracker.get(new_trade.trade_id))
            else:
                # Order expired or was cancelled
                self._pending_entry_meta.pop(symbol, None)
                self.tracker.clear_pending_entry(symbol)
                log.info("[RUNTIME] LIMIT ENTRY EXPIRED: %s order=%s", symbol, order_id)

        # Check harvest orders
        for tracked in self.tracker.get_positions_with_harvest_orders():
            if tracked.harvest_order_id in pending_on_broker:
                continue  # Still pending

            # Harvest order gone — check if trade units decreased (filled)
            broker_trade = next(
                (t for t in self.broker.get_open_trades() if t.trade_id == tracked.trade_id),
                None,
            )
            if broker_trade and broker_trade.units < tracked.units:
                # Harvest filled — units decreased
                self.tracker.mark_tp1_taken(tracked.trade_id)
                self.tracker.clear_harvest_order(tracked.trade_id)
                log.info("[RUNTIME] HARVEST LIMIT FILLED: %s units %.0f → %.0f",
                         tracked.trade_id, tracked.units, broker_trade.units)
            else:
                # Harvest cancelled or expired without fill
                self.tracker.clear_harvest_order(tracked.trade_id)
                log.info("[RUNTIME] HARVEST LIMIT CANCELLED: %s order=%s",
                         tracked.trade_id, tracked.harvest_order_id)

    def _place_harvest_limit(self, tracked) -> None:
        """Pre-place a REDUCE_ONLY limit order at TP1 for partial harvest."""
        if not tracked or not tracked.tp1_price or tracked.tp1_taken:
            return
        if tracked.harvest_order_id:
            return  # Already have one

        harvest_units = int(tracked.units * 0.5)
        if harvest_units <= 0:
            return

        # Opposite sign: sell to reduce long, buy to reduce short
        if tracked.direction == "long":
            signed_units = -harvest_units
        else:
            signed_units = harvest_units

        result = self.broker.place_limit_order(
            symbol=tracked.symbol,
            units=signed_units,
            price=tracked.tp1_price,
            stop_loss=None,
            take_profit=None,
            gtd_time=None,  # GTC
            position_fill="REDUCE_ONLY",
        )

        if result.success and result.order_id:
            self.tracker.set_harvest_order(tracked.trade_id, result.order_id)
            log.info("[RUNTIME] HARVEST LIMIT PLACED: %s order=%s @ %.5f (%d units)",
                     tracked.trade_id, result.order_id, tracked.tp1_price, harvest_units)
        elif result.success and result.trade_id:
            # Immediate fill — TP1 already reached
            self.tracker.mark_tp1_taken(tracked.trade_id)
            log.info("[RUNTIME] HARVEST LIMIT FILLED IMMEDIATELY: %s @ %.5f",
                     tracked.trade_id, tracked.tp1_price)
        else:
            log.warning("[RUNTIME] HARVEST LIMIT FAILED: %s error=%s",
                        tracked.trade_id, result.error)
