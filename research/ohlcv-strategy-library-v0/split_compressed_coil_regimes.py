#!/usr/bin/env python3
"""
split_compressed_coil_regimes.py

Reverse-engineer sub-regime splits inside C01 and C02.

The 53-regime classifier puts 99.6% of trades into C01 + C02. This script asks:
is there real structure inside those mega-regimes? Can we slice each into ~10
sub-regimes that:
  (a) split the trades evenly  (each ~10% of parent volume)
  (b) have meaningfully different WR  (validates the split matters)

Method:
  1. For each of C01 / C02 separately:
     - Fit DecisionTreeClassifier(max_leaf_nodes=10, min_samples_leaf=parent//12)
       on the 7 factors -> is_win
     - The tree picks splits to maximize WR purity per leaf
     - Each leaf = one sub-regime
  2. Validate:
     - leaf size distribution (should be roughly even)
     - WR per leaf (should diverge if the split is meaningful)
     - rule reconstruction (so we can replay live)

Output:
  c0102_sub_regime_definitions.csv   one row per sub-regime: parent (C01/C02),
                                     sub_id (0-9), rule string, n_trades, wins, wr
  c0102_sub_regime_validation.md     summary of variance, recommendations
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
CORPUS = ROOT / 'routing-table-v2' / 'ml_training_corpus.parquet'
OUT = ROOT / 'seed-family-factory'

FACTORS = ['ATR_ratio','BB_compress','RSI14','volume_ratio','ADX14','hour_utc','bb_position']

MAX_LEAVES = 10
def main():
    cols = ['technical_regime_53','is_win'] + FACTORS
    print(f'[load] {CORPUS}')
    df = pq.read_table(CORPUS, columns=cols).to_pandas()
    print(f'  rows: {len(df):,}')

    results = []
    for parent_regime in ['C01', 'C02']:
        sub = df[df['technical_regime_53'] == parent_regime].copy()
        sub = sub.dropna(subset=FACTORS + ['is_win'])
        n = len(sub)
        print(f'\n=== {parent_regime}: {n:,} trades, parent WR {sub.is_win.mean():.4f} ===')
        if n == 0: continue

        X = sub[FACTORS].values
        y = sub['is_win'].astype(bool).values

        min_leaf = max(int(n * 0.05), 1000)  # at least 5% per leaf, min 1000 trades
        tree = DecisionTreeClassifier(
            max_leaf_nodes=MAX_LEAVES,
            min_samples_leaf=min_leaf,
            criterion='gini',
            random_state=42,
        )
        tree.fit(X, y)

        # assign leaf id per trade
        leaf_ids = tree.apply(X)
        # Map raw sklearn leaf ids -> consecutive 0..K-1 by leaf WR (so 0 = worst, K-1 = best)
        leaf_stats = {}
        for lid in np.unique(leaf_ids):
            mask = (leaf_ids == lid)
            leaf_stats[lid] = {
                'n': int(mask.sum()),
                'wins': int(y[mask].sum()),
                'wr': float(y[mask].mean()),
            }
        # sort by wr ascending
        sorted_lids = sorted(leaf_stats.keys(), key=lambda x: leaf_stats[x]['wr'])
        lid_to_sub = {lid: i for i, lid in enumerate(sorted_lids)}
        sub['sub_regime'] = [f'{parent_regime}_{lid_to_sub[l]}' for l in leaf_ids]

        # Reconstruct path-to-leaf rules
        t = tree.tree_
        def walk(node, path):
            if t.children_left[node] == _tree.TREE_LEAF:
                yield node, path; return
            feat = FACTORS[t.feature[node]]
            thr = float(t.threshold[node])
            yield from walk(t.children_left[node], path + [(feat, '<=', thr)])
            yield from walk(t.children_right[node], path + [(feat, '>', thr)])
        leaf_rules = {leaf: path for leaf, path in walk(0, [])}

        # Print + collect
        print(f'  min_samples_leaf={min_leaf:,}  n_leaves={len(sorted_lids)}')
        print(f'  {"sub_id":7s} {"n":>10s} {"%":>6s} {"wins":>8s} {"wr":>6s}  rule (path)')
        for lid in sorted_lids:
            stats = leaf_stats[lid]
            new_id = lid_to_sub[lid]
            rule = ' AND '.join(f'{f}{op}{v:.6g}' for f,op,v in leaf_rules.get(lid, []))
            row = {
                'parent_regime':  parent_regime,
                'sub_regime':     f'{parent_regime}_{new_id}',
                'sub_id':         new_id,
                'n_trades':       stats['n'],
                'pct_of_parent':  round(stats['n']/n, 4),
                'wins':           stats['wins'],
                'losses':         stats['n'] - stats['wins'],
                'wr':             round(stats['wr'], 5),
                'wr_lift_vs_parent': round(stats['wr'] - sub.is_win.mean(), 5),
                'rule':           rule,
            }
            results.append(row)
            print(f'  {parent_regime}_{new_id:<5d} {stats["n"]:>10,} {stats["n"]/n*100:5.1f}% {stats["wins"]:>8,} {stats["wr"]:6.3%}  {rule[:80]}{"..." if len(rule)>80 else ""}')

        # Validation stats
        wrs = [leaf_stats[lid]['wr'] for lid in sorted_lids]
        ns = [leaf_stats[lid]['n'] for lid in sorted_lids]
        print(f'\n  WR range across sub-regimes: {min(wrs):.3%} -> {max(wrs):.3%}  (spread {max(wrs)-min(wrs):.3%})')
        print(f'  size range: {min(ns):,} -> {max(ns):,}  (ratio {max(ns)/min(ns):.1f}x)')

    rdf = pd.DataFrame(results)
    rdf.to_csv(OUT / 'c0102_sub_regime_definitions.csv', index=False)
    print(f'\n[write] {OUT/"c0102_sub_regime_definitions.csv"}')

if __name__ == '__main__':
    main()
