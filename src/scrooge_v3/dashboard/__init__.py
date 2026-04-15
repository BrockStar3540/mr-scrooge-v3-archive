"""Dashboard layer — modular widget-based trading dashboard."""

from scrooge_v3.dashboard.app import create_app, run_dashboard
from scrooge_v3.dashboard.widget_registry import WidgetRegistry

__all__ = ["create_app", "run_dashboard", "WidgetRegistry"]
