"""Event bus tests."""

from scrooge_v3.core.events import Event, EventBus


def test_subscribe_and_emit():
    bus = EventBus()
    received = []

    bus.subscribe("TestEvent", lambda e: received.append(e))
    bus.emit(Event(type="TestEvent", payload={"x": 1}))

    assert len(received) == 1
    assert received[0].payload["x"] == 1


def test_global_handler():
    bus = EventBus()
    received = []

    bus.subscribe_all(lambda e: received.append(e.type))
    bus.emit(Event(type="A"))
    bus.emit(Event(type="B"))

    assert received == ["A", "B"]


def test_handler_exception_does_not_crash():
    bus = EventBus()

    def bad_handler(e):
        raise ValueError("boom")

    bus.subscribe("X", bad_handler)
    # Should not raise
    bus.emit(Event(type="X"))
