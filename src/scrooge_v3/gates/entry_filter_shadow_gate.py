"""EntryFilterShadowGate -- observe-only counterpart to EntryFilterGate.

Reads `routing_table_v9_observe.parquet` (or any user-specified file) and
runs the EntryFilterGate match + shave-rule evaluation logic in OBSERVE
mode against the BROADER routing surface (typically including Seed-tier
cells). Emits telemetry-only [GATE:entry_filter_shadow] lines that record
WHICH cells WOULD have fired had we been on the wider surface.

Purpose (Brock 2026-05-18): keep `Seed` tier OUT of live execution but
gather live evidence on Seed-cell candidates so we can promote them later
based on real-world performance rather than corpus replay alone.

Implementation: subclasses EntryFilterGate so the rule-replay logic stays
identical. Forces mode=OBSERVE in __init__ — even if config says "hard"
this gate cannot block the pipeline.
"""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode
from scrooge_v3.strategies.routing_table import RoutingTable

from .entry_filter_gate import EntryFilterGate


class EntryFilterShadowGate(EntryFilterGate):
    """Observe-only shadow of EntryFilterGate against a wider routing surface."""

    name = "entry_filter_shadow"

    def __init__(
        self,
        routing_table: RoutingTable,
        config: dict[str, Any] | None = None,
        # mode argument accepted for symmetry with bootstrap call site but
        # always coerced to OBSERVE -- shadow gates never block.
        mode: GateMode = GateMode.OBSERVE,
    ) -> None:
        super().__init__(
            routing_table=routing_table,
            config=config,
            mode=GateMode.OBSERVE,
        )
