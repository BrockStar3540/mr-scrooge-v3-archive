"""Centralized time and session authority for Mr. Scrooge V3.

Design rules (locked 2026-04-20):
  1. UTC is canonical everywhere. All timestamps stored and compared as UTC.
  2. OANDA is source of truth for market structure — box days anchor to OANDA's
     daily-candle convention (NY 17:00 close), implemented deterministically
     from the convention, NOT via live broker fetch per call.
  3. Session labels are a pure function of UTC timestamp. DST is handled via
     zoneinfo at each financial center.
  4. Nine semantic session labels replace the broken 5-bucket fixed-UTC map.
  5. Scorer threshold selection goes through SessionThresholdProfile + a
     compatibility mapping table (temporary — to be recalibrated via replay).
  6. Production code injects a Clock. Replay injects FixedClock. Never call
     datetime.now() directly in decision paths.

This module is the ONLY place that answers:
  - what time is it now?
  - what session are we in?
  - when does the current box day start?
  - is this a weekly re-open?
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Protocol
from zoneinfo import ZoneInfo

# Financial center timezones (DST-aware via zoneinfo).
_TZ_LONDON = ZoneInfo("Europe/London")
_TZ_NY = ZoneInfo("America/New_York")
_TZ_SYDNEY = ZoneInfo("Australia/Sydney")
_TZ_TOKYO = ZoneInfo("Asia/Tokyo")

# Local market hours at each center (local time, inclusive start, exclusive end).
_LONDON_OPEN, _LONDON_CLOSE = 8, 16
_NY_OPEN, _NY_CLOSE = 8, 17
_SYDNEY_OPEN, _SYDNEY_CLOSE = 7, 16
_TOKYO_OPEN, _TOKYO_CLOSE = 9, 18

# OANDA daily-candle convention: day closes at NY 17:00 local.
_OANDA_DAY_BOUNDARY_HOUR_NY = 17


class SessionLabel(str, Enum):
    """Nine semantic FX session labels, DST-aware."""

    WEEKLY_OPEN = "weekly_open"              # Sunday 20:00+ UTC — gap-risk flag
    SYDNEY_ONLY = "sydney_only"              # Sydney open, Tokyo not yet
    SYDNEY_TOKYO = "sydney_tokyo"            # both active
    TOKYO_ONLY = "tokyo_only"                # Tokyo active, Sydney closed, London not yet
    TOKYO_LONDON = "tokyo_london"            # Tokyo+London overlap
    LONDON_ONLY = "london_only"              # London active, Tokyo closed, NY not yet
    LONDON_NY_OVERLAP = "london_ny_overlap"  # highest-volume window
    NY_ONLY = "ny_only"                      # NY active, London closed
    DEAD_ZONE = "dead_zone"                  # all majors closed (rare)


@dataclass(frozen=True)
class SessionThresholdProfile:
    """Scorer thresholds for a single session. Replaces the hardcoded tuple."""

    base_floor: int
    b_tier: int
    a_tier: int
    pair_cap: int

    def as_tuple(self) -> tuple[int, int, int, int]:
        """Legacy-compat tuple form used by v3_scorer."""
        return (self.base_floor, self.b_tier, self.a_tier, self.pair_cap)


# Current production thresholds — 5 legacy buckets, calibrated on 50 trades.
# Kept as-is for Option A compatibility mode. Replay-driven recalibration to
# proper 9-bucket profiles is tracked in the follow-up task.
_LEGACY_PROFILES = {
    "asia_london_open": SessionThresholdProfile(30, 44, 54, 16),
    "london":           SessionThresholdProfile(32, 44, 54, 12),
    "ny_active":        SessionThresholdProfile(30, 42, 50, 12),
    "late_ny":          SessionThresholdProfile(34, 44, 54, 10),
    "dead_late":        SessionThresholdProfile(40, 52, 62, 8),
}

_LEGACY_PROFILES_TREND = {
    "asia_london_open": SessionThresholdProfile(28, 42, 52, 16),
    "london":           SessionThresholdProfile(30, 42, 52, 12),
    "ny_active":        SessionThresholdProfile(28, 40, 48, 12),
    "late_ny":          SessionThresholdProfile(32, 42, 52, 10),
    "dead_late":        SessionThresholdProfile(38, 50, 60, 8),
}

# Compatibility map: new 9 labels → legacy 5 buckets.
# Every Sydney/Tokyo-only window maps to asia_london_open.
# Every London window maps to london.
# All NY windows (including overlap) map to ny_active.
# Weekly open and dead zone map to dead_late.
# The late_ny legacy bucket (18-19 UTC) had its own thresholds — under the new
# model those hours are NY_ONLY, which gets ny_active thresholds. This is a
# known, small behavior drift and is acceptable for compat mode; the backtester
# will decide the correct 9-bucket thresholds later.
_COMPAT_LEGACY_KEY = {
    SessionLabel.WEEKLY_OPEN: "dead_late",
    SessionLabel.SYDNEY_ONLY: "dead_late",
    SessionLabel.SYDNEY_TOKYO: "asia_london_open",
    SessionLabel.TOKYO_ONLY: "asia_london_open",
    SessionLabel.TOKYO_LONDON: "london",
    SessionLabel.LONDON_ONLY: "london",
    SessionLabel.LONDON_NY_OVERLAP: "ny_active",
    SessionLabel.NY_ONLY: "ny_active",
    SessionLabel.DEAD_ZONE: "dead_late",
}


def compat_threshold_profile(label: SessionLabel, family: str = "default") -> SessionThresholdProfile:
    """Map a 9-label session to its compat legacy threshold profile.

    This is the bridge that lets us ship corrected session detection without
    changing scoring policy. Replace this function (not the scorer) once
    backtester produces calibrated 9-bucket thresholds.
    """
    legacy_key = _COMPAT_LEGACY_KEY[label]
    table = _LEGACY_PROFILES_TREND if family == "trend" else _LEGACY_PROFILES
    return table[legacy_key]


# Hour-penalty compat map. Legacy scorer used a raw UTC-hour bucket table:
#   h < 8: +10, h < 12: +2, h < 16: -3, h < 18: -1, h < 20: -3, else: -7
# That was a session-quality prior masquerading as a UTC hour lookup. Under
# the clock, we derive the penalty from the session label so DST is handled
# automatically. Values are picked to match the dominant legacy value for
# each label's typical UTC hours — same compat strategy as thresholds.
#
# Known drifts from legacy (all intentional, same DST-correction set):
#   - NY_ONLY covers old h<18 / h<20 / h>=20 spans; we pick -3 (dominant).
#     18-19 UTC hours now read -3 instead of legacy -1 (late_ny relief bucket
#     is dropped, same as for thresholds).
#   - Summer 07 UTC (TOKYO_LONDON) reads +2 instead of legacy +10.
#     London is actually open in BST; the old +10 was DST-wrong.
_COMPAT_HOUR_PENALTY = {
    SessionLabel.WEEKLY_OPEN: -7,
    SessionLabel.SYDNEY_ONLY: -7,
    SessionLabel.SYDNEY_TOKYO: 10,
    SessionLabel.TOKYO_ONLY: 10,
    SessionLabel.TOKYO_LONDON: 2,
    SessionLabel.LONDON_ONLY: 2,
    SessionLabel.LONDON_NY_OVERLAP: -3,
    SessionLabel.NY_ONLY: -3,
    SessionLabel.DEAD_ZONE: -7,
}


def compat_hour_penalty(label: SessionLabel) -> int:
    """Session-label-derived hour penalty (compat mode).

    Replaces the scorer's raw UTC hour if/elif. Uses session-label-to-value
    mapping so DST is handled through the clock. Recalibration of per-label
    values will come from the Oanda-Bot-Trainer backtester.
    """
    return _COMPAT_HOUR_PENALTY[label]


def _in_window(hour: int, open_h: int, close_h: int) -> bool:
    return open_h <= hour < close_h


def session_label_from_utc(ts_utc: datetime) -> SessionLabel:
    """Pure function: UTC timestamp → 9-label session classification.

    Precedence: weekly_open > overlaps > single-center > dead_zone.
    All open/close checks use zoneinfo local time, so DST is automatic.
    """
    if ts_utc.tzinfo is None:
        raise ValueError("session_label_from_utc requires tz-aware UTC datetime")

    # Weekly open: Sunday 20:00-24:00 UTC (Sydney begins reopening).
    if ts_utc.weekday() == 6 and ts_utc.hour >= 20:
        return SessionLabel.WEEKLY_OPEN

    london_h = ts_utc.astimezone(_TZ_LONDON).hour
    ny_h = ts_utc.astimezone(_TZ_NY).hour
    sydney_h = ts_utc.astimezone(_TZ_SYDNEY).hour
    tokyo_h = ts_utc.astimezone(_TZ_TOKYO).hour

    london_open = _in_window(london_h, _LONDON_OPEN, _LONDON_CLOSE)
    ny_open = _in_window(ny_h, _NY_OPEN, _NY_CLOSE)
    sydney_open = _in_window(sydney_h, _SYDNEY_OPEN, _SYDNEY_CLOSE)
    tokyo_open = _in_window(tokyo_h, _TOKYO_OPEN, _TOKYO_CLOSE)

    # Overlaps first (most specific wins).
    if london_open and ny_open:
        return SessionLabel.LONDON_NY_OVERLAP
    if ny_open:
        return SessionLabel.NY_ONLY
    if tokyo_open and london_open:
        return SessionLabel.TOKYO_LONDON
    if london_open:
        return SessionLabel.LONDON_ONLY
    if sydney_open and tokyo_open:
        return SessionLabel.SYDNEY_TOKYO
    if tokyo_open:
        return SessionLabel.TOKYO_ONLY
    if sydney_open:
        return SessionLabel.SYDNEY_ONLY
    return SessionLabel.DEAD_ZONE


def is_weekly_open(ts_utc: datetime) -> bool:
    """Separate flag — true whenever we're in Sunday's re-open window.

    A caller may want this even while mapping the label to a different threshold
    profile (gap-risk surcharge, widened spread expectation, etc.)
    """
    return ts_utc.weekday() == 6 and ts_utc.hour >= 20


def box_day_start_utc(ts_utc: datetime) -> datetime:
    """Return the start of the OANDA trading day that contains ts_utc.

    Deterministic. Uses NY 17:00 local as the day boundary, matching OANDA's
    default D-candle close convention. DST-aware (boundary shifts 1 hr in UTC
    twice a year, same as OANDA's own daily candles do).
    """
    if ts_utc.tzinfo is None:
        raise ValueError("box_day_start_utc requires tz-aware UTC datetime")
    ny = ts_utc.astimezone(_TZ_NY)
    if ny.hour >= _OANDA_DAY_BOUNDARY_HOUR_NY:
        start_ny = ny.replace(hour=_OANDA_DAY_BOUNDARY_HOUR_NY, minute=0, second=0, microsecond=0)
    else:
        prev = ny - timedelta(days=1)
        start_ny = prev.replace(hour=_OANDA_DAY_BOUNDARY_HOUR_NY, minute=0, second=0, microsecond=0)
    return start_ny.astimezone(timezone.utc)


def trading_day_id(ts_utc: datetime) -> str:
    """Stable string id for the OANDA trading day containing ts_utc (e.g. '2025-03-14')."""
    return box_day_start_utc(ts_utc).astimezone(_TZ_NY).strftime("%Y-%m-%d")


class Clock(Protocol):
    """The one authoritative time source. Inject everywhere decision-critical."""

    def now_utc(self) -> datetime: ...
    def session_label(self) -> SessionLabel: ...
    def is_weekly_open(self) -> bool: ...
    def box_day_start(self) -> datetime: ...
    def trading_day_id(self) -> str: ...


class OandaClock:
    """Live clock. Uses system UTC wall-clock by default.

    Future extension: for stricter broker-time alignment, accept an optional
    'broker_skew_seconds' that offsets system time based on observed OANDA
    response timestamps. Not needed for V3 today — skew vs OANDA is < 1s.
    """

    def now_utc(self) -> datetime:
        return datetime.now(timezone.utc)

    def session_label(self) -> SessionLabel:
        return session_label_from_utc(self.now_utc())

    def is_weekly_open(self) -> bool:
        return is_weekly_open(self.now_utc())

    def box_day_start(self) -> datetime:
        return box_day_start_utc(self.now_utc())

    def trading_day_id(self) -> str:
        return trading_day_id(self.now_utc())


class FixedClock:
    """Replay clock. Holds a fixed UTC timestamp; test or backtester sets it."""

    def __init__(self, t: datetime) -> None:
        if t.tzinfo is None:
            raise ValueError("FixedClock requires tz-aware UTC datetime")
        self._t = t.astimezone(timezone.utc)

    def set(self, t: datetime) -> None:
        if t.tzinfo is None:
            raise ValueError("FixedClock.set requires tz-aware UTC datetime")
        self._t = t.astimezone(timezone.utc)

    def now_utc(self) -> datetime:
        return self._t

    def session_label(self) -> SessionLabel:
        return session_label_from_utc(self._t)

    def is_weekly_open(self) -> bool:
        return is_weekly_open(self._t)

    def box_day_start(self) -> datetime:
        return box_day_start_utc(self._t)

    def trading_day_id(self) -> str:
        return trading_day_id(self._t)


# Process-level default. Production sets this to OandaClock() at startup;
# replay sets it to a FixedClock per bar. Individual callers may also receive
# a clock via DI in hot paths.
_default_clock: Clock = OandaClock()


def get_clock() -> Clock:
    return _default_clock


def set_clock(clock: Clock) -> None:
    """Replace the process-wide default clock. Used by bootstrap and replay."""
    global _default_clock
    _default_clock = clock
