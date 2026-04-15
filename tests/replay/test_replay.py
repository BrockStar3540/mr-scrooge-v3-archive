"""Replay harness tests — event recording, loading, replay, and comparison."""

import json
import tempfile
from pathlib import Path

from scrooge_v3.core.events import Event, EventBus
from scrooge_v3.telemetry.replay import EventRecorder, EventReplayer


def _temp_path():
    return Path(tempfile.mktemp(suffix=".jsonl"))


class TestEventRecorder:
    def test_records_events_to_jsonl(self):
        bus = EventBus()
        path = _temp_path()
        try:
            recorder = EventRecorder(bus, path)
            recorder.start()

            bus.emit(Event(type="CandidateCreated", payload={"symbol": "EUR_USD", "score": 75}))
            bus.emit(Event(type="CandidateRejected", payload={"symbol": "GBP_JPY", "reason": "spread"}))
            bus.emit(Event(type="FeaturesComputed", payload={"features": ["atr", "bb"]}))

            recorder.stop()

            assert recorder.event_count == 3
            lines = path.read_text().strip().split("\n")
            assert len(lines) == 3

            first = json.loads(lines[0])
            assert first["type"] == "CandidateCreated"
            assert first["payload"]["symbol"] == "EUR_USD"
        finally:
            path.unlink(missing_ok=True)

    def test_stop_prevents_further_recording(self):
        bus = EventBus()
        path = _temp_path()
        try:
            recorder = EventRecorder(bus, path)
            recorder.start()
            bus.emit(Event(type="A", payload={}))
            recorder.stop()
            bus.emit(Event(type="B", payload={}))

            lines = path.read_text().strip().split("\n")
            assert len(lines) == 1
        finally:
            path.unlink(missing_ok=True)


class TestEventReplayer:
    def _write_events(self, path, events):
        with open(path, "w") as f:
            for e in events:
                f.write(json.dumps(e) + "\n")

    def test_load_events(self):
        path = _temp_path()
        try:
            self._write_events(path, [
                {"type": "A", "payload": {"x": 1}},
                {"type": "B", "payload": {"x": 2}},
            ])
            replayer = EventReplayer(path)
            events = replayer.load()
            assert len(events) == 2
            assert events[0]["type"] == "A"
        finally:
            path.unlink(missing_ok=True)

    def test_filter_by_type(self):
        path = _temp_path()
        try:
            self._write_events(path, [
                {"type": "CandidateCreated", "payload": {"symbol": "EUR_USD"}},
                {"type": "CandidateRejected", "payload": {"symbol": "GBP_JPY"}},
                {"type": "CandidateCreated", "payload": {"symbol": "USD_JPY"}},
            ])
            replayer = EventReplayer(path)
            events = replayer.load()
            candidates = replayer.extract_candidates(events)
            assert len(candidates) == 2
            rejections = replayer.extract_rejections(events)
            assert len(rejections) == 1
        finally:
            path.unlink(missing_ok=True)

    def test_summary(self):
        path = _temp_path()
        try:
            self._write_events(path, [
                {"type": "CandidateCreated", "payload": {"symbol": "EUR_USD", "score": 75}},
                {"type": "CandidateApproved", "payload": {"symbol": "EUR_USD"}},
                {"type": "CandidateCreated", "payload": {"symbol": "GBP_JPY", "score": 30}},
                {"type": "CandidateRejected", "payload": {"symbol": "GBP_JPY", "reason": "spread"}},
                {"type": "FeaturesComputed", "payload": {}},
            ])
            replayer = EventReplayer(path)
            events = replayer.load()
            summary = replayer.summary(events)
            assert summary["total_events"] == 5
            assert summary["candidates_created"] == 2
            assert summary["candidates_approved"] == 1
            assert summary["candidates_rejected"] == 1
        finally:
            path.unlink(missing_ok=True)

    def test_trade_timeline(self):
        path = _temp_path()
        try:
            self._write_events(path, [
                {"type": "FeaturesComputed", "payload": {"symbol": "EUR_USD"}},
                {"type": "CandidateCreated", "payload": {"symbol": "EUR_USD", "score": 75}},
                {"type": "FeaturesComputed", "payload": {"symbol": "GBP_JPY"}},
                {"type": "CandidateApproved", "payload": {"symbol": "EUR_USD"}},
            ])
            replayer = EventReplayer(path)
            events = replayer.load()
            timeline = replayer.build_trade_timeline(events, "EUR_USD")
            assert len(timeline) == 3  # Features, Created, Approved for EUR_USD
            assert all(e["payload"]["symbol"] == "EUR_USD" for e in timeline)
        finally:
            path.unlink(missing_ok=True)


class TestReplayRoundTrip:
    def test_record_then_replay(self):
        """Full round trip: record events, load them, verify content."""
        bus = EventBus()
        path = _temp_path()
        try:
            # Record
            recorder = EventRecorder(bus, path)
            recorder.start()
            bus.emit(Event(type="CandidateCreated", payload={
                "symbol": "EUR_USD", "strategy": "reversal", "score": 82,
            }))
            bus.emit(Event(type="CandidateRejected", payload={
                "symbol": "USD_JPY", "strategy": "trend",
                "reason": "V3_REJECT:score=35",
            }))
            recorder.stop()

            # Replay
            replayer = EventReplayer(path)
            events = replayer.load()
            assert len(events) == 2

            candidates = replayer.extract_candidates(events)
            assert len(candidates) == 1
            assert candidates[0]["payload"]["symbol"] == "EUR_USD"

            rejections = replayer.extract_rejections(events)
            assert len(rejections) == 1
            assert "V3_REJECT" in rejections[0]["payload"]["reason"]
        finally:
            path.unlink(missing_ok=True)
