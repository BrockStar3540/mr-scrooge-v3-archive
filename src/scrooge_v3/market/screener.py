"""Universe screener — session-aware instrument selection.

Determines which currency pairs are active based on current UTC hour
and trading session windows. Supports balanced, standard, and aggressive modes.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

log = logging.getLogger("scrooge_v3.market.screener")


# Proven profitable pairs
BASE_PAIRS = {
    "AUD_CAD", "AUD_CHF", "USD_JPY", "EUR_CAD", "CHF_JPY",
}

# Tradable but conservative — excluded from thin sessions in balanced mode
PROBATION_PAIRS = {
    "AUD_USD", "EUR_GBP", "EUR_JPY",
    "GBP_AUD", "GBP_CAD", "GBP_JPY", "NZD_USD",
}

SESSION_WINDOWS = [
    {
        "name": "Sydney",
        "open_utc": 21,
        "close_utc": 6,
        "pairs": [
            "AUD_USD", "NZD_USD", "AUD_NZD", "AUD_CAD", "AUD_JPY", "NZD_JPY",
        ],
    },
    {
        "name": "Tokyo",
        "open_utc": 0,
        "close_utc": 9,
        "pairs": [
            "USD_JPY", "EUR_JPY", "GBP_JPY", "AUD_JPY", "CAD_JPY", "CHF_JPY",
            "NZD_JPY", "AUD_USD", "NZD_USD", "AUD_NZD",
        ],
    },
    {
        "name": "London",
        "open_utc": 7,
        "close_utc": 16,
        "pairs": [
            "EUR_USD", "GBP_USD", "EUR_GBP", "EUR_JPY", "GBP_JPY", "EUR_CHF",
            "GBP_CHF", "EUR_CAD", "EUR_AUD", "EUR_NZD", "GBP_CAD", "GBP_AUD",
            "GBP_NZD", "USD_CHF", "USD_JPY", "AUD_CHF",
        ],
    },
    {
        "name": "New York",
        "open_utc": 13,
        "close_utc": 22,
        "pairs": [
            "EUR_USD", "GBP_USD", "USD_JPY", "USD_CAD", "USD_CHF", "AUD_USD",
            "NZD_USD", "EUR_JPY", "GBP_JPY", "EUR_GBP", "CAD_JPY", "EUR_CAD",
            "GBP_CAD",
        ],
    },
]

CANDIDATE_PAIRS = [
    # Dollar majors
    "EUR_USD", "GBP_USD", "USD_JPY", "AUD_USD",
    "USD_CHF", "USD_CAD", "NZD_USD", "USD_MXN",
    # JPY crosses
    "EUR_JPY", "GBP_JPY", "AUD_JPY", "CAD_JPY", "CHF_JPY", "NZD_JPY",
    # EUR crosses
    "EUR_GBP", "EUR_CAD", "EUR_AUD", "EUR_NZD", "EUR_CHF",
    # GBP crosses
    "GBP_CAD", "GBP_AUD", "GBP_NZD", "GBP_CHF",
    # Commodity crosses
    "AUD_CAD", "AUD_NZD", "AUD_CHF",
]


def get_active_sessions(utc_hour: int) -> list[dict[str, Any]]:
    """Returns list of session dicts currently open."""
    active = []
    for session in SESSION_WINDOWS:
        o = session["open_utc"]
        c = session["close_utc"]
        if o > c:  # crosses midnight (e.g. Sydney 21-6)
            if utc_hour >= o or utc_hour < c:
                active.append(session)
        else:
            if o <= utc_hour < c:
                active.append(session)
    return active


def get_session_pairs(utc_hour: int, mode: str = "balanced") -> list[str]:
    """Session-aware pair list.

    Modes:
      balanced (default): suppress probation pairs when only thin sessions
        (Sydney/Tokyo) are open; include full list when London/NY open.
      standard: all session pairs regardless.
      aggressive: all candidate pairs for any open session.
    """
    active_sessions = get_active_sessions(utc_hour)
    if not active_sessions:
        return list(CANDIDATE_PAIRS)

    mode = (mode or "balanced").lower()
    active_names = {s["name"] for s in active_sessions}
    liquid_open = bool(active_names & {"London", "New York"})

    if mode == "aggressive":
        return list(CANDIDATE_PAIRS)

    seen: set[str] = set()
    pairs: list[str] = []
    for session in active_sessions:
        for p in session["pairs"]:
            if p in seen:
                continue
            # In balanced mode, skip probation pairs during thin sessions
            if mode == "balanced" and not liquid_open and p in PROBATION_PAIRS:
                continue
            seen.add(p)
            pairs.append(p)

    return pairs


def is_weekend() -> bool:
    """Return True if forex market is closed (Saturday/Sunday UTC)."""
    now = datetime.now(timezone.utc)
    # Market closes Friday ~22:00 UTC, opens Sunday ~22:00 UTC
    weekday = now.weekday()
    hour = now.hour
    if weekday == 5:  # Saturday
        return True
    if weekday == 6 and hour < 22:  # Sunday before 22:00
        return True
    if weekday == 4 and hour >= 22:  # Friday after 22:00
        return True
    return False
