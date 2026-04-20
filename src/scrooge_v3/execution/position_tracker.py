"""Position tracker — maintains per-trade state across cycles.

Bridges OANDA TradeInfo (what the broker knows) with the management
pipeline (what the bot needs to manage: TP1 level, partial status,
entry metadata, SL ownership).

Persists to JSON so state survives restarts.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.execution.position_tracker")


@dataclass
class TrackedPosition:
    """Everything the management pipeline needs about an open trade."""
    trade_id: str
    symbol: str
    direction: str  # "long" or "short"
    units: float
    entry_price: float
    current_stop: float
    current_tp: float = 0.0
    tp1_price: float = 0.0  # Center of box (half profit target)
    tp2_price: float = 0.0  # Opposite boundary
    tp1_taken: bool = False
    break_even_achieved: bool = False
    opened_at: str = ""
    strategy: str = ""
    v3_score: int = 0
    harvest_order_id: str = ""
    # Snapshotted at entry — never mutated. Used for:
    #  - profit_r computation (initial risk distance, not dynamic SL)
    #  - double-harvest guard (compare vs broker live_units)
    original_units: float = 0.0
    initial_risk_distance: float = 0.0
    # MFE tracking (Phase 3 / Bug I) — most-favorable price reached since
    # entry. Used by ratchet to anchor locks on peak, not current, so
    # retracement can't unlock already-protected gains.
    peak_price: float = 0.0
    peak_profit_distance: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


class PositionTracker:
    """Tracks all open positions with metadata the broker doesn't store."""

    def __init__(self, persist_path: Path | None = None):
        self._positions: dict[str, TrackedPosition] = {}
        self._persist_path = persist_path
        # Pending entries (limit orders waiting to fill) — per-instance to
        # avoid cross-instance pollution (was class-scoped before 2026-04-19).
        self._pending_entries: dict[str, str] = {}
        self._pending_entry_meta: dict[str, dict] = {}

    def register_entry(
        self,
        trade_id: str,
        symbol: str,
        direction: str,
        units: float,
        entry_price: float,
        stop_price: float,
        tp_price: float = 0.0,
        tp1_price: float = 0.0,
        tp2_price: float = 0.0,
        strategy: str = "",
        v3_score: int = 0,
        metadata: dict | None = None,
    ) -> None:
        """Register a new trade after fill confirmation."""
        initial_risk = abs(entry_price - stop_price) if stop_price else 0.0
        self._positions[trade_id] = TrackedPosition(
            trade_id=trade_id,
            symbol=symbol,
            direction=direction,
            units=units,
            entry_price=entry_price,
            current_stop=stop_price,
            current_tp=tp_price,
            tp1_price=tp1_price,
            tp2_price=tp2_price,
            opened_at=datetime.now(timezone.utc).isoformat(),
            strategy=strategy,
            v3_score=v3_score,
            original_units=units,
            initial_risk_distance=initial_risk,
            peak_price=entry_price,
            peak_profit_distance=0.0,
            metadata=metadata or {},
        )
        log.info("[TRACKER] Registered: %s %s %s %d units @ %.5f SL=%.5f",
                 trade_id, symbol, direction, units, entry_price, stop_price)
        self.persist()

    def get(self, trade_id: str) -> TrackedPosition | None:
        return self._positions.get(trade_id)

    def all_positions(self) -> list[TrackedPosition]:
        return list(self._positions.values())

    def update_stop(self, trade_id: str, new_stop: float) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.current_stop = new_stop
            self.persist()

    def update_units(self, trade_id: str, new_units: float) -> None:
        """Sync tracked unit count with broker truth after a partial close.

        Without this, tracked.units stays at the original size forever, and
        any subsequent fraction-based close (e.g. int(units * 0.5)) will
        compute half of the ORIGINAL size — not half of what's actually
        open — generating dust or over-sized close requests.
        """
        pos = self._positions.get(trade_id)
        if pos:
            old_units = pos.units
            pos.units = float(new_units)
            log.info("[TRACKER] Units updated: %s %.0f -> %.0f", trade_id, old_units, new_units)
            self.persist()

    def update_peak(self, trade_id: str, current_price: float) -> bool:
        """Update MFE tracking (peak_price + peak_profit_distance).

        Called every management cycle. Persists only when the peak actually
        moves (avoids writing on every tick). Returns True if updated.
        """
        pos = self._positions.get(trade_id)
        if not pos:
            return False
        # Direction-aware "more favorable" check.
        if pos.direction == "long":
            if current_price > pos.peak_price:
                pos.peak_price = current_price
                pos.peak_profit_distance = current_price - pos.entry_price
                self.persist()
                return True
        else:
            # For shorts: peak is the LOWEST price seen. Bootstrap peak_price
            # at entry_price on register, so initial comparison works.
            if pos.peak_price <= 0 or current_price < pos.peak_price:
                pos.peak_price = current_price
                pos.peak_profit_distance = pos.entry_price - current_price
                self.persist()
                return True
        return False

    def mark_tp1_taken(self, trade_id: str) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.tp1_taken = True
            log.info("[TRACKER] TP1 taken: %s", trade_id)
            self.persist()

    def mark_break_even(self, trade_id: str) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.break_even_achieved = True
            self.persist()

    def remove(self, trade_id: str) -> TrackedPosition | None:
        pos = self._positions.pop(trade_id, None)
        if pos:
            log.info("[TRACKER] Removed: %s %s", trade_id, pos.symbol)
            self.persist()
        return pos

    def reconcile_with_broker(self, broker_trade_ids: set[str]) -> list[str]:
        """Remove positions that OANDA no longer has open. Returns vanished IDs."""
        vanished = []
        for tid in list(self._positions.keys()):
            if tid not in broker_trade_ids:
                pos = self._positions.pop(tid)
                vanished.append(tid)
                log.warning("[TRACKER] Trade vanished: %s %s (closed externally)", tid, pos.symbol)
        if vanished:
            self.persist()
        return vanished

    def persist(self) -> None:
        if not self._persist_path:
            return
        self._persist_path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "_positions": {tid: asdict(pos) for tid, pos in self._positions.items()},
            "_pending_entries": self._pending_entries,
            "_pending_entry_meta": self._pending_entry_meta,
        }
        with open(self._persist_path, "w") as f:
            json.dump(data, f, indent=2, default=str)

    def restore(self) -> int:
        if not self._persist_path or not self._persist_path.exists():
            return 0
        with open(self._persist_path) as f:
            data = json.load(f)
        # Handle both old format (flat dict of positions) and new format
        if "_positions" in data:
            positions = data["_positions"]
            self._pending_entries = data.get("_pending_entries", {})
            self._pending_entry_meta = data.get("_pending_entry_meta", {})
        else:
            positions = data  # old format: entire dict is positions
            self._pending_entries = {}
            self._pending_entry_meta = {}
        for tid, d in positions.items():
            self._positions[tid] = TrackedPosition(**{
                k: v for k, v in d.items() if k in TrackedPosition.__dataclass_fields__
            })
        log.info("[TRACKER] Restored %d positions, %d pending entries from disk",
                 len(self._positions), len(self._pending_entries))
        return len(self._positions)

    # --- Pending entries (limit orders waiting to fill) ---

    def register_pending_entry(self, symbol: str, order_id: str) -> None:
        self._pending_entries[symbol] = order_id
        self.persist()

    def get_pending_entry(self, symbol: str) -> str | None:
        return self._pending_entries.get(symbol)

    def clear_pending_entry(self, symbol: str) -> None:
        self._pending_entries.pop(symbol, None)
        self._pending_entry_meta.pop(symbol, None)
        self.persist()

    def all_pending_entries(self) -> dict[str, str]:
        return dict(self._pending_entries)

    def set_pending_entry_meta(self, symbol: str, meta: dict) -> None:
        """Store metadata for a pending entry (survives restart)."""
        self._pending_entry_meta[symbol] = meta
        self.persist()

    def get_pending_entry_meta(self, symbol: str) -> dict:
        """Get stored metadata for a pending entry."""
        return self._pending_entry_meta.get(symbol, {})

    def clear_pending_entry_meta(self, symbol: str) -> None:
        self._pending_entry_meta.pop(symbol, None)

    # --- Harvest limit orders ---

    def set_harvest_order(self, trade_id: str, order_id: str) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.harvest_order_id = order_id
            self.persist()

    def clear_harvest_order(self, trade_id: str) -> None:
        pos = self._positions.get(trade_id)
        if pos:
            pos.harvest_order_id = ""
            self.persist()

    def get_positions_with_harvest_orders(self) -> list[TrackedPosition]:
        return [p for p in self._positions.values() if p.harvest_order_id]
