"""Telemetry-driven seed/island expansion.

Brock 2026-05-18: each live-blocked candidate identifies a specific
(regime, pair, family, direction, session) tuple where the routing
surface has a gap or a near-miss. Mine the corpus targeted at those
exact tuples, generate child rules, classify as winner / false-friend /
reject, and emit candidate cells for v10.

Three queues, each driven by a target CSV produced by
extract_expansion_targets.py:

  A. live_gap (no_match)   -- no cell anywhere at this tuple
     Approach: extract trades from the corpus matching the tuple. If
     enough trades exist, fit a depth-2 decision tree on (ATR_ratio,
     BB_compress, ADX14, RSI14, bb_position, volume_ratio) and find
     the highest-WR leaf with n_unique >= 10.

  B. boundary_thin         -- cell exists, shave_rule misses by <10%
     Approach: take the cell's shave_rule, widen the violated threshold
     by 5/10/15% in the violating direction. Replay each variant on the
     corpus. If WR holds at >=0.70 and n_unique >= 10, emit as
     boundary_widen sibling.

  C. session_sibling       -- cell exists but for the wrong session
     Approach: take the cell's shave_rule, substitute session_bucket
     equality to the candidate's session. Replay. If WR holds, emit as
     session_sibling.

Output: one winner CSV per queue + a unified expansion_winners.csv that
can be fed to a v10 routing-table builder.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

CORPUS_PATH = Path(
    "/Users/brock-mini-mac/scrooge-research/routing-table-v2/ml_training_corpus.parquet"
)

FACTOR_COLS = ["ATR_ratio", "BB_compress", "ADX14", "RSI14", "bb_position", "volume_ratio"]
FACTOR_ALIAS = {"price_pos": "close_pos"}
NUMERIC_FACTORS = FACTOR_COLS + ["close_pos", "hour_utc"]

FAMILY_MAP = {
    "alpha_pullback_v2": "dbb_trend",
    "alpha_breakout_retest_v2": "direct",
    "alpha_extended_fade_v2": "reversal",
    "echo_box_fade_v2": "reversal",
    "echo_failed_breakout_v2": "reversal",
    "charlie_pullback_continuation_v2": "dbb_trend",
    "charlie_compression_breakout": "direct",
    "bravo_failed_momentum": "reversal",
    "bravo_expansion_continuation": "dbb_trend",
    "delta_tag_and_go_v2": "direct",
}
TEXTBOOK_FAMILY = {
    "TF": "dbb_trend", "MR": "reversal", "BR": "direct", "CP": "direct",
    "FB": "reversal", "HY": "direct", "MO": "reversal",
    "RG": "direct", "SS": "direct",
}


def family_for(strategy_id: str) -> str:
    if strategy_id in FAMILY_MAP:
        return FAMILY_MAP[strategy_id]
    m = re.match(r"^([A-Z]+)\d", strategy_id)
    if m and m.group(1) in TEXTBOOK_FAMILY:
        return TEXTBOOK_FAMILY[m.group(1)]
    return "unknown"


def wilson_lb(wins: int, n: int, z: float = 1.28) -> float:
    if n == 0:
        return 0.0
    p = wins / n
    z2 = z * z
    denom = 1 + z2 / n
    center = (p + z2 / (2 * n)) / denom
    half = z * np.sqrt((p * (1 - p) + z2 / (4 * n)) / n) / denom
    return max(0.0, center - half)


_RULE_RE = re.compile(r"^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$")


def parse_rule(rule: str) -> list[tuple[str, str, object]]:
    out = []
    if not rule:
        return out
    for raw in rule.split(" AND "):
        m = _RULE_RE.match(raw.strip())
        if not m:
            continue
        feat, op, val = m.group(1), m.group(2), m.group(3)
        feat = FACTOR_ALIAS.get(feat, feat)
        op = "==" if op == "=" else op
        if feat in ("session_bucket",):
            v: object = val.strip("\"'")
        elif feat == "hour_utc":
            try:
                v = int(float(val))
            except ValueError:
                continue
        else:
            try:
                v = float(val)
            except ValueError:
                continue
        out.append((feat, op, v))
    return out


def serialize_rule(clauses: list[tuple[str, str, object]]) -> str:
    out = []
    for f, op, v in clauses:
        if isinstance(v, str):
            out.append(f"{f}{op}{v}")
        else:
            out.append(f"{f}{op}{v}")
    return " AND ".join(out)


def apply_rule(df: pd.DataFrame, clauses: list) -> pd.Series:
    if not clauses:
        return pd.Series(False, index=df.index)
    mask = pd.Series(True, index=df.index)
    for feat, op, val in clauses:
        feat = FACTOR_ALIAS.get(feat, feat)
        if feat == "session_bucket":
            if "session_bucket" in df.columns:
                col = df["session_bucket"]
            elif "hour_utc" in df.columns:
                col = df["hour_utc"].map(session_bucket_for_hour)
            else:
                return pd.Series(False, index=df.index)
            if op == "==":
                mask &= col.astype(str) == str(val)
            else:
                mask &= col.astype(str) != str(val)
            continue
        if feat not in df.columns:
            return pd.Series(False, index=df.index)
        num = pd.to_numeric(df[feat], errors="coerce")
        mask &= num.notna()
        if op == "<=": mask &= num <= val
        elif op == ">=": mask &= num >= val
        elif op == "<":  mask &= num <  val
        elif op == ">":  mask &= num >  val
        elif op == "==": mask &= num == val
    return mask


def session_bucket_for_hour(h):
    try:
        h = int(h)
    except (TypeError, ValueError):
        return None
    if   0 <= h < 4:   return "asia"
    elif 4 <= h < 6:   return "asia_late"
    elif 6 <= h < 9:   return "london_open"
    elif 9 <= h < 13:  return "ny_open"
    elif 13 <= h < 17: return "ny_mid"
    elif 17 <= h < 21: return "ny_close"
    else:              return "off_hours"


def dedup_probe(parent: pd.DataFrame) -> pd.DataFrame:
    """Remove 2x duplication for source=trainer rows."""
    if "source" in parent.columns:
        textbook = parent[parent["source"] == "textbook"]
        trainer = parent[parent["source"] == "trainer"]
        if len(trainer):
            trainer = trainer.drop_duplicates(
                subset=["entry_ts", "strategy_id", "pair", "direction"],
            )
        return pd.concat([textbook, trainer], ignore_index=True)
    return parent


def score(matched: pd.DataFrame) -> dict:
    n = len(matched)
    wins = int(matched["is_win"].sum()) if n else 0
    losses = n - wins
    wr = wins / n if n else 0.0
    return {
        "n_unique": n,
        "wins_unique": wins,
        "losses_unique": losses,
        "wr_unique": wr,
        "wilson_lb": wilson_lb(wins, n),
    }


# ---------------------------------------------------------------------------
# Queue A: live_gap (no_match)
# ---------------------------------------------------------------------------

def expand_live_gap(targets: pd.DataFrame, corpus: pd.DataFrame, min_n: int = 10,
                    min_wr: float = 0.70) -> pd.DataFrame:
    if targets.empty:
        return pd.DataFrame()
    out = []
    for _, t in targets.iterrows():
        sub = corpus[
            (corpus["technical_regime_53"] == t["regime53"])
            & (corpus["pair"] == t["symbol"])
            & (corpus["direction"] == t["direction"])
        ]
        sub = dedup_probe(sub)
        # filter to candidates whose strategy maps to the requested family
        sub = sub[sub["strategy_id"].map(family_for) == t["candidate_family"]]
        if "session_bucket" not in sub.columns and "hour_utc" in sub.columns:
            sub = sub.copy()
            sub["session_bucket"] = sub["hour_utc"].map(session_bucket_for_hour)
        if "session_bucket" in sub.columns:
            sub = sub[sub["session_bucket"] == t["session_bucket"]]
        if len(sub) < min_n:
            continue
        # depth-2 split: find best single-factor threshold that maximizes WR
        # within the tuple, subject to n >= min_n in the kept side
        best = None
        for feat in NUMERIC_FACTORS:
            if feat not in sub.columns:
                continue
            vals = pd.to_numeric(sub[feat], errors="coerce").dropna()
            if len(vals) < min_n * 2:
                continue
            for q in [0.25, 0.50, 0.75]:
                thr = float(vals.quantile(q))
                for op in ("<=", ">"):
                    if op == "<=":
                        cm = pd.to_numeric(sub[feat], errors="coerce") <= thr
                    else:
                        cm = pd.to_numeric(sub[feat], errors="coerce") > thr
                    kept = sub[cm]
                    if len(kept) < min_n:
                        continue
                    s = score(kept)
                    if s["wr_unique"] < min_wr:
                        continue
                    cand = {**s, "feat": feat, "op": op, "thr": thr}
                    if best is None or s["wilson_lb"] > best["wilson_lb"]:
                        best = cand
        if best:
            out.append({
                "queue": "live_gap",
                "regime53": t["regime53"], "pair": t["symbol"],
                "session_bucket": t["session_bucket"], "direction": t["direction"],
                "family": t["candidate_family"],
                "child_rule": f"{best['feat']}{best['op']}{best['thr']:.6g}",
                "n_unique": best["n_unique"], "wins_unique": best["wins_unique"],
                "wr_unique": best["wr_unique"], "wilson_lb": best["wilson_lb"],
                "source_strategy": "synthesized_from_corpus",
            })
    return pd.DataFrame(out)


# ---------------------------------------------------------------------------
# Queue B: boundary_thin
# ---------------------------------------------------------------------------

def widen_threshold(op: str, thr: float, pct: float, observed: float | None) -> float:
    """Move threshold so that the previously-rejected `observed` value passes.

    For `<=`: thr was too low; widen UP by pct, but at minimum past observed.
    For `>=`: thr was too high; widen DOWN by pct, at minimum below observed.
    """
    delta = abs(thr) * pct
    if op in ("<=", "<"):
        new = thr + delta
        if observed is not None:
            new = max(new, observed + delta * 0.1)
        return new
    if op in (">=", ">"):
        new = thr - delta
        if observed is not None:
            new = min(new, observed - delta * 0.1)
        return new
    return thr


def expand_boundary_thin(targets: pd.DataFrame, corpus: pd.DataFrame,
                         min_n: int = 10, min_wr: float = 0.65) -> pd.DataFrame:
    if targets.empty:
        return pd.DataFrame()
    out = []
    for _, t in targets.iterrows():
        rule = t.get("shadow_shave_rule") or ""
        clauses = parse_rule(rule)
        if not clauses:
            continue
        v_feat = t.get("violated_feature")
        v_op = t.get("violated_op")
        v_thr = t.get("violated_threshold")
        v_obs = t.get("violated_observed")

        sub = corpus[
            (corpus["technical_regime_53"] == t["regime53"])
            & (corpus["pair"] == t["symbol"])
            & (corpus["direction"] == t["direction"])
        ]
        # Filter to the specific strategy_id the shave_rule was fit to,
        # not just family. Without this we re-score the rule against an
        # 8x-larger sample of other strategies and dilute the edge.
        cell_strategy = t.get("shadow_cell_strategy")
        if cell_strategy:
            sub = sub[sub["strategy_id"] == cell_strategy]
        sub = dedup_probe(sub)
        if "session_bucket" not in sub.columns and "hour_utc" in sub.columns:
            sub = sub.copy()
            sub["session_bucket"] = sub["hour_utc"].map(session_bucket_for_hour)

        for pct in (0.05, 0.10, 0.15):
            widened = []
            for f, op, val in clauses:
                if f == v_feat and op == v_op and isinstance(val, (int, float)):
                    new_thr = widen_threshold(op, float(val), pct, v_obs if isinstance(v_obs, (int, float)) else None)
                    widened.append((f, op, new_thr))
                else:
                    widened.append((f, op, val))
            mask = apply_rule(sub, widened)
            matched = sub[mask]
            s = score(matched)
            if s["n_unique"] >= min_n and s["wr_unique"] >= min_wr:
                out.append({
                    "queue": "boundary_thin",
                    "regime53": t["regime53"], "pair": t["symbol"],
                    "session_bucket": t["session_bucket"], "direction": t["direction"],
                    "family": t["candidate_family"],
                    "child_rule": serialize_rule(widened),
                    "n_unique": s["n_unique"], "wins_unique": s["wins_unique"],
                    "wr_unique": s["wr_unique"], "wilson_lb": s["wilson_lb"],
                    "source_strategy": "boundary_widen",
                    "widen_pct": pct,
                    "parent_rule": rule,
                })
                break  # take the tightest widening that works
    return pd.DataFrame(out)


# ---------------------------------------------------------------------------
# Queue C: session_sibling
# ---------------------------------------------------------------------------

def expand_session_sibling(targets: pd.DataFrame, corpus: pd.DataFrame,
                           min_n: int = 10, min_wr: float = 0.65) -> pd.DataFrame:
    if targets.empty:
        return pd.DataFrame()
    out = []
    for _, t in targets.iterrows():
        rule = t.get("shadow_shave_rule") or ""
        clauses = parse_rule(rule)
        if not clauses:
            continue
        new_session = t.get("candidate_session")
        if not new_session:
            continue
        # replace session_bucket clause
        sibling = []
        for f, op, val in clauses:
            if f == "session_bucket":
                sibling.append((f, "==", new_session))
            else:
                sibling.append((f, op, val))

        sub = corpus[
            (corpus["technical_regime_53"] == t["regime53"])
            & (corpus["pair"] == t["symbol"])
            & (corpus["direction"] == t["direction"])
        ]
        cell_strategy = t.get("shadow_cell_strategy")
        if cell_strategy:
            sub = sub[sub["strategy_id"] == cell_strategy]
        sub = dedup_probe(sub)
        if "session_bucket" not in sub.columns and "hour_utc" in sub.columns:
            sub = sub.copy()
            sub["session_bucket"] = sub["hour_utc"].map(session_bucket_for_hour)

        mask = apply_rule(sub, sibling)
        matched = sub[mask]
        s = score(matched)
        if s["n_unique"] >= min_n and s["wr_unique"] >= min_wr:
            out.append({
                "queue": "session_sibling",
                "regime53": t["regime53"], "pair": t["symbol"],
                "session_bucket": new_session, "direction": t["direction"],
                "family": t["candidate_family"],
                "child_rule": serialize_rule(sibling),
                "n_unique": s["n_unique"], "wins_unique": s["wins_unique"],
                "wr_unique": s["wr_unique"], "wilson_lb": s["wilson_lb"],
                "source_strategy": "session_substitute",
                "parent_rule": rule,
                "parent_session": t.get("cell_session"),
            })
    return pd.DataFrame(out)


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--targets-dir", required=True)
    p.add_argument("--out-dir", required=True)
    args = p.parse_args()

    targets_dir = Path(args.targets_dir)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    def _maybe(p):
        if not p.exists() or p.stat().st_size == 0:
            return pd.DataFrame()
        try:
            return pd.read_csv(p)
        except pd.errors.EmptyDataError:
            return pd.DataFrame()

    no_match_t = _maybe(targets_dir / "live_gap_expansion_targets.csv")
    boundary_t = _maybe(targets_dir / "boundary_thin_targets.csv")
    session_t  = _maybe(targets_dir / "session_sibling_targets.csv")

    print(f"targets loaded: no_match={len(no_match_t)} boundary={len(boundary_t)} session={len(session_t)}")
    print(f"Loading corpus: {CORPUS_PATH} ...")
    corpus = pq.read_table(
        CORPUS_PATH,
        columns=["source","strategy_id","pair","direction","entry_ts",
                 "is_win","technical_regime_53","hour_utc",
                 "ATR_ratio","BB_compress","ADX14","RSI14",
                 "bb_position","volume_ratio","close_pos"],
    ).to_pandas()
    print(f"  corpus rows: {len(corpus):,}")

    print("Queue A: live_gap ...")
    a = expand_live_gap(no_match_t, corpus)
    print(f"  -> {len(a)} winners")
    print("Queue B: boundary_thin ...")
    b = expand_boundary_thin(boundary_t, corpus)
    print(f"  -> {len(b)} winners")
    print("Queue C: session_sibling ...")
    c = expand_session_sibling(session_t, corpus)
    print(f"  -> {len(c)} winners")

    a.to_csv(out / "expansion_winners_live_gap.csv", index=False)
    b.to_csv(out / "expansion_winners_boundary_thin.csv", index=False)
    c.to_csv(out / "expansion_winners_session_sibling.csv", index=False)
    non_empty = [df for df in [a, b, c] if not df.empty]
    all_w = pd.concat(non_empty, ignore_index=True) if non_empty else pd.DataFrame()
    all_w.to_csv(out / "expansion_winners_all.csv", index=False)
    print(f"\nTotal winners: {len(all_w)}")
    print(f"  -> {out}/expansion_winners_all.csv")


if __name__ == "__main__":
    main()
