"""Build the mirrored loser_contrast_bank artifact.

For each seed in winner_island_sibling_seed_bank.csv:
  - parent_losers:           losing trades in the (strategy, pair, direction,
                             technical_regime_53) cell that birthed the seed
  - rejected_by_shave:       losing trades in the parent NOT matching the
                             seed's rule (the seeds the shave excluded)
  - residual_losers:         losing trades INSIDE the seed's rule (the seed's
                             own internal failure modes — typically 0-2 per seed)

The fourth bucket (false_friend_siblings) requires re-running the shaver with
permissive output. Not produced here; flagged as a separate task.

Schema:
  seed_id           — synthetic ID matching the winner-bank seed
  bucket            — "parent" | "rejected_by_shave" | "residual"
  entry_ts, pair, strategy_id, direction, technical_regime_53,
  realized_R, mfe_R, mae_R, ADX14, ATR_ratio, BB_compress, RSI14,
  price_pos, volume_ratio, session_bucket, hour_utc, weekday
"""
import pandas as pd
import numpy as np
import re
import sys
from pathlib import Path

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
PARQUET = ROOT / "all_strategies_all_pairs_trades.parquet"
SEEDS = ROOT / "winner_island_sibling_seed_bank.csv"
OUT_DIR = ROOT
SUMMARY_MD = OUT_DIR / "loser_contrast_bank.md"
BANK_CSV = OUT_DIR / "loser_contrast_bank.csv"
INDEX_CSV = OUT_DIR / "loser_contrast_bank_seed_index.csv"

print("loading parquet ...", flush=True)
keep_cols = ["pair","pair_family","strategy_id","category","direction",
             "entry_ts","realized_R","mfe_R","mae_R","exit_reason",
             "technical_regime_53","technical_regime_desc",
             "session_bucket","hour_utc",
             "ADX14","ATR_ratio","BB_compress","RSI14","price_pos","volume_ratio",
             "is_win"]
df = pd.read_parquet(PARQUET, columns=keep_cols)
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
df["weekday"] = df["entry_ts"].dt.weekday.astype("int8")
print(f"  {len(df):,} rows", flush=True)

print("loading sibling seed bank ...", flush=True)
seeds = pd.read_csv(SEEDS)
print(f"  {len(seeds)} seeds across {seeds.groupby(['strategy_id','pair','direction','technical_regime_53']).ngroups} parent cells", flush=True)


def parse_rule(rt):
    if pd.isna(rt) or not isinstance(rt, str) or rt.strip() in ("", "ALL"):
        return []
    parts = re.split(r"\s+AND\s+", rt)
    out = []
    for p in parts:
        m = re.match(r"^([\w_]+)\s*(<=|>=|<|>|=|==)\s*(-?[\d.eE+]+)$", p.strip())
        if m:
            op = m.group(2)
            if op == "==": op = "="
            out.append((m.group(1), op, float(m.group(3))))
    return out


def apply_rule(sub, rule):
    if not rule:
        return np.ones(len(sub), dtype=bool)
    m = np.ones(len(sub), dtype=bool)
    for f, op, thr in rule:
        if f not in sub.columns:
            return np.zeros(len(sub), dtype=bool)
        col = sub[f].values
        if op == "<=": m &= col <= thr
        elif op == ">=": m &= col >= thr
        elif op == "<":  m &= col <  thr
        elif op == ">":  m &= col >  thr
        elif op == "=":  m &= col == thr
    return m


# Identify factor name aliases the rules may use
def normalize_factor_name(f):
    aliases = {
        "atr_ratio": "ATR_ratio",
        "rsi14":     "RSI14",
        "bb_compress": "BB_compress",
        "price_pos": "price_pos",
        "volume_ratio": "volume_ratio",
        "adx14":     "ADX14",
        "session_bucket": "session_bucket",
        "hour_utc":  "hour_utc",
    }
    return aliases.get(f.lower(), f)


# Build buckets
parent_loser_rows = []
rejected_rows = []
residual_rows = []
seed_index_rows = []

# Stable seed_id from (strategy, pair, direction, regime, factor_signature)
seeds = seeds.reset_index(drop=False).rename(columns={"index": "seed_id"})
print(f"\nprocessing {len(seeds)} seeds ...", flush=True)

