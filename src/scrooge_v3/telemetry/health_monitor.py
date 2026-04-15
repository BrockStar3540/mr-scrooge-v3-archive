"""
Health Monitor — component health tracking and circuit breakers.

Singleton registry for all ComponentHealth / CircuitBreaker instances.
Each module registers itself on import; dashboard reads from here.
"""

from __future__ import annotations

import logging
import threading
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional

from scrooge_v3.core.types import HealthColor

log = logging.getLogger('scrooge_v3.telemetry.health')


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

@dataclass
class ComponentHealth:
    """
    Health record for one named component.
    Written by each component after every operation.
    Read by dashboard and HealthMonitor.
    """
    name: str
    status: HealthColor = HealthColor.GREEN
    last_success: Optional[datetime] = None
    last_failure: Optional[datetime] = None
    last_failure_reason: str = ''
    consecutive_failures: int = 0
    total_calls: int = 0
    total_failures: int = 0
    latency_ms_last: float = 0.0
    latency_ms_p95: float = 0.0          # rolling p95 of last 100 calls
    notes: str = ''                       # human-readable summary

    def record_success(self, latency_ms: float = 0.0):
        self.last_success = datetime.now(timezone.utc)
        self.consecutive_failures = 0
        self.total_calls += 1
        self.latency_ms_last = latency_ms
        if self.status == HealthColor.RED:
            # Auto-recover after first success
            self.status = HealthColor.YELLOW  # Stays YELLOW until N consecutive successes
        elif self.status == HealthColor.YELLOW and self.consecutive_failures == 0:
            self.status = HealthColor.GREEN

    def record_failure(self, reason: str, latency_ms: float = 0.0):
        self.last_failure = datetime.now(timezone.utc)
        self.last_failure_reason = reason
        self.consecutive_failures += 1
        self.total_calls += 1
        self.total_failures += 1
        self.latency_ms_last = latency_ms
        if self.consecutive_failures >= 3:
            self.status = HealthColor.RED
        elif self.consecutive_failures >= 1:
            self.status = HealthColor.YELLOW

    @property
    def failure_rate(self) -> float:
        if self.total_calls == 0:
            return 0.0
        return self.total_failures / self.total_calls

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'status': self.status.value,
            'last_success': self.last_success.isoformat() if self.last_success else None,
            'last_failure': self.last_failure.isoformat() if self.last_failure else None,
            'last_failure_reason': self.last_failure_reason,
            'consecutive_failures': self.consecutive_failures,
            'total_calls': self.total_calls,
            'total_failures': self.total_failures,
            'failure_rate': round(self.failure_rate, 4),
            'latency_ms_last': self.latency_ms_last,
            'latency_ms_p95': self.latency_ms_p95,
            'notes': self.notes,
        }


@dataclass
class CircuitBreaker:
    """
    Wraps a ComponentHealth. Auto-disables a component after N consecutive
    failures; auto-recovers after a cooldown period.
    """
    component: ComponentHealth
    failure_threshold: int = 5        # trips after this many consecutive failures
    recovery_seconds: int = 300       # wait this long before trying again
    _tripped: bool = field(default=False, init=False)
    _tripped_at: Optional[datetime] = field(default=None, init=False)

    @property
    def is_open(self) -> bool:
        """True means circuit is open (disabled) -- calls should be skipped."""
        if not self._tripped:
            return False
        if self._tripped_at is None:
            return True
        elapsed = (datetime.now(timezone.utc) - self._tripped_at).total_seconds()
        if elapsed >= self.recovery_seconds:
            # Allow one probe attempt
            self._tripped = False
            return False
        return True

    def record_success(self, latency_ms: float = 0.0):
        self._tripped = False
        self.component.record_success(latency_ms)

    def record_failure(self, reason: str, latency_ms: float = 0.0):
        self.component.record_failure(reason, latency_ms)
        if self.component.consecutive_failures >= self.failure_threshold:
            self._tripped = True
            self._tripped_at = datetime.now(timezone.utc)

    @property
    def name(self) -> str:
        return self.component.name

    @property
    def status(self) -> HealthColor:
        if self.is_open:
            return HealthColor.RED
        return self.component.status


@dataclass
class HealthReport:
    """Snapshot of all components for the dashboard."""
    timestamp: datetime
    components: List[ComponentHealth] = field(default_factory=list)

    @property
    def overall_status(self) -> HealthColor:
        if any(c.status == HealthColor.RED for c in self.components):
            return HealthColor.RED
        if any(c.status == HealthColor.YELLOW for c in self.components):
            return HealthColor.YELLOW
        return HealthColor.GREEN

    def to_dict(self) -> dict:
        return {
            'timestamp': self.timestamp.isoformat(),
            'overall': self.overall_status.value,
            'components': [c.to_dict() for c in self.components],
        }


# ---------------------------------------------------------------------------
# Monitor (singleton)
# ---------------------------------------------------------------------------

class HealthMonitor:
    """
    Singleton. Thread-safe.
    Usage:
        monitor = HealthMonitor.get()
        monitor.register('oanda_client')
        monitor.record_success('oanda_client', latency_ms=120)
        report = monitor.report()
    """

    _instance: Optional[HealthMonitor] = None
    _lock = threading.Lock()

    def __init__(self):
        self._components: Dict[str, ComponentHealth] = {}
        self._breakers:   Dict[str, CircuitBreaker]  = {}
        self._rlock = threading.RLock()

    @classmethod
    def get(cls) -> HealthMonitor:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    # -- Registration ---------------------------------------------------------

    def register(self, name: str,
                 failure_threshold: int = 5,
                 recovery_seconds: int = 300) -> CircuitBreaker:
        """Register a named component. Idempotent -- safe to call on every import."""
        with self._rlock:
            if name not in self._components:
                comp = ComponentHealth(name=name)
                breaker = CircuitBreaker(
                    component=comp,
                    failure_threshold=failure_threshold,
                    recovery_seconds=recovery_seconds,
                )
                self._components[name] = comp
                self._breakers[name] = breaker
                log.debug(f'HealthMonitor: registered component "{name}"')
            return self._breakers[name]

    def get_breaker(self, name: str) -> Optional[CircuitBreaker]:
        return self._breakers.get(name)

    def get_component(self, name: str) -> Optional[ComponentHealth]:
        return self._components.get(name)

    # -- Recording ------------------------------------------------------------

    def record_success(self, name: str, latency_ms: float = 0.0):
        with self._rlock:
            b = self._breakers.get(name)
            if b:
                b.record_success(latency_ms)

    def record_failure(self, name: str, reason: str, latency_ms: float = 0.0):
        with self._rlock:
            b = self._breakers.get(name)
            if b:
                b.record_failure(reason, latency_ms)
                if b.is_open:
                    log.error(f'CIRCUIT OPEN: {name} -- {reason}')
                else:
                    log.warning(f'FAILURE: {name} -- {reason}')

    def is_open(self, name: str) -> bool:
        """Returns True if the circuit breaker is tripped (calls should be skipped)."""
        b = self._breakers.get(name)
        return b.is_open if b else False

    # -- Reporting ------------------------------------------------------------

    def report(self) -> HealthReport:
        with self._rlock:
            return HealthReport(
                timestamp=datetime.now(timezone.utc),
                components=list(self._components.values()),
            )

    def status_line(self) -> str:
        """One-line summary for logs. e.g. 'green(8) yellow(1) red(0)'"""
        with self._rlock:
            counts = {s: 0 for s in HealthColor}
            for c in self._components.values():
                counts[c.status] += 1
            return ' '.join(f'{s.value}({counts[s]})' for s in HealthColor)
