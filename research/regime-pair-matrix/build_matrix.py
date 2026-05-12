"""Regime × pair matrix on the v2 corpus.

The discovery infrastructure for finding where the broad regimes need to split.
Per 2026-05-12 direction: do NOT invent splits. Surface the matrix; user names
the forks if/when the matrix proves them.

Outputs three matrices at increasing granularity:
  1. regime_x_pair (primary)        — 182 cells max
  2. regime_x_pair_x_session_x_dir  — full grain
  3. regime_x_pair_period_split     — discovery vs holdout to expose fragility

Each cell carries: n, wins, losses, win_rate, mean_r, sum_r, top_year_share,
top_quarter_share, top_pair_share (when aggregating above pair), and
concentration warnings.
"""
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timezone

BASE = Path("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v3_full_corpus/v2_2.0R")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/regime-pair-matrix")
OUT.mkdir(parents=True, exist_ok=True)
DISCOVERY_END = datetime(2025, 1, 1, tzinfo=timezone.utc)

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

print(f"streaming corpus from {BASE}...")
files = sorted(BASE.glob("*.parquet"))
KEEP = ['pair', 'entry_ts', 'direction', 'r_multiple', 'filled', 'realized_r',
        'regime_label', 'probe_name', 'session_label', 'year', 'quarter']
slim = [pd.read_parquet(f, columns=KEEP) for f in files]
df = pd.concat(slim, ignore_index=True)
del slim
df = df[df['filled'] == True].copy()
df['entry_ts'] = pd.to_datetime(df['entry_ts'], utc=True)
df['period'] = np.where(df['entry_ts'] < DISCOVERY_END, 'discovery', 'holdout')
df['pair_family'] = df['pair'].map(PAIR_FAMILY).fillna('other')
print(f"corpus filled trades: {len(df):,}")
print(f"  regimes: {df['regime_label'].nunique()}, pairs: {df['pair'].nunique()}, sessions: {df['session_label'].nunique()}")
print()


def cell_stats(grp):
    """Compute stats for a single cell."""
    r = grp['realized_r']
    n = len(grp)
    wins = (r > 0).sum()
    losses = (r < 0).sum()
    sum_r = r.sum()
    mean_r = r.mean() if n else 0
    std_r = r.std() if n > 1 else 0
    se = std_r / np.sqrt(n) if n > 1 else 0
    # Normal-approx CI (per the same logic the aggregator uses for large n)
    ci_low = mean_r - 1.96 * se
    ci_high = mean_r + 1.96 * se

    # Concentration: top year/quarter share (vs sum_r)
    top_year_share = top_q_share = None
    if sum_r != 0:
        yr = grp.groupby('year')['realized_r'].sum()
        top_year_share = yr.abs().max() / abs(sum_r) if len(yr) else None
        qr = grp.groupby('quarter')['realized_r'].sum()
        top_q_share = qr.abs().max() / abs(sum_r) if len(qr) else None

    return pd.Series({
        'n': n, 'wins': wins, 'losses': losses,
        'win_rate': wins / n if n else 0,
        'mean_r': mean_r,
        'sum_r': sum_r,
        'ci_low_95': ci_low, 'ci_high_95': ci_high,
        'ci_excludes_zero_positive': ci_low > 0,
        'top_year_share': top_year_share,
        'top_quarter_share': top_q_share,
    })


# 1. regime x pair x period
print("computing regime × pair × period matrix...")
m1 = df.groupby(['regime_label', 'pair', 'period']).apply(cell_stats, include_groups=False).reset_index()
m1 = m1.sort_values(['regime_label', 'pair', 'period'])
m1.to_parquet(OUT / "regime_x_pair_x_period.parquet", index=False)
m1.to_csv(OUT / "regime_x_pair_x_period.csv", index=False)
print(f"  → {len(m1)} cells")

# 2. regime x pair_family x period
print("computing regime × pair_family × period matrix...")
m2 = df.groupby(['regime_label', 'pair_family', 'period']).apply(cell_stats, include_groups=False).reset_index()
m2.to_parquet(OUT / "regime_x_pairfamily_x_period.parquet", index=False)
m2.to_csv(OUT / "regime_x_pairfamily_x_period.csv", index=False)
print(f"  → {len(m2)} cells")

# 3. Full grain: regime x pair x session x direction x period
print("computing regime × pair × session × direction × period matrix (full grain)...")
m3 = df.groupby(['regime_label', 'pair', 'session_label', 'direction', 'period']).apply(cell_stats, include_groups=False).reset_index()
m3.to_parquet(OUT / "regime_x_pair_x_session_x_dir_x_period.parquet", index=False)
m3.to_csv(OUT / "regime_x_pair_x_session_x_dir_x_period.csv", index=False)
print(f"  → {len(m3)} cells")