# Cache parent-cell slices to avoid redundant filtering
parent_cache = {}
parent_loser_seen = set()  # avoid duplicating parent_losers across siblings sharing a parent
n_done = 0
for _, seed in seeds.iterrows():
    sid = int(seed["seed_id"])
    strat = seed["strategy_id"]; pair = seed["pair"]; dirn = seed["direction"]
    reg = seed["technical_regime_53"]
    rule_str = seed.get("rule", "")
    rule_norm = [(normalize_factor_name(f), op, thr) for (f, op, thr) in parse_rule(rule_str)]

    parent_key = (strat, pair, dirn, reg)
    if parent_key not in parent_cache:
        parent_cache[parent_key] = df[(df.strategy_id == strat) & (df.pair == pair)
                                       & (df.direction == dirn) & (df.technical_regime_53 == reg)].copy()
    parent = parent_cache[parent_key]
    parent_losers = parent[parent.is_win == False]

    if rule_norm:
        in_rule_mask = apply_rule(parent, rule_norm)
    else:
        in_rule_mask = np.ones(len(parent), dtype=bool)

    in_rule_losers = parent_losers[apply_rule(parent_losers, rule_norm).astype(bool)]
    rejected_losers = parent_losers.loc[~apply_rule(parent_losers, rule_norm).astype(bool)]

    # Parent losers: emit only once per parent_key
    if parent_key not in parent_loser_seen:
        parent_loser_seen.add(parent_key)
        for _, t in parent_losers.iterrows():
            parent_loser_rows.append({
                "seed_id": -1,            # parent losers are pre-seed
                "parent_strategy": strat, "parent_pair": pair, "parent_direction": dirn,
                "parent_regime": reg,
                "bucket": "parent",
                **{c: t[c] for c in ("entry_ts","realized_R","mfe_R","mae_R","exit_reason",
                                       "session_bucket","hour_utc","weekday",
                                       "ADX14","ATR_ratio","BB_compress","RSI14",
                                       "price_pos","volume_ratio") if c in t.index},
            })

    for _, t in rejected_losers.iterrows():
        rejected_rows.append({
            "seed_id": sid,
            "parent_strategy": strat, "parent_pair": pair, "parent_direction": dirn,
            "parent_regime": reg,
            "bucket": "rejected_by_shave",
            **{c: t[c] for c in ("entry_ts","realized_R","mfe_R","mae_R","exit_reason",
                                   "session_bucket","hour_utc","weekday",
                                   "ADX14","ATR_ratio","BB_compress","RSI14",
                                   "price_pos","volume_ratio") if c in t.index},
        })

    for _, t in in_rule_losers.iterrows():
        residual_rows.append({
            "seed_id": sid,
            "parent_strategy": strat, "parent_pair": pair, "parent_direction": dirn,
            "parent_regime": reg,
            "bucket": "residual",
            **{c: t[c] for c in ("entry_ts","realized_R","mfe_R","mae_R","exit_reason",
                                   "session_bucket","hour_utc","weekday",
                                   "ADX14","ATR_ratio","BB_compress","RSI14",
                                   "price_pos","volume_ratio") if c in t.index},
        })

    seed_index_rows.append({
        "seed_id": sid,
        "strategy_id": strat, "pair": pair, "direction": dirn,
        "technical_regime_53": reg,
        "rule": rule_str,
        "parent_n":          len(parent),
        "parent_winners":    int(parent["is_win"].sum()),
        "parent_losers":     int((~parent["is_win"]).sum()),
        "rejected_by_shave": int(len(rejected_losers)),
        "residual_losers":   int(len(in_rule_losers)),
        "factor_signature":  seed.get("factor_signature", ""),
        "is_pure_seed":      bool(seed.get("is_pure_seed", False)),
        "is_holdout_clean_seed": bool(seed.get("is_holdout_clean_seed", False)),
        "purity_class": (
            "pure" if seed.get("is_pure_seed") else
            ("holdout_clean" if seed.get("is_holdout_clean_seed") else
             "near_pure" if (int(seed.get("losses", 0)) <= 2 and int(seed.get("wins", 0)) >= 10) else
             "exploratory")
        ),
    })

    n_done += 1
    if n_done % 50 == 0:
        print(f"  ... {n_done}/{len(seeds)}", flush=True)


