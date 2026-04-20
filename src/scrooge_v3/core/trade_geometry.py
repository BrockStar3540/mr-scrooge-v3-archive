"""Trade geometry — single source of truth for pip math, pair classification,
initial risk, and R<->price conversions.

Every management module (BE, ratchet, trail, harvest, sizing) must use these
helpers rather than computing pip_size / initial_risk locally. That guarantees
JPY vs non-JPY handling is consistent and prevents 10x rounding bugs.

Phase 3 — fix/mgmt-r-unified.
"""

from __future__ import annotations

from enum import Enum
from typing import Callable


class PairFamily(Enum):
    """Pair family — compatible with the classify_pair(...) strings used by
    `execution.sizing.classify_pair` ("usd_base", "usd_quote", "cross").
    Adds JPY_CROSS explicitly for pip-size decisions.
    """
    USD_BASE = "usd_base"      # e.g. USD_JPY
    USD_QUOTE = "usd_quote"    # e.g. EUR_USD
    JPY_CROSS = "jpy_cross"    # e.g. EUR_JPY, AUD_JPY
    CROSS = "cross"            # e.g. EUR_GBP


def pip_size(symbol: str) -> float:
    """Canonical pip size: 0.01 for JPY pairs, 0.0001 otherwise.

    This is THE function to use. Do not check `"JPY" in symbol` ad-hoc.
    """
    if not symbol:
        return 0.0001
    # OANDA uses UNDERSCORE naming (USD_JPY, AUD_JPY, EUR_USD).
    # Any leg being JPY => 0.01 pip.
    parts = symbol.split("_")
    if any(p == "JPY" for p in parts):
        return 0.01
    return 0.0001


def classify_pair(symbol: str) -> PairFamily:
    """Classify a pair into its family.

    Import-compatible with `execution.sizing.classify_pair` (which returns the
    string value). Use `.value` to get the legacy string if you must interop.
    """
    parts = symbol.split("_")
    if len(parts) != 2:
        return PairFamily.CROSS
    base, quote = parts
    if base == "USD":
        return PairFamily.USD_BASE
    if quote == "USD":
        return PairFamily.USD_QUOTE
    if base == "JPY" or quote == "JPY":
        return PairFamily.JPY_CROSS
    return PairFamily.CROSS


def pip_value_usd(
    symbol: str,
    price: float,
    conversion_lookup: Callable[[str], float | None] | None = None,
) -> float:
    """Per-unit pip value in USD.

    Thin wrapper: delegates to `execution.sizing.compute_notional_and_pip`
    so we don't fork the conversion logic, but exposes it via the canonical
    `trade_geometry` facade.
    """
    # Local import to avoid a module-level cycle.
    from scrooge_v3.execution.sizing import compute_notional_and_pip
    _, pip_usd, _ = compute_notional_and_pip(
        symbol, price, pip_size(symbol), conversion_lookup,
    )
    return pip_usd


def initial_risk(entry: float, sl: float) -> float:
    """Distance from entry to stop — always positive.

    This is the 1R unit. Snapshotted at entry time and never recomputed
    against a moving stop.
    """
    return abs(entry - sl)


def r_to_price_distance(r: float, initial_risk_distance: float) -> float:
    """Convert an R-multiple to a price distance."""
    return r * initial_risk_distance


def price_distance_to_r(dist: float, initial_risk_distance: float) -> float:
    """Convert a price distance to an R-multiple."""
    if initial_risk_distance <= 0:
        return 0.0
    return dist / initial_risk_distance


def r_to_price(
    entry: float,
    direction_sign: int,
    r: float,
    initial_risk_distance: float,
) -> float:
    """Compute absolute price at an R-multiple from entry.

    direction_sign: +1 for long (profit above entry), -1 for short.
    """
    return entry + direction_sign * r * initial_risk_distance


def compute_tp1(
    entry_price: float,
    stop_price: float,
    direction: str,
    tp1_r: float = 1.0,
) -> float:
    """Unified TP1 in R-multiples from entry/stop.

    `direction`: "long" or "short" (accepts `TradeDirection.value`).
    Returns 0.0 if stop_price is invalid.

    This replaces the per-strategy TP1 levels (bollinger center, impulse
    distance, breakout peak) that produced wildly inconsistent R-multiples
    across pairs — see task context trades 1445/1502/1488.
    """
    if stop_price is None or stop_price <= 0 or entry_price <= 0:
        return 0.0
    risk = initial_risk(entry_price, stop_price)
    if risk <= 0:
        return 0.0
    sign = 1 if str(direction).lower() == "long" else -1
    return entry_price + sign * tp1_r * risk


__all__ = [
    "PairFamily",
    "pip_size",
    "classify_pair",
    "pip_value_usd",
    "initial_risk",
    "r_to_price_distance",
    "price_distance_to_r",
    "r_to_price",
    "compute_tp1",
]
