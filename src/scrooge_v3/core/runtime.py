"""Runtime — thin orchestrator for the V3 trading platform.

Wires together: bootstrap, scan pipeline, execution, position management.
The runtime is the conductor — it calls into specialized modules
rather than implementing their logic directly.

Phase 1 extraction (2026-04-16):
  - boot logic → bootstrap.py
  - typed dependencies → runtime_context.py
  - dashboard updates → services/dashboard_bridge.py
"""

from __future__ import annotations

import logging
import signal
import time
from datetime import datetime, timedelta, timezone
from typing import Any

from .config import ConfigStore
from .bootstrap import build_runtime, BootFailure
from .runtime_context import RuntimeContext
from .types import MarketSnapshot, TradeDirection

log = logging.getLogger("scrooge_v3.core.runtime")


class Runtime:
    """Main runtime — boots the system and runs the trading loop.

    Responsibilities:
      - Boot via bootstrap.build_runtime()
      - Run scan cycle
      - Delegate execution and position management
      - Publish state via DashboardBridge
      - Handle shutdown gracefully
    """

    def __init__(self, config: ConfigStore, live_state: Any = None):
        self.config = config
        self.live_state = live_state
        self.ctx: RuntimeContext | None = None
        self._shutdown_requested = False
        self.dashboard: Any = None

    def boot(self) -> bool:
        """Initialize all engines via bootstrap."""
        log.info("[RUNTIME] Booting V3...")

        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

        try:
            self.ctx = build_runtime(self.config, self.live_state)
        except BootFailure as e:
            log.error("[RUNTIME] Boot failed: %s", e)
            return False
        except Exception:
            log.exception("[RUNTIME] Boot failed with unexpected error")
            return False

        # Wire config hot reload
        self.config.on_change(self._handle_config_change)

        # Create dashboard bridge
        if self.live_state:
            from scrooge_v3.services.dashboard_bridge import DashboardBridge
            self.dashboard = DashboardBridge(self.live_state)

        log.info("[RUNTIME] Boot complete")
        return True

    @staticmethod
    def is_weekend() -> bool:
        """True during OANDA weekend close (Sat 00:00 - Sun 22:00 UTC)."""
        now = datetime.now(timezone.utc)
        wd = now.weekday()
        if wd == 5:
            return True
        if wd == 6 and now.hour < 22:
            return True
        return False

    def run(self) -> None:
        """Main trading loop."""
        if not self.boot():
            log.error("[RUNTIME] Boot failed — not starting")
            return

        ctx = self.ctx
        log.info("[RUNTIME] Starting main loop (interval=%ds)", ctx.scan_interval)

        while not self._shutdown_requested:
            cycle_start = time.monotonic()
            ctx.state.cycle_count += 1

            try:
                self._run_cycle()
            except Exception:
                log.exception("[RUNTIME] Cycle %d failed", ctx.state.cycle_count)

            ctx.state.persist()

            elapsed = time.monotonic() - cycle_start
            sleep_time = max(0, ctx.scan_interval - elapsed)
            if sleep_time > 0 and not self._shutdown_requested:
                self._interruptible_sleep(sleep_time)

        log.info("[RUNTIME] Shutdown complete after %d cycles", ctx.state.cycle_count)

    def _run_cycle(self) -> None:
        """Execute one scan cycle."""
        ctx = self.ctx
        now = datetime.now(timezone.utc)

        # Weekend detection
        if self.is_weekend():
            log.debug("[RUNTIME] Weekend — market closed, skipping cycle")
            return

        # Daily reset at date boundary
        if ctx.state.session_start.date() != now.date():
            ctx.state.daily_reset()
            ctx.state.session_start = now
            acct = ctx.broker.get_account()
            if acct:
                ctx.state.equity_start = acct.equity
                log.info("[RUNTIME] New day — equity baseline: $%.2f", acct.equity)

        # Daily loss limit
        if ctx.state.is_daily_loss_exceeded():
            log.warning("[RUNTIME] Daily loss limit reached — skipping cycle")
            return

        # --- Vanished trade detection ---
        current_trades = ctx.broker.get_open_trades()
        current_ids = {t.trade_id for t in current_trades}
        vanished = ctx.known_trade_ids - current_ids
        if vanished:
            for tid in vanished:
                log.warning("[RUNTIME] Trade vanished (closed externally): %s", tid)
                ctx.state.decrement_positions()
        ctx.known_trade_ids = current_ids
        ctx.state.position_count = len(current_trades)

        # Get active pairs
        from scrooge_v3.market.screener import get_session_pairs
        pairs = get_session_pairs(now.hour)
        if not pairs:
            log.debug("[RUNTIME] No active pairs this session")
            return

        # Fetch market snapshots
        prices = ctx.broker.get_prices(pairs)
        snapshots: dict[str, MarketSnapshot] = {}
        for symbol, quote in prices.items():
            candles = {}
            for oanda_tf, internal_key in (("D", "D"), ("H1", "1H"), ("M5", "5M")):
                df = ctx.broker.get_candles(symbol, oanda_tf)
                if df is not None:
                    candles[internal_key] = df
            snapshots[symbol] = MarketSnapshot(
                symbol=symbol, bid=quote.bid, ask=quote.ask,
                mid=quote.mid, spread=quote.spread,
                timestamp=quote.timestamp or now, candles=candles,
            )
            ctx.spread_monitor.record(symbol, quote.spread)

        # Run scan pipeline
        candidates, reports = ctx.scan_pipeline.scan_universe(pairs, snapshots)

        # Filter held/pending symbols
        held_symbols = {pos.symbol for pos in ctx.tracker.all_positions()}
        pending_symbols = set(ctx.tracker.all_pending_entries().keys())
        candidates = [c for c in candidates if c.symbol not in held_symbols and c.symbol not in pending_symbols]

        # --- Entry logic ---
        if candidates and ctx.state.position_count < ctx.state.max_positions:
            best = candidates[0]
            log.info("[RUNTIME] Best candidate: %s %s score=%.0f",
                     best.symbol, best.strategy, best.score)

            # Spread quality gate
            spread_stats = ctx.spread_monitor.get_stats(best.symbol)
            if spread_stats["mean"] > 0:
                spread_ratio = spread_stats["current"] / spread_stats["mean"]
                if spread_ratio > 1.5:
                    log.warning("[RUNTIME] ENTRY SKIPPED: %s spread elevated (%.1fx mean)",
                                best.symbol, spread_ratio)
                    if self.live_state:
                        self.live_state.update(
                            spread_skips=self.live_state.spread_skips + 1,
                            last_spread_skip=f"{best.symbol} ({spread_ratio:.1f}x)",
                        )
                    candidates = []

            if candidates:
                self._try_entry(best)

        # --- Reconcile pending orders ---
        self._reconcile_pending_orders()

        # --- Manage open positions ---
        self._manage_positions()

        # --- Publish to dashboard ---
        if self.dashboard:
            self.dashboard.publish_cycle(
                broker=ctx.broker,
                state=ctx.state,
                tracker=ctx.tracker,
                execution_audit=ctx.execution_audit,
                dbb_audit=ctx.dbb_audit,
                reports=reports,
                now=now,
            )

        log.debug("[RUNTIME] Cycle %d complete — positions=%d, candidates=%d",
                  ctx.state.cycle_count, ctx.state.position_count, len(candidates))

    # ------------------------------------------------------------------
    # Entry execution
    # ------------------------------------------------------------------

    def _try_entry(self, best) -> None:
        """Attempt to execute the best candidate."""
        ctx = self.ctx
        from scrooge_v3.execution.sizing import SizingCalculator
        from scrooge_v3.execution.stop_planner import StopPlanner

        sizer = SizingCalculator()
        stop_planner = StopPlanner()
        acct = ctx.broker.get_account()
        equity = acct.equity if acct else 10000.0
        inst = ctx.broker.get_instruments().get(best.symbol, {})
        inst_info = {"pipLocation": inst.pip_location, "marginRate": inst.margin_rate} if hasattr(inst, "pip_location") else {}
        free_margin = acct.margin_available if acct else equity
        units = sizer.calculate(best.symbol, best.entry_price, equity, inst_info, free_margin=free_margin)

        if not units or units <= 0:
            return

        quote = ctx.broker.get_price(best.symbol)
        if not quote:
            log.error("[RUNTIME] Cannot get price for %s — skipping entry", best.symbol)
            return

        validated_sl, sl_reason = stop_planner.validate_stop(
            best.direction, best.stop_price,
            quote.bid, quote.ask, quote.spread,
        )
        if sl_reason != "valid":
            log.warning("[RUNTIME] SL adjusted: %s %.5f → %.5f (%s)",
                        best.symbol, best.stop_price, validated_sl, sl_reason)

        trail_ok, trail_reason = stop_planner.should_trail(
            best.direction, best.stop_price, validated_sl,
            quote.spread, ctx.spread_monitor.get_stats(best.symbol).get('mean', quote.spread),
        )
        if not trail_ok and "hostile_spread" in trail_reason:
            log.warning("[RUNTIME] ENTRY SKIPPED: %s spread kill — %s", best.symbol, trail_reason)
            return

        signed_units = units if best.direction.value == "long" else -units
        limit_price = quote.bid if best.direction.value == "long" else quote.ask
        gtd_time = (datetime.now(timezone.utc) + timedelta(minutes=5)).strftime(
            "%Y-%m-%dT%H:%M:%S.000000000Z"
        )

        log.info("[RUNTIME] Placing LIMIT order: %s %s %d units @ %.5f SL=%.5f TP=%.5f GTD=%s",
                 best.symbol, best.direction.value, signed_units,
                 limit_price, validated_sl, best.take_profit or 0, gtd_time)

        result = ctx.broker.place_limit_order(
            symbol=best.symbol, units=signed_units,
            price=limit_price,
            stop_loss=validated_sl, take_profit=best.take_profit,
            gtd_time=gtd_time,
        )

        if result.success and result.trade_id:
            ctx.state.position_count += 1
            ctx.tracker.register_entry(
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
            ctx.state.record_zone_entry(best.symbol, f"{validated_sl:.5f}")
            log.info("[RUNTIME] LIMIT FILLED IMMEDIATELY: %s %s %d units @ %.5f",
                     result.trade_id, best.symbol, signed_units, result.fill_price)
            self._place_harvest_limit(ctx.tracker.get(result.trade_id))
        elif result.success and result.order_id:
            ctx.tracker.register_pending_entry(best.symbol, result.order_id)
            ctx.pending_entry_meta[best.symbol] = {
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

    # ------------------------------------------------------------------
    # Position management
    # ------------------------------------------------------------------

    def _manage_positions(self) -> None:
        """Run management pipeline on all tracked positions."""
        ctx = self.ctx
        from scrooge_v3.execution.stop_planner import StopPlanner
        from scrooge_v3.telemetry.execution_audit import AuditEvent

        open_trades = ctx.broker.get_open_trades()
        broker_ids = {t.trade_id for t in open_trades}
        vanished = ctx.tracker.reconcile_with_broker(broker_ids)
        for tid in vanished:
            tracked = ctx.tracker.get(tid)
            if tracked and tracked.harvest_order_id:
                ctx.broker.cancel_order(tracked.harvest_order_id)
                log.info("[RUNTIME] Cancelled harvest limit %s for vanished trade %s",
                         tracked.harvest_order_id, tid)
            ctx.state.decrement_positions()
        ctx.state.position_count = len(open_trades)

        sp = StopPlanner(self.config.section("execution"))
        audit = ctx.execution_audit

        def _audit(etype, reason, **kw):
            if audit:
                audit.record(AuditEvent(type=etype, reason=reason, **kw))

        for tracked in ctx.tracker.all_positions():
            quote = ctx.broker.get_price(tracked.symbol)
            if not quote:
                continue

            h1 = ctx.broker.get_candles(tracked.symbol, "H1", 24)
            pip = 0.01 if "JPY" in tracked.symbol else 0.0001
            direction = TradeDirection(tracked.direction)

            action = ctx.position_pipeline.manage_position(
                tracked,
                current_price=quote.mid,
                bid=quote.bid,
                ask=quote.ask,
                spread=quote.spread,
                mean_spread=ctx.spread_monitor.get_stats(tracked.symbol).get('mean', quote.spread),
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
                _audit("hold", details.get("reason", "no_action"), **audit_base)
                continue

            new_stop = details.get("new_stop")
            log.info("[RUNTIME] Position %s: action=%s phase=%s profit_r=%.3f details=%s",
                     tracked.trade_id, action.action, phase, profit_r, details)

            if action.action in ("trail", "ratchet", "break_even") and new_stop:
                trail_ok, trail_reason = sp.should_trail(
                    direction, tracked.current_stop, new_stop,
                    quote.spread, quote.spread,
                )
                if not trail_ok:
                    log.warning("[RUNTIME] SL %s BLOCKED (%s): %s spread=%.5f",
                                action.action, trail_reason, tracked.trade_id, quote.spread)
                    _audit("sl_blocked", trail_reason, old_sl=tracked.current_stop,
                           new_sl=new_stop, **audit_base)
                    continue

                validated, reason = sp.validate_stop(
                    direction, new_stop, quote.bid, quote.ask, quote.spread,
                )

                if reason == "valid" or "adjusted" in reason:
                    if direction == TradeDirection.LONG and validated < tracked.current_stop:
                        _audit("sl_blocked", "would_loosen", old_sl=tracked.current_stop,
                               new_sl=validated, **audit_base)
                        continue
                    if direction == TradeDirection.SHORT and validated > tracked.current_stop:
                        _audit("sl_blocked", "would_loosen", old_sl=tracked.current_stop,
                               new_sl=validated, **audit_base)
                        continue
                    success = ctx.broker.modify_stop_loss(tracked.trade_id, validated)
                    if success:
                        old_sl = tracked.current_stop
                        ctx.tracker.update_stop(tracked.trade_id, validated)
                        if action.action == "break_even":
                            ctx.tracker.mark_break_even(tracked.trade_id)
                        log.info("[RUNTIME] SL %s: %s %.5f → %.5f (%s)",
                                 action.action, tracked.trade_id, old_sl, validated, reason)
                        _audit("sl_moved", f"{action.action}_{reason}", old_sl=old_sl,
                               new_sl=validated, **audit_base)
                    else:
                        log.error("[RUNTIME] SL modify failed: %s", tracked.trade_id)
                        _audit("sl_blocked", "broker_reject", old_sl=tracked.current_stop,
                               new_sl=validated, **audit_base)
                else:
                    log.warning("[RUNTIME] SL %s BLOCKED (%s): %s",
                                action.action, reason, tracked.trade_id)
                    _audit("sl_blocked", reason, old_sl=tracked.current_stop,
                           new_sl=new_stop, **audit_base)

            elif action.action == "harvest":
                fraction = details.get("fraction", 0.5)
                close_units = int(tracked.units * fraction)
                if close_units > 0:
                    result = ctx.broker.close_trade(tracked.trade_id, close_units)
                    if result.success:
                        ctx.tracker.mark_tp1_taken(tracked.trade_id)
                        log.info("[RUNTIME] HARVEST: %s closed %d units @ %.5f",
                                 tracked.trade_id, close_units, result.fill_price)
                        _audit("harvest", "tp1_taken", **audit_base)

            elif action.action == "favorable_exit":
                trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
                if trade:
                    method = details.get("method", "market")
                    result = ctx.broker.close_trade(trade.trade_id)
                    if result.success:
                        log.info("[RUNTIME] FAVORABLE EXIT (%s): %s @ %.5f",
                                 method, trade.trade_id, result.fill_price)
                        _audit("favorable_exit", f"{method}_{details.get('reason', '')}", **audit_base)

            elif action.action == "emergency_close":
                trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
                if trade:
                    result = ctx.broker.close_trade(trade.trade_id)
                    if result.success:
                        ctx.state.record_loss(abs(result.realized_pl) if result.realized_pl < 0 else 0)
                        log.warning("[RUNTIME] EMERGENCY CLOSE: %s @ %.5f pl=%.2f reason=%s",
                                    trade.trade_id, result.fill_price,
                                    result.realized_pl, details.get("reason", ""))
                        _audit("emergency_close", details.get("reason", "unknown"), **audit_base)

    # ------------------------------------------------------------------
    # Pending order reconciliation
    # ------------------------------------------------------------------

    def _reconcile_pending_orders(self) -> None:
        """Reconcile pending entry and harvest limit orders with OANDA."""
        ctx = self.ctx
        pending_on_broker = {o.order_id for o in ctx.broker.get_pending_orders()}

        for symbol, order_id in list(ctx.tracker.all_pending_entries().items()):
            if order_id in pending_on_broker:
                continue

            open_trades = ctx.broker.get_open_trades()
            new_trade = None
            for t in open_trades:
                if t.symbol == symbol and not ctx.tracker.get(t.trade_id):
                    new_trade = t
                    break

            if new_trade:
                meta = ctx.pending_entry_meta.pop(symbol, {})
                ctx.tracker.register_entry(
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
                ctx.state.position_count += 1
                ctx.state.record_zone_entry(symbol, f"{new_trade.current_stop:.5f}")
                log.info("[RUNTIME] LIMIT ENTRY FILLED: %s %s @ %.5f (order %s)",
                         new_trade.trade_id, symbol, new_trade.entry_price, order_id)
                ctx.tracker.clear_pending_entry(symbol)
                self._place_harvest_limit(ctx.tracker.get(new_trade.trade_id))
            else:
                ctx.pending_entry_meta.pop(symbol, None)
                ctx.tracker.clear_pending_entry(symbol)
                log.info("[RUNTIME] LIMIT ENTRY EXPIRED: %s order=%s", symbol, order_id)

        for tracked in ctx.tracker.get_positions_with_harvest_orders():
            if tracked.harvest_order_id in pending_on_broker:
                continue
            broker_trade = next(
                (t for t in ctx.broker.get_open_trades() if t.trade_id == tracked.trade_id),
                None,
            )
            if broker_trade and broker_trade.units < tracked.units:
                ctx.tracker.mark_tp1_taken(tracked.trade_id)
                ctx.tracker.clear_harvest_order(tracked.trade_id)
                log.info("[RUNTIME] HARVEST LIMIT FILLED: %s units %.0f → %.0f",
                         tracked.trade_id, tracked.units, broker_trade.units)
            else:
                ctx.tracker.clear_harvest_order(tracked.trade_id)
                log.info("[RUNTIME] HARVEST LIMIT CANCELLED: %s order=%s",
                         tracked.trade_id, tracked.harvest_order_id)

    # ------------------------------------------------------------------
    # Harvest limit placement
    # ------------------------------------------------------------------

    def _place_harvest_limit(self, tracked) -> None:
        """Pre-place a REDUCE_ONLY limit order at TP1 for partial harvest."""
        if not tracked or not tracked.tp1_price or tracked.tp1_taken:
            return
        if tracked.harvest_order_id:
            return

        ctx = self.ctx
        harvest_units = int(tracked.units * 0.5)
        if harvest_units <= 0:
            return

        signed_units = -harvest_units if tracked.direction == "long" else harvest_units

        result = ctx.broker.place_limit_order(
            symbol=tracked.symbol,
            units=signed_units,
            price=tracked.tp1_price,
            stop_loss=None,
            take_profit=None,
            gtd_time=None,
            position_fill="REDUCE_ONLY",
        )

        if result.success and result.order_id:
            ctx.tracker.set_harvest_order(tracked.trade_id, result.order_id)
            log.info("[RUNTIME] HARVEST LIMIT PLACED: %s order=%s @ %.5f (%d units)",
                     tracked.trade_id, result.order_id, tracked.tp1_price, harvest_units)
        elif result.success and result.trade_id:
            ctx.tracker.mark_tp1_taken(tracked.trade_id)
            log.info("[RUNTIME] HARVEST LIMIT FILLED IMMEDIATELY: %s @ %.5f",
                     tracked.trade_id, tracked.tp1_price)
        else:
            log.warning("[RUNTIME] HARVEST LIMIT FAILED: %s error=%s",
                        tracked.trade_id, result.error)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def shutdown(self) -> None:
        """Graceful shutdown."""
        log.info("[RUNTIME] Shutdown requested")
        self._shutdown_requested = True
        self.config.stop_watcher()
        if self.ctx:
            self.ctx.state.persist()

    def _handle_signal(self, signum: int, frame: Any) -> None:
        log.info("[RUNTIME] Received signal %d", signum)
        self.shutdown()

    def _handle_config_change(self, change: dict) -> None:
        """Handle config hot-reload changes."""
        from .events import CONFIG_CHANGED, Event
        path = change.get("path", "")
        new_val = change.get("new")

        parts = path.split(".")
        if len(parts) >= 3 and parts[2] == "mode":
            category = parts[0]
            module_name = parts[1]
            new_mode = str(new_val)
            log.info("[RUNTIME] Config change: %s.%s mode → %s", category, module_name, new_mode)
            if self.ctx:
                self.ctx.registry.set_mode(category, module_name, new_mode)

        if path == "runtime.scan_interval_seconds" and isinstance(new_val, (int, float)) and self.ctx:
            self.ctx.scan_interval = int(new_val)
            log.info("[RUNTIME] Scan interval changed to %ds", self.ctx.scan_interval)

        if self.ctx:
            self.ctx.event_bus.emit(Event(type=CONFIG_CHANGED, payload=change))

    def _interruptible_sleep(self, seconds: float) -> None:
        """Sleep that can be interrupted by shutdown."""
        end = time.monotonic() + seconds
        while time.monotonic() < end and not self._shutdown_requested:
            time.sleep(min(1.0, end - time.monotonic()))
