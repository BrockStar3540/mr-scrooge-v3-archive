"""Context builder -- assembles SymbolContext from features and classifiers.

Runs all registered feature modules, then all registered classifier modules,
producing a complete SymbolContext ready for strategy evaluation.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Sequence

from scrooge_v3.core.types import (
    ClassificationResult,
    FeatureResult,
    MarketSnapshot,
    SymbolContext,
)

log = logging.getLogger("scrooge_v3.context.builder")


class ContextBuilder:
    """
    Builds a complete SymbolContext by running all features and classifiers.

    Usage:
        builder = ContextBuilder(
            feature_registry=[atr, bollinger, zone_detector, range_builder, otr],
            classifier_registry=[bb_classifier, regime, structure, opening],
        )
        ctx = builder.build(symbol, snapshot, state)
    """

    def __init__(
        self,
        feature_registry: Sequence[Any],
        classifier_registry: Sequence[Any],
    ):
        self.features = list(feature_registry)
        self.classifiers = list(classifier_registry)

    def build(
        self,
        symbol: str,
        snapshot: MarketSnapshot,
        state: dict,
    ) -> SymbolContext:
        """
        Builds a complete SymbolContext.

        1. Run all active features -> populate ctx.features
        2. Run all active classifiers -> populate ctx.classifications
        3. Return complete SymbolContext
        """
        ctx = SymbolContext(
            symbol=symbol,
            snapshot=snapshot,
            features={},
            classifications={},
            state=state,
            metadata={"built_at": datetime.now().isoformat()},
        )

        # Phase 1: Features
        for feature in self.features:
            try:
                result: FeatureResult = feature.compute(symbol, snapshot, state)
                ctx.features[feature.name] = result
            except Exception as e:
                log.error(
                    f"Feature '{feature.name}' failed for {symbol}: {e}",
                    exc_info=True,
                )
                ctx.features[feature.name] = FeatureResult(
                    name=feature.name,
                    values={"error": str(e)},
                    computed_at=datetime.now(),
                )

        # Phase 2: Classifiers (can read features from ctx)
        for classifier in self.classifiers:
            try:
                result: ClassificationResult = classifier.classify(ctx)
                ctx.classifications[classifier.name] = result
            except Exception as e:
                log.error(
                    f"Classifier '{classifier.name}' failed for {symbol}: {e}",
                    exc_info=True,
                )
                ctx.classifications[classifier.name] = ClassificationResult(
                    name=classifier.name,
                    label="ERROR",
                    confidence=0.0,
                    metadata={"error": str(e)},
                )

        return ctx
