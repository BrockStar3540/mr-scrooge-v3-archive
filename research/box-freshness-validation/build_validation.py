"""Box Freshness Validation Pass.

Per 2026-05-13: test box_age_hours as a hypothesis across thresholds,
pockets, and sessions. Determine if signal is independent or just a
pocket-tag for Asia / USD-antipodean.

Inputs: broker rows with factor_box_age_hours non-null. Manual rows
excluded (no box_age data). Contaminated rows excluded.

For each threshold T in {24, 48, 72, 120, 168, inf}h:
  bucket trades as <=T or >T
  metrics: n, winner_rate, mean_r, median_mfe, median_mae,
           gave_back_rate, clean_stop_rate, skip_rate

Per pocket grain:
  Coarse: pair_family × direction
  Mid:    + session_bucket

Tests:
  1. Does fresh box have higher winner_rate within EACH pocket?
  2. If yes uniformly → independent signal
  3. If only in some pockets → pocket-tag
  4. Session-controlled view: within each session, does box_age still separate?
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/box-freshness-validation")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_parquet(LEDGER)

# Broker pool, not contaminated, with box_age
mask = (
    df["source_label"].isin(["bot_actual_winner", "bot_actual_loser"]) &
    (df["repair_taxonomy"] != "correct_box_replay_required") &
    df["factor_box_age_hours"].notna()
)
pool = df[mask].copy()
pool["box_age"] = pd.to_numeric(pool["factor_box_age_hours"], errors="coerce")
pool["realized_r"] = pd.to_numeric(pool["actual_realized_r"], errors="coerce")
pool["mfe_r"] = pd.to_numeric(pool["actual_mfe_r"], errors="coerce")
pool["mae_r"] = pd.to_numeric(pool["actual_mae_r"], errors="coerce")
pool["is_winner"] = pool["realized_r"] > 0
print(f"pool: {len(pool)} broker rows with box_age")
print(f"  winners: {pool['is_winner'].sum()}")
print(f"  losers: {(~pool['is_winner']).sum()}")
print(f"  box_age stats: min={pool['box_age'].min():.1f} median={pool['box_age'].median():.1f} max={pool['box_age'].max():.1f}")

# Define gave_back / clean_stop within losers
pool["gave_back"] = (pool["mfe_r"] > 0.3) & (pool["realized_r"] < -0.1)
pool["clean_stop"] = (pool["realized_r"] <= -0.95) & (pool["mfe_r"] < 0.15)

THRESHOLDS = [24, 48, 72, 120, 168]


def bucket_metrics(sub):
    n = len(sub)
    if n == 0: return {"n": 0}
    return {
        "n": n,
        "winner_rate": sub["is_winner"].mean(),
        "mean_r": sub["realized_r"].mean(),
        "median_r": sub["realized_r"].median(),
        "median_mfe": sub["mfe_r"].median(),
        "median_mae": sub["mae_r"].median(),
        "gave_back_rate": sub["gave_back"].mean(),
        "clean_stop_rate": sub["clean_stop"].mean(),
    }


print("\n=== GLOBAL THRESHOLD SWEEP ===")
rows = []
for T in THRESHOLDS + [None]:
    if T is None:
        # >168h
        sub = pool[pool["box_age"] > 168]
        label = ">168h"
    else:
        sub = pool[pool["box_age"] <= T]
        label = f"<={T}h"
    m = bucket_metrics(sub)
    m["bucket"] = label
    rows.append(m)
# Also: stratified — non-cumulative buckets (0-24, 24-48, etc.)
print("Cumulative thresholds:")
for r in rows:
    print(f"  {r['bucket']:>8}: n={r['n']:>3}  winner_rate={r['winner_rate']*100:.1f}%  mean_r={r['mean_r']:+.3f}  median_mfe={r['median_mfe']:.2f}  gave_back_rate={r['gave_back_rate']*100:.1f}%")
pd.DataFrame(rows).to_csv(OUT / "global_thresholds.csv", index=False)


# Stratified (non-cumulative) buckets
print("\nStratified buckets:")
bins = [0, 24, 48, 72, 120, 168, float('inf')]
labels = ["0-24h", "24-48h", "48-72h", "72-120h", "120-168h", ">168h"]
pool["age_bucket"] = pd.cut(pool["box_age"], bins=bins, labels=labels, right=True)
strat_rows = []
for lbl in labels:
    sub = pool[pool["age_bucket"] == lbl]
    m = bucket_metrics(sub)
    m["bucket"] = lbl
    strat_rows.append(m)
    print(f"  {lbl:>10}: n={m['n']:>3}  winner_rate={m.get('winner_rate',0)*100:.1f}%  mean_r={m.get('mean_r',0):+.3f}  median_mfe={m.get('median_mfe',0):.2f}  gave_back_rate={m.get('gave_back_rate',0)*100:.1f}%")
pd.DataFrame(strat_rows).to_csv(OUT / "global_stratified.csv", index=False)


# === Per pocket: pair_family × direction × age_bucket ===
print("\n=== PER POCKET STRATIFIED (pair_family × direction × age_bucket) ===")
pocket_rows = []
for (pf, dr), grp in pool.groupby(["pair_family", "direction"]):
    for lbl in labels:
        sub = grp[grp["age_bucket"] == lbl]
        if len(sub) == 0: continue
        m = bucket_metrics(sub)
        m.update({"pair_family": pf, "direction": dr, "age_bucket": lbl})
        pocket_rows.append(m)
pocket_df = pd.DataFrame(pocket_rows)
pocket_df.to_csv(OUT / "per_pocket_stratified.csv", index=False)

# Compute per-pocket signal strength (winner_rate of fresh vs stale)
print(f"\n=== POCKET INDEPENDENCE TEST ===")
print(f"For each (pair_family, direction): is winner_rate higher for FRESH (<=72h) vs STALE (>72h)?\n")
indep_rows = []
for (pf, dr), grp in pool.groupby(["pair_family", "direction"]):
    fresh = grp[grp["box_age"] <= 72]
    stale = grp[grp["box_age"] > 72]
    if len(fresh) < 3 or len(stale) < 3:
        indep_rows.append({
            "pair_family": pf, "direction": dr,
            "n_fresh": len(fresh), "n_stale": len(stale),
            "fresh_winner_rate": fresh["is_winner"].mean() if len(fresh) else None,
            "stale_winner_rate": stale["is_winner"].mean() if len(stale) else None,
            "fresh_mean_r": fresh["realized_r"].mean() if len(fresh) else None,
            "stale_mean_r": stale["realized_r"].mean() if len(stale) else None,
            "wr_diff": None,
            "signal_holds": "n_too_small",
        })
        continue
    fwr = fresh["is_winner"].mean()
    swr = stale["is_winner"].mean()
    fmr = fresh["realized_r"].mean()
    smr = stale["realized_r"].mean()
    diff = fwr - swr
    signal_holds = "yes" if diff > 0.05 else ("flat" if abs(diff) <= 0.05 else "REVERSED")
    indep_rows.append({
        "pair_family": pf, "direction": dr,
        "n_fresh": len(fresh), "n_stale": len(stale),
        "fresh_winner_rate": fwr, "stale_winner_rate": swr,
        "fresh_mean_r": fmr, "stale_mean_r": smr,
        "wr_diff": diff,
        "signal_holds": signal_holds,
    })
indep_df = pd.DataFrame(indep_rows).sort_values("wr_diff", ascending=False, na_position="last")
indep_df.to_csv(OUT / "pocket_independence.csv", index=False)
print(indep_df.to_string(index=False))


# === Session control: per session_bucket, fresh vs stale ===
print(f"\n=== SESSION CONTROLLED VIEW (session_bucket × fresh/stale, ignore pair_family) ===")
sess_rows = []
for sb, grp in pool.groupby("session_bucket"):
    fresh = grp[grp["box_age"] <= 72]
    stale = grp[grp["box_age"] > 72]
    sess_rows.append({
        "session_bucket": sb,
        "n_fresh": len(fresh), "n_stale": len(stale),
        "fresh_winner_rate": fresh["is_winner"].mean() if len(fresh) else None,
        "stale_winner_rate": stale["is_winner"].mean() if len(stale) else None,
        "fresh_mean_r": fresh["realized_r"].mean() if len(fresh) else None,
        "stale_mean_r": stale["realized_r"].mean() if len(stale) else None,
        "wr_diff": (fresh["is_winner"].mean() - stale["is_winner"].mean()) if (len(fresh) and len(stale)) else None,
    })
sess_df = pd.DataFrame(sess_rows)
sess_df.to_csv(OUT / "session_control.csv", index=False)
print(sess_df.to_string(index=False))


# === Distribution of fresh trades by session (is box_age proxying for session?) ===
print(f"\n=== IS FRESH BOX A SESSION-PROXY? ===")
cross = pool.groupby(["session_bucket", pd.cut(pool["box_age"], [0, 72, float('inf')], labels=["fresh<=72", "stale>72"])])\
    .size().unstack(fill_value=0)
print("count of trades by session × fresh/stale:")
print(cross.to_string())
print()
fresh_by_sess = pool[pool["box_age"] <= 72].groupby("session_bucket").size()
total_by_sess = pool.groupby("session_bucket").size()
fresh_pct = (fresh_by_sess / total_by_sess * 100).round(1)
print("% of trades that are FRESH (<=72h) per session:")
print(fresh_pct.to_string())


# Also: is the fresh-box winning concentrated in usd_base + antipodean (the strong pockets)?
print(f"\n=== IS THE SIGNAL CONCENTRATED IN STRONG POCKETS? ===")
strong_pockets = [("usd_base", "long"), ("usd_base", "short"), ("antipodean_cross", "long"), ("antipodean_cross", "short")]
strong = pool[pool.apply(lambda r: (r["pair_family"], r["direction"]) in strong_pockets, axis=1)]
weak = pool[~pool.apply(lambda r: (r["pair_family"], r["direction"]) in strong_pockets, axis=1)]
print(f"Strong pockets (usd_base/antipodean × any dir):")
for label, sub in [("strong", strong), ("weak", weak)]:
    fresh = sub[sub["box_age"] <= 72]
    stale = sub[sub["box_age"] > 72]
    print(f"  {label}: fresh n={len(fresh)} wr={fresh['is_winner'].mean()*100:.1f}%, stale n={len(stale)} wr={stale['is_winner'].mean()*100:.1f}%")


print("\nsaved outputs to", OUT)
