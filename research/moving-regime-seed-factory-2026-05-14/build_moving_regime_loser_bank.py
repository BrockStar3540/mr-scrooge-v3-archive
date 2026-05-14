"""Extend the moving-regime loser bank to all 4 buckets.

Existing state (moving_regime_loser_bank.csv): only `parent` bucket.

Builds:
  - rejected_by_shave  — parent losers where the seed's shave rule is FALSE
  - residual           — parent losers where the seed's shave rule is TRUE
  - false_friend_sibling — losers from permissive sibling shaves that look
                            promising but include enough losers to not pass
                            the strict winner-island purity bar
Plus a per-seed index (counts in each bucket).

Per Brock's seed-factory doctrine:
  bucket parent             — full reference loser population for the parent
  bucket rejected_by_shave  — what the seed claims it would have skipped
  bucket residual           — what fell through despite the shave (true cost)
  bucket false_friend_sibling — siblings that look like seeds but bring losers

Inputs read by this script:
  - all_strategies_all_pairs_trades.parquet  (textbook)
  - trainer-replay-v2/*.parquet               (V3 probes)
  - dense_regime53_lookup_last6mo.parquet     (per-bar regime53)
  - moving-regime-seed-factory/moving_regime_seeds.csv

Outputs:
  - moving-regime-seed-factory/moving_regime_loser_bank_extended.csv  (4 buckets)
  - moving-regime-seed-factory/moving_regime_seed_index.csv           (per-seed)
"""
import pandas as pd
import numpy as np
import glob
from pathlib import Path

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
FOUND = ROOT / "all_strategies_all_pairs_trades.parquet"
DENSE = ROOT / "dense_regime53_lookup_last6mo.parquet"
TRAINER_DIR = ROOT / "trainer-replay-v2"
OUT_DIR = ROOT / "moving-regime-seed-factory"
SEEDS_CSV = OUT_DIR / "moving_regime_seeds.csv"

CUTOFF = pd.Timestamp("2025-10-22", tz="UTC")
HARD_LATEST = pd.Timestamp("2026-04-22", tz="UTC")
DEAD_REGIMES = {"R04", "T07", "Z01"}

FACTORS = ["ATR_ratio", "BB_compress", "ADX14", "RSI14",
           "close_pos", "EMA_slope", "hour_utc"]

# Permissive thresholds for false_friend_sibling discovery — looser than
# the seed factory's purity bar so we capture "looks like a winner island
# but contaminated with losers" candidates.
FF_MIN_ISLAND = 6
FF_MIN_PURITY = 0.40       # 40%+ within-island WR
FF_MIN_LIFT = 1.20
FF_REJECT_PURE = True      # exclude actual pure seeds (already in seed bank)


# --------------------------------------------------------------------------
# Data loading — mirror the seed factory exactly
# --------------------------------------------------------------------------

print("loading dense regime53 lookup ...", flush=True)
lookup = pd.read_parquet(DENSE)
lookup["ts"] = pd.to_datetime(lookup["ts"], utc=True)

print("loading textbook trades + filtering to moving regimes ...", flush=True)
foundational = pd.read_parquet(FOUND, columns=[
    "strategy_id", "pair", "pair_family", "direction", "entry_ts",
    "is_win", "realized_R",
])
foundational["entry_ts"] = pd.to_datetime(foundational["entry_ts"], utc=True)
foundational = foundational[(foundational.entry_ts >= CUTOFF) & (foundational.entry_ts <= HARD_LATEST)].copy()
foundational = foundational.merge(
    lookup.rename(columns={"ts": "entry_ts"}),
    on=["pair", "entry_ts"], how="left",
)
foundational = foundational[~foundational.technical_regime_53.isin(DEAD_REGIMES)].copy()
foundational["source"] = "textbook"
print(f"  textbook moving: {len(foundational):,}", flush=True)

print("loading trainer probes + filtering to moving regimes ...", flush=True)
parts = []
for f in sorted(glob.glob(str(TRAINER_DIR / "*.parquet"))):
    parts.append(pd.read_parquet(f, columns=[
        "pair", "entry_ts", "direction", "probe_name", "realized_r", "filled",
    ]))
