"""Build the mirrored loser_contrast_bank artifact.

Buckets:
  - parent
  - rejected_by_shave
  - residual
  - false_friend_sibling
"""
from pathlib import Path
import re

import numpy as np
import pandas as pd

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
PARQUET = ROOT / "all_strategies_all_pairs_trades.parquet"
SEEDS = ROOT / "winner_island_sibling_seed_bank.csv"
FALSE_FRIENDS = ROOT / "winner-islands" / "fast_targeted_false_friend_siblings.csv"

OUT_DIR = ROOT
SUMMARY_MD = OUT_DIR / "loser_contrast_bank.md"
BANK_CSV = OUT_DIR / "loser_contrast_bank.csv"
INDEX_CSV = OUT_DIR / "loser_contrast_bank_seed_index.csv"
FALSE_INDEX_CSV = OUT_DIR / "loser_contrast_bank_false_friend_index.csv"

RULE_RE = re.compile(r'^([\w_]+)\s*(<=|>=|<|>|=|==)\s*(.+?)\s*$')
CAT_FACTORS = {"session_bucket"}


def normalize_factor_name(f):
    aliases = {
        "atr_ratio": "ATR_ratio",
        "rsi14": "RSI14",
        "bb_compress": "BB_compress",
        "price_pos": "price_pos",
        "volume_ratio": "volume_ratio",
        "adx14": "ADX14",
        "session_bucket": "session_bucket",
        "hour_utc": "hour_utc",
    }
    return aliases.get(f.lower(), f)


def parse_rule(rt):
    if pd.isna(rt) or not isinstance(rt, str) or rt.strip() in ("", "ALL"):
        return []
    parts = re.split(r"\s+AND\s+", rt)
    out = []
    for p in parts:
        m = RULE_RE.match(p.strip())
        if not m:
            continue
        field, op, raw = m.groups()
        op = "=" if op == "==" else op
        field = normalize_factor_name(field)
        raw = raw.strip()
        if field in CAT_FACTORS:
            value = raw
        else:
            try:
                value = float(raw)
            except ValueError:
                continue
        out.append((field, op, value))
    return out


def apply_rule(sub, rule):
    if not rule:
        return np.ones(len(sub), dtype=bool)
    m = np.ones(len(sub), dtype=bool)
    for field, op, thr in rule:
        if field not in sub.columns:
            return np.zeros(len(sub), dtype=bool)
        if field in CAT_FACTORS:
            col = sub[field].astype(str).values
            if op == "=":
                m &= col == str(thr)
            else:
                return np.zeros(len(sub), dtype=bool)
            continue
        col = sub[field].astype(float).values
        if op == "<=":
            m &= col <= thr
        elif op == ">=":
            m &= col >= thr
        elif op == "<":
            m &= col < thr
        elif op == ">":
            m &= col > thr
        elif op == "=":
            m &= col == thr
    return m


def row_payload(t):
    return {
        c: t[c]
        for c in (
            "entry_ts", "realized_R", "mfe_R", "mae_R", "exit_reason",
            "session_bucket", "hour_utc", "weekday",
            "ADX14", "ATR_ratio", "BB_compress", "RSI14",
            "price_pos", "volume_ratio"
        )
        if c in t.index
    }


print("loading parquet ...", flush=True)
keep_cols = [
    "pair", "pair_family", "strategy_id", "category", "direction",
    "entry_ts", "realized_R", "mfe_R", "mae_R", "exit_reason",
    "technical_regime_53", "technical_regime_desc",
    "session_bucket", "hour_utc",
    "ADX14", "ATR_ratio", "BB_compress", "RSI14", "price_pos", "volume_ratio",
    "is_win"
]
df = pd.read_parquet(PARQUET, columns=keep_cols)
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
df["weekday"] = df["entry_ts"].dt.weekday.astype("int8")
print(f"  {len(df):,} rows", flush=True)

print("loading sibling seed bank ...", flush=True)
seeds = pd.read_csv(SEEDS)
print(f"  {len(seeds)} seeds across {seeds.groupby(['strategy_id','pair','direction','technical_regime_53']).ngroups} parent cells", flush=True)

false_friends = pd.DataFrame()
if FALSE_FRIENDS.exists():
    print("loading false-friend sibling bank ...", flush=True)
    false_friends = pd.read_csv(FALSE_FRIENDS)
    print(f"  {len(false_friends)} false-friend candidates", flush=True)
else:
    print("false-friend sibling file not found; continuing without fourth bucket", flush=True)

