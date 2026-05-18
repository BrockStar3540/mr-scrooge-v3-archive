"""routing_table_v9 builder — two-surface deploy from the corrected seed bank.

Doctrine (Brock 2026-05-18):
  * Trade surface  = Elite + Pro + Seed-Pro     (high evidence)
  * Observe surface= adds Seed                  (telemetry only)
  * Never trade    = Probationary

Corrections vs v8 (same as the dry-run, now writing deployable parquets):
  1. V3 probe stats are 2x inflated (one row per target_R) — divide.
  2. Textbook children with legacy session_bucket vocabulary (`asia`/`london`/`ny`)
     cannot replay against the live 7-bucket classifier — drop.
  3. Tier rule reasons on n_unique with Wilson 80% LB.

Outputs (drop-in compatible with the existing RoutingTable loader):
  routing_table_v9_trade.parquet      Elite + Pro + Seed-Pro only
  routing_table_v9_observe.parquet    + Seed
  routing_table_v9_summary.md         counts, coverage, doctrine notes
  routing_table_v9_sensitivity.csv    threshold sweep

Schema matches v8 plus four new audit columns:
  tier                  (existing) Elite / Pro / Seed-Pro / Seed / Probationary
  n_unique              (new)      sample size in unique trades
  wilson_lb             (new)      Wilson 80% lower bound on raw WR
  source_bank           (new)      "probe" or "textbook"
  oos_status            (new)      "untested" (filled by validator later)
  promotion_status      (new)      "candidate" / "observe" / "live" / "demoted"
"""
from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

V3_PROBES = {
    "alpha_pullback_v2", "alpha_breakout_retest_v2", "alpha_extended_fade_v2",
    "echo_box_fade_v2", "echo_failed_breakout_v2",
    "charlie_pullback_continuation_v2", "charlie_compression_breakout",
    "bravo_failed_momentum", "bravo_expansion_continuation",
    "delta_tag_and_go_v2",
}

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

# Live SessionBucketClassifier (DST-stable 7-bucket map). Used for session
# expansion — every cell is replicated across all 7 buckets, the shave_rule
# carries any session-specific filter.
SESSION_BUCKETS = ("asia", "asia_late", "london_open", "ny_open",
                   "ny_mid", "ny_close", "off_hours")

LEGACY_SESSION_RE = re.compile(r"session_bucket==(london|asia|ny)(?!_)")


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


def tier_for(wr_unique: float, n_unique: int, wr_lb: float) -> str:
    if wr_lb >= 0.55 and n_unique >= 30: return "Elite"
    if wr_lb >= 0.45 and n_unique >= 30: return "Pro"
    if wr_unique >= 0.85 and n_unique >= 15: return "Seed-Pro"
    if wr_lb >= 0.35 and n_unique >= 30: return "Standard"
    if wr_unique >= 0.70 and n_unique >= 10: return "Seed"
    return "Probationary"


TIER_RANK = {
    "Elite": 5, "Pro": 4, "Seed-Pro": 3, "Standard": 2, "Seed": 1, "Probationary": 0,
}
TRADE_TIERS = {"Elite", "Pro", "Seed-Pro"}
OBSERVE_ALSO = TRADE_TIERS | {"Seed"}


