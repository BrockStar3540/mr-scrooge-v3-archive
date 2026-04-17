# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Feature Extraction (V3)
Extracts a flat feature vector from a V3 /api/data signal object.

2026-04-16: Rewritten for V3 scorer format. V1/V2 score_detail
is replaced by V3 breakdown (hr, age, stp, vol, mom, etc.) plus
per-module features (bollinger, rsi, atr, ema, volume, zone_detector).
"""

from datetime import datetime
from typing import Optional


# Ordered feature names matching the vector — 30 features
FEATURE_NAMES = [
    # V3 scorer breakdown (17 factors)
    "sc_hr", "sc_age", "sc_stp", "sc_vol", "sc_mom", "sc_dc",
    "sc_z", "sc_bb", "sc_e50", "sc_e20", "sc_otr", "sc_adr",
    "sc_dur", "sc_wal", "sc_bdy", "sc_bbs", "sc_rsi",
    # V3 scorer aggregate
    "v3_score", "v3_pairs_total",
    # Market features
    "z_score", "bb_position", "rsi", "adr_consumed",
    "otr_ratio", "volume_ratio", "box_age_hours", "wall_proximity",
    "ema20_dist_pct", "ema50_dist_pct",
    # Regime
    "regime_score",
    # Temporal
    "hour_utc",
]


def _safe_get(d: dict, *keys, default=0.0):
    """Nested dict get with fallback."""
    current = d
    for k in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(k, None)
        if current is None:
            return default
    try:
        return float(current)
    except (TypeError, ValueError):
        return default


def extract_features(signal: dict, timestamp: Optional[str] = None) -> dict:
    """
    Extract a flat feature dict from a V3 signal object.

    V3 signals have:
      - scorer.breakdown: {hr, age, stp, vol, mom, dc, z, bb, ...}
      - features: {bollinger: {z_score, bb_position}, rsi: {rsi}, ...}
      - classifications: {regime: {metadata: {score}}, bb_state: ...}
      - verdict: NO_CANDIDATE, V3_REJECT, V3_BLOCKED, TAKE_LONG, TAKE_SHORT
    """
    sc = signal.get("scorer", {})
    bd = sc.get("breakdown", {})
    feat = signal.get("features", {})
    cls = signal.get("classifications", {})

    # Parse hour from timestamp
    hour_utc = 0.0
    if timestamp:
        try:
            dt = datetime.fromisoformat(timestamp)
            hour_utc = float(dt.hour)
        except (ValueError, TypeError):
            pass

    # Regime score from classifications
    regime_score = _safe_get(cls, "regime", "metadata", "score")

    features = {
        # V3 scorer breakdown
        "sc_hr": float(bd.get("hr", 0)),
        "sc_age": float(bd.get("age", 0)),
        "sc_stp": float(bd.get("stp", 0)),
        "sc_vol": float(bd.get("vol", 0)),
        "sc_mom": float(bd.get("mom", 0)),
        "sc_dc": float(bd.get("dc", 0)),
        "sc_z": float(bd.get("z", 0)),
        "sc_bb": float(bd.get("bb", 0)),
        "sc_e50": float(bd.get("e50", 0)),
        "sc_e20": float(bd.get("e20", 0)),
        "sc_otr": float(bd.get("otr", 0)),
        "sc_adr": float(bd.get("adr", 0)),
        "sc_dur": float(bd.get("dur", 0)),
        "sc_wal": float(bd.get("wal", 0)),
        "sc_bdy": float(bd.get("bdy", 0)),
        "sc_bbs": float(bd.get("bbs", 0)),
        "sc_rsi": float(bd.get("rsi", 0)),
        # V3 scorer aggregate
        "v3_score": float(sc.get("score", 0)),
        "v3_pairs_total": float(bd.get("pairs_total", 0)),
        # Market features from modules
        "z_score": _safe_get(feat, "bollinger", "z_score"),
        "bb_position": _safe_get(feat, "bollinger", "bb_position"),
        "rsi": _safe_get(feat, "rsi", "rsi"),
        "adr_consumed": _safe_get(feat, "atr", "adr_consumed"),
        "otr_ratio": _safe_get(feat, "otr", "otr_ratio"),
        "volume_ratio": _safe_get(feat, "volume", "volume_ratio"),
        "box_age_hours": _safe_get(feat, "zone_detector", "box_age_hours"),
        "wall_proximity": _safe_get(feat, "zone_detector", "wall_proximity"),
        "ema20_dist_pct": _safe_get(feat, "ema", "ema20_dist_pct"),
        "ema50_dist_pct": _safe_get(feat, "ema", "ema50_dist_pct"),
        # Regime
        "regime_score": regime_score,
        # Temporal
        "hour_utc": hour_utc,
    }

    # Metadata (not used as ML features)
    metadata = {
        "symbol": signal.get("symbol", ""),
        "verdict": signal.get("verdict", ""),
        "v3_tier": sc.get("tier", ""),
        "v3_blocks": sc.get("blocks", []),
        "spread": signal.get("spread", 0),
        "bb_state": _safe_get(cls, "bb_state", "label", default=""),
        "regime_state": _safe_get(cls, "regime", "label", default=""),
    }

    return {"features": features, "metadata": metadata}
