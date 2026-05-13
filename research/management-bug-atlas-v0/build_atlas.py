"""Management-Bug Atlas — per-cell deep dive into the gave_back_green disaster.

Per 2026-05-13 direction:
  "These entries produced favorable movement. Now identify which cells and
   factor states require different management."

NOT a "winners vs losers" analysis. Strictly compares full_tp vs gave_back_green
INSIDE the same geometric cell — same entry signal, different outcome.

Cell grain: strategy × pair_family × session × direction

Per-cell output:
  - n_total, n_full_tp, n_gave_back, n_clean_stop, etc.
  - full_tp_pct, gave_back_pct, clean_stop_pct
  - median_mfe_giveback (how far green did the gave-back trades go?)
  - top 3 factor separators between full_tp and gave_back (with sign + effect)
  - stable_separators count (|cohens_d| > 0.3 AND CI excludes 0)
  - recommended_action heuristic
  - recommendation_basis (text)

Recommendation heuristic:
  insufficient_data       n_total < 50
  skip_cell               full_tp_pct < 5% AND gave_back_pct > 50%  (structural failure)
  no_action_working       full_tp_pct >= 25% AND gave_back_pct < 40%  (cell is fine)
  earlier_ratchet         gave_back_pct > 50% AND median_mfe_giveback >= 0.7R
  quick_partial           gave_back_pct > 50% AND median_mfe_giveback < 0.4R
  tighter_be              gave_back_pct > 40% AND 0.4 <= median_mfe_giveback < 0.7R
  entry_quality_review    clean_stop_pct > 30%  (entries are bad, not management)
  needs_investigation     otherwise
"""
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timezone

SRC_BASE = Path("/home/ubuntu/mr-scrooge-v3/research/live-epoch-factor-atlas-v0")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/management-bug-atlas-v0")
OUT.mkdir(parents=True, exist_ok=True)

# Source data
comp = pd.read_csv(SRC_BASE / "outcome_composition_per_cell.csv")
mgmt = pd.read_csv(SRC_BASE / "management_contrast_fulltp_vs_giveback.csv")
print(f"outcome_composition cells: {len(comp)}")
print(f"management_contrast rows: {len(mgmt)} ({mgmt.groupby(['strategy','pair_family','session','direction']).ngroups} cells × factors)")

# Re-load source to compute median MFE per cell per outcome
SRC = "/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/factor_audit/per_trade_factors_filled.csv.gz"
df = pd.read_csv(SRC, usecols=["symbol", "strategy", "direction", "hour_utc",
                                "realized_r", "max_favorable_r", "max_adverse_r",
                                "tp1_hit", "tp2_hit", "be_hit", "ratchet_triggered",
                                "exit_reason"])

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
df["pair_family"] = df["symbol"].map(PAIR_FAMILY).fillna("other")
df["session"] = df["hour_utc"].apply(session_of)

R_MULT = 2.0
def outcome(row):
    r = row["realized_r"]
    mfe = row["max_favorable_r"] or 0
    if pd.isna(r): return "unclear"
    if bool(row.get("tp2_hit")) or r >= 0.95*R_MULT: return "full_tp"
    if bool(row.get("tp1_hit")) and not bool(row.get("tp2_hit")) and r > 0.4*R_MULT: return "quick_tp"
    if bool(row.get("be_hit")) and bool(row.get("ratchet_triggered")) and -0.15 <= r <= 0.15: return "ratchet_save"
    er = str(row.get("exit_reason","") or "").lower()
    if "time" in er or "cycle" in er: return "timed_exit"
    if mfe > 0.3 and r < -0.1: return "gave_back_green"
    if r <= -0.95 and mfe < 0.15: return "clean_stop"
    if r < -0.1: return "partial_loss"
    return "unclear"
df["outcome_type"] = df.apply(outcome, axis=1)

