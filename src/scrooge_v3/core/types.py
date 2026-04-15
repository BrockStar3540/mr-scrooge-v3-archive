"""Core type definitions used across all modules."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# Module modes
# ---------------------------------------------------------------------------

class ModuleMode(str, Enum):
    DISABLED = "disabled"
    OBSERVE = "observe"
    ACTIVE = "active"


class GateMode(str, Enum):
    HARD = "hard"
    SOFT = "soft"
    OBSERVE = "observe"


class AdvisorMode(str, Enum):
    DISABLED = "disabled"
    OBSERVE = "observe"
    ADVISORY = "advisory"
    WEIGHTED = "weighted"
    HARD_BLOCK = "hard_block"


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------

class HealthColor(str, Enum):
    GREEN = "green"      # healthy
    YELLOW = "yellow"    # degraded
    RED = "red"          # failed
    GRAY = "gray"        # disabled
    BLUE = "blue"        # observe-only


@dataclass
class HealthStatus:
    name: str
    color: HealthColor
    reason: str = ""
    last_run: datetime | None = None
    last_success: datetime | None = None
    avg_latency_ms: float = 0.0
    error_count: int = 0
    mode: str = ""


# ---------------------------------------------------------------------------
# Market data
# ---------------------------------------------------------------------------

@dataclass
class MarketSnapshot:
    symbol: str
    bid: float
    ask: float
    mid: float
    spread: float
    timestamp: datetime
    candles: dict[str, Any] = field(default_factory=dict)  # tf -> list[candle]


# ---------------------------------------------------------------------------
# Feature results
# ---------------------------------------------------------------------------

@dataclass
class FeatureResult:
    name: str
    values: dict[str, Any] = field(default_factory=dict)
    computed_at: datetime | None = None


# ---------------------------------------------------------------------------
# Classification results
# ---------------------------------------------------------------------------

@dataclass
class ClassificationResult:
    name: str
    label: str
    confidence: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Symbol context — the single object passed through the pipeline
# ---------------------------------------------------------------------------

@dataclass
class SymbolContext:
    symbol: str
    snapshot: MarketSnapshot
    features: dict[str, FeatureResult] = field(default_factory=dict)
    classifications: dict[str, ClassificationResult] = field(default_factory=dict)
    state: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Trade candidate
# ---------------------------------------------------------------------------

class TradeDirection(str, Enum):
    LONG = "long"
    SHORT = "short"


@dataclass
class TradeCandidate:
    symbol: str
    direction: TradeDirection
    strategy: str
    entry_price: float
    stop_price: float
    take_profit: float | None = None
    size: float = 0.0
    risk_reward: float = 0.0
    score: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: datetime | None = None


# ---------------------------------------------------------------------------
# Gate result
# ---------------------------------------------------------------------------

@dataclass
class GateResult:
    gate_name: str
    passed: bool
    mode: GateMode = GateMode.HARD
    reason: str = ""
    metrics: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Order / execution types
# ---------------------------------------------------------------------------

class OrderState(str, Enum):
    CREATED = "created"
    ACKNOWLEDGED = "acknowledged"
    TRIGGERED = "triggered"
    FILLED = "filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"


@dataclass
class OrderPlan:
    symbol: str
    direction: TradeDirection
    entry_price: float
    stop_price: float
    take_profit: float | None = None
    size: float = 0.0
    order_type: str = "STOP"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class StopPlan:
    position_id: str
    new_stop: float
    reason: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Position state
# ---------------------------------------------------------------------------

@dataclass
class PositionState:
    position_id: str
    symbol: str
    direction: TradeDirection
    entry_price: float
    current_stop: float
    size: float
    unrealized_pnl: float = 0.0
    opened_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Advisor result
# ---------------------------------------------------------------------------

@dataclass
class AdvisorResult:
    advisor_name: str
    recommendation: str = ""
    confidence: float = 0.0
    adjustments: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
