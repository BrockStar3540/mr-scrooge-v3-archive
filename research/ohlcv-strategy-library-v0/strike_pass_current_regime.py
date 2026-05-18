"""Current-regime strike pass -- Brock 2026-05-18.

Goal: open opportunity tonight. The live bot is in C02 mostly,
candidates are 98% direct family, ny_open + ny_mid sessions.
v9_observe has SEED cells matching exactly this universe but min_tier=Seed-Pro
locks them out. We do NOT want to drop min_tier globally; we want to
identify cells with EITHER:

  (a) Strong live shadow evidence (shave_rule_satisfied count >= threshold)
  (b) High in-sample evidence (wr_unique >= 0.85 + n_unique >= 12)
  (c) Both

and promote ONLY those to a fast trade tier.

Outputs:
  strike_live_validated_cells.csv        cells with live shadow passes
  strike_top_seed_candidates.csv         cells most-hit at below_min_tier:Seed
  strike_v10_fast_cells.csv              union: live-validated + in-sample-strong
  strike_v10_fast_summary.md             counts, coverage, deployment plan
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import pandas as pd
import numpy as np


def load_ledger(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return pd.DataFrame(rows)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True)
    p.add_argument("--v9-observe", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--min-live-passes", type=int, default=2,
                   help="Min shave_rule_satisfied count to include a cell")
    p.add_argument("--min-seed-hits", type=int, default=30,
                   help="Min below_min_tier:Seed count to consider for in-sample fallback")
    p.add_argument("--top-regimes", type=int, default=2)
    p.add_argument("--top-sessions", type=int, default=4)
    p.add_argument("--top-pairs", type=int, default=20)
    args = p.parse_args()

    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)

    print(f"Loading ledger {args.ledger} ...")
    df = load_ledger(args.ledger)
    df['ts'] = pd.to_datetime(df['ts'])
    live = df[df.gate == 'entry_filter'].copy()
    shadow = df[df.gate == 'entry_filter_shadow'].copy()
    print(f"  live rows: {len(live):,} | shadow rows: {len(shadow):,}")
    span_hr = (df.ts.max() - df.ts.min()).total_seconds() / 3600
    print(f"  span: {span_hr:.1f} hours")

    # 1. Active regime / session / pair / family universe
    regs = live.regime53.value_counts().head(args.top_regimes).index.tolist()
    sess = live.session_bucket.value_counts().head(args.top_sessions).index.tolist()
    pairs = live.symbol.value_counts().head(args.top_pairs).index.tolist()
    print(f"\nActive universe:")
    print(f"  regimes:  {regs}")
    print(f"  sessions: {sess}")
    print(f"  pairs:    {pairs}")

    # 2. Live shadow passes — these are live-validated cells
    passed = shadow[shadow.block_reason == "shave_rule_satisfied"]
    passed_keys = passed.groupby(
        ['regime53','symbol','cell_strategy','direction','session_bucket']
    ).size().reset_index(name='live_passes')
    passed_keys = passed_keys.sort_values('live_passes', ascending=False)
    live_validated = passed_keys[passed_keys.live_passes >= args.min_live_passes].copy()
    live_validated.rename(columns={'symbol':'pair'}, inplace=True)
    live_validated.to_csv(out / "strike_live_validated_cells.csv", index=False)
    print(f"\n[A] Live-validated cells (shave_rule_satisfied >= {args.min_live_passes}):")
    print(f"    {len(live_validated)} cells")
    for _, r in live_validated.iterrows():
        print(f"      {r.regime53}|{r.pair}|{r.cell_strategy}|{r.direction}|{r.session_bucket}  "
              f"passes={int(r.live_passes)}")

    # 3. Most-hit Seed-tier cells in live flow — these aren't validated but are the
    #    bot's actual demand pattern. Pair with shadow rows to get cell_strategy.
    seed_hits = live[live.block_reason.str.startswith('below_min_tier:Seed', na=False)].copy()
    seed_hits['ts2'] = seed_hits.ts.dt.strftime('%Y-%m-%dT%H:%M:%S')
    sh = shadow.copy()
    sh['ts2'] = sh.ts.dt.strftime('%Y-%m-%dT%H:%M:%S')
    merged = seed_hits.merge(
        sh[['ts2','symbol','direction','candidate_strategy','cell_strategy']],
        on=['ts2','symbol','direction','candidate_strategy'],
        suffixes=('','_shadow'),
    )
    seed_demand = merged.groupby(
        ['regime53','symbol','cell_strategy_shadow','direction','session_bucket']
    ).size().reset_index(name='live_seed_hits')
    seed_demand = seed_demand[seed_demand.live_seed_hits >= args.min_seed_hits]
    seed_demand.rename(columns={'symbol':'pair','cell_strategy_shadow':'cell_strategy'}, inplace=True)
    seed_demand = seed_demand.sort_values('live_seed_hits', ascending=False)
    seed_demand.to_csv(out / "strike_top_seed_candidates.csv", index=False)
    print(f"\n[B] High-demand Seed-tier cells (live hits >= {args.min_seed_hits}):")
    print(f"    {len(seed_demand)} cells")
    for _, r in seed_demand.head(20).iterrows():
        print(f"      {r.regime53}|{r.pair}|{r.cell_strategy}|{r.direction}|{r.session_bucket}  "
              f"hits={int(r.live_seed_hits)}")

    # 4. Load v9_observe to enrich with in-sample stats
    v9 = pd.read_parquet(args.v9_observe)
    v9_keys = v9.drop_duplicates(subset=['parent_regime','pair','strategy','direction','session_bucket'])
    v9_lookup = v9_keys.set_index(['parent_regime','pair','strategy','direction','session_bucket'])
    print(f"\nv9_observe baseline: {len(v9)} rows / {len(v9_keys)} unique cells")

    def enrich(df_cells):
        recs = []
        for _, r in df_cells.iterrows():
            key = (r['regime53'], r['pair'], r['cell_strategy'], r['direction'], r['session_bucket'])
            try:
                row = v9_lookup.loc[key]
                recs.append({
                    **r.to_dict(),
                    'v9_tier': row.tier,
                    'v9_n_unique': int(row.get('n_unique', 0) or 0),
                    'v9_wins_unique': int(row.get('wins', 0) or 0),
                    'v9_wr': float(row.get('wr', 0) or 0),
                    'v9_wilson_lb': float(row.get('wilson_lb', 0) or 0),
                    'v9_shave_rule': row.get('shave_rule', ''),
                    'v9_family': row.get('family', ''),
                })
            except KeyError:
                pass
        return pd.DataFrame(recs)

    live_validated_enriched = enrich(live_validated)
    seed_demand_enriched = enrich(seed_demand)
    print(f"\nAfter v9 enrichment:")
    print(f"  live-validated cells in v9: {len(live_validated_enriched)}")
    print(f"  high-demand seed cells in v9: {len(seed_demand_enriched)}")

    # 5. Build the v10_fast cell set
    # Path 1: Live-validated (high confidence -- cell fired correctly on real data)
    # Path 2: High-demand + high in-sample (probable-good but unvalidated)
    fast_a = live_validated_enriched.copy()
    fast_a['source'] = 'live_validated'
    fast_a['priority'] = 1

    fast_b = seed_demand_enriched[
        (seed_demand_enriched.v9_wr >= 0.85)
        & (seed_demand_enriched.v9_n_unique >= 12)
    ].copy()
    fast_b['source'] = 'high_demand_strong_in_sample'
    fast_b['priority'] = 2

    fast = pd.concat([fast_a, fast_b], ignore_index=True)
    # Dedup at deploy granularity, keep highest priority (lowest number)
    fast = fast.sort_values('priority').drop_duplicates(
        subset=['regime53','pair','cell_strategy','direction','session_bucket'],
        keep='first',
    )
    fast.to_csv(out / "strike_v10_fast_cells.csv", index=False)

    # Summary MD
    md = ["# Current-regime strike pass — v10_fast candidate set", ""]
    md.append(f"**Generated**: {pd.Timestamp.now(tz='UTC').isoformat()}")
    md.append(f"**Ledger span**: {span_hr:.1f} hours / {len(df):,} rows / {len(live):,} live candidates")
    md.append("")
    md.append("## Active universe (what the bot is actually seeing)")
    md.append("")
    md.append(f"- regimes: `{regs}`")
    md.append(f"- sessions: `{sess}`")
    md.append(f"- pairs: `{pairs}`")
    md.append("")
    fam_dist = live.candidate_strategy.value_counts().to_dict()
    md.append(f"- families: {fam_dist}")
    md.append("")
    md.append("## [A] Live-validated cells")
    md.append(f"Cells where the shadow gate emitted `shave_rule_satisfied` >= {args.min_live_passes} times.")
    md.append("These are the strongest live evidence we have — rule fires correctly on live ticks.")
    md.append("")
    md.append("| regime | pair | strategy | dir | session | live_passes | v9_tier | v9_n | v9_wr | v9_lb |")
    md.append("|---|---|---|---|---|---:|---|---:|---:|---:|")
    for _, r in live_validated_enriched.sort_values('live_passes', ascending=False).iterrows():
        md.append(f"| {r.regime53} | {r.pair} | {r.cell_strategy} | {r.direction} | "
                  f"{r.session_bucket} | {int(r.live_passes)} | {r.v9_tier} | "
                  f"{r.v9_n_unique} | {r.v9_wr:.3f} | {r.v9_wilson_lb:.3f} |")
    md.append("")
    md.append("## [B] High-demand Seed cells (top 25)")
    md.append(f"Cells the bot hit at min_tier=Seed >= {args.min_seed_hits} times (lots of live candidates,")
    md.append("but blocked at tier check before shave_rule eval). Not live-validated, but high-priority")
    md.append("for promotion *if* in-sample evidence is strong.")
    md.append("")
    md.append("| regime | pair | strategy | dir | session | seed_hits | v9_tier | v9_n | v9_wr | v9_lb |")
    md.append("|---|---|---|---|---|---:|---|---:|---:|---:|")
    for _, r in seed_demand_enriched.sort_values('live_seed_hits', ascending=False).head(25).iterrows():
        md.append(f"| {r.regime53} | {r.pair} | {r.cell_strategy} | {r.direction} | "
                  f"{r.session_bucket} | {int(r.live_seed_hits)} | {r.v9_tier} | "
                  f"{r.v9_n_unique} | {r.v9_wr:.3f} | {r.v9_wilson_lb:.3f} |")
    md.append("")
    md.append("## v10_fast candidate set")
    md.append(f"Total cells: **{len(fast)}**")
    md.append(f"  - live_validated path: {len(fast[fast.source=='live_validated'])}")
    md.append(f"  - high_demand_strong_in_sample path: {len(fast[fast.source=='high_demand_strong_in_sample'])}")
    md.append("")
    md.append("By family:")
    for f, n in fast['v9_family'].fillna('unknown').value_counts().items():
        md.append(f"- `{f}`: {n}")
    md.append("")
    md.append("By cell_strategy:")
    for s, n in fast['cell_strategy'].value_counts().items():
        md.append(f"- `{s}`: {n}")
    md.append("")
    md.append("By regime:")
    for r, n in fast['regime53'].value_counts().items():
        md.append(f"- `{r}`: {n}")
    md.append("")
    md.append("By session:")
    for s, n in fast['session_bucket'].value_counts().items():
        md.append(f"- `{s}`: {n}")
    md.append("")
    md.append("## Deployment plan")
    md.append("")
    md.append("1. Build `routing_table_v10_fast_current_regime.parquet` from these cells with `tier='Fast'`.")
    md.append("2. Add `Fast` to the EntryFilterGate tier rank (between Seed-Pro and Pro).")
    md.append("3. Flip `gates.entry_filter.min_tier = 'Fast'` and `routing_table_path` to the new parquet.")
    md.append("4. Bot resumes live trading with this narrow current-regime surface.")
    md.append("")
    md.append("Risk profile: all live-validated cells fired correctly in shadow >= threshold times.")
    md.append("High-demand cells have v9 in-sample wr >= 0.85 / n >= 12. Both bounded by daily-circuit,")
    md.append("cooldown, debounce, and existing zone-blacklist gates. Position sizing unchanged.")
    md.append("")
    md.append("Caveat: probe cells lack corpus-OOS evidence. Live deployment IS the OOS test.")
    md.append("Recommend daily-circuit threshold tightened (e.g. 2.5% from 3%) until ~50 cells have")
    md.append("accumulated >= 5 LIMIT placements each, then revert.")

    md_path = out / "strike_v10_fast_summary.md"
    md_path.write_text("\n".join(md))
    print(f"\n  -> {md_path}")
    print(f"  -> {out / 'strike_v10_fast_cells.csv'} ({len(fast)} cells)")


if __name__ == "__main__":
    main()
