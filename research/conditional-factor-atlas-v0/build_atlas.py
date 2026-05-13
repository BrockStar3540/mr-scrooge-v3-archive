"""Conditional Factor Atlas v0 — 47 factors × conditional cells.

Per 2026-05-12 direction: NOT a global score. NOT a points system. The atlas
maps which factors synchronize with winners, which synchronize with losers,
and which INVERT meaning across cells.

Scope honesty:
  Source: per_trade_factors_filled.csv.gz (90K filled trades)
  Time:   2026-03-15 → 2026-04-13 (30 days, all V1/V2 live era / post-2024)
  Regimes: V1/V2 STATE machine (CAUTION/NORMAL/RESTRICTED) — NOT V2 classifier
  Strategy: V3 branch (dbb_trend / direct / reversal)
  No discovery/holdout split: all data is in V2 corpus's holdout period

Grain:
  Primary (dense):  strategy × pair_family × direction          (~30 cells)
  Full (sparse):    strategy × regime × pair_family × session × direction
                                                                  (~360 cells)

Per cell × factor:
  - n_winners, n_losers, win_rate
  - winner_mean, loser_mean
  - effect_size (Cohen's d on means)
  - 95% CI on (winner_mean - loser_mean)
  - sign: winner_positive | loser_positive | neutral
  - n_warning: winner_n < 30 OR loser_n < 30 (flag, not exclude)

Inversion analysis:
  For each (strategy, factor) — does the sign vary across cells?
  Stability score = fraction of non-neutral cells that agree on sign.
  Inversion factors are flagged.

Output:
  /home/ubuntu/mr-scrooge-v3/research/conditional-factor-atlas-v0/
    atlas_primary.parquet         — dense grain table
    atlas_full.parquet            — sparse full-grain table
    inversion_report.csv          — per (strategy, factor) stability
    headline_inversions.csv       — factors that flip sign across cells
    summary.md
"""
from pathlib import Path
import pandas as pd
import numpy as np
import json
from datetime import datetime, timezone

SRC = "/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/factor_audit/per_trade_factors_filled.csv.gz"
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/conditional-factor-atlas-v0")
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


def session_of(hour_utc):
    """Forex session by UTC hour. Asia 22-08, London 07-15, NY 12-21, overlap = London+NY."""
    if pd.isna(hour_utc):
        return "unknown"
    h = int(hour_utc) % 24
    if 22 <= h or h < 6:
        return "asia"
    elif 6 <= h < 12:
        return "london"
    elif 12 <= h < 16:
        return "overlap"
    else:
        return "ny_pm"


# Load
print(f"loading {SRC} ...")
df = pd.read_csv(SRC)
df["ts"] = pd.to_datetime(df["ts"], utc=True)
df["pair_family"] = df["symbol"].map(PAIR_FAMILY).fillna("other")
df["session"] = df["hour_utc"].apply(session_of)
df["winner"] = df["realized_r"] > 0
print(f"  rows: {len(df):,}")
print(f"  winners: {df.winner.sum():,} ({df.winner.mean()*100:.1f}%)")

# Identify factor columns — numeric, not identity/setup/outcome/ML
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
DERIVED = {"pair_family", "session", "winner"}
EXCLUDE = IDENTITY | SETUP | OUTCOME | ML | DERIVED

factor_cols = [c for c in df.columns
               if c not in EXCLUDE and df[c].dtype in (np.float64, np.int64)]
print(f"  factor columns: {len(factor_cols)}")
print(f"  factors: {factor_cols}")
print()


def cell_factor_stats(grp, factors):
    """Compute per-factor stats for a single cell."""
    winners = grp[grp.winner]
    losers = grp[~grp.winner]
    n_w, n_l = len(winners), len(losers)
    rows = []
    for f in factors:
        wv = winners[f].dropna()
        lv = losers[f].dropna()
        nw, nl = len(wv), len(lv)
        if nw < 5 or nl < 5:
            continue
        mw, ml_ = wv.mean(), lv.mean()
        sw, sl = wv.std(), lv.std()
        # Pooled std for Cohen's d
        pool = np.sqrt(((nw - 1) * sw**2 + (nl - 1) * sl**2) / (nw + nl - 2)) if (nw + nl > 2) else 0
        d = (mw - ml_) / pool if pool > 0 else 0
        # 95% CI on mean diff (Welch)
        se = np.sqrt(sw**2/nw + sl**2/nl) if (nw > 1 and nl > 1) else 0
        ci_low = (mw - ml_) - 1.96 * se
        ci_high = (mw - ml_) + 1.96 * se
        # Sign
        if ci_low > 0:
            sign = "winner_positive"
        elif ci_high < 0:
            sign = "loser_positive"
        else:
            sign = "neutral"
        rows.append({
            "factor": f,
            "n_winners": nw, "n_losers": nl,
            "winner_mean": mw, "loser_mean": ml_,
            "mean_diff": mw - ml_,
            "cohens_d": d,
            "ci_low_95": ci_low, "ci_high_95": ci_high,
            "sign": sign,
            "n_warning": (nw < 30) or (nl < 30),
        })
    return pd.DataFrame(rows)


