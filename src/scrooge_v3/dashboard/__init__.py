"""Dashboard layer — real-time trading dashboard."""

from scrooge_v3.dashboard.app import create_app, run_dashboard
from scrooge_v3.dashboard.live_state import LiveState, PairSignal

__all__ = ["create_app", "run_dashboard", "LiveState", "PairSignal"]
