"""Routing Table v2 — built from ungated 26-pair replay evidence.

v1 was mined from 1.26M trades but with the regime gate's bias baked in
(the trainer probes used regime_label internally before the ungated rerun).

v2 sources:
  - V3 probes: ungated 26-pair / 6mo replay (90,015 trades at r=1.5,
    same again at r=2.0). This is the cleanest probe evidence available.
  - Textbook strategies: same foundational+dense data as v1 (no ungated
    rerun available for textbook).

Per-cell granularity: (regime53, pair, session_bucket, strategy, direction).

Attachment rule (same as v1):
  n >= 10 AND sum_R > 0 AND wr >= 0.30

Also exports an explicit DENY list (the 26 ungated bleeders at (probe x
regime) sum_R <= -10) for audit visibility. Bleeders are already filtered
out by the attachment rule; the deny list is documentation only.

Output:
  routing_table_v2.parquet         (the attachment table)
  routing_table_v2.csv             (inspection)
  routing_table_v2_deny_list.csv   (documented bleeders)
  routing_table_v2_summary.md      (counts + headline cells)
"""
from pathlib import Path
import pandas as pd
import numpy as np
import glob

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
FOUND = ROOT / "all_strategies_all_pairs_trades.parquet"
DENSE = ROOT / "dense_regime53_lookup_last6mo.parquet"
REPLAY = Path("/tmp/v2_ungated")
OUT = ROOT / "routing-table-v2"
OUT.mkdir(exist_ok=True)

CUTOFF = pd.Timestamp("2025-10-22", tz="UTC")
HARD_LATEST = pd.Timestamp("2026-04-22", tz="UTC")

MIN_N = 10
MIN_WR = 0.30
MIN_SUM_R = 0.0  # strictly positive


def session_bucket(h):
    if 0 <= h < 4:   return "asia"
    if 4 <= h < 6:   return "asia_late"
    if 6 <= h < 9:   return "london_open"
    if 9 <= h < 13:  return "ny_open"
    if 13 <= h < 17: return "ny_mid"
    if 17 <= h < 21: return "ny_close"
    return "off_hours"


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


def family_for_strategy(name):
    if name in PROBE_FAMILY: return PROBE_FAMILY[name]
    n = name.lower()
    if n.startswith("tf"):  return "dbb_trend"
    if n.startswith("mr"):  return "reversal"
    if n.startswith("br"):  return "direct"
    if n.startswith("mo"):  return "direct"
    if n.startswith("cp"):  return "dbb_trend"
    if n.startswith("ss"):  return "reversal"
    if n.startswith("vc"):  return "direct"
    return "direct"


def derive_r_target(mean_R):
    return 2.0 if mean_R >= 0.20 else 1.5


def score_boost(mean_R, n):
    if n < 10: return 0.0
    base = min(2.0, max(0.0, mean_R * 4.0))
    conf = min(1.0, n / 50.0) * 0.5 + 0.5
    return round(base * conf, 3)


# --------------------------------------------------------------------------
# V3 PROBES — ungated replay
# --------------------------------------------------------------------------

print("loading dense regime53 lookup ...", flush=True)
lookup = pd.read_parquet(DENSE, columns=["pair", "ts", "technical_regime_53", "technical_regime_desc"])
lookup["ts"] = pd.to_datetime(lookup["ts"], utc=True)

print("loading ungated replay (26 pairs) ...", flush=True)
files = sorted(glob.glob(str(REPLAY / "*.parquet")))
replay = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
replay = replay[replay.filled].copy()
replay["entry_ts"] = pd.to_datetime(replay["entry_ts"], utc=True)
replay["is_win"] = replay["realized_r"] > 0
replay = replay.rename(columns={"probe_name": "strategy", "realized_r": "realized_R"})

# Merge regime53
replay = replay.merge(lookup.rename(columns={"ts": "entry_ts"}),
                      on=["pair", "entry_ts"], how="left")
