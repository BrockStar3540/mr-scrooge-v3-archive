"""Synchrony check: raw-M5 v2 double-survivors vs textbook winners.

Compares the strongest raw-M5 v2 survivor cells against the daily textbook /
repaired-winner ledger. This is intentionally separate from the broad OHLCV
formula library: v2's proven axes are trigger x pair_family x direction x
session_quarter x M15 trend x H1 regime.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path('/home/ubuntu/mr-scrooge-v3')
V2 = ROOT / 'research/raw-m5-winner-factory-v2'
REG = ROOT / 'research/technical-regime-53-atlas-v1'
SURV = V2 / 'report_double_survivors.csv'
DAILY = REG / 'daily_textbook_trade_ledger_with_regime53_bartrue.parquet'
OUT = V2 / 'report_textbook_synchrony_double_survivors.csv'
SUMMARY = V2 / 'summary_textbook_synchrony.md'

# Bridge raw-M5 trigger IDs to the textbook strategy names where a direct
# semantic relationship exists.
TRIGGER_TO_TEXTBOOK = {
    'T1_bb_lower_reclaim': ['lower_band_reclaim_snapback_long', 'lower_rail_band_reentry_long'],
    'T2_bb_upper_reject': ['upper_band_rejection_snapback_short', 'upper_rail_band_reentry_short'],
    'T3_band_reentry_long': ['lower_band_reclaim_snapback_long', 'lower_rail_band_reentry_long'],
    'T4_band_reentry_short': ['upper_band_rejection_snapback_short', 'upper_rail_band_reentry_short'],
    'T7_pdl_proximity_reversal': ['pdl_rail_reversal_long'],
    'T7_pdh_proximity_reversal': ['pdh_rail_reversal_short'],
    'T8_pdl_failed_breakdown': ['failed_pdl_breakdown_long'],
    'T8_pdh_failed_breakout': ['failed_pdh_breakout_short'],
}


def main() -> None:
    surv = pd.read_csv(SURV)
    daily = pd.read_parquet(DAILY)
    repaired = daily[daily['record_type'].eq('repaired_winner')].copy()
    first = daily[daily['record_type'].eq('first_pass')].copy()

    # Exact-ish synchrony at available shared grain. Daily encyclopedia does not
    # carry M15/H1 labels, so those remain as survivor-side context only.
    grain = ['pair_family', 'direction', 'session_quarter']
    rep_all = repaired.groupby(grain).agg(
        repaired_winners=('ledger_id', 'size'),
        repaired_median_R=('realized_at_2R_net', 'median'),
        repaired_strategy_examples=('strategy_name', lambda x: '; '.join(x.value_counts().head(5).index.astype(str))),
    ).reset_index()
    first_all = first.groupby(grain).agg(
        first_pass_rows=('ledger_id', 'size'),
        first_pass_win_rate=('clean_2r', 'mean'),
        first_pass_mean_R=('realized_at_2R_net', 'mean'),
    ).reset_index()

    # Strategy-family synchrony: require the repaired strategy name to match the
    # raw trigger's semantic family.
    pieces = []
    for trigger, names in TRIGGER_TO_TEXTBOOK.items():
        sub = repaired[repaired['strategy_name'].isin(names)]
        if sub.empty:
            continue
        g = sub.groupby(grain).agg(
            matched_repaired_winners=('ledger_id', 'size'),
            matched_repaired_median_R=('realized_at_2R_net', 'median'),
            matched_strategy_examples=('strategy_name', lambda x: '; '.join(x.value_counts().head(5).index.astype(str))),
        ).reset_index()
        g['trigger_type'] = trigger
        pieces.append(g)
    matched = pd.concat(pieces, ignore_index=True) if pieces else pd.DataFrame(columns=grain + ['trigger_type'])

    out = surv.merge(rep_all, on=grain, how='left').merge(first_all, on=grain, how='left').merge(matched, on=['trigger_type'] + grain, how='left')
    for col in ['repaired_winners', 'first_pass_rows', 'matched_repaired_winners']:
        out[col] = out[col].fillna(0).astype(int)
    out['textbook_any_synchrony'] = out['repaired_winners'] > 0
    out['textbook_strategy_synchrony'] = out['matched_repaired_winners'] > 0
    out['same_structural_gate'] = ((out['h1_regime'] == 'breakout') & (((out['direction'] == 'long') & (out['m15_trend'] == 'up')) | ((out['direction'] == 'short') & (out['m15_trend'] == 'down'))))
    out['synchrony_score'] = (
        out['textbook_strategy_synchrony'].astype(int) * 3.0 +
        out['textbook_any_synchrony'].astype(int) * 1.0 +
        out['same_structural_gate'].astype(int) * 1.0 +
        np.minimum(out['matched_repaired_winners'], 25) / 12.5 +
        np.minimum(out['repaired_winners'], 100) / 100.0 +
        np.where(out['first_pass_win_rate'].fillna(0) > 0.30, 0.5, 0.0)
    )
    out = out.sort_values(['synchrony_score', 'mean_R_2r_hold', 'mean_R_2r_disc'], ascending=[False, False, False])
    out.to_csv(OUT, index=False)

    top = out.head(30)
    top_matched = out[out['textbook_strategy_synchrony']].head(30)
    with open(SUMMARY, 'w') as f:
        f.write('# Raw-M5 v2 Survivor x Textbook Synchrony\n\n')
        f.write('Compares v2 double-survivor cells against the repaired/textbook winner ledger. The shared grain is pair_family x session_quarter x direction, with trigger-to-strategy-family matching where possible.\n\n')
        f.write('## Coverage\n\n')
        f.write(f'- v2 double-survivor cells: {len(out):,}\n')
        f.write(f'- cells with any repaired-winner synchrony: {int(out["textbook_any_synchrony"].sum()):,}\n')
        f.write(f'- cells with trigger-matched repaired-winner synchrony: {int(out["textbook_strategy_synchrony"].sum()):,}\n')
        f.write(f'- cells with H1-breakout + M15-aligned structural gate: {int(out["same_structural_gate"].sum()):,}\n\n')
        f.write('## Top Trigger-Matched Synchrony\n\n')
        if len(top_matched):
            cols = ['trigger_type', 'pair_family', 'direction', 'session_quarter', 'm15_trend', 'h1_regime', 'n_disc', 'mean_R_2r_disc', 'n_hold', 'mean_R_2r_hold', 'matched_repaired_winners', 'matched_strategy_examples', 'repaired_winners']
            f.write(top_matched[cols].to_markdown(index=False))
        else:
            f.write('No trigger-matched synchrony found.\n')
        f.write('\n\n## Top Overall Synchrony\n\n')
        cols2 = ['trigger_type', 'pair_family', 'direction', 'session_quarter', 'm15_trend', 'h1_regime', 'n_disc', 'mean_R_2r_disc', 'n_hold', 'mean_R_2r_hold', 'synchrony_score', 'matched_repaired_winners', 'repaired_winners']
        f.write(top[cols2].to_markdown(index=False))
        f.write('\n\n## Interpretation\n\n')
        f.write('- Trigger-matched synchrony is strongest: blind v2 survivor and repaired winner use the same semantic setup family.\n')
        f.write('- Any repaired-winner synchrony means the same market-state pocket produced textbook winners even if the exact trigger name differs.\n')
        f.write('- The daily ledger lacks M15/H1 labels, so the H1-breakout + M15-aligned gate is verified from v2 survivor data, not from manual rows.\n')
    print(f'Wrote {OUT} and {SUMMARY}')


if __name__ == '__main__':
    main()
