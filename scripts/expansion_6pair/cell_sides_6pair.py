"""Direction-key the 6-pair sweep survivors -> candidate cell-SIDES.
Same rule as the live book refinement: a side is granted when OOS n>=30
and OOS ev>=1.25 for that side specifically; sides inherit cell provenance."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
df = pq.read_table('/home/ubuntu/scored_6pair.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
te = df[df.entry_time >= pd.Timestamp('2025-07-01', tz='UTC')]

cells = pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/full_cell_sweep_6pair_2026-06-11.csv')
cells = cells[cells.dir_robust]

rows=[]
for _, c in cells.iterrows():
    sub = te[(te.pair==c['pair'])&(te.strategy==c['strategy'])&(te.alignv==c['align'])&(te[c['factor']].astype(str)==c['bucket'])]
    for d in ('long','short'):
        sd = sub[sub.direction==d].net_ladder
        if len(sd)<30: continue
        ev = sd.mean()
        if ev<1.25: continue
        t = ev/(sd.std(ddof=1)/np.sqrt(len(sd))+1e-9)
        rows.append(dict(pair=c['pair'], strategy=c['strategy'], align=c['align'],
            factor=c['factor'], bucket=c['bucket'], direction=d, n_te=len(sd),
            ev_te=round(ev,2), t_oos=round(t,1), wr_te=round(100*(sd>0).mean(),1),
            cell_lift=c['lift']))
res = pd.DataFrame(rows).sort_values(['pair','ev_te'], ascending=[True,False])
res.to_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/cell_book_6pair_candidate_sides_2026-06-11.csv', index=False)
print(f"candidate cell-sides: {len(res)}")
print(res.groupby(['pair','direction'], observed=True).agg(sides=('ev_te','size'), best_ev=('ev_te','max'), vol=('n_te','sum')).to_string())
print("\nTOP 20 sides by OOS ev:")
print(res.sort_values('ev_te',ascending=False).head(20).to_string(index=False))
