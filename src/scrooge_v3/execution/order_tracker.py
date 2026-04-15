"""Order tracker — lifecycle tracking for all orders.

Tracks: CREATED → SENT → ACK → TRIGGERED → FILLED / CANCELLED / REJECTED

Every order state transition is logged for the execution audit trail.
This is first-class, not optional.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import OrderState

log = logging.getLogger("scrooge_v3.execution.order_tracker")


@dataclass
class TrackedOrder:
    """Full lifecycle record for one order."""

    order_id: str
    trade_id: str
    symbol: str
    direction: str
    order_type: str  # MARKET, LIMIT, STOP
    size: float
    price: float
    stop_loss: float = 0.0
    take_profit: float = 0.0
    state: OrderState = OrderState.CREATED
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    sent_at: datetime | None = None
    acknowledged_at: datetime | None = None
    triggered_at: datetime | None = None
    filled_at: datetime | None = None
    fill_price: float = 0.0
    cancelled_at: datetime | None = None
    rejected_at: datetime | None = None
    reject_reason: str = ""
    transitions: list[dict[str, Any]] = field(default_factory=list)

    def transition(self, new_state: OrderState, **kwargs: Any) -> None:
        """Record a state transition."""
        now = datetime.now(timezone.utc)
        old_state = self.state
        self.state = new_state
        self.transitions.append({
            "from": old_state.value,
            "to": new_state.value,
            "at": now.isoformat(),
            **kwargs,
        })

        # Set timestamp fields
        if new_state == OrderState.ACKNOWLEDGED:
            self.sent_at = self.sent_at or now
            self.acknowledged_at = now
        elif new_state == OrderState.TRIGGERED:
            self.triggered_at = now
        elif new_state == OrderState.FILLED:
            self.filled_at = now
            self.fill_price = kwargs.get("fill_price", self.price)
        elif new_state == OrderState.CANCELLED:
            self.cancelled_at = now
        elif new_state == OrderState.REJECTED:
            self.rejected_at = now
            self.reject_reason = kwargs.get("reason", "")

        log.info(
            "[ORDER_TRACKER] %s %s→%s order=%s symbol=%s",
            self.trade_id, old_state.value, new_state.value,
            self.order_id, self.symbol,
        )


class OrderTracker:
    """Tracks all active and recent orders."""

    def __init__(self, max_history: int = 500):
        self._active: dict[str, TrackedOrder] = {}
        self._history: list[TrackedOrder] = []
        self._max_history = max_history

    def create(
        self,
        order_id: str,
        trade_id: str,
        symbol: str,
        direction: str,
        order_type: str,
        size: float,
        price: float,
        stop_loss: float = 0.0,
        take_profit: float = 0.0,
    ) -> TrackedOrder:
        """Create and track a new order."""
        order = TrackedOrder(
            order_id=order_id,
            trade_id=trade_id,
            symbol=symbol,
            direction=direction,
            order_type=order_type,
            size=size,
            price=price,
            stop_loss=stop_loss,
            take_profit=take_profit,
        )
        self._active[order_id] = order
        return order

    def transition(self, order_id: str, new_state: OrderState, **kwargs: Any) -> bool:
        """Transition an order to a new state. Returns False if order not found."""
        order = self._active.get(order_id)
        if order is None:
            log.warning("[ORDER_TRACKER] Order %s not found", order_id)
            return False

        order.transition(new_state, **kwargs)

        # Move to history if terminal state
        if new_state in (OrderState.FILLED, OrderState.CANCELLED, OrderState.REJECTED):
            self._history.append(order)
            del self._active[order_id]
            # Trim history
            if len(self._history) > self._max_history:
                self._history = self._history[-self._max_history:]

        return True

    def get_active(self, symbol: str | None = None) -> list[TrackedOrder]:
        """Return active orders, optionally filtered by symbol."""
        if symbol is None:
            return list(self._active.values())
        return [o for o in self._active.values() if o.symbol == symbol]

    def get_history(self, limit: int = 50) -> list[TrackedOrder]:
        return self._history[-limit:]
