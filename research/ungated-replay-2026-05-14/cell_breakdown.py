"""Full 26-pair ungated replay × regime53 cell breakdown.

What we asked for at the start of this arc: "we need to simulate the V3
trading without the old regime filters, we want to see all the winners
and losers" — this is the report.

Inputs:
  /tmp/v2_ungated/*.parquet  (26 pair-files, the ungated replay output)
  dense_regime53_lookup_last6mo.parquet  (per-bar regime53)

Slices:
  - headline: total trades, WR, mean R by r_target (1.5R vs 2.0R)
  - by probe: which probes are positive vs bleeding (full corpus)
  - by regime53: where do trades land + perform
  - by (probe, regime53): the actionable cells
  - by (probe, regime53, session): the deep cells
  - by (probe, pair, regime53): pair-specific signal
  - gate-impact analysis: cells the current regime gate would have killed
"""
import pandas as pd
import numpy as np
import glob
from pathlib import Path

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
REPLAY = Path("/tmp/v2_ungated")
DENSE = ROOT / "dense_regime53_lookup_last6mo.parquet"
OUT = ROOT / "ungated-replay-analysis-2026-05-14"
OUT.mkdir(exist_ok=True)


def session_bucket(h):
    if 0 <= h < 4:   return "asia"
    if 4 <= h < 6:   return "asia_late"
    if 6 <= h < 9:   return "london_open"
    if 9 <= h < 13:  return "ny_open"
    if 13 <= h < 17: return "ny_mid"
    if 17 <= h < 21: return "ny_close"
    return "off_hours"


DEAD = {"R04", "T07", "Z01"}  # current router would veto these


print("loading 26 replay parquets ...", flush=True)
files = sorted(glob.glob(str(REPLAY / "*.parquet")))
df = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
df = df[df.filled].copy()
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
df["is_win"] = df["realized_r"] > 0
print(f"  total filled rows: {len(df):,}", flush=True)
print(f"  (note: 2 rows per trade — one per r_target 1.5/2.0)")

print("\nloading dense regime53 lookup ...", flush=True)
lookup = pd.read_parquet(DENSE, columns=["pair", "ts", "technical_regime_53", "technical_regime_desc"])
lookup["ts"] = pd.to_datetime(lookup["ts"], utc=True)
df = df.merge(lookup.rename(columns={"ts": "entry_ts"}),
              on=["pair", "entry_ts"], how="left")
matched = df.technical_regime_53.notna().sum()
print(f"  regime53 matched: {matched:,} / {len(df):,} ({matched/len(df):.1%})")
df["technical_regime_53"] = df["technical_regime_53"].fillna("unknown")
df["session_bucket"] = df["entry_ts"].dt.hour.apply(session_bucket)
df["in_dead_regime"] = df["technical_regime_53"].isin(DEAD)

# Take r_target=1.5 slice for the headline (cleaner WR than dual-target dupes)
df15 = df[df.r_multiple == 1.5].copy()
df20 = df[df.r_multiple == 2.0].copy()

print(f"\n=== HEADLINE — UNGATED 6mo / 26 pairs ===")
for label, sub in [("r_target=1.5", df15), ("r_target=2.0", df20)]:
    if len(sub) == 0: continue
    wins = sub.is_win.sum()
    print(f"  {label}: n={len(sub):,}  W={wins:,}  L={len(sub)-wins:,}  "
          f"WR={wins/len(sub):.1%}  meanR={sub.realized_r.mean():+.3f}  "
          f"sumR={sub.realized_r.sum():+.0f}")

print(f"\n=== BY PROBE (r=1.5, full corpus) ===")
g = df15.groupby("probe_name").agg(
    n=("realized_r","size"), wins=("is_win","sum"),
    mean_R=("realized_r","mean"), sum_R=("realized_r","sum"),
).reset_index()
g["wins"] = g["wins"].astype(int)
g["wr"] = (g["wins"] / g["n"]).round(3)
g["mean_R"] = g["mean_R"].round(3)
g["sum_R"] = g["sum_R"].round(0)
g = g.sort_values("mean_R", ascending=False)
print(g.to_string(index=False))

print(f"\n=== BY REGIME53 (r=1.5, n>=200) ===")
gr = df15.groupby(["technical_regime_53", "technical_regime_desc"]).agg(
    n=("realized_r","size"), wins=("is_win","sum"),
    mean_R=("realized_r","mean"), sum_R=("realized_r","sum"),
    n_probes=("probe_name","nunique"),
).reset_index()
gr["wins"] = gr["wins"].astype(int)
gr["wr"] = (gr["wins"] / gr["n"]).round(3)
gr["mean_R"] = gr["mean_R"].round(3)
gr["sum_R"] = gr["sum_R"].round(0)
gr = gr[gr.n >= 200].sort_values("mean_R", ascending=False)
print(gr.to_string(index=False))

