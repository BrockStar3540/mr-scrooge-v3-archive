"""FULL cell sweep: every (strategy, align, factor, bucket) on the live-4-pair
corpus. Survival bar (mass-test hardened): n_tr>=300, n_te>=100, ev_tr>=1.25,
ev_te>=1.25, OOS lift vs strategy+align baseline >= +0.5, OOS t-stat>=2,
and BOTH directions separately +EV OOS (n>=30 each) -> dir_robust."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet',
    columns=F14+['pair','strategy','direction','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
df = df[df.pair.isin(['AUD_USD','EUR_USD','GBP_USD','USD_CAD'])]
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
ALIGNED = {'T1':'T1a','T4':'T4a','H20':('H20a','H20b'),'H60':('H60a','H60b')}

out=[]
for strat in ROSTER:
    ds = df[df.strategy==strat]
    for a in range(5):
        da = ds[ds.alignv==a]
        tr_b = da[da.era=='tr'].net_ladder; te_b = da[da.era=='te'].net_ladder
        if len(te_b) < 100: continue
        bte = te_b.mean()
        for f in F14:
            # skip tautological aligned-bucket conditions at align4
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
                # direction robustness OOS
                okdir=True
                for d in ('long','short'):
                    sd = sub[(sub.era=='te')&(sub.direction==d)].net_ladder
                    if len(sd)>=30 and sd.mean()<=0: okdir=False
                out.append(dict(strategy=strat, align=a, factor=f, bucket=str(bucket),
                    n_tr=len(str_), n_te=len(ste), ev_tr=round(etr,2), ev_te=round(ete,2),
                    base_te=round(bte,2), lift=round(lift,2), t_oos=round(t,1),
                    wr_te=round(100*(ste>0).mean(),1), dir_robust=okdir))
res = pd.DataFrame(out).sort_values(['strategy','lift'], ascending=[True,False])
res.to_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/full_cell_sweep_2026-06-11.csv', index=False)
rob = res[res.dir_robust]
print(f"survivors: {len(res)} ({res.strategy.nunique()} strategies) | dir-robust: {len(rob)} ({rob.strategy.nunique()} strategies)")
print("\ndir-robust survivors per strategy:")
print(rob.groupby('strategy').agg(cells=('lift','size'), best_lift=('lift','max'),
      best_ev=('ev_te','max'), vol_te=('n_te','sum')).sort_values('best_lift',ascending=False).to_string())
print("\nTOP 25 dir-robust cells by OOS lift:")
print(rob.sort_values('lift',ascending=False).head(25).to_string(index=False))
