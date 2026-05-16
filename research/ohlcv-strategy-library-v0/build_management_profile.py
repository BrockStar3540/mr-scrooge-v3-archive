#!/usr/bin/env python3
"""
Build per-cell management profile from the per_cell_mgmt_stats.csv diagnostic.

For each (strategy_id, pair, direction, technical_regime_53) cell, derive
recommended knob values for BE / harvest / ratchet / favorable_exit.

Heuristics derived from the data (textbook 6.8yr corpus, mfe/mae in proper R-units):

  be_trigger_r:
    - if missed_runner_10R > 0.5  (more than half of losers hit 1R first) -> 0.5R  (move BE EARLY)
    - elif missed_runner_10R > 0.3 -> 0.7R
    - elif missed_runner_05R > 0.7 -> 0.6R
    - else -> 0.8R

  harvest_at_R (tp1 target):
    - if win_mfe_p50 < 1.2  (most winners barely make 1R) -> 0.8R  (take half EARLY)
    - elif win_mfe_p50 > 2.5 (winners run big)             -> 1.5R
    - else -> 1.0R  (default)

  ratchet_lock_pct:
    - if giveback_winners > 0.30 -> 0.65  (lock more, market chops)
    - elif runaway_25R > 0.40    -> 0.40  (let winners run)
    - else -> 0.50

  favorable_exit_threshold_r:
    - if giveback_winners > 0.40 -> 1.2R  (take green earlier on choppy cells)
    - else -> disabled (let ratchet handle it)

Output: management_profile.parquet
        keyed on (strategy_id, pair, direction, technical_regime_53)
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
IN_CSV = ROOT / 'seed-family-factory' / 'per_cell_mgmt_stats.csv'
OUT = ROOT / 'seed-family-factory'

def derive_knobs(r):
    mr10 = r['missed_runner_10R']; mr5 = r['missed_runner_05R']
    win_mfe_p50 = r['win_mfe_p50']; runaway = r['runaway_25R']
    giveback = r['giveback_winners']

    # be_trigger_r
    if pd.notna(mr10) and mr10 > 0.5: be_r = 0.5
    elif pd.notna(mr10) and mr10 > 0.3: be_r = 0.7
    elif pd.notna(mr5) and mr5 > 0.7: be_r = 0.6
    else: be_r = 0.8

    # harvest_at_R
    if pd.notna(win_mfe_p50) and win_mfe_p50 < 1.2: harvest_r = 0.8
    elif pd.notna(win_mfe_p50) and win_mfe_p50 > 2.5: harvest_r = 1.5
    else: harvest_r = 1.0

    # ratchet_lock_pct
    if pd.notna(giveback) and giveback > 0.30: ratchet_pct = 0.65
    elif pd.notna(runaway) and runaway > 0.40: ratchet_pct = 0.40
    else: ratchet_pct = 0.50

    # favorable_exit
    fav_exit_r = 1.2 if (pd.notna(giveback) and giveback > 0.40) else None

    return be_r, harvest_r, ratchet_pct, fav_exit_r

def main():
    print(f'[load] {IN_CSV}')
    df = pd.read_csv(IN_CSV)
    print(f'  cells: {len(df):,}')

    rows = []
    for _, r in df.iterrows():
        be_r, harvest_r, ratchet_pct, fav_exit_r = derive_knobs(r)
        rows.append({
            'strategy_id':         r['strategy_id'],
            'pair':                r['pair'],
            'direction':           r['direction'],
            'technical_regime_53': r['technical_regime_53'],
            'n':                   int(r['n']),
            'wr':                  float(r['wr']),
            # diagnostic context
            'missed_runner_10R':   r['missed_runner_10R'],
            'missed_runner_05R':   r['missed_runner_05R'],
            'win_mfe_p50':         r['win_mfe_p50'],
            'runaway_25R':         r['runaway_25R'],
            'giveback_winners':    r['giveback_winners'],
            # derived knobs
            'be_trigger_r':        be_r,
            'harvest_at_R':        harvest_r,
            'ratchet_lock_pct':    ratchet_pct,
            'favorable_exit_r':    fav_exit_r,
        })

    out_df = pd.DataFrame(rows)
    out_pq = OUT / 'management_profile.parquet'
    out_cs = OUT / 'management_profile.csv'
    out_df.to_parquet(out_pq, index=False)
    out_df.to_csv(out_cs, index=False)
    print(f'[write] {out_pq}  +  {out_cs}  ({len(out_df):,} cells)')
    print()
    print('=== Knob distribution across cells ===')
    print(f'be_trigger_r:')
    print(out_df['be_trigger_r'].value_counts().to_string())
    print()
    print(f'harvest_at_R:')
    print(out_df['harvest_at_R'].value_counts().to_string())
    print()
    print(f'ratchet_lock_pct:')
    print(out_df['ratchet_lock_pct'].value_counts().to_string())
    print()
    print(f'favorable_exit_r set: {out_df.favorable_exit_r.notna().sum()} / {len(out_df)}')

if __name__ == '__main__':
    main()
