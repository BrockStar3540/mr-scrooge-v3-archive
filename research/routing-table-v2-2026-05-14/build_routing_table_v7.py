#!/usr/bin/env python3
"""
build_routing_table_v7.py

Build routing_table_v7 from the 20,190 sub-regime islands.

Cell key: (sub_regime, pair, strategy, direction)
  -- session_bucket is dropped because it is implicitly encoded in sub_regime
     via hour_utc, which was a major splitter in the 40-leaf tree.

Selection criteria:
  - winner_rule must exist
  - winner_wr >= 0.33
  - winner_n  >= 30  (statistical confidence floor)

Output columns:
  sub_regime, parent_regime, pair, strategy, family, direction,
  r_target, score_boost, n, wins, sum_R, mean_R, wr, source, last_updated,
  shave_rule (= winner_rule),
  loser_skip_rule (= loser_rule when loss_rate >= 0.85),
  winner_lift, depth, parent_n, parent_wr
"""
from __future__ import annotations
import datetime as dt
from pathlib import Path
import pandas as pd

ROOT = Path('/home/ubuntu/mr-scrooge-v3')
IN_CSV = ROOT / 'research' / 'ohlcv-strategy-library-v0' / 'sub_regime_islands.csv'
OUT_PARQ = ROOT / 'data' / 'routing_table_v7.parquet'
OUT_CSV  = ROOT / 'data' / 'routing_table_v7.csv'
OUT_MD   = ROOT / 'data' / 'routing_table_v7_summary.md'

PROBE_FAMILY = {
    'alpha_pullback_v2':'dbb_trend','charlie_pullback_continuation_v2':'dbb_trend',
    'bravo_expansion_continuation':'dbb_trend','alpha_breakout_retest_v2':'direct',
    'charlie_compression_breakout':'direct','delta_tag_and_go_v2':'direct',
    'alpha_extended_fade_v2':'reversal','echo_box_fade_v2':'reversal',
    'echo_failed_breakout_v2':'reversal','bravo_failed_momentum':'reversal',
}
FADE_R_15 = {'alpha_extended_fade_v2','echo_box_fade_v2','echo_failed_breakout_v2','bravo_failed_momentum'}

def family_for(s):
    if s in PROBE_FAMILY: return PROBE_FAMILY[s]
    if s.startswith('TF'): return 'dbb_trend'
    if s.startswith('MR') or s.startswith('SS'): return 'reversal'
    if s.startswith('BR') or s.startswith('CP') or s.startswith('MO') or s.startswith('RG'): return 'direct'
    return 'direct'

def r_target_for(s):
    return 1.5 if s in FADE_R_15 else 2.0