print(f"\n=== GATE-IMPACT: trades that current RegimeStrategyRouterGate would VETO (DEAD regimes) ===")
dead = df15[df15.in_dead_regime]
alive = df15[~df15.in_dead_regime]
unk = df15[df15.technical_regime_53 == "unknown"]
print(f"  DEAD-regime trades (R04+T07+Z01): n={len(dead):,}  "
      f"WR={dead.is_win.mean():.1%}  meanR={dead.realized_r.mean():+.3f}  sumR={dead.realized_r.sum():+.0f}")
print(f"  ALIVE-regime trades:               n={len(alive):,}  "
      f"WR={alive.is_win.mean():.1%}  meanR={alive.realized_r.mean():+.3f}  sumR={alive.realized_r.sum():+.0f}")
print(f"  UNKNOWN-regime trades:             n={len(unk):,}  "
      f"WR={unk.is_win.mean():.1%}  meanR={unk.realized_r.mean():+.3f}  sumR={unk.realized_r.sum():+.0f}")

print(f"\n=== WINNING (probe x regime53) CELLS, r=1.5, n>=30, sum_R>0 ===")
cells = df15.groupby(["probe_name", "technical_regime_53", "technical_regime_desc"]).agg(
    n=("realized_r","size"), wins=("is_win","sum"),
    mean_R=("realized_r","mean"), sum_R=("realized_r","sum"),
).reset_index()
cells["wins"] = cells["wins"].astype(int)
cells["wr"] = (cells["wins"] / cells["n"]).round(3)
cells["mean_R"] = cells["mean_R"].round(3)
cells["sum_R"] = cells["sum_R"].round(2)
winners = cells[(cells.n >= 30) & (cells.sum_R > 0)].sort_values("mean_R", ascending=False)
print(f"  winning cells: {len(winners)}  (total of {len(cells)} cells with n>=30: {(cells.n>=30).sum()})")
print(winners.head(30).to_string(index=False))

print(f"\n=== BLEEDING (probe x regime53) CELLS, r=1.5, n>=30, sum_R < -10 ===")
bleeders = cells[(cells.n >= 30) & (cells.sum_R < -10)].sort_values("sum_R", ascending=True)
print(f"  bleeders: {len(bleeders)}")
print(bleeders.head(20).to_string(index=False))

print(f"\n=== WINNING CELLS IN DEAD REGIMES (router would block these) ===")
dead_winners = winners[winners.technical_regime_53.isin(DEAD)]
print(f"  count: {len(dead_winners)}  -- if > 0, gate is too aggressive")
if len(dead_winners):
    print(dead_winners.head(20).to_string(index=False))

print(f"\n=== WINNING CELLS IN ALIVE REGIMES (gate keeps these = GOOD) ===")
alive_winners = winners[~winners.technical_regime_53.isin(DEAD) & (winners.technical_regime_53 != "unknown")]
print(f"  count: {len(alive_winners)}")

# Save full outputs
df15.to_parquet(OUT / "ungated_replay_r15_with_regime53.parquet", index=False)
cells.to_csv(OUT / "ungated_cells_probe_regime53.csv", index=False)
winners.to_csv(OUT / "ungated_winning_cells.csv", index=False)
bleeders.to_csv(OUT / "ungated_bleeding_cells.csv", index=False)
gr.to_csv(OUT / "ungated_regime53_summary.csv", index=False)
g.to_csv(OUT / "ungated_probe_summary.csv", index=False)

# Deep slice: (probe, regime53, session)
deep = df15.groupby(["probe_name", "technical_regime_53", "session_bucket"]).agg(
    n=("realized_r","size"), wins=("is_win","sum"),
    mean_R=("realized_r","mean"), sum_R=("realized_r","sum"),
).reset_index()
deep["wins"] = deep["wins"].astype(int)
deep["wr"] = (deep["wins"] / deep["n"]).round(3)
deep["mean_R"] = deep["mean_R"].round(3)
deep["sum_R"] = deep["sum_R"].round(2)
deep = deep[deep.n >= 20].sort_values("mean_R", ascending=False)
deep.to_csv(OUT / "ungated_cells_probe_regime53_session.csv", index=False)
print(f"\n=== TOP 25 DEEP CELLS (probe x regime53 x session, n>=20) ===")
print(deep.head(25).to_string(index=False))

print(f"\nsaved -> {OUT}/")
for f in sorted(OUT.iterdir()):
    sz = f.stat().st_size
    print(f"  {f.name}  ({sz/1024:.1f} KB)")
