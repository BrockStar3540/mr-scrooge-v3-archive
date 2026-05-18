"""Seed-tier telemetry ledger -- append-only JSONL of every EntryFilter
(and shadow) evaluation, with enough context to drive offline expansion
mining without re-scanning the corpus.

Per Brock 2026-05-18: the bot is the search-target generator. Every
blocked candidate identifies a real-world (regime, pair, session,
family, direction) tuple that the routing surface should cover. The
offline expansion queues consume this ledger to drive:

  - no_match queue        (no cell anywhere -- find or mine a new one)
  - boundary_thin queue   (cell exists but shave_rule misses by <10%)
  - session_sibling queue (cell exists but for the wrong session)
"""

from __future__ import annotations

import json
import logging
import os
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.telemetry.seed_telemetry")


class SeedTelemetryLedger:
    """JSONL appender. One file per ledger, thread-safe via simple lock.

    Schema per row (any field may be null/missing if not applicable):
      ts                   ISO-8601 UTC timestamp
      gate                 'entry_filter' | 'entry_filter_shadow'
      symbol               pair, e.g. EUR_JPY
      regime53             technical_regime_53 label (C01, C02, ...)
      session_bucket       7-bucket session (asia, london_open, ny_mid, ...)
      direction            long | short
      candidate_strategy   the FAMILY name the bot generated (direct/dbb_trend/reversal)
      block_reason         entry_filter's structured reason string
      cell_strategy        matched cell strategy_id (e.g. TF4_sar_long) or null
      cell_family          matched cell family or null
      cell_tier            Probationary / Seed / Standard / Seed-Pro / Pro / Elite
      cell_direction       matched cell direction or null
      shave_rule           the shave_rule from the matched cell, if any
      shave_outcome        ok | violated:<feat><op><val> (got <value>) | null
      factors              snapshot dict of features used in shave_rule eval
      passed               final pipeline-relevant pass/fail (HARD gate semantics)
    """

    def __init__(self, filepath: str | Path):
        self._path = Path(filepath)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._fp = open(self._path, "a", buffering=1)  # line-buffered
        log.info("[SEED_TELEMETRY] ledger opened path=%s", self._path)

    def record(self, **fields: Any) -> None:
        row = {"ts": datetime.now(timezone.utc).isoformat(), **fields}
        line = json.dumps(row, default=str)
        with self._lock:
            self._fp.write(line)
            self._fp.write(os.linesep)

    def close(self) -> None:
        try:
            self._fp.close()
        except Exception:
            pass
