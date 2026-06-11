"""Combined focused-five book: alpha_pullback, alpha_breakout, MR5_short, TF2, AEF.
OOS 2025-07..2026-05, gate-proxy trades, slot-constrained sims."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
FIVE = ['alpha_pullback_v2','alpha_breakout_retest_v2','MR5_williams_extreme_short',
        'TF2_pullback_EMA20_short','alpha_extended_fade_v2']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
df = df[df.pair.isin(['AUD_USD','EUR_USD','GBP_USD','USD_CAD']) & df.strategy.isin(FIVE)]

pb = pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/playbook_ev_pairaware.csv')
amp_of = pb.groupby('strategy')['amp_factor'].agg(lambda s: s.mode().iat[0]).to_dict()
floor_of = pb.groupby('strategy')['floor'].agg(lambda s: s.mode().iat[0]).to_dict()
cell = {(r['pair'],r['strategy'],r['direction'],int(r['align']),str(r['bucket'])): r['ev_pips'] for _,r in pb.iterrows()}
def takes(r):
    amp = amp_of.get(r.strategy)
    if amp is None or int(r.alignv) < floor_of.get(r.strategy, 2): return False
    ev = cell.get((str(r.pair), r.strategy, str(r.direction), int(r.alignv), str(getattr(r, amp))))
    return ev is not None and ev >= 1.25
df['ok'] = [takes(r) for r in df.itertuples()]
g = df[df['ok']].sort_values('entry_time')
oos = g[g.entry_time >= pd.Timestamp('2025-07-01', tz='UTC')].copy()
days = (oos.entry_time.max()-oos.entry_time.min()).days

# state-dedup within the book: same (pair, time, direction) = ONE idea; keep best-avg strategy's row
prio = {s:i for i,s in enumerate(FIVE)}
oos['prio'] = oos.strategy.map(prio)
ded = oos.sort_values(['entry_time','prio']).drop_duplicates(['pair','entry_time','direction'], keep='first')
print(f"combined raw signals: {len(oos)} ({len(oos)/days:.1f}/d) | after state-dedup: {len(ded)} ({len(ded)/days:.1f}/d)")
print(f"deduped book: WR={(ded.net_ladder>0).mean()*100:.1f}% avg={ded.net_ladder.mean():+.2f}p total={ded.net_ladder.sum():+,.0f}p")
yr = g.sort_values(['entry_time']).drop_duplicates(['pair','entry_time','direction'], keep='first')
yt = yr.groupby(yr.entry_time.dt.year).net_ladder.agg(['size','mean']).round(2)
print("yearly (deduped, 8yr): " + "  ".join(f"{y}:{m:+.2f}" for y,m in yt['mean'].items()))

def sim(trades, label, risk_frac, slots=1, hold_h=2, eq0=29000.0, sl=12.0):
    eq=eq0; peak=eq; mdd=0; busy=[]; n=0
    for r in trades.itertuples():
        busy=[b for b in busy if b > r.entry_time]
        if len(busy) >= slots: continue
        busy.append(r.entry_time + pd.Timedelta(hours=hold_h))
        pipv = 0.0001 if str(r.pair)!='USD_CAD' else 0.0001/1.39
        units = (eq*risk_frac)/(sl*pipv)/max(slots,1)  # split risk across slots? no: per-trade risk
        units = (eq*risk_frac)/(sl*pipv)
        eq += r.net_ladder*pipv*units; n+=1
        peak=max(peak,eq); mdd=max(mdd,(peak-eq)/peak)
    print(f"{label:42} trades={n:4d} ({n/days:4.1f}/d) end=${eq:>10,.0f} ({(eq/eq0-1)*100:+,.0f}%) maxDD={mdd*100:.1f}%")

print(f"\n=== 11-month OOS sims, state-deduped book, start $29k ===")
sim(ded, "5-book, 1 slot, 1% risk", 0.01, 1)
sim(ded, "5-book, 2 slots, 1% risk", 0.01, 2)
sim(ded, "5-book, 4 slots, 1% risk", 0.01, 4)
sim(ded, "5-book, 1 slot, 2% risk", 0.02, 1)
sim(ded, "5-book, 2 slots, 2% risk", 0.02, 2)
# stop streak on deduped book
ll=(ded.net_ladder<=-9.5).astype(int).values
streak=mx=0
for v in ll: streak=streak+1 if v else 0; mx=max(mx,streak)
print(f"\ndeduped book full-stop rate: {ll.mean()*100:.0f}% | worst streak: {mx}")
