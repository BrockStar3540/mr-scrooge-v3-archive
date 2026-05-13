"""Live-Epoch Conditional Factor Atlas v0.

Per locked 2026-05-13 direction:
  - OLD regime labels (V2 Alpha/Echo, V1 CAUTION/NORMAL/RESTRICTED) are
    metadata only, NOT clustering drivers.
  - Primary grain: strategy_branch × pair_family × session × direction × outcome_type
  - Discover what winners synchronize around — do NOT pre-impose regime structure.

Outcome taxonomy (derived per trade, one-and-only-one assignment):
  full_tp           — tp2_hit OR realized_r >= 0.95 * r_multiple
  quick_tp          — tp1_hit AND NOT tp2_hit AND realized_r > 0.4 * r_multiple
  ratchet_save      — be_hit AND ratchet_triggered AND |realized_r| <= 0.15
  gave_back_green   — mfe_r > 0.3 AND realized_r < -0.1
  clean_stop        — realized_r <= -0.95 AND mfe_r < 0.15
  partial_loss      — other losing trades
  timed_exit        — exit_reason indicates time/cycle
  unclear           — fallback

Answers (per Brock 2026-05-13):
  1. What factor states repeat in winners (full_tp, quick_tp, ratchet_save)?
  2. What factor states repeat in losers?
  3. Which factors invert by pair/session/direction/strategy?
  4. Which exit path do winners share within a geometric cell?
  5. Which losing trades looked close (matched a winner's factor signature)?
"""
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timezone

SRC = "/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/factor_audit/per_trade_factors_filled.csv.gz"
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/live-epoch-factor-atlas-v0")
OUT.mkdir(parents=True, exist_ok=True)

PAIR_FAMILY = {
    "EUR_USD": "usd_base", "GBP_USD": "usd_base", "AUD_USD": "usd_base",
    "NZD_USD": "usd_base", "USD_JPY": "usd_base", "USD_CHF": "usd_base",
    "USD_CAD": "usd_base", "USD_MXN": "usd_base",
    "EUR_GBP": "eur_cross", "EUR_AUD": "eur_cross", "EUR_NZD": "eur_cross",
    "EUR_CAD": "eur_cross", "EUR_CHF": "eur_cross", "EUR_JPY": "eur_cross",
    "GBP_AUD": "gbp_cross", "GBP_NZD": "gbp_cross", "GBP_CAD": "gbp_cross",
    "GBP_CHF": "gbp_cross", "GBP_JPY": "gbp_cross",
    "AUD_NZD": "antipodean_cross", "AUD_CAD": "antipodean_cross",
    "AUD_CHF": "antipodean_cross", "AUD_JPY": "antipodean_cross",
    "NZD_JPY": "antipodean_cross", "CAD_JPY": "antipodean_cross",
    "CHF_JPY": "antipodean_cross",
}


def session_of(h):
    if pd.isna(h): return "unknown"
    h = int(h) % 24
    if 22 <= h or h < 6: return "asia"
    elif 6 <= h < 12: return "london"
    elif 12 <= h < 16: return "overlap"
    else: return "ny_pm"


def derive_outcome(row):
    r = row["realized_r"]
    rm = row.get("r_multiple", 2.0) or 2.0
    mfe = row.get("max_favorable_r", 0) or 0
    tp1 = bool(row.get("tp1_hit", False))
    tp2 = bool(row.get("tp2_hit", False))
    be = bool(row.get("be_hit", False))
    ratchet = bool(row.get("ratchet_triggered", False))
    er = str(row.get("exit_reason", "") or "").lower()

    if pd.isna(r): return "unclear"
    if tp2 or r >= 0.95 * rm: return "full_tp"
    if tp1 and not tp2 and r > 0.4 * rm: return "quick_tp"
    if be and ratchet and -0.15 <= r <= 0.15: return "ratchet_save"
    if "time" in er or "cycle" in er: return "timed_exit"
    if mfe > 0.3 and r < -0.1: return "gave_back_green"
    if r <= -0.95 and mfe < 0.15: return "clean_stop"
    if r < -0.1: return "partial_loss"
    return "unclear"


print(f"loading {SRC} ...")
df = pd.read_csv(SRC)
df["ts"] = pd.to_datetime(df["ts"], utc=True)
df["pair_family"] = df["symbol"].map(PAIR_FAMILY).fillna("other")
df["session"] = df["hour_utc"].apply(session_of)
df["winner"] = df["realized_r"] > 0

# r_multiple not in source; derive from tp_distance_pips / natural_stop_pips when available
# Default to 2.0 (the corpus run's setting)
df["r_multiple"] = 2.0  # walker default
df["outcome_type"] = df.apply(derive_outcome, axis=1)

