"""Echo-tight x echo_box_fade_v2 autopsy: why did discovery PASS but holdout FAIL?

Decomposition by pair, quarter, year over both discovery (pre-2025) and holdout (2025+).
"""
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timezone

BASE = Path("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v3_full_corpus/v2_2.0R")
DISCOVERY_END = datetime(2025, 1, 1, tzinfo=timezone.utc)

files = sorted(BASE.glob("*.parquet"))
KEEP = ['pair', 'entry_ts', 'r_multiple', 'filled', 'realized_r', 'realized_pnl',
        'regime_label', 'probe_name', 'year', 'quarter']
print(f"streaming {len(files)} parquets...")
slim = [pd.read_parquet(f, columns=KEEP) for f in files]
df = pd.concat(slim, ignore_index=True)
del slim
df = df[df['filled'] == True]
df = df[(df['regime_label'] == 'Echo-tight') & (df['probe_name'] == 'echo_box_fade_v2')]
df['entry_ts'] = pd.to_datetime(df['entry_ts'], utc=True)
df['period'] = np.where(df['entry_ts'] < DISCOVERY_END, 'discovery', 'holdout')
print(f"Echo-tight x echo_box_fade_v2: n={len(df):,}")
print(f"  discovery n={len(df[df.period=='discovery']):,}")
print(f"  holdout   n={len(df[df.period=='holdout']):,}")
print()

# =============================
# 1. Per-pair by period
# =============================
print("=" * 80)
print("BY PAIR — sorted by holdout sum_r (worst→best)")
print("=" * 80)
print(f"{'pair':>10}  {'disc_n':>7} {'disc_sum_r':>11} {'disc_avg':>10}  ||  "
      f"{'hold_n':>6} {'hold_sum_r':>11} {'hold_avg':>10}  Δavg")
pairs_summary = []
for pair, sub in df.groupby('pair'):
    d = sub[sub.period == 'discovery']
    h = sub[sub.period == 'holdout']
    pairs_summary.append({
        'pair': pair,
        'disc_n': len(d), 'disc_sum_r': d.realized_r.sum(), 'disc_avg': d.realized_r.mean() if len(d) else 0,
        'hold_n': len(h), 'hold_sum_r': h.realized_r.sum(), 'hold_avg': h.realized_r.mean() if len(h) else 0,
    })
pairs_df = pd.DataFrame(pairs_summary).sort_values('hold_sum_r')
for _, r in pairs_df.iterrows():
    d_avg = r.disc_avg if pd.notna(r.disc_avg) else 0
    h_avg = r.hold_avg if pd.notna(r.hold_avg) else 0
    delta = h_avg - d_avg
    print(f"{r.pair:>10}  {r.disc_n:>7,} {r.disc_sum_r:>+11,.1f} {d_avg:>+10.4f}  ||  "
          f"{r.hold_n:>6,} {r.hold_sum_r:>+11,.1f} {h_avg:>+10.4f}  {delta:>+7.4f}")
print()
print(f"Total discovery sum_r: {pairs_df.disc_sum_r.sum():+,.1f}")
print(f"Total holdout sum_r:   {pairs_df.hold_sum_r.sum():+,.1f}")
print()

# =============================
# 2. Holdout concentration breakdown
# =============================
print("=" * 80)
print("HOLDOUT — pair concentration (top_pair_share = 136% means top pair > total net)")
print("=" * 80)
holdout = df[df.period == 'holdout']
holdout_total = holdout.realized_r.sum()
print(f"Holdout total sum_r: {holdout_total:+.1f}")
print()
print("Pair contribution to holdout total (sorted by sum_r desc):")
pair_h = holdout.groupby('pair').realized_r.agg(['sum', 'count']).sort_values('sum', ascending=False)
print(f"{'pair':>10} {'n':>7} {'sum_r':>10} {'share':>9} {'cum_share':>10}")
cum = 0
for pair, row in pair_h.iterrows():
    share = row['sum'] / holdout_total if holdout_total != 0 else 0
    cum += share
    print(f"{pair:>10} {int(row['count']):>7,} {row['sum']:>+10.1f} {share*100:>+8.1f}% {cum*100:>+9.1f}%")
