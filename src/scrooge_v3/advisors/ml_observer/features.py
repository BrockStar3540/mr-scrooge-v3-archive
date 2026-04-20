# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Feature Extraction (V3, expanded).

Builds a full-fidelity scan row from a V3 /api/data signal object plus an
optional parsed [V3_SCORER] log line. Target: >=47 fields per scan. Nothing
is dropped — variable fields (p_*/n_* pair adjustments, any unrecognized
scorer key) are preserved verbatim under `pair_adjustments` / `raw_extra`.

Layout of a `scans.jsonl` row:
    {
        "ts": <iso8601>,
        "cycle": <int>,
        "symbol": <str>,
        "verdict": <str>,
        "strategy_allowed": <str>,
        "spread": <float>,

        "scorer": {base, final, tier, fam, session, floor, b, a, cap,
                   pairs_raw, capped, score, pairs_total, base_score,
                   blocks, blocks_count, factors, pair_adjustments,
                   context, raw_extra},

        "features": {  # all module outputs, flattened per module namespace
            "atr": {...}, "bollinger": {...}, "rsi": {...}, "ema": {...},
            "otr": {...}, "volume": {...}, "zone_detector": {...},
        },
        "classifications": {regime, bb_state, opening_state, structure},
        "gates": {<gate_name>: {"passed": bool, "reason": str}},

        "ml_features": {flat numeric dict — stable schema for XGBoost},
        "metadata": {hour_utc, day_of_week, ...},
        "trade_id": null,  # outcomes.jsonl owns this linkage
    }

FEATURE_NAMES lists the stable ml_features keys (positional vector used
by the trainer). New factors append at the end so older model files
keep loading; retraining refreshes the importance ranking.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional


# Stable, append-only ordering of ML feature names.
FEATURE_NAMES = [
    # V3 scorer head
    "scorer_base", "scorer_final", "scorer_floor", "scorer_b", "scorer_a",
    "scorer_cap", "scorer_pairs_raw", "scorer_capped",
    # V3 scorer 17-factor breakdown
    "sc_hr", "sc_age", "sc_stp", "sc_vol", "sc_mom", "sc_dc",
    "sc_z", "sc_bb", "sc_e50", "sc_e20", "sc_otr", "sc_adr",
    "sc_dur", "sc_wal", "sc_bdy", "sc_bbs", "sc_rsi",
    # Aggregates (API)
    "v3_score", "v3_pairs_total", "v3_base_score",
    # Market features
    "z_score", "bb_position", "rsi", "adr_consumed",
    "atr", "atr_20pct", "atr_60pct", "atr_80pct",
    "otr_ratio", "total_overhead", "range_half",
    "volume_ratio", "current_volume", "avg_volume",
    "box_age_hours", "box_range", "wall_proximity",
    "ema20_dist_pct", "ema50_dist_pct",
    "px_vs_ema20_bps", "px_vs_ema50_bps",
    # Regime / classifications
    "regime_score",
    "bb_state_confidence", "opening_state_confidence", "regime_confidence",
    # Context (from scorer log line)
    "ctx_px", "ctx_ema20", "ctx_ema50", "ctx_box", "ctx_box_age_hours",
    # Temporal
    "hour_utc", "day_of_week", "minute_of_day",
]

# Sanity: must be at least 47 as documented in the scope brief.
assert len(FEATURE_NAMES) >= 47, \
    f"FEATURE_NAMES has {len(FEATURE_NAMES)} entries — spec requires >=47"


def _safe_get(d: dict, *keys, default=0.0) -> float:
    cur = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
        if cur is None:
            return default
    try:
        return float(cur)
    except (TypeError, ValueError):
        return default


def _safe_str(d: dict, *keys, default="") -> str:
    cur = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
        if cur is None:
            return default
    return str(cur)


def _normalize_gates(gates_raw: dict) -> dict:
    """V3 emits gates as {name: {passed: bool, reason: str}} per candidate.
    Empty dict means scorer ran with no candidate-level gate evaluation
    (e.g. early scorer REJECT path). Preserve as-is but normalize types."""
    out: dict = {}
    if not isinstance(gates_raw, dict):
        return out
    for name, info in gates_raw.items():
        if isinstance(info, dict):
            out[name] = {
                "passed": bool(info.get("passed", False)),
                "reason": str(info.get("reason", "")),
            }
        else:
            out[name] = {"passed": False, "reason": str(info)}
    return out


