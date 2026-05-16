#!/usr/bin/env python3
"""
Brother/sister expansion on sub-regime islands.

Starting set: filter sub_regime_islands.csv to deployment-confident seeds
  (winner_n >= 30 AND winner_wr >= 0.40)  -- ~76 seeds
For each seed, generate ~30 sibling mutations (one-factor-at-a-time)
inside the same parent cell (strategy + pair + direction + sub_regime).
Score children against the same parent rows. Bucket: winner_seed / near_pure /
false_friend / reject.

Output: probe-style child bank for the new sub-regime layer.
"""
from __future__ import annotations
import time, re
from pathlib import Path
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from sklearn.tree import DecisionTreeClassifier
import math

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
CORPUS = ROOT / 'routing-table-v2' / 'ml_training_corpus.parquet'
ISLANDS = ROOT / 'seed-family-factory' / 'sub_regime_islands.csv'
OUT = ROOT / 'seed-family-factory'

FACTORS = ['ATR_ratio','BB_compress','RSI14','volume_ratio','ADX14','hour_utc','bb_position']
ADD_POOL = FACTORS  # any factor can be added

QSTEP = 0.05

_NUM = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*(<=|>=|<|>)\s*(-?[0-9.eE+-]+)$')

def parse_rule(rule: str):
    out = []
    if not isinstance(rule, str) or not rule: return out
    for raw in rule.split(' AND '):
        m = _NUM.match(raw.strip())
        if m:
            out.append({'feat':m.group(1),'op':m.group(2),'val':float(m.group(3))})
    return out

def render(clauses):
    return ' AND '.join(f'{c["feat"]}{c["op"]}{c["val"]:.6g}' for c in clauses)

def qstep(vals, target, direction):
    fin = vals[np.isfinite(vals)]
    if len(fin) < 20: return target
    sv = np.sort(fin)
    rank = float(np.searchsorted(sv, target)) / len(sv)
    rank_new = max(0.0, min(1.0, rank + direction * QSTEP))
    return float(np.quantile(sv, rank_new))

def mutate(clauses, parent_df):
    out = []
    for idx, c in enumerate(clauses):
        feat = c['feat']
        if feat not in parent_df.columns: continue
        vals = parent_df[feat].to_numpy()
        op = c['op']; val = c['val']
        # widen
        if op in ('>=','>'):
            v = qstep(vals, val, -1)
            if v != val: out.append(('widen_low', [dict(cc) if i!=idx else dict(cc,val=v) for i,cc in enumerate(clauses)]))
        if op in ('<=','<'):
            v = qstep(vals, val, +1)
            if v != val: out.append(('widen_high',[dict(cc) if i!=idx else dict(cc,val=v) for i,cc in enumerate(clauses)]))
        # narrow
        if op in ('>=','>'):
            v = qstep(vals, val, +1)
            if v != val: out.append(('narrow_low',[dict(cc) if i!=idx else dict(cc,val=v) for i,cc in enumerate(clauses)]))
        if op in ('<=','<'):
            v = qstep(vals, val, -1)
            if v != val: out.append(('narrow_high',[dict(cc) if i!=idx else dict(cc,val=v) for i,cc in enumerate(clauses)]))
    # add_filter
    used = {c['feat'] for c in clauses}
    for feat in ADD_POOL:
        if feat in used or feat not in parent_df.columns: continue
        v = parent_df[feat].to_numpy()
        f = v[np.isfinite(v)]
        if len(f) < 20: continue
        med = float(np.median(f))
        out.append(('add_filter', clauses + [{'feat':feat,'op':'>=','val':med}]))
        out.append(('add_filter', clauses + [{'feat':feat,'op':'<=','val':med}]))
    # remove_filter
    if len(clauses) > 1:
        for i in range(len(clauses)):
            kept = [c for j,c in enumerate(clauses) if j != i]
            out.append(('remove_filter', kept))
    return out

def apply_rule(df, clauses):
    mask = pd.Series(True, index=df.index)
    for c in clauses:
        if c['feat'] not in df.columns:
            return pd.Series(False, index=df.index)
        s = df[c['feat']]
        if   c['op'] == '<=': mask &= (s <= c['val'])
        elif c['op'] == '>=': mask &= (s >= c['val'])
        elif c['op'] == '<':  mask &= (s <  c['val'])
        elif c['op'] == '>':  mask &= (s >  c['val'])
    return mask.fillna(False)

