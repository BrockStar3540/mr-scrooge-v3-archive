"""DBB Candidate Audit — tracks every dbb_trend candidate for calibration.

Logs to data/dbb-candidate-audit.jsonl with full context:
symbol, direction, entry_type, bb_state, base_score, final_score,
tier, rejection reason, breakout_level, pullback_depth, rr, session.

Also maintains in-memory summary for dashboard display.
"""

from __future__ import annotations

import json
import logging
import time
from collections import deque
from pathlib import Path
from threading import Lock
from typing import Any

log = logging.getLogger("scrooge_v3.telemetry.dbb_candidate_audit")


class DBBCandidateAudit:
    """Append-only JSONL audit + in-memory ring buffer for DBB candidates."""

    def __init__(
        self,
        filepath: str | Path = "data/dbb-candidate-audit.jsonl",
        buffer_size: int = 100,
    ):
        self._filepath = Path(filepath)
        self._filepath.parent.mkdir(parents=True, exist_ok=True)
        self._buffer: deque[dict[str, Any]] = deque(maxlen=buffer_size)
        self._lock = Lock()

    def record(self, event: dict[str, Any]) -> None:
        """Record a DBB candidate event."""
        event["timestamp"] = time.time()

        with self._lock:
            self._buffer.append(event)

        try:
            with open(self._filepath, "a") as f:
                f.write(json.dumps(event) + "\n")
        except Exception as e:
            log.warning("[DBB_AUDIT] Write failed: %s", e)

    def recent(self, limit: int = 50) -> list[dict[str, Any]]:
        """Return most recent events."""
        with self._lock:
            items = list(self._buffer)
        return items[-limit:]

    def summary(self) -> dict[str, Any]:
        """Compute summary stats from buffer."""
        with self._lock:
            events = list(self._buffer)

        if not events:
            return {"total": 0, "approved": 0, "rejected": 0, "blocked": 0}

        approved = [e for e in events if e.get("tier") in ("A", "B")]
        rejected = [e for e in events if e.get("tier") == "REJECT"]
        blocked = [e for e in events if e.get("tier") == "BLOCKED"]

        # Breakdown by entry type
        breakouts = [e for e in events if e.get("entry_type") == "DBB_BREAKOUT"]
        pullbacks = [e for e in events if e.get("entry_type") == "DBB_PULLBACK"]

        # Session breakdown
        session_counts: dict[str, int] = {}
        for e in events:
            s = e.get("session", "unknown")
            session_counts[s] = session_counts.get(s, 0) + 1

        # Age bucket breakdown
        age_counts: dict[str, int] = {}
        for e in events:
            age = e.get("box_age", 0)
            if age < 8:
                bucket = "fresh"
            elif age < 18:
                bucket = "mid"
            else:
                bucket = "stale"
            age_counts[bucket] = age_counts.get(bucket, 0) + 1

        # Avg scores
        base_scores = [e.get("base_score", 0) for e in events if e.get("base_score") is not None]
        final_scores = [e.get("final_score", 0) for e in events if e.get("final_score") is not None]

        return {
            "total": len(events),
            "approved": len(approved),
            "rejected": len(rejected),
            "blocked": len(blocked),
            "breakouts": len(breakouts),
            "pullbacks": len(pullbacks),
            "by_session": session_counts,
            "by_age": age_counts,
            "avg_base_score": round(sum(base_scores) / len(base_scores), 1) if base_scores else 0,
            "avg_final_score": round(sum(final_scores) / len(final_scores), 1) if final_scores else 0,
        }