def build_scan_row(
    signal: dict,
    *,
    cycle: Optional[int] = None,
    timestamp: Optional[str] = None,
    scorer_log_parsed: Optional[dict] = None,
) -> dict:
    """
    Build a full-fidelity scan row. `scorer_log_parsed` comes from
    `v3_scorer_parser.parse_v3_scorer_line`; if absent, the row is still
    valid — the log-only fields (fam, session, floor, b, a, cap,
    pairs_raw, capped, pair_adjustments, context) will be empty or
    defaulted.
    """
    sc = signal.get("scorer", {}) or {}
    bd = sc.get("breakdown", {}) or {}
    feat = signal.get("features", {}) or {}
    cls = signal.get("classifications", {}) or {}
    gates = signal.get("gates", {}) or {}

    # Parse temporal from timestamp
    hour_utc = 0.0
    day_of_week = 0.0
    minute_of_day = 0.0
    if timestamp:
        try:
            dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            hour_utc = float(dt.hour)
            day_of_week = float(dt.weekday())
            minute_of_day = float(dt.hour * 60 + dt.minute)
        except (ValueError, TypeError):
            pass

    # Scorer section: merge API scorer + parsed log head/factors/extras.
    parsed = scorer_log_parsed or {}
    scorer_section = {
        # API-provided
        "score": sc.get("score"),
        "tier": sc.get("tier", parsed.get("tier", "")),
        "pairs_total": bd.get("pairs_total"),
        "base_score": bd.get("base_score"),
        "blocks": sc.get("blocks", []),
        "blocks_count": len(sc.get("blocks") or []),
        # Log-only additions
        "base": parsed.get("base"),
        "final": parsed.get("final"),
        "fam": parsed.get("fam", ""),
        "session": parsed.get("session", ""),
        "floor": parsed.get("floor"),
        "b": parsed.get("b"),
        "a": parsed.get("a"),
        "cap": parsed.get("cap"),
        "pairs_raw": parsed.get("pairs_raw"),
        "capped": parsed.get("capped"),
        # Factor dict (prefer parsed; fall back to API breakdown)
        "factors": parsed.get("factors") or {
            k: bd.get(k) for k in
            ("hr", "age", "stp", "vol", "mom", "dc", "z", "bb", "e50", "e20",
             "otr", "adr", "dur", "wal", "bdy", "bbs", "rsi")
            if k in bd
        },
        "pair_adjustments": parsed.get("pair_adjustments", {}),
        "context": parsed.get("context", {}),
        "raw_extra": parsed.get("raw_extra", {}),
    }

    # Flat ML features vector — exhaustive, schema-stable.
    factors = scorer_section["factors"] or {}
    ctx = scorer_section["context"] or {}

    px_ema20_bps = 0.0
    px_ema50_bps = 0.0
    px = ctx.get("px", 0.0) or 0.0
    e20 = ctx.get("ema20", 0.0) or 0.0
    e50 = ctx.get("ema50", 0.0) or 0.0
    if px and e20:
        px_ema20_bps = (px - e20) / e20 * 1e4
    if px and e50:
        px_ema50_bps = (px - e50) / e50 * 1e4

    ml_features = {
        # Scorer head
        "scorer_base":     float(scorer_section.get("base") or 0),
        "scorer_final":    float(scorer_section.get("final") or 0),
        "scorer_floor":    float(scorer_section.get("floor") or 0),
        "scorer_b":        float(scorer_section.get("b") or 0),
        "scorer_a":        float(scorer_section.get("a") or 0),
        "scorer_cap":      float(scorer_section.get("cap") or 0),
        "scorer_pairs_raw": float(scorer_section.get("pairs_raw") or 0),
        "scorer_capped":   float(scorer_section.get("capped") or 0),
        # 17 factors
        "sc_hr":   float(factors.get("hr", 0)),
        "sc_age":  float(factors.get("age", 0)),
        "sc_stp":  float(factors.get("stp", 0)),
        "sc_vol":  float(factors.get("vol", 0)),
        "sc_mom":  float(factors.get("mom", 0)),
        "sc_dc":   float(factors.get("dc", 0)),
        "sc_z":    float(factors.get("z", 0)),
        "sc_bb":   float(factors.get("bb", 0)),
        "sc_e50":  float(factors.get("e50", 0)),
        "sc_e20":  float(factors.get("e20", 0)),
        "sc_otr":  float(factors.get("otr", 0)),
        "sc_adr":  float(factors.get("adr", 0)),
        "sc_dur":  float(factors.get("dur", 0)),
        "sc_wal":  float(factors.get("wal", 0)),
        "sc_bdy":  float(factors.get("bdy", 0)),
        "sc_bbs":  float(factors.get("bbs", 0)),
        "sc_rsi":  float(factors.get("rsi", 0)),
        # Aggregates
        "v3_score":        float(sc.get("score", 0) or 0),
        "v3_pairs_total":  float(bd.get("pairs_total", 0) or 0),
        "v3_base_score":   float(bd.get("base_score", 0) or 0),
        # Market
        "z_score":         _safe_get(feat, "bollinger", "z_score"),
        "bb_position":     _safe_get(feat, "bollinger", "bb_position"),
        "rsi":             _safe_get(feat, "rsi", "rsi"),
        "adr_consumed":    _safe_get(feat, "atr", "adr_consumed"),
        "atr":             _safe_get(feat, "atr", "atr"),
        "atr_20pct":       _safe_get(feat, "atr", "atr_20pct"),
        "atr_60pct":       _safe_get(feat, "atr", "atr_60pct"),
        "atr_80pct":       _safe_get(feat, "atr", "atr_80pct"),
        "otr_ratio":       _safe_get(feat, "otr", "otr_ratio"),
        "total_overhead":  _safe_get(feat, "otr", "total_overhead"),
        "range_half":      _safe_get(feat, "otr", "range_half"),
        "volume_ratio":    _safe_get(feat, "volume", "volume_ratio"),
        "current_volume":  _safe_get(feat, "volume", "current_volume"),
        "avg_volume":      _safe_get(feat, "volume", "avg_volume"),
        "box_age_hours":   _safe_get(feat, "zone_detector", "box_age_hours"),
        "box_range":       _safe_get(feat, "zone_detector", "box_range"),
        "wall_proximity":  _safe_get(feat, "zone_detector", "wall_proximity"),
        "ema20_dist_pct":  _safe_get(feat, "ema", "ema20_dist_pct"),
        "ema50_dist_pct":  _safe_get(feat, "ema", "ema50_dist_pct"),
        "px_vs_ema20_bps": float(px_ema20_bps),
        "px_vs_ema50_bps": float(px_ema50_bps),
        # Regime
        "regime_score":             _safe_get(cls, "regime", "metadata", "score"),
        "bb_state_confidence":      _safe_get(cls, "bb_state", "confidence"),
        "opening_state_confidence": _safe_get(cls, "opening_state", "confidence"),
        "regime_confidence":        _safe_get(cls, "regime", "confidence"),
        # Context (from log)
        "ctx_px":             float(ctx.get("px", 0.0) or 0.0),
        "ctx_ema20":          float(ctx.get("ema20", 0.0) or 0.0),
        "ctx_ema50":          float(ctx.get("ema50", 0.0) or 0.0),
        "ctx_box":            float(ctx.get("box", 0.0) or 0.0),
        "ctx_box_age_hours":  float(ctx.get("age", 0.0) or 0.0),
        # Temporal
        "hour_utc":      float(hour_utc),
        "day_of_week":   float(day_of_week),
        "minute_of_day": float(minute_of_day),
    }

    classifications_clean = {
        label_key: {
            "label": _safe_str(cls, label_key, "label"),
            "confidence": _safe_get(cls, label_key, "confidence"),
            "metadata": (cls.get(label_key) or {}).get("metadata", {})
                       if isinstance(cls.get(label_key), dict) else {},
        }
        for label_key in ("regime", "bb_state", "opening_state", "structure")
    }

    return {
        "ts": timestamp,
        "cycle": cycle,
        "symbol": signal.get("symbol", ""),
        "verdict": signal.get("verdict", ""),
        "strategy_allowed": signal.get("strategy_allowed", ""),
        "spread": signal.get("spread", 0),
        "scorer": scorer_section,
        "features": feat,  # raw module outputs, preserved verbatim
        "classifications": classifications_clean,
        "gates": _normalize_gates(gates),
        "ml_features": ml_features,
        "metadata": {
            "hour_utc": hour_utc,
            "day_of_week": day_of_week,
            "minute_of_day": minute_of_day,
        },
        "trade_id": None,
    }


# Backwards-compat wrapper for the old call signature (used by advise()).
def extract_features(signal: dict, timestamp: Optional[str] = None) -> dict:
    row = build_scan_row(signal, timestamp=timestamp)
    return {"features": row["ml_features"], "metadata": {
        "symbol": row["symbol"],
        "verdict": row["verdict"],
        "v3_tier": row["scorer"].get("tier", ""),
        "v3_blocks": row["scorer"].get("blocks", []),
        "spread": row["spread"],
        "bb_state": row["classifications"]["bb_state"]["label"],
        "regime_state": row["classifications"]["regime"]["label"],
    }}


__all__ = ["FEATURE_NAMES", "build_scan_row", "extract_features"]