# === Primary grain: strategy × pair_family × direction ===
print("building primary atlas (strategy × pair_family × direction × factor)...")
primary = []
for keys, grp in df.groupby(["strategy", "pair_family", "direction"]):
    s, pf, dr = keys
    n_total = len(grp)
    n_w = grp.winner.sum()
    cell_stats = cell_factor_stats(grp, factor_cols)
    cell_stats["strategy"] = s
    cell_stats["pair_family"] = pf
    cell_stats["direction"] = dr
    cell_stats["cell_n"] = n_total
    cell_stats["cell_wins"] = n_w
    cell_stats["cell_win_rate"] = n_w / n_total if n_total else 0
    primary.append(cell_stats)
primary_df = pd.concat(primary, ignore_index=True)
print(f"  primary rows: {len(primary_df):,}")
primary_df.to_parquet(OUT / "atlas_primary.parquet", index=False)
primary_df.to_csv(OUT / "atlas_primary.csv", index=False)

# === Full grain: strategy × regime × pair_family × session × direction ===
print("building full-grain atlas (× regime × session)...")
full = []
for keys, grp in df.groupby(["strategy", "regime", "pair_family", "session", "direction"]):
    s, rg, pf, ses, dr = keys
    if len(grp) < 20:
        continue
    cell_stats = cell_factor_stats(grp, factor_cols)
    if len(cell_stats) == 0:
        continue
    cell_stats["strategy"] = s
    cell_stats["regime"] = rg
    cell_stats["pair_family"] = pf
    cell_stats["session"] = ses
    cell_stats["direction"] = dr
    cell_stats["cell_n"] = len(grp)
    cell_stats["cell_wins"] = grp.winner.sum()
    cell_stats["cell_win_rate"] = grp.winner.mean()
    full.append(cell_stats)
full_df = pd.concat(full, ignore_index=True)
print(f"  full-grain rows: {len(full_df):,}")
full_df.to_parquet(OUT / "atlas_full.parquet", index=False)
full_df.to_csv(OUT / "atlas_full.csv", index=False)


# === Inversion analysis: per (strategy, factor), how does sign vary? ===
print("\nbuilding inversion analysis...")
inv_rows = []
for (s, f), grp in primary_df.groupby(["strategy", "factor"]):
    non_neutral = grp[grp.sign != "neutral"]
    n_cells = len(grp)
    n_nn = len(non_neutral)
    if n_nn == 0:
        sign_consensus = "neutral_only"
        stability = None
    else:
        winner_pos = (non_neutral.sign == "winner_positive").sum()
        loser_pos = (non_neutral.sign == "loser_positive").sum()
        if winner_pos == n_nn:
            sign_consensus = "winner_positive"
            stability = 1.0
        elif loser_pos == n_nn:
            sign_consensus = "loser_positive"
            stability = 1.0
        else:
            sign_consensus = "INVERTED"
            stability = max(winner_pos, loser_pos) / n_nn
    inv_rows.append({
        "strategy": s,
        "factor": f,
        "n_cells_total": n_cells,
        "n_cells_non_neutral": n_nn,
        "n_winner_positive": (grp.sign == "winner_positive").sum(),
        "n_loser_positive": (grp.sign == "loser_positive").sum(),
        "n_neutral": (grp.sign == "neutral").sum(),
        "consensus": sign_consensus,
        "stability_score": stability,
    })
inv_df = pd.DataFrame(inv_rows).sort_values(["strategy", "consensus", "stability_score"])
inv_df.to_csv(OUT / "inversion_report.csv", index=False)
print(f"  inversion rows: {len(inv_df):,}")

# Headlines: factors that INVERT across cells
inverted = inv_df[inv_df.consensus == "INVERTED"].sort_values("stability_score")
inverted.to_csv(OUT / "headline_inversions.csv", index=False)
print(f"  headline inversion factors: {len(inverted):,}")

