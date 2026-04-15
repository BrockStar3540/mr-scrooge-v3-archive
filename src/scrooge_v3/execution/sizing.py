"""Position sizing — risk-based calculation.

Sizes positions so that the stop loss distance risks a fixed
percentage of account equity (default 1%). This produces sane
unit counts regardless of margin rate or leverage.
"""

from __future__ import annotations

import logging
from typing import Any

log = logging.getLogger("scrooge_v3.execution.sizing")


class SizingCalculator:
    """Risk-based sizing.

    units = (equity * risk_pct) / stop_distance_in_account_currency

    Example: $80K equity, 1% risk = $800.
    Stop is 5 pips on NZD/USD (pip value ~$1/unit) → 800 / 0.0005 = ~160K units.
    """

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.risk_pct = config.get("risk_pct", 0.01)  # 1% of equity per trade
        self.max_units = config.get("max_units", 500_000)  # absolute cap

    def calculate(
        self,
        symbol: str,
        current_price: float,
        equity: float,
        instrument_info: dict[str, Any] | None = None,
        stop_distance: float = 0.0,
        **kwargs: Any,
    ) -> int | None:
        """Returns integer unit count based on risk.

        Args:
            symbol: Instrument symbol
            current_price: Current mid price
            equity: Account equity
            instrument_info: Dict with pipLocation, marginRate
            stop_distance: Distance from entry to stop in price units
        """
        if equity <= 0 or stop_distance <= 0:
            log.warning("[SIZING] %s: equity=%.0f stop_dist=%.5f — cannot size",
                        symbol, equity, stop_distance)
            return None

        risk_amount = equity * self.risk_pct
        units = round(risk_amount / stop_distance)

        if units < 1:
            log.warning("[SIZING] %s: sized to %d units — too small", symbol, units)
            return None

        if units > self.max_units:
            log.info("[SIZING] %s: capped %d → %d units", symbol, units, self.max_units)
            units = self.max_units

        info = instrument_info or {}
        pip_size = 10 ** int(info.get("pipLocation", -4))
        risk_pips = stop_distance / pip_size if pip_size > 0 else 0

        log.info(
            "[SIZING] %s: %d units | equity $%.0f | risk $%.0f (%.1f%%) | "
            "stop %.1f pips | $%.2f/pip",
            symbol, units, equity, risk_amount, self.risk_pct * 100,
            risk_pips, units * pip_size,
        )
        return units
