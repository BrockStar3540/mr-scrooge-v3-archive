"""Build initial routing table v1 from existing trade evidence.

Inputs:
  - all_strategies_all_pairs_trades.parquet  (textbook 56 strategies)
  - trainer-replay-v2/*.parquet              (V3 trainer probes — 10)
  - dense_regime53_lookup_last6mo.parquet    (per-bar regime53)

Window: last 6mo (2025-10-22 -> 2026-04-22).

Cell key: (regime53, pair, session_bucket, strategy_name, direction)
Attachment rule:
  - n >= 10
  - sum_R > 0
  - WR >= 0.30  (not pure noise)

Each row carries evidence (n, wins, sum_R, mean_R, wr) AND parameters
(r_target hint, score_boost derived from mean_R).

Session bucket — UTC hour buckets (DST-stable):
  asia          00-04 UTC   (Tokyo + Sydney)
  asia_late     04-06 UTC   (late Asia, pre-London)
  london_open   06-09 UTC   (London core)
  ny_open       09-13 UTC   (London-NY overlap + NY open)
  ny_mid        13-17 UTC   (NY full session)
  ny_close      17-21 UTC   (NY late + close)
  off_hours     21-24 UTC   (pre-Asia low-vol)

Output:
  routing_table_v1.parquet         — the table (CSV mirror for inspection)
  routing_table_summary.md         — counts + top cells
"""
from pathlib import Path
import pandas as pd
import numpy as np
import glob

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
FOUND = ROOT / "all_strategies_all_pairs_trades.parquet"
DENSE = ROOT / "dense_regime53_lookup_last6mo.parquet"
TRAINER_DIR = ROOT / "trainer-replay-v2"
OUT_DIR = ROOT / "routing-table-v1"
OUT_DIR.mkdir(exist_ok=True)

CUTOFF = pd.Timestamp("2025-10-22", tz="UTC")
HARD_LATEST = pd.Timestamp("2026-04-22", tz="UTC")

# Attachment thresholds
MIN_N = 10
MIN_WR = 0.30


def session_bucket(hour_utc):
    if 0 <= hour_utc < 4:   return "asia"
    if 4 <= hour_utc < 6:   return "asia_late"
    if 6 <= hour_utc < 9:   return "london_open"
    if 9 <= hour_utc < 13:  return "ny_open"
    if 13 <= hour_utc < 17: return "ny_mid"
    if 17 <= hour_utc < 21: return "ny_close"
    return "off_hours"


