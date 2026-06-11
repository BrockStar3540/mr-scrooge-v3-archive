"""What if: alpha_extended_fade_v2 ONLY, single slot, 80% margin sizing.
OOS era (2025-07..2026-05), gate-proxy filtered, serialized 1-at-a-time."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
df = df[(df.strategy=='alpha_extended_fade_v2') & df.pair.isin(['AUD_USD','EUR_USD','GBP_USD','USD_CAD'])]

pb = pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/playbook_ev_pairaware.csv')
pb = pb[pb.strategy=='alpha_extended_fade_v2']
amp = pb.amp_factor.mode().iat[0]; floor = pb['floor'].mode().iat[0]
cell = {(r['pair'],r['direction'],int(r['align']),str(r['bucket'])): r['ev_pips'] for _,r in pb.iterrows()}
def takes(r):
    if int(r.alignv) < floor: return False
    ev = cell.get((str(r.pair), str(r.direction), int(r.alignv), str(getattr(r, amp))))
    return ev is not None and ev >= 1.25
df['ok'] = [takes(r) for r in df.itertuples()]
g = df[df['ok']].sort_values('entry_time')
oos = g[g.entry_time >= pd.Timestamp('2025-07-01', tz='UTC')]
days = (oos.entry_time.max()-oos.entry_time.min()).days
print(f"AEF gate-passing OOS: n={len(oos)} over {days}d = {len(oos)/days:.1f}/day | WR={(oos.net_ladder>0).mean()*100:.1f}% avg={oos.net_ladder.mean():+.2f}p")

def sim(trades, label, margin_frac=None, risk_frac=None, hold_h=2, eq0=29000.0, sl=12.0):
    eq = eq0; peak = eq; maxdd = 0; busy_until = None; taken=0; pnl_hist=[]
    for r in trades.itertuples():
        if busy_until is not None and r.entry_time < busy_until: continue
        busy_until = r.entry_time + pd.Timedelta(hours=hold_h)
        px = {'AUD_USD':0.70,'EUR_USD':1.155,'GBP_USD':1.34,'USD_CAD':1.0}[str(r.pair)]
        pipv_per_unit = 0.0001 if str(r.pair)!='USD_CAD' else 0.0001/1.39
        if margin_frac:
            units = eq*margin_frac/0.03/px
        else:
            units = eq*risk_frac/(sl*pipv_per_unit)
        pnl = r.net_ladder * pipv_per_unit * units
        eq += pnl; taken += 1; pnl_hist.append(pnl)
        peak = max(peak, eq); maxdd = max(maxdd, (peak-eq)/peak)
    ret = (eq/eq0-1)*100
    print(f"{label:38} trades={taken:4d} end=${eq:>10,.0f} ({ret:+.1f}%) maxDD={maxdd*100:.1f}% worst=${min(pnl_hist):,.0f} best=${max(pnl_hist):,.0f}")
    return eq

print(f"\n=== 11-month OOS simulations (start $29,000, 1 slot, ~2h hold) ===")
sim(oos, "AEF-only, 80% MARGIN", margin_frac=0.80)
sim(oos, "AEF-only, 1% risk (current sizing)", risk_frac=0.01)
sim(oos, "AEF-only, 2% risk", risk_frac=0.02)
sim(oos, "AEF-only, 3% risk", risk_frac=0.03)

# losing-streak / drawdown stress: worst stretch
ll = (oos.net_ladder<=-9.5).astype(int).values
streak=mx=0
for v in ll:
    streak = streak+1 if v else 0; mx=max(mx,streak)
print(f"\nfull-stop rate OOS: {ll.mean()*100:.0f}% | longest consecutive full-stop streak: {mx}")
print(f"at 80% margin each full stop ~= -5% equity -> streak of {mx} ~= -{(1-0.95**mx)*100:.0f}%")
# yearly stability whole corpus
g['yr']=g.entry_time.dt.year
print("\nyearly avg (all gate-passing AEF, 8yr):")
print(g.groupby('yr').net_ladder.agg(['size','mean']).round(2).to_string())
