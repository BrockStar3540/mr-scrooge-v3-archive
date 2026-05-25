"""Mr Scrooge V3 — backtesting.py replay lab.

Deterministic offline replay around the LIVE strategy modules. Use for:
  - Strategy truth-testing (does the code actually have edge?)
  - Direction inversion experiments (long vs short on same bars)
  - Entry-geometry experiments (signal vs pullback)
  - Management ablations (TP1/BE/ratchet on vs off)
  - Regression suite (catch silent drift on every commit)

NOT for:
  - Broker timeout / orphan-order behavior
  - Cross-pair portfolio throttles
  - Live engine simulation
"""
from .models import (
    ReplaySpec, DirectionMode, EntryMode, RoutingMode, ManagementMode,
)

__all__ = [
    "ReplaySpec", "DirectionMode", "EntryMode", "RoutingMode", "ManagementMode",
]
