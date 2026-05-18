"""v4 scorer training-set assembler.

Brock 2026-05-18: build the dataset that v4 will train on. v4 is the
new ranker replacing v3 (which is now demoted-then-retired).

Joins:
  ml_training_corpus.parquet       per-trade rows with factors + outcome
  routing_table_v9_observe.parquet cell-level evidence (tier/wr/n/lb)
  optional: live fills from execution-audit (deferred until fills exist)

Output: research/.../v4_scorer/v4_training_set_YYYY-MM-DD.parquet
  One row per trade (after probe-dedup) with:
    -- features --
    technical_regime_53, parent_regime, pair, direction,
    session_bucket, hour_utc, day_of_week,
    ATR_ratio, BB_compress, ADX14, RSI14, close_pos, bb_position,
    volume_ratio, z_score, ema20_dist_pct, ema50_dist_pct,
    sma20_dist_signed_bps,
    cell_tier (ordinal), cell_n_unique, cell_wr, cell_wilson_lb,
    cell_source_bank, cell_match_kind (always 'exact' in training -- the
    match_kind for live family-loose runtime cases),
    -- targets --
    is_win  (Head A: should_trade)
    realized_R  (Head B: expected_r)
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

CORPUS = Path("/Users/brock-mini-mac/scrooge-research/routing-table-v2/ml_training_corpus.parquet")
TIER_RANK = {"Probationary": 0, "Seed": 1, "Standard": 2, "Seed-Pro": 3, "Pro": 4, "Elite": 5}


def session_for_hour(h):
    try: h = int(h)
    except: return None
    if   0 <= h < 4:   return "asia"
    elif 4 <= h < 6:   return "asia_late"
    elif 6 <= h < 9:   return "london_open"
    elif 9 <= h < 13:  return "ny_open"
    elif 13 <= h < 17: return "ny_mid"
    elif 17 <= h < 21: return "ny_close"
    else:              return "off_hours"


def dedup_probe(df):
    """Remove 2x probe inflation."""
    if "source" not in df.columns:
        return df
    t = df[df.source == "trainer"]
    nt = df[df.source != "trainer"]
    if len(t):
        t = t.drop_duplicates(subset=["entry_ts", "strategy_id", "pair", "direction"])
    return pd.concat([nt, t], ignore_index=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v9-observe", required=True,
                    help="path to routing_table_v9_observe.parquet")
    ap.add_argument("--corpus", default=str(CORPUS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--tier-floor", default="Seed",
                    help="Minimum cell tier to include (drops Probationary by default)")
    ap.add_argument("--max-rows", type=int, default=0,
                    help="If >0, sample this many rows for quick iteration")
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tier_floor_rank = TIER_RANK.get(args.tier_floor, 1)
    print(f"=== v4 training set assembly ===")
    print(f"  corpus: {args.corpus}")
    print(f"  v9_observe: {args.v9_observe}")
    print(f"  tier floor: {args.tier_floor} (rank >= {tier_floor_rank})")

    # 1. Load v9 cells (deduped to one row per cell-key)
    v9 = pd.read_parquet(args.v9_observe)
    v9_cells = v9.drop_duplicates(subset=[
        "parent_regime", "pair", "strategy", "direction"
    ]).copy()
    v9_cells["tier_rank"] = v9_cells.tier.map(TIER_RANK).fillna(0).astype(int)
    v9_cells = v9_cells[v9_cells.tier_rank >= tier_floor_rank]
    print(f"  cells in v9 (tier >= {args.tier_floor}): {len(v9_cells):,}")

    # 2. Load corpus
    print(f"  loading corpus ...")
    cols = [
        "source","strategy_id","pair","direction","entry_ts","is_win",
        "realized_R","technical_regime_53","hour_utc","day_of_week",
        "ATR_ratio","BB_compress","ADX14","RSI14","close_pos","bb_position",
        "volume_ratio","z_score","ema20_dist_pct","ema50_dist_pct",
        "sma20_dist_signed_bps",
    ]
    available = set(pq.read_schema(args.corpus).names)
    cols = [c for c in cols if c in available]
    corpus = pq.read_table(args.corpus, columns=cols).to_pandas()
    print(f"  corpus rows raw: {len(corpus):,}")
    corpus = dedup_probe(corpus)
    print(f"  corpus rows post-dedup: {len(corpus):,}")
    corpus["session_bucket"] = corpus["hour_utc"].map(session_for_hour)
    corpus["parent_regime"] = corpus["technical_regime_53"].astype(str).str[:3]
    # parent_regime extraction (C01 -> C01, C02 -> C02, B01 -> B01, etc.)
    # safe simple slice since regime53 codes are 3 chars

    # 3. Join cell info onto trades
    cell_lookup = v9_cells.set_index(
        ["parent_regime", "pair", "strategy", "direction"]
    )
    print(f"  joining cell info onto trades ...")

    # Per-trade cell join
    def lookup_cell(row):
        key = (row.parent_regime, row.pair, row.strategy_id, row.direction)
        try:
            c = cell_lookup.loc[key]
            return pd.Series({
                "cell_tier_rank": int(c.tier_rank),
                "cell_tier": c.tier,
                "cell_n_unique": int(c.get("n_unique", c.get("n", 0)) or 0),
                "cell_wr": float(c.get("wr", 0.0)),
                "cell_wilson_lb": float(c.get("wilson_lb", 0.0)),
                "cell_source_bank": str(c.get("source_bank", "unknown")),
            })
        except KeyError:
            return pd.Series({
                "cell_tier_rank": 0, "cell_tier": "none",
                "cell_n_unique": 0, "cell_wr": 0.0, "cell_wilson_lb": 0.0,
                "cell_source_bank": "no_cell",
            })

    # Limit to trades where the (regime, pair, strategy, direction) has a
    # v9 cell at the tier floor; this is the universe v4 will reason about
    keys = set(cell_lookup.index)
    corpus["_key"] = list(zip(
        corpus.parent_regime, corpus.pair, corpus.strategy_id, corpus.direction
    ))
    in_universe = corpus[corpus._key.isin(keys)].drop(columns="_key").copy()
    print(f"  trades in cell-universe: {len(in_universe):,}")
    if args.max_rows > 0 and len(in_universe) > args.max_rows:
        in_universe = in_universe.sample(args.max_rows, random_state=42)
        print(f"  sampled to {len(in_universe):,} for quick build")

    # Vectorized cell join via merge for speed
    cell_df = v9_cells[["parent_regime","pair","strategy","direction","tier",
                        "tier_rank","wr","wilson_lb"]].rename(columns={
        "strategy":"strategy_id", "tier":"cell_tier",
        "tier_rank":"cell_tier_rank", "wr":"cell_wr",
        "wilson_lb":"cell_wilson_lb",
    })
    n_col = "n_unique" if "n_unique" in v9_cells.columns else "n"
    cell_df["cell_n_unique"] = v9_cells[n_col].values if n_col in v9_cells.columns else 0
    src_col = "source_bank" if "source_bank" in v9_cells.columns else None
    if src_col:
        cell_df["cell_source_bank"] = v9_cells[src_col].astype(str).values
    else:
        cell_df["cell_source_bank"] = "unknown"
    in_universe = in_universe.merge(
        cell_df, on=["parent_regime","pair","strategy_id","direction"], how="left",
    )
    print(f"  joined rows: {len(in_universe):,}")

    # 4. Final feature/target frame
    keep = [
        # identity
        "entry_ts","strategy_id","pair","direction",
        # regime / session / time
        "technical_regime_53","parent_regime","session_bucket",
        "hour_utc","day_of_week",
        # factors
        "ATR_ratio","BB_compress","ADX14","RSI14","close_pos","bb_position",
        "volume_ratio","z_score","ema20_dist_pct","ema50_dist_pct",
        "sma20_dist_signed_bps",
        # cell features
        "cell_tier","cell_tier_rank","cell_n_unique","cell_wr","cell_wilson_lb",
        "cell_source_bank",
        # targets
        "is_win","realized_R",
    ]
    keep = [c for c in keep if c in in_universe.columns]
    final = in_universe[keep].copy()
    final["v4_split"] = np.where(
        pd.to_datetime(final.entry_ts, utc=True) < pd.Timestamp("2025-01-01", tz="UTC"),
        "train", "test",
    )
    print(f"  final rows: {len(final):,}")
    print(f"  train/test split: {final.v4_split.value_counts().to_dict()}")
    print(f"  win rate overall: {final.is_win.mean():.3f}")
    print(f"  win rate by split: {final.groupby('v4_split').is_win.mean().to_dict()}")

    final.to_parquet(out, index=False)
    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
