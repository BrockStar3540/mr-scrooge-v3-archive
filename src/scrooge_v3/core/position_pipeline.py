"""Position pipeline — manages all open positions.

Replaces V2 coordinator's position management logic (lines 358-427,
694-1027, 1265-1291).

Orchestrates: stop updates, trailing, partial harvest, break-even,
ratchet, favorable exit, emergency close.

Profit-phase aware: trades progress through EARLY_HOLD → LOCK → HARVEST
phases based on profit-R, controlling when trailing/ratchet activate.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

from .trade_geometry import pip_size as _pip_size
from .events import (
    POSITION_CLOSED,
    STOP_UPDATE_ATTEMPTED,
    STOP_UPDATE_BLOCKED,
    STOP_UPDATED,
    Event,
    EventBus,
)
from .types import TradeDirection

log = logging.getLogger("scrooge_v3.core.position_pipeline")


@dataclass
class ManagementAction:
    """Result of managing one position."""

    position_id: str
    action: str  # "hold", "trail", "ratchet", "break_even", "harvest", "favorable_exit", "close", "emergency_close"
    details: dict[str, Any] | None = None


class PositionPipeline:
    """Orchestrates all position management logic.

    Profit-phase chain:
      0. Compute profit_r (profit / initial risk)
      1. Emergency close check (always runs)
      2. Partial harvest check (always runs)
      3. Break-even check (always runs)
      4. Profit phase gate:
         - EARLY_HOLD (< 0.5R): skip ratchet/trail
         - LOCK (0.5-0.8R): normal ratchet/trail
         - HARVEST (>= 0.8R): aggressive ratchet/trail
      5. Spread guard on ratchet (same as trail)
      6. Min-step filter (prevents thrashing)
      7. Trailing stop check
      8. Stop validation (trigger-side, no-man's-zone)
    """

    def __init__(
        self,
        trail_manager: Any = None,
        ratchet_manager: Any = None,
        be_manager: Any = None,
        harvest_manager: Any = None,
        favorable_exit_manager: Any = None,
        emergency_manager: Any = None,
        stop_planner: Any = None,
        event_bus: EventBus | None = None,
        exit_config: dict | None = None,
        green_exit_manager: Any = None,
    ):
        self.trail = trail_manager
        self.ratchet = ratchet_manager
        self.be = be_manager
        self.harvest = harvest_manager
        self.favorable_exit = favorable_exit_manager
        self.emergency = emergency_manager
        self.stop_planner = stop_planner
        self.event_bus = event_bus
        self.green_exit = green_exit_manager

        # Exit manager config
        cfg = exit_config or {}
        self.early_hold_r = cfg.get("early_hold_threshold_r", 0.5)
        self.lock_r = cfg.get("lock_threshold_r", 0.8)
        self.min_sl_step_pips = cfg.get("min_sl_step_pips", 3.0)

    def manage_position(
        self,
        position: Any,
        current_price: float,
        bid: float,
        ask: float,
        spread: float,
        mean_spread: float = 0.0,
        hourly_bars: Any = None,
        m5_bars: Any = None,
        pip_size: float = 0.0001,
        live_units: float | None = None,
        tracker: Any = None,
    ) -> ManagementAction:
        """Run the full management chain for one position.

        Returns the highest-priority action to take.

        Args:
            live_units: broker-authoritative unit count (if different from
                position.units, the pre-placed harvest has already filled).
            tracker: PositionTracker — used to mark tp1_taken when a
                broker-observed reduction is detected.
        """
        # --- Green Exit ladder (Brock 2026-06-04) — top priority when enabled ---
        if self.green_exit is not None and getattr(self.green_exit, "enabled", False):
            try:
                _gx = self.green_exit.check(position, current_price, pip_size, bid=bid, ask=ask, hourly_bars=hourly_bars, m5_bars=m5_bars)
            except Exception:
                log.exception("[PIPELINE] green_exit.check failed")
                _gx = None
            if _gx is not None:
                _gpid = getattr(position, "trade_id", None) or getattr(position, "position_id", str(id(position)))
                try:
                    from scrooge_v3.management.green_exit import _xlog
                    _xlog(kind=getattr(_gx, "kind", "?"), tranche=getattr(_gx, "tranche", None),
                          trade_id=str(_gpid), symbol=getattr(position, "symbol", "?"),
                          reason=str(getattr(_gx, "reason", ""))[:120])
                except Exception:
                    pass
                return ManagementAction(position_id=_gpid, action="green_exit", details={"gx": _gx})

        pos_id = getattr(position, "position_id", None) or getattr(position, "trade_id", str(id(position)))
        direction = TradeDirection(getattr(position, "direction", "long"))
        entry_price = getattr(position, "entry_price", 0.0)
        current_stop = getattr(position, "current_stop", 0.0)

        # Phase 3 / Bug I: update MFE (peak) each cycle so ratchet can anchor
        # its lock on peak price, not current — retracement can't unlock gains.
        peak_price = getattr(position, "peak_price", 0.0) or entry_price
        if tracker is not None:
            try:
                if tracker.update_peak(pos_id, current_price):
                    peak_price = getattr(position, "peak_price", peak_price)
            except Exception as exc:  # pragma: no cover — defensive
                log.warning("[PIPELINE] update_peak failed for %s: %s", pos_id, exc)
        else:
            # Inline update when no tracker is provided (tests, bootstrap).
            if direction == TradeDirection.LONG and current_price > peak_price:
                peak_price = current_price
            elif direction == TradeDirection.SHORT and (peak_price <= 0 or current_price < peak_price):
                peak_price = current_price

        # --- Compute profit-R for phase selection ---
        # BUG FIX: use initial_risk_distance (snapshotted at entry), NOT the
        # dynamic entry-to-current_stop distance. After BE, the latter shrinks
        # to near-zero and profit_r balloons, triggering premature HARVEST phase.
        initial_risk = getattr(position, "initial_risk_distance", 0.0)
        if initial_risk <= 0:
            # Fallback for positions registered before this field existed
            initial_risk = abs(entry_price - current_stop) if current_stop else 0.0
        risk_distance = initial_risk

        if direction == TradeDirection.LONG:
            profit_distance = current_price - entry_price
        else:
            profit_distance = entry_price - current_price

        profit_r = profit_distance / risk_distance if risk_distance > 0 else 0.0

        # --- Management profile branching ---
        profile = "default"
        if hasattr(position, "metadata") and isinstance(position.metadata, dict):
            profile = position.metadata.get("management_profile", "default")

        if profile == "trend_runner":
            effective_early_hold_r = 0.6   # More patience before trailing
            effective_min_sl_step = 4.0    # Wider steps, less thrashing
        elif profile == "reversal_core":
            effective_early_hold_r = self.early_hold_r
            effective_min_sl_step = self.min_sl_step_pips
        else:
            effective_early_hold_r = self.early_hold_r
            effective_min_sl_step = self.min_sl_step_pips

        # Determine phase using profile-aware threshold
        if profit_r < effective_early_hold_r:
            phase = "EARLY_HOLD"
        elif profit_r < self.lock_r:
            phase = "LOCK"
        else:
            phase = "HARVEST"

        # Build details dict with phase info for audit
        phase_info = {"phase": phase, "profit_r": round(profit_r, 3), "profile": profile}

        # 1. Partial harvest — broker-authoritative to prevent double-harvest race.
        #
        # Race: pre-placed harvest limit fills at broker; local tp1_taken and
        # live units aren't updated until StateRecovery.reconcile_pending_orders
        # runs. In that window, the old code fired a second market harvest.
        #
        # Guard order:
        #   A. If broker live_units < original_units -> limit already filled.
        #      Mark tp1_taken, clear stale harvest_order_id, skip harvest.
        #   B. If harvest_order_id is set -> limit still pending, skip harvest.
        #   C. Otherwise consult harvest manager.
        if self.harvest:
            harvest_order_id = getattr(position, "harvest_order_id", "")
            original_units = getattr(position, "original_units", 0.0) or getattr(position, "units", 0.0)
            effective_live_units = live_units if live_units is not None else getattr(position, "units", 0.0)
            tp1_taken = getattr(position, "tp1_taken", False)

            # Guard A: broker shows a reduction — limit must have filled.
            if (
                original_units > 0
                and effective_live_units > 0
                and effective_live_units < original_units - 0.5  # tolerate fp
                and not tp1_taken
            ):
                if tracker is not None:
                    try:
                        tracker.mark_tp1_taken(pos_id)
                        if harvest_order_id:
                            tracker.clear_harvest_order(pos_id)
                    except Exception as exc:  # pragma: no cover — defensive
                        log.warning("[HARVEST-GUARD] tracker update failed for %s: %s",
                                    pos_id, exc)
                log.info(
                    "[HARVEST-GUARD] %s: broker live_units=%.0f < original=%.0f "
                    "— limit already filled, skipping market harvest.",
                    pos_id, effective_live_units, original_units,
                )
                # Fall through to other management (BE, trail, etc.)

            elif harvest_order_id:
                # Guard B: limit pending on broker — do NOT fire market harvest.
                pass

            else:
                # Guard C: no pre-placed limit, no broker reduction — safe to check.
                tp1 = getattr(position, "tp1_price", None) or (
                    position.metadata.get("tp1", 0) if hasattr(position, "metadata") else 0
                )
                if tp1:
                    harvest_action = self.harvest.check_harvest(
                        pos_id, direction, current_price, tp1, tp1_taken,
                    )
                    if harvest_action:
                        return ManagementAction(
                            position_id=pos_id,
                            action="harvest",
                            details={
                                "fraction": harvest_action.close_fraction,
                                "target": harvest_action.target_label,
                                **phase_info,
                            },
                        )

        # 2. Break-even check (always runs — risk removal is never gated)
        if self.be:
            partial_taken = getattr(position, "tp1_taken", False)
            be_plan = self.be.should_move_to_be(
                direction, entry_price, current_price, current_stop,
                pip_size, partial_taken,
                initial_risk_distance=risk_distance,
            )
            if be_plan:
                try:
                    from scrooge_v3.management.green_exit import _xlog
                    _xlog(kind="be_move", trade_id=str(pos_id), symbol=getattr(position, 'symbol', '?'), new_stop=float(getattr(be_plan, 'new_stop', getattr(be_plan, 'stop_price', 0.0)) or 0.0))
                except Exception:
                    pass
                self._emit(STOP_UPDATE_ATTEMPTED, position_id=pos_id, type="break_even")
                return ManagementAction(
                    position_id=pos_id,
                    action="break_even",
                    details={"new_stop": be_plan.new_stop, **phase_info},
                )

        # 2b. Favorable exit -- fire when MFE peaked >= 1R then retraced 50%+
        # This catches "gave back green" trades that didn't trigger ratchet
        # (e.g. tight-R trades where step filter blocked ratchet moves).
        if self.favorable_exit and peak_price > 0 and risk_distance > 0:
            cfg = getattr(self.favorable_exit, '_pipeline_cfg', None)
            min_peak_r = 1.0
            retrace_pct = 0.5
            if direction == TradeDirection.LONG:
                peak_profit_r = (peak_price - entry_price) / risk_distance
                current_profit_r = profit_r
            else:
                peak_profit_r = (entry_price - peak_price) / risk_distance
                current_profit_r = profit_r
            # Only fire if peak was meaningful AND current is well below peak AND still positive
            if (peak_profit_r >= min_peak_r and current_profit_r > 0.2
                and current_profit_r < peak_profit_r * retrace_pct):
                fav_plan = self.favorable_exit.plan_exit(
                    position_id=pos_id,
                    direction=direction,
                    bid=bid, ask=ask,
                    is_fast_market=(spread > 3 * mean_spread if mean_spread > 0 else False),
                    reason=f"peak_{peak_profit_r:.2f}R_retraced_to_{current_profit_r:.2f}R",
                )
                return ManagementAction(
                    position_id=pos_id,
                    action="favorable_exit",
                    details={
                        "method": fav_plan.method,
                        "limit_price": fav_plan.limit_price,
                        "reason": fav_plan.reason,
                        "expiry_seconds": fav_plan.expiry_seconds,
                        "peak_r": round(peak_profit_r, 3),
                        "current_r": round(current_profit_r, 3),
                        **phase_info,
                    },
                )

        # 3. Phase gate — EARLY_HOLD skips ratchet and trail
        if phase == "EARLY_HOLD":
            return ManagementAction(
                position_id=pos_id,
                action="hold",
                details={"reason": "early_hold", **phase_info},
            )

        # 4. Ratchet check (with spread guard + min-step filter)
        if self.ratchet:
            # Brock 2026-06-01 Fix A: pass position's prior ratchet stamp + read updated stamp from plan
            _prior_stamp = getattr(position, "ratchet_stamped_sl", 0.0) if position else 0.0
            ratchet_plan = self.ratchet.compute_ratchet_stop(
                direction, entry_price, current_price, current_stop, pip_size,
                initial_risk_distance=risk_distance,
                peak_price=peak_price,
                stamped_sl=_prior_stamp,
                spread=spread,
            )
            # Persist the (possibly new) stamp value back onto the position
            # so subsequent cycles can enforce it. Mutation is safe because
            # tracker.persist() is called every cycle.
            if ratchet_plan and position is not None:
                position.ratchet_stamped_sl = ratchet_plan.new_stop
            if ratchet_plan:
                new_stop = ratchet_plan.new_stop

                # Spread guard — same logic as trail
                if self.stop_planner:
                    should, reason = self.stop_planner.should_trail(
                        direction, current_stop, new_stop, spread, mean_spread,
                    )
                    if not should:
                        self._emit(STOP_UPDATE_BLOCKED, position_id=pos_id, reason=f"ratchet_{reason}")
                        return ManagementAction(
                            position_id=pos_id,
                            action="hold",
                            details={"reason": f"ratchet_blocked_{reason}", **phase_info},
                        )

                # Min-step filter — prevent thrashing
                # Brock 2026-06-01 Option 1: bypass min-step when ratchet is
                # enforcing a previously-stamped target. Stamps are deliberate
                # checkpoint locks, not routine adjustments — trust them through.
                step_pips = abs(new_stop - current_stop) / pip_size
                _is_stamp = bool(getattr(ratchet_plan, "reason_tag", "").startswith("stamp_"))
                if step_pips < effective_min_sl_step and not _is_stamp:
                    return ManagementAction(
                        position_id=pos_id,
                        action="hold",
                        details={"reason": "step_too_small", "step_pips": round(step_pips, 1), **phase_info},
                    )

                return ManagementAction(
                    position_id=pos_id,
                    action="ratchet",
                    details={"new_stop": new_stop, **phase_info},
                )

        # 5. Trailing stop (already has spread guard via should_trail + min-step filter)
        if self.trail and hourly_bars is not None:
            trail_plan = self.trail.compute_trail_stop(
                direction, current_stop, hourly_bars, pip_size,
            )
            if trail_plan and self.stop_planner:
                should, reason = self.stop_planner.should_trail(
                    direction, current_stop, trail_plan.new_stop, spread, mean_spread,
                )
                if should:
                    new_stop = trail_plan.new_stop

                    # Min-step filter
                    step_pips = abs(new_stop - current_stop) / pip_size
                    if step_pips < effective_min_sl_step:
                        return ManagementAction(
                            position_id=pos_id,
                            action="hold",
                            details={"reason": "trail_step_too_small", "step_pips": round(step_pips, 1), **phase_info},
                        )

                    return ManagementAction(
                        position_id=pos_id,
                        action="trail",
                        details={"new_stop": new_stop, **phase_info},
                    )
                else:
                    self._emit(STOP_UPDATE_BLOCKED, position_id=pos_id, reason=reason)

        # 6. Default: hold
        return ManagementAction(
            position_id=pos_id,
            action="hold",
            details=phase_info,
        )

    def manage_all(
        self,
        positions: list[Any],
        market_data: dict[str, Any],
    ) -> list[ManagementAction]:
        """Run management chain for all open positions."""
        actions = []
        for pos in positions:
            symbol = getattr(pos, "symbol", "")
            data = market_data.get(symbol, {})
            action = self.manage_position(
                pos,
                current_price=data.get("mid", 0.0),
                bid=data.get("bid", 0.0),
                ask=data.get("ask", 0.0),
                spread=data.get("spread", 0.0),
                mean_spread=data.get("mean_spread", 0.0),
                hourly_bars=data.get("hourly_bars"),
                m5_bars=data.get("m5_bars"),
                pip_size=_pip_size(symbol),
            )
            actions.append(action)
        return actions

    def _emit(self, event_type: str, **payload: Any) -> None:
        if self.event_bus:
            self.event_bus.emit(Event(type=event_type, payload=payload))
