"""Moving-Regime Seed Factory — 6mo last-6 months winner-island mining.

Inputs:
  - unified moving-regime trades (textbook + V3 trainer probes, dense regime53)
  - 6,779 winners / 48,050 losers / 54,829 total

Process per (strategy_id, regime53) cell with at least 30 trades:
  - Treat the cell as a parent nursery
  - Mine sub-conditions inside that group where winners cluster
  - Output factor-shave seeds + their loser contrast buckets

Factor shave dimensions (all available at entry from foundational/trainer data):
  - direction
  - pair_family (heuristic)
  - hour_utc (categorical)
  - weekday (categorical)
  - ATR14, ATR_ratio, BB_compress, ADX14, RSI14, price_pos, close_pos, EMA_slope
    (from dense regime53 lookup; some via merge)
"""
import pandas as pd
import numpy as np
import glob
from pathlib import Path
import json

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
FOUND = ROOT / "all_strategies_all_pairs_trades.parquet"
DENSE = ROOT / "dense_regime53_lookup_last6mo.parquet"
TRAINER_DIR = ROOT / "trainer-replay-v2"
OUT_DIR = ROOT / "moving-regime-seed-factory"
OUT_DIR.mkdir(exist_ok=True)

CUTOFF = pd.Timestamp("2025-10-22", tz="UTC")
HARD_LATEST = pd.Timestamp("2026-04-22", tz="UTC")
DEAD_REGIMES = {"R04", "T07", "Z01"}  # the 96% that doesn't move

print("loading dense lookup ...")
lookup = pd.read_parquet(DENSE)
lookup["ts"] = pd.to_datetime(lookup["ts"], utc=True)

print("loading + filtering textbook to moving regimes ...")
foundational = pd.read_parquet(FOUND, columns=[
    "strategy_id","pair","pair_family","direction","entry_ts","is_win","realized_R"
])
foundational["entry_ts"] = pd.to_datetime(foundational["entry_ts"], utc=True)
foundational = foundational[(foundational.entry_ts >= CUTOFF) & (foundational.entry_ts <= HARD_LATEST)].copy()
foundational = foundational.merge(lookup.rename(columns={"ts":"entry_ts"}), on=["pair","entry_ts"], how="left")
foundational = foundational[~foundational.technical_regime_53.isin(DEAD_REGIMES)].copy()
foundational["source"] = "textbook"
print(f"  textbook moving-regime trades: {len(foundational):,}")

print("loading + filtering trainer probes to moving regimes ...")
parts = []
for f in sorted(glob.glob(str(TRAINER_DIR / "*.parquet"))):
    parts.append(pd.read_parquet(f, columns=[
        "pair","entry_ts","direction","probe_name","realized_r","filled"
    ]))
trainer = pd.concat(parts, ignore_index=True)
trainer["entry_ts"] = pd.to_datetime(trainer["entry_ts"], utc=True)
trainer = trainer[(trainer.entry_ts >= CUTOFF) & (trainer.entry_ts <= HARD_LATEST)].copy()
trainer = trainer[trainer.filled].copy()
trainer["is_win"] = trainer["realized_r"] > 0
trainer = trainer.rename(columns={"probe_name":"strategy_id","realized_r":"realized_R"})
trainer = trainer.merge(lookup.rename(columns={"ts":"entry_ts"}), on=["pair","entry_ts"], how="left")
trainer = trainer[~trainer.technical_regime_53.isin(DEAD_REGIMES)].copy()
trainer["source"] = "v3_trainer_probe"
# Derive pair_family
PAIR_FAMILY_MAP = {}
for p in ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN"]:
    PAIR_FAMILY_MAP[p] = "usd_base"
for p in ["EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY"]:
    PAIR_FAMILY_MAP[p] = "eur_cross"
for p in ["GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY"]:
    PAIR_FAMILY_MAP[p] = "gbp_cross"
