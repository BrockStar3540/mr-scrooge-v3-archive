"""Expiry-backoff gate - blocks re-submitting limits that keep expiring.

Part of Phase 4 Signal Discipline. Reads limit-expiry state from
``ctx.state['limit_expiry']``. If the (symbol, direction, zone) key has
hit ``max_consecutive_expiries`` and a ``backoff_until`` is in the
future, the gate blocks.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


def _parse(ts: str | None):
    if not ts:
        return None
    try:
        dt = datetime.fromisoformat(ts)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError):
        return None


def _zone_key(symbol: str, direction: str, price: float, pips: int = 20) -> str:
    pip_size = 0.01 if "_JPY" in symbol else 0.0001
    bucket_width = pips * pip_size if pips > 0 else 0.0020
    bucket = round(price / bucket_width) * bucket_width
    return f"{symbol}:{direction}:{bucket:.5f}"


class ExpiryBackoffGate(BaseGate):
    """Hard-block re-submission after repeated limit expiries at a zone."""

    name = "expiry_backoff"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.zone_bucket_pips: int = int(self.config.get("zone_bucket_pips", 20))

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        risk_cfg = ctx.state.get("risk_config", {})
        bucket_pips = int(risk_cfg.get("zone_bucket_pips", self.zone_bucket_pips))

        key = _zone_key(
            candidate.symbol, candidate.direction.value,
            candidate.entry_price, bucket_pips,
        )
        entry = ctx.state.get("limit_expiry", {}).get(key)
        if not entry:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="No prior expiries at this zone",
                metrics={"score": 1.0, "key": key},
            )

        until = _parse(entry.get("backoff_until"))
        now = datetime.now(timezone.utc)
        if until and now < until:
            remaining = (until - now).total_seconds() / 60.0
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=(
                    f"Expiry backoff active: {entry.get('count', 0)} "
                    f"consecutive expiries, {remaining:.0f}m remaining"
                ),
                metrics={
                    "count": entry.get("count", 0),
                    "remaining_min": remaining,
                    "key": key,
                },
            )

        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=f"Expiry backoff cleared (count={entry.get('count', 0)})",
            metrics={"score": 1.0, "key": key},
        )
