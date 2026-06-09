"""Position coordinator — manages all open positions each cycle.

Owns: tracker reconciliation, management pipeline dispatch, SL validation,
harvest/exit/emergency execution, execution audit logging.

Does NOT own: scanning, entry placement, dashboard.
"""

from __future__ import annotations

import logging
from typing import Any

from .types import TradeDirection

log = logging.getLogger("scrooge_v3.core.position_coordinator")


class PositionCoordinator:
    """Manages all open positions through the shared management pipeline."""

    def __init__(self, ctx: Any, recovery: Any, config: Any):
        self.ctx = ctx
        self.recovery = recovery
        self.config = config

    def manage_all(self) -> None:
        """Run management pipeline on all tracked positions."""
        ctx = self.ctx
        from scrooge_v3.execution.stop_planner import StopPlanner
        from scrooge_v3.telemetry.execution_audit import AuditEvent

        # Reconcile tracker with broker
        open_trades = self.recovery.reconcile_tracker()

        sp = StopPlanner(self.config.section("execution"))
        audit = ctx.execution_audit

        def _audit(etype, reason, **kw):
            if audit:
                audit.record(AuditEvent(type=etype, reason=reason, **kw))

        # Map broker trade_id -> live units for the double-harvest guard
        live_units_by_id = {t.trade_id: t.units for t in open_trades}

        for tracked in ctx.tracker.all_positions():
            quote = ctx.broker.get_price(tracked.symbol)
            if not quote:
                continue

            h1 = ctx.broker.get_candles(tracked.symbol, "H1", 24)
            # M5 for the exit brain's recent_range (last 13 bars ~= 1h, matching
            # exit_corpus.py training window). H1 stays for the trailing-stop manager.
            m5 = ctx.broker.get_candles(tracked.symbol, "M5", 16)
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
                m5_bars=m5,
                pip_size=pip,
                live_units=live_units_by_id.get(tracked.trade_id),
                tracker=ctx.tracker,
            )

            details = action.details or {}
            profit_r = details.get("profit_r", 0.0)
            phase = details.get("phase", "")
            audit_base = dict(
                trade_id=tracked.trade_id, symbol=tracked.symbol,
                direction=tracked.direction,
                strategy=getattr(tracked, "strategy", "") or "",
                profit_r=profit_r,
                spread=quote.spread, action=action.action,
            )

            if action.action == "hold":
                _audit("hold", details.get("reason", "no_action"), **audit_base)
                continue

            new_stop = details.get("new_stop")
            log.info("[POSITIONS] %s: action=%s phase=%s profit_r=%.3f",
                     tracked.trade_id, action.action, phase, profit_r)

            if action.action in ("trail", "ratchet", "break_even") and new_stop:
                self._handle_sl_action(
                    ctx, sp, direction, tracked, new_stop, quote,
                    action, audit_base, _audit,
                )

            elif action.action == "harvest":
                self._handle_harvest(ctx, tracked, details, audit_base, _audit)

            elif action.action == "favorable_exit":
                self._handle_favorable_exit(
                    ctx, open_trades, action, details, audit_base, _audit,
                )

            elif action.action == "emergency_close":
                self._handle_emergency_close(
                    ctx, open_trades, action, details, audit_base, _audit,
                )

            elif action.action == "green_exit":
                self._handle_green_exit(
                    ctx, tracked, details, quote, audit_base, _audit, live_units_by_id,
                )

    def _handle_sl_action(self, ctx, sp, direction, tracked, new_stop, quote,
                          action, audit_base, _audit) -> None:
        """Execute SL move with full execution physics guards."""
        # 1. Spread kill switch
        trail_ok, trail_reason = sp.should_trail(
            direction, tracked.current_stop, new_stop,
            quote.spread, quote.spread,
        )
        if not trail_ok:
            log.warning("[POSITIONS] SL %s BLOCKED (%s): %s spread=%.5f",
                        action.action, trail_reason, tracked.trade_id, quote.spread)
            _audit("sl_blocked", trail_reason, old_sl=tracked.current_stop,
                   new_sl=new_stop, **audit_base)
            return

        # 2-4. Trigger-side, no-man's-zone, buffer
        validated, reason = sp.validate_stop(
            direction, new_stop, quote.bid, quote.ask, quote.spread,
        )

        if reason == "valid" or "adjusted" in reason:
            # Never loosen stop after spread adjustment
            if direction == TradeDirection.LONG and validated < tracked.current_stop:
                _audit("sl_blocked", "would_loosen", old_sl=tracked.current_stop,
                       new_sl=validated, **audit_base)
                return
            if direction == TradeDirection.SHORT and validated > tracked.current_stop:
                _audit("sl_blocked", "would_loosen", old_sl=tracked.current_stop,
                       new_sl=validated, **audit_base)
                return

            success = ctx.broker.modify_stop_loss(tracked.trade_id, validated)
            if success:
                old_sl = tracked.current_stop
                ctx.tracker.update_stop(tracked.trade_id, validated)
                if action.action == "break_even":
                    ctx.tracker.mark_break_even(tracked.trade_id)
                log.info("[POSITIONS] SL %s: %s %.5f → %.5f (%s)",
                         action.action, tracked.trade_id, old_sl, validated, reason)
                _audit("sl_moved", f"{action.action}_{reason}", old_sl=old_sl,
                       new_sl=validated, **audit_base)
            else:
                log.error("[POSITIONS] SL modify failed: %s", tracked.trade_id)
                _audit("sl_blocked", "broker_reject", old_sl=tracked.current_stop,
                       new_sl=validated, **audit_base)
        else:
            log.warning("[POSITIONS] SL %s BLOCKED (%s): %s",
                        action.action, reason, tracked.trade_id)
            _audit("sl_blocked", reason, old_sl=tracked.current_stop,
                   new_sl=new_stop, **audit_base)

    def _handle_green_exit(self, ctx, tracked, details, quote, audit_base, _audit, live_units_by_id) -> None:
        """Execute one Green Exit ladder action (Brock 2026-06-04).

        OBSERVE mode logs the intended action and executes nothing — used to
        verify the ladder fires correctly on live positions before activating.
        """
        gx = details.get("gx")
        if gx is None:
            return
        try:
            _mgmt = ctx.config.section("management") if hasattr(ctx, "config") else {}
            observe = bool(((_mgmt or {}).get("green_exit", {}) or {}).get("observe", True))
        except Exception:
            observe = True
        tag = "OBSERVE" if observe else "LIVE"
        log.info("[GREEN_EXIT %s] %s kind=%s profit=%.1fp elapsed=%.0fm :: %s",
                 tag, tracked.trade_id, gx.kind, getattr(gx, "profit_pips", 0.0),
                 getattr(gx, "elapsed_min", 0.0), gx.reason)
        meta = tracked.metadata if isinstance(getattr(tracked, "metadata", None), dict) else None

        if observe:
            _audit("green_exit_observe", f"{gx.kind}:{gx.reason}", **audit_base)
            return

        # ---- LIVE execution ----
        if gx.kind == "partial":
            live_rem = live_units_by_id.get(tracked.trade_id, tracked.units)
            orig = getattr(tracked, "original_units", 0.0) or tracked.units
            close_units = int(round(orig * gx.close_fraction))
            close_units = min(close_units, int(live_rem))
            if close_units <= 0:
                _audit("green_exit_skip", f"{gx.tranche}_no_units", **audit_base)
                return
            res = ctx.broker.close_trade(tracked.trade_id, close_units)
            if getattr(res, "success", False):
                if meta is not None:
                    meta[f"gx_{gx.tranche}_done"] = True
                if gx.tranche == "tp1":
                    try:
                        ctx.tracker.mark_tp1_taken(tracked.trade_id)
                    except Exception:
                        pass
                    if gx.move_sl_after is not None:
                        _prec = 3 if any(j in tracked.symbol for j in ("JPY", "MXN")) else 5
                        ctx.broker.modify_stop_loss(tracked.trade_id, round(gx.move_sl_after, _prec))
                ctx.tracker.persist()
                log.info("[GREEN_EXIT LIVE] %s %s closed %d units (SL->%s)",
                         tracked.trade_id, gx.tranche, close_units,
                         f"{gx.move_sl_after:.5f}" if gx.move_sl_after else "unchanged")
                _audit("green_exit", f"{gx.tranche}_closed_{close_units}", **audit_base)

        elif gx.kind == "limit_exit":
            # Rest a closing LIMIT at gx.limit_price by setting the trade's TP
            # (server-side, survives bot downtime). 4h harvest = 0.5p past tick;
            # Phase-2 = +7.5p. Once armed, the manager stops re-emitting.
            if gx.limit_price is not None:
                _prec = 3 if any(j in tracked.symbol for j in ("JPY", "MXN")) else 5
                ok = ctx.broker.modify_take_profit(tracked.trade_id, round(gx.limit_price, _prec))
                if ok:
                    if meta is not None:
                        meta["gx_harvest_armed"] = True
                        meta["gx_green_exit"] = bool(gx.green)  # tag for no-cooldown on this close
                        ctx.tracker.persist()
                    _audit("green_exit", f"limit_armed@{round(gx.limit_price, _prec)}_green={gx.green}", **audit_base)
                    log.info("[GREEN_EXIT LIVE] %s limit harvest armed @ %.5f (%s)",
                             tracked.trade_id, gx.limit_price, gx.reason)

        elif gx.kind == "enter_phase2":
            if meta is not None:
                meta["gx_phase2"] = True
                ctx.tracker.persist()
            _audit("green_exit", "enter_phase2", **audit_base)

        elif gx.kind == "scan_tick":
            if meta is not None:
                meta["gx_last_scan_min"] = round(getattr(gx, "elapsed_min", 0.0), 1)
                ctx.tracker.persist()

    def _handle_harvest(self, ctx, tracked, details, audit_base, _audit) -> None:
        """Execute partial harvest using broker-authoritative remaining units.

        Reading tracked.units directly is unsafe: if a prior partial already
        reduced the broker side but the tracker wasn't synced, we'd close
        half of the ORIGINAL size and leave dust (or over-close and fail).
        Always anchor on broker truth before computing close size.
        """
        fraction = details.get("fraction", 0.5)

        open_trades = ctx.broker.get_open_trades()
        if open_trades is None:
            log.warning("[POSITIONS] HARVEST SKIPPED — broker view unavailable for %s", tracked.trade_id)
            _audit("harvest_blocked", "broker_view_unavailable", **audit_base)
            return
        broker = next((t for t in open_trades if t.trade_id == tracked.trade_id), None)
        if not broker:
            log.warning("[POSITIONS] HARVEST skipped: trade %s not found on broker",
                        tracked.trade_id)
            _audit("harvest_blocked", "trade_missing_on_broker", **audit_base)
            return

        remaining = broker.units
        # If tracker is stale, update it so downstream sees truth.
        if remaining != tracked.units:
            ctx.tracker.update_units(tracked.trade_id, remaining)

        close_units = int(remaining * fraction)
        if close_units <= 0:
            log.info("[POSITIONS] HARVEST skipped: %s remaining=%.0f fraction=%.2f",
                     tracked.trade_id, remaining, fraction)
            return

        result = ctx.broker.close_trade(tracked.trade_id, close_units)
        if result.success:
            new_remaining = remaining - close_units
            ctx.tracker.update_units(tracked.trade_id, new_remaining)
            ctx.tracker.mark_tp1_taken(tracked.trade_id)
            ctx.tracker.clear_harvest_order(tracked.trade_id)
            log.info("[POSITIONS] HARVEST: %s closed %d units @ %.5f (remaining=%d)",
                     tracked.trade_id, close_units, result.fill_price, new_remaining)
            _audit("harvest", "tp1_taken", **audit_base)

    def _handle_favorable_exit(self, ctx, open_trades, action, details,
                                audit_base, _audit) -> None:
        """Execute favorable exit (limit or market)."""
        trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
        if trade:
            method = details.get("method", "market")
            result = ctx.broker.close_trade(trade.trade_id)
            if result.success:
                log.info("[POSITIONS] FAVORABLE EXIT (%s): %s @ %.5f",
                         method, trade.trade_id, result.fill_price)
                _audit("favorable_exit", f"{method}_{details.get('reason', '')}", **audit_base)

    def _handle_emergency_close(self, ctx, open_trades, action, details,
                                 audit_base, _audit) -> None:
        """Execute emergency close."""
        trade = next((t for t in open_trades if t.trade_id == action.position_id), None)
        if trade:
            result = ctx.broker.close_trade(trade.trade_id)
            if result.success:
                ctx.state.record_loss(abs(result.realized_pl) if result.realized_pl < 0 else 0)
                log.warning("[POSITIONS] EMERGENCY CLOSE: %s @ %.5f pl=%.2f reason=%s",
                            trade.trade_id, result.fill_price,
                            result.realized_pl, details.get("reason", ""))
                _audit("emergency_close", details.get("reason", "unknown"), **audit_base)
