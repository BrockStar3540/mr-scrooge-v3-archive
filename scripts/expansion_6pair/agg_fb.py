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
