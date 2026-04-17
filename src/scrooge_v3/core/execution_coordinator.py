"""Execution coordinator — handles order placement and preflight checks.

Owns: sizing, SL validation, spread kill switch, limit order submission,
tracker entry registration, pending entry metadata.

Does NOT own: scanning, position management, dashboard.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from typing import Any

from .types import TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.core.execution_coordinator")


class ExecutionCoordinator:
    """Handles all entry execution logic."""

    def __init__(self, ctx: Any, recovery: Any):
        self.ctx = ctx
        self.recovery = recovery

    def try_execute(self, best: TradeCandidate) -> bool:
        """Attempt to execute the best candidate.

        Returns True if an order was placed (filled or pending).
        """
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
            return False

        quote = ctx.broker.get_price(best.symbol)
        if not quote:
            log.error("[EXEC] Cannot get price for %s — skipping entry", best.symbol)
            return False

        # Validate SL (trigger-side, no-man's-zone)
        validated_sl, sl_reason = stop_planner.validate_stop(
            best.direction, best.stop_price,
            quote.bid, quote.ask, quote.spread,
        )
        if sl_reason != "valid":
            log.warning("[EXEC] SL adjusted: %s %.5f → %.5f (%s)",
                        best.symbol, best.stop_price, validated_sl, sl_reason)

        # Spread kill switch
        trail_ok, trail_reason = stop_planner.should_trail(
            best.direction, best.stop_price, validated_sl,
            quote.spread, ctx.spread_monitor.get_stats(best.symbol).get('mean', quote.spread),
        )
        if not trail_ok and "hostile_spread" in trail_reason:
            log.warning("[EXEC] ENTRY SKIPPED: %s spread kill — %s", best.symbol, trail_reason)
            return False

        # Build order
        signed_units = units if best.direction.value == "long" else -units
        limit_price = quote.bid if best.direction.value == "long" else quote.ask
        gtd_time = (datetime.now(timezone.utc) + timedelta(minutes=5)).strftime(
            "%Y-%m-%dT%H:%M:%S.000000000Z"
        )

        log.info("[EXEC] Placing LIMIT order: %s %s %d units @ %.5f SL=%.5f TP=%.5f GTD=%s",
                 best.symbol, best.direction.value, signed_units,
                 limit_price, validated_sl, best.take_profit or 0, gtd_time)

        result = ctx.broker.place_limit_order(
            symbol=best.symbol, units=signed_units,
            price=limit_price,
            stop_loss=validated_sl, take_profit=best.take_profit,
            gtd_time=gtd_time,
        )

        if result.success and result.trade_id:
            # Immediate fill
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
            log.info("[EXEC] LIMIT FILLED IMMEDIATELY: %s %s %d units @ %.5f",
                     result.trade_id, best.symbol, signed_units, result.fill_price)
            self.recovery._place_harvest_limit(ctx.tracker.get(result.trade_id))
            return True

        elif result.success and result.order_id:
            # Pending — limit order placed, waiting for fill
            ctx.tracker.register_pending_entry(best.symbol, result.order_id)
            ctx.tracker.set_pending_entry_meta(best.symbol, {
                "direction": best.direction.value,
                "stop_loss": validated_sl,
                "take_profit": best.take_profit or 0,
                "tp1_price": best.metadata.get("tp1", 0),
                "strategy": best.strategy,
                "v3_score": int(best.score),
                "metadata": best.metadata,
            })
            log.info("[EXEC] LIMIT ENTRY PLACED: %s %s order=%s @ %.5f",
                     best.symbol, best.direction.value, result.order_id, limit_price)
            return True

        else:
            log.error("[EXEC] LIMIT ORDER FAILED: %s %s error=%s",
                      best.symbol, best.direction.value, result.error)
            return False