print(f"  rows: {len(df):,}")
print(f"  outcome distribution:")
print(df["outcome_type"].value_counts().to_string())
print()

# Geometric cell key
GEOM_KEYS = ["strategy", "pair_family", "session", "direction"]

# Factor cols (same exclusion as before)
IDENTITY = {"candidate_id", "scan_id", "ts", "symbol", "strategy", "regime",
            "direction", "tier", "exit_reason"}
SETUP = {"entry_price", "stop_price", "tp1_price", "take_profit", "fill_price",
         "natural_stop_pips", "tp_distance_pips"}
OUTCOME = {"realized_r", "max_favorable_r", "max_adverse_r", "holding_minutes",
           "tp1_hit", "tp2_hit", "be_hit", "ratchet_triggered", "filled",
           "gate_passed", "time_to_fill_minutes", "won_realized_r_pos",
           "won_hit_05_first", "won_hit_1r_first", "hit_0_5r_before_minus_1r",
           "hit_1r_before_minus_1r", "time_to_0_5r", "time_to_1r"}
ML = {"ml_prob_dbb_trend", "ml_prob_dbb_trend_raw"}
DERIVED = {"pair_family", "session", "winner", "outcome_type", "r_multiple"}
EXCLUDE = IDENTITY | SETUP | OUTCOME | ML | DERIVED

factor_cols = [c for c in df.columns
               if c not in EXCLUDE and df[c].dtype in (np.float64, np.int64)]
print(f"  factors: {len(factor_cols)}")
print()


# === 1. Outcome composition per geometric cell ===
print("1/4: outcome composition per geometric cell...")
comp = df.groupby(GEOM_KEYS + ["outcome_type"]).size().unstack(fill_value=0)
comp["total"] = comp.sum(axis=1)
for o in ["full_tp", "quick_tp", "ratchet_save", "gave_back_green",
          "clean_stop", "partial_loss", "timed_exit", "unclear"]:
    if o not in comp.columns: comp[o] = 0
    comp[f"{o}_pct"] = comp[o] / comp["total"] * 100
comp = comp.reset_index().sort_values(["strategy", "pair_family", "session", "direction"])
comp.to_csv(OUT / "outcome_composition_per_cell.csv", index=False)
print(f"   → {len(comp)} cells")


# === 2. Factor profile per (cell, outcome_type) ===
print("2/4: factor profile per (geometric cell × outcome_type)...")
profile_rows = []
for keys, grp in df.groupby(GEOM_KEYS + ["outcome_type"]):
    if len(grp) < 20:
        continue
    s, pf, ses, dr, oc = keys
    for f in factor_cols:
        vals = grp[f].dropna()
        if len(vals) < 10:
            continue
        profile_rows.append({
            "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
            "outcome_type": oc,
            "factor": f,
            "n": len(vals),
            "median": vals.median(),
            "q25": vals.quantile(0.25),
            "q75": vals.quantile(0.75),
            "mean": vals.mean(),
        })
profile = pd.DataFrame(profile_rows)
profile.to_parquet(OUT / "factor_profile_per_cell_outcome.parquet", index=False)
profile.to_csv(OUT / "factor_profile_per_cell_outcome.csv", index=False)
print(f"   → {len(profile):,} profile rows")


# === 3. Contrasts: full_tp vs clean_stop within same geometric cell ===
print("3/4: contrasts full_tp vs clean_stop (winners vs failed-entries)...")
def cohen_d_from_two_samples(w, l):
    nw, nl = len(w), len(l)
    if nw < 5 or nl < 5: return np.nan, np.nan, np.nan
    mw, ml_ = w.mean(), l.mean()
    sw, sl = w.std(), l.std()
    pool = np.sqrt(((nw-1)*sw**2 + (nl-1)*sl**2) / max(nw+nl-2,1))
    if pool == 0: return mw - ml_, np.nan, np.nan
    d = (mw - ml_) / pool
    se = np.sqrt(sw**2/nw + sl**2/nl)
    return mw - ml_, d, se


contrasts = []
for keys, grp in df.groupby(GEOM_KEYS):
    s, pf, ses, dr = keys
    winners = grp[grp.outcome_type.isin(["full_tp", "quick_tp", "ratchet_save"])]
    losers = grp[grp.outcome_type.isin(["clean_stop", "partial_loss", "gave_back_green"])]
    if len(winners) < 20 or len(losers) < 20:
        continue
    for f in factor_cols:
        w = winners[f].dropna()
        l = losers[f].dropna()
        if len(w) < 10 or len(l) < 10:
            continue
        diff, d, se = cohen_d_from_two_samples(w, l)
        ci_low = diff - 1.96 * se if pd.notna(se) else np.nan
        ci_high = diff + 1.96 * se if pd.notna(se) else np.nan
        if pd.isna(ci_low):
            sign = "neutral"
        elif ci_low > 0:
            sign = "winner_positive"
        elif ci_high < 0:
            sign = "loser_positive"
        else:
            sign = "neutral"
        contrasts.append({
            "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
            "factor": f,
            "n_winners": len(w), "n_losers": len(l),
            "winner_mean": w.mean(), "loser_mean": l.mean(),
            "winner_median": w.median(), "loser_median": l.median(),
            "mean_diff": diff,
            "cohens_d": d,
            "ci_low_95": ci_low, "ci_high_95": ci_high,
            "sign": sign,
        })
