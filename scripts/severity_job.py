"""Severity head redesign: P(full stop) classifier (replaces broken q10).
Label: net_ladder <= -9.5 (a full -10/-12 stop, era-tolerant). Walk-forward.
Test: does vetoing high-P(stop) candidates ON TOP of the gate add OOS pips?"""
import pandas as pd, numpy as np
import pyarrow.parquet as pq
import lightgbm as lgb
from sklearn.metrics import roc_auc_score

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
IDC = ['pair','strategy_id','direction_exec','session_bucket']
ALL = F14 + IDC
df = pq.read_table('/home/ubuntu/scored_7yr.parquet',
    columns=F14+['pair','strategy','direction','session','entry_time','net_ladder','alignv']).to_pandas(categories=F14+['pair','strategy','direction','session'])
df = df.rename(columns={'strategy':'strategy_id','direction':'direction_exec','session':'session_bucket'})
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
df['stopped'] = (df.net_ladder <= -9.5).astype(int)
for c in ALL: df[c] = df[c].astype('category')
tr = df[df.entry_time < pd.Timestamp('2024-07-01', tz='UTC')]
te = df[df.entry_time >= pd.Timestamp('2025-07-01', tz='UTC')].copy()
print(f"stop rate: train {tr.stopped.mean()*100:.1f}%  test {te.stopped.mean()*100:.1f}%", flush=True)
m = lgb.LGBMClassifier(n_estimators=400, learning_rate=0.05, num_leaves=63,
                       min_child_samples=300, random_state=7, verbose=-1)
m.fit(tr[ALL], tr['stopped'], categorical_feature=ALL)
te['p_stop'] = m.predict_proba(te[ALL])[:,1]
print(f"P(stop) OOS AUC: {roc_auc_score(te.stopped, te.p_stop):.4f}", flush=True)
dec = pd.qcut(te.p_stop, 10, duplicates='drop')
print(te.groupby(dec, observed=True).agg(n=('stopped','size'), stop_rate=('stopped','mean'), avg_pips=('net_ladder','mean')).round(2).to_string(), flush=True)

# replicate gate proxy from prospector job
pb = pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/playbook_ev_pairaware.csv')
amp_of = pb.groupby('strategy')['amp_factor'].agg(lambda s: s.mode().iat[0]).to_dict()
floor_of = pb.groupby('strategy')['floor'].agg(lambda s: s.mode().iat[0]).to_dict()
cell_ev = {(r['pair'],r['strategy'],r['direction'],int(r['align']),str(r['bucket'])): r['ev_pips'] for _,r in pb.iterrows()}
def takes(row):
    amp = amp_of.get(row.strategy_id)
    if amp is None: return False
    al = int(row.alignv)
    if al < floor_of.get(row.strategy_id, 2): return False
    ev = cell_ev.get((str(row.pair), row.strategy_id, str(row.direction_exec), al, str(getattr(row, amp)) if amp in F14 else ''))
    return ev is not None and ev >= 1.25
te['take_gate'] = [takes(r) for r in te.itertuples()]
g = te[te.take_gate]
days = (te.entry_time.max()-te.entry_time.min()).days
print(f"\ngate proxy baseline: n={len(g)} avg={g.net_ladder.mean():+.2f} total={g.net_ladder.sum():+.0f}", flush=True)
for cap in (0.55, 0.50, 0.45, 0.40):
    k = g[g.p_stop <= cap]
    cut = g[g.p_stop > cap]
    print(f"gate + P(stop)<={cap}: keep n={len(k)} ({len(k)/days:.0f}/d) avg={k.net_ladder.mean():+.2f} total={k.net_ladder.sum():+.0f} | cut avg={cut.net_ladder.mean():+.2f} (cut total {cut.net_ladder.sum():+.0f})", flush=True)
import os
os.makedirs('/home/ubuntu/mr-scrooge-v3/data/lab_training/severity_v1', exist_ok=True)
m.booster_.save_model('/home/ubuntu/mr-scrooge-v3/data/lab_training/severity_v1/p_stop.txt')
print("saved severity_v1 (NOT wired)", flush=True)
