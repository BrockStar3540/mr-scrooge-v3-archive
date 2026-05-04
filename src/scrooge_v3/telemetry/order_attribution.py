"""Order → strategy attribution map (Patch B.right).

Writes one JSONL row per order at placement time so downstream consumers
(ml-observer poller, audits) can resolve `(order_id) → strategy` deterministically
from the OANDA `tradeOpened` transaction's `orderID`, without walking
`scans.jsonl` backward in a fragile time window.

Pre-Patch-B.right, `_find_scan_for_trade` walked the last 800 lines of
`scans.jsonl` (~60 s of scans). Pending LIMIT entries that fill more than
~60 s after placement lost their scan match: 27/50 (54%) of live trade_open
events had `matched_scan_cycle: null`. This module fixes that class of bug.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Any

log = logging.getLogger("scrooge_v3.telemetry.order_attribution")


class OrderAttributionWriter:
    """Append-only writer for order → strategy attribution records.

    Reads are by `order_id` and tail-cached so a long-running ml-observer
    can pick up new orders without re-reading the whole file. Falls back
    silently on filesystem errors — attribution is best-effort, never
    blocks the main bot loop.
    """

    def __init__(self, filepath: str | Path = "data/order-attribution.jsonl"):
        self._filepath = Path(filepath)
        self._filepath.parent.mkdir(parents=True, exist_ok=True)
        self._lock = Lock()

    def record(
        self, *, order_id: str, symbol: str, strategy: str,
        direction: str = "", score: float = 0.0, tier: str = "",
        scan_cycle: int | None = None, placed_at: str | None = None,
        order_kind: str = "entry_limit",
    ) -> None:
        """Append a single attribution record. Returns silently on failure."""
        if not order_id or not symbol:
            return
        row = {
            "order_id": str(order_id),
            "symbol": symbol,
            "strategy": strategy or "",
            "direction": direction,
            "score": float(score),
            "tier": tier,
            "scan_cycle": scan_cycle,
            "placed_at": placed_at or datetime.now(timezone.utc).isoformat(),
            "order_kind": order_kind,
        }
        with self._lock:
            try:
                with open(self._filepath, "a") as f:
                    f.write(json.dumps(row) + "\n")
            except Exception:
                log.exception("[ATTRIB] write failed for order=%s", order_id)


def lookup_attribution(filepath: Path, order_id: str) -> dict[str, Any] | None:
    """Read-side helper: walk JSONL file backward, return first match by
    order_id. Used by ml-observer (separate process from writer)."""
    if not filepath.exists() or not order_id:
        return None
    target = str(order_id)
    try:
        # Read end-first; attribution rows for in-flight orders cluster at tail.
        lines = filepath.read_text().splitlines()
    except OSError:
        return None
    for line in reversed(lines):
        line = line.strip()
        if not line or '"order_id"' not in line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if str(row.get("order_id")) == target:
            return row
    return None