parent_loser_rows = []
rejected_rows = []
residual_rows = []
false_friend_rows = []
seed_index_rows = []
false_friend_index_rows = []

seeds = seeds.reset_index(drop=False).rename(columns={"index": "seed_id"})
if not false_friends.empty:
    false_friends = false_friends.reset_index(drop=False).rename(columns={"index": "false_friend_id"})

print(f"\nprocessing {len(seeds)} seeds ...", flush=True)

parent_cache = {}
parent_loser_seen = set()

for _, seed in seeds.iterrows():
    sid = int(seed["seed_id"])
    strat = seed["strategy_id"]
    pair = seed["pair"]
    dirn = seed["direction"]
    reg = seed["technical_regime_53"]
    rule_str = seed.get("rule", "")
    rule_norm = parse_rule(rule_str)

    parent_key = (strat, pair, dirn, reg)
    if parent_key not in parent_cache:
        parent_cache[parent_key] = df[
            (df.strategy_id == strat)
            & (df.pair == pair)
            & (df.direction == dirn)
            & (df.technical_regime_53 == reg)
        ].copy()

    parent = parent_cache[parent_key]
    parent_losers = parent[parent.is_win == False]

    in_rule_losers = parent_losers[apply_rule(parent_losers, rule_norm).astype(bool)]
    rejected_losers = parent_losers.loc[~apply_rule(parent_losers, rule_norm).astype(bool)]

    if parent_key not in parent_loser_seen:
        parent_loser_seen.add(parent_key)
        for _, t in parent_losers.iterrows():
            parent_loser_rows.append({
                "seed_id": -1,
                "false_friend_id": pd.NA,
                "matched_rule": "",
                "parent_strategy": strat,
                "parent_pair": pair,
                "parent_direction": dirn,
                "parent_regime": reg,
                "bucket": "parent",
                **row_payload(t),
            })

    for _, t in rejected_losers.iterrows():
        rejected_rows.append({
            "seed_id": sid,
            "false_friend_id": pd.NA,
            "matched_rule": rule_str,
            "parent_strategy": strat,
            "parent_pair": pair,
            "parent_direction": dirn,
            "parent_regime": reg,
            "bucket": "rejected_by_shave",
            **row_payload(t),
        })

    for _, t in in_rule_losers.iterrows():
        residual_rows.append({
            "seed_id": sid,
            "false_friend_id": pd.NA,
            "matched_rule": rule_str,
            "parent_strategy": strat,
            "parent_pair": pair,
            "parent_direction": dirn,
            "parent_regime": reg,
            "bucket": "residual",
            **row_payload(t),
        })

    seed_index_rows.append({
        "seed_id": sid,
        "strategy_id": strat,
        "pair": pair,
        "direction": dirn,
        "technical_regime_53": reg,
        "rule": rule_str,
        "parent_n": len(parent),
        "parent_winners": int(parent["is_win"].sum()),
        "parent_losers": int((~parent["is_win"]).sum()),
        "rejected_by_shave": int(len(rejected_losers)),
        "residual_losers": int(len(in_rule_losers)),
        "factor_signature": seed.get("factor_signature", ""),
        "is_pure_seed": bool(seed.get("is_pure_seed", False)),
        "is_holdout_clean_seed": bool(seed.get("is_holdout_clean_seed", False)),
        "purity_class": (
            "pure" if seed.get("is_pure_seed") else
            ("holdout_clean" if seed.get("is_holdout_clean_seed") else
             "near_pure" if (int(seed.get("losses", 0)) <= 2 and int(seed.get("wins", 0)) >= 10) else
             "exploratory")
        ),
    })

