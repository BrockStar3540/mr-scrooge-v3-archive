"""matrix_engine — shared backend for the 4 layered matrix gates.

Each layered gate (session_filter, pair_filter, matrix_combo_filter,
matrix_signature_filter) does one focused thing. This module owns:
  * winner_loser_formulas index, lazily loaded once.
  * factor_buckets.FACTORS list.
  * candidate-row builder so every gate sees the same row schema.
  * bucket computation.
  * combo-string helpers (family resolution, key formatting).
"""

from __future__ import annotations

import logging
import sys
import threading
from pathlib import Path
from typing import Optional

import pandas as pd

from scrooge_v3.core.types import SymbolContext, TradeCandidate

LAB_DIR = Path("/home/ubuntu/mr-scrooge-v3/data/lab_matrix")
WLF_CSV = LAB_DIR / "winner_loser_formulas.csv"

if str(LAB_DIR) not in sys.path:
    sys.path.insert(0, str(LAB_DIR))

log = logging.getLogger("scrooge_v3.gate.matrix_engine")

HTF20_MISMATCH_BUCKETS = {"H20d", "H20e"}
KNOWN_SESSIONS = {
    "asia", "asia_late", "london_open", "london",
    "ny_open", "ny_mid", "ny_close", "off_hours",
}

_lock = threading.Lock()
_FACTORS = None
_wlf_index: Optional[dict] = None
_pair_session_combos: Optional[dict] = None
_loaded = False


def _do_load() -> None:
    global _FACTORS, _wlf_index, _pair_session_combos, _loaded
    if _loaded:
        return
    from factor_buckets import FACTORS  # type: ignore  # noqa
    _FACTORS = FACTORS
    df = pd.read_csv(WLF_CSV)
    idx: dict = {}
    ps: dict = {}
    winners = losers = neutrals = insufficient = 0
    for r in df.itertuples(index=False):
        cls = str(r.classification)
        if cls == "WINNER": winners += 1
        elif cls == "LOSER": losers += 1
        elif cls == "NEUTRAL": neutrals += 1
        else: insufficient += 1
        combo = str(r.combo)
        f = str(r.factor)
        b = str(r.bucket)
        try:
            wr = float(r.wr); n = int(r.n)
        except Exception:
            wr, n = 0.0, 0
        idx.setdefault(combo, {}).setdefault(f, {})[b] = (cls, wr, n)
        try:
            pair, strat, direction, session = combo.split("|", 3)
            ps.setdefault((pair, session), set()).add((strat, direction))
        except Exception:
            pass
    _wlf_index = idx
    _pair_session_combos = ps
    _loaded = True
    log.info(
        "[MATRIX_ENGINE] loaded WLF: %d rows, %d combos, %d (pair,session) pairs, "
        "%d WINNER / %d LOSER / %d NEUTRAL / %d INSUFFICIENT, %d factors",
        len(df), len(idx), len(ps), winners, losers, neutrals, insufficient, len(FACTORS),
    )


def load() -> None:
    if _loaded:
        return
    with _lock:
        if _loaded:
            return
        _do_load()


def factors():
    load()
    return _FACTORS


def wlf_index() -> dict:
    load()
    return _wlf_index or {}


def pair_session_combos() -> dict:
    load()
    return _pair_session_combos or {}


def candidate_family(candidate: TradeCandidate) -> str:
    md_fam = (candidate.metadata or {}).get("strategy_family", "")
    if md_fam:
        return str(md_fam)
    strat = (candidate.strategy or "").lower()
    if strat.startswith("dbb"): return "canonical_lien_dbb"
    if strat.startswith("mtb"): return "box_master_theory"
    if strat.startswith("drv"): return "canonical_darvas"
    if strat.startswith("rg"): return "reversal"
    if strat.startswith("itp_"): return "trend_pullback"
    if strat.startswith("cma_"): return "chaikin_macd_atr"
    if strat.startswith("cmr_"): return "compression_reversion"
    if strat.startswith("ce_"): return "compression_expansion"
    if strat.startswith("sb_"): return "session_breakout"
    if strat.startswith("ifvg"): return "ifvg"
    return candidate.strategy or ""


