"""Execution widget — entry log, stop movements, order lifecycle."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class ExecutionWidget:
    """Shows execution events: entries, SL moves, fills, closes."""

    widget_name = "execution"
    widget_category = "execution"

    def __init__(self):
        self._events: list[dict[str, Any]] = []

    def record_entry(self, symbol: str, direction: str, units: int,
                     entry_price: float, stop: float, score: float) -> None:
        self._events.append({
            "type": "entry", "symbol": symbol, "direction": direction,
            "units": units, "price": entry_price, "stop": stop,
            "score": score, "time": datetime.now(timezone.utc).isoformat(),
        })
        self._trim()

    def record_stop_move(self, trade_id: str, old_stop: float,
                         new_stop: float, reason: str) -> None:
        self._events.append({
            "type": "sl_move", "trade_id": trade_id,
            "old_stop": old_stop, "new_stop": new_stop, "reason": reason,
            "time": datetime.now(timezone.utc).isoformat(),
        })
        self._trim()

    def record_close(self, trade_id: str, symbol: str,
                     exit_price: float, realized_pl: float) -> None:
        self._events.append({
            "type": "close", "trade_id": trade_id, "symbol": symbol,
            "price": exit_price, "realized_pl": realized_pl,
            "time": datetime.now(timezone.utc).isoformat(),
        })
        self._trim()

    def _trim(self) -> None:
        if len(self._events) > 200:
            self._events = self._events[-200:]

    def render_data(self) -> dict[str, Any]:
        entries = [e for e in self._events if e["type"] == "entry"]
        closes = [e for e in self._events if e["type"] == "close"]
        return {
            "recent_events": self._events[-20:],
            "total_entries": len(entries),
            "total_closes": len(closes),
            "total_sl_moves": len([e for e in self._events if e["type"] == "sl_move"]),
        }
