"""Routing-table telemetry — tiered rollup + sampled death records.

Two tiers, sized for "enough to troubleshoot, not so much we drown":

  Tier 1 (rollup): in-memory counter per
        (regime53, pair, session, decision_state)
    Decision states:
      table_has_only        - table attaches, BB does not
      bb_has_only           - BB allows, table empty (a KILL under hard mode)
      both_have             - overlap
      both_empty            - universal death
    Flushed every N ticks (default 1000) to
        data/routing_rollup_YYYY-MM-DD.parquet
    ~10KB/day. This is the heatmap.

  Tier 2 (death sample): full records for the 'bb_has_only' state
    (the most-interesting case: BB-routing would have fired here but the
     table would kill it under hard mode). Sampled 1-in-N (default 10).
    Written to data/routing_death_samples_YYYY-MM-DD.parquet.
    ~50K rows/day. This is the drill-in.

Both tiers disabled by default. Enable via:
    config.strategies.routing_telemetry.enabled = true
    config.strategies.routing_telemetry.flush_every = 1000
    config.strategies.routing_telemetry.death_sample_rate = 10
"""

from __future__ import annotations

import logging
import random
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.strategies.routing_telemetry")


def _decision_state(bb_allowed: list[str], table_attached: list[str]) -> str:
    has_bb = bool(bb_allowed)
    has_table = bool(table_attached)
    if has_bb and has_table:    return "both_have"
    if has_bb and not has_table:return "bb_has_only"
    if not has_bb and has_table:return "table_has_only"
    return "both_empty"


@dataclass
class _Counter:
    count: int = 0


class RoutingTelemetryRollup:
    """In-memory rollup + sampled death writer.

    Thread-safety: not designed for concurrent writers. The scan pipeline is
    single-threaded per scheduler tick so this is fine. If we ever go
    multi-threaded, wrap _rollup + _death_buffer in a lock.
    """

    def __init__(
        self,
        data_dir: str | Path = "data",
        enabled: bool = False,
        flush_every: int = 1000,
        death_sample_rate: int = 10,
    ):
        self.data_dir = Path(data_dir)
        self.enabled = enabled
        self.flush_every = max(100, int(flush_every))
        self.death_sample_rate = max(1, int(death_sample_rate))

        self._rollup: dict[tuple[str, str, str, str], _Counter] = defaultdict(_Counter)
        self._death_buffer: list[dict[str, Any]] = []
        self._tick_count = 0
        self._last_flush = datetime.now(timezone.utc)

    def record(
        self,
        symbol: str,
        regime53: str | None,
        session_bucket: str | None,
        bb_allowed: list[str],
        table_strategies: list[str],
        table_families: list[str],
        ts: datetime | None = None,
    ) -> None:
        if not self.enabled:
            return
        if not regime53 or not session_bucket:
            return
        state = _decision_state(bb_allowed, table_strategies)
        key = (regime53, symbol, session_bucket, state)
        self._rollup[key].count += 1
        self._tick_count += 1

        # Sample death records — the bb_has_only case is the most interesting
        # (what would die under hard mode).
        if state == "bb_has_only" and self.death_sample_rate > 0:
            if random.randrange(self.death_sample_rate) == 0:
                self._death_buffer.append({
                    "ts": (ts or datetime.now(timezone.utc)).isoformat(),
                    "symbol": symbol,
                    "regime53": regime53,
                    "session_bucket": session_bucket,
                    "bb_allowed": ",".join(bb_allowed),
                    "table_strategies": ",".join(table_strategies),
                    "table_families": ",".join(table_families),
                })

        if self._tick_count >= self.flush_every:
            self.flush()

    def flush(self) -> None:
        if not self.enabled:
            return
        if not self._rollup and not self._death_buffer:
            self._tick_count = 0
            return
        try:
            import pandas as pd
        except ImportError:
            log.warning("[ROUTING_TELEMETRY] pandas not available; rollup discarded")
            self._rollup.clear()
            self._death_buffer.clear()
            self._tick_count = 0
            return

        self.data_dir.mkdir(parents=True, exist_ok=True)
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        # Tier 1: rollup
        if self._rollup:
            rollup_rows = [{
                "regime53": k[0], "pair": k[1], "session_bucket": k[2],
                "decision_state": k[3], "count": v.count,
                "flushed_at": datetime.now(timezone.utc).isoformat(),
            } for k, v in self._rollup.items()]
            new_df = pd.DataFrame(rollup_rows)
            rollup_path = self.data_dir / f"routing_rollup_{today}.parquet"
            if rollup_path.exists():
                try:
                    old = pd.read_parquet(rollup_path)
                    new_df = pd.concat([old, new_df], ignore_index=True)
                except Exception as e:
                    log.warning("[ROUTING_TELEMETRY] rollup merge failed: %s", e)
            new_df.to_parquet(rollup_path, index=False)
            self._rollup.clear()

        # Tier 2: death samples
        if self._death_buffer:
            death_df = __import__("pandas").DataFrame(self._death_buffer)
            death_path = self.data_dir / f"routing_death_samples_{today}.parquet"
            if death_path.exists():
                try:
                    old = __import__("pandas").read_parquet(death_path)
                    death_df = __import__("pandas").concat([old, death_df], ignore_index=True)
                except Exception as e:
                    log.warning("[ROUTING_TELEMETRY] death merge failed: %s", e)
            death_df.to_parquet(death_path, index=False)
            self._death_buffer.clear()

        log.info(
            "[ROUTING_TELEMETRY] flushed rollup ticks=%d (next flush every %d)",
            self._tick_count, self.flush_every,
        )
        self._tick_count = 0
        self._last_flush = datetime.now(timezone.utc)

    @property
    def stats(self) -> dict[str, Any]:
        return {
            "enabled": self.enabled,
            "buffered_cells": len(self._rollup),
            "buffered_deaths": len(self._death_buffer),
            "tick_count_since_flush": self._tick_count,
            "flush_every": self.flush_every,
            "death_sample_rate": self.death_sample_rate,
            "last_flush": self._last_flush.isoformat(),
        }
