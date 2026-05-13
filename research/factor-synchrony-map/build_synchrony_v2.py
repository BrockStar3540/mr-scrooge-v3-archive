"""Factor Synchrony Map v2 — broker-only with broader loser pool.

Key change from v1: manual winners (46 rows) have only 3 factors. Drop them from
the 79-factor synchrony. Use broker winners (68) + broker non-contaminated losers
(all 45). Compute at multiple grain levels since some pockets are sparse.

Grains:
  Coarse  pair_family × direction              (~10 pockets, ~7-10 winners each)
  Mid     + session_bucket                       (~30 pockets, 1-10 winners each)

Per pocket × factor:
  winner_median / loser_median + Cohen's d + CI + sign
  Sample-size warning loud
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/factor-synchrony-map")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_parquet(LEDGER)

# Winners: broker_actual_winner + step7-promoted broker rows (the 4 step7 cases are broker)
mask_winner = (df["source_label"] == "bot_actual_winner") | (
    df["step7_final_verdict"].isin(["direction_repair_confirmed", "direction_repair_partial"])
)
winners = df[mask_winner].copy()
print(f"broker verified winners: {len(winners)}")

# Losers: non-contaminated broker losers
mask_loser = (df["source_label"] == "bot_actual_loser") & (df["repair_taxonomy"] != "correct_box_replay_required")
losers = df[mask_loser].copy()
print(f"broker non-contaminated losers: {len(losers)}")

# Factor cols
factor_cols = [c for c in df.columns if c.startswith("factor_")]
priority = [
    "factor_bb_position", "factor_wall_proximity", "factor_bb_band_width_a_bps",
    "factor_ema20_dist_pct", "factor_ema50_dist_pct", "factor_px_vs_ema20_bps", "factor_px_vs_ema50_bps",
    "factor_atr", "factor_otr_ratio", "factor_adr_consumed",
    "factor_rsi", "factor_z_score",
    "factor_spread_pips", "factor_rr_ratio", "factor_natural_stop_pips",
    "factor_volume_ratio", "factor_current_volume", "factor_avg_volume",
    "factor_regime_score", "factor_regime_confidence", "factor_box_age_hours",
    "factor_range_half", "factor_total_overhead", "factor_sma20_dist_signed_bps",
    "factor_bb_band_width_b_bps", "factor_bb_percent_b_a",
]
priority = [c for c in priority if c in factor_cols]
print(f"priority factors: {len(priority)}")


def cohen_d_and_ci(w, l):
    w = pd.to_numeric(w, errors="coerce").dropna()
    l = pd.to_numeric(l, errors="coerce").dropna()
    nw, nl = len(w), len(l)
    if nw < 2 or nl < 2:
        return None, None, None, nw, nl
    mw, ml_, sw, sl = w.mean(), l.mean(), w.std(), l.std()
    pool = np.sqrt(((nw - 1)*sw**2 + (nl - 1)*sl**2) / max(nw + nl - 2, 1))
    if pool <= 0:
        return None, None, None, nw, nl
    d = (mw - ml_) / pool
    se = np.sqrt(sw**2/nw + sl**2/nl)
    return d, (mw - ml_) - 1.96*se, (mw - ml_) + 1.96*se, nw, nl


def synchrony_at_grain(grain_cols, name, min_n=3):
    rows = []
    pockets = set(map(tuple, winners[grain_cols].dropna().drop_duplicates().to_numpy())) | \
              set(map(tuple, losers[grain_cols].dropna().drop_duplicates().to_numpy()))
    for pocket in pockets:
        w_mask = pd.Series(True, index=winners.index)
        l_mask = pd.Series(True, index=losers.index)
        for col, val in zip(grain_cols, pocket):
            w_mask &= (winners[col] == val)
            l_mask &= (losers[col] == val)
        wg, lg = winners[w_mask], losers[l_mask]
        if len(wg) < 1 and len(lg) < 1: continue
        for f in priority:
            d, lo, hi, nw, nl = cohen_d_and_ci(wg[f], lg[f])
            wm = pd.to_numeric(wg[f], errors="coerce").dropna()
            lm_ = pd.to_numeric(lg[f], errors="coerce").dropna()
            if nw < min_n or nl < min_n:
                sign = "unstable"
            elif d is None:
                sign = "ambiguous"
            elif lo is not None and lo > 0:
                sign = "shared_winner_condition"
            elif hi is not None and hi < 0:
                sign = "loser_contrast"
            else:
                sign = "neutral"
            row = {
                "grain": name,
                "factor": f.replace("factor_", ""),
                "n_winners": nw, "n_losers": nl,
                "winner_median": float(wm.median()) if nw else None,
                "loser_median": float(lm_.median()) if nl else None,
                "winner_mean": float(wm.mean()) if nw else None,
                "loser_mean": float(lm_.mean()) if nl else None,
                "cohens_d": float(d) if d is not None else None,
                "ci_low": float(lo) if lo is not None else None,
                "ci_high": float(hi) if hi is not None else None,
                "sign": sign,
            }
            for col, val in zip(grain_cols, pocket):
                row[col] = val
            rows.append(row)
    return pd.DataFrame(rows)


# Coarse and mid grains
print("\nbuilding coarse grain (pair_family x direction) ...")
coarse = synchrony_at_grain(["pair_family", "direction"], "coarse", min_n=3)
print(f"  rows: {len(coarse)}  pockets: {coarse.groupby(['pair_family','direction']).ngroups}")
print(f"  sign distribution: {coarse['sign'].value_counts().to_dict()}")

print("\nbuilding mid grain (pair_family x session_bucket x direction) ...")
mid = synchrony_at_grain(["pair_family", "session_bucket", "direction"], "mid", min_n=3)
print(f"  rows: {len(mid)}  pockets: {mid.groupby(['pair_family','session_bucket','direction']).ngroups}")
print(f"  sign distribution: {mid['sign'].value_counts().to_dict()}")

# Save
coarse.to_csv(OUT / "synchrony_coarse.csv", index=False)
coarse.to_parquet(OUT / "synchrony_coarse.parquet", index=False)
mid.to_csv(OUT / "synchrony_mid.csv", index=False)
mid.to_parquet(OUT / "synchrony_mid.parquet", index=False)

# Per-factor cross-pocket inversion (only at coarse where n is reliable)
inv_rows = []
for factor, grp in coarse.groupby("factor"):
    nn = grp[grp.sign.isin(["shared_winner_condition", "loser_contrast"])]
    n_total = len(grp)
    n_nn = len(nn)
    wp = (nn.sign == "shared_winner_condition").sum()
    lp = (nn.sign == "loser_contrast").sum()
    if n_nn == 0:
        cons, stab = "neutral_or_unstable_only", None
    elif wp == n_nn:
        cons, stab = "shared_winner_universal", 1.0
    elif lp == n_nn:
        cons, stab = "loser_contrast_universal", 1.0
    else:
        cons, stab = "INVERTED_across_pockets", max(wp, lp) / n_nn
    inv_rows.append({
        "factor": factor,
        "grain": "coarse",
        "n_pockets": n_total, "n_non_neutral": n_nn,
        "n_shared_winner": int(wp), "n_loser_contrast": int(lp),
        "consensus": cons, "stability_score": stab,
    })
inv_df = pd.DataFrame(inv_rows).sort_values(["consensus", "stability_score"])
inv_df.to_csv(OUT / "inversion_coarse.csv", index=False)
print(f"\nCoarse-grain factor consensus:")
print(inv_df["consensus"].value_counts().to_string())

# Surface non-neutral coarse-grain findings
print(f"\nNon-neutral coarse-grain factor findings:")
sig = coarse[coarse.sign.isin(["shared_winner_condition","loser_contrast"])].sort_values(["sign","cohens_d"], ascending=[True, False])
if len(sig):
    print(sig[["pair_family","direction","factor","n_winners","n_losers","winner_median","loser_median","cohens_d","sign"]].head(40).to_string(index=False))
else:
    print("(none with n>=3 + CI excluding 0)")

# Inverted factors at coarse
inverted = inv_df[inv_df.consensus == "INVERTED_across_pockets"]
print(f"\nINVERTED at coarse: {len(inverted)} factors")
if len(inverted):
    print(inverted[["factor","n_pockets","n_non_neutral","n_shared_winner","n_loser_contrast","stability_score"]].head(15).to_string(index=False))
print("\nsaved")