for p in ["AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]:
    PAIR_FAMILY_MAP[p] = "antipodean_cross"
trainer["pair_family"] = trainer["pair"].map(PAIR_FAMILY_MAP)
print(f"  trainer moving-regime trades:  {len(trainer):,}")

cols = ["source","strategy_id","pair","pair_family","direction","entry_ts",
        "is_win","realized_R","technical_regime_53","technical_regime_desc",
        "ATR14","ATR_ratio","BB_width","BB_compress","ADX14","EMA_slope","RSI14","close_pos"]
unified = pd.concat([foundational[cols], trainer[cols]], ignore_index=True)
unified["hour_utc"] = unified["entry_ts"].dt.hour.astype(int)
unified["weekday"] = unified["entry_ts"].dt.weekday.astype(int)
print(f"\nunified moving-regime trades: {len(unified):,}")
print(f"  winners: {int(unified.is_win.sum()):,}")
print(f"  losers:  {int((~unified.is_win).sum()):,}")

# === Winner-island miner inside each (strategy, regime53) parent cell ===
# For each parent with at least 30 winners, mine sub-conditions where winners
# concentrate. Use a single-feature threshold split (greedy).
import itertools

FACTORS = ["ATR_ratio","BB_compress","ADX14","RSI14","close_pos","EMA_slope","hour_utc"]

def best_split(parent, factor, n_bins=4, min_island=5):
    """Find best threshold split inside parent: maximize island purity."""
    if parent[factor].isna().all(): return None
    try:
        qs = parent[factor].quantile([0.2, 0.4, 0.5, 0.6, 0.8]).values
    except Exception:
        return None
    best = None
    for thr in qs:
        for direction in ("<=", ">"):
            if direction == "<=":
                island = parent[parent[factor] <= thr]
                excluded = parent[parent[factor] > thr]
            else:
                island = parent[parent[factor] > thr]
                excluded = parent[parent[factor] <= thr]
            if len(island) < min_island: continue
            iw = island.is_win.sum()
            ew = excluded.is_win.sum()
            # Score: island purity AND winner share retained
            island_purity = iw / max(1, len(island))
            if island_purity < 0.40: continue
            parent_wr = parent.is_win.mean()
            lift = island_purity / max(0.05, parent_wr)
            if lift < 1.2: continue
            score = iw - len(island) * (1 - island_purity)  # net winners after losses
            if (best is None) or (score > best["score"]):
                best = {"factor": factor, "op": direction, "threshold": float(thr),
                        "score": float(score), "island_n": int(len(island)),
                        "island_wins": int(iw), "island_losses": int(len(island) - iw),
                        "island_wr": float(island_purity), "lift": float(lift),
                        "parent_wr": float(parent_wr)}
    return best


def shave_parent(parent, min_winners=10):
    """Mine winner islands inside one parent cell."""
    if parent.is_win.sum() < min_winners: return []
    # Try each factor independently, keep the best
    islands = []
    for f in FACTORS:
        b = best_split(parent, f)
        if b: islands.append(b)
    # Also try 2-factor conjunctions for the top-2 single splits
    if len(islands) >= 2:
        islands.sort(key=lambda x: x["score"], reverse=True)
        f1 = islands[0]["factor"]; f2 = islands[1]["factor"]
        if f1 != f2:
            try:
                if islands[0]["op"] == "<=":
                    mask1 = parent[f1] <= islands[0]["threshold"]
                else:
                    mask1 = parent[f1] > islands[0]["threshold"]
                stage2_parent = parent[mask1]
                if len(stage2_parent) >= 30 and stage2_parent.is_win.sum() >= 5:
                    b2 = best_split(stage2_parent, f2)
                    if b2:
                        # Combine as a sibling
                        islands.append({
                            "factor": f"{f1}+{f2}",
                            "op": f"({islands[0]['op']}{islands[0]['threshold']:.4g}) AND ({b2['op']}{b2['threshold']:.4g})",
                            "threshold": (islands[0]["threshold"], b2["threshold"]),
                            "score": b2["score"],
                            "island_n": b2["island_n"], "island_wins": b2["island_wins"],
                            "island_losses": b2["island_losses"], "island_wr": b2["island_wr"],
                            "lift": b2["lift"] * islands[0]["lift"],
                            "parent_wr": parent.is_win.mean(),
                        })
            except Exception:
                pass
    return islands


print("\n=== mining winner islands inside each (strategy, regime53) cell ===")
parent_cells = unified.groupby(["source","strategy_id","technical_regime_53","technical_regime_desc"])
seed_rows = []
loser_rows = []
n_parents_examined = 0
n_seeds_found = 0

for (src, strat, reg, desc), parent_df in parent_cells:
    if len(parent_df) < 30: continue
    if parent_df.is_win.sum() < 10: continue
    n_parents_examined += 1
    parent_wr = parent_df.is_win.mean()
    parent_n = len(parent_df)
    parent_winners = int(parent_df.is_win.sum())
    parent_losers = int(parent_n - parent_winners)

    # Bucket the parent's losers as background
    for _, r in parent_df[~parent_df.is_win].iterrows():
        loser_rows.append({
            "bucket": "parent",
            "source": src, "strategy_id": strat, "regime_53": reg,
            "pair": r["pair"], "direction": r["direction"], "entry_ts": r["entry_ts"],
            "realized_R": r["realized_R"],
            "ATR14": r["ATR14"], "ATR_ratio": r["ATR_ratio"],
            "BB_compress": r["BB_compress"], "ADX14": r["ADX14"],
            "RSI14": r["RSI14"], "close_pos": r["close_pos"],
        })

    # Mine islands
    islands = shave_parent(parent_df)
    for isl in islands:
        n_seeds_found += 1
        seed_rows.append({
            "source": src, "strategy_id": strat,
            "regime_53": reg, "regime_desc": desc,
            "parent_n": parent_n, "parent_winners": parent_winners,
            "parent_losers": parent_losers, "parent_wr": round(parent_wr, 3),
            "shave_factor": isl["factor"], "shave_op": isl.get("op",""),
            "shave_threshold": str(isl["threshold"]),
            "island_n": isl["island_n"], "island_wins": isl["island_wins"],
            "island_losses": isl["island_losses"],
            "island_wr": round(isl["island_wr"], 3),
            "wr_lift": round(isl["lift"], 3),
            "purity_class": (
                "pure" if isl["island_wins"] >= 10 and isl["island_losses"] == 0
                else "near_pure" if isl["island_wins"] >= 10 and isl["island_losses"] <= 2
                else "exploratory"
            ),
        })

print(f"\nparents examined: {n_parents_examined}")
print(f"seeds found: {n_seeds_found}")

seeds = pd.DataFrame(seed_rows)
losers = pd.DataFrame(loser_rows)
seeds.to_csv(OUT_DIR / "moving_regime_seeds.csv", index=False)
losers.to_csv(OUT_DIR / "moving_regime_loser_bank.csv", index=False)

# Summary stats
print(f"\n=== SEED FACTORY OUTPUT ===")
print(f"  total seeds:           {len(seeds)}")
if len(seeds):
    print(f"  pure seeds (>=10W/0L): {(seeds.purity_class=='pure').sum()}")
    print(f"  near-pure (>=10W/<=2L):{(seeds.purity_class=='near_pure').sum()}")
    print(f"  exploratory:           {(seeds.purity_class=='exploratory').sum()}")
    print()
    print("=== top 20 by island_wr ===")
    print(seeds.sort_values("island_wr", ascending=False).head(20)[
        ["source","strategy_id","regime_53","regime_desc","parent_winners","parent_losers",
         "shave_factor","shave_op","shave_threshold","island_n","island_wins","island_losses","island_wr","wr_lift"]
    ].to_string(index=False))

print(f"\n=== LOSER CONTRAST BANK (parent bucket only — other buckets per future shave) ===")
print(f"  total parent losers: {len(losers):,}")
print(f"  per (source × strategy) count:")
print(losers.groupby(["source","strategy_id"]).size().sort_values(ascending=False).head(15).to_string())

print(f"\nsaved -> {OUT_DIR}/")
print(f"  moving_regime_seeds.csv             ({len(seeds)} seeds)")
print(f"  moving_regime_loser_bank.csv        ({len(losers)} parent losers)")
