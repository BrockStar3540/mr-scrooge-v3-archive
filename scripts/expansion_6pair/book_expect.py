"""What should a NORMAL run of the 157-side cell book look like? OOS-era
(>=2025-07-01) simulation of the live allowlist on the 4 live pairs:
per-trade stats, red-day frequency, losing-streak odds, and whether
multi-cell confirmation (>=2 matching sides) beats single-hit."""
import json
import pandas as pd, numpy as np
import pyarrow.parquet as pq

ROOT='/home/ubuntu/mr-scrooge-v3'
ALLOW={k:[tuple(c) for c in v] for k,v in
       json.load(open(f'{ROOT}/config/default.json'))['gates']['pip_eater']['cell_allowlist'].items()
       if not k.startswith('_')}

F14=['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
df=pq.read_table('/home/ubuntu/scored_7yr.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time']=pd.to_datetime(df['entry_time'],utc=True)
df=df[(df.pair.isin(['AUD_USD','EUR_USD','GBP_USD','USD_CAD']))
      &(df.entry_time>=pd.Timestamp('2025-07-01',tz='UTC'))]

# count matching cell-sides per row
hits=np.zeros(len(df),dtype=int)
for strat,cells in ALLOW.items():
    m=(df.strategy==strat)
    if not m.any(): continue
    sub=df[m]
    h=np.zeros(len(sub),dtype=int)
    for a,f,b,d in cells:
        h+=((sub.alignv==a)&(sub[f].astype(str)==b)&(sub.direction.astype(str)==d)).values
    hits[m.values]=h
df['nhits']=hits
book=df[df.nhits>0].copy()

print(f"OOS book trades: {len(book)}  (era 2025-07-01 -> corpus end)")
print(f"per-trade: ev {book.net_ladder.mean():+.2f}p | WR {(book.net_ladder>0).mean()*100:.1f}% | "
      f"avg win {book.net_ladder[book.net_ladder>0].mean():+.2f} | avg loss {book.net_ladder[book.net_ladder<=0].mean():+.2f}")
wr=(book.net_ladder>0).mean()
print(f"P(3 losses in a row at book WR): {(1-wr)**3*100:.1f}% per any 3-trade window")

# daily aggregation (corpus is exhaustive — overstates live counts; shape still informative)
book['day']=book.entry_time.dt.date
daily=book.groupby('day').net_ladder.agg(['sum','size'])
print(f"\nOOS days with >=1 book trade: {len(daily)}")
print(f"red days: {(daily['sum']<0).mean()*100:.1f}% | mean red day {daily['sum'][daily['sum']<0].mean():+.1f}p | worst {daily['sum'].min():+.1f}p")
print(f"mean green day {daily['sum'][daily['sum']>=0].mean():+.1f}p")
streak=0; mx=0
for v in daily['sum']: streak=streak+1 if v<0 else 0; mx=max(mx,streak)
print(f"longest red-day streak OOS: {mx} days")

# multi-cell confirmation
print("\nmulti-cell confirmation (n matching sides):")
for lo,hi,lab in [(1,1,'exactly 1'),(2,99,'>=2')]:
    s=book[(book.nhits>=lo)&(book.nhits<=hi)].net_ladder
    if len(s):
        t=s.mean()/(s.std(ddof=1)/np.sqrt(len(s))+1e-9)
        print(f"  {lab:9}: n={len(s):6} ev {s.mean():+.2f}p WR {(s>0).mean()*100:.1f}% t={t:.1f}")
# and per the trades-we'd-give-up question
one=book[book.nhits==1].net_ladder; multi=book[book.nhits>=2].net_ladder
if len(multi): print(f"  tightening to >=2 keeps {len(multi)/len(book)*100:.0f}% of volume, forfeits {one.sum():+.0f}p of single-hit net")
