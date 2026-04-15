"""Range state models — tracking session range lifecycle and breaches."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from scrooge_v3.features.models import SessionRange


class RangeState(Enum):
    RANGING = "RANGING"
    BREACH_INITIATED = "BREACH_INITIATED"
    CONFIRMED_BREAK_RECALCULATING = "CONFIRMED_BREAK_RECALCULATING"
    NEW_RANGE_STANDBY = "NEW_RANGE_STANDBY"
    SHELVED = "SHELVED"


@dataclass
class RangeStateRecord:
    """Full state snapshot for one instrument."""
    symbol: str
    state: RangeState
    active_range: SessionRange
    alternative_range: Optional[SessionRange]
    using_alternative: bool

    # Breach tracking
    breach_started_at: Optional[str]
    breach_price: float
    breach_direction: str           # 'up' or 'down'
    breach_candles_confirmed: int

    # Range age confidence
    session_start_time: str
    range_age_hours: float
    age_confidence_pct: float       # 100% -> 50% through session

    # Confirmation requirements (tighten as range ages)
    confirmation_gates_required: int  # 2 or 3 — goes to 3 as range ages

    # New range proven status
    new_range_trades: int             # Successful trades in new range
    new_range_proven: bool            # True after 3 successful trades

    # Return-to-range setup
    broken_wall_price: float        # Price of broken wall for RTR setup
    broken_wall_direction: str      # Which wall was broken

    # Current status
    entry_paused: bool
    pause_reason: str
    last_spread: float
    spread_threshold: float
    last_updated: str
    spread_bad_count: int = 0  # consecutive scans with spread > threshold


@dataclass
class AlternativeRangeResult:
    """Result of drawing a new alternative range."""
    success: bool
    new_range: Optional[SessionRange]
    method: str                     # 'original_wall_to_new_extreme', 'session_cheat_code'
    viable: bool
    viability_reason: str
    efficiency_ratio: float
