"""v2 analysis: 6-dimension report per Brock 2026-05-13."""
import pandas as pd
import numpy as np
from pathlib import Path

OUT = Path("/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v2")
print("loading parquet ...")
full = pd.read_parquet(OUT / "raw_m5_v2_candidate_events.parquet")
fam = pd.read_csv(OUT / "raw_m5_v2_clusters_family_grain.csv")
pair = pd.read_csv(OUT / "raw_m5_v2_clusters_pair_grain.csv")

print(f"total candidates: {len(full):,}")
print(f"family cells: {len(fam):,}   pair cells: {len(pair):,}")
print(f"GLOBAL baseline (all trades, all eras): mean R@2_net = {full['realized_at_2R_net'].mean():+.4f}")
print(f"GLOBAL discovery: {full[full.era=='discovery']['realized_at_2R_net'].mean():+.4f}")
print(f"GLOBAL holdout:   {full[full.era=='holdout']['realized_at_2R_net'].mean():+.4f}")
print()

# === 1. POSITIVE NET CELLS ===
print("="*80)
print("1. POSITIVE NET CELLS (family grain)")
print("="*80)
pos_disc = fam[(fam.n_disc >= 100) & (fam.mean_R_2r_disc > 0)].sort_values("mean_R_2r_disc", ascending=False)
pos_hold = fam[(fam.n_hold >= 30) & (fam.mean_R_2r_hold > 0)].sort_values("mean_R_2r_hold", ascending=False)
print(f"  positive disc (n>=100): {len(pos_disc)}")
print(f"  positive hold (n>=30):  {len(pos_hold)}")

# === 2. DOUBLE-SURVIVORS ===
print("\n" + "="*80)
print("2. DOUBLE-SURVIVORS (positive disc AND positive hold)")
print("="*80)
ds = fam[(fam.n_disc >= 100) & (fam.n_hold >= 30) &
         (fam.mean_R_2r_disc > 0) & (fam.mean_R_2r_hold > 0)].sort_values("mean_R_2r_disc", ascending=False)
print(f"  count: {len(ds)}")
cols = ["trigger_type","pair_family","direction","session_quarter","m15_trend","h1_regime",
        "n_disc","clean_2r_rate_disc","mean_R_2r_disc",
        "n_hold","clean_2r_rate_hold","mean_R_2r_hold"]
print("\nTop 25:")
print(ds[cols].head(25).to_string(index=False))
ds.to_csv(OUT / "report_double_survivors.csv", index=False)

# === 3. COST-KILLED ===
# Note: we only have net realized in the parquet. Approximate "pre-cost" by adding back mean spread_cost_R
# spread_cost_R was stored per row; pre-cost realized = realized_at_2R_net + 2*spread_cost_R (rough)
# Actually simpler: re-aggregate from per-row data ignoring spread effect (mfe alone).
print("\n" + "="*80)
print("3. COST-KILLED CELLS (clean_2R from MFE positive but net negative)")
print("="*80)
# clean_2r captures whether mfe reached 2R (i.e., would have hit TP if no cost penalty on slip)
# So clean_2R_rate * 2.0 + (1 - clean_2R_rate) * (-1.0) approximates pre-cost mean.
fam["pre_cost_mean_disc"] = fam["clean_2r_rate_disc"] * 2.0 + (1 - fam["clean_2r_rate_disc"]) * (-1.0)
fam["pre_cost_mean_hold"] = fam["clean_2r_rate_hold"] * 2.0 + (1 - fam["clean_2r_rate_hold"]) * (-1.0)
fam["cost_drag_disc"] = fam["pre_cost_mean_disc"] - fam["mean_R_2r_disc"]
ck = fam[(fam.n_disc >= 200) & (fam.pre_cost_mean_disc > 0.1) & (fam.mean_R_2r_disc < 0)].sort_values("cost_drag_disc", ascending=False)
print(f"  cells with pre-cost mean > 0.1 but post-cost negative: {len(ck)}")
print("\nTop 10:")
print(ck[cols + ["pre_cost_mean_disc","cost_drag_disc"]].head(10).to_string(index=False))
ck.to_csv(OUT / "report_cost_killed.csv", index=False)