if not false_friends.empty:
    print(f"\nprocessing {len(false_friends)} false-friend siblings ...", flush=True)
    for _, ff in false_friends.iterrows():
        ffid = int(ff["false_friend_id"])
        strat = ff["strategy_id"]
        pair = ff["pair"]
        dirn = ff["direction"]
        reg = ff["technical_regime_53"]
        rule_str = ff.get("rule", "")
        rule_norm = parse_rule(rule_str)

        parent_key = (strat, pair, dirn, reg)
        if parent_key not in parent_cache:
            parent_cache[parent_key] = df[
                (df.strategy_id == strat)
                & (df.pair == pair)
                & (df.direction == dirn)
                & (df.technical_regime_53 == reg)
            ].copy()

        parent = parent_cache[parent_key]
        parent_losers = parent[parent.is_win == False]
        matched_losers = parent_losers[apply_rule(parent_losers, rule_norm).astype(bool)]

        for _, t in matched_losers.iterrows():
            false_friend_rows.append({
                "seed_id": pd.NA,
                "false_friend_id": ffid,
                "matched_rule": rule_str,
                "parent_strategy": strat,
                "parent_pair": pair,
                "parent_direction": dirn,
                "parent_regime": reg,
                "bucket": "false_friend_sibling",
                **row_payload(t),
            })

        false_friend_index_rows.append({
            "false_friend_id": ffid,
            "strategy_id": strat,
            "pair": pair,
            "direction": dirn,
            "technical_regime_53": reg,
            "rule": rule_str,
            "factor_signature": ff.get("factor_signature", ""),
            "false_friend_reason": ff.get("false_friend_reason", ""),
            "parent_n": len(parent),
            "parent_winners": int(parent["is_win"].sum()),
            "parent_losers": int((~parent["is_win"]).sum()),
            "false_friend_n": int(ff.get("n", 0)),
            "false_friend_wins": int(ff.get("wins", 0)),
            "false_friend_losses": int(len(matched_losers)),
            "wr": float(ff.get("wr", 0.0)),
            "mean_R": float(ff.get("mean_R", 0.0)),
        })

all_loser_rows = parent_loser_rows + rejected_rows + residual_rows + false_friend_rows
bank = pd.DataFrame(all_loser_rows)
front = ["seed_id", "false_friend_id", "bucket", "matched_rule", "parent_strategy", "parent_pair", "parent_direction", "parent_regime", "entry_ts"]
rest = [c for c in bank.columns if c not in front]
bank = bank[front + rest]
bank.to_csv(BANK_CSV, index=False)

print(f"\nloser_contrast_bank.csv: {len(bank):,} rows", flush=True)
print(f"  parent rows:              {len(parent_loser_rows):,}")
print(f"  rejected_by_shave:        {len(rejected_rows):,}")
print(f"  residual:                 {len(residual_rows):,}")
print(f"  false_friend_sibling:     {len(false_friend_rows):,}")

idx = pd.DataFrame(seed_index_rows)
idx.to_csv(INDEX_CSV, index=False)
print(f"\nloser_contrast_bank_seed_index.csv: {len(idx)} rows", flush=True)

ff_idx = pd.DataFrame(false_friend_index_rows)
ff_idx.to_csv(FALSE_INDEX_CSV, index=False)
print(f"loser_contrast_bank_false_friend_index.csv: {len(ff_idx)} rows", flush=True)

md_lines = [
    "# Loser Contrast Bank",
    "",
    "Mirrored archive of losing trades for every seed in the winner sibling bank, plus false-friend sibling traps.",
    "Built from `winner_island_sibling_seed_bank.csv`, `fast_targeted_false_friend_siblings.csv`, and `all_strategies_all_pairs_trades.parquet`.",
    "Per Brock 2026-05-14 doctrine: keep losers as contrast inventory, not noise.",
    "",
    "## Summary",
    f"- Seeds processed: {len(seeds)}",
    f"- Distinct parent cells: {len(parent_loser_seen)}",
    f"- Parent losers: {len(parent_loser_rows):,} rows",
    f"- Rejected-by-shave losers: {len(rejected_rows):,} rows",
    f"- Residual losers: {len(residual_rows):,} rows",
    f"- False-friend sibling losers: {len(false_friend_rows):,} rows",
    "",
    "## Files",
    f"- `loser_contrast_bank.csv` — full row-level loser archive ({len(bank):,} rows)",
    f"- `loser_contrast_bank_seed_index.csv` — per-seed loser counts + purity class",
    f"- `loser_contrast_bank_false_friend_index.csv` — per-false-friend trap counts",
    "",
    "## Purity class distribution",
    "```",
    idx["purity_class"].value_counts().to_string(),
    "```",
    "",
    "## Schema (loser_contrast_bank.csv)",
    "```",
    "seed_id / false_friend_id  — one is populated depending on artifact lineage",
    "bucket                     — 'parent' | 'rejected_by_shave' | 'residual' | 'false_friend_sibling'",
    "matched_rule               — rule that defined the winner seed or false-friend trap",
    "parent_strategy, parent_pair, parent_direction, parent_regime",
    "entry_ts, realized_R, mfe_R, mae_R, exit_reason",
    "session_bucket, hour_utc, weekday",
    "ADX14, ATR_ratio, BB_compress, RSI14, price_pos, volume_ratio",
    "```",
]
SUMMARY_MD.write_text("\n".join(md_lines))
print(f"\nsaved markdown summary: {SUMMARY_MD}")