contrast_df = pd.DataFrame(contrasts)
contrast_df.to_parquet(OUT / "winner_vs_loser_contrast.parquet", index=False)
contrast_df.to_csv(OUT / "winner_vs_loser_contrast.csv", index=False)
print(f"   → {len(contrast_df):,} contrast rows ({contrast_df.groupby(GEOM_KEYS).ngroups} cells × {len(factor_cols)} factors)")


# === 4. Management-only contrast: full_tp vs gave_back_green within cell ===
# Same entry signal, different management outcome — isolates management failure
print("4/4: management contrast (full_tp vs gave_back_green)...")
mgmt = []
for keys, grp in df.groupby(GEOM_KEYS):
    s, pf, ses, dr = keys
    a = grp[grp.outcome_type == "full_tp"]
    b = grp[grp.outcome_type == "gave_back_green"]
    if len(a) < 20 or len(b) < 20:
        continue
    for f in factor_cols:
        w, l = a[f].dropna(), b[f].dropna()
        if len(w) < 10 or len(l) < 10:
            continue
        diff, d, se = cohen_d_from_two_samples(w, l)
        if pd.isna(se):
            sign = "neutral"
        else:
            ci_low = diff - 1.96*se; ci_high = diff + 1.96*se
            if ci_low > 0: sign = "full_tp_higher"
            elif ci_high < 0: sign = "gave_back_higher"
            else: sign = "neutral"
        mgmt.append({
            "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
            "factor": f,
            "n_full_tp": len(w), "n_gave_back": len(l),
            "full_tp_median": w.median(), "gave_back_median": l.median(),
            "mean_diff": diff, "cohens_d": d, "sign": sign,
        })
mgmt_df = pd.DataFrame(mgmt)
mgmt_df.to_csv(OUT / "management_contrast_fulltp_vs_giveback.csv", index=False)
print(f"   → {len(mgmt_df):,} management-contrast rows")


# === 5. Inversion analysis on winner-vs-loser contrast ===
print("\ninversion analysis (factor × strategy)...")
inv_rows = []
for (s, f), grp in contrast_df.groupby(["strategy", "factor"]):
    nn = grp[grp.sign != "neutral"]
    n_total = len(grp)
    n_nn = len(nn)
    wp = (nn.sign == "winner_positive").sum()
    lp = (nn.sign == "loser_positive").sum()
    if n_nn == 0:
        cons = "neutral_only"; stab = None
    elif wp == n_nn:
        cons = "winner_positive"; stab = 1.0
    elif lp == n_nn:
        cons = "loser_positive"; stab = 1.0
    else:
        cons = "INVERTED"; stab = max(wp, lp) / n_nn
    inv_rows.append({
        "strategy": s, "factor": f,
        "n_cells_total": n_total, "n_cells_non_neutral": n_nn,
        "n_winner_positive": wp, "n_loser_positive": lp,
        "consensus": cons, "stability_score": stab,
    })
inv_df = pd.DataFrame(inv_rows).sort_values(["strategy", "consensus", "stability_score"])
inv_df.to_csv(OUT / "inversion_report.csv", index=False)
inv_df[inv_df.consensus == "INVERTED"].to_csv(OUT / "headline_inversions.csv", index=False)


# === 6. Old-regime annotation table (METADATA, NOT clustering driver) ===
print("\nold-regime annotation (metadata only)...")
regime_anno = df.groupby(GEOM_KEYS + ["regime"]).size().unstack(fill_value=0)
regime_anno = regime_anno.reset_index()
regime_anno.to_csv(OUT / "old_regime_annotation.csv", index=False)


