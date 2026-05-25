"""Build a live-shaped SymbolContext for one bar index.

Reuses real V3 feature + classifier modules so the same logic that runs
live runs in replay. The only synthetic part is the snapshot rolling
slices fed in.
"""
from __future__ import annotations
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

# Make sure src/ is importable
_SRC = Path("/home/ubuntu/mr-scrooge-v3/src")
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from scrooge_v3.core.types import MarketSnapshot, SymbolContext, FeatureResult, ClassificationResult

log = logging.getLogger("replay_lab.context_factory")


def build_snapshot(
    bundle: dict,
    i: int,
    symbol: str,
    m5_lookback: int = 200,
    h1_lookback: int = 200,
    d_lookback: int = 60,   # regime53 bb_compress needs 41+ daily bars
) -> MarketSnapshot:
    """Build a MarketSnapshot rooted at bar index i of the M5 frame."""
    m5 = bundle["M5"]
    h1 = bundle["H1"]
    d = bundle["D"]

    if i >= len(m5):
        raise IndexError(f"i={i} >= len(m5)={len(m5)}")

    bar = m5.iloc[i]
    ts = m5.index[i]
    mid = float(bar["Close"])
    spread = float(bar.get("spread", 0.0))
    bid = mid - spread / 2.0
    ask = mid + spread / 2.0

    # Rolling slices ending at the current bar (inclusive)
    m5_slice = m5.iloc[max(0, i - m5_lookback + 1): i + 1]
    h1_slice = h1[h1.index <= ts].tail(h1_lookback) if len(h1) > 0 else h1
    d_slice = d[d.index <= ts].tail(d_lookback) if len(d) > 0 else d

    # Live bot uses dict keys "M5", "1H", "D" — let'\''s match.
    candles = {
        "M5": m5_slice.rename(columns={"Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume"}),
        "5M": m5_slice.rename(columns={"Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume"}),
        "1H": h1_slice.rename(columns={"Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume"}) if len(h1_slice) > 0 else None,
        "D":  d_slice.rename(columns={"Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume"})  if len(d_slice) > 0  else None,
    }

    return MarketSnapshot(
        symbol=symbol, bid=bid, ask=ask, mid=mid,
        spread=spread, timestamp=ts.to_pydatetime() if hasattr(ts, "to_pydatetime") else ts,
        candles=candles,
    )


def _instantiate_feature_modules():
    """Lazy-import to avoid heavy startup when context_factory is just being checked."""
    from scrooge_v3.features.atr import ATRCalculator
    from scrooge_v3.features.bollinger import BollingerCalculator
    from scrooge_v3.features.ema import EMACalculator
    from scrooge_v3.features.rsi import RSICalculator
    from scrooge_v3.features.volume import VolumeCalculator
    from scrooge_v3.features.zone_detector import ZoneDetector
    from scrooge_v3.features.otr import OverheadRatioCalculator
    return {
        "atr": ATRCalculator(),
        "bollinger": BollingerCalculator(),
        "ema": EMACalculator(),
        "rsi": RSICalculator(),
        "volume": VolumeCalculator(),
        "zone_detector": ZoneDetector(),
        "otr": OverheadRatioCalculator(),
    }


def _instantiate_classifier_modules():
    from scrooge_v3.classifiers.session_bucket import SessionBucketClassifier
    from scrooge_v3.classifiers.mtb_sub_regime import MTBSubRegimeClassifier
    from scrooge_v3.classifiers.bb_state import BollingerStateClassifier
    from scrooge_v3.classifiers.regime import RegimeClassifier
    from scrooge_v3.classifiers.opening import OpeningStateClassifier
    from scrooge_v3.classifiers.structure import StructureClassifier
    from scrooge_v3.features.technical_regime_53 import TechnicalRegime53Calculator
    return {
        "session_bucket": SessionBucketClassifier(),
        "mtb_sub_regime": MTBSubRegimeClassifier(),
        "bb_state": BollingerStateClassifier(),
        "regime": RegimeClassifier(),
        "opening_state": OpeningStateClassifier(),
        "structure": StructureClassifier(),
        "regime53": TechnicalRegime53Calculator(),
    }


_FEATURES = None
_CLASSIFIERS = None

def get_features():
    global _FEATURES
    if _FEATURES is None:
        _FEATURES = _instantiate_feature_modules()
    return _FEATURES


def get_classifiers():
    global _CLASSIFIERS
    if _CLASSIFIERS is None:
        _CLASSIFIERS = _instantiate_classifier_modules()
    return _CLASSIFIERS


def build_context(
    bundle: dict,
    i: int,
    symbol: str,
    state: dict | None = None,
) -> SymbolContext:
    """Build a SymbolContext at bar index i.

    Runs the real feature calculators + classifiers against the synthetic
    snapshot so downstream strategy modules see live-shaped state.
    """
    state = state or {}
    snap = build_snapshot(bundle, i, symbol)
    features = {}
    for name, mod in get_features().items():
        try:
            features[name] = mod.compute(symbol, snap, state)
        except Exception as e:
            log.debug("feature %s failed for %s at %d: %s", name, symbol, i, e)
            features[name] = FeatureResult(name=name, values={"_degraded": True},
                                            computed_at=datetime.now())
    # Pre-build a context for classifiers that take (ctx) signature
    proto = SymbolContext(symbol=symbol, snapshot=snap, features=features,
                          classifications={}, state=state)

    classifications = {}
    for name, mod in get_classifiers().items():
        # Try (ctx) signature first, then (symbol, snap, state, features),
        # then (symbol, snap, state) — covers all observed live signatures.
        last_err = None
        for sig in ("ctx", "symbol_snap_state_features", "symbol_snap_state",
                     "ctx_features"):
            try:
                if sig == "ctx":
                    classifications[name] = mod.classify(proto)
                elif sig == "symbol_snap_state_features":
                    classifications[name] = mod.classify(symbol, snap, state, features)
                elif sig == "symbol_snap_state":
                    classifications[name] = mod.classify(symbol, snap, state)
                elif sig == "ctx_features":
                    # technical_regime_53.TechnicalRegime53Calculator.compute(symbol, snap, state)
                    classifications[name] = mod.compute(symbol, snap, state)
                break
            except (TypeError, AttributeError) as e:
                last_err = e
                continue
            except Exception as e:
                last_err = e
                break
        else:
            log.debug("classifier %s failed all sigs: %s", name, last_err)
            classifications[name] = ClassificationResult(name=name, label="unknown")
        if name not in classifications:
            classifications[name] = ClassificationResult(name=name, label="unknown")
        # Update proto so later classifiers see earlier classifications
        proto.classifications = classifications
    return SymbolContext(
        symbol=symbol, snapshot=snap,
        features=features, classifications=classifications,
        state=state,
    )
