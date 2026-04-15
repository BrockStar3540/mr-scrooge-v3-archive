"""Telemetry layer -- health monitoring, trade quality tracking, and experiments."""

from scrooge_v3.telemetry.health_monitor import (
    ComponentHealth,
    CircuitBreaker,
    HealthMonitor,
    HealthReport,
)
from scrooge_v3.telemetry.quality_models import (
    LiveExcursion,
    QualityPressure,
    TradeQualityRecord,
)
from scrooge_v3.telemetry.quality_tracker import TradeQualityTracker
from scrooge_v3.telemetry.entry_context import EntryContextLogger
from scrooge_v3.telemetry.quality_indicators import (
    compute_rsi,
    compute_ema,
    compute_macd,
    compute_bollinger,
    compute_z_score,
    compute_realized_vol,
    compute_trend_1h,
    compute_adr_consumed,
    compute_touch_count,
    compute_volume_ratio,
    compute_entry_distance_pips,
    ema_aligned,
)
from scrooge_v3.telemetry.experiments import (
    Experiment,
    ExperimentResults,
    ExperimentTracker,
    TradeOutcome,
    VariantStats,
)

__all__ = [
    # Health
    'ComponentHealth',
    'CircuitBreaker',
    'HealthMonitor',
    'HealthReport',
    # Quality models
    'LiveExcursion',
    'QualityPressure',
    'TradeQualityRecord',
    # Quality tracker
    'TradeQualityTracker',
    # Entry context
    'EntryContextLogger',
    # Indicators
    'compute_rsi',
    'compute_ema',
    'compute_macd',
    'compute_bollinger',
    'compute_z_score',
    'compute_realized_vol',
    'compute_trend_1h',
    'compute_adr_consumed',
    'compute_touch_count',
    'compute_volume_ratio',
    'compute_entry_distance_pips',
    'ema_aligned',
    # Experiments
    'Experiment',
    'ExperimentResults',
    'ExperimentTracker',
    'TradeOutcome',
    'VariantStats',
]
