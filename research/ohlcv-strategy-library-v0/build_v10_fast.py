"""Build routing_table_v10_fast_current_regime.parquet from strike-pass cells.

Brock 2026-05-18: prepare the parquet but do not flip. Each strike cell is
promoted to tier='Seed-Pro' (so the existing min_tier=Seed-Pro live gate
allows it) and the table is narrowed to only the strike cells. Other
candidates get no_routing_match and stay blocked.

Schema is v8-compatible (drop-in to RoutingTable.load).
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

SESSION_BUCKETS = ("asia","asia_late","london_open","ny_open","ny_mid","ny_close","off_hours")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--strike-cells", required=True)
    p.add_argument("--v9-observe", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--promote-tier", default="Seed-Pro",
                   help="Tier to assign to strike cells (Seed-Pro lets the existing gate fire)")
    args = p.parse_args()

    strike = pd.read_csv(args.strike_cells)
    v9 = pd.read_parquet(args.v9_observe)

    # Look up the original v9 row for each strike cell; carry all v8 columns
    keys = ['parent_regime','pair','strategy','direction','session_bucket']
    v9_dedup = v9.drop_duplicates(subset=keys)

    rows = []
    now = datetime.now(timezone.utc).isoformat()
    for _, sc in strike.iterrows():
        m = v9_dedup[
            (v9_dedup.parent_regime == sc.regime53)
            & (v9_dedup.pair == sc.pair)
            & (v9_dedup.strategy == sc.cell_strategy)
            & (v9_dedup.direction == sc.direction)
            & (v9_dedup.session_bucket == sc.session_bucket)
        ]
        if m.empty:
            print(f"  NO V9 MATCH: {sc.regime53}|{sc.pair}|{sc.cell_strategy}|{sc.direction}|{sc.session_bucket}")
            continue
        base = m.iloc[0].to_dict()
        base['tier'] = args.promote_tier
        base['promotion_status'] = 'live'  # earned via strike pass
        base['source_bank'] = base.get('source_bank') or 'strike_promoted'
        base['last_updated'] = now
        # Carry strike evidence in basis
        if 'live_passes' in sc.index and pd.notna(sc.get('live_passes')):
            base['source'] = f"strike_live_validated_passes={int(sc.live_passes)}"
        else:
            base['source'] = f"strike_high_demand_hits={int(sc.get('live_seed_hits', 0) or 0)}"
        rows.append(base)

    df = pd.DataFrame(rows)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(args.out, index=False)
    print(f"Wrote {len(df)} rows to {args.out}")
    print(f"  unique cells: {df.drop_duplicates(subset=['parent_regime','pair','strategy','direction']).shape[0]}")
    print(f"  tier: {args.promote_tier}")


if __name__ == "__main__":
    main()
