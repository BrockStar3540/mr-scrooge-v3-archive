#!/usr/bin/env python3
"""
upgrade_seed_family_artifacts.py

Post-hoc upgrades to the seed-family factory output:
  1. Add wr_lift_vs_seed / mean_R_lift_vs_seed columns to lineage by joining
     the original 141-seed bank's WR and mean_R per parent_seed_id
  2. Build seed_regime_coverage_matrix.csv  (which regimes are rich vs sparse)
  3. Overlap-dedup winner-side artifacts: drop near-duplicate siblings
     (same factor_signature + n within +/- 10% + wr within +/- 5pp) keeping
     the strongest one
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
OUT  = ROOT / 'seed-family-factory'
SEED_BANK = ROOT / 'winner_island_sibling_seed_bank.csv'

# --- Load existing artifacts ----------------------------------------------
print('[load] seed bank + lineage')
seeds = pd.read_csv(SEED_BANK).reset_index(drop=True)
seeds['parent_seed_id'] = [f's{i+1:04d}' for i in seeds.index]
seed_lookup = seeds.set_index('parent_seed_id')[['n','wins','losses','wr','mean_R']].rename(
    columns={'n':'seed_base_n','wins':'seed_base_wins','losses':'seed_base_losses',
             'wr':'seed_base_wr','mean_R':'seed_base_mean_R'})

lineage = pd.read_csv(OUT / 'seed_family_lineage.csv')
print(f'  lineage rows: {len(lineage):,}')

# --- 1) Add lift-vs-seed columns ------------------------------------------
print('[upgrade 1] add wr_lift_vs_seed / mean_R_lift_vs_seed')
lineage = lineage.merge(seed_lookup, left_on='parent_seed_id', right_index=True, how='left')
lineage['wr_lift_vs_seed'] = lineage['wr'] - lineage['seed_base_wr']
lineage['mean_R_lift_vs_seed'] = lineage['mean_R'] - lineage['seed_base_mean_R']
lineage['wr_lift_vs_parent'] = lineage['wr']  # placeholder, parent_wr not in lineage
# we need parent_wr from elsewhere; compute later if needed

# --- 2) Coverage matrix ---------------------------------------------------
print('[upgrade 2] build seed_regime_coverage_matrix.csv')
def regime_summary(g):
    n = len(g)
    return pd.Series({
        'seed_count':         n,
        'winner_seed_count':  int((g['bucket']=='winner_seed').sum()),
        'near_pure_count':    int((g['bucket']=='near_pure_seed').sum()),
        'false_friend_count': int((g['bucket']=='false_friend_sibling').sum()),
        'reject_count':       int((g['bucket']=='child_reject').sum()),
        'distinct_pairs':     g['pair'].nunique(),
        'distinct_strategies':g['strategy_id'].nunique(),
        'distinct_root_strategies': g['root_strategy_id'].nunique(),
        'long_count':         int((g['direction']=='long').sum()),
        'short_count':        int((g['direction']=='short').sum()),
        'mean_wr':            round(g['wr'].mean(), 4),
        'mean_lift_vs_seed':  round(g['wr_lift_vs_seed'].mean(), 4) if 'wr_lift_vs_seed' in g.columns else 0.0,
    })

cov = lineage.groupby('technical_regime_53').apply(regime_summary).reset_index()
cov = cov.sort_values('winner_seed_count', ascending=False)
cov_path = OUT / 'seed_regime_coverage_matrix.csv'
cov.to_csv(cov_path, index=False)
print(f'  wrote {cov_path}  ({len(cov)} regimes)')

# --- 3) Overlap dedup -----------------------------------------------------
print('[upgrade 3] overlap-dedup on winner-side rows')
keep_buckets = ['winner_seed','near_pure_seed','false_friend_sibling']
keepable = lineage[lineage['bucket'].isin(keep_buckets)].copy()
print(f'  pre-dedup keepable: {len(keepable):,}')

# Group by (parent_seed_id, factor_signature). Within each group, sort by
# survival_score desc and drop near-duplicates where (n within +/-10%, wr within +/-5pp).
def dedup_group(g):
    g = g.sort_values('seed_survival_score', ascending=False).reset_index(drop=True)
    keep_idx = []
    for i, row in g.iterrows():
        is_dup = False
        for k in keep_idx:
            k_row = g.iloc[k]
            same_n = abs(row['n'] - k_row['n']) <= 0.10 * max(k_row['n'], 1)
            same_wr = abs(row['wr'] - k_row['wr']) <= 0.05
            if same_n and same_wr:
                is_dup = True
                break
        if not is_dup:
            keep_idx.append(i)
    return g.iloc[keep_idx]

kept = keepable.groupby(['parent_seed_id','factor_signature'], group_keys=False).apply(dedup_group)
print(f'  post-dedup keepable: {len(kept):,}')

# Tag dedupe status in full lineage
lineage['is_dup_of_better_sibling'] = False
dup_ids = set(keepable['seed_id']) - set(kept['seed_id'])
lineage.loc[lineage['seed_id'].isin(dup_ids), 'is_dup_of_better_sibling'] = True

# --- Write upgraded artifacts ---------------------------------------------
upgraded_path = OUT / 'seed_family_lineage_v2.csv'
lineage.to_csv(upgraded_path, index=False)
print(f'[write] {upgraded_path}  ({len(lineage):,} rows, {len(dup_ids):,} marked duplicate)')

# Coverage matrix preview
print()
print('=== seed_regime_coverage_matrix top 15 ===')
print(cov.head(15).to_string())
