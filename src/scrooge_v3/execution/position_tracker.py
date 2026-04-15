"""Position tracker — maintains per-trade state across cycles.

Bridges OANDA TradeInfo (what the broker knows) with the management
pipeline (what the bot needs to manage: TP1 level, partial status,
entry metadata, SL ownership).

Persists to JSON so state survives restarts.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.execution.position_tracker")


@dataclass
class TrackedPosition:
    """Everything the management pipeline needs about an open trade."""
    trade_id: str
    symbol: str
    direction: str  # "long" or "short"
    units: float
    entry_price: float
    current_stop: float
    current_tp: float = 0.0
    tp1_price: float = 0.0  # Center of box (half profit target)
    tp2_price: float = 0.0  # Opposite boundary
    tp1_taken: bool = False
    break_even_achieved: bool = False
    opened_at: str = ""
    strategy: str = ""
    v3_score: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


class PositionTracker:
    """Tracks all open positions with metadata the broker doesn't store."""

    def __init__(self, persist_path: Path | None = None):
        self._positions: dict[str, TrackedPosition] = {}
        self._persist_path = persist_path

    def register_entry(
        self,
        trade_id: str,
        symbol: str,
        direction: str,
        units: float,
        entry_price: float,
        stop_price: float,
        tp_price: float = 0.0,
        tp1_price: float = 0.0,
        tp2_price: float = 0.0,
        strategy: str = "",
        v3_score: int = 0,
        metadata: dict | None = None,
    ) -> None:
        """Register a new trade after fill confirmation."""
        self._positions[trade_id] = TrackedPosition(
            trade_id=trade_id,
            symbol=symbol,
            direction=direction,
            units=units,
            entry_price=entry_price,
            current_stop=stop_price,
            current_tp=tp_price,
            tp1_price=tp1_price,
            tp2_price=tp2_price,
            opened_at=datetime.now(timezone.utc).isoformat(),
            strategy=strategy,
            v3_score=v3_score,
            metadata=metadata or {},
        )
        log.info("[TRACKER] Registered: %s %s %s %d units @ %.5f SL=%.5f",
                 trade_id, symbol, direction, units, entry_price, stop_price)
        self.persist()

    def get(self, trade_id: str) -> TrackedPosition | None:
        return self._positions.get(trade_id)

    def all_positions(self) -> list[TrackedPosition]:
        return list(self._positions.values())

    def update_stop(self, trade_id: str, new_stop: float) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.current_stop = new_stop

    def mark_tp1_taken(self, trade_id: str) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.tp1_taken = True
            log.info("[TRACKER] TP1 taken: %s", trade_id)

    def mark_break_even(self, trade_id: str) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.break_even_achieved = True

    def remove(self, trade_id: str) -> TrackedPosition | None:
        pos = self._positions.pop(trade_id, None)
        if pos:
            log.info("[TRACKER] Removed: %s %s", trade_id, pos.symbol)
            self.persist()
        return pos

    def reconcile_with_broker(self, broker_trade_ids: set[str]) -> list[str]:
        """Remove positions that OANDA no longer has open. Returns vanished IDs."""
        vanished = []
        for tid in list(self._positions.keys()):
            if tid not in broker_trade_ids:
                pos = self._positions.pop(tid)
                vanished.append(tid)
                log.warning("[TRACKER] Trade vanished: %s %s (closed externally)", tid, pos.symbol)
        if vanished:
            self.persist()
        return vanished

    def persist(self) -> None:
        if not self._persist_path:
            return
        self._persist_path.parent.mkdir(parents=True, exist_ok=True)
        data = {tid: asdict(pos) for tid, pos in self._positions.items()}
        with open(self._persist_path, "w") as f:
            json.dump(data, f, indent=2, default=str)

    def restore(self) -> int:
        if not self._persist_path or not self._persist_path.exists():
            return 0
        with open(self._persist_path) as f:
            data = json.load(f)
        for tid, d in data.items():
            self._positions[tid] = TrackedPosition(**{
                k: v for k, v in d.items() if k in TrackedPosition.__dataclass_fields__
            })
        log.info("[TRACKER] Restored %d positions from disk", len(self._positions))
        return len(self._positions)