# === Summary md ===
report = []
report.append("# Conditional Factor Atlas v0")
report.append("")
report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
report.append("")
report.append("## Scope honesty")
report.append("")
report.append(f"- Source: `per_trade_factors_filled.csv.gz` — {len(df):,} filled trades")
report.append(f"- Time window: {df.ts.min().date()} → {df.ts.max().date()} (30 days, all post-2024)")
report.append(f"- Strategies: {sorted(df.strategy.unique())}")
report.append(f"- Regimes (V1/V2 state machine, NOT V2 classifier): {sorted(df.regime.unique())}")
report.append(f"- Pair families: {sorted(df.pair_family.unique())}")
report.append(f"- Factor columns: {len(factor_cols)}")
report.append("")
report.append("## Cells")
report.append("")
report.append(f"- Primary grain (strategy × pair_family × direction): {primary_df.groupby(['strategy','pair_family','direction']).ngroups} cells, {len(primary_df):,} (cell, factor) rows")
report.append(f"- Full grain (× regime × session): {full_df.groupby(['strategy','regime','pair_family','session','direction']).ngroups} cells, {len(full_df):,} (cell, factor) rows")
report.append("")
report.append("## Inversion headline")
report.append("")
report.append("Across primary grain cells (strategy × pair_family × direction), how each factor's sign behaves:")
report.append("")
report.append(inv_df.groupby(["strategy", "consensus"]).size().unstack(fill_value=0).to_markdown())
report.append("")
report.append("### Most-inverted factors (consensus = INVERTED, sorted by lowest stability)")
report.append("")
report.append("These factors switch meaning between cells. Same factor is winner-positive in some")
report.append("(strategy, pair_family, direction) combinations and loser-positive in others.")
report.append("**This is the structural evidence that the old global 47-factor system was unconditioned.**")
report.append("")
if len(inverted):
    report.append(inverted.head(25).to_markdown(index=False, floatfmt=".3f"))
report.append("")
report.append("### Most-stable winner-positive factors (consensus = winner_positive)")
report.append("")
report.append("These factors consistently mark winners across all cells where the signal is")
report.append("non-neutral. They're the candidates for 'always-on' winner indicators (within this")
report.append("30-day window — not yet validated across periods).")
report.append("")
wp = inv_df[inv_df.consensus == "winner_positive"].sort_values("n_cells_non_neutral", ascending=False)
if len(wp):
    report.append(wp.head(15).to_markdown(index=False, floatfmt=".3f"))
report.append("")
report.append("### Most-stable loser-positive factors")
report.append("")
report.append("Consistently mark losers. These are 'do NOT take' signals.")
report.append("")
lp = inv_df[inv_df.consensus == "loser_positive"].sort_values("n_cells_non_neutral", ascending=False)
if len(lp):
    report.append(lp.head(15).to_markdown(index=False, floatfmt=".3f"))
report.append("")
report.append("## How to use this atlas")
report.append("")
report.append("DO NOT collapse into a single score. The point of the atlas is that the same")
report.append("factor means different things in different cells.")
report.append("")
report.append("Workflow:")
report.append("1. Pick a candidate pocket from the regime × pair matrix (e.g. Echo-tight × USD_CHF,")
report.append("   Charlie × CAD_JPY × holdout).")
report.append("2. Look up the matching cell in `atlas_full.csv` (strategy × regime × pair_family ×")
report.append("   session × direction). Note: V2 regime labels are NOT in this v0; use V1/V2 state")
report.append("   regime as a proxy and cross-reference manually.")
report.append("3. Identify which factors are winner-positive vs loser-positive in THAT cell.")
report.append("4. Cross-check the inverted factors — same factor in a neighboring cell may say")
report.append("   the opposite.")
report.append("5. The winning factor signature in the cell is one candidate micro-strategy input.")
report.append("")
report.append("## What v0 cannot do")
report.append("")
report.append("- No discovery/holdout period split (data is 30 days, all in holdout era)")
report.append("- No V2 regime labels (corpus join recovered only 7.8%, abandoned)")
report.append("- No cross-period stability for individual factors (would need same data >12 months)")
report.append("- No micro-strategy promotion logic (out of scope by direction)")
report.append("")
report.append("Next iteration v1 should extend feature extraction to corpus (currently 11 features")
report.append("in `feature_snapshot`; need 47+). Then atlas can run on full V2 regime grain with")
report.append("real discovery/holdout split.")

Path(OUT / "summary.md").write_text("\n".join(report))
print(f"\n✅ summary.md: {OUT / 'summary.md'}")
print(f"\nOutputs in {OUT}:")
for f in sorted(OUT.iterdir()):
    print(f"  {f.name} ({f.stat().st_size} B)")
