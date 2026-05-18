"""OOS validator for the 1,001 strict winners from the batch expansion.

Brock 2026-05-18 doctrine: a strict winner is in-sample. Before promotion
into routing_table_v10_trade, every rule must replay on a held-out time
window and hold above a minimum WR. The 2025-01-01 cutover is consistent
with the original v3 OOS validation (see scrooge-claude-sessions-index
2026-05-15: 122/261 islands held).

Method per cell:
  1. Slice corpus by (regime53, pair, direction, strategy_id)
  2. Dedup probe 2x inflation
  3. Apply the child_rule
  4. Split matched rows by entry_ts >= 2025-01-01 (test) vs < (train)
  5. Compute test n, wins, WR, Wilson 80% LB
  6. Classify:
       oos_strict_pass:  n_test >=  8 AND wr_test >= 0.60
       oos_loose_pass:   n_test >=  5 AND wr_test >= 0.55
       oos_thin:         n_test <   5 (cell rule rarely fires in holdout)
       oos_fail:         meets neither pass bar

For the final v10 candidate set we collapse to one row per
(regime, pair, strategy, direction) — keep the best surviving sibling
by oos_wilson_lb.
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
OOS_CUTOVER = pd.Timestamp("2025-01-01", tz="UTC")

FACTOR_ALIAS = {"price_pos": "close_pos"}
_RULE_RE = re.compile(r"^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$")


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


def parse_rule(rule: str):
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


def dedup_probe(parent):
    if "source" in parent.columns:
        t = parent[parent["source"] == "trainer"]
        nt = parent[parent["source"] != "trainer"]
        if len(t):
            t = t.drop_duplicates(subset=["entry_ts", "strategy_id", "pair", "direction"])
        return pd.concat([nt, t], ignore_index=True)
    return parent


def classify(n, wr):
    if n < 5: return "oos_thin"
    if n >= 8 and wr >= 0.60: return "oos_strict_pass"
    if n >= 5 and wr >= 0.55: return "oos_loose_pass"
    return "oos_fail"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--strict-winners", required=True)
    p.add_argument("--out-dir", required=True)
    args = p.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    print(f"Loading strict winners: {args.strict_winners}")
    cells = pd.read_csv(args.strict_winners)
    print(f"  {len(cells):,} rows")

    print(f"Loading corpus: {CORPUS_PATH}")
    corpus = pq.read_table(
        CORPUS_PATH,
        columns=["source","strategy_id","pair","direction","entry_ts",
                 "is_win","technical_regime_53","hour_utc",
                 "ATR_ratio","BB_compress","ADX14","RSI14",
                 "bb_position","volume_ratio","close_pos"],
    ).to_pandas()
    corpus["entry_ts"] = pd.to_datetime(corpus["entry_ts"], utc=True)
    print(f"  {len(corpus):,} rows | "
          f"train < {OOS_CUTOVER.date()}: {(corpus['entry_ts'] < OOS_CUTOVER).sum():,} | "
          f"test  >= {OOS_CUTOVER.date()}: {(corpus['entry_ts'] >= OOS_CUTOVER).sum():,}")
    corpus["session_bucket"] = corpus["hour_utc"].map(session_bucket_for_hour)

    rows = []
    for i, c in cells.iterrows():
        if i % 100 == 0:
            print(f"  validating {i}/{len(cells)} ...")
        # Required tuple columns: regime53, pair, direction, cell_strategy
        regime = c.get("regime53")
        pair = c.get("pair")
        direction = c.get("direction")
        strat = c.get("cell_strategy")
        rule = c.get("child_rule")
        if not all([regime, pair, direction, strat, isinstance(rule, str)]):
            continue

        sub = corpus[
            (corpus["technical_regime_53"] == regime)
            & (corpus["pair"] == pair)
            & (corpus["direction"] == direction)
            & (corpus["strategy_id"] == strat)
        ]
        sub = dedup_probe(sub)
        clauses = parse_rule(rule)
        mask = apply_rule(sub, clauses)
        matched = sub[mask]

        train = matched[matched["entry_ts"] < OOS_CUTOVER]
        test = matched[matched["entry_ts"] >= OOS_CUTOVER]
        n_train, w_train = len(train), int(train["is_win"].sum()) if len(train) else 0
        n_test, w_test = len(test), int(test["is_win"].sum()) if len(test) else 0
        wr_test = w_test / n_test if n_test else 0.0
        wr_train = w_train / n_train if n_train else 0.0
        lb_test = wilson_lb(w_test, n_test)

        rows.append({
            **{k: c.get(k) for k in ("queue","outcome_tier","regime53","pair",
                                     "family","direction","session_bucket",
                                     "cell_strategy","source_strategy","child_rule",
                                     "widen_pct","parent_rule","parent_session",
                                     "n_unique","wins_unique","wr_unique","wilson_lb")},
            "oos_n_train": n_train,
            "oos_wr_train": round(wr_train, 4),
            "oos_n_test": n_test,
            "oos_wins_test": w_test,
            "oos_wr_test": round(wr_test, 4),
            "oos_wilson_lb": round(lb_test, 4),
            "oos_status": classify(n_test, wr_test),
        })

    df = pd.DataFrame(rows)
    out_path = out / "oos_validation_strict_winners.csv"
    df.to_csv(out_path, index=False)
    print(f"\n  -> {out_path}")

    # Collapse to deployable v10 cell: one row per (regime, pair, strategy, direction)
    survivors = df[df["oos_status"].isin(["oos_strict_pass", "oos_loose_pass"])].copy()
    if not survivors.empty:
        survivors = survivors.sort_values("oos_wilson_lb", ascending=False)
        best = survivors.drop_duplicates(
            subset=["regime53", "pair", "cell_strategy", "direction"], keep="first",
        )
        best.to_csv(out / "oos_survivors_v10_candidate_cells.csv", index=False)
        print(f"  -> {out / 'oos_survivors_v10_candidate_cells.csv'} ({len(best)} cells)")

    # Quick summary
    print("\n=== OOS status counts ===")
    status_counts = df["oos_status"].value_counts().to_dict()
    for s in ["oos_strict_pass", "oos_loose_pass", "oos_thin", "oos_fail"]:
        print(f"  {s:<20s} {status_counts.get(s, 0):>5d}")

    # Pass rate breakdowns
    print("\n=== Pass rate by family ===")
    passed = df["oos_status"].isin(["oos_strict_pass", "oos_loose_pass"])
    for fam, g in df.groupby("family"):
        p = passed[g.index]
        print(f"  {fam:<12s} {p.sum():>4d} / {len(g):>4d} ({100*p.mean():.1f}%)")

    print("\n=== Pass rate by widening factor (parsed from child_rule) ===")
    def main_factor(rule):
        if not isinstance(rule, str): return None
        m = re.search(r"BB_compress|ATR_ratio|ADX14|RSI14|volume_ratio|bb_position", rule)
        return m.group(0) if m else None
    df["main_factor"] = df["child_rule"].map(main_factor)
    for f, g in df.groupby("main_factor"):
        p = passed[g.index]
        if f is None: continue
        print(f"  {f:<14s} {p.sum():>4d} / {len(g):>4d} ({100*p.mean():.1f}%)")


if __name__ == "__main__":
    main()
