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
from .types import MarketSnapshot, ModuleMode

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
        self.state = StateController(
            config=config.section("risk") | config.section("runtime"),
        )
        self.router = StrategyRouter()
        self.broker: Any = None
        self.screener: Any = None
        self.live_state = live_state  # Dashboard LiveState (thread-safe)
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
        from scrooge_v3.strategies import ReversalStrategy, TrendStrategy, V3HybridScorer
        from scrooge_v3.strategies.direct_entry import DirectEntryStrategy

        strat_cfg = self.config.section("strategies")
        self.registry.register("strategies", "reversal", ReversalStrategy(strat_cfg.get("reversal", {})))
        self.registry.register("strategies", "trend", TrendStrategy(strat_cfg.get("trend", {})))
        self.registry.register("strategies", "direct", DirectEntryStrategy(strat_cfg.get("direct", {})))

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

        mgmt_cfg = self.config.section("management") if self.config.get("management") else {}
        self.position_pipeline = PositionPipeline(
            trail_manager=TrailManager(mgmt_cfg.get("trail", {})),
            ratchet_manager=RatchetManager(mgmt_cfg.get("ratchet", {})),
            be_manager=BreakEvenManager(mgmt_cfg.get("break_even", {})),
            harvest_manager=PartialHarvestManager(mgmt_cfg.get("harvest", {})),
            emergency_manager=EmergencyCloseManager(mgmt_cfg.get("emergency", {})),
            stop_planner=StopPlanner(self.config.section("execution")),
            event_bus=self.event_bus,
        )
        log.info("[RUNTIME] Position pipeline initialized (trail, ratchet, BE, harvest, emergency)")

        # --- Universe screener ---
        from scrooge_v3.market.screener import get_session_pairs
        self.screener = get_session_pairs

        # --- Load instruments ---
        instruments = self.broker.get_instruments()
        log.info("[RUNTIME] Loaded %d instruments from broker", len(instruments))

        # --- Reconcile open positions ---
        open_trades = self.broker.get_open_trades()
        self.state.position_count = len(open_trades)
        log.info("[RUNTIME] Found %d open positions", len(open_trades))

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

        if self.state.session_start.date() != now.date():
            self.state.daily_reset()
            self.state.session_start = now

        if self.state.is_daily_loss_exceeded():
            log.warning("[RUNTIME] Daily loss limit reached — skipping cycle")
            return

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

        # Run scan pipeline — returns candidates + full per-pair reports
        candidates, reports = self.scan_pipeline.scan_universe(pairs, snapshots)

        # Fire best candidate if not at max positions
        if candidates and self.state.position_count < self.state.max_positions:
            best = candidates[0]
            log.info("[RUNTIME] Best candidate: %s %s score=%.0f",
                     best.symbol, best.strategy, best.score)

            from scrooge_v3.execution.sizing import SizingCalculator
            from scrooge_v3.execution.stop_planner import StopPlanner
            sizer = SizingCalculator()
            stop_planner = StopPlanner()
            acct = self.broker.get_account()
            equity = acct.equity if acct else 10000.0
            inst = self.broker.get_instruments().get(best.symbol, {})
            inst_info = {"pipLocation": inst.pip_location, "marginRate": inst.margin_rate} if hasattr(inst, "pip_location") else {}
            units = sizer.calculate(best.symbol, best.entry_price, equity, inst_info)
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
                        quote.spread, quote.spread,  # mean_spread = current (first cycle)
                    )
                    if not trail_ok and "hostile_spread" in trail_reason:
                        log.warning("[RUNTIME] ENTRY SKIPPED: %s spread kill — %s",
                                    best.symbol, trail_reason)
                    else:
                        # Sign units: positive for LONG, negative for SHORT
                        signed_units = units if best.direction.value == "long" else -units
                        log.info("[RUNTIME] Placing order: %s %s %d units SL=%.5f TP=%.5f",
                                 best.symbol, best.direction.value, signed_units,
                                 validated_sl, best.take_profit or 0)
                        result = self.broker.place_market_order(
                            symbol=best.symbol, units=signed_units,
                            stop_loss=validated_sl, take_profit=best.take_profit,
                        )
                        if result.success:
                            self.state.position_count += 1
                            log.info("[RUNTIME] ORDER FILLED: %s %s %d units @ %.5f",
                                     result.trade_id, best.symbol, signed_units, result.fill_price)
                        else:
                            log.error("[RUNTIME] ORDER FAILED: %s %s error=%s",
                                      best.symbol, best.direction.value, result.error)
                else:
                    log.error("[RUNTIME] Cannot get price for %s — skipping entry", best.symbol)

        # --- Manage open positions (trail, ratchet, BE, harvest, emergency) ---
        open_trades = self.broker.get_open_trades()
        self.state.position_count = len(open_trades)

        if open_trades and hasattr(self, 'position_pipeline'):
            # Build market data for each position's symbol
            market_data: dict[str, dict] = {}
            for trade in open_trades:
                sym = trade.symbol
                if sym not in market_data:
                    q = self.broker.get_price(sym)
                    h1 = self.broker.get_candles(sym, "H1", 24)
                    if q:
                        market_data[sym] = {
                            "mid": q.mid, "bid": q.bid, "ask": q.ask,
                            "spread": q.spread, "mean_spread": q.spread,
                            "hourly_bars": h1,
                        }

            actions = self.position_pipeline.manage_all(open_trades, market_data)
            for action in actions:
                if action.action == "hold":
                    continue
                details = action.details or {}
                new_stop = details.get("new_stop")

                if action.action in ("trail", "ratchet", "break_even") and new_stop:
                    # Validate SL before submitting (execution physics)
                    trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
                    if trade:
                        q = self.broker.get_price(trade.symbol)
                        if q:
                            from scrooge_v3.execution.stop_planner import StopPlanner
                            sp = StopPlanner()
                            validated, reason = sp.validate_stop(
                                TradeDirection(trade.direction), new_stop,
                                q.bid, q.ask, q.spread,
                            )
                            if reason == "valid" or "adjusted" in reason:
                                success = self.broker.modify_stop_loss(trade.trade_id, validated)
                                if success:
                                    log.info("[RUNTIME] SL %s: %s → %.5f (%s)",
                                             action.action, trade.trade_id, validated, reason)
                            else:
                                log.warning("[RUNTIME] SL blocked: %s %s (%s)",
                                            trade.trade_id, action.action, reason)

                elif action.action == "harvest":
                    trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
                    if trade:
                        fraction = details.get("fraction", 0.5)
                        close_units = int(trade.units * fraction)
                        if close_units > 0:
                            result = self.broker.close_trade(trade.trade_id, close_units)
                            if result.success:
                                log.info("[RUNTIME] HARVEST: %s closed %d units @ %.5f",
                                         trade.trade_id, close_units, result.fill_price)

                elif action.action == "emergency_close":
                    trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
                    if trade:
                        result = self.broker.close_trade(trade.trade_id)
                        if result.success:
                            log.warning("[RUNTIME] EMERGENCY CLOSE: %s @ %.5f reason=%s",
                                        trade.trade_id, result.fill_price, details.get("reason", ""))

        # --- Detect vanished trades (OANDA closed between cycles) ---
        broker_trade_ids = {t.trade_id for t in open_trades}
        # (Position tracking will be enhanced when state persistence is added)

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
                realized_pl=acct.unrealized_pl if acct else 0,
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
