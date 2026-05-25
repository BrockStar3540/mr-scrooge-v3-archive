"""Replay-lab type definitions."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

DirectionMode = Literal["native", "reversed"]
EntryMode = Literal["signal", "pullback_2", "pullback_4", "old_stop_zone"]
RoutingMode = Literal["bypass", "exact_strategy_only", "exact_plus_family", "exact_plus_loose_override"]
ManagementMode = Literal["none", "tp1_only", "tp1_be", "tp1_be_ratchet"]
SpreadMode = Literal["idealized", "realistic", "wide"]


@dataclass
class ReplaySpec:
    """Single replay configuration."""
    symbol: str
    strategy_name: str | None = None
    family_name: str | None = None
    regime53: str | None = None
    session_bucket: str | None = None
    direction: str | None = None
    routing_table_path: str | None = None
    date_from: str | None = None   # ISO 8601
    date_to: str | None = None
    direction_mode: DirectionMode = "native"
    entry_mode: EntryMode = "signal"
    routing_mode: RoutingMode = "exact_strategy_only"
    management_mode: ManagementMode = "tp1_be"
    spread_mode: SpreadMode = "realistic"
    slippage_pips: float = 0.0
    sl_pips: float = 10.0
    tp_pips: float = 12.0
    cash: float = 50_000.0
    margin: float = 0.02   # 50× leverage
    label: str = ""

    def key(self) -> str:
        parts = [self.symbol, self.strategy_name or "any",
                 self.direction_mode, self.entry_mode,
                 self.routing_mode, self.management_mode]
        return "/".join(parts)