replay = replay[replay.technical_regime_53.notna()].copy()
replay["session_bucket"] = replay["entry_ts"].dt.hour.apply(session_bucket)
replay["family"] = replay["strategy"].apply(family_for_strategy)
replay["source"] = "v3_trainer_probe_ungated"

# Keep both r_target slices but split — table rows carry per-target params,
# so each (probe, regime, pair, session, direction, r_target) is a row.
print(f"  replay rows (both r-targets): {len(replay):,}", flush=True)
print(f"  unique probes: {replay.strategy.nunique()}", flush=True)


def aggregate(df, src_label):
    g = df.groupby([
        "strategy", "family", "technical_regime_53", "technical_regime_desc",
        "pair", "session_bucket", "direction", "r_multiple",
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
    g["source"] = src_label
    return g


probe_cells = aggregate(replay, "v3_trainer_probe_ungated")
# For probe attachment, pick the BEST r_target per (probe, regime, pair, session, direction)
probe_cells_best = probe_cells.sort_values(
    ["strategy", "technical_regime_53", "pair", "session_bucket", "direction", "mean_R"],
    ascending=[True, True, True, True, True, False],
).drop_duplicates(subset=["strategy", "technical_regime_53", "pair", "session_bucket", "direction"], keep="first")
print(f"  probe (best-r-target) cells:  {len(probe_cells_best):,}", flush=True)

# --------------------------------------------------------------------------
# TEXTBOOK — foundational data (no ungated rerun available)
# --------------------------------------------------------------------------

print("\nloading textbook trades + regime53 ...", flush=True)
foundational = pd.read_parquet(FOUND, columns=[
    "strategy_id", "pair", "direction", "entry_ts", "is_win", "realized_R",
])
foundational["entry_ts"] = pd.to_datetime(foundational["entry_ts"], utc=True)
foundational = foundational[(foundational.entry_ts >= CUTOFF) & (foundational.entry_ts <= HARD_LATEST)].copy()
foundational = foundational.merge(lookup.rename(columns={"ts": "entry_ts"}),
                                   on=["pair", "entry_ts"], how="left")
foundational = foundational[foundational.technical_regime_53.notna()].copy()
foundational = foundational.rename(columns={"strategy_id": "strategy"})
foundational["session_bucket"] = foundational["entry_ts"].dt.hour.apply(session_bucket)
foundational["family"] = foundational["strategy"].apply(family_for_strategy)
foundational["source"] = "textbook"
foundational["r_multiple"] = 2.0  # textbook trades are 2:1 by convention
print(f"  textbook trades with regime53: {len(foundational):,}", flush=True)

textbook_cells = aggregate(foundational, "textbook")
print(f"  textbook cells:  {len(textbook_cells):,}", flush=True)

# --------------------------------------------------------------------------
# Combine and apply attachment rule
# --------------------------------------------------------------------------

all_cells = pd.concat([probe_cells_best, textbook_cells], ignore_index=True)
print(f"\ntotal cells: {len(all_cells):,}", flush=True)

attached = all_cells[
    (all_cells.n >= MIN_N) & (all_cells.sum_R > MIN_SUM_R) & (all_cells.wr >= MIN_WR)
].copy()
attached["r_target"] = attached.apply(
    lambda r: derive_r_target(r["mean_R"]) if r["r_multiple"] != r["r_multiple"] else r["r_multiple"],
    axis=1,
).astype(float)
attached["score_boost"] = attached.apply(lambda r: score_boost(r["mean_R"], int(r["n"])), axis=1)
attached["last_updated"] = pd.Timestamp.utcnow().isoformat()

table = attached[[
    "technical_regime_53", "technical_regime_desc", "pair", "session_bucket",
    "strategy", "family", "direction",
    "r_target", "score_boost",
    "n", "wins", "sum_R", "mean_R", "wr",
    "source", "last_updated",
]].sort_values(
    ["technical_regime_53", "pair", "session_bucket", "mean_R"],
    ascending=[True, True, True, False],
)

# --------------------------------------------------------------------------
# Deny list (documentation only — bleeders are auto-excluded by attachment rule)
# --------------------------------------------------------------------------

# Coarse (probe x regime) cells with sum_R <= -10 across the full corpus
deny_probe_regime = replay[replay.r_multiple == 1.5].groupby(
    ["strategy", "technical_regime_53", "technical_regime_desc"]
).agg(
    n=("realized_R","size"), wins=("is_win","sum"),
    sum_R=("realized_R","sum"), mean_R=("realized_R","mean"),
).reset_index()
deny_probe_regime["wr"] = (deny_probe_regime["wins"].astype(int) / deny_probe_regime["n"]).round(3)
deny_probe_regime["mean_R"] = deny_probe_regime["mean_R"].round(3)
deny_probe_regime["sum_R"] = deny_probe_regime["sum_R"].round(2)
deny = deny_probe_regime[(deny_probe_regime.n >= 30) & (deny_probe_regime.sum_R <= -10)].copy()
deny = deny.sort_values("sum_R")
deny["deny_reason"] = "ungated_replay_bleeder_sum_R_le_minus_10"

# Save outputs
table.to_parquet(OUT / "routing_table_v2.parquet", index=False)
table.to_csv(OUT / "routing_table_v2.csv", index=False)
deny.to_csv(OUT / "routing_table_v2_deny_list.csv", index=False)
all_cells.to_parquet(OUT / "routing_cells_all_v2.parquet", index=False)

# --------------------------------------------------------------------------
# Summary
# --------------------------------------------------------------------------

print(f"\n=== ROUTING TABLE v2 ===")
print(f"  attached cells: {len(table):,}")
print(f"  unique (regime, pair, session) leaves: "
      f"{table.groupby(['technical_regime_53','pair','session_bucket']).ngroups:,}")
print(f"  by source:")
print(table.source.value_counts().to_string())
print(f"\n  by family:")
print(table.family.value_counts().to_string())
print(f"\n  by regime53 (top 15):")
print(table.technical_regime_53.value_counts().head(15).to_string())
print(f"\n  by session_bucket:")
print(table.session_bucket.value_counts().to_string())

print(f"\n=== DENY LIST (documented bleeders, auto-excluded by attachment rule) ===")
print(f"  count: {len(deny)}")
if len(deny):
    print(deny.head(10).to_string(index=False))

print(f"\n=== TOP 20 ATTACHED CELLS BY MEAN R ===")
print(table.head(20)[
    ["technical_regime_53","pair","session_bucket","strategy","family",
     "direction","n","wins","sum_R","mean_R","wr","r_target","score_boost"]
].to_string(index=False))

# Compare to v1
v1 = pd.read_parquet(ROOT / "routing-table-v1" / "routing_table_v1.parquet")
print(f"\n=== v2 vs v1 ===")
print(f"  v1 attached cells: {len(v1):,}")
print(f"  v2 attached cells: {len(table):,}")
print(f"  delta: {len(table) - len(v1):+,}")

# Save summary md
md = OUT / "routing_table_v2_summary.md"
with md.open("w") as fh:
    fh.write(f"""# Routing Table v2 — built from ungated evidence

Built 2026-05-14.

## Counts
- Attached cells: **{len(table):,}**
- Unique (regime, pair, session) leaves: **{table.groupby(['technical_regime_53','pair','session_bucket']).ngroups}**
- v1 → v2 delta: **{len(table) - len(v1):+,} cells**

## Sources
{table.source.value_counts().to_string()}

## Families
{table.family.value_counts().to_string()}

## Deny list
{len(deny)} (probe × regime) cells documented as bleeders (sum_R ≤ −10 over 6mo).
Already auto-excluded by attachment rule; deny list is documentation only.

## Attachment rule
- n >= {MIN_N}
- sum_R > {MIN_SUM_R}
- WR >= {MIN_WR}

## Schema
regime53, regime_desc, pair, session_bucket, strategy, family, direction,
r_target, score_boost, n, wins, sum_R, mean_R, wr, source, last_updated
""")
print(f"\nsaved -> {OUT}/")
for f in sorted(OUT.iterdir()):
    print(f"  {f.name}  ({f.stat().st_size/1024:.1f} KB)")
