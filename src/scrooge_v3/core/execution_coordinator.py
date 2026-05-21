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

        risk_cfg = ctx.config.section("risk") if hasattr(ctx, "config") else {}
        sizer = SizingCalculator(config=risk_cfg)
        stop_planner = StopPlanner()
        acct = ctx.broker.get_account()
        equity = acct.equity if acct else 10000.0
        inst = ctx.broker.get_instruments().get(best.symbol, {})
        inst_info = {"pipLocation": inst.pip_location, "marginRate": inst.margin_rate} if hasattr(inst, "pip_location") else {}
        free_margin = acct.margin_available if acct else equity

        # Cross-pair USD conversion lookup — returns base_ccy -> USD rate, or None.
        def _usd_conversion(ccy: str) -> float | None:
            if ccy == "USD":
                return 1.0
            q = ctx.broker.get_price(f"{ccy}_USD")
            if q and q.mid > 0:
                return q.mid
            q = ctx.broker.get_price(f"USD_{ccy}")
            if q and q.mid > 0:
                return 1.0 / q.mid
            return None

        # Compute stop distance in pips for risk-capped sizing (TRADE_MATH).
        try:
            pip_size = 0.01 if any(j in best.symbol for j in ("JPY", "MXN")) else 0.0001
            stop_pips = abs(best.entry_price - best.stop_price) / pip_size if best.stop_price else None
        except Exception:
            stop_pips = None

        # Scalper clamp (Brock 2026-05-21): override zone-based SL/TP with
        # fixed pip distances. Strategies emit wide zone-to-zone targets,
        # but the bot's intent is scalping. SL at 6 pips, TP at 12 pips
        # (2:1 R:R, breakeven WR 33.3%, win = 0.60% account, loss = 0.30%).
        SCALPER_SL_PIPS = 6.0
        SCALPER_TP_PIPS = 12.0
        try:
            if best.entry_price and pip_size > 0:
                pre_sl = best.stop_price
                pre_tp = best.take_profit
                if best.direction.value == "long":
                    best.stop_price = best.entry_price - SCALPER_SL_PIPS * pip_size
                    best.take_profit = best.entry_price + SCALPER_TP_PIPS * pip_size
                else:
                    best.stop_price = best.entry_price + SCALPER_SL_PIPS * pip_size
                    best.take_profit = best.entry_price - SCALPER_TP_PIPS * pip_size
                # Override sizer's input -- always 6 pips
                stop_pips = SCALPER_SL_PIPS
                log.info(
                    "[EXEC] scalper_clamp symbol=%s dir=%s entry=%.5f "
                    "pre_SL=%.5f pre_TP=%.5f -> SL=%.5f TP=%.5f "
                    "pip_risk=%.1f pip_target=%.1f",
                    best.symbol, best.direction.value, best.entry_price,
                    pre_sl or 0.0, pre_tp or 0.0,
                    best.stop_price, best.take_profit,
                    SCALPER_SL_PIPS, SCALPER_TP_PIPS,
                )
        except Exception:
            log.exception("[EXEC] scalper_clamp failed; falling back to strategy SL/TP")

        units = sizer.calculate(
            best.symbol, best.entry_price, equity, inst_info,
            free_margin=free_margin,
            usd_conversion_lookup=_usd_conversion,
            stop_distance_pips=stop_pips,
        )

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

        # Entry spread preflight (dedicated — was previously bypassed because
        # should_trail() returns new_stop_not_tighter on fresh entries before
        # ever evaluating spread).
        mean_spread = ctx.spread_monitor.get_stats(best.symbol).get('mean', quote.spread)
        hostile, hostile_reason = stop_planner.is_entry_spread_hostile(
            quote.spread, mean_spread,
        )
        if hostile:
            log.warning("[EXEC] ENTRY SKIPPED: %s spread kill — %s", best.symbol, hostile_reason)
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

        # Phase 4: direction flip resets opposite-direction expiry counters.
        tracker_obj = getattr(ctx, "cooldown_tracker", None)
        if tracker_obj is not None:
            try:
                tracker_obj.record_direction_flip(best.symbol, best.direction.value)
            except Exception:
                log.exception("[EXEC] direction-flip hook failed")

        result = ctx.broker.place_limit_order(
            symbol=best.symbol, units=signed_units,
            price=limit_price,
            stop_loss=validated_sl, take_profit=best.take_profit,
            gtd_time=gtd_time,
        )

        # Patch B.right: capture (order_id → strategy) at placement so
        # downstream ml-observer can resolve attribution by orderID from the
        # OANDA fill transaction, not by walking scans.jsonl backward.
        attrib = getattr(ctx, "order_attribution", None)
        cycle = getattr(getattr(ctx, "state", None), "cycle_count", None)
        tier = best.metadata.get("v3_tier", "") if best.metadata else ""

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
            if attrib is not None:
                # Immediate fills come back with trade_id (no separate order_id);
                # attribute under the trade_id so ml-observer's tradeID lookup
                # resolves either way.
                attrib.record(
                    order_id=result.trade_id, symbol=best.symbol,
                    strategy=best.strategy, direction=best.direction.value,
                    score=best.score, tier=str(tier), scan_cycle=cycle,
                    order_kind="entry_immediate_fill",
                )
            self.recovery._place_harvest_limit(ctx.tracker.get(result.trade_id))
            return True

        elif result.success and result.order_id:
            # Pending — limit order placed, waiting for fill
            ctx.tracker.register_pending_entry(best.symbol, result.order_id)
            ctx.tracker.set_pending_entry_meta(best.symbol, {
                "direction": best.direction.value,
                "stop_loss": validated_sl,
                "entry_price": limit_price,
                "take_profit": best.take_profit or 0,
                "tp1_price": best.metadata.get("tp1", 0),
                "strategy": best.strategy,
                "v3_score": int(best.score),
                "metadata": best.metadata,
            })
            log.info("[EXEC] LIMIT ENTRY PLACED: %s %s order=%s @ %.5f",
                     best.symbol, best.direction.value, result.order_id, limit_price)
            if attrib is not None:
                attrib.record(
                    order_id=result.order_id, symbol=best.symbol,
                    strategy=best.strategy, direction=best.direction.value,
                    score=best.score, tier=str(tier), scan_cycle=cycle,
                    order_kind="entry_limit",
                )
            return True

        else:
            log.error("[EXEC] LIMIT ORDER FAILED: %s %s error=%s",
                      best.symbol, best.direction.value, result.error)
            return False