# === 4. HOLDOUT-DECAY ===
print("\n" + "="*80)
print("4. HOLDOUT-DECAY (positive disc, negative hold)")
print("="*80)
hd = fam[(fam.n_disc >= 200) & (fam.n_hold >= 50) &
         (fam.mean_R_2r_disc > 0.2) & (fam.mean_R_2r_hold < 0)].sort_values("mean_R_2r_disc", ascending=False)
print(f"  count: {len(hd)}")
print("\nTop 10:")
print(hd[cols].head(10).to_string(index=False))
hd.to_csv(OUT / "report_holdout_decay.csv", index=False)

# === 5. TRIGGER FAMILY VERDICTS ===
print("\n" + "="*80)
print("5. TRIGGER FAMILY VERDICTS")
print("="*80)
tf = full.groupby("trigger_type").agg(
    n=("realized_at_2R_net","size"),
    mean_R=("realized_at_2R_net","mean"),
    clean_2r_rate=("clean_2r","mean"),
    gave_back_rate=("gave_back_green","mean"),
).reset_index().sort_values("mean_R", ascending=False)
print("\nGlobal per trigger (all cells, all eras):")
print(tf.to_string(index=False))

# Best pocket per trigger (best double-survivor cell)
print("\nBest double-survivor pocket per trigger:")
best = ds.sort_values("mean_R_2r_disc", ascending=False).groupby("trigger_type").head(1)
print(best[cols].to_string(index=False))

# Triggers that never produce double-survivors
all_triggers = full["trigger_type"].unique()
producing = ds["trigger_type"].unique()
dead = set(all_triggers) - set(producing)
print(f"\nTriggers with ZERO double-survivors: {sorted(dead)}")

# === 6. MANAGEMENT SENSITIVITY ===
print("\n" + "="*80)
print("6. MANAGEMENT SENSITIVITY on TOP 20 double-survivor cells")
print("="*80)
# For each top cell, look at trades in full and compute alt-management outcomes.
# We have mfe_r and mae_r per trade. Variants:
#   V_2R    = hit_TP_2R (mfe>=2, mae<=1)
#   V_1R    = hit_TP_1R always (mfe>=1, mae<=1)  [closer TP]
#   V_BE05  = if mfe>=0.5 first, sl moves to 0; then need mfe>=2 OR mae>=1
#   V_BE10  = if mfe>=1.0 first, sl moves to 0
#   V_PART1 = 50% off at 1R, 50% runner to 2R
#
# CRITICAL: with mfe/mae alone we cannot prove BE order-of-events; we can only
# upper/lower-bound. Use the approximation: if mae > 1.0 (stop hit) BEFORE mfe reaches threshold,
# we can't tell. So we'll compute LOWER-BOUND outcomes (most pessimistic order):
#   V_BE_thr: if mfe>=thr AND mae<=1.0: assume BE survives. mean_R = 2 if mfe>=2 else 0.
#                                       (charge -spread_cost_R for stopped-after-BE)
#   else (mae>1): stop at -1
# V_PART1: if mfe>=1 (always hits 1R before mae>=1 we approximate by mae<=1 first):
#            half at +1, runner half: 2R if mfe>=2 else -1R (or 0 if BE in runner?)
#            simple: runner_R = 2 if mfe>=2 else (-1)
#            blended = 0.5*1 + 0.5*runner_R

