"""Structure classifier -- formalizes the range state as a classification.

Reads ctx.features["range_builder"] for the current RangeStateRecord
and returns the range state as a ClassificationResult.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import ClassificationResult, SymbolContext
from scrooge_v3.features.range_models import RangeState

log = logging.getLogger("scrooge_v3.classifiers.structure")


class StructureClassifier:
    """
    Classifies the current range/box structure state.

    Labels: RANGING, BREACH_INITIATED, CONFIRMED_BREAK_RECALCULATING,
            NEW_RANGE_STANDBY, SHELVED

    Implements ClassifierModule protocol.
    """

    name: str = "structure"

    def classify(self, ctx: SymbolContext) -> ClassificationResult:
        rb = ctx.features.get("range_builder")
        if rb is None or not rb.values:
            return ClassificationResult(
                name=self.name,
                label="UNKNOWN",
                confidence=0.0,
                metadata={"detail": "No range_builder data available"},
            )

        record = rb.values.get("range_state_record")
        if record is None:
            return ClassificationResult(
                name=self.name,
                label="UNKNOWN",
                confidence=0.0,
                metadata={"detail": "No range state record in range_builder output"},
            )

        state: RangeState = record.state

        return ClassificationResult(
            name=self.name,
            label=state.value,
            confidence=1.0,
            metadata={
                "range_state": state.value,
                "entry_paused": record.entry_paused,
                "pause_reason": record.pause_reason,
                "breach_direction": record.breach_direction,
                "range_age_hours": record.range_age_hours,
                "age_confidence_pct": record.age_confidence_pct,
                "using_alternative": record.using_alternative,
                "new_range_proven": record.new_range_proven,
            },
        )
