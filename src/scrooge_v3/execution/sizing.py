"""Position sizing — margin-utilization based calculation.

Determines unit count based on equity, margin rate, and free margin caps.
Broker-agnostic interface — requires instrument metadata and pip values
but does not call the broker directly.
"""

from __future__ import annotations

import logging
from typing import Any

log = logging.getLogger("scrooge_v3.execution.sizing")


class SizingCalculator:
    """Margin-utilization sizing.

    base_units = (equity * margin_utilization) / (base_price_usd * margin_rate)
    Caps at 80% of free margin to avoid INSUFFICIENT_MARGIN rejections.
    """

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.margin_utilization = config.get("margin_utilization", 0.80)

    def calculate(
        self,
        symbol: str,
        current_price: float,
        equity: float,
        instrument_info: dict[str, Any] | None = None,
        pip_value_per_unit: float = 0.0,
        free_margin: float | None = None,
    ) -> int | None:
        """Returns integer unit count, or None if sizing is impossible.

        Args:
            symbol: Instrument symbol
            current_price: Current mid price
            equity: Account equity
            instrument_info: Dict with pipLocation, marginRate
            pip_value_per_unit: Value of one pip per one unit in account currency
            free_margin: Available margin (optional cap)
        """
        info = instrument_info or {}
        pip_size = 10 ** int(info.get("pipLocation", -4))
        margin_rate = float(info.get("marginRate", 0.0333))

        if pip_value_per_unit <= 0:
            pip_value_per_unit = pip_size  # rough fallback

        base_price_usd = pip_value_per_unit * current_price / pip_size if pip_size > 0 else current_price
        if base_price_usd <= 0:
            log.warning("[SIZING] %s: base_price_usd=%.4f — cannot size", symbol, base_price_usd)
            return None

        target_margin = equity * self.margin_utilization
        units = round(target_margin / (base_price_usd * margin_rate))

        if units < 1:
            log.warning("[SIZING] %s: sized to %d units — too small", symbol, units)
            return None

        # Cap to 80% of free margin
        if free_margin is not None:
            usable = free_margin * 0.80
            max_units = round(usable / (base_price_usd * margin_rate))
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
                log.info("[SIZING] %s: units capped by margin: %d → %d", symbol, units, max_units)
                units = max_units

        pip_dollar = units * pip_value_per_unit
        log.info(
            "[SIZING] %s: %d units | equity $%.0f | "
            "margin target $%.0f (%.0f%%) | margin_rate %.2f%% | $%.2f/pip",
            symbol, units, equity, target_margin,
            self.margin_utilization * 100, margin_rate * 100, pip_dollar,
        )
        return units
