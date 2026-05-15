#!/usr/bin/env python3
"""
prepare_probe_inputs.py — build probe-side corpus + parent universe.

Inputs:
  routing-table-v2/ml_training_corpus.parquet  (15.27M rows; has 481K V3 probe trades)

Outputs:
  seed-family-factory/probe_corpus.parquet      — probes only, plus derived
                                                  session_bucket + synthetic era
                                                  + price_pos alias of bb_position
  seed-family-factory/probe_parents.csv         — parent cell universe matching
                                                  test3_inside_regime_splits.csv schema,
                                                  with top1/top2/top3 factor priors
                                                  derived per-cell via Cohen's d
"""
from __future__ import annotations
import time
from pathlib import Path
import numpy as np
import pandas as pd
import pyarrow.parquet as pq

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
CORPUS_IN = ROOT / 'routing-table-v2' / 'ml_training_corpus.parquet'
OUT = ROOT / 'seed-family-factory'
OUT.mkdir(parents=True, exist_ok=True)

# Probe families (V3 trainer-built strategies)
PROBES = [
    'echo_box_fade_v2', 'echo_failed_breakout_v2',
    'alpha_pullback_v2', 'alpha_breakout_retest_v2', 'alpha_extended_fade_v2',
    'bravo_expansion_continuation', 'bravo_failed_momentum',
    'charlie_pullback_continuation_v2', 'charlie_compression_breakout',
    'delta_tag_and_go_v2',
]

FACTORS = ['ATR_ratio','BB_compress','RSI14','volume_ratio','ADX14','hour_utc','bb_position']

SESSION_OF = {h: ('asia' if 0<=h<4 else 'asia_late' if 4<=h<6 else 'london_open' if 6<=h<9
                  else 'ny_open' if 9<=h<13 else 'ny_mid' if 13<=h<17 else 'ny_close' if 17<=h<21
                  else 'off_hours') for h in range(24)}

MIN_CELL_N = 200

def cohens_d(w, l):
    nw, nl = len(w), len(l)
    if nw < 2 or nl < 2: return 0.0
    mw, ml = float(np.mean(w)), float(np.mean(l))
    vw, vl = float(np.var(w, ddof=1)), float(np.var(l, ddof=1))
    pooled = ((nw-1)*vw + (nl-1)*vl) / (nw + nl - 2)
    if pooled <= 0: return 0.0
    return (mw - ml) / np.sqrt(pooled)

def main():
    t0 = time.time()
    print(f'[load] {CORPUS_IN}')
    cols = ['source','strategy_id','pair','direction','entry_ts','is_win',
            'technical_regime_53','technical_regime_desc',
            'ATR_ratio','BB_compress','RSI14','volume_ratio','ADX14',
            'bb_position','hour_utc']
    df = pq.read_table(CORPUS_IN, columns=cols).to_pandas()
    print(f'  rows: {len(df):,}  ({time.time()-t0:.1f}s)')

    df = df[df['strategy_id'].isin(PROBES)].copy()
    print(f'  probe rows: {len(df):,}')

    # session_bucket
    df['session_bucket'] = df['hour_utc'].map(SESSION_OF)

    # synthetic era: sort by ts, last 20% = holdout
    df = df.sort_values('entry_ts').reset_index(drop=True)
    n_hold = int(len(df) * 0.2)
    df['era'] = 'discovery'
    df.loc[len(df)-n_hold:, 'era'] = 'holdout'

    # price_pos alias of bb_position (best proxy available in this corpus)
    df['price_pos'] = df['bb_position']

    # realized_R placeholder (we don't have actual R in ml corpus -- use synthetic)
    df['realized_R'] = np.where(df['is_win'], 1.5, -1.0)  # rough proxy

    # pair_family placeholder
    df['pair_family'] = df['pair'].apply(lambda p: 'jpy' if 'JPY' in p else 'usd_base' if p.startswith('USD') or p.endswith('USD') else 'cross')

    out_parquet = OUT / 'probe_corpus.parquet'
    df.to_parquet(out_parquet, index=False)
    print(f'[write] {out_parquet}  ({len(df):,} rows, {time.time()-t0:.1f}s)')

    # Build parent universe ----------------------------------------------
    print()
    print('[build] parent universe')
    key_cols = ['strategy_id','pair','direction','technical_regime_53']
    parents = []
    for key, sub in df.groupby(key_cols, sort=False):
        n = len(sub)
        if n < MIN_CELL_N: continue
        wins = int(sub['is_win'].sum()); losses = n - wins
        if wins < 10 or losses < 10: continue
        ds = {}
        for f in FACTORS:
            if f not in sub.columns: continue
            w = sub.loc[sub['is_win'], f].dropna().values
            l = sub.loc[~sub['is_win'], f].dropna().values
            ds[f] = abs(cohens_d(w, l))
        ranked = sorted(ds.items(), key=lambda x: x[1], reverse=True)
        top1, top2, top3 = (ranked + [(None,0.0)]*3)[:3]
        parents.append({
            'strategy_id': key[0], 'pair': key[1], 'direction': key[2], 'regime': key[3],
            'regime_desc': sub['technical_regime_desc'].iloc[0],
            'cell_n_total': n, 'cell_winners': wins, 'cell_losers': losses,
            'cell_wr': wins/n, 'cell_mean_R': float(sub['realized_R'].mean()),
            'top1_factor': top1[0], 'top1_d': round(top1[1],4),
            'top2_factor': top2[0], 'top2_d': round(top2[1],4),
            'top3_factor': top3[0], 'top3_d': round(top3[1],4),
            'split_rule': '',  # no prior split
            'split_n_train': 0, 'split_wr_train': 0.0, 'split_mean_R_train': 0.0,
            'split_n_test': 0,  'split_wr_test': 0.0,  'split_mean_R_test': 0.0,
            'split_ci_lo_test': 0.0, 'wr_lift_test': 0.0,
        })
    pdf = pd.DataFrame(parents)
    out_parents = OUT / 'probe_parents.csv'
    pdf.to_csv(out_parents, index=False)
    print(f'[write] {out_parents}  ({len(pdf)} parent cells, {time.time()-t0:.1f}s)')
    print()
    print('strategy_id parent counts:')
    print(pdf['strategy_id'].value_counts().to_string())
    print()
    print('top factor by frequency:')
    print(pdf['top1_factor'].value_counts().to_string())

if __name__ == '__main__':
    main()
