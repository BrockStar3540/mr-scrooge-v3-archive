"""Top-3 strategies: rank all by gate-passing OOS performance, deep-dive the
top 3 (yearly stability, stop streaks, sims), plus combined top-3 book."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
df = df[df.pair.isin(['AUD_USD','EUR_USD','GBP_USD','USD_CAD'])]

pb = pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/playbook_ev_pairaware.csv')
amp_of = pb.groupby('strategy')['amp_factor'].agg(lambda s: s.mode().iat[0]).to_dict()
floor_of = pb.groupby('strategy')['floor'].agg(lambda s: s.mode().iat[0]).to_dict()
cell = {(r['pair'],r['strategy'],r['direction'],int(r['align']),str(r['bucket'])): r['ev_pips'] for _,r in pb.iterrows()}
def takes(r):
    amp = amp_of.get(r.strategy)
    if amp is None: return False
    if int(r.alignv) < floor_of.get(r.strategy, 2): return False
    ev = cell.get((str(r.pair), r.strategy, str(r.direction), int(r.alignv), str(getattr(r, amp))))
    return ev is not None and ev >= 1.25
df['ok'] = [takes(r) for r in df.itertuples()]
g = df[df['ok']].sort_values('entry_time')
oos = g[g.entry_time >= pd.Timestamp('2025-07-01', tz='UTC')]
days = (oos.entry_time.max()-oos.entry_time.min()).days

print("=== ALL strategies, gate-passing OOS (2025-07..2026-05) ===")
t = oos.groupby('strategy', observed=True).agg(n=('net_ladder','size'),
    wr=('net_ladder', lambda s:(s>0).mean()*100), avg=('net_ladder','mean'),
    tot=('net_ladder','sum'))
t['per_day'] = t.n/days
t = t[t.n>=150].sort_values('avg', ascending=False).round(2)
print(t.to_string())

top3 = list(t.head(3).index)
print(f"\nTOP 3 by OOS avg (n>=150): {top3}")
for s in top3:
    gs = g[g.strategy==s]; os_ = oos[oos.strategy==s]
    yr = gs.groupby(gs.entry_time.dt.year).net_ladder.agg(['size','mean']).round(2)
    pos_years = (yr['mean']>0).sum()
    ll = (os_.net_ladder<=-9.5).astype(int).values
    streak=mx=0
    for v in ll: streak = streak+1 if v else 0; mx=max(mx,streak)
    print(f"\n--- {s} ---")
    print(f"OOS: {len(os_)} trades ({len(os_)/days:.1f}/d) WR={(os_.net_ladder>0).mean()*100:.1f}% avg={os_.net_ladder.mean():+.2f}p | full-stop rate {ll.mean()*100:.0f}%, worst streak {mx}")
    print(f"yearly avg 8yr: " + "  ".join(f"{y}:{m:+.2f}" for y,m in yr['mean'].items()) + f"  (positive {pos_years}/{len(yr)} years)")

def sim(trades, label, risk_frac, hold_h=2, eq0=29000.0, sl=12.0):
    eq=eq0; peak=eq; mdd=0; busy=None; n=0
    for r in trades.itertuples():
        if busy is not None and r.entry_time < busy: continue
        busy = r.entry_time + pd.Timedelta(hours=hold_h)
        pipv = 0.0001 if str(r.pair)!='USD_CAD' else 0.0001/1.39
        units = eq*risk_frac/(sl*pipv)
        eq += r.net_ladder*pipv*units; n+=1
        peak=max(peak,eq); mdd=max(mdd,(peak-eq)/peak)
    print(f"{label:46} trades={n:4d} end=${eq:>9,.0f} ({(eq/eq0-1)*100:+,.1f}%) maxDD={mdd*100:.1f}%")

print(f"\n=== 11-month OOS sims (1 slot, 2h hold, start $29k) ===")
for s in top3:
    sim(oos[oos.strategy==s], f"{s} only, 1% risk", 0.01)
sim(oos[oos.strategy.isin(top3)], "COMBINED top-3, 1 slot, 1% risk", 0.01)
sim(oos[oos.strategy.isin(top3)], "COMBINED top-3, 1 slot, 2% risk", 0.02)
