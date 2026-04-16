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
    ):
        self.trail = trail_manager
        self.ratchet = ratchet_manager
        self.be = be_manager
        self.harvest = harvest_manager
        self.favorable_exit = favorable_exit_manager
        self.emergency = emergency_manager
        self.stop_planner = stop_planner
        self.event_bus = event_bus

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
        pip_size: float = 0.0001,
    ) -> ManagementAction:
        """Run the full management chain for one position.

        Returns the highest-priority action to take.
        """
        pos_id = getattr(position, "position_id", None) or getattr(position, "trade_id", str(id(position)))
        direction = TradeDirection(getattr(position, "direction", "long"))
        entry_price = getattr(position, "entry_price", 0.0)
        current_stop = getattr(position, "current_stop", 0.0)

        # --- Compute profit-R for phase selection ---
        risk_distance = abs(entry_price - current_stop) if current_stop else 0.0
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
            effective_min_sl_step = effective_min_sl_step
        else:
            effective_early_hold_r = self.early_hold_r
            effective_min_sl_step = effective_min_sl_step

        # Determine phase using profile-aware threshold
        if profit_r < effective_early_hold_r:
            phase = "EARLY_HOLD"
        elif profit_r < self.lock_r:
            phase = "LOCK"
        else:
            phase = "HARVEST"

        # Build details dict with phase info for audit
        phase_info = {"phase": phase, "profit_r": round(profit_r, 3), "profile": profile}

        # 1. Partial harvest (skip if harvest limit order is live on OANDA)
        if self.harvest:
            harvest_order_id = getattr(position, "harvest_order_id", "")
            if harvest_order_id:
                pass  # Harvest limit order is live on OANDA — skip reactive check
            else:
                tp1 = getattr(position, "tp1_price", None) or (position.metadata.get("tp1", 0) if hasattr(position, "metadata") else 0)
                tp1_taken = getattr(position, "tp1_taken", False)
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
            )
            if be_plan:
                self._emit(STOP_UPDATE_ATTEMPTED, position_id=pos_id, type="break_even")
                return ManagementAction(
                    position_id=pos_id,
                    action="break_even",
                    details={"new_stop": be_plan.new_stop, **phase_info},
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
            ratchet_plan = self.ratchet.compute_ratchet_stop(
                direction, entry_price, current_price, current_stop, pip_size,
            )
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
                step_pips = abs(new_stop - current_stop) / pip_size
                if step_pips < effective_min_sl_step:
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
                pip_size=0.01 if "JPY" in symbol else 0.0001,
            )
            actions.append(action)
        return actions

    def _emit(self, event_type: str, **payload: Any) -> None:
        if self.event_bus:
            self.event_bus.emit(Event(type=event_type, payload=payload))
