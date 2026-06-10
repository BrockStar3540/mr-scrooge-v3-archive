import pandas as pd, numpy as np
import pyarrow.parquet as pq
NEED = ['pair','strategy','direction','entry_time','net_ladder','alignv']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet', columns=NEED).to_pandas(categories=['pair','strategy','direction'])
df = df[df.pair.isin(['AUD_USD','EUR_USD','GBP_USD','USD_CAD'])]

print("=== CURRENT strategy x direction x align EV (net_ladder, 4 live pairs, 8yr) ===")
m = df.groupby(['strategy','direction','alignv'], observed=True).net_ladder.mean().unstack('alignv').round(2)
n = df.groupby(['strategy','direction'], observed=True).size()
m['n'] = n
m = m[m['n'] >= 4000]
print(m.sort_values(4, ascending=False).to_string())

print("\n=== OVERLAP: strategies co-firing on the same (pair, entry_time, direction) ===")
g = df.groupby(['pair','entry_time','direction'], observed=True).strategy.nunique()
print(f"distinct (pair,time,dir) setups: {len(g)}")
print("strategies firing simultaneously:", g.value_counts().sort_index().to_dict())
multi = (g>=2).mean()
print(f"share of setups with >=2 strategy names on the SAME state: {multi*100:.1f}%")
# which names co-fire most
pairs = {}
sub = df[['pair','entry_time','direction','strategy']]
for (p,t,d), grp in sub.groupby(['pair','entry_time','direction'], observed=True):
    ss = sorted(set(grp.strategy))
    if len(ss)>=2:
        for i in range(len(ss)):
            for j in range(i+1,len(ss)):
                k=(ss[i],ss[j]); pairs[k]=pairs.get(k,0)+1
top = sorted(pairs.items(), key=lambda kv:-kv[1])[:10]
for (a,b),c in top: print(f"  {a} + {b}: {c}")
