"""Fee calculator — spread cost and viability assessment.

Ported from V2 core/fee_calculator.py with V3 scoring thresholds.
OTR scoring is INVERTED from V2: low OTR (<8%) = danger (17% WR).
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

log = logging.getLogger("scrooge_v3.market.fee_calculator")

# London session baseline spreads (pips) for spike detection
_BASELINE_SPREADS: dict[str, float] = {
    "EUR_USD": 0.00012, "GBP_USD": 0.00016, "USD_JPY": 0.011,
    "AUD_USD": 0.00015, "NZD_USD": 0.00018, "USD_CAD": 0.00018,
    "USD_CHF": 0.00016, "EUR_GBP": 0.00018, "EUR_JPY": 0.016,
    "GBP_JPY": 0.020, "AUD_CAD": 0.00022, "AUD_CHF": 0.00024,
    "CHF_JPY": 0.018, "EUR_CAD": 0.00024, "GBP_AUD": 0.00030,
    "GBP_CAD": 0.00028,
}

# Session spread multipliers
_SESSION_MULTIPLIERS: dict[str, float] = {
    "london": 1.0, "ny": 1.1, "overlap": 1.0,
    "london_close": 1.8, "asian": 1.5, "weekend": 3.0,
}


@dataclass
class CostBreakdown:
    instrument: str
    spread: float
    spread_pips: float
    entry_cost: float
    exit_cost: float
    total_round_trip: float
    half_box: float
    net_profit_potential: float
    otr_ratio: float
    otr_category: str
    viable: bool
    spread_is_spiked: bool


class FeeCalculator:
    """Calculates trading costs and overhead-to-range ratios."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.spike_threshold = config.get("spike_threshold", 4.0)

    def calculate(
        self,
        instrument: str,
        live_spread: float,
        half_box: float,
        units: float = 1.0,
    ) -> CostBreakdown:
        """Calculate complete cost breakdown for a potential trade."""
        entry_cost = live_spread * units
        exit_cost = live_spread * units
        total_rt = entry_cost + exit_cost
        net_profit = half_box * units - total_rt if half_box > 0 else 0.0

        otr = total_rt / (half_box * units) if half_box > 0 else float("inf")

        # V3 OTR categories (INVERTED from V2: low OTR = danger)
        if otr < 0.08:
            otr_category = "too_low"  # Wide unfocused box, 17% WR
        elif otr <= 0.18:
            otr_category = "sweet_spot"  # 63-68% WR
        elif otr < 0.25:
            otr_category = "marginal"
        else:
            otr_category = "skip"

        pip_size = 0.01 if "JPY" in instrument else 0.0001
        spread_pips = live_spread / pip_size

        is_spiked = self.is_spread_spiked(instrument, live_spread)
        viable = otr_category in ("sweet_spot", "marginal") and not is_spiked

        return CostBreakdown(
            instrument=instrument,
            spread=live_spread,
            spread_pips=spread_pips,
            entry_cost=entry_cost,
            exit_cost=exit_cost,
            total_round_trip=total_rt,
            half_box=half_box,
            net_profit_potential=net_profit,
            otr_ratio=otr,
            otr_category=otr_category,
            viable=viable,
            spread_is_spiked=is_spiked,
        )

    def is_spread_spiked(self, instrument: str, live_spread: float) -> bool:
        """Check if spread exceeds spike threshold vs London baseline."""
        baseline = _BASELINE_SPREADS.get(instrument, 0.0002)
        return live_spread > baseline * self.spike_threshold

    def get_session_spread_estimate(
        self, instrument: str, session: str = "london"
    ) -> float:
        """Estimate spread for a given session."""
        baseline = _BASELINE_SPREADS.get(instrument, 0.0002)
        multiplier = _SESSION_MULTIPLIERS.get(session, 1.5)
        return baseline * multiplier
