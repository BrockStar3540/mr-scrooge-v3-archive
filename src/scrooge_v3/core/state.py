"""Centralized state store — typed, snapshotable, persistent."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from .types import HealthStatus

logger = logging.getLogger(__name__)


@dataclass
class CooldownState:
    zone_debounce_until: datetime | None = None
    entry_cooldown_until: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class SymbolState:
    symbol: str
    bb_state: str = ""
    regime: str = ""
    opening_state: str = ""
    structure_state: str = ""
    volatility_state: str = ""
    cooldowns: CooldownState = field(default_factory=CooldownState)
    features: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class StopState:
    current_stop: float = 0.0
    last_attempt_reason: str = ""
    last_update: datetime | None = None


@dataclass
class TradePositionState:
    position_id: str
    symbol: str
    direction: str = ""
    entry_price: float = 0.0
    size: float = 0.0
    stop: StopState = field(default_factory=StopState)
    opened_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class StateStore:
    """Central state store for the entire system."""

    def __init__(self, persist_path: Path | None = None) -> None:
        self.symbols: dict[str, SymbolState] = {}
        self.positions: dict[str, TradePositionState] = {}
        self.health: dict[str, HealthStatus] = {}
        self.counters: dict[str, int] = {}
        self.memories: dict[str, Any] = {}
        self.experiments: dict[str, Any] = {}
        self._persist_path = persist_path

    def get_symbol(self, symbol: str) -> SymbolState:
        if symbol not in self.symbols:
            self.symbols[symbol] = SymbolState(symbol=symbol)
        return self.symbols[symbol]

    def get_position(self, position_id: str) -> TradePositionState | None:
        return self.positions.get(position_id)

    def snapshot(self) -> dict[str, Any]:
        """Create a serializable snapshot of the entire state."""
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "symbols": {k: vars(v) for k, v in self.symbols.items()},
            "positions": {k: vars(v) for k, v in self.positions.items()},
            "counters": self.counters.copy(),
        }

    def persist(self) -> None:
        if self._persist_path:
            snap = self.snapshot()
            with open(self._persist_path, "w") as f:
                json.dump(snap, f, indent=2, default=str)
            logger.debug("State persisted to %s", self._persist_path)

    def restore(self) -> bool:
        if self._persist_path and self._persist_path.exists():
            logger.info("Restoring state from %s", self._persist_path)
            # Full restore logic to be implemented per domain
            return True
        return False
