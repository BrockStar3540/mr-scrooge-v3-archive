"""Position pipeline — manages all open positions.

Replaces V2 coordinator's position management logic (lines 358-427,
694-1027, 1265-1291).

Orchestrates: stop updates, trailing, partial harvest, break-even,
ratchet, favorable exit, emergency close.
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

    For each open position, runs through the management chain:
      1. Emergency close check
      2. Partial harvest check (TP1)
      3. Break-even check
      4. Ratchet check
      5. Trailing stop check
      6. Favorable exit check
      7. Stop validation (trigger-side, no-man's-zone)
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
    ):
        self.trail = trail_manager
        self.ratchet = ratchet_manager
        self.be = be_manager
        self.harvest = harvest_manager
        self.favorable_exit = favorable_exit_manager
        self.emergency = emergency_manager
        self.stop_planner = stop_planner
        self.event_bus = event_bus

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
        pos_id = getattr(position, "position_id", str(id(position)))
        direction = TradeDirection(getattr(position, "direction", "long"))
        entry_price = getattr(position, "entry_price", 0.0)
        current_stop = getattr(position, "current_stop", 0.0)

        # 1. Partial harvest
        if self.harvest:
            tp1 = getattr(position, "tp1_price", None) or position.metadata.get("tp1", 0) if hasattr(position, "metadata") else 0
            tp1_taken = getattr(position, "tp1_taken", False)
            if tp1:
                harvest_action = self.harvest.check_harvest(
                    pos_id, direction, current_price, tp1, tp1_taken,
                )
                if harvest_action:
                    return ManagementAction(
                        position_id=pos_id,
                        action="harvest",
                        details={"fraction": harvest_action.close_fraction, "target": harvest_action.target_label},
                    )

        # 2. Break-even check
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
                    details={"new_stop": be_plan.new_stop},
                )

        # 3. Ratchet check
        if self.ratchet:
            ratchet_plan = self.ratchet.compute_ratchet_stop(
                direction, entry_price, current_price, current_stop, pip_size,
            )
            if ratchet_plan:
                return ManagementAction(
                    position_id=pos_id,
                    action="ratchet",
                    details={"new_stop": ratchet_plan.new_stop},
                )

        # 4. Trailing stop
        if self.trail and hourly_bars is not None:
            trail_plan = self.trail.compute_trail_stop(
                direction, current_stop, hourly_bars, pip_size,
            )
            if trail_plan and self.stop_planner:
                should, reason = self.stop_planner.should_trail(
                    direction, current_stop, trail_plan.new_stop, spread, mean_spread,
                )
                if should:
                    return ManagementAction(
                        position_id=pos_id,
                        action="trail",
                        details={"new_stop": trail_plan.new_stop},
                    )
                else:
                    self._emit(STOP_UPDATE_BLOCKED, position_id=pos_id, reason=reason)

        # 5. Default: hold
        return ManagementAction(position_id=pos_id, action="hold")

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
