"""Era-split factor synchrony rerun with daily-cache quarantine.

Per 2026-05-13: post-Apr-22 audit data has stale daily-derived factors due to
dukascopy daily cache boundary. Quarantine those fields. Re-run synchrony only
on intraday_safe factors. Split eras at the cache boundary.

Eras:
  PRE  = entry_ts <= 2026-04-22 (audit's daily data reliable)
  POST = entry_ts >  2026-04-22 (daily-derived fields contaminated)

Factor lineage (informed by V3 code review):
  DAILY_CONTAMINATED  — uses daily bars at scan time:
    box_age_hours, box_range, ctx_box_age_hours, ctx_box,
    wall_proximity (uses PDH/PDL),
    atr, atr_20pct, atr_60pct, atr_80pct (daily ATR),
    adr_consumed (daily range), range_half, otr_ratio,
    total_overhead, natural_stop_pips, rr_ratio,
    tp_distance_pips, tier_a_flag, tier_b_flag, score, sc_* (downstream)
  INTRADAY_SAFE — M5/hourly/live-tick:
    bb_position, bb_band_width_a_bps, bb_band_width_b_bps,
    bb_percent_b_a, bb_percent_b_b, bb_state_id, bb_state_confidence,
    rsi, z_score,
    ema20_dist_pct, ema50_dist_pct, ema20, ema50, sma20_dist_signed_bps,
    px_vs_ema20_bps, px_vs_ema50_bps,
    current_volume, avg_volume, volume_ratio,
    spread_pips,
    hour_utc, minute_of_day, day_of_week (timing metadata)
  UNKNOWN_LINEAGE / METADATA:
    regime_id, regime_score, regime_confidence (V1/V2 state, computed at scan)
    opening_state_confidence, v3_pairs_total
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/factor-synchrony-era-split")
OUT.mkdir(parents=True, exist_ok=True)

DAILY_CONTAMINATED = {
    "box_age_hours", "box_range", "ctx_box_age_hours", "ctx_box",
    "wall_proximity",
    "atr", "atr_20pct", "atr_60pct", "atr_80pct",
    "adr_consumed", "range_half", "otr_ratio", "total_overhead",
    "natural_stop_pips", "rr_ratio", "tp_distance_pips",
    "tier_a_flag", "tier_b_flag", "score", "scorer_final",
}

INTRADAY_SAFE = {
    "bb_position", "bb_band_width_a_bps", "bb_band_width_b_bps",
    "bb_percent_b_a", "bb_percent_b_b", "bb_state_id", "bb_state_confidence",
    "rsi", "z_score",
    "ema20_dist_pct", "ema50_dist_pct", "ema20", "ema50",
    "sma20_dist_signed_bps", "px_vs_ema20_bps", "px_vs_ema50_bps",
    "current_volume", "avg_volume", "volume_ratio",
    "spread_pips",
    "hour_utc", "minute_of_day", "day_of_week",
}

UNKNOWN_OR_METADATA = {
    "regime_id", "regime_score", "regime_confidence",
    "opening_state_confidence", "v3_pairs_total", "direction_long",
    "ctx_ema20", "ctx_ema50", "ctx_px", "strategy_id",
}


def factor_lineage(factor_name):
    base = factor_name.replace("factor_", "")
    if base in DAILY_CONTAMINATED: return "daily_cache_contaminated"
    if base in INTRADAY_SAFE: return "intraday_safe"
    if base in UNKNOWN_OR_METADATA: return "metadata_or_unknown"
    return "unknown_lineage"


def cohen_d_and_ci(w, l):
    w = pd.to_numeric(w, errors="coerce").dropna()
    l = pd.to_numeric(l, errors="coerce").dropna()
    nw, nl = len(w), len(l)
    if nw < 2 or nl < 2: return None, None, None, nw, nl
    mw, ml_, sw, sl = w.mean(), l.mean(), w.std(), l.std()
    pool = np.sqrt(((nw - 1)*sw**2 + (nl - 1)*sl**2) / max(nw + nl - 2, 1))
    if pool <= 0: return None, None, None, nw, nl
    d = (mw - ml_) / pool
    se = np.sqrt(sw**2/nw + sl**2/nl)
    return d, (mw - ml_) - 1.96*se, (mw - ml_) + 1.96*se, nw, nl


# === Load ===
df = pd.read_parquet(LEDGER)
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True, errors="coerce")

# Era assignment
boundary = pd.Timestamp("2026-04-22", tz="UTC")
df["era"] = np.where(df["entry_ts"] <= boundary, "pre", "post")
print(f"Era distribution:")
print(df.groupby(["era", "source_label"]).size().unstack(fill_value=0).to_string())

# Winners + losers (broker non-contaminated)
mask_winner = (df["source_label"] == "bot_actual_winner") | (
    df["step7_final_verdict"].isin(["direction_repair_confirmed", "direction_repair_partial"])
)
mask_loser = (df["source_label"] == "bot_actual_loser") & (df["repair_taxonomy"] != "correct_box_replay_required")
winners = df[mask_winner].copy()
losers = df[mask_loser].copy()
print(f"\nwinners (broker): {len(winners)} total")
print(f"  pre-boundary: {(winners['era'] == 'pre').sum()}")
print(f"  post-boundary: {(winners['era'] == 'post').sum()}")
print(f"losers (broker non-contaminated): {len(losers)} total")
print(f"  pre-boundary: {(losers['era'] == 'pre').sum()}")
print(f"  post-boundary: {(losers['era'] == 'post').sum()}")


# === Factor lineage table ===
all_factor_cols = sorted([c for c in df.columns if c.startswith("factor_")])
lineage_rows = []
for c in all_factor_cols:
    base = c.replace("factor_", "")
    lin = factor_lineage(c)
    sample_vals = pd.to_numeric(df[c], errors="coerce").dropna()
    lineage_rows.append({
        "factor": base,
        "lineage": lin,
        "n_non_null": int(len(sample_vals)),
        "min": float(sample_vals.min()) if len(sample_vals) else None,
        "median": float(sample_vals.median()) if len(sample_vals) else None,
        "max": float(sample_vals.max()) if len(sample_vals) else None,
        "all_zero": bool(len(sample_vals) and (sample_vals == 0).all()),
    })
lineage_df = pd.DataFrame(lineage_rows)
lineage_df.to_csv(OUT / "factor_lineage.csv", index=False)
print(f"\nfactor lineage counts:")
print(lineage_df["lineage"].value_counts().to_string())
print()
# Flag the all-zero factors (broken in audit)
broken = lineage_df[lineage_df["all_zero"]]
print(f"all-zero factors in ledger (broken in audit reconstruction): {len(broken)}")
if len(broken):
    print(broken[["factor","lineage"]].to_string(index=False))
print()


# === Per-era synchrony on intraday_safe factors ONLY ===
intraday_factors = [f"factor_{c}" for c in INTRADAY_SAFE if f"factor_{c}" in df.columns]
print(f"intraday-safe factors available: {len(intraday_factors)}")


def synchrony_for_era(era_label, w, l, factors):
    rows = []
    for (pf, dr), wg in w.groupby(["pair_family", "direction"]):
        lg = l[(l["pair_family"] == pf) & (l["direction"] == dr)]
        for f in factors:
            d, lo, hi, nw, nl = cohen_d_and_ci(wg[f], lg[f])
            wm = pd.to_numeric(wg[f], errors="coerce").dropna()
            lm_ = pd.to_numeric(lg[f], errors="coerce").dropna()
            if nw < 3 or nl < 3: sign = "unstable"
            elif d is None: sign = "ambiguous"
            elif lo is not None and lo > 0: sign = "shared_winner_condition"
            elif hi is not None and hi < 0: sign = "loser_contrast"
            else: sign = "neutral"
            rows.append({
                "era": era_label, "pair_family": pf, "direction": dr,
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
            })
    return pd.DataFrame(rows)


print("\n=== PRE-BOUNDARY ERA SYNCHRONY ===")
pre_w = winners[winners["era"] == "pre"]
pre_l = losers[losers["era"] == "pre"]
pre_sync = synchrony_for_era("pre", pre_w, pre_l, intraday_factors)
print(f"  rows: {len(pre_sync)}")
print(f"  sign distribution: {pre_sync['sign'].value_counts().to_dict()}")
pre_sig = pre_sync[pre_sync.sign.isin(["shared_winner_condition","loser_contrast"])]
print(f"  significant findings: {len(pre_sig)}")

print("\n=== POST-BOUNDARY ERA SYNCHRONY ===")
post_w = winners[winners["era"] == "post"]
post_l = losers[losers["era"] == "post"]
post_sync = synchrony_for_era("post", post_w, post_l, intraday_factors)
print(f"  rows: {len(post_sync)}")
print(f"  sign distribution: {post_sync['sign'].value_counts().to_dict()}")
post_sig = post_sync[post_sync.sign.isin(["shared_winner_condition","loser_contrast"])]
print(f"  significant findings: {len(post_sig)}")


# === Cross-era consistency check ===
print("\n=== CROSS-ERA CONSISTENCY ===")
print("Per (pair_family, direction, factor): does sign agree across eras?")
join = pre_sync.merge(post_sync, on=["pair_family", "direction", "factor"], suffixes=("_pre", "_post"), how="outer")
join = join.dropna(subset=["sign_pre", "sign_post"])
def consistency(pre, post):
    if pre == post and pre in ("shared_winner_condition", "loser_contrast"): return "consistent_signal"
    if pre == post: return "consistent_noise"
    if pre == "unstable" or post == "unstable": return "n_too_small_in_one"
    if pre in ("shared_winner_condition","loser_contrast") and post == "neutral": return "pre_only"
    if post in ("shared_winner_condition","loser_contrast") and pre == "neutral": return "post_only"
    if (pre == "shared_winner_condition" and post == "loser_contrast") or (pre == "loser_contrast" and post == "shared_winner_condition"):
        return "INVERTED"
    return "other"
join["consistency"] = join.apply(lambda r: consistency(r["sign_pre"], r["sign_post"]), axis=1)
print(join["consistency"].value_counts().to_string())

consistent_signals = join[join["consistency"] == "consistent_signal"]
print(f"\nconsistent_signal rows (factor agrees across BOTH eras): {len(consistent_signals)}")
if len(consistent_signals):
    print(consistent_signals[["pair_family","direction","factor","sign_pre","cohens_d_pre","cohens_d_post","n_winners_pre","n_winners_post"]].to_string(index=False))

inverted = join[join["consistency"] == "INVERTED"]
print(f"\nINVERTED rows (factor flipped sign between eras): {len(inverted)}")
if len(inverted):
    print(inverted[["pair_family","direction","factor","sign_pre","sign_post","cohens_d_pre","cohens_d_post"]].to_string(index=False))


# Save outputs
pre_sync.to_csv(OUT / "synchrony_pre_boundary.csv", index=False)
post_sync.to_csv(OUT / "synchrony_post_boundary.csv", index=False)
join.to_csv(OUT / "cross_era_join.csv", index=False)
consistent_signals.to_csv(OUT / "consistent_signals.csv", index=False)
print(f"\nsaved {OUT}/")
