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
from .regime_compat import RegimeCompatGate
from .regime_strategy_router import RegimeStrategyRouterGate
from .box_v3_shadow import BoxV3ShadowGate
from .entry_filter_gate import EntryFilterGate
from .entry_filter_shadow_gate import EntryFilterShadowGate
from .sub_regime_filter_gate import SubRegimeFilterGate
from .matrix_router_gate import MatrixRouterGate
from .session_filter_gate import SessionFilterGate
from .pair_filter_gate import PairFilterGate
from .matrix_combo_filter_gate import MatrixComboFilterGate
from .matrix_signature_filter_gate import MatrixSignatureFilterGate

# Phase 4 Signal Discipline
from .cooldown import CooldownGate
from .expiry_backoff import ExpiryBackoffGate
from .daily_circuit import DailyCircuitGate
from .news_blackout import NewsBlackoutGate  # Brock 2026-06-10 CPI-day
from .pip_eater_gate import PipEaterGate  # Brock 2026-05-31

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
    "RegimeCompatGate",
    "RegimeStrategyRouterGate",
    "BoxV3ShadowGate",
    "EntryFilterGate",
    "EntryFilterShadowGate",
    "SubRegimeFilterGate",
    "MatrixRouterGate",
    "SessionFilterGate",
    "PairFilterGate",
    "MatrixComboFilterGate",
    "MatrixSignatureFilterGate",
    # Phase 4
    "CooldownGate",
    "ExpiryBackoffGate",
    "DailyCircuitGate",
    "NewsBlackoutGate",
]
