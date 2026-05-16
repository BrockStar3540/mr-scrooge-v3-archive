#!/usr/bin/env python3
"""
mine_sub_regime_islands.py

Option B: mine winner + loser islands inside each of the 80 C01/C02 sub-regimes
(plus rare regimes kept as-is), at (strategy_id, pair, direction, sub_regime)
cell granularity.

Tree-based shaver per cell (max_depth=4, min_samples_leaf=10) for speed.
Walks leaves and picks:
  - best WINNER leaf (max P(win) with min support)
  - best LOSER leaf  (max P(loss) with min support)

Output: one row per (cell with rule found). Columns include:
  strategy_id, pair, direction, sub_regime, n, wins, losses, wr,
  winner_rule, winner_n, winner_wins, winner_losses, winner_wr, winner_lift,
  loser_rule,  loser_n,  loser_wins,  loser_losses,  loser_lr,  loser_lift

Total cells viable at n>=200 in sub-regime layout: 22,233.
Expected runtime: ~30 min on Mini.
"""
from __future__ import annotations
import time
from pathlib import Path
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
CORPUS = ROOT / 'routing-table-v2' / 'ml_training_corpus.parquet'
OUT = ROOT / 'seed-family-factory'

FACTORS = ['ATR_ratio','BB_compress','RSI14','volume_ratio','ADX14','hour_utc','bb_position']
MIN_CELL_N = 200
MIN_LEAF = 10
MIN_PURITY_GAIN = 0.10   # rule must beat parent target_rate by >=10pp

def build_sub_regime_column(df):
    """Re-fit the 40-leaf classifier for C01 and C02; tag sub_regime per row."""
    df['sub_regime'] = df['technical_regime_53']
    for parent in ['C01','C02']:
        p_mask = df['technical_regime_53'] == parent
        sub = df.loc[p_mask].dropna(subset=FACTORS + ['is_win'])
        n = len(sub)
        X = sub[FACTORS].values
        y = sub['is_win'].astype(bool).values
        min_leaf = max(int(n*0.0125), 500)
        tree = DecisionTreeClassifier(max_leaf_nodes=40, min_samples_leaf=min_leaf,
                                      criterion='gini', random_state=42)
        tree.fit(X, y)
        leaf_ids = tree.apply(X)
        stats = {lid:{'n':int((leaf_ids==lid).sum()), 'w':int(y[leaf_ids==lid].sum())} for lid in np.unique(leaf_ids)}
        sorted_lids = sorted(stats.keys(), key=lambda x: stats[x]['w']/stats[x]['n'])
        lid_to_sub = {lid:i for i,lid in enumerate(sorted_lids)}
        df.loc[sub.index, 'sub_regime'] = [f'{parent}_{lid_to_sub[l]}' for l in leaf_ids]
    return df

def best_target_leaf(tree, target_value, min_keep):
    t = tree.tree_
    class_idx = {c:i for i,c in enumerate(tree.classes_)}
    tgt_idx = class_idx.get(target_value, class_idx.get(int(target_value), None))
    if tgt_idx is None: return None
    best = None
    def walk(node, path):
        nonlocal best
        if t.children_left[node] == _tree.TREE_LEAF:
            n_kept = int(t.n_node_samples[node])
            if n_kept < min_keep: return
            probs = t.value[node][0]
            tgt_kept = int(round(float(probs[tgt_idx]) * n_kept))
            rate = tgt_kept / n_kept
            if best is None or rate > best[4]:
                best = (list(path), n_kept, tgt_kept, n_kept - tgt_kept, rate)
            return
        feat = FACTORS[t.feature[node]]
        thr = float(t.threshold[node])
        walk(t.children_left[node],  path + [(feat,'<=',thr)])
        walk(t.children_right[node], path + [(feat,'>',thr)])
    walk(0, [])
    return best

def rule_string(clauses):
    return ' AND '.join(f'{f}{op}{v:.6g}' for f,op,v in clauses)

