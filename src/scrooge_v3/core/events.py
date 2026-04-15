"""Typed event bus — modules communicate through events, not direct calls."""

from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable

logger = logging.getLogger(__name__)


@dataclass
class Event:
    """Base event. All events carry a type tag, timestamp, and optional payload."""

    type: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    payload: dict[str, Any] = field(default_factory=dict)
    source: str = ""


# Pre-defined event types (not exhaustive — modules may define their own)
MARKET_SNAPSHOT_RECEIVED = "MarketSnapshotReceived"
FEATURES_COMPUTED = "FeaturesComputed"
CONTEXT_BUILT = "ContextBuilt"
CLASSIFICATION_COMPUTED = "ClassificationComputed"
STRATEGY_EVALUATED = "StrategyEvaluated"
CANDIDATE_CREATED = "CandidateCreated"
GATE_EVALUATED = "GateEvaluated"
CANDIDATE_REJECTED = "CandidateRejected"
CANDIDATE_APPROVED = "CandidateApproved"
ORDER_PLANNED = "OrderPlanned"
ORDER_SUBMITTED = "OrderSubmitted"
ORDER_TRIGGERED = "OrderTriggered"
ORDER_FILLED = "OrderFilled"
STOP_UPDATE_ATTEMPTED = "StopUpdateAttempted"
STOP_UPDATE_BLOCKED = "StopUpdateBlocked"
STOP_UPDATED = "StopUpdated"
POSITION_CLOSED = "PositionClosed"
HEALTH_CHANGED = "HealthChanged"
CONFIG_CHANGED = "ConfigChanged"


EventHandler = Callable[[Event], None]


class EventBus:
    """Simple synchronous event bus. Handlers are called in registration order."""

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)
        self._global_handlers: list[EventHandler] = []

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        self._handlers[event_type].append(handler)

    def subscribe_all(self, handler: EventHandler) -> None:
        """Subscribe to every event (useful for audit/telemetry)."""
        self._global_handlers.append(handler)

    def emit(self, event: Event) -> None:
        for handler in self._global_handlers:
            try:
                handler(event)
            except Exception:
                logger.exception("Global handler failed for %s", event.type)

        for handler in self._handlers.get(event.type, []):
            try:
                handler(event)
            except Exception:
                logger.exception(
                    "Handler failed for %s", event.type
                )