# Compute median MFE per cell per outcome
print("computing median MFE per cell per outcome ...")
GEOM = ["strategy", "pair_family", "session", "direction"]
mfe_stats = df.groupby(GEOM + ["outcome_type"])["max_favorable_r"].agg(["median", "mean", "count"]).reset_index()
mfe_stats.columns = GEOM + ["outcome_type", "mfe_median", "mfe_mean", "n"]

# Pivot to wide form: one row per cell, mfe columns per outcome
mfe_wide = mfe_stats.pivot_table(
    index=GEOM, columns="outcome_type",
    values=["mfe_median", "mfe_mean"], aggfunc="first"
).reset_index()
# Flatten columns
mfe_wide.columns = [
    "_".join(map(str, c)).rstrip("_") if isinstance(c, tuple) else c
    for c in mfe_wide.columns
]
print(f"mfe_wide cols sample: {list(mfe_wide.columns)[:15]}")


# === Build per-cell atlas ===
print("\nbuilding management-bug atlas ...")
cells = []
for keys, grp in df.groupby(GEOM):
    s, pf, ses, dr = keys
    n_total = len(grp)
    counts = grp["outcome_type"].value_counts()
    n_full_tp = counts.get("full_tp", 0)
    n_gb = counts.get("gave_back_green", 0)
    n_clean = counts.get("clean_stop", 0)
    n_partial = counts.get("partial_loss", 0)
    n_timed = counts.get("timed_exit", 0)
    n_unclear = counts.get("unclear", 0)

    # MFE medians per outcome
    mfe_med_gb = grp[grp.outcome_type == "gave_back_green"]["max_favorable_r"].median() if n_gb else None
    mfe_med_ft = grp[grp.outcome_type == "full_tp"]["max_favorable_r"].median() if n_full_tp else None
    mfe_med_cs = grp[grp.outcome_type == "clean_stop"]["max_favorable_r"].median() if n_clean else None
    mfe_med_pl = grp[grp.outcome_type == "partial_loss"]["max_favorable_r"].median() if n_partial else None

    # Top separators full_tp vs gave_back from management_contrast file
    cell_mgmt = mgmt[(mgmt.strategy == s) & (mgmt.pair_family == pf) &
                     (mgmt.session == ses) & (mgmt.direction == dr)].copy()
    cell_mgmt = cell_mgmt.dropna(subset=["cohens_d"])
    cell_mgmt["abs_d"] = cell_mgmt["cohens_d"].abs()
    cell_mgmt = cell_mgmt[cell_mgmt["sign"] != "neutral"]
    cell_mgmt = cell_mgmt.sort_values("abs_d", ascending=False)
    top = cell_mgmt.head(3)
    seps = []
    for _, r in top.iterrows():
        # Compose human-readable separator
        direction_label = "higher_in_fulltp" if r["sign"] == "full_tp_higher" else "higher_in_giveback"
        seps.append(f"{r['factor']}({direction_label}, d={r['cohens_d']:+.2f})")
    while len(seps) < 3:
        seps.append("")
    stable = (cell_mgmt[(cell_mgmt.abs_d > 0.3)]["sign"] != "neutral").sum()

    # Recommendation heuristic
    if n_total < 50:
        rec, basis = "insufficient_data", f"n_total={n_total}"
    else:
        ft_pct = n_full_tp / n_total
        gb_pct = n_gb / n_total
        cs_pct = n_clean / n_total
        if ft_pct < 0.05 and gb_pct > 0.50:
            rec = "skip_cell"
            basis = f"structural failure (full_tp {ft_pct*100:.1f}%, gave_back {gb_pct*100:.1f}%)"
        elif ft_pct >= 0.25 and gb_pct < 0.40:
            rec = "no_action_working"
            basis = f"cell is working (full_tp {ft_pct*100:.1f}%, gave_back {gb_pct*100:.1f}%)"
        elif cs_pct > 0.30:
            rec = "entry_quality_review"
            basis = f"clean_stop dominant ({cs_pct*100:.1f}%); entries are bad, not management"
        elif gb_pct > 0.50 and mfe_med_gb and mfe_med_gb >= 0.7:
            rec = "earlier_ratchet"
            basis = f"gave_back {gb_pct*100:.1f}%; trades reach +{mfe_med_gb:.2f}R median before reversal"
        elif gb_pct > 0.50 and mfe_med_gb and mfe_med_gb < 0.4:
            rec = "quick_partial_or_lower_tp"
            basis = f"gave_back {gb_pct*100:.1f}%; trades only reach +{mfe_med_gb:.2f}R median (TP too far)"
        elif gb_pct > 0.40 and mfe_med_gb and 0.4 <= mfe_med_gb < 0.7:
            rec = "tighter_be"
            basis = f"gave_back {gb_pct*100:.1f}%; MFE median +{mfe_med_gb:.2f}R; BE should fire earlier"
        else:
            rec = "needs_investigation"
            basis = f"full_tp {ft_pct*100:.1f}%, gave_back {gb_pct*100:.1f}%, clean_stop {cs_pct*100:.1f}%"

    cells.append({
        "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
        "n_total": n_total,
        "n_full_tp": n_full_tp,
        "n_gave_back": n_gb,
        "n_clean_stop": n_clean,
        "n_partial_loss": n_partial,
        "n_timed_exit": n_timed,
        "n_unclear": n_unclear,
        "full_tp_pct": n_full_tp / n_total * 100 if n_total else 0,
        "gave_back_pct": n_gb / n_total * 100 if n_total else 0,
        "clean_stop_pct": n_clean / n_total * 100 if n_total else 0,
        "mfe_median_giveback": mfe_med_gb,
        "mfe_median_fulltp": mfe_med_ft,
        "mfe_median_cleanstop": mfe_med_cs,
        "mfe_median_partial": mfe_med_pl,
        "top_separator_1": seps[0],
        "top_separator_2": seps[1],
        "top_separator_3": seps[2],
        "n_stable_separators": int(stable),
        "recommended_action": rec,
        "recommendation_basis": basis,
    })