# Combine + write
all_loser_rows = parent_loser_rows + rejected_rows + residual_rows
bank = pd.DataFrame(all_loser_rows)
# Stable column order
front = ["seed_id","bucket","parent_strategy","parent_pair","parent_direction","parent_regime","entry_ts"]
rest = [c for c in bank.columns if c not in front]
bank = bank[front + rest]
bank.to_csv(BANK_CSV, index=False)
print(f"\nloser_contrast_bank.csv: {len(bank):,} rows", flush=True)
print(f"  parent rows:           {len(parent_loser_rows):,}")
print(f"  rejected_by_shave:     {len(rejected_rows):,}")
print(f"  residual:              {len(residual_rows):,}")

idx = pd.DataFrame(seed_index_rows)
idx.to_csv(INDEX_CSV, index=False)
print(f"\nloser_contrast_bank_seed_index.csv: {len(idx)} rows (one per seed)", flush=True)
print(idx[["seed_id","strategy_id","pair","direction","parent_n","parent_winners",
           "parent_losers","rejected_by_shave","residual_losers","purity_class"]].head(15).to_string(index=False))

print(f"\npurity class counts:")
print(idx["purity_class"].value_counts().to_string())

# Markdown summary
md_lines = [
    "# Loser Contrast Bank",
    "",
    "Mirrored archive of losing trades for every seed in the winner sibling bank.",
    "Built from `winner_island_sibling_seed_bank.csv` + `all_strategies_all_pairs_trades.parquet`.",
    "Per Brock 2026-05-14 doctrine: keep losers as contrast inventory, not noise.",
    "",
    "## Summary",
    f"- Seeds processed: {len(seeds)}",
    f"- Distinct parent cells: {len(parent_loser_seen)}",
    f"- Parent losers: {len(parent_loser_rows):,} rows",
    f"- Rejected-by-shave losers: {len(rejected_rows):,} rows (per seed mirror)",
    f"- Residual losers: {len(residual_rows):,} rows (in-seed failure modes)",
    f"- False-friend siblings: NOT YET BUILT — requires re-running shaver with permissive output",
    "",
    "## Files",
    f"- `loser_contrast_bank.csv` — full row-level loser archive ({len(bank):,} rows)",
    f"- `loser_contrast_bank_seed_index.csv` — per-seed loser counts + purity class",
    "",
    "## Purity class distribution",
    "```",
    idx["purity_class"].value_counts().to_string(),
    "```",
    "",
    "## Schema (loser_contrast_bank.csv)",
    "```",
    "seed_id                — int. -1 = parent-cell loser (pre-seed background)",
    "                        Otherwise refers to a row in loser_contrast_bank_seed_index.csv",
    "bucket                 — 'parent' | 'rejected_by_shave' | 'residual'",
    "parent_strategy        — textbook strategy_id",
    "parent_pair            — currency pair",
    "parent_direction       — long | short",
    "parent_regime          — technical_regime_53 of the parent cell",
    "entry_ts               — UTC timestamp",
    "realized_R             — outcome (always <= 0 here, since this is the loser archive)",
    "mfe_R, mae_R           — within-trade extremes",
    "exit_reason            — stop | time | etc",
    "session_bucket, hour_utc, weekday",
    "ADX14, ATR_ratio, BB_compress, RSI14, price_pos, volume_ratio",
    "```",
    "",
    "## Use cases",
    "1. **Skip maps**: aggregate parent + rejected losers by factor combinations → conditions to avoid",
    "2. **Boundary definition**: rejected_by_shave losers per seed = the seed's mirrored exclusion set",
    "3. **Next-pass material**: residual_losers per near-pure seed = inputs for the recursive shave",
    "4. **Anti-regime discovery**: cluster the parent loser population for potential reversal seeds",
    "",
    "## Cross-references",
    "- [[seed-factory-doctrine]] — operating doctrine",
    "- [[scrooge-microbot-research-arc]] — research arc",
    "- `research/ohlcv-strategy-library-v0/winner_island_sibling_seed_bank.csv` — paired winner bank",
]
SUMMARY_MD.write_text("\n".join(md_lines))
print(f"\nsaved markdown summary: {SUMMARY_MD}")
