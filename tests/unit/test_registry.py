"""Basic registry tests — verify module discovery and mode switching."""

from scrooge_v3.core.registry import ModuleRegistry
from scrooge_v3.core.types import HealthColor


class FakeModule:
    def __init__(self, name: str):
        self.name = name


def test_register_and_retrieve():
    reg = ModuleRegistry()
    mod = FakeModule("atr")
    reg.register("features", "atr", mod)

    entry = reg.get("features", "atr")
    assert entry is not None
    assert entry.name == "atr"
    assert entry.instance is mod
    assert entry.enabled is True


def test_get_active_excludes_disabled():
    reg = ModuleRegistry()
    reg.register("gates", "spread", FakeModule("spread"), enabled=True)
    reg.register("gates", "otr", FakeModule("otr"), enabled=False)

    active = reg.get_active("gates")
    assert len(active) == 1
    assert active[0].name == "spread"


def test_set_mode_disabled():
    reg = ModuleRegistry()
    reg.register("strategies", "reversal", FakeModule("reversal"))

    reg.set_mode("strategies", "reversal", "disabled")
    entry = reg.get("strategies", "reversal")
    assert entry is not None
    assert entry.enabled is False
    assert entry.mode == "disabled"


def test_health_summary():
    reg = ModuleRegistry()
    reg.register("features", "atr", FakeModule("atr"), enabled=True)
    reg.register("features", "bb", FakeModule("bb"), enabled=False)

    summary = reg.health_summary()
    assert "features" in summary
    colors = [s.color for s in summary["features"]]
    assert HealthColor.GREEN in colors
    assert HealthColor.GRAY in colors
