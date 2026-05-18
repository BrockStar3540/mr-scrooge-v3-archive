"""Batch target synthesizer -- generate expansion targets from existing
banks instead of (or in parallel with) live telemetry.

Brock 2026-05-18: don't be hostage to waiting for live blocked rows.
Pre-identified expansion targets already exist in v9_observe:

  session_sibling   for each cell with session_bucket==X, try the same
                    rule at each of the other 6 sessions

  boundary_thin     for each numeric threshold in each cell's shave_rule,
                    test widened variants (5/10/15%)

  live_gap          for every (regime, pair, session, direction, family)
                    tuple not currently covered by a Seed+ cell, attempt
                    a fresh corpus-driven fit

Outputs the same target-CSV schema as extract_expansion_targets.py, so
expand_telemetry_driven.py runs unchanged.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd

SESSION_BUCKETS = ("asia", "asia_late", "london_open", "ny_open",
                   "ny_mid", "ny_close", "off_hours")
ALL_PAIRS = []  # filled at runtime from v9_observe
ALL_REGIMES = ["C01", "C02"]  # the regimes the seed factory mined
FAMILIES = ["dbb_trend", "direct", "reversal"]
DIRECTIONS = ["long", "short"]

_RULE_RE = re.compile(r"^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$")


def parse_rule(rule: str):
    out = []
    if not isinstance(rule, str):
        return out
    for raw in rule.split(" AND "):
        m = _RULE_RE.match(raw.strip())
        if not m:
            continue
        feat, op, val = m.group(1), m.group(2), m.group(3)
        op = "==" if op == "=" else op
        try:
            fval: object = float(val)
        except ValueError:
            fval = val
        out.append((feat, op, fval))
    return out


def synthesize_session_siblings(v9: pd.DataFrame) -> pd.DataFrame:
    rows = []
    # de-session-expand so we don't generate 7x duplicates
    base = v9.drop_duplicates(subset=["sub_regime", "pair", "strategy", "direction"])
    for _, c in base.iterrows():
        if not isinstance(c.get("shave_rule"), str):
            continue
        clauses = parse_rule(c["shave_rule"])
        cell_session = None
        for f, op, v in clauses:
            if f == "session_bucket" and op == "==":
                cell_session = v
                break
        # If the rule has no session clause, sibling expansion is moot;
        # the rule already applies to all sessions.
        if cell_session is None:
            continue
        if cell_session not in SESSION_BUCKETS:
            continue
        for other in SESSION_BUCKETS:
            if other == cell_session:
                continue
            rows.append({
                "ts": "synth",
                "symbol": c["pair"],
                "regime53": c.get("technical_regime_53") or c.get("parent_regime"),
                "session_bucket": other,
                "direction": c["direction"],
                "candidate_family": c.get("family"),
                "live_block_reason": "synth_batch_session_sibling",
                "shadow_reason": f"shave_rule_violated: session_bucket == {cell_session} (got {other})",
                "shadow_cell": f"{c.get('technical_regime_53')}|{c['pair']}|{other}",
                "shadow_cell_strategy": c["strategy"],
                "shadow_cell_family": c.get("family"),
                "shadow_shave_rule": c["shave_rule"],
                "shadow_factors": "{}",
                "violated_feature": "session_bucket",
                "violated_op": "==",
                "violated_threshold": "",
                "violated_observed": "",
                "delta_pct_of_thr": "",
                "cell_session": cell_session,
                "candidate_session": other,
            })
    return pd.DataFrame(rows)


def synthesize_boundary_thin(v9: pd.DataFrame) -> pd.DataFrame:
    rows = []
    base = v9.drop_duplicates(subset=["sub_regime", "pair", "strategy", "direction"])
    for _, c in base.iterrows():
        if not isinstance(c.get("shave_rule"), str):
            continue
        clauses = parse_rule(c["shave_rule"])
        for feat, op, val in clauses:
            if feat == "session_bucket" or not isinstance(val, (int, float)):
                continue
            # synthesize an observed value just outside the threshold
            delta = abs(val) * 0.05 if abs(val) > 0 else 0.001
            if op == "<=":
                observed = val + delta
            elif op == "<":
                observed = val + delta
            elif op == ">=":
                observed = val - delta
            elif op == ">":
                observed = val - delta
            else:
                continue
            rows.append({
                "ts": "synth",
                "symbol": c["pair"],
                "regime53": c.get("technical_regime_53") or c.get("parent_regime"),
                "session_bucket": c.get("session_bucket", "any"),
                "direction": c["direction"],
                "candidate_family": c.get("family"),
                "live_block_reason": "synth_batch_boundary_thin",
                "shadow_reason": f"shave_rule_violated: {feat} {op} {val} (got {observed:.6g})",
                "shadow_cell": f"{c.get('technical_regime_53')}|{c['pair']}|{c.get('session_bucket','any')}",
                "shadow_cell_strategy": c["strategy"],
                "shadow_cell_family": c.get("family"),
                "shadow_shave_rule": c["shave_rule"],
                "shadow_factors": json.dumps({feat: float(observed)}),
                "violated_feature": feat,
                "violated_op": op,
                "violated_threshold": val,
                "violated_observed": observed,
                "delta_pct_of_thr": 0.05,
            })
    return pd.DataFrame(rows)


def synthesize_live_gaps(v9: pd.DataFrame) -> pd.DataFrame:
    """Tuples (regime, pair, session, direction, family) not covered by any
    Seed+ cell in v9_observe."""
    # Universe of pairs comes from v9_observe (pairs that have ANY cell)
    pairs = sorted(v9["pair"].unique().tolist())
    seed_plus = v9[v9["tier"].isin(["Seed", "Seed-Pro", "Pro", "Elite"])]
    covered_tuples = set(
        zip(
            seed_plus["parent_regime"].astype(str),
            seed_plus["pair"].astype(str),
            seed_plus["session_bucket"].astype(str),
            seed_plus["direction"].astype(str),
            seed_plus["family"].astype(str),
        )
    )
    rows = []
    for regime in ALL_REGIMES:
        for pair in pairs:
            for sess in SESSION_BUCKETS:
                for direction in DIRECTIONS:
                    for fam in FAMILIES:
                        key = (regime, pair, sess, direction, fam)
                        if key in covered_tuples:
                            continue
                        rows.append({
                            "ts": "synth",
                            "symbol": pair,
                            "regime53": regime,
                            "session_bucket": sess,
                            "direction": direction,
                            "candidate_family": fam,
                            "live_block_reason": "synth_batch_live_gap",
                            "shadow_reason": "synth_batch_live_gap",
                        })
    return pd.DataFrame(rows)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--v9-observe", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--max-live-gap", type=int, default=200,
                   help="Cap on synthesized live_gap targets (full universe is 10k+)")
    args = p.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    v9 = pd.read_parquet(args.v9_observe)
    print(f"v9_observe: {len(v9)} rows, {v9['pair'].nunique()} pairs, "
          f"{v9['strategy'].nunique()} strategies, "
          f"tiers={v9.tier.value_counts().to_dict()}")

    ss = synthesize_session_siblings(v9)
    bt = synthesize_boundary_thin(v9)
    lg = synthesize_live_gaps(v9)

    # Cap live_gap to avoid blowing the corpus query loop
    if len(lg) > args.max_live_gap:
        lg = lg.sample(args.max_live_gap, random_state=42)

    ss.to_csv(out / "session_sibling_targets.csv", index=False)
    bt.to_csv(out / "boundary_thin_targets.csv", index=False)
    lg.to_csv(out / "live_gap_expansion_targets.csv", index=False)

    print(f"\nSynthesized targets:")
    print(f"  session_sibling : {len(ss):>5d} -> session_sibling_targets.csv")
    print(f"  boundary_thin   : {len(bt):>5d} -> boundary_thin_targets.csv")
    print(f"  live_gap        : {len(lg):>5d} -> live_gap_expansion_targets.csv (capped)")


if __name__ == "__main__":
    main()
