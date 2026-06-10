"""Adversarial pass on miner v3 gen-1 winners: state-overlap dedup.
Winner children from different strategy NAMES may be the same underlying
trades (32.5% co-firing). Greedy weighted set-cover: keep highest-OOS-total
child, drop children sharing >30% of its (pair,time,dir) trades, repeat."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
gen1 = pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/miner_v3_gen1.csv')
W = gen1[(gen1.verdict=='WINNER') & (gen1.depth>0)].copy()
print(f"gen-1 winner children: {len(W)}, naive OOS total {W.tot_te.sum():+,.0f}p")

NEED = F14 + ['pair','strategy','direction','entry_time','net_ladder','alignv','era_dummy']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
df = df[(df.entry_time >= pd.Timestamp('2025-07-01', tz='UTC'))]  # OOS era only

def child_trades(row):
    a, pair, strat, d = row.base.split('|')
    sub = df[(df.alignv==int(a[1:])) & (df.pair==pair) & (df.strategy==strat) & (df.direction==d)]
    for cond in row.lineage.split('>'):
        if cond == '(root)': continue
        f, lvl = cond.split('=')
        sub = sub[sub[f]==lvl]
    return sub

W = W.sort_values('tot_te', ascending=False).reset_index(drop=True)
keysets = []
for _, r in W.iterrows():
    t = child_trades(r)
    keysets.append(set(zip(t.pair.astype(str), t.entry_time, t.direction.astype(str))))

kept, dropped = [], []
covered = set()
for i, r in W.iterrows():
    ks = keysets[i]
    if not ks: dropped.append((r, 'no trades')); continue
    ov = len(ks & covered) / len(ks)
    if ov > 0.30:
        dropped.append((r, f'{ov*100:.0f}% overlap')); continue
    kept.append((r, ov)); covered |= ks
print(f"\nDEDUPED winners: {len(kept)} kept / {len(W)-len(kept)} dropped as overlap-duplicates")
uq = df[[ (str(p),t,str(d)) in covered for p,t,d in zip(df.pair, df.entry_time, df.direction) ]]
# unique-state OOS pips: count each state once (mean across co-firing rows)
u = uq.groupby(['pair','entry_time','direction'], observed=True).net_ladder.mean()
print(f"HONEST unique-state OOS total: {u.sum():+,.0f}p across {len(u)} unique trades ({(u>0).mean()*100:.0f}% WR)")
print("\nKept (top 15):")
for r, ov in kept[:15]:
    print(f"  {r.base:55} {r.lineage:12} ev_te={r.ev_te:+.2f} n_te={r.n_te} tot={r.tot_te:+.0f}")
out = pd.DataFrame([dict(r._asdict() if hasattr(r,'_asdict') else r) for r,_ in kept])
out.to_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/miner_v3_gen1_winners_deduped.csv', index=False)
print("\nsaved -> miner_v3_gen1_winners_deduped.csv")
