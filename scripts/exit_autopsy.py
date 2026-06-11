"""Exit autopsy v2 — pips from PRICES (per closing fill, unit-weighted), not P&L.
Counterfactual sims cleaned + half-spread penalty on sim exits."""
import json, urllib.request
from datetime import datetime, timedelta, timezone

env={}
for line in open('/home/ubuntu/mr-scrooge-v3/.env'):
    line=line.strip()
    if '=' in line and not line.startswith('#'): k,v=line.split('=',1); env[k]=v
API=env['OANDA_API_URL'].rstrip('/'); AC=env['OANDA_ACCOUNT_ID']
HDR={'Authorization':f"Bearer {env['OANDA_API_TOKEN']}"}
def get(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=HDR),timeout=30).read())

last=int(get(f"{API}/v3/accounts/{AC}/summary")['lastTransactionID'])
txns=[]; lo=5200
while lo<=last:
    hi=min(lo+899,last)
    txns+=get(f"{API}/v3/accounts/{AC}/transactions/idrange?from={lo}&to={hi}")['transactions']
    lo=hi+1

opens={}; fills={}
for t in txns:
    if t['type']!='ORDER_FILL': continue
    if t.get('tradeOpened'):
        tid=t['tradeOpened']['tradeID']; u=float(t['units'])
        opens[tid]=dict(sym=t['instrument'], sign=1 if u>0 else -1,
                        entry=float(t['price']), ot=t['time'][:19], units=abs(u))
    px=float(t['price'])
    for key in ('tradesClosed','tradesReduced'):
        arr=t.get(key) or []
        if isinstance(arr,dict): arr=[arr]
        for c in arr:
            tid=c.get('tradeID')
            if not tid: continue
            cu=abs(float(c.get('units',0)))
            fills.setdefault(tid,[]).append(dict(px=px, u=cu, ct=t['time'][:19], reason=t.get('reason','')))

trades=[]
for tid,o in opens.items():
    fl=fills.get(tid)
    if not fl or o['ot']<'2026-06-01': continue
    pip=0.01 if 'JPY' in o['sym'] else 0.0001
    tot_u=sum(f['u'] for f in fl)
    if tot_u<=0: continue
    pips=sum(((f['px']-o['entry'])*o['sign']/pip)*f['u'] for f in fl)/tot_u
    trades.append(dict(tid=tid, **o, pips=round(pips,1), ct=max(f['ct'] for f in fl),
                       reason=fl[-1]['reason'], nfills=len(fl)))
print(f"trades since June 1: {len(trades)} | actual avg {sum(t['pips'] for t in trades)/len(trades):+.2f}p total {sum(t['pips'] for t in trades):+.0f}p")

cache={}
def candles(sym, frm):
    k=(sym,frm[:13])
    if k not in cache:
        try: cache[k]=get(f"{API}/v3/instruments/{sym}/candles?granularity=M5&from={frm}Z&count=600&price=M")['candles']
        except Exception: cache[k]=None
    return cache[k]

SPREAD_PEN=0.75  # half-spread penalty per sim exit (mid-based sim honesty)
def sim_policy(path, sl, be_at, be_to, tp1):
    """Phase-1 ladder approximation: tp1 50% out -> SL +6 lock; +20 25%; +30 25%.
       Optional BE move at be_at -> be_to before tp1. Returns pips (spread-penalized)."""
    cur_sl=-sl; acc=0.0; rem=1.0; tp1_done=tp2_done=False
    for fav,adv in path:
        if not tp1_done:
            if be_at and fav>=be_at and cur_sl<be_to: cur_sl=be_to
            if adv>=abs(cur_sl) and cur_sl<0: return cur_sl-SPREAD_PEN
            if cur_sl>=0 and fav<=cur_sl: return cur_sl-SPREAD_PEN
            if fav>=tp1:
                tp1_done=True; acc+=0.5*tp1; rem=0.5; cur_sl=6
                continue
        else:
            if fav<=cur_sl: return acc+rem*cur_sl-SPREAD_PEN
            if not tp2_done and fav>=20:
                tp2_done=True; acc+=0.25*20; rem=0.25
            if tp2_done and fav>=30:
                return acc+0.25*30-SPREAD_PEN
    return acc+rem*path[-1][0]-SPREAD_PEN if path else 0.0

