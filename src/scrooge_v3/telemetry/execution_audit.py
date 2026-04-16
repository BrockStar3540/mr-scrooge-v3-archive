"""Execution audit — JSONL logger for every position management decision.

Logs SL moves, blocks, harvests, holds, and exits with full context
so the dashboard can display execution health metrics and event timelines.
"""

from __future__ import annotations

import json
import logging
import time
from collections import deque
from dataclasses import asdict, dataclass, field
from pathlib import Path
from threading import Lock
from typing import Any

log = logging.getLogger("scrooge_v3.telemetry.execution_audit")


@dataclass
class AuditEvent:
    """Single execution audit event."""
    type: str          # sl_moved, sl_blocked, harvest, hold, favorable_exit, emergency_close
    reason: str        # spread_too_wide, step_too_small, early_hold, ratchet_lock, etc.
    trade_id: str = ""
    symbol: str = ""
    direction: str = ""
    profit_r: float = 0.0
    spread: float = 0.0
    old_sl: float = 0.0
    new_sl: float = 0.0
    action: str = ""   # the pipeline action that produced this (trail, ratchet, break_even, etc.)
    timestamp: float = 0.0
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        if not d["extra"]:
            del d["extra"]
        return d


class ExecutionAudit:
    """Append-only JSONL audit trail + in-memory ring buffer for dashboard."""

    def __init__(
        self,
        filepath: str | Path = "data/execution-audit.jsonl",
        buffer_size: int = 200,
    ):
        self._filepath = Path(filepath)
        self._filepath.parent.mkdir(parents=True, exist_ok=True)
        self._buffer: deque[dict[str, Any]] = deque(maxlen=buffer_size)
        self._lock = Lock()
        # Counters for summary metrics (reset daily)
        self._counts: dict[str, int] = {}

    def record(self, event: AuditEvent) -> None:
        """Record an audit event to disk and buffer."""
        if not event.timestamp:
            event.timestamp = time.time()
        d = event.to_dict()

        with self._lock:
            self._buffer.append(d)
            key = f"{event.type}:{event.reason}"
            self._counts[key] = self._counts.get(key, 0) + 1

        try:
            with open(self._filepath, "a") as f:
                f.write(json.dumps(d) + "\n")
        except Exception as e:
            log.warning("[AUDIT] Write failed: %s", e)

    def recent_events(self, limit: int = 50) -> list[dict[str, Any]]:
        """Return most recent events from buffer."""
        with self._lock:
            items = list(self._buffer)
        return items[-limit:]

    def summary(self) -> dict[str, Any]:
        """Compute summary metrics from buffer."""
        with self._lock:
            events = list(self._buffer)
            counts = dict(self._counts)

        if not events:
            return {"total": 0, "moves": 0, "blocks": 0, "holds": 0, "block_reasons": {}}

        moves = sum(1 for e in events if e["type"] == "sl_moved")
        blocks = sum(1 for e in events if e["type"] == "sl_blocked")
        holds = sum(1 for e in events if e["type"] == "hold")
        harvests = sum(1 for e in events if e["type"] == "harvest")
        exits = sum(1 for e in events if e["type"] in ("favorable_exit", "emergency_close"))

        # Block reasons breakdown
        block_reasons: dict[str, int] = {}
        spreads_at_block: list[float] = []
        spreads_at_move: list[float] = []
        for e in events:
            if e["type"] == "sl_blocked":
                r = e.get("reason", "unknown")
                block_reasons[r] = block_reasons.get(r, 0) + 1
                if e.get("spread"):
                    spreads_at_block.append(e["spread"])
            elif e["type"] == "sl_moved" and e.get("spread"):
                spreads_at_move.append(e["spread"])

        sl_attempts = moves + blocks
        sl_efficiency = round(moves / sl_attempts * 100, 1) if sl_attempts else 0.0
        avg_spread_block = round(sum(spreads_at_block) / len(spreads_at_block), 5) if spreads_at_block else 0.0
        avg_spread_move = round(sum(spreads_at_move) / len(spreads_at_move), 5) if spreads_at_move else 0.0

        return {
            "total": len(events),
            "moves": moves,
            "blocks": blocks,
            "holds": holds,
            "harvests": harvests,
            "exits": exits,
            "sl_efficiency_pct": sl_efficiency,
            "avg_spread_at_block": avg_spread_block,
            "avg_spread_at_move": avg_spread_move,
            "block_reasons": block_reasons,
        }

    def reset_counts(self) -> None:
        """Reset daily counters."""
        with self._lock:
            self._counts.clear()