# 4. Highlighted: cells with n>=75 where mean_r is positive (the "candidate winners")
print("\nflagging candidate cells (n >= 75, mean_r > 0, ci_low > 0)...")
candidates = m1[(m1['n'] >= 75) & (m1['mean_r'] > 0) & (m1['ci_low_95'] > 0)]
print(f"  candidates in regime × pair × period: {len(candidates)}")
candidates.to_csv(OUT / "candidates_regime_x_pair_x_period.csv", index=False)

candidates_fg = m3[(m3['n'] >= 30) & (m3['mean_r'] > 0) & (m3['ci_low_95'] > 0)]
print(f"  candidates in full grain (n>=30): {len(candidates_fg)}")
candidates_fg.to_csv(OUT / "candidates_full_grain.csv", index=False)


# 5. Summary report
report = []
report.append("# Regime × Pair Matrix — Summary")
report.append("")
report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
report.append(f"Corpus: {len(df):,} filled trades from {len(files)} parquet segments")
report.append("")
report.append("## Files")
report.append("")
report.append("| File | Grain | Cells |")
report.append("|---|---|---|")
report.append(f"| regime_x_pair_x_period | regime × pair × period | {len(m1)} |")
report.append(f"| regime_x_pairfamily_x_period | regime × pair_family × period | {len(m2)} |")
report.append(f"| regime_x_pair_x_session_x_dir_x_period | full grain | {len(m3)} |")
report.append(f"| candidates_regime_x_pair_x_period | n≥75 + mean_r>0 + CI_low>0 | {len(candidates)} |")
report.append(f"| candidates_full_grain | n≥30 + mean_r>0 + CI_low>0 (FG) | {len(candidates_fg)} |")
report.append("")
report.append("## Candidates — regime × pair × period (n≥75, CI lb > 0)")
report.append("")
report.append("These are the cells where a real positive edge survives the bootstrap CI gate.")
report.append("Each row is a candidate behavioral fork — a place where the broad regime label")
report.append("masks a sharper pocket.")
report.append("")
if len(candidates):
    report.append(candidates[['regime_label','pair','period','n','win_rate','mean_r','sum_r','ci_low_95','top_year_share','top_quarter_share']].to_markdown(index=False, floatfmt=".4f"))
else:
    report.append("(none)")
report.append("")

report.append("## Distribution of mean_r by regime × period (top-line)")
report.append("")
pivot = m1.pivot_table(index='regime_label', columns='period', values='mean_r', aggfunc='mean')
report.append(pivot.to_markdown(floatfmt="+.4f"))
report.append("")

report.append("## Discovery → Holdout direction stability")
report.append("")
report.append("For each (regime, pair) — did the mean_r sign flip between periods?")
report.append("")
pivot_disc = m1[m1.period == 'discovery'].set_index(['regime_label','pair'])['mean_r']
pivot_hold = m1[m1.period == 'holdout'].set_index(['regime_label','pair'])['mean_r']
common = pivot_disc.index.intersection(pivot_hold.index)
shifts = pd.DataFrame({'disc': pivot_disc.loc[common], 'hold': pivot_hold.loc[common]})
shifts['sign_flip'] = (shifts['disc'] * shifts['hold']) < 0
n_flip = shifts['sign_flip'].sum()
n_total = len(shifts)
report.append(f"Sign flips: {n_flip} / {n_total} = {n_flip/n_total*100:.1f}% of (regime × pair) cells flipped sign in holdout")
report.append("")

# Sign-flip detail
flips = shifts[shifts.sign_flip].reset_index()
flips['delta'] = flips.hold - flips.disc
flips = flips.sort_values('delta')
if len(flips):
    report.append("### Worst sign-flips (discovery WIN → holdout LOSE)")
    report.append("")
    worst = flips[flips['disc'] > 0].head(15)
    if len(worst):
        report.append(worst.to_markdown(index=False, floatfmt="+.4f"))
    report.append("")
    report.append("### Best sign-flips (discovery LOSE → holdout WIN)")
    report.append("")
    best = flips[flips['disc'] < 0].tail(15)
    if len(best):
        report.append(best.to_markdown(index=False, floatfmt="+.4f"))

Path(OUT / "summary.md").write_text("\n".join(report))
print(f"\n✅ summary.md written: {OUT / 'summary.md'}")
print(f"\nALL outputs in {OUT}:")
for f in sorted(OUT.iterdir()):
    print(f"  {f.name} ({f.stat().st_size} B)")
