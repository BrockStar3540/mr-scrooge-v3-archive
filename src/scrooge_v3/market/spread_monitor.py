"""Spread monitor — tracks live spread conditions per symbol.

Used by the spread gate and spread-aware trailing logic to detect
hostile spread environments where stop placement is dangerous.
"""

from __future__ import annotations

import logging
from collections import defaultdict, deque
from datetime import datetime
from typing import Any

log = logging.getLogger("scrooge_v3.market.spread_monitor")


class SpreadMonitor:
    """Tracks rolling spread statistics per symbol."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.window_size = config.get("window_size", 60)  # rolling window
        self.spike_multiplier = config.get("spike_multiplier", 3.0)
        self._history: dict[str, deque] = defaultdict(lambda: deque(maxlen=self.window_size))

    def record(self, symbol: str, spread: float) -> None:
        """Record a spread observation."""
        self._history[symbol].append(spread)

    def get_stats(self, symbol: str) -> dict[str, float]:
        """Return current spread statistics for a symbol."""
        history = self._history.get(symbol)
        if not history or len(history) < 2:
            return {"current": 0.0, "mean": 0.0, "max": 0.0, "is_hostile": False}

        current = history[-1]
        values = list(history)
        mean = sum(values) / len(values)
        max_spread = max(values)

        return {
            "current": current,
            "mean": mean,
            "max": max_spread,
            "is_hostile": current > mean * self.spike_multiplier,
        }

    def is_hostile(self, symbol: str) -> bool:
        """Return True if current spread is hostile (spike detected)."""
        stats = self.get_stats(symbol)
        return stats.get("is_hostile", False)
