"""Synchrony check: blind OHLCV survivors vs textbook/repaired winners.

Run after `backtest_ohlcv_strategy_library_v0.py --scope all` completes.
Compares blind candidate cells against the daily textbook trade encyclopedia
using the shared grain Brock cares about: regime x pair family x session x
direction. Strategy names are treated as supporting evidence, not required,
because formula strategy IDs and repaired-winner strategy names come from
different libraries.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path('/home/ubuntu/mr-scrooge-v3')
LIB = ROOT / 'research/ohlcv-strategy-library-v0'
REG = ROOT / 'research/technical-regime-53-atlas-v1'
CANDIDATES = LIB / 'candidate_strategy_regime_cells_all.csv'
DAILY = REG / 'daily_textbook_trade_ledger_with_regime53_bartrue.parquet'
OUT = LIB / 'candidate_textbook_synchrony_all.csv'
SUMMARY = LIB / 'summary_synchrony_all.md'
GRAIN = ['technical_regime_53', 'pair_family', 'session_bucket', 'direction']


def norm_session(s: pd.Series) -> pd.Series:
    return s.replace({'ny_pm': 'ny', 'overlap': 'ny', 'tokyo_only': 'asia', 'london_only': 'london', 'ny_only': 'ny'})


def main() -> None:
    if not CANDIDATES.exists():
        raise SystemExit(f'Missing {CANDIDATES}; run the blind strategy harness first')
    cand = pd.read_csv(CANDIDATES)
    if cand.empty:
        with open(SUMMARY, 'w') as f:
            f.write('# Candidate x Textbook Synchrony\n\nNo blind candidate cells existed, so no synchrony test was possible.\n')
        pd.DataFrame().to_csv(OUT, index=False)
        print('No blind candidates; wrote empty synchrony report')
        return
    daily = pd.read_parquet(DAILY)
    daily['session_bucket'] = norm_session(daily['session_bucket'])
    if 'session_bucket' not in cand.columns:
        cand['session_bucket'] = 'unknown'
    cand['session_bucket'] = norm_session(cand['session_bucket'])

    repaired = daily[daily['record_type'].eq('repaired_winner')].copy()
    first = daily[daily['record_type'].eq('first_pass')].copy()
    baseline_repaired_rate = len(repaired) / max(1, len(daily))

    rep_group = repaired.groupby(GRAIN).agg(
        repaired_winners=('ledger_id', 'size'),
        repaired_median_R=('realized_at_2R_net', 'median'),
        repaired_median_mfe=('mfe_r_net', 'median'),
        repaired_strategy_examples=('strategy_name', lambda x: '; '.join(x.value_counts().head(4).index.astype(str))),
    ).reset_index()
    all_group = daily.groupby(GRAIN).agg(
        textbook_rows=('ledger_id', 'size'),
    ).reset_index()
    fp_group = first.groupby(GRAIN).agg(
        first_pass_rows=('ledger_id', 'size'),
        first_pass_win_rate=('clean_2r', 'mean'),
        first_pass_mean_R=('realized_at_2R_net', 'mean'),
    ).reset_index()

    out = cand.merge(rep_group, on=GRAIN, how='left').merge(all_group, on=GRAIN, how='left').merge(fp_group, on=GRAIN, how='left')
    for col in ['repaired_winners', 'textbook_rows', 'first_pass_rows']:
        out[col] = out[col].fillna(0).astype(int)
    out['textbook_repaired_rate'] = np.where(out['textbook_rows'] > 0, out['repaired_winners'] / out['textbook_rows'], 0.0)
    out['manual_synchrony'] = out['repaired_winners'] > 0
    out['synchrony_enrichment'] = np.where(baseline_repaired_rate > 0, out['textbook_repaired_rate'] / baseline_repaired_rate, np.nan)
    out['synchrony_score'] = (
        out['manual_synchrony'].astype(int) * 2.0 +
        np.minimum(out['repaired_winners'], 50) / 25.0 +
        np.minimum(out['synchrony_enrichment'].fillna(0), 5.0) / 2.5 +
        (out['first_pass_win_rate'].fillna(0) > 0.30).astype(float)
    )
    out = out.sort_values(['synchrony_score', 'mean_R_holdout', 'repaired_winners'], ascending=[False, False, False])
    out.to_csv(OUT, index=False)

    synced = out[out['manual_synchrony']]
    with open(SUMMARY, 'w') as f:
        f.write('# Candidate x Textbook Synchrony\n\n')
        f.write('Compares blind OHLCV formula survivor cells against the daily textbook/repaired-winner ledger at regime x pair_family x session x direction grain.\n\n')
        f.write('## Coverage\n\n')
        f.write(f'- Blind candidate cells: {len(out):,}\n')
        f.write(f'- Candidate cells with repaired-winner synchrony: {len(synced):,}\n')
        f.write(f'- Baseline repaired-winner rate in daily ledger: {baseline_repaired_rate:.3f}\n\n')
        f.write('## Top Synchronized Candidates\n\n')
        if len(synced):
            cols = ['technical_regime_53', 'strategy_id', 'pair_family', 'session_bucket', 'direction', 'n', 'mean_R_holdout', 'profit_factor', 'repaired_winners', 'textbook_repaired_rate', 'synchrony_enrichment', 'repaired_strategy_examples']
            f.write(synced[cols].head(30).to_markdown(index=False))
        else:
            f.write('No blind candidate cells overlapped repaired-winner cells.\n')
        f.write('\n\n## Interpretation\n\n')
        f.write('- High synchrony means the blind formula survivor lands in the same market-state pocket as repaired/textbook winners.\n')
        f.write('- No synchrony does not automatically kill a blind candidate, but it lowers trust.\n')
        f.write('- Synchrony without blind survival remains a research clue, not a deployable strategy.\n')
    print(f'Wrote {OUT} and {SUMMARY}')


if __name__ == '__main__':
    main()
