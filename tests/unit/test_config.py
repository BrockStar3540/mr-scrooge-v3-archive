"""Config validation + hot reload tests."""

import json
import os
import tempfile
import time
from pathlib import Path

from scrooge_v3.core.config import ConfigStore, ConfigValidationError


def _valid_config() -> dict:
    """Minimal valid config for testing."""
    return {
        "runtime": {"scan_interval_seconds": 60, "dry_run": True, "log_level": "INFO"},
        "risk": {"max_open_positions": 5, "max_daily_loss_pct": 3.0, "margin_utilization": 0.80},
        "features": {"atr": {"period": 14}},
        "gates": {"rr": {"reversal_min_rr": 1.0, "trend_min_rr": 1.0}},
        "strategies": {"reversal": {"enabled": True}},
    }


def _write_config(path: Path, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f)


# =====================================================================
# Schema Validation
# =====================================================================

class TestValidation:
    def test_valid_config_passes(self):
        store = ConfigStore()
        store._data = _valid_config()
        errors = store.validate()
        assert errors == []

    def test_missing_section_fails(self):
        store = ConfigStore()
        store._data = {"runtime": {"scan_interval_seconds": 60, "dry_run": True}}
        errors = store.validate()
        assert any("Missing required section: risk" in e for e in errors)

    def test_wrong_type_fails(self):
        store = ConfigStore()
        cfg = _valid_config()
        cfg["runtime"]["scan_interval_seconds"] = "sixty"
        store._data = cfg
        errors = store.validate()
        assert any("expected int" in e for e in errors)

    def test_out_of_range_fails(self):
        store = ConfigStore()
        cfg = _valid_config()
        cfg["risk"]["max_daily_loss_pct"] = 50.0  # max is 10.0
        store._data = cfg
        errors = store.validate()
        assert any("above maximum" in e for e in errors)

    def test_below_range_fails(self):
        store = ConfigStore()
        cfg = _valid_config()
        cfg["runtime"]["scan_interval_seconds"] = 1  # min is 10
        store._data = cfg
        errors = store.validate()
        assert any("below minimum" in e for e in errors)

    def test_validate_or_raise(self):
        store = ConfigStore()
        store._data = {"runtime": {"scan_interval_seconds": 60, "dry_run": True}}
        try:
            store.validate_or_raise()
            assert False, "Should have raised"
        except ConfigValidationError as e:
            assert "Missing required section" in str(e)

    def test_int_accepted_for_float(self):
        """Integer values should be accepted where float is expected."""
        store = ConfigStore()
        cfg = _valid_config()
        cfg["risk"]["max_daily_loss_pct"] = 3  # int, not float
        store._data = cfg
        errors = store.validate()
        assert not any("max_daily_loss_pct" in e for e in errors)


# =====================================================================
# Dot-path Access + Change History
# =====================================================================

class TestDotPath:
    def test_get_nested(self):
        store = ConfigStore()
        store._data = _valid_config()
        assert store.get("runtime.scan_interval_seconds") == 60

    def test_set_records_history(self):
        store = ConfigStore()
        store._data = _valid_config()
        store.set("runtime.scan_interval_seconds", 120)
        assert store.get("runtime.scan_interval_seconds") == 120
        history = store.change_history()
        assert len(history) == 1
        assert history[0]["path"] == "runtime.scan_interval_seconds"
        assert history[0]["old"] == 60
        assert history[0]["new"] == 120

    def test_set_with_persist(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
            json.dump(_valid_config(), f)
            path = Path(f.name)
        try:
            store = ConfigStore(path)
            store.load()
            store.set("runtime.dry_run", False, persist=True)
            # Reload and verify persisted
            store2 = ConfigStore(path)
            store2.load()
            assert store2.get("runtime.dry_run") is False
        finally:
            path.unlink()


# =====================================================================
# Environment Variable Overrides
# =====================================================================

class TestEnvOverrides:
    def test_applies_env_override(self):
        store = ConfigStore()
        store._data = _valid_config()
        os.environ["SCROOGE_RUNTIME_DRY_RUN"] = "false"
        try:
            count = store.apply_env_overrides()
            assert count >= 1
            assert store.get("runtime.dry_run") is False
        finally:
            del os.environ["SCROOGE_RUNTIME_DRY_RUN"]

    def test_type_coercion_int(self):
        store = ConfigStore()
        store._data = _valid_config()
        os.environ["SCROOGE_RUNTIME_SCAN_INTERVAL_SECONDS"] = "120"
        try:
            store.apply_env_overrides()
            val = store.get("runtime.scan_interval_seconds")
            assert val == 120
            assert isinstance(val, int)
        finally:
            del os.environ["SCROOGE_RUNTIME_SCAN_INTERVAL_SECONDS"]


# =====================================================================
# Change Callbacks
# =====================================================================

class TestCallbacks:
    def test_callback_fires_on_set(self):
        store = ConfigStore()
        store._data = _valid_config()
        changes = []
        store.on_change(lambda c: changes.append(c))
        store.set("runtime.dry_run", False)
        assert len(changes) == 1
        assert changes[0]["path"] == "runtime.dry_run"


# =====================================================================
# File Watcher
# =====================================================================

class TestFileWatcher:
    def test_detects_file_change(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
            json.dump(_valid_config(), f)
            path = Path(f.name)
        try:
            store = ConfigStore(path)
            store.load()
            changes = []
            store.on_change(lambda c: changes.append(c))

            store.start_watcher(interval=0.5)

            # Modify the file
            time.sleep(0.2)
            cfg = _valid_config()
            cfg["runtime"]["scan_interval_seconds"] = 120
            _write_config(path, cfg)

            # Wait for watcher to detect
            time.sleep(1.5)
            store.stop_watcher()

            assert store.get("runtime.scan_interval_seconds") == 120
            assert any(c.get("path") == "runtime.scan_interval_seconds" for c in changes)
        finally:
            path.unlink()

    def test_rollback_on_invalid_change(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
            json.dump(_valid_config(), f)
            path = Path(f.name)
        try:
            store = ConfigStore(path)
            store.load()
            original_interval = store.get("runtime.scan_interval_seconds")

            store.start_watcher(interval=0.5)

            # Write invalid config (scan_interval = 1, below minimum 10)
            time.sleep(0.2)
            cfg = _valid_config()
            cfg["runtime"]["scan_interval_seconds"] = 1
            _write_config(path, cfg)

            time.sleep(1.5)
            store.stop_watcher()

            # Should have rolled back
            assert store.get("runtime.scan_interval_seconds") == original_interval
        finally:
            path.unlink()


# =====================================================================
# Diff Detection
# =====================================================================

class TestDiff:
    def test_detects_changes(self):
        old = {"a": 1, "b": {"c": 2, "d": 3}}
        new = {"a": 1, "b": {"c": 5, "d": 3}}
        changes = ConfigStore._diff(old, new)
        assert "b.c" in changes
        assert changes["b.c"] == (2, 5)
        assert "a" not in changes

    def test_detects_additions(self):
        old = {"a": 1}
        new = {"a": 1, "b": 2}
        changes = ConfigStore._diff(old, new)
        assert "b" in changes
        assert changes["b"] == (None, 2)