def family_for_strategy(name):
    """Map strategy name -> V3 family for downstream routing/scoring."""
    # V3 trainer probes
    PROBE_FAMILY = {
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
    if name in PROBE_FAMILY:
        return PROBE_FAMILY[name]
    # Textbook strategy heuristic by prefix
    n = name.lower()
    if n.startswith("tf"):  return "dbb_trend"      # trend-following
    if n.startswith("mr"):  return "reversal"       # mean reversion
    if n.startswith("br"):  return "direct"         # breakout
    if n.startswith("mo"):  return "direct"         # momentum
    if n.startswith("cp"):  return "dbb_trend"      # coil/pullback
    if n.startswith("ss"):  return "reversal"       # support/structure
    if n.startswith("vc"):  return "direct"         # volatility/compression
    return "direct"


def derive_r_target(mean_R, mfe_mean=None):
    """Pick 1.5 or 2.0 based on mean_R. Brock's two-rung default."""
    # If the cell is solid, prefer the higher target; if marginal, the lower.
    return 2.0 if mean_R >= 0.20 else 1.5


def score_boost(mean_R, n):
    """Tiny boost for cells with strong historical edge.
    Caps at +2.0; scales with n (confidence)."""
    if n < 10: return 0.0
    base = min(2.0, max(0.0, mean_R * 4.0))
    # Confidence dampener: cell with n=10 gets 50% of boost, n>=50 gets 100%
    conf = min(1.0, n / 50.0) * 0.5 + 0.5
    return round(base * conf, 3)


print("loading dense regime53 lookup ...", flush=True)
lookup = pd.read_parquet(DENSE, columns=["pair", "ts", "technical_regime_53", "technical_regime_desc"])
lookup["ts"] = pd.to_datetime(lookup["ts"], utc=True)

print("loading textbook trades ...", flush=True)
foundational = pd.read_parquet(FOUND, columns=[
    "strategy_id", "pair", "direction", "entry_ts", "is_win", "realized_R",
])
foundational["entry_ts"] = pd.to_datetime(foundational["entry_ts"], utc=True)
foundational = foundational[(foundational.entry_ts >= CUTOFF) & (foundational.entry_ts <= HARD_LATEST)].copy()
foundational = foundational.merge(
    lookup.rename(columns={"ts": "entry_ts"}),
    on=["pair", "entry_ts"], how="left",
)
foundational["source"] = "textbook"
foundational = foundational.rename(columns={"strategy_id": "strategy"})
foundational = foundational[foundational.technical_regime_53.notna()].copy()
print(f"  textbook with regime53: {len(foundational):,}", flush=True)

print("loading trainer probes ...", flush=True)
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
trainer = trainer.rename(columns={"probe_name": "strategy", "realized_r": "realized_R"})
trainer = trainer.merge(
    lookup.rename(columns={"ts": "entry_ts"}),
    on=["pair", "entry_ts"], how="left",
)
trainer["source"] = "v3_trainer_probe"
trainer = trainer[trainer.technical_regime_53.notna()].copy()
print(f"  trainer with regime53: {len(trainer):,}", flush=True)

cols = ["source", "strategy", "pair", "direction", "entry_ts",
        "is_win", "realized_R", "technical_regime_53", "technical_regime_desc"]
unified = pd.concat([foundational[cols], trainer[cols]], ignore_index=True)
unified["hour_utc"] = unified["entry_ts"].dt.hour.astype(int)
unified["session_bucket"] = unified["hour_utc"].apply(session_bucket)
unified["family"] = unified["strategy"].apply(family_for_strategy)
print(f"unified: {len(unified):,} trades", flush=True)

# Cell aggregation
print("\naggregating cells ...", flush=True)
g = unified.groupby([
    "source", "strategy", "family", "technical_regime_53", "technical_regime_desc",
    "pair", "session_bucket", "direction",
]).agg(
    n=("realized_R", "size"),
    wins=("is_win", "sum"),
    sum_R=("realized_R", "sum"),
    mean_R=("realized_R", "mean"),
).reset_index()
g["wins"] = g["wins"].astype(int)
g["wr"] = (g["wins"] / g["n"]).round(3)
g["mean_R"] = g["mean_R"].round(3)
g["sum_R"] = g["sum_R"].round(2)
print(f"  total cells: {len(g):,}", flush=True)

# Attachment filter
attached = g[(g.n >= MIN_N) & (g.sum_R > 0) & (g.wr >= MIN_WR)].copy()
attached["r_target"] = attached["mean_R"].apply(lambda x: derive_r_target(x))
attached["score_boost"] = attached.apply(lambda r: score_boost(r["mean_R"], int(r["n"])), axis=1)
attached["last_updated"] = pd.Timestamp.utcnow().isoformat()

# Final table schema
table = attached[[
    "technical_regime_53", "technical_regime_desc", "pair", "session_bucket",
    "strategy", "family", "direction",
    "r_target", "score_boost",
    "n", "wins", "sum_R", "mean_R", "wr",
    "source", "last_updated",
]].sort_values(["technical_regime_53", "pair", "session_bucket", "mean_R"],
               ascending=[True, True, True, False])

# Save
table.to_parquet(OUT_DIR / "routing_table_v1.parquet", index=False)
table.to_csv(OUT_DIR / "routing_table_v1.csv", index=False)

# Also save FULL cell stats (including unattached) for the death-point analysis
all_cells = g.copy()
all_cells["attached"] = (
    (all_cells.n >= MIN_N) & (all_cells.sum_R > 0) & (all_cells.wr >= MIN_WR)
)
all_cells.to_parquet(OUT_DIR / "routing_cells_all.parquet", index=False)

# Summary
print(f"\n=== ROUTING TABLE v1 ===")
print(f"  attached cells (n>={MIN_N}, sum_R>0, wr>={MIN_WR}): {len(table):,}")
print(f"  unattached cells with data:                          {(~all_cells.attached).sum():,}")
print(f"  unique (regime53, pair, session) leaves with >=1 strat: "
      f"{table.groupby(['technical_regime_53','pair','session_bucket']).ngroups:,}")
print(f"  by family:")
print(table.family.value_counts().to_string())
print(f"\n  by regime53 (top 15):")
print(table.technical_regime_53.value_counts().head(15).to_string())
print(f"\n  by session_bucket:")
print(table.session_bucket.value_counts().to_string())

print(f"\n=== TOP 25 ATTACHED CELLS BY MEAN R ===")
print(table.head(25)[["technical_regime_53","pair","session_bucket","strategy","family",
                       "direction","n","wins","sum_R","mean_R","wr","r_target","score_boost"]].to_string(index=False))

# Death-point preview
print(f"\n=== DEATH-POINT PREVIEW: regimes with most volume but few attached cells ===")
deathdf = all_cells.groupby(["technical_regime_53", "pair", "session_bucket"]).agg(
    total_n=("n", "sum"),
    attached_strats=("attached", "sum"),
).reset_index()
deathdf = deathdf.sort_values("total_n", ascending=False)
deathdf_dead = deathdf[deathdf.attached_strats == 0]
print(f"  cells with traffic but NO attached strategy: {len(deathdf_dead):,}")
print(f"  total trades in those cells (historical):     {deathdf_dead.total_n.sum():,}")
print(f"  top 15:")
print(deathdf_dead.head(15).to_string(index=False))

print(f"\nsaved -> {OUT_DIR}/")
print(f"  routing_table_v1.parquet   ({len(table)} attached cells)")
print(f"  routing_table_v1.csv       (inspection mirror)")
print(f"  routing_cells_all.parquet  ({len(all_cells)} total cells, attached + unattached)")