# === Summary ===
report = []
report.append("# Live-Epoch Conditional Factor Atlas v0")
report.append("")
report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
report.append("")
report.append("## Design")
report.append("")
report.append("**Old regime labels are METADATA, not clustering drivers.** The atlas")
report.append("discovers what winners synchronize around without pre-imposing regime structure.")
report.append("")
report.append("Primary grain: `strategy_branch × pair_family × session × direction × outcome_type`")
report.append("")
report.append("Old regime labels (V1/V2 CAUTION/NORMAL/RESTRICTED) preserved in")
report.append("`old_regime_annotation.csv` as annotation; not used to define cells.")
report.append("")
report.append("## Scope (live epoch only — by design)")
report.append("")
report.append(f"- Source: per_trade_factors_filled.csv.gz — {len(df):,} filled trades")
report.append(f"- Time: {df.ts.min().date()} → {df.ts.max().date()} (30 days, all post-2024 — the current live epoch)")
report.append(f"- Strategies: {sorted(df.strategy.unique())}")
report.append(f"- Pair families: {sorted(df.pair_family.unique())}")
report.append(f"- Sessions: {sorted(df.session.unique())}")
report.append(f"- Factor columns: {len(factor_cols)}")
report.append("")
report.append("## Outcome taxonomy distribution")
report.append("")
oc_pct = df["outcome_type"].value_counts(normalize=True) * 100
oc_n = df["outcome_type"].value_counts()
oc_table = pd.DataFrame({"n": oc_n, "pct": oc_pct})
report.append(oc_table.to_markdown(floatfmt=".2f"))
report.append("")
report.append("## Files (this is the discovery substrate; act on it, don't summarize it)")
report.append("")
report.append("| File | Purpose |")
report.append("|---|---|")
report.append("| `outcome_composition_per_cell.csv` | What share of trades in each geom cell ended in each outcome |")
report.append("| `factor_profile_per_cell_outcome.csv/parquet` | Per-factor median/IQR per cell per outcome |")
report.append("| `winner_vs_loser_contrast.csv/parquet` | Factor signal: full_tp+quick_tp+ratchet_save vs clean_stop+partial_loss+gave_back |")
report.append("| `management_contrast_fulltp_vs_giveback.csv` | SAME entry quality, different management — isolates management failure factors |")
report.append("| `inversion_report.csv` | Per (strategy, factor): does sign vary across cells? |")
report.append("| `headline_inversions.csv` | Just the INVERTED factors |")
report.append("| `old_regime_annotation.csv` | METADATA only — old V1/V2 regime labels by cell |")
report.append("")
report.append("## Inversion headline (winner vs loser contrast)")
report.append("")
report.append("Across primary geometric cells (strategy × pair_family × session × direction):")
report.append("")
report.append(inv_df.groupby(["strategy", "consensus"]).size().unstack(fill_value=0).to_markdown())
report.append("")
report.append("### Most-inverted factors")
report.append("")
inverted = inv_df[inv_df.consensus == "INVERTED"].sort_values("stability_score")
if len(inverted):
    report.append(inverted.head(20).to_markdown(index=False, floatfmt=".3f"))
report.append("")
report.append("### Universal winner-positive (across all non-neutral cells)")
report.append("")
wp = inv_df[inv_df.consensus == "winner_positive"].sort_values("n_cells_non_neutral", ascending=False)
if len(wp):
    report.append(wp.head(15).to_markdown(index=False, floatfmt=".3f"))
report.append("")
report.append("### Universal loser-positive")
report.append("")
lp = inv_df[inv_df.consensus == "loser_positive"].sort_values("n_cells_non_neutral", ascending=False)
if len(lp):
    report.append(lp.head(15).to_markdown(index=False, floatfmt=".3f"))
report.append("")
report.append("## How to use")
report.append("")
report.append("1. `outcome_composition_per_cell.csv` — find cells with high `full_tp_pct` and/or low `clean_stop_pct`.")
report.append("   These are the cells where the bot's current entry+management actually works.")
report.append("2. `winner_vs_loser_contrast.csv` — for each such cell, look up which factors define winners vs losers.")
report.append("3. `management_contrast_fulltp_vs_giveback.csv` — for cells with high `gave_back_green` share,")
report.append("   compare factor signature to `full_tp` to identify management bugs.")
report.append("4. `headline_inversions.csv` — these are the factors where conditional logic matters most.")
report.append("   Same factor flips meaning across cells. Do NOT score them globally.")
report.append("5. Cluster naming comes from looking at OUTCOME-WINNER signatures (full_tp full_tp full_tp")
report.append("   patterns across geometric cells), not from the old V1/V2 regime labels.")
report.append("")
report.append("## Constraints (per direction 2026-05-13)")
report.append("")
report.append("- Do NOT collapse into one global score")
report.append("- Do NOT use V1/V2 regime labels as clustering drivers (they're annotations)")
report.append("- Discovery period is 30 days = the current live epoch. Treat findings as describing")
report.append("  this epoch, not validated across history")
report.append("- v1 should extend corpus feature extraction so this same workflow runs at corpus scale")

Path(OUT / "summary.md").write_text("\n".join(report))
print(f"\n✅ summary at {OUT / 'summary.md'}")
print("\nOutputs:")
for f in sorted(OUT.iterdir()):
    print(f"  {f.name}: {f.stat().st_size} B")
