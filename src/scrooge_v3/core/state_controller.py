"""State controller — owns all runtime state extracted from the V2 coordinator.

Manages: zone entry caps, counter-trend failure memory, zone debounce,
cooldowns, daily counters, position count, bar cache, and persistence.

Source: V2 coordinator.py lines 79-130 (init), 257-274 (daily_reset),
and scattered state attributes throughout.
"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.core.state_controller")


class StateController:
    """Centralized runtime state for the trading system.

    Replaces the ~35 scattered attributes on V2's coordinator.

    NOTE: No regime floor logic (score >= -1 check) here. Regime floor
    is handled by the gate pipeline (gates.regime_floor in config).
    V3 scorer supersedes any inline regime floor checks.
    """

    def __init__(self, config: dict | None = None, persist_path: Path | None = None):
        config = config or {}
        self._persist_path = persist_path

        # Config
        self.max_entries_per_zone = config.get("max_entries_per_zone", 3)
        self.max_ct_failures = config.get("max_ct_failures", 2)
        self.debounce_minutes = config.get("debounce_minutes", 20)
        self.default_cooldown_minutes = config.get("default_cooldown_minutes", 30)

        # Daily counters (cleared on daily_reset)
        self.zone_entry_counts: dict[str, int] = defaultdict(int)
        self.ct_failure_counts: dict[str, int] = defaultdict(int)

        # Zone debounce — timestamp of last entry at each zone
        self.zone_debounce: dict[str, datetime] = {}

        # Cooldowns — timestamp until which re-entry is blocked per symbol
        self.cooldowns: dict[str, datetime] = {}

        # Candle debounce — last processed candle key per symbol
        self.last_candle: dict[str, str] = {}

        # Position tracking
        # Read from risk.max_open_positions (canonical path in default.json).
        # Support both a pre-flattened dict (current bootstrap path) and a
        # nested config. Defaults to 2 per user spec.
        self.position_count: int = 0
        risk_section = config.get("risk") if isinstance(config.get("risk"), dict) else {}
        self.max_positions: int = (
            config.get("max_open_positions")
            or risk_section.get("max_open_positions")
            or config.get("max_concurrent_positions")  # legacy key — still honored
            or 2
        )

        # Equity tracking
        self.equity_start: float = 0.0
        self.daily_loss: float = 0.0
        self.max_daily_loss_pct: float = config.get("max_daily_loss_pct", 3.0)

        # Bar cache (API error fallback)
        self.bar_cache: dict[str, Any] = {}

        # Cycle counter
        self.cycle_count: int = 0

        # Session tracking
        self.session_start: datetime = datetime.utcnow()
        self.active_sessions: set[str] = set()

    # ----------------------------------------------------------
    # Daily reset
    # ----------------------------------------------------------

    def daily_reset(self) -> None:
        """Clear all daily counters. Called at date boundary."""
        self.zone_entry_counts.clear()
        self.ct_failure_counts.clear()
        self.zone_debounce.clear()
        self.cooldowns.clear()
        self.last_candle.clear()
        self.daily_loss = 0.0
        self.cycle_count = 0
        log.info("[STATE] Daily reset complete")

    # ----------------------------------------------------------
    # Zone entry cap (replaces V2 "D3")
    # ----------------------------------------------------------

    def record_zone_entry(self, symbol: str, zone_key: str) -> None:
        """Record an entry at a zone. Call after successful fill."""
        key = f"{symbol}:{zone_key}"
        self.zone_entry_counts[key] += 1
        self.zone_debounce[key] = datetime.utcnow()
        log.debug("[STATE] Zone entry recorded: %s count=%d", key, self.zone_entry_counts[key])

    def check_zone_cap(self, symbol: str, zone_key: str) -> bool:
        """Return True if zone entry cap has been reached."""
        key = f"{symbol}:{zone_key}"
        count = self.zone_entry_counts.get(key, 0)
        return count >= self.max_entries_per_zone

    # ----------------------------------------------------------
    # Counter-trend failure memory (replaces V2 "D1")
    # ----------------------------------------------------------

    def record_ct_failure(self, symbol: str, zone_key: str) -> None:
        """Record a counter-trend stop loss at a zone."""
        key = f"{symbol}:{zone_key}"
        self.ct_failure_counts[key] += 1
        log.debug("[STATE] CT failure recorded: %s count=%d", key, self.ct_failure_counts[key])

    def check_ct_exhausted(self, symbol: str, zone_key: str) -> bool:
        """Return True if CT zone has too many failures today."""
        key = f"{symbol}:{zone_key}"
        return self.ct_failure_counts.get(key, 0) >= self.max_ct_failures

    # ----------------------------------------------------------
    # Zone debounce
    # ----------------------------------------------------------

    def check_debounce(self, symbol: str, zone_key: str) -> bool:
        """Return True if zone is still in debounce period."""
        key = f"{symbol}:{zone_key}"
        last = self.zone_debounce.get(key)
        if last is None:
            return False
        elapsed = (datetime.utcnow() - last).total_seconds() / 60
        return elapsed < self.debounce_minutes

    # ----------------------------------------------------------
    # Cooldowns
    # ----------------------------------------------------------

    def set_cooldown(self, symbol: str, minutes: int | None = None) -> None:
        """Set cooldown for a symbol after exit."""
        mins = minutes if minutes is not None else self.default_cooldown_minutes
        self.cooldowns[symbol] = datetime.utcnow() + timedelta(minutes=mins)
        log.debug("[STATE] Cooldown set: %s for %d min", symbol, mins)

    def is_in_cooldown(self, symbol: str) -> bool:
        """Return True if symbol is in cooldown."""
        until = self.cooldowns.get(symbol)
        if until is None:
            return False
        return datetime.utcnow() < until

    # ----------------------------------------------------------
    # Candle debounce
    # ----------------------------------------------------------

    def is_same_candle(self, symbol: str, candle_key: str) -> bool:
        """Return True if this candle was already processed."""
        return self.last_candle.get(symbol) == candle_key

    def mark_candle(self, symbol: str, candle_key: str) -> None:
        self.last_candle[symbol] = candle_key

    # ----------------------------------------------------------
    # Position tracking
    # ----------------------------------------------------------

    def at_max_positions(self) -> bool:
        return self.position_count >= self.max_positions

    def increment_positions(self) -> None:
        self.position_count += 1

    def decrement_positions(self) -> None:
        self.position_count = max(0, self.position_count - 1)

    # ----------------------------------------------------------
    # Daily loss limit
    # ----------------------------------------------------------

    def record_loss(self, loss_amount: float) -> None:
        """Record a loss (positive number)."""
        self.daily_loss += abs(loss_amount)

    def is_daily_loss_exceeded(self) -> bool:
        if self.equity_start <= 0:
            return False
        loss_pct = (self.daily_loss / self.equity_start) * 100
        return loss_pct >= self.max_daily_loss_pct

    # ----------------------------------------------------------
    # Snapshot / persistence
    # ----------------------------------------------------------

    def snapshot(self) -> dict[str, Any]:
        """Full state snapshot for dashboard or persistence."""
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "cycle_count": self.cycle_count,
            "position_count": self.position_count,
            "equity_start": self.equity_start,
            "daily_loss": self.daily_loss,
            "zone_entry_counts": dict(self.zone_entry_counts),
            "ct_failure_counts": dict(self.ct_failure_counts),
            "active_cooldowns": {
                k: v.isoformat() for k, v in self.cooldowns.items()
                if v > datetime.utcnow()
            },
        }

    def persist(self) -> None:
        """Save state to disk for restart recovery."""
        if self._persist_path:
            snap = self.snapshot()
            with open(self._persist_path, "w") as f:
                json.dump(snap, f, indent=2, default=str)
            log.debug("[STATE] Persisted to %s", self._persist_path)

    def restore(self) -> bool:
        """Restore state from disk."""
        if self._persist_path and self._persist_path.exists():
            with open(self._persist_path) as f:
                data = json.load(f)
            self.cycle_count = data.get("cycle_count", 0)
            self.position_count = data.get("position_count", 0)
            self.equity_start = data.get("equity_start", 0.0)
            self.daily_loss = data.get("daily_loss", 0.0)
            self.zone_entry_counts = defaultdict(int, data.get("zone_entry_counts", {}))
            self.ct_failure_counts = defaultdict(int, data.get("ct_failure_counts", {}))
            log.info("[STATE] Restored from %s", self._persist_path)
            return True
        return False
