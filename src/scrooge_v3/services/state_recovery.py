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
        vanished = ctx.tracker.reconcile_with_broker(broker_ids)

        for tid in vanished:
            tracked = ctx.tracker.get(tid)
            if tracked and hasattr(tracked, 'harvest_order_id') and tracked.harvest_order_id:
                ctx.broker.cancel_order(tracked.harvest_order_id)
                log.info("[RECOVERY] Cancelled harvest limit %s for vanished trade %s",
                         tracked.harvest_order_id, tid)
            ctx.state.decrement_positions()

        ctx.state.position_count = len(open_trades)
        return open_trades

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
                ctx.tracker.clear_pending_entry(symbol)
                # Place harvest limit for the new trade
                self._place_harvest_limit(ctx.tracker.get(new_trade.trade_id))
            else:
                # Order expired or was cancelled
                ctx.tracker.clear_pending_entry_meta(symbol)
                ctx.tracker.clear_pending_entry(symbol)
                log.info("[RECOVERY] LIMIT ENTRY EXPIRED: %s order=%s", symbol, order_id)

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
            else:
                ctx.tracker.clear_harvest_order(tracked.trade_id)
                log.info("[RECOVERY] HARVEST LIMIT CANCELLED: %s order=%s",
                         tracked.trade_id, tracked.harvest_order_id)


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
