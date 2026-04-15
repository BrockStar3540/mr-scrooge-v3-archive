"""Strategy models — directional pressure, entry confirmation, and strategy evaluation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from scrooge_v3.features.models import LiquidityZone


@dataclass
class DirectionalPressureResult:
    """Result of directional pressure detection (was: SuckerMoveResult)."""
    detected: bool
    direction: str
    candle_count: int
    atr_consumed_pct: float
    atr_threshold_met: bool
    atr_strength: str           # 'strong', 'valid', 'weak'
    move_size: float
    terminating_at_zone: bool
    zone_hit: Optional[LiquidityZone]
    rejection_reason: str


@dataclass
class EntryConfirmationResult:
    """Result of entry confirmation detection (was: PitchforkResult)."""
    detected: bool
    signal_type: str            # 'entry_confirmation', 'wick_rejection', 'engulfing_reversal', 'none'
    direction: str
    directional_candles: int
    trigger_price: float
    stop_price: float
    reversal_candle_idx: int
    confidence: str             # 'HIGH', 'MODERATE', 'LOW'
    timeframe_used: str         # '5M', '1H'
    details: str


@dataclass
class StrategyEvaluation:
    """Complete evaluation for one instrument at one moment (was: SignalResult).

    Does not duplicate TradeCandidate from core/types.py — instead wraps
    gate results and candidate generation metadata.  A passing evaluation
    produces a TradeCandidate via to_candidate().
    """
    symbol: str
    timestamp: str
    action: str                 # 'ENTER_LONG', 'ENTER_SHORT', 'WAIT', 'NO_TRADE'

    # Gate results
    zone_gate: bool
    zone_tier: int
    zone_details: str

    directional_pressure_gate: bool
    directional_pressure: Optional[DirectionalPressureResult]

    atr_gate: bool
    atr_consumed_pct: float
    atr_strength: str

    entry_confirmation_gate: bool
    entry_confirmation: Optional[EntryConfirmationResult]

    otr_gate: bool
    otr_ratio: float
    otr_category: str

    # Entry details
    entry_price: float
    stop_price: float
    tp1_price: float
    tp2_price: float
    risk_points: float
    reward_points: float
    risk_reward_ratio: float

    rejection_reasons: list[str] = field(default_factory=list)
    all_gates_passed: bool = False
    wait_for: str = ''
    score: int = 0
    rr_tp1: float = 0.0
    is_counter_trend: bool = False
    score_detail: dict | None = None
    validity_detail: dict | None = None