def sim_trail(path):
    cur_sl=-12; acc=0.0; rem=1.0; tp1_done=False; peak=0.0
    for fav,adv in path:
        if not tp1_done:
            if adv>=12: return -12-SPREAD_PEN
            if fav>=12: tp1_done=True; acc+=6.0; rem=0.5; peak=fav; continue
        else:
            peak=max(peak,fav)
            stop=max(6.0, peak-8.0)
            if fav<=stop: return acc+rem*stop-SPREAD_PEN
    return acc+rem*path[-1][0]-SPREAD_PEN if path else 0.0

res=[]
for tr in trades:
    pip=0.01 if 'JPY' in tr['sym'] else 0.0001
    cs=candles(tr['sym'], tr['ot'])
    if not cs: continue
    ct=datetime.fromisoformat(tr['ct']+'+00:00')
    e=tr['entry']; sign=tr['sign']
    path=[]; mfe=mae=0.0
    for k in cs:
        kt=datetime.fromisoformat(k['time'].replace('.000000000','').replace('Z','+00:00'))
        if kt>ct+timedelta(minutes=5): break
        hi,lo=float(k['mid']['h']),float(k['mid']['l'])
        fav=((hi-e) if sign>0 else (e-lo))/pip; adv=((e-lo) if sign>0 else (hi-e))/pip
        path.append((fav,adv)); mfe=max(mfe,fav); mae=max(mae,adv)
    if not path: continue
    res.append(dict(tid=tr['tid'], sym=tr['sym'], pips=tr['pips'], mfe=round(mfe,1), mae=round(mae,1),
        reason=tr['reason'],
        base=round(sim_policy(path,12,None,0,12),1),
        be8=round(sim_policy(path,12,8,0,12),1),
        be10=round(sim_policy(path,12,10,2,12),1),
        tp1_10=round(sim_policy(path,12,None,0,10),1),
        sl15=round(sim_policy(path,15,None,0,12),1),
        be6=round(sim_policy(path,12,6,0,12),1),
        be8sl15=round(sim_policy(path,15,8,0,12),1),
        be8tp10=round(sim_policy(path,12,8,0,10),1),
        trail=round(sim_trail(path),1)))

import statistics as st
n=len(res)
print(f"paths analyzed: {n}")
print(f"\nSANITY: actual avg {st.mean([r['pips'] for r in res]):+.2f}p | sim-of-current-policy avg {st.mean([r['base'] for r in res]):+.2f}p  <- these should be CLOSE")
losers=[r for r in res if r['pips']<-2]; winners=[r for r in res if r['pips']>2]
print(f"\nFAKE-OUTS ({len(losers)} losers): MFE>=4: {sum(r['mfe']>=4 for r in losers)} ({100*sum(r['mfe']>=4 for r in losers)//len(losers)}%) | >=6: {sum(r['mfe']>=6 for r in losers)} | >=8: {sum(r['mfe']>=8 for r in losers)} | >=10: {sum(r['mfe']>=10 for r in losers)}")
cap=[r['pips']/r['mfe'] for r in winners if r['mfe']>0]
print(f"CAPTURE ({len(winners)} winners): median {st.median(cap)*100:.0f}% of MFE | left on table median {st.median([r['mfe']-r['pips'] for r in winners]):.1f}p")
print(f"\nPOLICY TOTALS on identical paths (sim vs sim — fair):")
for k in ('base','be6','be8','be10','tp1_10','sl15','be8sl15','be8tp10','trail'):
    print(f"  {k:8} total={sum(r[k] for r in res):+8.1f}p  avg={st.mean([r[k] for r in res]):+5.2f}p")
json.dump(res, open('/home/ubuntu/mr-scrooge-v3/data/lab_training/exit_autopsy_latest.json','w'))
print("saved v2")
