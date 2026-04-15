"""Dashboard widgets — one per module category."""

from scrooge_v3.dashboard.widgets.health_widget import HealthWidget
from scrooge_v3.dashboard.widgets.system_widget import SystemWidget
from scrooge_v3.dashboard.widgets.scoring_widget import ScoringWidget
from scrooge_v3.dashboard.widgets.gate_widget import GateWidget
from scrooge_v3.dashboard.widgets.execution_widget import ExecutionWidget

__all__ = [
    "HealthWidget", "SystemWidget", "ScoringWidget",
    "GateWidget", "ExecutionWidget",
]