def main():
    t0 = time.time()
    print(f'[load] {CORPUS}')
    cols = ['source','strategy_id','pair','direction','technical_regime_53','is_win'] + FACTORS
    df = pq.read_table(CORPUS, columns=cols).to_pandas()
    print(f'  rows: {len(df):,}  ({time.time()-t0:.1f}s)')

    print('[classify sub_regimes...]')
    df = build_sub_regime_column(df)
    print(f'  done  ({time.time()-t0:.1f}s)')

    print('[group by (strategy, pair, direction, sub_regime)]')
    keys = ['strategy_id','pair','direction','sub_regime']
    grouped = df.groupby(keys, sort=False)
    print(f'  groups: {grouped.ngroups:,}  ({time.time()-t0:.1f}s)')

    rows = []
    cells_done = 0
    for key, cell in grouped:
        n = len(cell)
        if n < MIN_CELL_N: continue
        sub = cell.dropna(subset=FACTORS + ['is_win'])
        if len(sub) < MIN_CELL_N: continue
        wins = int(sub['is_win'].sum())
        losses = len(sub) - wins
        if wins < 5 or losses < 5: continue
        wr_parent = wins / len(sub)
        loss_rate_parent = 1 - wr_parent

        X = sub[FACTORS].values
        y = sub['is_win'].astype(bool).values
        tree = DecisionTreeClassifier(max_depth=4, criterion='gini',
                                      min_samples_leaf=MIN_LEAF, random_state=42)
        tree.fit(X, y)

        # winner
        wleaf = best_target_leaf(tree, target_value=True, min_keep=MIN_LEAF)
        # loser
        lleaf = best_target_leaf(tree, target_value=False, min_keep=MIN_LEAF)

        row = {
            'strategy_id': key[0], 'pair': key[1], 'direction': key[2], 'sub_regime': key[3],
            'parent_n': n, 'parent_wins': wins, 'parent_losses': losses, 'parent_wr': round(wr_parent,4),
        }
        if wleaf and (wleaf[4] - wr_parent) >= MIN_PURITY_GAIN:
            clauses, nk, wk, lk, rate = wleaf
            row.update({
                'winner_rule': rule_string(clauses),
                'winner_n': nk, 'winner_wins': wk, 'winner_losses': lk,
                'winner_wr': round(rate, 4),
                'winner_lift': round((rate / wr_parent) if wr_parent > 0 else 0, 3),
            })
        if lleaf and (lleaf[4] - loss_rate_parent) >= MIN_PURITY_GAIN:
            clauses, nk, wk, lk, rate = lleaf
            row.update({
                'loser_rule': rule_string(clauses),
                'loser_n': nk, 'loser_wins': wk, 'loser_losses': lk,
                'loser_lr': round(rate, 4),
                'loser_lift': round((rate / loss_rate_parent) if loss_rate_parent > 0 else 0, 3),
            })

        if 'winner_rule' in row or 'loser_rule' in row:
            rows.append(row)
        cells_done += 1
        if cells_done % 2000 == 0:
            print(f'  [{cells_done:,} cells]  islands so far: {len(rows):,}  ({time.time()-t0:.1f}s)')

    print(f'  total cells processed: {cells_done:,}  islands found: {len(rows):,}')

    out_df = pd.DataFrame(rows)
    out_csv = OUT / 'sub_regime_islands.csv'
    out_df.to_csv(out_csv, index=False)
    print(f'[write] {out_csv}  ({len(out_df):,} rows, {time.time()-t0:.1f}s)')

    # Summary
    has_w = out_df['winner_rule'].notna() if 'winner_rule' in out_df.columns else pd.Series(dtype=bool)
    has_l = out_df['loser_rule'].notna()  if 'loser_rule'  in out_df.columns else pd.Series(dtype=bool)
    print()
    print(f'cells with winner_rule:        {int(has_w.sum()):,}')
    print(f'cells with loser_rule:         {int(has_l.sum()):,}')
    print(f'cells with both:               {int((has_w & has_l).sum()):,}')
    print(f'cells with neither:            {int((~has_w & ~has_l).sum()):,}')

    if has_w.any():
        w = out_df[has_w]
        print(f'  winner cells with wr>=0.50:  {int((w["winner_wr"]>=0.50).sum()):,}')
        print(f'  winner cells with wr>=0.75:  {int((w["winner_wr"]>=0.75).sum()):,}')
        print(f'  winner cells with wr=1.00:   {int((w["winner_wr"]>=0.99).sum()):,}')
    if has_l.any():
        l = out_df[has_l]
        print(f'  loser cells with loss_rate>=0.85:  {int((l["loser_lr"]>=0.85).sum()):,}')
        print(f'  loser cells with loss_rate=1.00:    {int((l["loser_lr"]>=0.99).sum()):,}')

    print(f'Total elapsed: {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
