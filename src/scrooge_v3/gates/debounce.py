"""Debounce gate — prevents re-entry at the same zone within cooldown.

Reads zone price from candidate.stop_price (zone boundary).
V3 pattern: reads from ctx.state, not ctx.metadata.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class DebounceGate(BaseGate):
    """Enforces a minimum cooldown between entries at the same zone.

    Prevents rapid re-entry after a stop-out at the same level
    (replaces V2 zone_cache logic).
    """

    name = "debounce"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.debounce_minutes: int = self.config.get(
            "debounce_minutes", 20
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        # Zone identified by stop price (the zone boundary this trade targets)
        zone_price = candidate.stop_price
        direction = candidate.direction.value
        symbol = candidate.symbol

        zone_key = f"{symbol}_{zone_price}_{direction}"

        # Read last entry timestamps from state
        zone_timestamps: dict[str, str] = ctx.state.get(
            "zone_last_entry", {}
        )
        last_entry_str = zone_timestamps.get(zone_key)

        if last_entry_str is None:
            self._log.debug(
                "[GATE:%s] PASSED symbol=%s reason=no prior entry at zone",
                self.name, symbol,
            )
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="No prior entry at this zone",
                metrics={"score": 1.0, "zone_key": zone_key},
            )

        try:
            last_entry = datetime.fromisoformat(last_entry_str)
        except (ValueError, TypeError):
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="Invalid timestamp in state -- allowing entry",
                metrics={"score": 1.0, "zone_key": zone_key},
            )

        now = datetime.now(timezone.utc)
        if last_entry.tzinfo is None:
            last_entry = last_entry.replace(tzinfo=timezone.utc)

        elapsed_minutes = (now - last_entry).total_seconds() / 60.0

        if elapsed_minutes < self.debounce_minutes:
            remaining = self.debounce_minutes - elapsed_minutes
            reason = (
                f"Debounce active: {elapsed_minutes:.0f}min since last"
                f" entry at zone ({remaining:.0f}min remaining)"
            )
            self._log.debug(
                "[GATE:%s] FAILED symbol=%s reason=%s",
                self.name, symbol, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={
                    "elapsed_minutes": elapsed_minutes,
                    "debounce_minutes": self.debounce_minutes,
                    "zone_key": zone_key,
                },
            )

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=%.0fmin since last entry (>%d)",
            self.name, symbol, elapsed_minutes, self.debounce_minutes,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=(
                f"Debounce cleared: {elapsed_minutes:.0f}min"
                f" since last entry"
            ),
            metrics={
                "score": 1.0,
                "elapsed_minutes": elapsed_minutes,
                "debounce_minutes": self.debounce_minutes,
                "zone_key": zone_key,
            },
        )
