"""Zone entry cap gate -- max entries per zone+direction per day."""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class ZoneEntryCapGate(BaseGate):
    """Limits the number of entries at the same zone+direction per day.

    Prevents over-trading at a single level that keeps getting tested
    without producing clean moves (formerly the "D3" rule).
    """

    name = "zone_entry_cap"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.max_entries_per_zone: int = self.config.get(
            "max_entries_per_zone", 3
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        zone_price = ctx.metadata.get("zone_price")
        direction = candidate.direction.value
        symbol = candidate.symbol

        # Build a zone key from price (rounded) + direction
        zone_key = f"{symbol}_{zone_price}_{direction}"

        # Read entry count from state controller
        zone_entries: dict[str, int] = ctx.state.get(
            "zone_entries_today", {}
        )
        current_count = zone_entries.get(zone_key, 0)

        if current_count >= self.max_entries_per_zone:
            reason = (
                f"Zone entry cap reached: {current_count}"
                f"/{self.max_entries_per_zone} at {zone_price}"
                f" {direction}"
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
                    "current_count": current_count,
                    "max_allowed": self.max_entries_per_zone,
                    "zone_key": zone_key,
                },
            )

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=%d/%d entries at zone",
            self.name, symbol, current_count, self.max_entries_per_zone,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=(
                f"Zone entries {current_count}"
                f"/{self.max_entries_per_zone}"
            ),
            metrics={
                "score": 1.0,
                "current_count": current_count,
                "max_allowed": self.max_entries_per_zone,
                "zone_key": zone_key,
            },
        )
