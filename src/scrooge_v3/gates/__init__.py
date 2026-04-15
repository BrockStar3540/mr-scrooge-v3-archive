"""Gates layer -- ordered filters in the trade evaluation pipeline."""

from .base import BaseGate, GatePipelineResult
from .pipeline import GatePipeline

# Ported V2 gates
from .zone_proximity import ZoneProximityGate
from .trend_filter import TrendFilterGate
from .atr_budget import ATRBudgetGate
from .directional_pressure import DirectionalPressureGate
from .entry_confirmation import EntryConfirmationGate
from .overhead_ratio import OverheadRatioGate

# New gates extracted from V2 coordinator
from .spread import SpreadGate
from .risk_reward import RiskRewardGate
from .zone_entry_cap import ZoneEntryCapGate
from .debounce import DebounceGate
from .regime_floor import RegimeFloorGate
from .exhaustion_filter import ExhaustionFilterGate

__all__ = [
    # Base
    "BaseGate",
    "GatePipelineResult",
    "GatePipeline",
    # Ported gates
    "ZoneProximityGate",
    "TrendFilterGate",
    "ATRBudgetGate",
    "DirectionalPressureGate",
    "EntryConfirmationGate",
    "OverheadRatioGate",
    # New gates
    "SpreadGate",
    "RiskRewardGate",
    "ZoneEntryCapGate",
    "DebounceGate",
    "RegimeFloorGate",
    "ExhaustionFilterGate",
]
