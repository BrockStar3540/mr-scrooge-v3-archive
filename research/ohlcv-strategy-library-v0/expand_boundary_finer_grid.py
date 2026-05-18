"""Finer-grid boundary-widening pass on already-productive parents.

Brock 2026-05-18: scale boundary_thin -- the engine that worked. Re-run
with finer grid (+1%, +2%, +3%, +5%, +7%) ONLY on parents that produced
strict or near-miss winners in the first pass. We avoid re-scanning the
2,102-target universe and focus compute on the seam that produced 92%
hit rate.

Input: strict + near-miss winners from the batch run -- each row already
carries the parent_rule and which factor was widened.

For each productive parent (regime, pair, direction, cell_strategy):
  For each numeric clause in the parent shave_rule:
    For each widen_pct in (0.01, 0.02, 0.03, 0.05, 0.07):
      Replay; tier as strict/near_miss/dead.

Output: refined_boundary_widening_winners.csv with the finer-grid results.
The finer grid lets us find which widening step is the TRUE edge boundary
rather than just confirming +5% works.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

CORPUS_PATH = Path(
    "/Users/brock-mini-mac/scrooge-research/routing-table-v2/ml_training_corpus.parquet"
)

FACTOR_ALIAS = {"price_pos": "close_pos"}
NUMERIC_FACTORS = {"ATR_ratio", "BB_compress", "ADX14", "RSI14", "bb_position",
                   "volume_ratio", "close_pos"}
_RULE_RE = re.compile(r"^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$")

STRICT_MIN_N = 10
STRICT_MIN_WR = 0.65
NEAR_MIN_N = 8
NEAR_MIN_WR = 0.55

WIDEN_GRID = (0.01, 0.02, 0.03, 0.05, 0.07)


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


def parse_rule(rule):
    out = []
    if not isinstance(rule, str):
        return out
    for raw in rule.split(" AND "):
        m = _RULE_RE.match(raw.strip())
        if not m:
            continue
        feat, op, val = m.group(1), m.group(2), m.group(3)
        feat = FACTOR_ALIAS.get(feat, feat)
        op = "==" if op == "=" else op
        if feat == "session_bucket":
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


def serialize(clauses):
    parts = []
    for f, op, v in clauses:
        if isinstance(v, str):
            parts.append(f"{f}{op}{v}")
        else:
            parts.append(f"{f}{op}{v}")
    return " AND ".join(parts)


def apply_rule(df, clauses):
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
            mask &= (col.astype(str) == str(val)) if op == "==" else (col.astype(str) != str(val))
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


def wilson_lb(wins, n, z=1.28):
    if n == 0:
        return 0.0
    p = wins / n
    z2 = z * z
    denom = 1 + z2 / n
    center = (p + z2 / (2 * n)) / denom
    half = z * np.sqrt((p * (1 - p) + z2 / (4 * n)) / n) / denom
    return max(0.0, center - half)


def widen(op, thr, pct):
    delta = abs(thr) * pct
    if op in ("<=", "<"): return thr + delta
    if op in (">=", ">"): return thr - delta
    return thr


def dedup_probe(parent):
    if "source" in parent.columns:
        t = parent[parent["source"] == "trainer"]
        nt = parent[parent["source"] != "trainer"]
        if len(t):
            t = t.drop_duplicates(subset=["entry_ts", "strategy_id", "pair", "direction"])
        return pd.concat([nt, t], ignore_index=True)
    return parent


def classify(n, wr):
    if n >= STRICT_MIN_N and wr >= STRICT_MIN_WR: return "strict_winner"
    if n >= NEAR_MIN_N and wr >= NEAR_MIN_WR: return "near_miss_candidate"
    return "dead"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--productive-parents", required=True,
                   help="CSV of strict + near-miss winners from previous batch")
    p.add_argument("--out-dir", required=True)
    args = p.parse_args()

    parents = pd.read_csv(args.productive_parents)
    # Keep only boundary_thin productive (the engine we're scaling)
    bt = parents[parents["queue"] == "boundary_thin"].copy()
    bt = bt[bt["outcome_tier"].isin(["strict_winner", "near_miss_candidate"])]
    # Use parent_rule (the original cell's shave_rule) as the basis
    bt = bt.dropna(subset=["parent_rule", "cell_strategy"])
    print(f"Productive boundary_thin parents: {len(bt):,}")

    # Dedup parents -- one (regime, pair, direction, cell_strategy, parent_rule) per
    parent_keys = ["regime53", "pair", "direction", "cell_strategy", "parent_rule"]
    parents_uniq = bt.drop_duplicates(subset=parent_keys)
    print(f"Unique parents: {len(parents_uniq):,}")

    print(f"Loading corpus: {CORPUS_PATH}")
    corpus = pq.read_table(
        CORPUS_PATH,
        columns=["source","strategy_id","pair","direction","entry_ts",
                 "is_win","technical_regime_53","hour_utc",
                 "ATR_ratio","BB_compress","ADX14","RSI14",
                 "bb_position","volume_ratio","close_pos"],
    ).to_pandas()
    corpus["session_bucket"] = corpus["hour_utc"].map(session_bucket_for_hour)
    print(f"  corpus: {len(corpus):,} rows")

    out_rows = []
    for i, par in parents_uniq.iterrows():
        if i % 100 == 0:
            print(f"  parent {i} ...")
        regime = par["regime53"]
        pair = par["pair"]
        direction = par["direction"]
        strat = par["cell_strategy"]
        rule = par["parent_rule"]

        sub = corpus[
            (corpus["technical_regime_53"] == regime)
            & (corpus["pair"] == pair)
            & (corpus["direction"] == direction)
            & (corpus["strategy_id"] == strat)
        ]
        sub = dedup_probe(sub)
        clauses = parse_rule(rule)
        if not clauses:
            continue

        # For each numeric clause, try every widen_pct
        for idx, (feat, op, val) in enumerate(clauses):
            if feat == "session_bucket" or feat == "hour_utc":
                continue
            if not isinstance(val, (int, float)):
                continue
            for pct in WIDEN_GRID:
                widened = list(clauses)
                widened[idx] = (feat, op, widen(op, float(val), pct))
                mask = apply_rule(sub, widened)
                matched = sub[mask]
                n = len(matched)
                w = int(matched["is_win"].sum()) if n else 0
                wr = w / n if n else 0.0
                lb = wilson_lb(w, n)
                tier = classify(n, wr)
                out_rows.append({
                    "regime53": regime, "pair": pair, "direction": direction,
                    "cell_strategy": strat, "family": par.get("family"),
                    "session_bucket": par.get("session_bucket"),
                    "widened_feature": feat, "widened_op": op,
                    "parent_threshold": float(val), "widen_pct": pct,
                    "new_threshold": float(widen(op, float(val), pct)),
                    "child_rule": serialize(widened),
                    "n_unique": n, "wins_unique": w,
                    "wr_unique": round(wr, 4), "wilson_lb": round(lb, 4),
                    "outcome_tier": tier,
                    "parent_rule": rule,
                })

    df = pd.DataFrame(out_rows)
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "finer_grid_boundary_widening_all.csv", index=False)
    strict = df[df.outcome_tier == "strict_winner"]
    near = df[df.outcome_tier == "near_miss_candidate"]
    strict.to_csv(out / "finer_grid_strict_winners.csv", index=False)
    near.to_csv(out / "finer_grid_near_miss.csv", index=False)
    print(f"\nFiner grid totals: {len(df):,} candidates evaluated")
    print(f"  strict: {len(strict):,}")
    print(f"  near:   {len(near):,}")
    print(f"  dead:   {(df.outcome_tier == 'dead').sum():,}")

    # By widen_pct: which step works best at finer grain?
    print("\nBy widen_pct (productive rate):")
    print("  pct |  total |  strict |  near  | hit_rate | avg_wr")
    for pct in WIDEN_GRID:
        g = df[df.widen_pct == pct]
        s = (g.outcome_tier == "strict_winner").sum()
        n = (g.outcome_tier == "near_miss_candidate").sum()
        hit = (s + n) / len(g) if len(g) else 0
        avg_wr = g[g.outcome_tier.isin(["strict_winner","near_miss_candidate"])].wr_unique.mean() if (s+n) else 0
        print(f"  {pct:.2f} | {len(g):>6d} | {s:>6d} | {n:>5d} | {hit:>7.1%} | {avg_wr:.3f}")


if __name__ == "__main__":
    main()
