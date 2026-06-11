#!/bin/bash
set -e
AD="/Volumes/Alien Device"
OUT="$AD/mr-scrooge-v3/research/replay_lab/results/backfill_8yr_6pair"
ASM="$AD/mr-scrooge-v3/ml-lab/scripts/assemble_extended_corpus.py"
cd /Users/brock-mini-mac
mkdir -p /tmp/all6; rm -f /tmp/all6/trades_*.csv
for f in "$OUT"/trades_*.csv; do ln -sf "$f" "/tmp/all6/$(basename "$f")"; done
echo "[0] trades files linked: $(ls /tmp/all6/trades_*.csv 2>/dev/null | wc -l | tr -d ' ')"

echo "[1] assemble (bucketize all 6 pairs)..."
/usr/bin/python3 "$ASM" /tmp/all6 /tmp/corpus_6pair.csv.gz 2>&1 | tail -3

echo "[2] score_extended (net_ladder, 6-pair spreads)..."
cp score_extended.py /tmp/score_6.py
sed -i '' 's/"USD_CAD":1.8}/"USD_CAD":1.8,"USD_JPY":1.0,"USD_CHF":1.5,"NZD_USD":1.8,"EUR_JPY":1.5,"AUD_JPY":1.5,"EUR_GBP":1.5}/' /tmp/score_6.py
/usr/bin/python3 /tmp/score_6.py /tmp/corpus_6pair.csv.gz /tmp/scored_6pair.parquet 2>&1 | tail -3

echo "[3] factor-bucket EV by pair x direction (net_ladder, the locked model)..."
cat > /tmp/agg_fb.py <<'PYEOF'
import pandas as pd
df=pd.read_parquet('/tmp/scored_6pair.parquet')
FACTORS=['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
df['_winp']=df['net_ladder'].where(df['net_ladder']>0)
df['_losp']=df['net_ladder'].where(df['net_ladder']<0)
df['_w']=(df['net_ladder']>0).astype('int32')
df['_l']=(df['net_ladder']<0).astype('int32')
parts=[]
for F in FACTORS:
    keys=['pair','direction','strategy','alignv',F]
    g=df.groupby(keys,observed=True)
    r=g.agg(n=('net_ladder','size'),wins=('_w','sum'),losses=('_l','sum'),
            avgWin=('_winp','mean'),avgLoss=('_losp','mean'),
            ev_pips=('net_ladder','mean'),net_pips=('net_ladder','sum')).reset_index()
    r=r.rename(columns={F:'bucket','alignv':'align'}); r['factor']=F
    parts.append(r)
res=pd.concat(parts,ignore_index=True)
res['WR_pct']=(100*res['wins']/res['n']).round(1)
for c in ['avgWin','avgLoss','ev_pips']: res[c]=res[c].round(3)
res['net_pips']=res['net_pips'].round(1)
res=res[['pair','direction','strategy','align','factor','bucket','n','wins','losses','WR_pct','avgWin','avgLoss','ev_pips','net_pips']]
res=res.sort_values(['pair','direction','net_pips'],ascending=[True,True,False])
res.to_csv('/tmp/factor_bucket_ev_6pair_dir.csv',index=False)
print('WROTE /tmp/factor_bucket_ev_6pair_dir.csv  rows=%d  pairs=%s'%(len(res),sorted(res['pair'].unique())))
print('rows per pair x direction:'); print(res.groupby(['pair','direction']).size().to_string())
PYEOF
/usr/bin/python3 /tmp/agg_fb.py
# durable copy to Dropbox
DB="/Users/brock-mini-mac/Library/CloudStorage/Dropbox/LLM Sessions/Claude Sessions/Scrooge"
cp /tmp/factor_bucket_ev_6pair_dir.csv "$DB/" 2>/dev/null && echo "[4] copied to Dropbox" || echo "[4] (dropbox copy skipped)"
echo "ALLDONE"
