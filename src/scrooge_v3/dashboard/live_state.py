"""Live state — thread-safe shared state between runtime and dashboard.

The runtime writes cycle data here every scan cycle.
The dashboard reads it to render the UI.
"""

from __future__ import annotations

import threading
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class PairSignal:
    """Per-pair scan result for dashboard display."""
    symbol: str
    signal_type: str = ""  # MEAN_REV, TREND_FULL, etc.
    bb_state: str = ""
    regime_state: str = ""
    regime_score: float = 0.0
    zone_tier: int = 0
    zone_name: str = ""
    atr_consumed: float = 0.0
    otr_ratio: float = 0.0
    spread: float = 0.0
    rsi: float = 0.0
    z_score: float = 0.0
    bb_position: float = 0.0
    box_age: float = 0.0
    # Gate results
    gates: dict[str, dict[str, Any]] = field(default_factory=dict)  # gate_name -> {passed, reason}
    # V3 scorer
    v3_score: int = 0
    v3_tier: str = ""
    v3_blocks: list[str] = field(default_factory=list)
    v3_breakdown: dict[str, int] = field(default_factory=dict)
    # Verdict
    verdict: str = "NO_TRADE"  # NO_TRADE, CANDIDATE, APPROVED, REJECTED, BLOCKED
    rejection_reason: str = ""
    tradeable: bool = False


@dataclass
class LiveState:
    """Thread-safe state shared between runtime and dashboard."""

    # Lock for thread safety
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    # System
    cycle_count: int = 0
    uptime_start: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    last_update: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    dry_run: bool = True

    # Account (from broker)
    equity: float = 0.0
    balance: float = 0.0
    daily_pnl: float = 0.0
    unrealized_pl: float = 0.0
    margin_used_pct: float = 0.0
    position_count: int = 0

    # Scan summary
    pairs_scanned: int = 0
    pairs_viable: int = 0
    signals_evaluated: int = 0

    # Sessions
    active_sessions: list[str] = field(default_factory=list)

    # Market state
    market_state: str = ""
    regime_summary: dict[str, int] = field(default_factory=dict)  # {blocked: N, restricted: N, clean: N}
    regime_avg_score: float = 0.0
    regime_dominant: str = ""

    # Blockers summary
    blockers: dict[str, int] = field(default_factory=dict)  # {reason: count}

    # Per-pair scan reports from pipeline (the main display)
    scan_reports: list[dict[str, Any]] = field(default_factory=list)

    # Recent trades
    recent_entries: list[dict[str, Any]] = field(default_factory=list)
    recent_closes: list[dict[str, Any]] = field(default_factory=list)

    # Decision summary
    valid_count: int = 0
    rejected_count: int = 0
    top_rejections: dict[str, int] = field(default_factory=dict)
    setup_types: dict[str, int] = field(default_factory=dict)

    # Daily loss
    daily_loss_exceeded: bool = False
    spread_skips: int = 0
    pending_limit_orders: int = 0
    last_spread_skip: str = ""

    # Execution audit (populated by runtime from ExecutionAudit)
    execution_summary: dict[str, Any] = field(default_factory=dict)
    execution_events: list[dict[str, Any]] = field(default_factory=list)

    def update(self, **kwargs: Any) -> None:
        """Thread-safe update of multiple fields."""
        with self._lock:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            self.last_update = datetime.now(timezone.utc)

    def snapshot(self) -> dict[str, Any]:
        """Thread-safe snapshot of all state for API response."""
        with self._lock:
            return {
                "system": {
                    "cycle_count": self.cycle_count,
                    "uptime_hours": round((datetime.now(timezone.utc) - self.uptime_start).total_seconds() / 3600, 2),
                    "last_update": self.last_update.strftime("%I:%M:%S %p"),
                    "dry_run": self.dry_run,
                },
                "account": {
                    "equity": round(self.equity, 2),
                    "balance": round(self.balance, 2),
                    "daily_pnl": round(self.daily_pnl, 2),
                    "unrealized_pl": round(self.unrealized_pl, 2),
                    "margin_used_pct": round(self.margin_used_pct, 1),
                    "position_count": self.position_count,
                    "daily_loss_exceeded": self.daily_loss_exceeded,
                    "spread_skips": self.spread_skips,
                    "pending_limit_orders": self.pending_limit_orders,
                    "last_spread_skip": self.last_spread_skip,
                },
                "scan": {
                    "pairs_scanned": self.pairs_scanned,
                    "pairs_viable": self.pairs_viable,
                    "signals_evaluated": self.signals_evaluated,
                },
                "sessions": self.active_sessions,
                "market": {
                    "state": self.market_state,
                    "regime": self.regime_summary,
                    "regime_avg_score": round(self.regime_avg_score, 1),
                    "regime_dominant": self.regime_dominant,
                },
                "blockers": self.blockers,
                "signals": self._clean_reports(self.scan_reports),
                "decision": {
                    "valid": self.valid_count,
                    "rejected": self.rejected_count,
                    "top_rejections": self.top_rejections,
                    "setup_types": self.setup_types,
                },
                "recent_entries": self.recent_entries[-10:],
                "recent_closes": self.recent_closes[-10:],
                "execution": {
                    "summary": self.execution_summary,
                    "events": self.execution_events[-50:],
                },
            }

    @staticmethod
    def _clean_reports(reports: list[dict]) -> list[dict]:
        """Serialize scan reports for JSON — strip non-serializable objects."""
        clean = []
        for r in reports:
            cr: dict[str, Any] = {
                "symbol": r.get("symbol", ""),
                "spread": r.get("spread", 0),
                "verdict": r.get("verdict", ""),
                "features": {},
                "classifications": r.get("classifications", {}),
                "strategy_allowed": r.get("strategy_allowed", []),
                "gates": r.get("gates", {}),
                "scorer": r.get("scorer", {}),
            }
            # Clean features — extract only serializable values
            for fname, fvals in r.get("features", {}).items():
                if isinstance(fvals, dict):
                    safe = {}
                    for k, v in fvals.items():
                        if isinstance(v, (str, int, float, bool, type(None))):
                            safe[k] = v
                        elif k == "zone_map":
                            # Extract key zone fields
                            if hasattr(v, "session_range") and v.session_range:
                                sr = v.session_range
                                safe["PDH"] = sr.PDH
                                safe["PDL"] = sr.PDL
                                safe["center"] = sr.center if hasattr(sr, "center") else (sr.PDH + sr.PDL) / 2
                                safe["box_range"] = sr.PDH - sr.PDL
                    cr["features"][fname] = safe
            clean.append(cr)
        return clean

    @staticmethod
    def _signal_dict(s: PairSignal) -> dict[str, Any]:
        return {
            "symbol": s.symbol,
            "signal_type": s.signal_type,
            "bb_state": s.bb_state,
            "regime_state": s.regime_state,
            "zone_tier": s.zone_tier,
            "atr_consumed": round(s.atr_consumed * 100, 1),
            "otr_ratio": round(s.otr_ratio * 100, 1),
            "spread": s.spread,
            "rsi": round(s.rsi, 1),
            "z_score": round(s.z_score, 2),
            "box_age": round(s.box_age, 1),
            "gates": s.gates,
            "v3_score": s.v3_score,
            "v3_tier": s.v3_tier,
            "v3_blocks": s.v3_blocks,
            "verdict": s.verdict,
            "rejection_reason": s.rejection_reason,
            "tradeable": s.tradeable,
        }
