"""ml_router.py — bot-side ML router that replaces the old strategy_router.

Asks the per-pair module: "given the current (pair, regime, session, buckets)
state, which strategies have a WIN rule matching, and no LOSE rule blocking?"
Returns the set of allowed strategy names — the scan_pipeline then iterates
ONLY those.

Loads the same per_pair_modules code the ml-observer service uses, so the
bot and the observer share the same knowledge library (both read the same
master_rules.csv and regime_centroids.csv files on disk).
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any

# Reuse the ml_observer's per_pair_modules loader to share state with observer.
ML_OBSERVER_DIR = Path("/home/ubuntu/mr-scrooge-v3/src/scrooge_v3/advisors/ml_observer")
if str(ML_OBSERVER_DIR) not in sys.path:
    sys.path.insert(0, str(ML_OBSERVER_DIR))

import per_pair_modules as ppm  # type: ignore  # noqa: E402

# factor_buckets is shipped alongside each pair's module, but we only need
# one copy at runtime. Use EUR_USD's bundled copy (all pairs ship identical lib).
FACTOR_BUCKETS_PATH = Path("/home/ubuntu/mr-scrooge-v3/data/per_pair_modules/EUR_USD/lib")
if str(FACTOR_BUCKETS_PATH) not in sys.path:
    sys.path.insert(0, str(FACTOR_BUCKETS_PATH))

import factor_buckets as fb  # type: ignore  # noqa: E402

log = logging.getLogger("scrooge_v3.strategies.ml_router")


# ---------------------------------------------------------------------------
# Variant -> family name resolution
# ---------------------------------------------------------------------------
# Lab rules pin family names (box_master_theory, canonical_lien_dbb).
# The bot's strategy code emits variant names (MTB2_pitchfork_long_with_wick,
# DBB1_buy_zone_long). When the ML router looks up rules, the variant is
# mapped to its family so the rule pinned to the family still applies.

def variant_to_family(strategy_name: str) -> str:
    if not strategy_name:
        return strategy_name
    s = strategy_name.lower()
    if s.startswith("dbb1") or s.startswith("dbb2") or s.startswith("dbb3"): return "canonical_lien_dbb"
    if s.startswith("dbb"):     return "canonical_lien_dbb"  # also dbb_trend etc.
    if s.startswith("mtb"):     return "box_master_theory"
    if s.startswith("drv"):     return "canonical_darvas"
    if s.startswith("ifvg"):    return "ifvg"
    if s.startswith("itp"):     return "trend_pullback"
    if s.startswith("cma"):     return "chaikin_macd_atr"
    if s.startswith("ce_"):     return "compression_expansion"
    if s.startswith("cmr"):     return "compression_reversion"
    if s.startswith("sb_"):     return "session_breakout"
    if s.startswith("rg"):      return "reversal"
    return strategy_name  # already family-level (direct, trend, reversal, etc.)


def _extract_row_for_buckets(symbol: str, ctx: Any) -> dict:
    """Pull the 14 factor-input values from ctx.features for bucket computation."""
    feat = ctx.features or {}

    def fv(name: str) -> dict:
        f = feat.get(name)
        if f is None:
            return {}
        v = getattr(f, "values", None)
        return v if isinstance(v, dict) else (f if isinstance(f, dict) else {})

    mx = fv("matrix_features")
    bb = fv("bollinger")
    atr = fv("atr")
    rsi = fv("rsi")

    pip = 0.01 if any(j in (symbol or "") for j in ("JPY", "MXN")) else 0.0001
    spread_raw = float(getattr(getattr(ctx, "snapshot", None), "spread", 0.0) or 0.0)
    spread_pips = spread_raw / pip if pip > 0 else 0.0

    bb_width_live = None
    ua, la = bb.get("upper_a"), bb.get("lower_a")
    if ua is not None and la is not None and pip > 0:
        try:
            bb_width_live = (float(ua) - float(la)) / pip
        except Exception:
            bb_width_live = None

    return {
        "pair": symbol,
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
    }


def _compute_buckets(symbol: str, row: dict) -> dict[str, str]:
    pip = 0.01 if any(j in (symbol or "") for j in ("JPY", "MXN")) else 0.0001
    ctx_dict = {"stop_pips": 7.0, "pip_size": pip, "rv_baseline": 0.002}
    out: dict[str, str] = {}
    for f in fb.FACTORS:
        try:
            out[f.code] = f.bucket_for(row, ctx_dict)
        except Exception:
            out[f.code] = f"{f.code}x"
    return out


def _session(ctx: Any) -> str:
    cls = getattr(ctx, "classifications", {}) or {}
    sb = cls.get("session_bucket")
    return getattr(sb, "label", "") if sb else ""


def get_allowed(symbol: str, ctx: Any) -> set[str]:
    """Return the set of strategy NAMES allowed for this candidate state.

    Algorithm:
      1. Look up per-pair module. If missing -> empty set (block all).
      2. Compute 14-bucket signature from current features.
      3. Assign regime via nearest centroid.
      4. For each (long, short) direction:
         For each known strategy in this regime's rules, check if any WIN rule
         matches AND no LOSE rule vetoes.
         If yes -> add that strategy name to allowed.
      5. Return union across both directions (strategies emit per-direction
         themselves; bot iterates allowed set then strategy decides direction).
    """
    mod = ppm.get(symbol)
    if mod is None:
        log.debug("[ML_ROUTER] no per-pair module for %s -> empty allowed", symbol)
        return set()

    row = _extract_row_for_buckets(symbol, ctx)
    buckets = _compute_buckets(symbol, row)
    session = _session(ctx)

    if not mod.rules.empty:
        regime = mod.assign_regime(buckets)
    else:
        regime = "R00"

    # Filter to this regime's rules
    sub = mod.rules[mod.rules["regime"] == regime]
    if sub.empty:
        log.debug("[ML_ROUTER] %s regime %s session %s -> no rules", symbol, regime, session)
        return set()

    allowed_strategies: set[str] = set()
    # Track every strategy referenced in the regime's rules — even strategy-
    # agnostic WIN rules (which don't pin strategy_id) imply "any strategy
    # that emits a candidate matching this rule may fire."
    has_unpinned_win = False

    for _, r in sub.iterrows():
        if str(r.get("rule_type", "")) != "WIN":
            continue
        raw = str(r.get("raw_rule", "") or "")
        if not raw:
            continue

        # Quick condition check (session, direction, bucket constraints)
        conds = [c.strip() for c in raw.split("AND") if "=" in c]
        cand_map = {"session_bucket": session, **buckets}
        ok = True
        rule_strategy = None
        for c in conds:
            ax, _, bv = c.partition("=")
            ax, bv = ax.strip(), bv.strip()
            if ax == "strategy_id":
                rule_strategy = bv
            elif ax == "direction_exec":
                continue  # direction handled per-strategy at evaluate time
            elif cand_map.get(ax) != bv:
                ok = False
                break
        if not ok:
            continue

        # Refinement check
        ref_op = str(r.get("refine_op", "") or "")
        ref_ax = str(r.get("refine_axis", "") or "")
        ref_b = str(r.get("refine_bucket", "") or "")
        if ref_op == "exclude" and ref_ax and ref_ax != "strategy_id" and ref_ax != "direction_exec":
            if cand_map.get(ref_ax) == ref_b:
                continue

        if rule_strategy:
            allowed_strategies.add(rule_strategy)
        else:
            has_unpinned_win = True

    # ---------------------------------------------------------------
    # LOSE veto (Brock 2026-05-28): walk LOSE rules for this regime.
    # Any LOSE rule whose conditions match current state vetoes either:
    #   - the specific strategy_id pinned in the rule, or
    #   - ALL strategies (unpinned LOSE → "this state loses regardless")
    # ---------------------------------------------------------------
    vetoed_strategies: set[str] = set()
    unpinned_lose_match = False
    for _, r in sub.iterrows():
        if str(r.get("rule_type", "")) != "LOSE":
            continue
        raw = str(r.get("raw_rule", "") or "")
        if not raw:
            continue
        conds = [c.strip() for c in raw.split("AND") if "=" in c]
        cand_map = {"session_bucket": session, **buckets}
        ok = True
        rule_strategy = None
        for c in conds:
            ax, _, bv = c.partition("=")
            ax, bv = ax.strip(), bv.strip()
            if ax == "strategy_id":
                rule_strategy = bv
            elif ax == "direction_exec":
                continue
            elif cand_map.get(ax) != bv:
                ok = False
                break
        if not ok:
            continue
        # Refinement: for LOSE rules, refine_op="include" means the sharpest
        # AVOID condition. Require the include bucket to match.
        ref_op = str(r.get("refine_op", "") or "")
        ref_ax = str(r.get("refine_axis", "") or "")
        ref_b = str(r.get("refine_bucket", "") or "")
        if ref_op == "include" and ref_ax and ref_ax not in ("strategy_id","direction_exec"):
            if cand_map.get(ref_ax) != ref_b:
                continue
        if rule_strategy:
            vetoed_strategies.add(rule_strategy)
        else:
            unpinned_lose_match = True

    if unpinned_lose_match:
        # An un-pinned LOSE pattern matches this state → block every strategy.
        log.info("[ML_ROUTER] %s regime=%s session=%s LOSE veto (unpinned) → block all",
                 symbol, regime, session)
        return set()
    if vetoed_strategies:
        log.info("[ML_ROUTER] %s regime=%s session=%s LOSE veto on %d strategy/ies: %s",
                 symbol, regime, session, len(vetoed_strategies),
                 ",".join(sorted(vetoed_strategies)))
        allowed_strategies -= vetoed_strategies
        # If we had an unpinned WIN but losers veto specific strategies, the
        # remaining "*" sentinel still needs to honor vetoes downstream — we
        # signal this via a tuple including a "_vetoed" hint.
        if has_unpinned_win:
            # Re-emit the "*" sentinel; get_allowed_or_all will subtract vetoed.
            return {"*"} | set(f"-{s}" for s in vetoed_strategies)

    if has_unpinned_win and not allowed_strategies:
        return {"*"}
    return allowed_strategies


def get_allowed_or_all(symbol: str, ctx: Any, all_strategies: set[str]) -> set[str]:
    """Wrapper that maps the '*' sentinel to the full active set.

    Sentinels:
      "*"       — unpinned WIN matched → allow all registered strategies.
      "-NAME"   — pinned LOSE veto → subtract NAME (and any variant whose
                  family maps to NAME) from the allowed set.
    Family-mapping: include any registered strategy whose family matches an
    allowed family name.
    """
    sel = get_allowed(symbol, ctx)
    vetoes = {s[1:] for s in sel if isinstance(s, str) and s.startswith("-")}
    sel = sel - {f"-{v}" for v in vetoes}
    if "*" in sel:
        sel = (sel - {"*"}) | set(all_strategies)
    # Family-mapping
    expanded = set(sel)
    for s in all_strategies:
        fam = variant_to_family(s)
        if fam in sel:
            expanded.add(s)
    # Apply vetoes — remove vetoed family names AND any variant that maps to
    # a vetoed family.
    if vetoes:
        kept = set()
        for s in expanded:
            fam = variant_to_family(s)
            if s in vetoes or fam in vetoes:
                continue
            kept.add(s)
        expanded = kept
    return expanded