trainer = pd.concat(parts, ignore_index=True)
trainer["entry_ts"] = pd.to_datetime(trainer["entry_ts"], utc=True)
trainer = trainer[(trainer.entry_ts >= CUTOFF) & (trainer.entry_ts <= HARD_LATEST)].copy()
trainer = trainer[trainer.filled].copy()
trainer["is_win"] = trainer["realized_r"] > 0
trainer = trainer.rename(columns={"probe_name": "strategy_id", "realized_r": "realized_R"})
trainer = trainer.merge(
    lookup.rename(columns={"ts": "entry_ts"}),
    on=["pair", "entry_ts"], how="left",
)
trainer = trainer[~trainer.technical_regime_53.isin(DEAD_REGIMES)].copy()
trainer["source"] = "v3_trainer_probe"

PAIR_FAMILY_MAP = {}
for p in ["EUR_USD", "GBP_USD", "AUD_USD", "NZD_USD", "USD_JPY", "USD_CHF", "USD_CAD", "USD_MXN"]:
    PAIR_FAMILY_MAP[p] = "usd_base"
for p in ["EUR_GBP", "EUR_AUD", "EUR_NZD", "EUR_CAD", "EUR_CHF", "EUR_JPY"]:
    PAIR_FAMILY_MAP[p] = "eur_cross"
for p in ["GBP_AUD", "GBP_NZD", "GBP_CAD", "GBP_CHF", "GBP_JPY"]:
    PAIR_FAMILY_MAP[p] = "gbp_cross"
for p in ["AUD_CAD", "AUD_CHF", "AUD_JPY", "AUD_NZD", "CAD_JPY", "CHF_JPY", "NZD_JPY"]:
    PAIR_FAMILY_MAP[p] = "antipodean_cross"
trainer["pair_family"] = trainer["pair"].map(PAIR_FAMILY_MAP)
print(f"  trainer moving:  {len(trainer):,}", flush=True)

cols = ["source", "strategy_id", "pair", "pair_family", "direction", "entry_ts",
        "is_win", "realized_R", "technical_regime_53", "technical_regime_desc",
        "ATR14", "ATR_ratio", "BB_width", "BB_compress", "ADX14", "EMA_slope",
        "RSI14", "close_pos"]
unified = pd.concat([foundational[cols], trainer[cols]], ignore_index=True)
unified["hour_utc"] = unified["entry_ts"].dt.hour.astype(int)
unified["weekday"] = unified["entry_ts"].dt.weekday.astype(int)
print(f"unified moving-regime: {len(unified):,} ({int(unified.is_win.sum())}W / {int((~unified.is_win).sum())}L)", flush=True)


# --------------------------------------------------------------------------
# Seed rule parsing
# --------------------------------------------------------------------------

print("\nloading seed bank ...", flush=True)
seeds = pd.read_csv(SEEDS_CSV)
seeds = seeds.reset_index(drop=False).rename(columns={"index": "seed_id"})
print(f"  {len(seeds)} seeds", flush=True)


def apply_rule(df: pd.DataFrame, factor: str, op: str, threshold) -> np.ndarray:
    """Apply a (factor, op, threshold) rule. Returns boolean mask."""
    if factor not in df.columns:
        return np.zeros(len(df), dtype=bool)
    col = df[factor].astype(float).values
    thr = float(threshold)
    if op == "<=": return col <= thr
    if op == ">=": return col >= thr
    if op == "<":  return col < thr
    if op == ">":  return col > thr
    if op in ("=", "=="): return col == thr
    return np.zeros(len(df), dtype=bool)


def parse_two_factor_rule(seed):
    """Seed factories produced 'f1+f2' factor + a textual op like
    '(<=0.5) AND (>30)'. Returns list[(factor, op, threshold)] or None."""
    fac = str(seed["shave_factor"])
    op_str = str(seed["shave_op"])
    thr_str = str(seed["shave_threshold"])
    if "+" not in fac:
        return None
    f1, f2 = fac.split("+", 1)
    # The threshold string was tuple-repr'd, e.g. "(0.4, 30.5)"
    try:
        thr_str_clean = thr_str.strip("()")
        t1, t2 = [float(x.strip()) for x in thr_str_clean.split(",")]
    except Exception:
        return None
    # op_str like "(<=0.4) AND (>30.5)" — extract the two ops
    import re
    ops = re.findall(r"([<>]=?|==?)", op_str)
    if len(ops) < 2:
        return None
    return [(f1, ops[0], t1), (f2, ops[1], t2)]


