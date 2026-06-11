"""How often does the CELL BOOK trade at a 0.55 p_win floor, and at what
expectation? Scores the OOS book rows (4 live pairs, >=2025-07-01, allowlist
hit) with the LIVE v0 serving model, sweeps floors, and crosses with cell-hit
depth. Corpus volumes are exhaustive-sim counts; live-rate estimates are
scaled to observed live volume at the current 0.45 floor."""
import json
import numpy as np, pandas as pd
import lightgbm as lgb
import pyarrow.parquet as pq

ROOT='/home/ubuntu/mr-scrooge-v3'
F14=['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
ALLOW={k:[tuple(c) for c in v] for k,v in
       json.load(open(f'{ROOT}/config/default.json'))['gates']['pip_eater']['cell_allowlist'].items()
       if not k.startswith('_')}

NEED=F14+['pair','strategy','direction','session','entry_time','net_ladder','alignv']
df=pq.read_table('/home/ubuntu/scored_7yr.parquet',columns=NEED).to_pandas(categories=F14+['pair','strategy','direction','session'])
df['entry_time']=pd.to_datetime(df['entry_time'],utc=True)
df=df[(df.pair.isin(['AUD_USD','EUR_USD','GBP_USD','USD_CAD']))&(df.entry_time>=pd.Timestamp('2025-07-01',tz='UTC'))]

hits=np.zeros(len(df),dtype=int)
for strat,cells in ALLOW.items():
    m=(df.strategy==strat).values
    if not m.any(): continue
    sub=df[m]; h=np.zeros(len(sub),dtype=int)
    for a,f,b,d in cells:
        h+=((sub.alignv==a)&(sub[f].astype(str)==b)&(sub.direction.astype(str)==d)).values
    hits[m]=h
df['nhits']=hits
book=df[df.nhits>0].copy()
days=(book.entry_time.max()-book.entry_time.min()).days or 1
print(f"OOS book rows: {len(book)} over {days}d")

meta=json.loads(open(f'{ROOT}/data/lab_training/v0/feature_meta.json').read())
order=meta['feature_order']; levels=meta['categorical_levels']
booster=lgb.Booster(model_file=f'{ROOT}/data/lab_training/v0/model.txt')
ren={'strategy':'strategy_id','direction':'direction_exec','session':'session_bucket'}
te=book.rename(columns=ren)
X=np.full((len(te),len(order)),-1.0)
for j,c in enumerate(order):
    lv={v:i for i,v in enumerate(levels.get(c,[]))}
    X[:,j]=te[c].astype(str).map(lv).fillna(-1).to_numpy()
book['pw']=booster.predict(X)
book['y']=(book.net_ladder>0).astype(int)

print(f"\np_win distribution within book: p10={book.pw.quantile(.1):.3f} p50={book.pw.quantile(.5):.3f} p90={book.pw.quantile(.9):.3f}")

base45=len(book[book.pw>=0.45])
LIVE_TPD_AT_45=3.0   # observed live book volume June 11 (first day, rough anchor)
print(f"\n{'floor':>5} {'n':>7} {'kept%':>6} {'WR%':>5} {'ev/trade':>8} {'tot_pips':>9} {'corpus tr/d':>11} {'~live tr/d':>10}")
for f in (0.0,0.45,0.50,0.55,0.60,0.65):
    k=book[book.pw>=f]
    if not len(k): print(f"{f:5.2f}       0"); continue
    est=LIVE_TPD_AT_45*len(k)/base45
    print(f"{f:5.2f} {len(k):7d} {len(k)/len(book)*100:6.1f} {k.y.mean()*100:5.1f} {k.net_ladder.mean():+8.2f} {k.net_ladder.sum():+9.0f} {len(k)/days:11.1f} {est:10.1f}")

print("\nband detail (what a 0.55 floor cuts):")
for lo,hi in [(0.45,0.50),(0.50,0.55),(0.55,0.60),(0.60,0.65),(0.65,1.0)]:
    k=book[(book.pw>=lo)&(book.pw<hi)]
    if not len(k): continue
    print(f"  [{lo:.2f},{hi:.2f}): n={len(k):6d} WR {k.y.mean()*100:5.1f}% ev {k.net_ladder.mean():+6.2f}p tot {k.net_ladder.sum():+8.0f}")

print("\nfloor x cell-hit depth (OOS ev/trade | n):")
print(f"{'floor':>5} {'1-hit ev':>9} {'1-hit n':>8} {'>=2 ev':>7} {'>=2 n':>7}")
for f in (0.45,0.50,0.55,0.60):
    k=book[book.pw>=f]
    s1=k[k.nhits==1]; s2=k[k.nhits>=2]
    print(f"{f:5.2f} {s1.net_ladder.mean():+9.2f} {len(s1):8d} {s2.net_ladder.mean():+7.2f} {len(s2):7d}")

print("\nred-day profile by floor (days with >=1 trade):")
book['day']=book.entry_time.dt.date
for f in (0.45,0.55):
    k=book[book.pw>=f]
    d=k.groupby('day').net_ladder.sum()
    print(f"  floor {f:.2f}: trading days {len(d)} | red days {(d<0).mean()*100:.1f}% | mean red {d[d<0].mean():+.1f}p | worst {d.min():+.1f}p")