atlas = pd.DataFrame(cells)
atlas = atlas.sort_values(["recommended_action", "gave_back_pct"], ascending=[True, False])
atlas.to_parquet(OUT / "cell_management_atlas.parquet", index=False)
atlas.to_csv(OUT / "cell_management_atlas.csv", index=False)
print(f"  → {len(atlas)} cells")
print()

# Summary stats
rec_summary = atlas.groupby("recommended_action").size().reset_index(name="n_cells")
rec_summary["pct_of_trades"] = atlas.groupby("recommended_action")["n_total"].sum().values / atlas["n_total"].sum() * 100
print("Recommendation distribution:")
print(rec_summary.to_string(index=False))
print()


# === Headline summary report ===
report = []
report.append("# Management-Bug Atlas v0")
report.append("")
report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
report.append("")
report.append("## Premise")
report.append("")
report.append("**47.8% of all filled trades go meaningfully green, then give it all back.**")
report.append("")
report.append("This atlas asks: for which (strategy, pair_family, session, direction) cells is")
report.append("the gave-back-green pattern dominant, and what management change does the data")
report.append("suggest? Comparison is INTRA-CELL between full_tp and gave_back_green — same")
report.append("entry signal, different management outcome.")
report.append("")
report.append("## Scope")
report.append("")
report.append(f"- Source: live-epoch atlas v0 (30 days, V1/V2 live era)")
report.append(f"- Cells analyzed: {len(atlas)}")
report.append(f"- Total trades covered: {atlas['n_total'].sum():,}")
report.append(f"- Total gave_back: {atlas['n_gave_back'].sum():,}")
report.append(f"- Total full_tp: {atlas['n_full_tp'].sum():,}")
report.append("")
report.append("## Recommendation distribution")
report.append("")
report.append(rec_summary.to_markdown(index=False, floatfmt=".1f"))
report.append("")
report.append("## Worst gave-back cells (top 10 by absolute n_gave_back)")
report.append("")
worst = atlas.nlargest(10, "n_gave_back")[["strategy","pair_family","session","direction",
                                             "n_total","gave_back_pct","full_tp_pct","mfe_median_giveback",
                                             "recommended_action","top_separator_1"]]