def main():
    t0 = time.time()
    print(f'[load] {ISLANDS}')
    isl = pd.read_csv(ISLANDS)
    seeds = isl[(isl.winner_rule.notna()) & (isl.winner_n >= 30) & (isl.winner_wr >= 0.40)].copy()
    seeds['parent_seed_id'] = [f'sr{i+1:05d}' for i in range(len(seeds))]
    print(f'  seeds: {len(seeds):,}  ({time.time()-t0:.1f}s)')

    print(f'[load] {CORPUS}')
    cols = ['strategy_id','pair','direction','technical_regime_53','is_win'] + FACTORS
    corpus = pq.read_table(CORPUS, columns=cols).to_pandas()
    # re-classify sub_regime
    print('[classify sub_regimes]')
    corpus['sub_regime'] = corpus['technical_regime_53']
    for parent in ['C01','C02']:
        p_mask = corpus['technical_regime_53'] == parent
        sub = corpus.loc[p_mask].dropna(subset=FACTORS + ['is_win'])
        n = len(sub)
        X = sub[FACTORS].values; y = sub['is_win'].astype(bool).values
        min_leaf = max(int(n*0.0125), 500)
        tree = DecisionTreeClassifier(max_leaf_nodes=40, min_samples_leaf=min_leaf, random_state=42)
        tree.fit(X, y)
        lids = tree.apply(X)
        stats = {l:{'n':int((lids==l).sum()),'w':int(y[lids==l].sum())} for l in np.unique(lids)}
        sorted_l = sorted(stats.keys(), key=lambda x: stats[x]['w']/stats[x]['n'])
        m = {l:i for i,l in enumerate(sorted_l)}
        corpus.loc[sub.index, 'sub_regime'] = [f'{parent}_{m[l]}' for l in lids]
    print(f'  done  ({time.time()-t0:.1f}s)')

    keys = ['strategy_id','pair','direction','sub_regime']
    grp = corpus.groupby(keys, sort=False)
    print(f'  cell groups: {grp.ngroups:,}  ({time.time()-t0:.1f}s)')

    lineage = []
    for si, seed in seeds.iterrows():
        key = (seed['strategy_id'], seed['pair'], seed['direction'], seed['sub_regime'])
        try:
            parent = grp.get_group(key)
        except KeyError:
            continue
        parent = parent.dropna(subset=FACTORS + ['is_win'])
        if len(parent) < 30: continue
        n_p = len(parent); w_p = int(parent['is_win'].sum()); l_p = n_p - w_p
        wr_p = w_p / n_p
        base_clauses = parse_rule(seed['winner_rule'])
        children = mutate(base_clauses, parent)
        for ci, (mtype, cl) in enumerate(children):
            child_rule = render(cl)
            if child_rule == seed['winner_rule']: continue
            mask = apply_rule(parent, cl)
            sub = parent[mask]
            n_c = len(sub)
            if n_c < 10: continue
            w_c = int(sub['is_win'].sum()); l_c = n_c - w_c
            wr_c = w_c / n_c
            purity_gain = wr_c - wr_p
            survival = max(0.0, purity_gain) * math.sqrt(max(0, w_c - 10)) / (1 + l_c)
            # bucket
            if w_c >= 10 and (l_c <= 2 or wr_c >= 0.75): bucket = 'winner_seed'
            elif w_c >= 8 and wr_c >= 0.65 and wr_c > wr_p + 0.15: bucket = 'near_pure_seed'
            elif w_c >= 5 and wr_c > wr_p + 0.10: bucket = 'false_friend_sibling'
            else: bucket = 'child_reject'
            lineage.append({
                'seed_id': f'{seed["parent_seed_id"]}_c{ci:04d}',
                'parent_seed_id': seed['parent_seed_id'],
                'strategy_id': key[0], 'pair': key[1], 'direction': key[2], 'sub_regime': key[3],
                'mutation_type': mtype,
                'base_rule': seed['winner_rule'],
                'child_rule': child_rule,
                'n': n_c, 'wins': w_c, 'losses': l_c, 'wr': round(wr_c, 4),
                'parent_n': n_p, 'parent_wins': w_p, 'parent_wr': round(wr_p, 4),
                'seed_n': int(seed['winner_n']), 'seed_wins': int(seed['winner_wins']),
                'seed_wr': round(float(seed['winner_wr']), 4),
                'purity_gain': round(purity_gain, 4),
                'wr_lift_vs_seed': round(wr_c - float(seed['winner_wr']), 4),
                'seed_survival_score': round(survival, 4),
                'bucket': bucket,
            })
        if (si+1) % 25 == 0:
            print(f'  [seed {si+1}/{len(seeds)}]  children so far: {len(lineage):,}  ({time.time()-t0:.1f}s)')

    df = pd.DataFrame(lineage)
    out_csv = OUT / 'sub_regime_seed_family_lineage.csv'
    df.to_csv(out_csv, index=False)
    print(f'[write] {out_csv}  ({len(df):,} rows, {time.time()-t0:.1f}s)')

    print()
    print('Bucket distribution:')
    print(df['bucket'].value_counts().to_string())
    print()
    print('Top 20 by seed_survival_score (winner_seed only):')
    ws = df[df.bucket=='winner_seed'].sort_values('seed_survival_score', ascending=False).head(20)
    print(ws[['strategy_id','pair','direction','sub_regime','mutation_type','n','wins','losses','wr','seed_wr','wr_lift_vs_seed','seed_survival_score']].to_string())

if __name__ == '__main__':
    main()