def load_probe(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["n_unique"] = (df["n"] // 2).astype(int)
    df["wins_unique"] = (df["wins"] // 2).astype(int)
    df["losses_unique"] = df["n_unique"] - df["wins_unique"]
    df["wr_unique"] = np.where(df["n_unique"] > 0,
                               df["wins_unique"] / df["n_unique"], 0.0)
    df["source_bank"] = "probe"
    df["family"] = df["root_strategy_id"].map(family_for)
    return df


def load_textbook(path: Path) -> tuple[pd.DataFrame, int]:
    df = pd.read_csv(path)
    if "bucket" in df.columns:
        df = df[df["bucket"].isin(["winner_seed", "near_pure_seed"])]
    legacy_mask = df["child_rule"].fillna("").str.contains(LEGACY_SESSION_RE)
    legacy_n = int(legacy_mask.sum())
    df = df[~legacy_mask].copy()
    df["n_unique"] = df["n"].astype(int)
    df["wins_unique"] = df["wins"].astype(int)
    df["losses_unique"] = df["n_unique"] - df["wins_unique"]
    df["wr_unique"] = df["wr"]
    df["source_bank"] = "textbook"
    df["family"] = df["root_strategy_id"].map(family_for)
    return df, legacy_n


def aggregate_to_cells(combined: pd.DataFrame) -> pd.DataFrame:
    """Best winning child per (strategy x pair x direction x parent_regime) cell."""
    combined = combined.copy()
    combined["wilson_lb"] = [
        wilson_lb(int(w), int(n))
        for w, n in zip(combined["wins_unique"], combined["n_unique"])
    ]
    combined["tier"] = [
        tier_for(wr, int(n), lb)
        for wr, n, lb in zip(combined["wr_unique"], combined["n_unique"], combined["wilson_lb"])
    ]
    combined["tier_rank"] = combined["tier"].map(TIER_RANK)
    combined = combined.sort_values(
        ["tier_rank", "wilson_lb", "wr_unique", "n_unique"], ascending=False,
    )
    cell_key = ["root_strategy_id", "pair", "direction", "technical_regime_53"]
    return combined.drop_duplicates(subset=cell_key).reset_index(drop=True)


def materialize_for_routing_table(cells: pd.DataFrame, now_iso: str) -> pd.DataFrame:
    """Expand to the v8 schema + session buckets so the live RoutingTable loads it.

    One row per (cell x session_bucket). The shave_rule carries any session
    filter; EntryFilterGate evaluates it at lookup time.
    """
    rows = []
    for _, c in cells.iterrows():
        for sb in SESSION_BUCKETS:
            rows.append({
                # v8 schema (load-bearing for RoutingTable.lookup + _build_basis)
                "sub_regime": c["technical_regime_53"],  # parent-regime grain
                "technical_regime_53": c["technical_regime_53"],
                "technical_regime_desc": "",
                "parent_regime": c["technical_regime_53"],
                "session_bucket": sb,
                "pair": c["pair"],
                "strategy": c["root_strategy_id"],
                "family": c["family"],
                "direction": c["direction"],
                "r_target": 1.5,
                "score_boost": 0.0,
                "n": int(c["n_unique"]),
                "wins": int(c["wins_unique"]),
                "sum_R": 0.0,
                "mean_R": 0.0,
                "wr": float(c["wr_unique"]),
                "source": "v9_seed_aggregation",
                "last_updated": now_iso,
                "shave_rule": c.get("child_rule", "") or "",
                "loser_skip_rule": "",
                "winner_lift": float(c.get("purity_gain") or 0.0),
                "parent_n": 0,
                "parent_wr": 0.0,
                "tier": c["tier"],
                # v9 additions (Brock 2026-05-18)
                "n_unique": int(c["n_unique"]),
                "wilson_lb": float(c["wilson_lb"]),
                "source_bank": c["source_bank"],
                "oos_status": "untested",
                "promotion_status": "candidate",
            })
    return pd.DataFrame(rows)


def summarize(cells: pd.DataFrame, expanded_trade: pd.DataFrame,
              expanded_obs: pd.DataFrame, v8_path: Path,
              legacy_dropped: int, total_candidates: int) -> str:
    v8 = pd.read_parquet(v8_path)
    v8_base = v8.drop_duplicates(subset=["sub_regime","pair","strategy","direction"])
    v8_at_parent = v8_base.drop_duplicates(
        subset=["parent_regime","pair","strategy","direction"],
    )

    md = []
    md.append("# routing_table_v9 — build summary")
    md.append("")
    md.append(f"Built: {datetime.now(timezone.utc).isoformat()}")
    md.append("")
    md.append("## Doctrine (Brock 2026-05-18)")
    md.append("")
    md.append("Two surfaces emitted from one candidate universe:")
    md.append("")
    md.append("- **`routing_table_v9_trade.parquet`** — only `Elite`/`Pro`/`Seed-Pro`. Live-tradable.")
    md.append("- **`routing_table_v9_observe.parquet`** — adds `Seed`. Telemetry only. Do NOT flip the bot to point at this file with HARD enforcement.")
    md.append("")
    md.append("## Inputs")
    md.append("")
    md.append(f"- Combined candidate children: **{total_candidates:,}**")
    md.append(f"- Legacy session-vocab textbook rows dropped: **{legacy_dropped:,}**")
    md.append(f"- Unique cells after best-per-cell aggregation: **{len(cells):,}** (parent-regime grain)")
    md.append("")
    md.append("## Tier distribution (cells, not session-expanded rows)")
    md.append("")
    by_tier = cells["tier"].value_counts().to_dict()
    v8_tiers = v8_at_parent["tier"].value_counts().to_dict()
    md.append("| Tier | v9 cells | v8 cells (parent-grain) | Δ | trade? |")
    md.append("|---|---:|---:|---:|---|")
    for tier in ["Elite","Pro","Seed-Pro","Standard","Seed","Probationary"]:
        v9c, v8c = by_tier.get(tier, 0), v8_tiers.get(tier, 0)
        trade = "✓" if tier in TRADE_TIERS else ("observe" if tier in OBSERVE_ALSO else "—")
        md.append(f"| {tier} | {v9c} | {v8c} | {v9c-v8c:+d} | {trade} |")
    md.append("")
    md.append("## Family × tier (v9)")
    md.append("")
    md.append("| Family | Elite | Pro | Seed-Pro | Standard | Seed | Probationary |")
    md.append("|---|---:|---:|---:|---:|---:|---:|")
    fxt = cells.groupby(["family","tier"]).size().unstack(fill_value=0).reindex(
        columns=["Elite","Pro","Seed-Pro","Standard","Seed","Probationary"], fill_value=0,
    )
    for fam, row in fxt.iterrows():
        md.append(f"| {fam} | {row.Elite} | {row.Pro} | {row['Seed-Pro']} | "
                  f"{row.Standard} | {row.Seed} | {row.Probationary} |")
    md.append("")
    md.append("## Output sizes")
    md.append("")
    md.append("| File | Cells | Rows (session-expanded) |")
    md.append("|---|---:|---:|")
    md.append(f"| routing_table_v9_trade.parquet | "
              f"{len(cells[cells.tier.isin(TRADE_TIERS)])} | "
              f"{len(expanded_trade)} |")
    md.append(f"| routing_table_v9_observe.parquet | "
              f"{len(cells[cells.tier.isin(OBSERVE_ALSO)])} | "
              f"{len(expanded_obs)} |")
    md.append("")
    md.append("## Live-deployment policy")
    md.append("")
    md.append("**To flip the bot to v9 trade surface:**")
    md.append("```")
    md.append('strategies.routing_table_path = "data/routing_table_v9_trade.parquet"')
    md.append("```")
    md.append("Keep `gates.entry_filter.mode = \"hard\"`. `min_tier` can stay at `Standard`")
    md.append("or move to `Seed-Pro` — both work; v9_trade has no Probationary/Standard")
    md.append("rows so the practical difference is small.")
    md.append("")
    md.append("**For Seed observation:** ship a separate observer that reads the observe parquet")
    md.append("and writes telemetry on Seed-cell candidates without affecting execution. The")
    md.append("trade parquet is the load-bearing path.")
    md.append("")
    md.append("## Promotion lifecycle")
    md.append("")
    md.append("Each row carries `promotion_status` and `oos_status`. The intended flow:")
    md.append("")
    md.append("1. `candidate` + `untested` — fresh from this build.")
    md.append("2. Run static-rule OOS replay on a held-out window. Sets `oos_status = passed|failed`.")
    md.append("3. After live observation accumulates clean evidence on Seed cells, those")
    md.append("   get `promotion_status = observe → live` and may move up a tier.")
    md.append("4. Cells that perform badly live get `demoted` and dropped from the trade parquet.")
    md.append("")
    md.append("These columns are written as `untested` / `candidate` here; a future")
    md.append("`promote_routing_cells.py` script will edit them based on OOS + live data.")
    return "\n".join(md)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--probe-winners", required=True)
    p.add_argument("--textbook", required=True)
    p.add_argument("--v8-parquet", required=True)
    p.add_argument("--out-dir", required=True)
    args = p.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    print("=== Loading inputs ===")
    probe = load_probe(Path(args.probe_winners))
    text, legacy_dropped = load_textbook(Path(args.textbook))
    common = ["source_bank", "root_strategy_id", "family", "pair", "direction",
              "technical_regime_53", "child_rule",
              "n_unique", "wins_unique", "losses_unique", "wr_unique",
              "purity_gain"]
    combined = pd.concat([probe[common], text[common]], ignore_index=True)
    print(f"  probe children:    {len(probe):,}  (2x-corrected)")
    print(f"  textbook children: {len(text):,}  ({legacy_dropped:,} legacy-vocab dropped)")
    print(f"  combined:          {len(combined):,}")

    print("\n=== Aggregating ===")
    cells = aggregate_to_cells(combined)
    print(f"  unique cells: {len(cells):,}")
    print(f"  tier dist: {cells['tier'].value_counts().to_dict()}")

    print("\n=== Building deployable parquets ===")
    now_iso = datetime.now(timezone.utc).isoformat()
    cells_trade = cells[cells.tier.isin(TRADE_TIERS)].copy()
    cells_obs   = cells[cells.tier.isin(OBSERVE_ALSO)].copy()
    cells_obs["promotion_status"] = np.where(
        cells_obs["tier"].isin(TRADE_TIERS), "candidate", "observe",
    )

    trade_parq = materialize_for_routing_table(cells_trade, now_iso)
    obs_parq   = materialize_for_routing_table(cells_obs, now_iso)

    trade_path = out / "routing_table_v9_trade.parquet"
    obs_path   = out / "routing_table_v9_observe.parquet"
    trade_parq.to_parquet(trade_path, index=False)
    obs_parq.to_parquet(obs_path, index=False)
    print(f"  -> {trade_path}  rows={len(trade_parq)}")
    print(f"  -> {obs_path}  rows={len(obs_parq)}")

    # Cells CSV for diagnostic use
    cells_csv = out / "routing_table_v9_cells.csv"
    cells.to_csv(cells_csv, index=False)
    print(f"  -> {cells_csv}")

    summary = summarize(cells, trade_parq, obs_parq,
                        Path(args.v8_parquet), legacy_dropped, len(combined))
    summary_path = out / "routing_table_v9_summary.md"
    summary_path.write_text(summary)
    print(f"  -> {summary_path}")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
