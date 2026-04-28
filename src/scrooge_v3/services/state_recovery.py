"""State recovery — handles trade reconciliation and vanished trade detection.

Extracted from Runtime._run_cycle() (vanished trade detection) and
Runtime._reconcile_pending_orders() to isolate recovery/reconciliation
logic from normal trading flow.
"""

from __future__ import annotations

import logging
from typing import Any

log = logging.getLogger("scrooge_v3.services.state_recovery")


class StateRecovery:
    """Reconciles broker state with local tracker state each cycle."""

    def __init__(self, ctx: Any):
        self.ctx = ctx

    def detect_vanished_trades(self) -> None:
        """Detect trades closed externally between cycles."""
        ctx = self.ctx
        current_trades = ctx.broker.get_open_trades()
        current_ids = {t.trade_id for t in current_trades}
        vanished = ctx.known_trade_ids - current_ids

        if vanished:
            for tid in vanished:
                log.warning("[RECOVERY] Trade vanished (closed externally): %s", tid)
                ctx.state.decrement_positions()

        ctx.known_trade_ids = current_ids
        ctx.state.position_count = len(current_trades)

    def reconcile_tracker(self) -> None:
        """Reconcile position tracker with broker — detect vanished tracked positions."""
        ctx = self.ctx
        open_trades = ctx.broker.get_open_trades()
        broker_ids = {t.trade_id for t in open_trades}

        # Phase 4: snapshot tracked positions BEFORE reconcile strips
        # them, so signal-discipline can inspect entry/stop/direction.
        pre_snapshot: dict[str, Any] = {}
        try:
            for _tid, _pos in ctx.tracker._positions.items():
                pre_snapshot[_tid] = _pos
        except Exception:
            pre_snapshot = {}

        vanished = ctx.tracker.reconcile_with_broker(broker_ids)

        for tid in vanished:
            tracked = pre_snapshot.get(tid) or ctx.tracker.get(tid)
            if tracked and hasattr(tracked, 'harvest_order_id') and tracked.harvest_order_id:
                ctx.broker.cancel_order(tracked.harvest_order_id)
                log.info("[RECOVERY] Cancelled harvest limit %s for vanished trade %s",
                         tracked.harvest_order_id, tid)

            # Phase 4: classify vanish, book realized PnL, cooldown + blacklist.
            try:
                self._record_vanish_for_signal_discipline(tid, tracked)
            except Exception:
                log.exception("[RECOVERY] signal-discipline hook failed: %s", tid)

            ctx.state.decrement_positions()

        ctx.state.position_count = len(open_trades)
        return open_trades

    def _record_vanish_for_signal_discipline(
        self, trade_id: str, tracked: Any,
    ) -> None:
        """Record cooldown/blacklist and daily PnL on a vanished trade.

        Heuristic for SL-hit: use the broker's realized-PnL-today delta
        since the last sample. A non-positive delta classifies as a
        stop-loss and records a cooldown + zone blacklist. All deltas
        feed the daily circuit breaker.
        """
        ctx = self.ctx
        tracker_obj = getattr(ctx, "cooldown_tracker", None)
        if tracker_obj is None:
            return

        broker = ctx.broker
        # Per-trade close attribution. Previously we used the brokers daily
        # P&L delta to estimate this trades P&L, but if two trades vanish
        # in the same cycle the first consumes the whole delta and the
        # second is wrongly tagged as a stop-loss. Now we ask OANDA for the
        # trades own realizedPL, which is the truthful per-close number.
        pnl_delta = 0.0
        per_trade_pl = None
        try:
            if hasattr(broker, "get_trade"):
                tdata = broker.get_trade(trade_id)
                if tdata is not None:
                    raw_pl = tdata.get("realizedPL")
                    if raw_pl is not None:
                        per_trade_pl = float(raw_pl)
                        # Add financing if present, subtract commission.
                        per_trade_pl += float(tdata.get("financing", 0) or 0)
        except Exception:
            log.exception("[RECOVERY] get_trade(%s) failed; falling back to daily delta", trade_id)

        if per_trade_pl is not None:
            pnl_delta = per_trade_pl
        else:
            # Fallback: legacy daily-aggregate delta heuristic.
            try:
                total_today = 0.0
                if hasattr(broker, "get_realized_pl_today"):
                    total_today = float(broker.get_realized_pl_today() or 0.0)
                last = getattr(ctx, "_last_realized_pl_today", 0.0)
                pnl_delta = total_today - last
                ctx._last_realized_pl_today = total_today
                log.warning("[RECOVERY] using daily-delta fallback for %s pnl=%.2f", trade_id, pnl_delta)
            except Exception:
                log.exception("[RECOVERY] failed to read realized_pl_today")

        acct = None
        try:
            acct = broker.get_account()
        except Exception:
            acct = None
        equity_ref = getattr(acct, "equity", None) if acct else None
        if pnl_delta != 0.0:
            tracker_obj.record_realized_pnl(
                pnl_delta, equity_start=equity_ref,
            )

        if tracked is None:
            return
        if pnl_delta <= 0:
            symbol = getattr(tracked, "symbol", None)
            direction = getattr(tracked, "direction", None)
            entry_price = getattr(tracked, "entry_price", None)
            if symbol and direction:
                tracker_obj.record_stop(
                    symbol=symbol,
                    direction=direction,
                    entry_price=entry_price,
                    reason="stop_loss_or_close",
                )
                log.warning(
                    "[RECOVERY] SL classification: %s %s %s pnl_delta=%.2f "
                    "-> cooldown + blacklist",
                    trade_id, symbol, direction, pnl_delta,
                )

    def reconcile_pending_orders(self) -> None:
        """Reconcile pending entry and harvest limit orders with OANDA."""
        ctx = self.ctx
        pending_on_broker = {o.order_id for o in ctx.broker.get_pending_orders()}

        # Check pending entries
        for symbol, order_id in list(ctx.tracker.all_pending_entries().items()):
            if order_id in pending_on_broker:
                continue  # Still pending, wait

            # Order gone — check if it filled (new trade appeared)
            open_trades = ctx.broker.get_open_trades()
            new_trade = None
            for t in open_trades:
                if t.symbol == symbol and not ctx.tracker.get(t.trade_id):
                    new_trade = t
                    break

            if new_trade:
                meta = ctx.tracker.get_pending_entry_meta(symbol)
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
                log.info("[RECOVERY] LIMIT ENTRY FILLED: %s %s @ %.5f (order %s)",
                         new_trade.trade_id, symbol, new_trade.entry_price, order_id)
                # Phase 4: fill resets expiry counter.
                tracker_obj = getattr(ctx, "cooldown_tracker", None)
                if tracker_obj is not None:
                    try:
                        tracker_obj.record_fill(
                            symbol, new_trade.direction, new_trade.entry_price,
                        )
                    except Exception:
                        log.exception("[RECOVERY] expiry reset on fill failed")
                ctx.tracker.clear_pending_entry(symbol)
                # Place harvest limit for the new trade
                self._place_harvest_limit(ctx.tracker.get(new_trade.trade_id))
            else:
                # Order expired or was cancelled
                meta = ctx.tracker.get_pending_entry_meta(symbol) or {}
                ctx.tracker.clear_pending_entry_meta(symbol)
                ctx.tracker.clear_pending_entry(symbol)
                log.info("[RECOVERY] LIMIT ENTRY EXPIRED: %s order=%s", symbol, order_id)
                # Phase 4: feed expiry tracker for anti-thrash.
                tracker_obj = getattr(ctx, "cooldown_tracker", None)
                if tracker_obj is not None:
                    try:
                        direction = meta.get("direction")
                        anchor = (
                            meta.get("entry_price")
                            or meta.get("stop_loss")
                            or 0.0
                        )
                        if direction and anchor:
                            tracker_obj.record_expiry(
                                symbol, direction, float(anchor),
                            )
                    except Exception:
                        log.exception("[RECOVERY] expiry tracker hook failed")

        # Check harvest orders
        for tracked in ctx.tracker.get_positions_with_harvest_orders():
            if tracked.harvest_order_id in pending_on_broker:
                continue  # Still pending

            broker_trade = next(
                (t for t in ctx.broker.get_open_trades() if t.trade_id == tracked.trade_id),
                None,
            )
            if broker_trade and broker_trade.units < tracked.units:
                old_units = tracked.units
                # Sync unit truth BEFORE flag — so downstream reads see the
                # correct remaining size if they happen between these calls.
                ctx.tracker.update_units(tracked.trade_id, broker_trade.units)
                ctx.tracker.mark_tp1_taken(tracked.trade_id)
                ctx.tracker.clear_harvest_order(tracked.trade_id)
                log.info("[RECOVERY] HARVEST LIMIT FILLED: %s units %.0f → %.0f",
                         tracked.trade_id, old_units, broker_trade.units)
                # Dust check — if the remaining size is below threshold,
                # flatten the residual so we don't carry orphan units.
                self._maybe_flatten_dust(tracked, broker_trade.units)
            else:
                ctx.tracker.clear_harvest_order(tracked.trade_id)
                log.info("[RECOVERY] HARVEST LIMIT CANCELLED: %s order=%s",
                         tracked.trade_id, tracked.harvest_order_id)

    def _dust_threshold(self) -> float:
        """Units below which a residual is considered accounting dust."""
        try:
            mgmt = self.ctx.config.section("management") if hasattr(self.ctx, "config") else {}
            if isinstance(mgmt, dict):
                return float(mgmt.get("dust_unit_threshold", 2))
        except Exception:
            pass
        return 2.0

    def _maybe_flatten_dust(self, tracked, remaining_units: float) -> None:
        """If remaining broker units are at/below the dust threshold, flatten.

        After a partial close, tiny residuals (1-2 units) are just accounting
        noise — they can't be meaningfully managed and generate log spam.
        Market-close them and let the normal vanish path clean up the tracker.
        """
        threshold = self._dust_threshold()
        if remaining_units <= 0 or remaining_units > threshold:
            return
        log.warning(
            "[RECOVERY] DUST FLATTEN: %s remaining=%.0f <= threshold=%.0f",
            tracked.trade_id, remaining_units, threshold,
        )
        try:
            result = self.ctx.broker.close_trade(tracked.trade_id)
            if getattr(result, "success", False):
                log.info("[RECOVERY] DUST FLATTENED: %s pl=%.2f",
                         tracked.trade_id, getattr(result, "realized_pl", 0.0))
            else:
                log.warning("[RECOVERY] DUST FLATTEN FAILED: %s error=%s",
                            tracked.trade_id, getattr(result, "error", "?"))
        except Exception:
            log.exception("[RECOVERY] DUST FLATTEN raised: %s", tracked.trade_id)

    def _place_harvest_limit(self, tracked) -> None:
        """Pre-place a REDUCE_ONLY limit order at TP1 for partial harvest."""
        if not tracked or not tracked.tp1_price or tracked.tp1_taken:
            return
        if hasattr(tracked, 'harvest_order_id') and tracked.harvest_order_id:
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
            log.info("[RECOVERY] HARVEST LIMIT PLACED: %s order=%s @ %.5f (%d units)",
                     tracked.trade_id, result.order_id, tracked.tp1_price, harvest_units)
        elif result.success and result.trade_id:
            ctx.tracker.mark_tp1_taken(tracked.trade_id)
            log.info("[RECOVERY] HARVEST LIMIT FILLED IMMEDIATELY: %s @ %.5f",
                     tracked.trade_id, tracked.tp1_price)
        else:
            log.warning("[RECOVERY] HARVEST LIMIT FAILED: %s error=%s",
                        tracked.trade_id, result.error)