# --------------------------------------------------------------------------
# Per-seed bucketing (parent / rejected_by_shave / residual)
# --------------------------------------------------------------------------

print("\nbuilding parent + rejected + residual buckets ...", flush=True)
parent_cache = {}
parent_seen = set()
bank_rows = []
seed_index_rows = []

LOSER_COLS = ["pair", "direction", "entry_ts", "realized_R",
              "ATR14", "ATR_ratio", "BB_compress", "ADX14",
              "RSI14", "close_pos", "EMA_slope", "hour_utc", "weekday"]


def loser_payload(t):
    return {c: t[c] for c in LOSER_COLS if c in t.index}


for _, seed in seeds.iterrows():
    sid = int(seed["seed_id"])
    src = seed["source"]
    strat = seed["strategy_id"]
    reg = seed["regime_53"]

    pkey = (src, strat, reg)
    if pkey not in parent_cache:
        parent_cache[pkey] = unified[
            (unified.source == src)
            & (unified.strategy_id == strat)
            & (unified.technical_regime_53 == reg)
        ].copy()
    parent = parent_cache[pkey]
    parent_losers = parent[~parent.is_win]

    # Apply rule(s)
    two_factor = parse_two_factor_rule(seed)
    if two_factor is not None:
        mask = np.ones(len(parent_losers), dtype=bool)
        for (f, op, t) in two_factor:
            mask &= apply_rule(parent_losers, f, op, t)
    else:
        mask = apply_rule(parent_losers,
                          seed["shave_factor"],
                          seed["shave_op"],
                          seed["shave_threshold"])

    in_rule_losers = parent_losers.loc[mask]
    rejected_losers = parent_losers.loc[~mask]

    # parent bucket — emit once per parent_key
    if pkey not in parent_seen:
        parent_seen.add(pkey)
        for _, t in parent_losers.iterrows():
            bank_rows.append({
                "seed_id": -1,
                "bucket": "parent",
                "source": src, "strategy_id": strat, "regime_53": reg,
                "matched_rule": "",
                **loser_payload(t),
            })

    rule_repr = f"{seed['shave_factor']} {seed['shave_op']} {seed['shave_threshold']}"
    for _, t in rejected_losers.iterrows():
        bank_rows.append({
            "seed_id": sid,
            "bucket": "rejected_by_shave",
            "source": src, "strategy_id": strat, "regime_53": reg,
            "matched_rule": rule_repr,
            **loser_payload(t),
        })
    for _, t in in_rule_losers.iterrows():
        bank_rows.append({
            "seed_id": sid,
            "bucket": "residual",
            "source": src, "strategy_id": strat, "regime_53": reg,
            "matched_rule": rule_repr,
            **loser_payload(t),
        })

    seed_index_rows.append({
        "seed_id": sid,
        "source": src, "strategy_id": strat,
        "regime_53": reg, "regime_desc": seed.get("regime_desc", ""),
        "rule": rule_repr,
        "parent_n": int(len(parent)),
        "parent_winners": int(parent.is_win.sum()),
        "parent_losers": int(len(parent_losers)),
        "island_n": int(seed["island_n"]),
        "island_wins": int(seed["island_wins"]),
        "island_losses": int(seed["island_losses"]),
        "island_wr": float(seed["island_wr"]),
        "rejected_by_shave": int(len(rejected_losers)),
        "residual_losers": int(len(in_rule_losers)),
        "purity_class": seed.get("purity_class", ""),
    })

print(f"  bank rows so far: {len(bank_rows):,}", flush=True)


# --------------------------------------------------------------------------
# false_friend_sibling pass — permissive shave around the same parents
# --------------------------------------------------------------------------

print("\nbuilding false_friend_sibling bucket (permissive shaves) ...", flush=True)


