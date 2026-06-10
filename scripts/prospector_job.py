"""Block 2 — quantile-EV prospector + off-policy head-to-head (overnight, 2026-06-10).
Train q10/q50/q90 net_ladder models walk-forward; compare model policy vs a
playbook-gate proxy on the same OOS rows. Nothing here touches live."""
import json
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import lightgbm as lgb

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
IDC = ['pair','strategy_id','direction_exec','session_bucket']
ALL = F14 + IDC
NEED = F14 + ['pair','strategy','direction','session','entry_time','net_ladder','alignv']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet', columns=NEED).to_pandas(categories=F14+['pair','strategy','direction','session'])
df = df.rename(columns={'strategy':'strategy_id','direction':'direction_exec','session':'session_bucket'})
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
for c in ALL: df[c] = df[c].astype('category')

TRAIN_END = pd.Timestamp('2024-07-01', tz='UTC')
TEST_START = pd.Timestamp('2025-07-01', tz='UTC')
tr = df[df.entry_time < TRAIN_END]
te = df[df.entry_time >= TEST_START].copy()
print(f"train n={len(tr)}  OOS test n={len(te)} ({te.entry_time.min().date()}..{te.entry_time.max().date()})", flush=True)

models = {}
for q in (0.1, 0.5, 0.9):
    m = lgb.LGBMRegressor(objective='quantile', alpha=q, n_estimators=400,
                          learning_rate=0.05, num_leaves=63, min_child_samples=300,
                          subsample=0.9, random_state=7, verbose=-1)
    m.fit(tr[ALL], tr['net_ladder'], categorical_feature=ALL)
    te[f'q{int(q*100)}'] = m.predict(te[ALL])
    models[q] = m
    print(f"q{q} trained", flush=True)

# quantile sanity: q50 decile lift on OOS
print("\n=== OOS decile lift by q50 prediction ===", flush=True)
dec = pd.qcut(te['q50'], 10, duplicates='drop')
print(te.groupby(dec, observed=True).agg(n=('net_ladder','size'), actual=('net_ladder','mean'), pred=('q50','mean')).round(2).to_string(), flush=True)

# ---- head-to-head on identical OOS rows ----
# (A) playbook-gate proxy: join live playbook cells (pair,strategy,direction,align,amp bucket), EV>=1.25 + floor + adr gate
pb = pd.read_csv('/home/ubuntu/mr-scrooge-v3/data/playbook_ev_pairaware.csv')
amp_of = pb.groupby('strategy')['amp_factor'].agg(lambda s: s.mode().iat[0]).to_dict()
floor_of = pb.groupby('strategy')['floor'].agg(lambda s: s.mode().iat[0]).to_dict()
cell_ev = {}
for _, r in pb.iterrows():
    cell_ev[(r['pair'], r['strategy'], r['direction'], int(r['align']), str(r['bucket']))] = r['ev_pips']
def gate_takes(row):
    strat = row.strategy_id; amp = amp_of.get(strat)
    if amp is None: return False
    al = int(row.alignv)
    if al < floor_of.get(strat, 2): return False
    b = str(getattr(row, amp)) if amp in F14 else ''
    ev = cell_ev.get((str(row.pair), strat, str(row.direction_exec), al, b))
    return ev is not None and ev >= 1.25
te['take_gate'] = [gate_takes(r) for r in te.itertuples()]

# (B) model policy: q50 > 0 and q10 bounded
for q10min in (-8, -6, -5):
    te[f'take_model_{abs(q10min)}'] = (te['q50'] > 0) & (te['q10'] > q10min)

days = (te.entry_time.max() - te.entry_time.min()).days
def report(mask, label):
    k = te[mask]
    if len(k)==0: print(f"{label:24} n=0"); return
    print(f"{label:24} n={len(k):7d} ({len(k)/days:5.1f}/d) WR={100*(k.net_ladder>0).mean():4.1f}% avg={k.net_ladder.mean():+5.2f}p total={k.net_ladder.sum():+9.0f}p", flush=True)
print(f"\n=== HEAD-TO-HEAD on {len(te)} identical OOS rows ({days}d) ===", flush=True)
report(te['take_gate'], "playbook-gate proxy")
for q10min in (8,6,5):
    report(te[f'take_model_{q10min}'], f"model q50>0 & q10>-{q10min}")
report(te['take_gate'] & (te['q50']>0), "gate AND model agree")
report(te['take_gate'] & ~(te['q50']>0), "gate takes, model refuses")
report(~te['take_gate'] & (te['q50']>0) & (te['q10']>-6), "model takes, gate refuses")

import os
os.makedirs('/home/ubuntu/mr-scrooge-v3/data/lab_training/prospector_v1', exist_ok=True)
for q, m in models.items():
    m.booster_.save_model(f'/home/ubuntu/mr-scrooge-v3/data/lab_training/prospector_v1/model_q{int(q*100)}.txt')
print("\nsaved prospector_v1 (NOT wired)", flush=True)