print()

# =============================
# 3. Quarter contribution in holdout
# =============================
print("=" * 80)
print("HOLDOUT — quarter concentration (top_quarter_share = 218% means top Q > total net)")
print("=" * 80)
q_h = holdout.groupby('quarter').realized_r.agg(['sum', 'count']).sort_values('sum', ascending=False)
print(f"{'quarter':>10} {'n':>7} {'sum_r':>10} {'share':>9}")
for q, row in q_h.iterrows():
    share = row['sum'] / holdout_total if holdout_total != 0 else 0
    print(f"{q:>10} {int(row['count']):>7,} {row['sum']:>+10.1f} {share*100:>+8.1f}%")
print()

# =============================
# 4. Year contribution in discovery
# =============================
print("=" * 80)
print("DISCOVERY — year contribution (top_year was 2019 at 41.7%)")
print("=" * 80)
disc = df[df.period == 'discovery']
disc_total = disc.realized_r.sum()
print(f"Discovery total sum_r: {disc_total:+.1f}")
y_d = disc.groupby('year').realized_r.agg(['sum', 'count']).sort_values('sum', ascending=False)
for y, row in y_d.iterrows():
    share = row['sum'] / disc_total if disc_total != 0 else 0
    print(f"{int(y):>10} {int(row['count']):>7,} {row['sum']:>+10.1f} {share*100:>+8.1f}%")
print()

# =============================
# 5. THE KEY QUESTION: which holdout pairs/quarters are MAKING the edge vs DRAGGING it
# =============================
print("=" * 80)
print("HOLDOUT — winners vs draggers (pairs)")
print("=" * 80)
print(f"  winners (positive sum_r): {(pair_h['sum'] > 0).sum()} pairs, total = {pair_h[pair_h['sum']>0]['sum'].sum():+.1f}")
print(f"  draggers (negative):      {(pair_h['sum'] < 0).sum()} pairs, total = {pair_h[pair_h['sum']<0]['sum'].sum():+.1f}")
print(f"  break-even:               {(pair_h['sum'] == 0).sum()} pairs")
print(f"  net of cancel-outs:       {pair_h['sum'].sum():+.1f}")
print()
print("If you removed EUR_USD (the 136%-share winner), holdout sum would be:",
      f"{(holdout_total - pair_h.loc['EUR_USD','sum']):+.1f}R")
print()

# =============================
# 6. Per-pair discovery → holdout direction shift
# =============================
print("=" * 80)
print("DISCOVERY → HOLDOUT DIRECTION SHIFT (per pair)")
print("=" * 80)
print(f"{'pair':>10}  {'disc avg_r':>10}  {'hold avg_r':>10}  {'sign flip?':>11}")
flips_neg = []
flips_pos = []
no_flip = []
for _, r in pairs_df.iterrows():
    d_a = r.disc_avg if pd.notna(r.disc_avg) else 0
    h_a = r.hold_avg if pd.notna(r.hold_avg) else 0
    if d_a > 0 and h_a < 0:
        flips_neg.append(r.pair)
        flip = "WIN→LOSE"
    elif d_a < 0 and h_a > 0:
        flips_pos.append(r.pair)
        flip = "LOSE→WIN"
    else:
        no_flip.append(r.pair)
        flip = "-"
    print(f"{r.pair:>10}  {d_a:>+10.4f}  {h_a:>+10.4f}  {flip:>11}")
print()
print(f"Pairs that flipped WIN→LOSE in holdout: {len(flips_neg)} — {flips_neg}")
print(f"Pairs that flipped LOSE→WIN in holdout: {len(flips_pos)} — {flips_pos}")
print(f"Pairs that maintained direction:        {len(no_flip)} — {no_flip}")
