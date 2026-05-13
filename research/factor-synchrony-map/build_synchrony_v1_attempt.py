"""Step 8: Raw Factor Synchrony Map (NOT a score).

Per 2026-05-13 direction:
  - Use only VERIFIED winners (114 rows): 110 actual + 1 confirmed dir-repair + 3 partial dir-repair
  - Compare against verified losers: true_skips, clean_stops, gave_back_green
  - Exclude: unverified TAKE scans, no-development candidates, contaminated rows pending box replay
  - Frame as: 'in this pocket, winners shared X; losers lacked X'
  - Sample-size warnings loud — this is DISCOVERY, not validation

Output per pocket (pair_family × session_bucket × direction):
  Per factor, median + IQR for winners vs losers + Cohen's d + CI + sign label:
    shared_winner_condition  — winner_mean > loser_mean, CI excludes 0
    loser_contrast           — loser_mean > winner_mean, CI excludes 0
    neutral                  — CI includes 0
    inverted                 — same factor reversed in a different pocket
    unstable                 — n too small

Cross-pocket inversion: per factor, count pockets where sign differs.

Honest disclosure:
  Manual winners (46 rows) have only 3 factors (bb_position, ema20_dist_pct,
  bb_band_width_a_bps from regime_manual_tradebook). Broker winners (64+4=68)
  have full 79-factor set. So most factor analyses are broker-only.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/factor-synchrony-map")
OUT.mkdir(parents=True, exist_ok=True)


df = pd.read_parquet(LEDGER)
print(f"ledger: {len(df)}")

# === Define VERIFIED WINNERS ===
mask_actual_winner = df["repair_taxonomy"] == "actual_winner"
mask_dir_repair_confirmed = df["step7_final_verdict"].isin(
    ["direction_repair_confirmed", "direction_repair_partial"]
)
winners = df[mask_actual_winner | mask_dir_repair_confirmed].copy()
print(f"verified winners: {len(winners)}")
print(f"  by source:\n{winners['source_label'].value_counts().to_string()}")
print(f"  with step7_final_verdict promoted:")
print(winners[mask_dir_repair_confirmed.reindex(winners.index, fill_value=False)][["pair","direction","step7_final_verdict","step7_replay_mfe_r"]].to_string())

# === Define VERIFIED LOSERS ===
# Include:
#   - step6b skip_required (24 V3-era)
#   - step7 false_candidate (1)
#   - bot_actual_loser with audit good_entry_clean_loser (5 audit-clean losses)
#   - bot_actual_loser with gave_back_green outcome
# Exclude:
#   - correct_box_replay_required (contaminated, pending box replay)
#   - direction_repair_or_skip without step7 verdict (unverified)

mask_step6b_skip = df["step6b_recommendation"] == "skip_required"
mask_step7_false = df["step7_final_verdict"] == "false_candidate"
mask_audit_clean_loser = df["audit_classification"] == "good_entry_clean_loser"
mask_not_contaminated = df["repair_taxonomy"] != "correct_box_replay_required"
mask_bot_loser = df["source_label"] == "bot_actual_loser"

losers_skip = df[mask_step6b_skip | mask_step7_false].copy()
losers_clean = df[mask_audit_clean_loser & mask_not_contaminated].copy()

# Gave-back-green loser pool: broker rows with mfe_r > 0.3 and realized_r < -0.1, not contaminated
mfe_r_num = pd.to_numeric(df["actual_mfe_r"], errors="coerce")
r_num = pd.to_numeric(df["actual_realized_r"], errors="coerce")
mask_gave_back = mask_bot_loser & mask_not_contaminated & (mfe_r_num > 0.3) & (r_num < -0.1)
losers_gave_back = df[mask_gave_back].copy()

print(f"\nVerified losers:")
print(f"  skip-required: {len(losers_skip)}")
print(f"  audit-clean losers: {len(losers_clean)}")
print(f"  gave-back-green (non-contaminated): {len(losers_gave_back)}")

# Combine, tag with outcome_path
losers_skip["outcome_path"] = "true_skip"
losers_clean["outcome_path"] = "clean_loss"
losers_gave_back["outcome_path"] = "gave_back_green"
all_losers = pd.concat([losers_skip, losers_clean, losers_gave_back], ignore_index=False)
all_losers = all_losers.drop_duplicates(subset="ledger_id")
print(f"  total unique losers: {len(all_losers)}")

# Winner outcome_path from existing fields
def winner_outcome_path(row):
    er = str(row.get("actual_exit_reason", "") or "").lower()
    r = pd.to_numeric(row.get("actual_realized_r"), errors="coerce")
    if pd.notna(r) and r >= 1.5: return "full_tp"
    if pd.notna(r) and r >= 0.5: return "partial_tp"
    if "tp" in er: return "tp_hit"
    if pd.notna(r) and r > 0: return "small_winner"
    if row.get("step7_final_verdict") == "direction_repair_confirmed": return "step7_confirmed_winner"
    if row.get("step7_final_verdict") == "direction_repair_partial": return "step7_ratchet_save"
    return "winner_unclassified"
winners["outcome_path"] = winners.apply(winner_outcome_path, axis=1)
print(f"\nWinner outcome_path:")
print(winners["outcome_path"].value_counts().to_string())

# === Identify factor columns ===
factor_cols = [c for c in df.columns if c.startswith("factor_")]
# Also include the manual bb_position / ema20_dist_pct / bb_band_width_a_bps (lower-case, no factor_ prefix)
extra_manual_factors = ["bb_position", "ema20_dist_pct", "bb_band_width_a_bps"]
print(f"\nfactor_* columns: {len(factor_cols)}")

# Focus on Brock's required factors first; full set as supplement
priority_factors = [
    "factor_bb_position", "factor_wall_proximity", "factor_bb_band_width_a_bps",
    "factor_ema20_dist_pct", "factor_ema50_dist_pct",
    "factor_atr", "factor_otr_ratio", "factor_adr_consumed",
    "factor_rsi", "factor_z_score",
    "factor_spread_pips", "factor_rr_ratio",
    "factor_volume_ratio", "factor_current_volume", "factor_avg_volume",
    "factor_regime_score", "factor_regime_confidence", "factor_box_age_hours",
    "factor_natural_stop_pips", "factor_sma20_dist_signed_bps",
]
priority_factors = [c for c in priority_factors if c in factor_cols]
print(f"priority factors available: {len(priority_factors)}")


# === Compute per-pocket factor stats ===
def cohens_d(w, l):
    nw, nl = len(w), len(l)
    if nw < 2 or nl < 2: return None, None, None
    mw, ml_, sw, sl = w.mean(), l.mean(), w.std(), l.std()
    pool = np.sqrt(((nw - 1)*sw**2 + (nl - 1)*sl**2) / max(nw + nl - 2, 1))
    if pool <= 0: return None, None, None
    d = (mw - ml_) / pool
    se = np.sqrt(sw**2/nw + sl**2/nl)
    ci_low = (mw - ml_) - 1.96 * se
    ci_high = (mw - ml_) + 1.96 * se
    return d, ci_low, ci_high


GRAIN = ["pair_family", "session_bucket", "direction"]

print("\nbuilding factor synchrony per pocket ...")
rows = []
for pocket_keys, w_grp in winners.groupby(GRAIN):
    if any(pd.isna(k) for k in pocket_keys): continue
    pf, sb, dr = pocket_keys
    l_grp = all_losers[
        (all_losers["pair_family"] == pf) &
        (all_losers["session_bucket"] == sb) &
        (all_losers["direction"] == dr)
    ]
    nw = len(w_grp)
    nl = len(l_grp)
    if nw < 1 and nl < 1: continue

    for f in priority_factors:
        if f not in w_grp.columns: continue
        wv = pd.to_numeric(w_grp[f], errors="coerce").dropna()
        lv = pd.to_numeric(l_grp[f], errors="coerce").dropna()
        nwf, nlf = len(wv), len(lv)

        d, ci_low, ci_high = cohens_d(wv, lv) if (nwf >= 2 and nlf >= 2) else (None, None, None)

        if nwf < 3 or nlf < 3:
            sign = "unstable"
        elif d is None:
            sign = "ambiguous"
        elif ci_low is not None and ci_low > 0:
            sign = "shared_winner_condition"
        elif ci_high is not None and ci_high < 0:
            sign = "loser_contrast"
        else:
            sign = "neutral"

        rows.append({
            "pair_family": pf,
            "session_bucket": sb,
            "direction": dr,
            "factor": f.replace("factor_", ""),
            "n_winners": nwf,
            "n_losers": nlf,
            "winner_median": float(wv.median()) if nwf else None,
            "winner_q25": float(wv.quantile(0.25)) if nwf >= 4 else None,
            "winner_q75": float(wv.quantile(0.75)) if nwf >= 4 else None,
            "loser_median": float(lv.median()) if nlf else None,
            "loser_q25": float(lv.quantile(0.25)) if nlf >= 4 else None,
            "loser_q75": float(lv.quantile(0.75)) if nlf >= 4 else None,
            "winner_mean": float(wv.mean()) if nwf else None,
            "loser_mean": float(lv.mean()) if nlf else None,
            "mean_diff": float(wv.mean() - lv.mean()) if (nwf and nlf) else None,
            "cohens_d": float(d) if d is not None else None,
            "ci_low": float(ci_low) if ci_low is not None else None,
            "ci_high": float(ci_high) if ci_high is not None else None,
            "sign": sign,
            "size_warning": "n<3_winners_or_losers" if (nwf < 3 or nlf < 3) else
                          ("n<10_one_side" if (nwf < 10 or nlf < 10) else None),
        })

synchrony = pd.DataFrame(rows)
print(f"  rows: {len(synchrony)}")
print(f"\nsign distribution (raw):")
print(synchrony["sign"].value_counts().to_string())

# === Cross-pocket inversion: which factors flip sign across pockets ===
print("\ncross-pocket inversion analysis ...")
inv_rows = []
for factor, grp in synchrony.groupby("factor"):
    n_total = len(grp)
    n_winner_pos = (grp["sign"] == "shared_winner_condition").sum()
    n_loser_pos = (grp["sign"] == "loser_contrast").sum()
    n_neutral = (grp["sign"] == "neutral").sum()
    n_unstable = (grp["sign"] == "unstable").sum()
    n_non_neutral = n_winner_pos + n_loser_pos

    if n_non_neutral == 0:
        consensus = "neutral_or_unstable"
        stab = None
    elif n_winner_pos == n_non_neutral:
        consensus = "shared_winner_condition_universal"
        stab = 1.0
    elif n_loser_pos == n_non_neutral:
        consensus = "loser_contrast_universal"
        stab = 1.0
    else:
        consensus = "INVERTED_across_pockets"
        stab = max(n_winner_pos, n_loser_pos) / n_non_neutral

    inv_rows.append({
        "factor": factor,
        "n_pockets_total": n_total,
        "n_pockets_non_neutral": n_non_neutral,
        "n_shared_winner": n_winner_pos,
        "n_loser_contrast": n_loser_pos,
        "n_neutral": n_neutral,
        "n_unstable": n_unstable,
        "consensus": consensus,
        "stability_score": stab,
    })

inv_df = pd.DataFrame(inv_rows).sort_values(["consensus", "stability_score"])
print(f"\ncross-pocket consensus:")
print(inv_df["consensus"].value_counts().to_string())


# === Pocket sample-size summary ===
print("\nPocket sample sizes:")
pocket_stats = winners.groupby(GRAIN).size().reset_index(name="n_winners")
pocket_stats_l = all_losers.groupby(GRAIN).size().reset_index(name="n_losers")
pocket_stats = pocket_stats.merge(pocket_stats_l, on=GRAIN, how="outer").fillna(0).astype({"n_winners":"int","n_losers":"int"})
pocket_stats["size_warning"] = pocket_stats.apply(
    lambda r: ("n<3_winners" if r["n_winners"] < 3 else
               ("n<5_winners" if r["n_winners"] < 5 else
                ("n<10_winners" if r["n_winners"] < 10 else None))),
    axis=1
)
print(pocket_stats.to_string(index=False))

# Save
synchrony.to_csv(OUT / "factor_synchrony_per_pocket.csv", index=False)
synchrony.to_parquet(OUT / "factor_synchrony_per_pocket.parquet", index=False)
inv_df.to_csv(OUT / "cross_pocket_inversion.csv", index=False)
pocket_stats.to_csv(OUT / "pocket_sample_sizes.csv", index=False)
print(f"\nsaved {OUT}/")
