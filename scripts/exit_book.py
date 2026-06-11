"""EXIT BOOK builder — per-cell-side exit-policy optimization (overnight).
For each of the 157 live cell-sides: replay its corpus entries through 7yr M5
paths, sweep exit policies, select on train (<2024-07), validate OOS (>=2025-07).
A cell earns custom exits only with OOS lift >= +0.3p and n_te >= 75; else
inherits the global policy (ladder + BE@6). Output: exit_book.csv."""
import json, numpy as np, pandas as pd
import pyarrow.parquet as pq

LIVE=['AUD_USD','EUR_USD','GBP_USD','USD_CAD']
F14=['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']

aud=pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/cell_book_direction_audit.csv')
cells=aud[aud.status=='KEEP'][['strategy','align','factor','bucket','direction']].drop_duplicates()
print(f"cell-sides: {len(cells)}", flush=True)

df=pq.read_table('/home/ubuntu/scored_7yr.parquet',
  columns=F14+['pair','strategy','direction','entry_time','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time']=pd.to_datetime(df['entry_time'],utc=True)
df=df[df.pair.isin(LIVE)]

m5={}
for P in LIVE:
    t=pd.read_parquet(f'/home/ubuntu/m5cache/{P}_M5.parquet').sort_index()
    m5[P]=dict(ts=t.index.values.astype('datetime64[s]'),
               o=t['Open'].values.astype('float32'),
               h=t['High'].values.astype('float32'),
               l=t['Low'].values.astype('float32'))
    print(P, len(t), 'bars', flush=True)

H=288  # 24h of M5
def paths_for(entries, pair, sign):
    M=m5[pair]; pip=0.0001
    idx=np.searchsorted(M['ts'], entries.values.astype('datetime64[s]'))
    out=[]
    for i in idx:
        if i+2>=len(M['o']) : continue
        e=M['o'][i+1]  # enter next bar open
        hi=M['h'][i+1:i+1+H]; lo=M['l'][i+1:i+1+H]
        if sign>0: fav=(hi-e)/pip; adv=(e-lo)/pip
        else: fav=(e-lo)/pip; adv=(hi-e)/pip
        out.append((fav,adv))
    return out

PEN=0.75
def sim(fav,adv,be,ts,tp3):
    cur=-12.0; acc=0.0; rem=1.0; tp1=False; tp2=False; mfe=0.0
    n=len(fav)
    for i in range(n):
        f=fav[i]; a=adv[i]; mfe=f if f>mfe else mfe
        if not tp1:
            if ts and i>=ts//5 and f<0 and mfe<3: return f-PEN
            if be and mfe>=be and cur<0.5: cur=0.5
            if cur<0 and a>=-cur: return cur-PEN
            if cur>=0 and f<=cur: return cur-PEN
            if f>=12: tp1=True; acc=6.0; rem=0.5; cur=6.0
        else:
            if f<=cur: return acc+rem*cur-PEN
            if not tp2 and f>=20: tp2=True; acc+=5.0; rem=0.25
            if tp2 and f>=tp3: return acc+0.25*tp3-PEN
    return acc+rem*fav[-1]-PEN if n else 0.0

POLS=[(be,ts,tp3) for be in (0,6,8) for ts in (0,90) for tp3 in (30,60)]
GLOBAL=(6,0,30)
TR_END=np.datetime64('2024-07-01'); TE_START=np.datetime64('2025-07-01')

rows=[]
for ci,(strat,al,fac,buc,d) in enumerate(cells.itertuples(index=False)):
    sub=df[(df.strategy==strat)&(df.alignv==al)&(df[fac]==buc)&(df.direction==d)]
    if len(sub)<200: continue
    res={}
    for era,lo_,hi_ in (('tr',None,TR_END),('te',TE_START,None)):
        e=sub
        if lo_ is not None: e=e[e.entry_time.values.astype('datetime64[s]')>=lo_]
        if hi_ is not None: e=e[e.entry_time.values.astype('datetime64[s]')<hi_]
        if len(e)>1200: e=e.sample(1200, random_state=7)
        allp=[]
        for pair in LIVE:
            ep=e[e.pair==pair]
            if len(ep): allp += paths_for(ep.entry_time, pair, 1 if d=='long' else -1)
        res[era]=allp
    if len(res.get('tr',[]))<150 or len(res.get('te',[]))<75: continue
    stats={}
    for pol in POLS:
        trv=np.mean([sim(f,a,*pol) for f,a in res['tr']])
        stats[pol]=trv
    best=max(stats, key=stats.get)
    te_best=np.mean([sim(f,a,*best) for f,a in res['te']])
    te_glob=np.mean([sim(f,a,*GLOBAL) for f,a in res['te']])
    lift=te_best-te_glob
    rows.append(dict(strategy=strat, align=al, factor=fac, bucket=buc, direction=d,
        n_tr=len(res['tr']), n_te=len(res['te']),
        be=best[0], timestop=best[1], tp3=best[2],
        tr_best=round(stats[best],2), te_best=round(te_best,2), te_global=round(te_glob,2),
        oos_lift=round(lift,2),
        custom=bool(lift>=0.3 and best!=GLOBAL)))
    if ci%20==0: print(f"[{ci}/{len(cells)}] done", flush=True)

eb=pd.DataFrame(rows)
eb.to_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/exit_book_v1.csv', index=False)
cust=eb[eb.custom]
print(f"\ncells analyzed: {len(eb)} | custom exits earned: {len(cust)}", flush=True)
print(f"OOS lift from custom cells: {cust.oos_lift.mean():+.2f}p avg, total weighted {(cust.oos_lift*cust.n_te).sum():+.0f}", flush=True)
print("\ntop 15 by OOS lift:", flush=True)
print(cust.sort_values('oos_lift',ascending=False).head(15).to_string(index=False), flush=True)
print("\npolicy distribution among custom cells:", flush=True)
print(cust.groupby(['be','timestop','tp3']).size().to_string(), flush=True)
