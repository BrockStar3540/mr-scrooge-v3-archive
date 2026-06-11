"""FULL cell sweep on the 6 NEW pairs (USD_JPY, USD_CHF, NZD_USD, EUR_JPY,
AUD_JPY, EUR_GBP) — identical survival bar to the live 4-pair cell book:
n_tr>=300, n_te>=100, ev_tr>=1.25, ev_te>=1.25, OOS lift vs strategy+align
baseline >= +0.5, OOS t-stat>=2, both directions separately +EV OOS (n>=30
each) -> dir_robust. Corpus: parallel-session scored_6pair.parquet
(net_ladder, spreads: USD_JPY 1.0 validated; others ASSUMED 1.5/1.8)."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
df = pq.read_table('/home/ubuntu/scored_6pair.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
PAIRS = ['USD_JPY','USD_CHF','NZD_USD','EUR_JPY','AUD_JPY','EUR_GBP']
df = df[df.pair.isin(PAIRS)]
print('rows:', len(df), '| pairs:', sorted(set(df.pair.astype(str))))
df['era'] = np.where(df.entry_time < pd.Timestamp('2024-07-01', tz='UTC'), 'tr',
             np.where(df.entry_time >= pd.Timestamp('2025-07-01', tz='UTC'), 'te', 'mid'))
df = df[df.era != 'mid']
ROSTER = sorted(set(df.strategy.astype(str)) & {
 'alpha_pullback_v2','alpha_breakout_retest_v2','alpha_extended_fade_v2','echo_box_fade_v2',
 'charlie_compression_breakout','bravo_failed_momentum','bravo_expansion_continuation',
 'delta_tag_and_go_v2','TF2_pullback_EMA20_short','BR2_vcb_short','CP3_vol_coil_fade_long',
 'CP3_vol_coil_fade_short','MR5_williams_extreme_short','MR4_zscore_extreme_short',
 'MR4_zscore_extreme_long','MR2_bb_reversion_short','RG1_range_bound_scalp_long',
 'RG1_range_bound_scalp_short','BR3_inside_bar_short','CP1_coil_breakout_short',
 'CP2_squeeze_momentum_long'})
print('strategies present:', len(ROSTER))
ALIGNED = {'T1':'T1a','T4':'T4a','H20':('H20a','H20b'),'H60':('H60a','H60b')}

out=[]
# per-PAIR sweep: new pairs must each earn their own cells (no cross-pair pooling)
for pair in PAIRS:
  dp = df[df.pair==pair]
  for strat in ROSTER:
    ds = dp[dp.strategy==strat]
    for a in range(5):
        da = ds[ds.alignv==a]
        tr_b = da[da.era=='tr'].net_ladder; te_b = da[da.era=='te'].net_ladder
        if len(te_b) < 100: continue
        bte = te_b.mean()
        for f in F14:
            g = da.groupby(f, observed=True)
            for bucket, sub in g:
                if a==4 and f in ALIGNED:
                    al = ALIGNED[f]
                    if (bucket==al) or (isinstance(al,tuple) and bucket in al): continue
                str_, ste = sub[sub.era=='tr'].net_ladder, sub[sub.era=='te'].net_ladder
                if len(str_)<300 or len(ste)<100: continue
                if len(ste)/max(len(te_b),1) > 0.85: continue  # near-tautology
                etr, ete = str_.mean(), ste.mean()
                if etr<1.25 or ete<1.25: continue
                lift = ete - bte
                if lift < 0.5: continue
                t = ete/ (ste.std(ddof=1)/np.sqrt(len(ste)) + 1e-9)
                if t < 2: continue
                okdir=True
                for d in ('long','short'):
                    sd = sub[(sub.era=='te')&(sub.direction==d)].net_ladder
                    if len(sd)>=30 and sd.mean()<=0: okdir=False
                out.append(dict(pair=pair, strategy=strat, align=a, factor=f, bucket=str(bucket),
                    n_tr=len(str_), n_te=len(ste), ev_tr=round(etr,2), ev_te=round(ete,2),
                    base_te=round(bte,2), lift=round(lift,2), t_oos=round(t,1),
                    wr_te=round(100*(ste>0).mean(),1), dir_robust=okdir))
res = pd.DataFrame(out)
if len(res):
    res = res.sort_values(['pair','strategy','lift'], ascending=[True,True,False])
res.to_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/full_cell_sweep_6pair_2026-06-11.csv', index=False)
if not len(res):
    print('NO SURVIVORS'); raise SystemExit
rob = res[res.dir_robust]
print(f"survivors: {len(res)} | dir-robust: {len(rob)}")
print("\nper-pair dir-robust:")
print(rob.groupby('pair').agg(cells=('lift','size'), strategies=('strategy','nunique'),
      best_lift=('lift','max'), best_ev=('ev_te','max'), vol_te=('n_te','sum')).to_string())
print("\nper-strategy dir-robust:")
print(rob.groupby('strategy').agg(cells=('lift','size'), best_lift=('lift','max'),
      best_ev=('ev_te','max')).sort_values('best_lift',ascending=False).to_string())
print("\nTOP 30 dir-robust cells by OOS lift:")
print(rob.sort_values('lift',ascending=False).head(30).to_string(index=False))
