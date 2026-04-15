"""Replay harness — event recording and replay for decision comparison.

Records all EventBus events to JSONL files. Can replay events through
the pipeline to verify same inputs produce same outputs.

Usage:
    # Recording
    recorder = EventRecorder(event_bus, Path("data/replay/session_001.jsonl"))
    recorder.start()
    ... (bot runs) ...
    recorder.stop()

    # Replay
    replayer = EventReplayer(Path("data/replay/session_001.jsonl"))
    events = replayer.load()
    results = replayer.replay_through_scorer(scorer, events)
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scrooge_v3.core.events import Event, EventBus

log = logging.getLogger("scrooge_v3.telemetry.replay")


class EventRecorder:
    """Records all events from an EventBus to a JSONL file.

    Subscribes via subscribe_all() and serializes every event to disk.
    """

    def __init__(self, event_bus: EventBus, output_path: Path):
        self._bus = event_bus
        self._path = output_path
        self._file = None
        self._count = 0
        self._recording = False

    def start(self) -> None:
        """Start recording events."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._file = open(self._path, "a")
        self._bus.subscribe_all(self._handle_event)
        self._recording = True
        log.info("[REPLAY] Recording started → %s", self._path)

    def stop(self) -> None:
        """Stop recording and close the file."""
        self._recording = False
        if self._file:
            self._file.close()
            self._file = None
        log.info("[REPLAY] Recording stopped — %d events captured", self._count)

    @property
    def event_count(self) -> int:
        return self._count

    def _handle_event(self, event: Event) -> None:
        if not self._recording or not self._file:
            return
        record = {
            "type": event.type,
            "timestamp": event.timestamp.isoformat() if event.timestamp else None,
            "payload": _serialize_payload(event.payload),
            "source": event.source,
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }
        try:
            self._file.write(json.dumps(record) + "\n")
            self._file.flush()
            self._count += 1
        except Exception:
            log.exception("[REPLAY] Failed to write event %s", event.type)


class EventReplayer:
    """Loads recorded events and replays them for decision comparison."""

    def __init__(self, path: Path):
        self._path = path

    def load(self) -> list[dict[str, Any]]:
        """Load all events from a JSONL file."""
        events = []
        with open(self._path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    log.warning("[REPLAY] Skipping invalid JSON line")
        log.info("[REPLAY] Loaded %d events from %s", len(events), self._path)
        return events

    def filter_by_type(self, events: list[dict], event_type: str) -> list[dict]:
        return [e for e in events if e.get("type") == event_type]

    def extract_candidates(self, events: list[dict]) -> list[dict]:
        """Extract all CandidateCreated events with scoring data."""
        return self.filter_by_type(events, "CandidateCreated")

    def extract_rejections(self, events: list[dict]) -> list[dict]:
        """Extract all CandidateRejected events with rejection reasons."""
        return self.filter_by_type(events, "CandidateRejected")

    def extract_approvals(self, events: list[dict]) -> list[dict]:
        """Extract all CandidateApproved events."""
        return self.filter_by_type(events, "CandidateApproved")

    def replay_through_scorer(
        self, scorer: Any, events: list[dict]
    ) -> list[dict[str, Any]]:
        """Re-score candidates from recorded events using current scorer.

        Returns list of {original_score, new_score, symbol, match} dicts
        for decision comparison.
        """
        results = []
        for event in self.extract_candidates(events):
            payload = event.get("payload", {})
            symbol = payload.get("symbol", "?")
            original_score = payload.get("score", 0)

            # Build factor dict from payload if available
            factors = payload.get("v3_breakdown")
            if factors:
                new_result = scorer._compute_score(factors)
                results.append({
                    "symbol": symbol,
                    "original_score": original_score,
                    "new_score": new_result.score,
                    "new_tier": new_result.tier,
                    "match": abs(original_score - new_result.score) < 1,
                    "delta": new_result.score - original_score,
                })

        return results

    def build_trade_timeline(self, events: list[dict], symbol: str) -> list[dict]:
        """Build a per-trade event timeline for a specific symbol.

        Shows all events + all module decisions + why blocked/fired.
        """
        return [
            e for e in events
            if e.get("payload", {}).get("symbol") == symbol
        ]

    def summary(self, events: list[dict]) -> dict[str, Any]:
        """Summary statistics for a replay session."""
        by_type: dict[str, int] = {}
        for e in events:
            t = e.get("type", "?")
            by_type[t] = by_type.get(t, 0) + 1

        candidates = self.extract_candidates(events)
        approvals = self.extract_approvals(events)
        rejections = self.extract_rejections(events)

        return {
            "total_events": len(events),
            "event_types": by_type,
            "candidates_created": len(candidates),
            "candidates_approved": len(approvals),
            "candidates_rejected": len(rejections),
            "unique_symbols": len(set(
                e.get("payload", {}).get("symbol", "")
                for e in candidates
            )),
        }


def _serialize_payload(payload: dict) -> dict:
    """Make payload JSON-serializable."""
    result = {}
    for k, v in payload.items():
        if isinstance(v, datetime):
            result[k] = v.isoformat()
        elif isinstance(v, (str, int, float, bool, type(None))):
            result[k] = v
        elif isinstance(v, (list, tuple)):
            result[k] = [str(x) for x in v]
        elif isinstance(v, dict):
            result[k] = _serialize_payload(v)
        else:
            result[k] = str(v)
    return result
