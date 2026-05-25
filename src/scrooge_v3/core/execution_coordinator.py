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

        # REVERSE DIRECTION (Brock 2026-05-25): flip every strategy direction.
        # Bot has delivered 32%% WR over 202 trades / 2 months at 12/10 R:R
        # (break-even is ~45%% WR). Systematically wrong, not random.
        # Flipping should yield ~68%% WR if edge is stable.
        # Config-flag controlled. Default false. Set true to enable experiment.
        try:
            reverse_enabled = bool(ctx.config.get("execution.reverse_direction", False))
        except Exception:
            reverse_enabled = False
        if reverse_enabled:
            from scrooge_v3.core.types import TradeDirection
            original_dir = best.direction.value
            if best.direction == TradeDirection.LONG:
                best.direction = TradeDirection.SHORT
            else:
                best.direction = TradeDirection.LONG
            log.warning(
                "[EXEC] REVERSAL_MODE_ACTIVE symbol=%s strategy=%s flipped %s -> %s",
                best.symbol, best.strategy, original_dir, best.direction.value,
            )
            # Also flip stop and take-profit hints (they were set for original
            # direction). scalper_clamp will override below but in case any
            # path uses these intermediate values, keep them sane.
            if best.stop_price is not None and best.entry_price:
                # If original was long, stop was BELOW entry. For short, stop is ABOVE.
                # Mirror around entry.
                best.stop_price = 2.0 * best.entry_price - best.stop_price
            if best.take_profit is not None and best.entry_price:
                best.take_profit = 2.0 * best.entry_price - best.take_profit

        # Preserve the original signal anchor before we reshape entry geometry.
        signal_entry_price = best.entry_price

        # Compute stop distance in pips for risk-capped sizing (TRADE_MATH).
        try:
            pip_size = 0.01 if any(j in best.symbol for j in ("JPY", "MXN")) else 0.0001
            stop_pips = abs(best.entry_price - best.stop_price) / pip_size if best.stop_price else None
        except Exception:
            stop_pips = None

        # Scalper clamp (Brock 2026-05-21): override zone-based SL/TP with
        # fixed pip distances. Strategies emit wide zone-to-zone targets,
        # but the bot's intent is scalping. We keep a fixed risk unit and
        # fixed TP1 anchor off the original signal price.
        SCALPER_SL_PIPS = 10.0  # Brock 2026-05-21: initial 10-pip stop, ratchet handles tightening
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
                # Override sizer's input -- always one fixed risk unit.
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
        # Shallow pullback execution (Brock 2026-05-25 revision): the 10-pip
        # full-stop pullback (cb958e2) was too extreme — 0% fill rate in asia
        # because price rarely retraces a full risk unit within the 5-min GTD.
        # New: shallow 2-pip pullback for small entry improvement at high fill
        # rate. SL stays anchored to signal at scalper_clamp default (signal -
        # SCALPER_SL_PIPS for long). With BE manager at 0.7R/0.6R (shipped
        # 190b85c), trades get the breathing room they need post-fill.
        LIMIT_PULLBACK_PIPS = 2.0
        pullback_distance = LIMIT_PULLBACK_PIPS * pip_size
        if reverse_enabled:
            # REVERSE MODE (Brock 2026-05-25 v2): "same trades, same entry,
            # just reverse direction." Place LIMIT at exactly the signal
            # price with the flipped direction. That makes the LIMIT
            # marketable on whichever side it sits, fills immediately at the
            # spread's favorable side, and lets scalper_clamp's signal-
            # anchored SL/TP land at the intended 10/12 distances from fill.
            # No pullback — pullback geometry assumed the original direction,
            # and flipping it produced LIMITs the wrong side of market that
            # never filled (order 3904 CAD_JPY 02:25Z is the proof).
            limit_price = signal_entry_price
        elif best.direction.value == "long":
            limit_price = signal_entry_price - pullback_distance
            # SL stays at scalper_clamp value: signal - SCALPER_SL_PIPS
            # TP stays at scalper_clamp value: signal + SCALPER_TP_PIPS
            # (already set by scalper_clamp above, do not override)
        else:
            limit_price = signal_entry_price + pullback_distance
            # SL stays at scalper_clamp value: signal + SCALPER_SL_PIPS
            # TP stays at scalper_clamp value: signal - SCALPER_TP_PIPS

        # Re-validate the reshaped stop against live spread rules.
        validated_sl, sl_reason = stop_planner.validate_stop(
            best.direction, best.stop_price,
            quote.bid, quote.ask, quote.spread,
        )
        if sl_reason != "valid":
            log.warning("[EXEC] reshaped SL adjusted: %s %.5f → %.5f (%s)",
                        best.symbol, best.stop_price, validated_sl, sl_reason)

        gtd_time = (datetime.now(timezone.utc) + timedelta(minutes=5)).strftime(
            "%Y-%m-%dT%H:%M:%S.000000000Z"
        )

        log.info("[EXEC] Placing LIMIT order: %s %s %d units @ %.5f signal=%.5f SL=%.5f TP=%.5f GTD=%s",
                 best.symbol, best.direction.value, signed_units,
                 limit_price, signal_entry_price, validated_sl, best.take_profit or 0, gtd_time)

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