def main():
    print(f'[load] {IN_CSV}')
    df = pd.read_csv(IN_CSV)
    print(f'  total cells: {len(df):,}')
    print(f'  with winner_rule: {df["winner_rule"].notna().sum():,}')

    # Selection
    sel = df[(df['winner_rule'].notna()) & (df['winner_wr'] >= 0.33) & (df['winner_n'] >= 30)].copy()
    print(f'  selected (wr>=0.33, n>=30): {len(sel):,}')

    sel['parent_regime'] = sel['sub_regime'].str.split('_').str[0]
    sel['family'] = sel['strategy_id'].map(family_for)
    sel['r_target'] = sel['strategy_id'].map(r_target_for)
    now_iso = dt.datetime.now(dt.timezone.utc).isoformat()

    rows = []
    sessions = ['asia','asia_late','london_open','ny_open','ny_mid','ny_close','off_hours']
    for _, r in sel.iterrows():
        winner_wr = float(r['winner_wr'])
        parent_wr = float(r['parent_wr'])
        r_target = float(r['r_target'])
        score_boost = max(0.5, min(2.0, (winner_wr / parent_wr - 1.0) if parent_wr > 0 else 0.5))
        mean_R_est = winner_wr * r_target - (1.0 - winner_wr)
        # Schema-compat: routing_table.py keys on (technical_regime_53, pair, session_bucket).
        # technical_regime_53 = parent_regime (C01/C02). Session expanded across all 7 buckets;
        # the shave_rule itself encodes sub-regime AND hour conditions so the EntryFilterGate
        # naturally enforces both at evaluate-time.
        for sess in sessions:
            rows.append({
                'sub_regime':            r['sub_regime'],
                'technical_regime_53':   r['parent_regime'],
                'technical_regime_desc': 'tight_coil_low_adx' if r['parent_regime']=='C01' else 'tight_coil_adx',
                'parent_regime':         r['parent_regime'],
                'session_bucket':        sess,
                'pair':                  r['pair'],
                'strategy':              r['strategy_id'],
                'family':                r['family'],
                'direction':             r['direction'],
                'r_target':              r_target,
                'score_boost':           round(score_boost, 3),
                'n':                     int(r['winner_n']),
                'wins':                  int(r['winner_wins']),
                'sum_R':                 round(mean_R_est * int(r['winner_n']), 3),
                'mean_R':                round(mean_R_est, 3),
                'wr':                    round(winner_wr, 4),
                'source':                'sub_regime_islands_v1',
                'last_updated':          now_iso,
                'shave_rule':            r['winner_rule'],
                'loser_skip_rule':       r['loser_rule'] if pd.notna(r.get('loser_rule')) and float(r.get('loser_lr', 0)) >= 0.85 else None,
                'winner_lift':           float(r['winner_lift']),
                'parent_n':              int(r['parent_n']),
                'parent_wr':             round(parent_wr, 4),
            })

    out = pd.DataFrame(rows)
    out.to_parquet(OUT_PARQ, index=False)
    out.to_csv(OUT_CSV, index=False)
    print(f'[write] {OUT_PARQ}  ({len(out):,} rows)')

    # Summary
    md = []
    md.append('# routing_table_v7 summary')
    md.append('')
    md.append(f'**Built:** {now_iso}')
    md.append(f'**Source:** sub_regime_islands.csv (Option B per-sub-regime mining)')
    md.append(f'**Selection:** winner_wr >= 0.33 (2:1 R break-even) AND winner_n >= 30 (sample-size floor)')
    md.append(f'**Cell key:** (sub_regime, pair, strategy, direction)  -- session_bucket dropped')
    md.append(f'**Rows:** {len(out):,}')
    md.append('')
    md.append('## Compared to v5')
    md.append('')
    md.append(f'- v5: 306 rows / 60 unique winner cells / keyed on (regime53, pair, session, strategy)')
    md.append(f'- v7: {len(out):,} rows / {out.drop_duplicates(subset=["sub_regime","pair","strategy","direction"]).shape[0]:,} unique winner cells / keyed on (sub_regime, pair, strategy, direction)')
    md.append('')
    md.append('## Family composition')
    md.append('')
    for fam, sub in out.groupby('family'):
        md.append(f'- **{fam}**: {len(sub):,} cells')
    md.append('')
    md.append('## Top sub-regimes by winner cells')
    md.append('')
    top_sr = out.groupby('sub_regime').size().sort_values(ascending=False).head(15)
    for sr, n in top_sr.items():
        md.append(f'- {sr}: {n} cells')
    md.append('')
    md.append('## Top strategies by winner cells')
    md.append('')
    top_st = out.groupby('strategy').size().sort_values(ascending=False).head(15)
    for st, n in top_st.items():
        md.append(f'- {st}: {n} cells')
    md.append('')
    md.append('## Cells with loser_skip_rule attached')
    md.append('')
    n_lsr = out['loser_skip_rule'].notna().sum()
    md.append(f'- {n_lsr:,} of {len(out):,} ({n_lsr/len(out)*100:.1f}%)')
    OUT_MD.write_text('\n'.join(md))
    print(f'[write] {OUT_MD}')

if __name__ == '__main__':
    main()
