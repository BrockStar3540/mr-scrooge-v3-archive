"""Position sizing — margin-utilization based calculation.

Determines unit count based on equity, margin rate, and free margin caps.
Computes notional and pip value per unit in account currency (USD) based on
instrument family: USD-base, USD-quote, or cross.

Broker-agnostic interface — the caller is responsible for resolving any
USD conversion rate needed for cross pairs (via an optional lookup callable).
"""

from __future__ import annotations

import logging
from typing import Any, Callable

log = logging.getLogger("scrooge_v3.execution.sizing")


def classify_pair(symbol: str) -> str:
    """Return "usd_base" | "usd_quote" | "cross"."""
    parts = symbol.split("_")
    if len(parts) != 2:
        return "cross"
    base, quote = parts
    if base == "USD":
        return "usd_base"
    if quote == "USD":
        return "usd_quote"
    return "cross"


def compute_notional_and_pip(
    symbol: str,
    current_price: float,
    pip_size: float,
    usd_conversion_lookup: Callable[[str], float | None] | None = None,
) -> tuple[float, float, str]:
    """Compute (notional_per_unit_USD, pip_value_per_unit_USD, family).

    Rules:
      USD-base  (USD_JPY): 1 unit = 1 USD notional; pip value = pip_size / current_price
      USD-quote (EUR_USD): 1 unit = current_price USD notional; pip value = pip_size (in USD)
      Cross     (EUR_JPY): need conversion of base-currency -> USD
                           notional_per_unit_USD  = base_to_USD
                           pip_value_per_unit_USD = pip_size * base_to_USD / current_price

    If a conversion is needed but lookup returns None, falls back to an
    approximation (treat base_to_USD == 1.0) and returns family = "cross_approx".
    """
    family = classify_pair(symbol)
    parts = symbol.split("_")
    base = parts[0] if len(parts) >= 1 else ""

    if family == "usd_base":
        notional = 1.0
        pip_usd = pip_size / current_price if current_price > 0 else 0.0
        return notional, pip_usd, family

    if family == "usd_quote":
        notional = current_price
        pip_usd = pip_size
        return notional, pip_usd, family

    base_to_usd: float | None = None
    if usd_conversion_lookup is not None:
        try:
            base_to_usd = usd_conversion_lookup(base)
        except Exception as exc:  # pragma: no cover
            log.warning("[SIZING] %s: conversion lookup failed for %s: %s", symbol, base, exc)
            base_to_usd = None

    if base_to_usd is None or base_to_usd <= 0:
        log.warning(
            "[SIZING] %s: cross pair with no USD conversion for %s — "
            "approximating base_to_USD=1.0 (position may be mis-sized)",
            symbol, base,
        )
        base_to_usd = 1.0
        family = "cross_approx"

    notional = base_to_usd
    pip_usd = (pip_size * base_to_usd / current_price) if current_price > 0 else 0.0
    return notional, pip_usd, family


class SizingCalculator:
    """Margin-utilization sizing.

    units = (equity * margin_utilization) / (notional_per_unit_USD * margin_rate)

    Caps at 80% of free margin to avoid INSUFFICIENT_MARGIN rejections.
    """

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.margin_utilization = config.get("margin_utilization", 0.40)

    def calculate(
        self,
        symbol: str,
        current_price: float,
        equity: float,
        instrument_info: dict[str, Any] | None = None,
        pip_value_per_unit: float = 0.0,
        free_margin: float | None = None,
        notional_per_unit: float = 0.0,
        usd_conversion_lookup: Callable[[str], float | None] | None = None,
    ) -> int | None:
        """Returns integer unit count, or None if sizing is impossible.

        If notional_per_unit and pip_value_per_unit are not provided, they
        are computed from symbol family via compute_notional_and_pip().
        """
        info = instrument_info or {}
        pip_size = 10 ** int(info.get("pipLocation", -4))
        margin_rate = float(info.get("marginRate", 0.0333))

        fam = classify_pair(symbol)
        if notional_per_unit <= 0 or pip_value_per_unit <= 0:
            n, p, fam = compute_notional_and_pip(
                symbol, current_price, pip_size, usd_conversion_lookup,
            )
            if notional_per_unit <= 0:
                notional_per_unit = n
            if pip_value_per_unit <= 0:
                pip_value_per_unit = p

        if notional_per_unit <= 0:
            log.warning("[SIZING] %s: notional_per_unit=%.6f — cannot size",
                        symbol, notional_per_unit)
            return None

        target_margin = equity * self.margin_utilization
        units = round(target_margin / (notional_per_unit * margin_rate))

        if units < 1:
            log.warning("[SIZING] %s: sized to %d units — too small", symbol, units)
            return None

        if free_margin is not None:
            usable = free_margin * 0.80
            max_units = round(usable / (notional_per_unit * margin_rate))
            if max_units < 1:
                log.warning("[SIZING] %s: insufficient free margin ($%.2f)", symbol, free_margin)
                return None
            if units > max_units:
                if max_units < units * 0.50:
                    log.warning(
                        "[SIZING] %s: margin cap too severe (%d < 50%% of %d) — skip",
                        symbol, max_units, units,
                    )
                    return None
                log.info("[SIZING] %s: units capped by margin: %d -> %d", symbol, units, max_units)
                units = max_units

        pip_dollar = units * pip_value_per_unit
        log.info(
            "[SIZING] %s (%s): %d units | equity $%.0f | "
            "margin target $%.0f (%.0f%%) | margin_rate %.2f%% | "
            "notional/unit $%.4f | $%.2f/pip",
            symbol, fam, units, equity, target_margin,
            self.margin_utilization * 100, margin_rate * 100,
            notional_per_unit, pip_dollar,
        )
        return units