def candidate_direction(candidate: TradeCandidate) -> str:
    d = getattr(candidate.direction, "value", str(candidate.direction))
    if d:
        d = d.lower().replace("tradedirection.", "")
    return d


def candidate_session(ctx: SymbolContext) -> str:
    cls = ctx.classifications or {}
    sb = cls.get("session_bucket")
    return getattr(sb, "label", "") if sb else ""


def row_from_ctx(candidate: TradeCandidate, ctx: SymbolContext) -> dict:
    feat = ctx.features or {}

    def fv(name):
        f = feat.get(name)
        if f is None:
            return {}
        return getattr(f, "values", {}) if hasattr(f, "values") else (f if isinstance(f, dict) else {})

    mx = fv("matrix_features")
    bb = fv("bollinger"); atr = fv("atr"); rsi = fv("rsi")
    st = fv("structure"); rng = fv("range")

    sym = candidate.symbol or ""
    spread_raw = float(getattr(ctx.snapshot, "spread", 0.0) or 0.0)
    pip = 0.01 if any(j in sym for j in ("JPY", "MXN")) else 0.0001
    spread_pips = spread_raw / pip if pip > 0 else 0.0

    bb_width_live = None
    ua, la = bb.get("upper_a"), bb.get("lower_a")
    if ua is not None and la is not None and pip > 0:
        try:
            bb_width_live = (float(ua) - float(la)) / pip
        except Exception:
            bb_width_live = None

    return {
        "pair": sym,
        "strategy_id": candidate.strategy or "",
        "direction_exec": candidate_direction(candidate),
        "session_bucket": candidate_session(ctx),
        "spread_pips": spread_pips,
        "rsi14": mx.get("rsi14") or rsi.get("rsi") or rsi.get("rsi14") or rsi.get("value"),
        "rsi": rsi.get("rsi"),
        "zscore": mx.get("zscore") or bb.get("z_score"),
        "z_score": bb.get("z_score"),
        "bb_position": bb.get("bb_position") or bb.get("position"),
        "bb_width_pips": mx.get("bb_width_pips") or bb_width_live,
        "atr_5m_pips": mx.get("atr_5m_pips"),
        "atr_1h_pips": mx.get("atr_1h_pips"),
        "realized_vol": atr.get("realized_vol"),
        "adr_consumed": atr.get("adr_consumed"),
        "ema20_slope": mx.get("ema20_slope"),
        "ema50_slope": mx.get("ema50_slope"),
        "htf_pct_20": mx.get("htf_pct_20"),
        "htf_pct_60": mx.get("htf_pct_60"),
        "htf_bias_20": mx.get("htf_bias_20"),
        "htf_bias_60": mx.get("htf_bias_60"),
        "trend_1h": mx.get("trend_1h"),
        "trend_4h": mx.get("trend_4h"),
        "range_percentile": rng.get("range_percentile"),
        "pullback_depth_pct": st.get("pullback_depth_pct"),
        "_matrix_features_degraded": mx.get("_degraded", []),
    }


def compute_buckets(row: dict, stop_pips: float = 7.0) -> dict:
    load()
    sym = row.get("pair", "") or ""
    pip = 0.01 if any(j in sym for j in ("JPY", "MXN")) else 0.0001
    ctx = {
        "stop_pips": stop_pips,
        "pip_size": pip,
        "rv_baseline": 0.002,
        "direction": row.get("direction_exec"),
    }
    out: dict = {}
    for f in _FACTORS or []:
        try:
            out[f.code] = f.bucket_for(row, ctx)
        except Exception:
            out[f.code] = f"{f.code}x"
    return out


def combo_key(pair: str, family: str, direction: str, session: str) -> str:
    return f"{pair}|{family}|{direction}|{session}"