def variant_outcomes(sub):
    mfe = sub["mfe_r_net"].values
    mae = sub["mae_r"].values
    cost = sub["spread_cost_R"].values
    n = len(sub)
    # V_2R baseline
    v2r = np.where(mfe >= 2.0, 2.0 - cost, np.where(mae >= 1.0, -1.0 - cost, -cost))
    # V_1R (TP at 1R)
    v1r = np.where(mfe >= 1.0, 1.0 - cost, np.where(mae >= 1.0, -1.0 - cost, -cost))
    # V_BE05: mfe>=0.5 first means BE active. We approximate: hit 0.5 → mae after that may stop at 0.
    # Pessimistic: if mfe<0.5 use baseline; if mfe>=0.5 AND mfe<2: assume BE_stop → 0 - cost
    v_be05 = np.where(mfe >= 2.0, 2.0 - cost,
              np.where(mfe >= 0.5, 0.0 - cost,
                np.where(mae >= 1.0, -1.0 - cost, -cost)))
    # V_BE10: BE at 1R
    v_be10 = np.where(mfe >= 2.0, 2.0 - cost,
              np.where(mfe >= 1.0, 0.0 - cost,
                np.where(mae >= 1.0, -1.0 - cost, -cost)))
    # V_PART1: half off at 1R, runner to 2R-or-BE
    runner = np.where(mfe >= 2.0, 2.0 - cost,
              np.where(mfe >= 1.0, 0.0 - cost,
                np.where(mae >= 1.0, -1.0 - cost, -cost)))
    half_1r = np.where(mfe >= 1.0, 1.0 - cost,
              np.where(mae >= 1.0, -1.0 - cost, -cost))
    vpart = 0.5*half_1r + 0.5*runner
    return {
        "V_2R": float(np.mean(v2r)),
        "V_1R": float(np.mean(v1r)),
        "V_BE05": float(np.mean(v_be05)),
        "V_BE10": float(np.mean(v_be10)),
        "V_PART1": float(np.mean(vpart)),
        "n": n,
    }

# Build a cell key in full so we can group
full["_cell"] = full["trigger_type"]+"|"+full["pair_family"]+"|"+full["direction"]+"|"+full["session_quarter"]+"|"+full["m15_trend"].astype(str)+"|"+full["h1_regime"].astype(str)
ds["_cell"] = ds["trigger_type"]+"|"+ds["pair_family"]+"|"+ds["direction"]+"|"+ds["session_quarter"]+"|"+ds["m15_trend"].astype(str)+"|"+ds["h1_regime"].astype(str)

top_cells = ds.sort_values("mean_R_2r_disc", ascending=False).head(20)
print(f"\nTop 20 double-survivors, management variants (mean_R per trade, all-era pooled):")
rows = []
for _, c in top_cells.iterrows():
    sub_all = full[full["_cell"] == c["_cell"]]
    sub_d   = sub_all[sub_all.era == "discovery"]
    sub_h   = sub_all[sub_all.era == "holdout"]
    oa = variant_outcomes(sub_all)
    od = variant_outcomes(sub_d)
    oh = variant_outcomes(sub_h)
    rows.append({
        "trigger": c["trigger_type"], "fam": c["pair_family"], "dir": c["direction"],
        "sq": c["session_quarter"], "m15": c["m15_trend"], "h1": c["h1_regime"],
        "n_d": int(c["n_disc"]), "n_h": int(c["n_hold"]),
        "V_2R_d": od["V_2R"], "V_2R_h": oh["V_2R"],
        "V_1R_d": od["V_1R"], "V_1R_h": oh["V_1R"],
        "V_BE05_d": od["V_BE05"], "V_BE05_h": oh["V_BE05"],
        "V_BE10_d": od["V_BE10"], "V_BE10_h": oh["V_BE10"],
        "V_PART1_d": od["V_PART1"], "V_PART1_h": oh["V_PART1"],
    })
mg = pd.DataFrame(rows)
print(mg.to_string(index=False, float_format="%.3f"))
mg.to_csv(OUT / "report_management_variants_top20.csv", index=False)

# === PAIR CONCENTRATION on top 20 ===
print("\n" + "="*80)
print("PAIR CONCENTRATION on top 20 double-survivor cells")
print("="*80)
conc_rows = []
for _, c in top_cells.iterrows():
    sub = full[full["_cell"] == c["_cell"]]
    vc = sub["pair"].value_counts(normalize=True)
    top_pair = vc.index[0]
    top_share = vc.iloc[0]
    fragile = top_share > 0.7
    conc_rows.append({
        "trigger": c["trigger_type"], "fam": c["pair_family"], "dir": c["direction"],
        "sq": c["session_quarter"], "m15": c["m15_trend"], "h1": c["h1_regime"],
        "n": len(sub), "top_pair": top_pair, "top_pair_share": top_share,
        "fragile_1pair": fragile,
    })
cc = pd.DataFrame(conc_rows)
print(cc.to_string(index=False, float_format="%.3f"))
cc.to_csv(OUT / "report_pair_concentration_top20.csv", index=False)

print(f"\nALL REPORTS WRITTEN TO {OUT}")
