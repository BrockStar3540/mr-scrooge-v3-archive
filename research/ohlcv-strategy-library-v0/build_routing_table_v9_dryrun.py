"""routing_table_v9 dry-run — corrected aggregation + tier sensitivity.

Three corrections applied vs v8:

  1. PROBE 2x INFLATION FIX. V3 probes in ml_training_corpus.parquet emit one
     row per (trade, target_R) pair (target_R in {1.5, 2.0}). Seed-family
     mining counted raw rows, so probe child n/wins are exactly 2x truth.
     We divide by 2 for source=trainer (V3 probes). Textbook is 1:1.

  2. LEGACY SESSION-BUCKET FILTER. seed_family_lineage_v2.csv uses an old
     3-bucket vocabulary (asia/london/ny) in 1,769 child rules. Those
     cannot replay against the live 7-bucket classifier. We drop them
     for this pass. v8 is already clean of this; the filter is on the
     seed-bank ingest, not on v8.

  3. TIER ON n_unique. v8 used `n >= 30 AND wr >= 0.50` for Pro; that
     thresholded 2x-inflated counts. v9 dry-run reasons on unique trade
     count and adds a "Seed" tier for promising-but-small islands.

Outputs:
  routing_table_v9_dryrun_cells.csv    one row per candidate cell
  routing_table_v9_dryrun_summary.md   counts + coverage + sensitivity
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd

# V3 probe identification — used to apply the 2x correction
V3_PROBES = {
    "alpha_pullback_v2", "alpha_breakout_retest_v2", "alpha_extended_fade_v2",
    "echo_box_fade_v2", "echo_failed_breakout_v2",
    "charlie_pullback_continuation_v2", "charlie_compression_breakout",
    "bravo_failed_momentum", "bravo_expansion_continuation",
    "delta_tag_and_go_v2",
}

# Family assignment — same as routing_table_v8 / probes_v2 wrapper module
FAMILY_MAP = {
    # V3 probes
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

# Textbook family mapping by prefix (TF=dbb_trend / MR=reversal / etc.)
TEXTBOOK_FAMILY = {
    "TF": "dbb_trend", "MR": "reversal", "BR": "direct",
    "CP": "direct", "FB": "reversal", "HY": "direct",
    "MO": "reversal", "RG": "direct", "SS": "direct",
}

LEGACY_SESSION_RE = re.compile(r"session_bucket==(london|asia|ny)(?!_)")


def family_for(strategy_id: str) -> str:
    if strategy_id in FAMILY_MAP:
        return FAMILY_MAP[strategy_id]
    m = re.match(r"^([A-Z]+)\d", strategy_id)
    if m and m.group(1) in TEXTBOOK_FAMILY:
        return TEXTBOOK_FAMILY[m.group(1)]
    return "unknown"


def wilson_lb(wins: int, n: int, z: float = 1.28) -> float:
    """Wilson lower bound on WR at confidence level z (default 80% = 1.28).

    Used as the evidence-adjusted WR for tier promotion.
    """
    if n == 0:
        return 0.0
    p = wins / n
    z2 = z * z
    denom = 1 + z2 / n
    center = (p + z2 / (2 * n)) / denom
    half = z * np.sqrt((p * (1 - p) + z2 / (4 * n)) / n) / denom
    return max(0.0, center - half)


def tier_for(wr_unique: float, n_unique: int, wr_lb: float) -> str:
    """v9 tier rule — small-but-pure aware.

    Two paths to each tier:
      * evidence path: high wr_lb (Wilson 80% LB) regardless of raw WR
      * promise path: high raw WR with adequate n_unique
    """
    if wr_lb >= 0.55 and n_unique >= 30: return "Elite"
    if wr_lb >= 0.45 and n_unique >= 30: return "Pro"
    if wr_unique >= 0.85 and n_unique >= 15: return "Seed-Pro"   # small-but-pure
    if wr_lb >= 0.35 and n_unique >= 30: return "Standard"
    if wr_unique >= 0.70 and n_unique >= 10: return "Seed"        # promising
    return "Probationary"


TIER_RANK = {
    "Elite": 5, "Pro": 4, "Seed-Pro": 3, "Standard": 2, "Seed": 1, "Probationary": 0,
}


def load_probe(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Apply 2x correction. Floor to int — half-trades don't make sense.
    df["n_unique"] = (df["n"] // 2).astype(int)
    df["wins_unique"] = (df["wins"] // 2).astype(int)
    df["losses_unique"] = df["n_unique"] - df["wins_unique"]
    df["wr_unique"] = np.where(df["n_unique"] > 0,
                               df["wins_unique"] / df["n_unique"], 0.0)
    df["source"] = "probe"
    df["family"] = df["root_strategy_id"].map(family_for)
    return df


def load_textbook(path: Path) -> tuple[pd.DataFrame, int]:
    df = pd.read_csv(path)
    if "bucket" in df.columns:
        df = df[df["bucket"].isin(["winner_seed", "near_pure_seed"])]
    legacy_mask = df["child_rule"].fillna("").str.contains(LEGACY_SESSION_RE)
    legacy_n = int(legacy_mask.sum())
    df = df[~legacy_mask].copy()
    # Textbook is 1:1 — no correction
    df["n_unique"] = df["n"].astype(int)
    df["wins_unique"] = df["wins"].astype(int)
    df["losses_unique"] = df["n_unique"] - df["wins_unique"]
    df["wr_unique"] = df["wr"]
    df["source"] = "textbook"
    df["family"] = df["root_strategy_id"].map(family_for)
    return df, legacy_n


def aggregate_to_cells(combined: pd.DataFrame) -> pd.DataFrame:
    """One winning row per (strategy, pair, direction, regime) cell.

    Selects the highest-tier child rule; ties broken by wr_lb desc then n_unique.
    """
    combined = combined.copy()
    combined["wr_lb"] = [
        wilson_lb(int(w), int(n))
        for w, n in zip(combined["wins_unique"], combined["n_unique"])
    ]
    combined["tier"] = [
        tier_for(wr, int(n), lb)
        for wr, n, lb in zip(combined["wr_unique"], combined["n_unique"], combined["wr_lb"])
    ]
    combined["tier_rank"] = combined["tier"].map(TIER_RANK)
    combined = combined.sort_values(
        ["tier_rank", "wr_lb", "wr_unique", "n_unique"], ascending=False,
    )
    cell_key = ["root_strategy_id", "pair", "direction", "technical_regime_53"]
    best = combined.drop_duplicates(subset=cell_key).reset_index(drop=True)
    return best


def coverage_table(best: pd.DataFrame) -> dict:
    """Build counts / family / pair / regime breakdowns."""
    rep: dict = {}
    rep["total_candidate_children"] = None  # filled by caller
    rep["unique_cells"] = len(best)
    rep["by_tier"] = best["tier"].value_counts().to_dict()
    rep["by_family_x_tier"] = (
        best.groupby(["family", "tier"]).size().unstack(fill_value=0)
        .reindex(columns=["Elite", "Pro", "Seed-Pro", "Standard", "Seed", "Probationary"], fill_value=0)
        .to_dict("index")
    )
    rep["by_regime_x_tier"] = (
        best.groupby(["technical_regime_53", "tier"]).size().unstack(fill_value=0)
        .reindex(columns=["Elite", "Pro", "Seed-Pro", "Standard", "Seed", "Probationary"], fill_value=0)
        .to_dict("index")
    )
    rep["pairs_covered"] = sorted(best["pair"].unique().tolist())
    rep["strategies_covered"] = sorted(best["root_strategy_id"].unique().tolist())
    return rep


def threshold_sensitivity(combined: pd.DataFrame) -> pd.DataFrame:
    """How many cells survive at different (min_n_unique, min_wr) bars."""
    combined = combined.copy()
    combined["wr_lb"] = [
        wilson_lb(int(w), int(n))
        for w, n in zip(combined["wins_unique"], combined["n_unique"])
    ]
    cell_key = ["root_strategy_id", "pair", "direction", "technical_regime_53"]
    rows = []
    for min_n in [10, 15, 20, 25, 30, 40]:
        for min_wr in [0.50, 0.60, 0.70, 0.80, 0.90]:
            qual = combined[
                (combined["n_unique"] >= min_n) & (combined["wr_unique"] >= min_wr)
            ]
            cells = qual.drop_duplicates(subset=cell_key)
            for min_lb in [0.0, 0.30, 0.40, 0.50]:
                qual2 = qual[qual["wr_lb"] >= min_lb].drop_duplicates(subset=cell_key)
                rows.append({
                    "min_n_unique": min_n,
                    "min_wr_raw": min_wr,
                    "min_wr_lb": min_lb,
                    "cells": len(qual2),
                })
    return pd.DataFrame(rows)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--probe-winners", required=True)
    p.add_argument("--textbook", required=True)
    p.add_argument("--v8-parquet", required=True,
                   help="data/routing_table_v8.parquet for comparison")
    p.add_argument("--out-dir", required=True)
    args = p.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    print("=== Loading inputs ===")
    probe = load_probe(Path(args.probe_winners))
    text, legacy_dropped = load_textbook(Path(args.textbook))
    print(f"  probe children: {len(probe):,} rows (2x-corrected)")
    print(f"  textbook children: {len(text):,} (kept) + {legacy_dropped:,} legacy-vocab dropped")

    common = ["source", "root_strategy_id", "family", "pair", "direction",
              "technical_regime_53", "child_rule",
              "n_unique", "wins_unique", "losses_unique", "wr_unique",
              "purity_gain"]
    combined = pd.concat([probe[common], text[common]], ignore_index=True)
    print(f"  combined candidate children: {len(combined):,}")

    print("\n=== Aggregating to cells ===")
    best = aggregate_to_cells(combined)
    cells_path = out / "routing_table_v9_dryrun_cells.csv"
    best.to_csv(cells_path, index=False)
    print(f"  unique cells: {len(best):,}")
    print(f"  -> {cells_path}")

    # Coverage
    rep = coverage_table(best)
    rep["total_candidate_children"] = len(combined)
    rep["legacy_session_dropped"] = legacy_dropped

    # Threshold sensitivity
    print("\n=== Threshold sensitivity ===")
    sens = threshold_sensitivity(combined)
    sens_path = out / "routing_table_v9_dryrun_sensitivity.csv"
    sens.to_csv(sens_path, index=False)
    print(f"  -> {sens_path}")

    # v8 comparison
    print("\n=== v8 comparison ===")
    v8 = pd.read_parquet(args.v8_parquet)
    v8_base = v8.drop_duplicates(subset=["sub_regime", "pair", "strategy", "direction"])
    v8_at_parent = v8_base.drop_duplicates(subset=["parent_regime", "pair", "strategy", "direction"])
    v8_tiers = v8_at_parent["tier"].value_counts().to_dict()

    # Summary MD
    md: list[str] = []
    md.append("# routing_table_v9 dry-run summary")
    md.append("")
    md.append(f"**Generated**: {pd.Timestamp.now(tz='UTC').isoformat()}")
    md.append("")
    md.append("## Inputs")
    md.append("")
    md.append(f"- Probe seed-family children: **{len(probe):,}** rows (2x correction applied for V3 probes)")
    md.append(f"- Textbook seed-family children: **{len(text):,}** rows (after dropping **{legacy_dropped:,}** with legacy session-bucket vocabulary)")
    md.append(f"- Combined candidate universe: **{len(combined):,}** child rules")
    md.append(f"- Unique cells after best-per-cell aggregation: **{len(best):,}**")
    md.append("")
    md.append("## Tier distribution (v9 dry-run vs v8)")
    md.append("")
    md.append("| Tier | v9 dry-run cells | v8 cells (parent-regime) | Delta |")
    md.append("|---|---:|---:|---:|")
    for tier in ["Elite", "Pro", "Seed-Pro", "Standard", "Seed", "Probationary"]:
        v9c = rep["by_tier"].get(tier, 0)
        v8c = v8_tiers.get(tier, 0)
        md.append(f"| {tier} | {v9c} | {v8c} | {v9c - v8c:+d} |")
    md.append("")
    md.append("## Family × Tier (v9)")
    md.append("")
    md.append("| Family | Elite | Pro | Seed-Pro | Standard | Seed | Probationary | Total |")
    md.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for fam, row in rep["by_family_x_tier"].items():
        total = sum(row.values())
        md.append(f"| {fam} | {row.get('Elite',0)} | {row.get('Pro',0)} | {row.get('Seed-Pro',0)} | "
                  f"{row.get('Standard',0)} | {row.get('Seed',0)} | {row.get('Probationary',0)} | {total} |")
    md.append("")
    md.append("## Parent regime × Tier")
    md.append("")
    md.append("| Regime | Elite | Pro | Seed-Pro | Standard | Seed | Probationary | Total |")
    md.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for regime in sorted(rep["by_regime_x_tier"].keys()):
        row = rep["by_regime_x_tier"][regime]
        total = sum(row.values())
        if total == 0: continue
        md.append(f"| {regime} | {row.get('Elite',0)} | {row.get('Pro',0)} | {row.get('Seed-Pro',0)} | "
                  f"{row.get('Standard',0)} | {row.get('Seed',0)} | {row.get('Probationary',0)} | {total} |")
    md.append("")
    md.append(f"## Coverage")
    md.append("")
    md.append(f"- Pairs covered: **{len(rep['pairs_covered'])}** — {', '.join(rep['pairs_covered'])}")
    md.append(f"- Strategies covered: **{len(rep['strategies_covered'])}**")
    md.append("")
    md.append("## Threshold sensitivity")
    md.append("")
    md.append("How many unique cells survive at different `(min_n_unique, min_wr_raw, min_wr_lb)` triplets?")
    md.append("")
    md.append("### Wilson LB = 0 (raw threshold only)")
    md.append("")
    md.append("| min_n_unique \\ min_wr | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 |")
    md.append("|---|---:|---:|---:|---:|---:|")
    pivot = sens[sens.min_wr_lb == 0.0].pivot(
        index="min_n_unique", columns="min_wr_raw", values="cells",
    )
    for n in sorted(pivot.index):
        cols = [str(int(pivot.loc[n, w])) for w in [0.50, 0.60, 0.70, 0.80, 0.90]]
        md.append(f"| {n} | " + " | ".join(cols) + " |")
    md.append("")
    md.append("### Wilson LB >= 0.40 (evidence-adjusted, the proposed Pro bar)")
    md.append("")
    md.append("| min_n_unique \\ min_wr | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 |")
    md.append("|---|---:|---:|---:|---:|---:|")
    pivot2 = sens[sens.min_wr_lb == 0.40].pivot(
        index="min_n_unique", columns="min_wr_raw", values="cells",
    )
    for n in sorted(pivot2.index):
        cols = [str(int(pivot2.loc[n, w])) for w in [0.50, 0.60, 0.70, 0.80, 0.90]]
        md.append(f"| {n} | " + " | ".join(cols) + " |")
    md.append("")
    md.append("## Tier rule used")
    md.append("")
    md.append("```")
    md.append("Elite         wr_lb >= 0.55 AND n_unique >= 30")
    md.append("Pro           wr_lb >= 0.45 AND n_unique >= 30")
    md.append("Seed-Pro      wr_raw >= 0.85 AND n_unique >= 15   (small-but-pure)")
    md.append("Standard      wr_lb >= 0.35 AND n_unique >= 30")
    md.append("Seed          wr_raw >= 0.70 AND n_unique >= 10   (promising)")
    md.append("Probationary  rest")
    md.append("")
    md.append("(wr_lb = Wilson 80% lower bound on raw WR)")
    md.append("```")
    md.append("")
    md.append("## Notes")
    md.append("")
    md.append("- This is a DRY RUN. No `routing_table_v9.parquet` is written. The cells CSV")
    md.append("  is informational, not deployable.")
    md.append("- Aggregation is at parent-regime granularity (C01/C02/etc.), NOT sub-regime.")
    md.append("  The seed-family children were mined at parent-regime grain. Sub-regime")
    md.append("  cell granularity would require re-mining or sub-regime classifier replay.")
    md.append("- OOS validation has NOT been applied. Cells shown are in-sample purity only.")
    md.append("  The next pass before deploying anything as Pro+ should replay the rules on")
    md.append("  a held-out time window and recompute Wilson LBs from holdout WR.")

    summary_path = out / "routing_table_v9_dryrun_summary.md"
    summary_path.write_text("\n".join(md))
    print(f"\n  -> {summary_path}")
    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
