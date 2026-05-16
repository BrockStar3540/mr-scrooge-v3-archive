#!/usr/bin/env python3
"""
Per-cell management diagnostic (mfe/mae in R-units, properly converted from pips).

Cell key: (strategy_id, pair, direction, technical_regime_53)
For each cell, compute:
  - n, wins, losses, wr
  - mfe in R: p25, p50, p75, p90 (max favorable excursion as multiple of stop)
  - mae in R: p50, p75 (max adverse excursion as multiple of stop)
  - giveback_rate_in_winners: pct of winning trades where mfe>=1.5R but realized<1.5R
  - missed_runner_rate_in_losers: pct of LOSING trades where mfe>=0.5R (went green then died)
  - missed_1R_runner_rate: pct of losers where mfe>=1.0R (the textbook BE candidates)
  - runaway_rate: pct of winners with mfe>=2.5R (long-runners)
  - drawdown_severity: median mae_R for winners (how deep did winners go negative first)

Output: per_cell_mgmt_stats.csv
"""
from __future__ import annotations
import time
from pathlib import Path
import numpy as np
import pandas as pd
import pyarrow.parquet as pq

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
CORPUS = ROOT / 'all_strategies_all_pairs_trades.parquet'
OUT = ROOT / 'seed-family-factory'

def main():
    t0 = time.time()
    cols = ['strategy_id','pair','direction','technical_regime_53','is_win',
            'realized_R','mfe_R','mae_R','entry_price','stop_loss','exit_reason']
    print(f'[load] {CORPUS}')
    df = pq.read_table(CORPUS, columns=cols).to_pandas()
    print(f'  rows: {len(df):,}  ({time.time()-t0:.1f}s)')

    # Convert mfe/mae from pips to R-units
    df['pip_size'] = np.where(df.pair.str.contains('JPY'), 0.01, 0.0001)
    df['stop_pips'] = (df.entry_price - df.stop_loss).abs() / df.pip_size
    df['mfe_R_units'] = df.mfe_R / df.stop_pips.replace(0, np.nan)
    df['mae_R_units'] = df.mae_R / df.stop_pips.replace(0, np.nan)

    print('[aggregate per cell at n>=50]')
    rows = []
    for key, cell in df.groupby(['strategy_id','pair','direction','technical_regime_53'], sort=False):
        cell = cell.dropna(subset=['mfe_R_units','mae_R_units','realized_R','is_win'])
        n = len(cell)
        if n < 50: continue
        wins = cell[cell['is_win']==True]
        losses = cell[cell['is_win']==False]
        n_w = len(wins); n_l = len(losses)
        if n_w < 5 or n_l < 10: continue

        def q(s, p): return float(s.quantile(p)) if len(s) >= 10 else float('nan')

        mfe_w = wins.mfe_R_units; mae_w = wins.mae_R_units
        mfe_l = losses.mfe_R_units; mae_l = losses.mae_R_units
        rR = cell.realized_R

        # Critical management signals:
        missed_runner_05 = (mfe_l >= 0.5).sum() / max(n_l, 1)     # losers that went green
        missed_runner_10 = (mfe_l >= 1.0).sum() / max(n_l, 1)     # losers that hit 1R
        missed_runner_15 = (mfe_l >= 1.5).sum() / max(n_l, 1)
        runaway_25 = (mfe_w >= 2.5).sum() / max(n_w, 1)            # long-runners
        runaway_30 = (mfe_w >= 3.0).sum() / max(n_w, 1)
        giveback_w = ((mfe_w >= 1.5) & (wins.realized_R < 1.5)).sum() / max(n_w, 1)
        mae_p75_w = q(mae_w, 0.75)                                  # drawdown before winners

        rows.append({
            'strategy_id': key[0], 'pair': key[1], 'direction': key[2], 'technical_regime_53': key[3],
            'n': n, 'wins': n_w, 'losses': n_l, 'wr': round(n_w/n, 4),
            'mean_realized_R': round(rR.mean(), 4),
            'sum_R': round(rR.sum(), 1),
            # winner MFE distribution
            'win_mfe_p25': round(q(mfe_w, 0.25), 3),
            'win_mfe_p50': round(q(mfe_w, 0.50), 3),
            'win_mfe_p75': round(q(mfe_w, 0.75), 3),
            'win_mfe_p90': round(q(mfe_w, 0.90), 3),
            # winner MAE (drawdown before win) -- key for BE setting
            'win_mae_p50': round(q(mae_w, 0.50), 3),
            'win_mae_p75': round(q(mae_w, 0.75), 3),
            'win_mae_p90': round(q(mae_w, 0.90), 3),
            # loser MFE (how high the doomed went)
            'lose_mfe_p50': round(q(mfe_l, 0.50), 3),
            'lose_mfe_p75': round(q(mfe_l, 0.75), 3),
            # Key management signals
            'missed_runner_05R': round(missed_runner_05, 3),
            'missed_runner_10R': round(missed_runner_10, 3),
            'missed_runner_15R': round(missed_runner_15, 3),
            'runaway_25R':       round(runaway_25, 3),
            'runaway_30R':       round(runaway_30, 3),
            'giveback_winners':  round(giveback_w, 3),
        })

    out_df = pd.DataFrame(rows)
    out_csv = OUT / 'per_cell_mgmt_stats.csv'
    out_df.to_csv(out_csv, index=False)
    print(f'[write] {out_csv}  ({len(out_df):,} cells, {time.time()-t0:.1f}s)')

    print()
    print('=== AGGREGATE: averaged across all cells ===')
    for c in ['win_mfe_p50','win_mfe_p75','win_mae_p75','lose_mfe_p50',
              'missed_runner_05R','missed_runner_10R','missed_runner_15R',
              'runaway_25R','giveback_winners']:
        print(f'  {c:<25s} {out_df[c].mean():.4f}')

    print()
    print('=== TOP 15 cells where missed_runner_10R rate is highest (best BE candidates) ===')
    top_bad = out_df[out_df.losses >= 50].sort_values('missed_runner_10R', ascending=False).head(15)
    print(top_bad[['strategy_id','pair','direction','technical_regime_53','n','losses','win_mae_p75','missed_runner_10R','missed_runner_15R']].to_string())
    print()
    print('=== TOP 15 cells with highest runaway rate (NEED to let winners run) ===')
    top_run = out_df[out_df.wins >= 20].sort_values('runaway_25R', ascending=False).head(15)
    print(top_run[['strategy_id','pair','direction','technical_regime_53','n','wins','wr','win_mfe_p50','win_mfe_p75','runaway_25R','runaway_30R']].to_string())

if __name__ == '__main__':
    main()