def permissive_islands(parent: pd.DataFrame, factor: str):
    """Enumerate (factor, op, threshold) shaves at quantile points that meet
    the permissive purity bar but are NOT pure (so they're 'false friends')."""
    if factor not in parent.columns or parent[factor].isna().all():
        return []
    try:
        qs = parent[factor].quantile([0.2, 0.4, 0.5, 0.6, 0.8]).values
    except Exception:
        return []
    out = []
    parent_wr = parent.is_win.mean()
    for thr in qs:
        for op in ("<=", ">"):
            mask = (parent[factor] <= thr) if op == "<=" else (parent[factor] > thr)
            island = parent[mask]
            if len(island) < FF_MIN_ISLAND:
                continue
            iw = int(island.is_win.sum())
            il = int(len(island) - iw)
            purity = iw / max(1, len(island))
            if purity < FF_MIN_PURITY:
                continue
            lift = purity / max(0.05, parent_wr)
            if lift < FF_MIN_LIFT:
                continue
            if FF_REJECT_PURE and il == 0:
                continue
            out.append({
                "factor": factor, "op": op, "threshold": float(thr),
                "island_n": int(len(island)),
                "island_wins": iw, "island_losses": il,
                "island_wr": purity, "lift": lift,
            })
    return out


ff_id = 0
ff_index_rows = []
parent_cells_examined = set()

for _, seed in seeds.iterrows():
    src = seed["source"]; strat = seed["strategy_id"]; reg = seed["regime_53"]
    pkey = (src, strat, reg)
    if pkey in parent_cells_examined:
        continue
    parent_cells_examined.add(pkey)
    parent = parent_cache[pkey]
    if parent.is_win.sum() < 10:
        continue
    # Run permissive shave across all factors
    for factor in FACTORS:
        cands = permissive_islands(parent, factor)
        for c in cands:
            # Build mask, capture the island's losers (these are the
            # false-friend siblings' "cost" — they LOOK like part of a winner
            # island but they're losers)
            mask = (parent[c["factor"]] <= c["threshold"]) if c["op"] == "<=" else (parent[c["factor"]] > c["threshold"])
            island = parent[mask]
            island_losers = island[~island.is_win]
            if len(island_losers) == 0:
                continue
            rule_repr = f"{c['factor']} {c['op']} {c['threshold']:.4g}"
            for _, t in island_losers.iterrows():
                bank_rows.append({
                    "seed_id": -2,
                    "bucket": "false_friend_sibling",
                    "source": src, "strategy_id": strat, "regime_53": reg,
                    "matched_rule": rule_repr,
                    "false_friend_id": ff_id,
                    **loser_payload(t),
                })
            ff_index_rows.append({
                "false_friend_id": ff_id,
                "source": src, "strategy_id": strat, "regime_53": reg,
                "rule": rule_repr,
                "island_n": c["island_n"],
                "island_wins": c["island_wins"],
                "island_losses": c["island_losses"],
                "island_wr": round(c["island_wr"], 3),
                "lift": round(c["lift"], 3),
            })
            ff_id += 1

print(f"  false_friend siblings: {ff_id}", flush=True)


# --------------------------------------------------------------------------
# Save
# --------------------------------------------------------------------------

print("\nsaving ...", flush=True)
bank = pd.DataFrame(bank_rows)
seed_index = pd.DataFrame(seed_index_rows)
ff_index = pd.DataFrame(ff_index_rows)

bank.to_csv(OUT_DIR / "moving_regime_loser_bank_extended.csv", index=False)
seed_index.to_csv(OUT_DIR / "moving_regime_seed_index.csv", index=False)
ff_index.to_csv(OUT_DIR / "moving_regime_false_friend_index.csv", index=False)

# Summary
print("\n=== LOSER BANK SUMMARY ===")
print(bank.groupby("bucket").size().to_string())
print(f"\ntotal rows: {len(bank):,}")
print(f"unique parent cells: {bank[bank.bucket=='parent'][['source','strategy_id','regime_53']].drop_duplicates().shape[0]}")
print(f"\nseed index rows: {len(seed_index)}")
print(f"false-friend index rows: {len(ff_index)}")

print(f"\n=== TOP SEEDS BY REJECTION POWER (rejected / parent_losers) ===")
si = seed_index.copy()
si["rejection_rate"] = si["rejected_by_shave"] / si["parent_losers"].replace(0, np.nan)
print(si.sort_values("rejection_rate", ascending=False).head(15)[
    ["seed_id", "source", "strategy_id", "regime_53", "rule",
     "parent_losers", "rejected_by_shave", "residual_losers", "rejection_rate"]
].to_string(index=False))

print(f"\nsaved to {OUT_DIR}/")
print(f"  moving_regime_loser_bank_extended.csv  ({len(bank):,} rows)")
print(f"  moving_regime_seed_index.csv           ({len(seed_index)} rows)")
print(f"  moving_regime_false_friend_index.csv   ({len(ff_index)} rows)")
