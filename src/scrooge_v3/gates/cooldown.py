"""Cooldown gate - blocks new entries on (symbol, direction) recently stopped.

Part of Phase 4 Signal Discipline. Reads cooldown registry from
``ctx.state['cooldowns']`` populated by the CooldownTracker in state
recovery. A cooldown expires after ``cooldown_after_stop_minutes``.
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


class CooldownGate(BaseGate):
    """Hard-block new entries during post-stopout cooldown."""

    name = "cooldown"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.cooldown_minutes: int = int(
            self.config.get("cooldown_after_stop_minutes", 60)
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        symbol = candidate.symbol
        direction = candidate.direction.value
        key = f"{symbol}:{direction}"

        cooldowns: dict[str, dict] = ctx.state.get("cooldowns", {})
        cfg_minutes = int(
            ctx.state.get("risk_config", {}).get(
                "cooldown_after_stop_minutes", self.cooldown_minutes,
            )
        )
        entry = cooldowns.get(key)
        if not entry:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="No active cooldown",
                metrics={"score": 1.0, "key": key},
            )

        stopped_at = _parse(entry.get("stopped_at"))
        if not stopped_at:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="Invalid cooldown timestamp - allowing",
                metrics={"score": 1.0, "key": key},
            )

        now = datetime.now(timezone.utc)
        elapsed_min = (now - stopped_at).total_seconds() / 60.0
        remaining = cfg_minutes - elapsed_min
        if remaining > 0:
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=(
                    f"Cooldown active: stopped {elapsed_min:.0f}m ago, "
                    f"{remaining:.0f}m remaining"
                ),
                metrics={
                    "elapsed_min": elapsed_min,
                    "cooldown_min": cfg_minutes,
                    "remaining_min": remaining,
                    "key": key,
                },
            )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=f"Cooldown cleared ({elapsed_min:.0f}m since stop)",
            metrics={"score": 1.0, "elapsed_min": elapsed_min, "key": key},
        )
