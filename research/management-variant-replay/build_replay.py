"""V3 management variant replay — test the long/short asymmetry hypothesis.

Per 2026-05-13: "longs deserve runway, shorts require fast protection."
Test by simulating management variants on the 90K intraday-safe corpus.

Method:
  For each trade, we have actual_realized_r, max_favorable_r (mfe_r),
  max_adverse_r (mae_r). Each variant rewrites realized_r per a different
  management rule. Compare aggregate R across cells × variants.

Variants:
  V0_baseline           — realized_r as-is (current walker output)
  V1_short_BE_0.5R      — shorts: if mfe>=0.5, realized = max(realized, 0). longs unchanged.
  V2_short_BE_0.6R      — same with 0.6 threshold
  V3_short_BE_0.7R      — same with 0.7 threshold
  V4_long_target_1R     — longs: cap realized at 1R (if mfe>=1, realized=1). shorts unchanged.
  V5_long_target_2R     — longs: baseline (no cap; assume already at 2R target). shorts unchanged.
  V6_direction_cond     — longs: cap at 2R baseline; shorts: BE@0.5R + cap at 1R
  V7_direction_cond_v2  — longs: hold to 2R; shorts: BE@0.5R only (no TP cap change)

CAVEAT (same as ratchet forensic): this is an UPPER BOUND on BE benefit.
The walker only records max MFE and final outcome, not the order of events.
A real BE rule could be tripped early by a retracement below BE before MFE
continues to TP. Our model treats winners as untouched by BE, which is
optimistic.

Output per (strategy × pair_family × session_bucket × direction × variant):
  total_R, winner_rate, mean_R, gave_back_rate, delta_vs_baseline
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

SRC = "/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/factor_audit/per_trade_factors_filled.csv.gz"
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/management-variant-replay")
OUT.mkdir(parents=True, exist_ok=True)

PAIR_FAMILY = {
    "EUR_USD":"usd_base","GBP_USD":"usd_base","AUD_USD":"usd_base","NZD_USD":"usd_base",
    "USD_JPY":"usd_base","USD_CHF":"usd_base","USD_CAD":"usd_base","USD_MXN":"usd_base",
    "EUR_GBP":"eur_cross","EUR_AUD":"eur_cross","EUR_NZD":"eur_cross","EUR_CAD":"eur_cross",
    "EUR_CHF":"eur_cross","EUR_JPY":"eur_cross",
    "GBP_AUD":"gbp_cross","GBP_NZD":"gbp_cross","GBP_CAD":"gbp_cross","GBP_CHF":"gbp_cross","GBP_JPY":"gbp_cross",
    "AUD_NZD":"antipodean_cross","AUD_CAD":"antipodean_cross","AUD_CHF":"antipodean_cross",
    "AUD_JPY":"antipodean_cross","NZD_JPY":"antipodean_cross","CAD_JPY":"antipodean_cross","CHF_JPY":"antipodean_cross",
}
def session_of(h):
    if pd.isna(h): return "unknown"
    h = int(h) % 24
    if 22 <= h or h < 6: return "asia"
    elif 6 <= h < 12: return "london"
    elif 12 <= h < 16: return "overlap"
    else: return "ny_pm"

df = pd.read_csv(SRC, usecols=["symbol","direction","strategy","hour_utc",
                                "realized_r","max_favorable_r","max_adverse_r"])
df["pair_family"] = df["symbol"].map(PAIR_FAMILY).fillna("other")
df["session_bucket"] = df["hour_utc"].apply(session_of)
df["mfe_r"] = pd.to_numeric(df["max_favorable_r"], errors="coerce")
df["mae_r"] = pd.to_numeric(df["max_adverse_r"], errors="coerce")
df["realized_r"] = pd.to_numeric(df["realized_r"], errors="coerce")
df = df.dropna(subset=["mfe_r","mae_r","realized_r","direction"])
print(f"trades loaded: {len(df):,}")
print(f"  direction split: {df['direction'].value_counts().to_dict()}")
print()


def apply_BE_short(r, mfe, direction, threshold):
    """BE rule for shorts: if mfe>=threshold and direction==short, floor realized at 0."""
    out = r.copy()
    trip = (direction == "short") & (mfe >= threshold) & (out < 0)
    out.loc[trip] = 0.0
    return out


def apply_BE_long(r, mfe, direction, threshold):
    """BE rule for longs: if mfe>=threshold and direction==long, floor realized at 0."""
    out = r.copy()
    trip = (direction == "long") & (mfe >= threshold) & (out < 0)
    out.loc[trip] = 0.0
    return out


def apply_target_cap(r, mfe, direction, target_dir, target_R):
    """Cap realized at target_R for the specified direction if mfe>=target_R."""
    out = r.copy()
    cap_trip = (direction == target_dir) & (mfe >= target_R) & (out > target_R)
    out.loc[cap_trip] = target_R
    # Also: when mfe>=target_R, the trade hits TP, so realized = target_R (even if walker had it lower)
    promote = (direction == target_dir) & (mfe >= target_R) & (out < target_R) & (out > 0)
    out.loc[promote] = target_R
    return out


# Build each variant
print("computing variants ...")
variants = {}

# V0: baseline
variants["V0_baseline"] = df["realized_r"].copy()

# V1-V3: shorts BE at thresholds
for thresh in [0.5, 0.6, 0.7]:
    v_r = apply_BE_short(df["realized_r"], df["mfe_r"], df["direction"], thresh)
    variants[f"V_short_BE_{thresh:.1f}R"] = v_r

# V4: longs cap at 1R
v4 = apply_target_cap(df["realized_r"], df["mfe_r"], df["direction"], "long", 1.0)
variants["V_long_target_1R"] = v4

# V5: longs hold to 2R (already baseline; shorts unchanged)
v5 = apply_target_cap(df["realized_r"], df["mfe_r"], df["direction"], "long", 2.0)
variants["V_long_target_2R"] = v5

# V6: direction-conditional — longs to 2R, shorts BE@0.5 + cap at 1R
v6 = apply_BE_short(df["realized_r"], df["mfe_r"], df["direction"], 0.5)
v6 = apply_target_cap(v6, df["mfe_r"], df["direction"], "short", 1.0)
v6 = apply_target_cap(v6, df["mfe_r"], df["direction"], "long", 2.0)
variants["V_direction_cond_short_BE05_cap1R_long_2R"] = v6

# V7: direction-conditional simpler — longs hold, shorts BE@0.5 only (no cap)
v7 = apply_BE_short(df["realized_r"], df["mfe_r"], df["direction"], 0.5)
variants["V_direction_cond_short_BE05_long_unchanged"] = v7


# === Aggregate per cell ===
print("\naggregating per cell × variant ...")
GRAIN = ["strategy", "pair_family", "direction", "session_bucket"]

rows = []
for variant_name, var_r in variants.items():
    df_v = df.copy()
    df_v["v_realized_r"] = var_r
    for keys, g in df_v.groupby(GRAIN):
        s, pf, dr, sb = keys
        r = g["v_realized_r"]
        rows.append({
            "variant": variant_name,
            "strategy": s, "pair_family": pf, "direction": dr, "session_bucket": sb,
            "n": len(g),
            "total_R": float(r.sum()),
            "mean_R": float(r.mean()),
            "winner_rate": float((r > 0).mean()),
            "gave_back_rate": float(((g["mfe_r"] > 0.3) & (r < -0.1)).mean()),
        })
cell_df = pd.DataFrame(rows)

# Pivot: deltas vs baseline
base = cell_df[cell_df["variant"] == "V0_baseline"].set_index(GRAIN)[["total_R","mean_R","winner_rate","gave_back_rate"]]
base.columns = [c + "_base" for c in base.columns]
merged = cell_df.merge(base, left_on=GRAIN, right_index=True, how="left")
merged["delta_total_R"] = merged["total_R"] - merged["total_R_base"]
merged["delta_mean_R"] = merged["mean_R"] - merged["mean_R_base"]
merged["delta_winner_rate"] = merged["winner_rate"] - merged["winner_rate_base"]
merged["delta_gave_back"] = merged["gave_back_rate"] - merged["gave_back_rate_base"]
merged.to_csv(OUT / "per_cell_variants.csv", index=False)


# === Global summary per variant ===
print("\n=== GLOBAL SUMMARY (sum across all cells) ===")
g_rows = []
for variant_name, var_r in variants.items():
    g_rows.append({
        "variant": variant_name,
        "n": len(var_r),
        "total_R": float(var_r.sum()),
        "mean_R": float(var_r.mean()),
        "winner_rate": float((var_r > 0).mean()),
        "gave_back_rate": float(((df["mfe_r"] > 0.3) & (var_r < -0.1)).mean()),
    })
g_df = pd.DataFrame(g_rows)
base_total = g_df.loc[g_df["variant"] == "V0_baseline", "total_R"].iloc[0]
g_df["delta_total_R"] = g_df["total_R"] - base_total
g_df["delta_per_trade"] = g_df["delta_total_R"] / len(df)
print(g_df.to_string(index=False))
g_df.to_csv(OUT / "global_summary.csv", index=False)


# === Per direction summary ===
print("\n=== PER DIRECTION ===")
for dr in ["long", "short"]:
    print(f"\n  {dr.upper()} subset:")
    dr_rows = []
    for variant_name, var_r in variants.items():
        mask = df["direction"] == dr
        sub = var_r[mask]
        dr_rows.append({
            "variant": variant_name,
            "n": int(mask.sum()),
            "total_R": float(sub.sum()),
            "mean_R": float(sub.mean()),
            "winner_rate": float((sub > 0).mean()),
            "gave_back_rate": float(((df.loc[mask, "mfe_r"] > 0.3) & (sub < -0.1)).mean()),
        })
    dr_df = pd.DataFrame(dr_rows)
    base = dr_df.loc[dr_df["variant"] == "V0_baseline", "total_R"].iloc[0]
    dr_df["delta_total_R"] = dr_df["total_R"] - base
    dr_df["delta_per_trade"] = dr_df["delta_total_R"] / dr_df["n"]
    print(dr_df.to_string(index=False))
    dr_df.to_csv(OUT / f"direction_{dr}_summary.csv", index=False)


# === Per (strategy, direction) summary — V0 vs V6 vs V7 ===
print("\n=== PER STRATEGY × DIRECTION (only the key variants) ===")
key_variants = ["V0_baseline", "V_short_BE_0.5R", "V_direction_cond_short_BE05_long_unchanged"]
for var in key_variants:
    print(f"\n  {var}:")
    df_v = df.copy()
    df_v["v_realized_r"] = variants[var]
    rep = df_v.groupby(["strategy","direction"]).agg(
        n=("v_realized_r", "size"),
        total_R=("v_realized_r", "sum"),
        mean_R=("v_realized_r", "mean"),
        winner_rate=("v_realized_r", lambda x: (x > 0).mean()),
    ).reset_index()
    print(rep.to_string(index=False))


# === Headline cells: what changes most ===
print("\n=== TOP 15 CELLS BY ABSOLUTE DELTA_TOTAL_R (V_direction_cond_short_BE05_long_unchanged) ===")
sig = merged[merged["variant"] == "V_direction_cond_short_BE05_long_unchanged"].sort_values("delta_total_R", ascending=False).head(15)
print(sig[["strategy","pair_family","direction","session_bucket","n","total_R_base","total_R","delta_total_R","delta_per_trade" if "delta_per_trade" in sig.columns else "delta_mean_R"]].to_string(index=False))

print(f"\nsaved {OUT}")
