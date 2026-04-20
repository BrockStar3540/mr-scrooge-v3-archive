"""Debounce gate - prevents re-entry at the same zone within cooldown.

Two-part check (Phase 4):
  1. Same-zone recent ENTRY: read from ``ctx.state['zone_last_entry']``
     - blocks if an entry at this zone happened within
     ``debounce_minutes``.
  2. Same-zone recent LOSS (blacklist): read from
     ``ctx.state['zone_blacklist']`` - blocks if the zone had a
     stop-loss within ``zone_blacklist_hours``. Zone is bucketed by
     entry price (configurable pip width) rather than exact stop price,
     so slightly-different re-entries at the same level are caught.
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


class DebounceGate(BaseGate):
    """Enforces a minimum cooldown between entries at the same zone.

    Also enforces a longer blacklist window after a stop-loss at the
    zone (Phase 4 extension).
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
        self.zone_blacklist_hours: float = float(
            self.config.get("zone_blacklist_hours", 4)
        )
        self.zone_bucket_pips: int = int(self.config.get("zone_bucket_pips", 20))

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        zone_price = candidate.stop_price
        direction = candidate.direction.value
        symbol = candidate.symbol
        zone_key = f"{symbol}_{zone_price}_{direction}"

        # Use latest runtime config values if present
        risk_cfg = ctx.state.get("risk_config", {})
        bucket_pips = int(risk_cfg.get("zone_bucket_pips", self.zone_bucket_pips))
        blacklist_hours = float(
            risk_cfg.get("zone_blacklist_hours", self.zone_blacklist_hours)
        )

        now = datetime.now(timezone.utc)

        # --- 1. Zone blacklist (recently-closed loss at this zone) ---
        blacklist: dict[str, str] = ctx.state.get("zone_blacklist", {})
        blk_key = _zone_key(symbol, direction, candidate.entry_price, bucket_pips)
        blk_ts = _parse(blacklist.get(blk_key))
        if blk_ts:
            elapsed_hours = (now - blk_ts).total_seconds() / 3600.0
            if elapsed_hours < blacklist_hours:
                remaining_h = blacklist_hours - elapsed_hours
                reason = (
                    f"Zone blacklisted: loss {elapsed_hours:.1f}h ago "
                    f"({remaining_h:.1f}h remaining)"
                )
                return GateResult(
                    gate_name=self.name,
                    passed=False,
                    reason=reason,
                    metrics={
                        "zone_key": zone_key,
                        "blacklist_key": blk_key,
                        "elapsed_hours": elapsed_hours,
                        "blacklist_hours": blacklist_hours,
                    },
                )

        # --- 2. Recent-entry debounce (original behavior) ---
        zone_timestamps: dict[str, str] = ctx.state.get("zone_last_entry", {})
        last_entry = _parse(zone_timestamps.get(zone_key))
        if last_entry is None:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="No prior entry at this zone",
                metrics={"score": 1.0, "zone_key": zone_key},
            )

        elapsed_minutes = (now - last_entry).total_seconds() / 60.0
        if elapsed_minutes < self.debounce_minutes:
            remaining = self.debounce_minutes - elapsed_minutes
            reason = (
                f"Debounce active: {elapsed_minutes:.0f}min since last"
                f" entry at zone ({remaining:.0f}min remaining)"
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