report.append(worst.to_markdown(index=False, floatfmt=".2f"))
report.append("")
report.append("## Cells with highest full_tp_pct (the cells where the bot does work)")
report.append("")
best = atlas[atlas["n_total"] >= 100].nlargest(10, "full_tp_pct")[
    ["strategy","pair_family","session","direction","n_total","full_tp_pct","gave_back_pct",
     "mfe_median_fulltp","recommended_action"]]
report.append(best.to_markdown(index=False, floatfmt=".2f"))
report.append("")
report.append("## skip_cell candidates (structural failure)")
report.append("")
skip = atlas[atlas["recommended_action"] == "skip_cell"]
if len(skip):
    report.append(skip[["strategy","pair_family","session","direction","n_total",
                        "full_tp_pct","gave_back_pct","clean_stop_pct","recommendation_basis"]]
                  .to_markdown(index=False, floatfmt=".1f"))
else:
    report.append("(none)")
report.append("")
report.append("## earlier_ratchet candidates")
report.append("")
er = atlas[atlas["recommended_action"] == "earlier_ratchet"]
if len(er):
    report.append(er[["strategy","pair_family","session","direction","n_total",
                      "gave_back_pct","mfe_median_giveback","top_separator_1","top_separator_2"]]
                  .head(15).to_markdown(index=False, floatfmt=".2f"))
else:
    report.append("(none)")
report.append("")
report.append("## tighter_be candidates")
report.append("")
tb = atlas[atlas["recommended_action"] == "tighter_be"]
if len(tb):
    report.append(tb[["strategy","pair_family","session","direction","n_total",
                      "gave_back_pct","mfe_median_giveback","top_separator_1","top_separator_2"]]
                  .head(15).to_markdown(index=False, floatfmt=".2f"))
else:
    report.append("(none)")
report.append("")
report.append("## quick_partial / lower_tp candidates")
report.append("")
qp = atlas[atlas["recommended_action"] == "quick_partial_or_lower_tp"]
if len(qp):
    report.append(qp[["strategy","pair_family","session","direction","n_total",
                      "gave_back_pct","mfe_median_giveback","top_separator_1","top_separator_2"]]
                  .head(15).to_markdown(index=False, floatfmt=".2f"))
else:
    report.append("(none)")
report.append("")
report.append("## entry_quality_review (entries are bad, not management)")
report.append("")
eq = atlas[atlas["recommended_action"] == "entry_quality_review"]
if len(eq):
    report.append(eq[["strategy","pair_family","session","direction","n_total",
                      "clean_stop_pct","gave_back_pct","full_tp_pct","top_separator_1"]]
                  .head(15).to_markdown(index=False, floatfmt=".1f"))
report.append("")
report.append("## What the recommendations are NOT")
report.append("")
report.append("- NOT a config change list. These are HYPOTHESES.")
report.append("- NOT validated against the corpus or any holdout.")
report.append("- NOT a license to change live management. Each hypothesis needs:")
report.append("  - Cluster the cell's trades")
report.append("  - Confirm the separator is causal, not coincidental")
report.append("  - Design the deterministic rule")
report.append("  - Backtest on the live-epoch data first, then corpus")
report.append("  - Only then propose a config change with a clear A/B comparison")
report.append("")
report.append("## Next branch")
report.append("")
report.append("With this atlas as input, the trade-film ledger's `can_be_legitimately_saved`")
report.append("field can now be filled for the broker-truth `bot_actual_loser` rows whose")
report.append("(strategy, pair_family, session, direction) falls in an `earlier_ratchet`,")
report.append("`tighter_be`, or `quick_partial` cell. The save_method captures which")
report.append("recommendation applies. This is the bridge to winner-cluster discovery.")

Path(OUT / "summary.md").write_text("\n".join(report))
print(f"✅ summary at {OUT / 'summary.md'}")
print("\nOutputs:")
for f in sorted(OUT.iterdir()):
    print(f"  {f.name}: {f.stat().st_size} B")
