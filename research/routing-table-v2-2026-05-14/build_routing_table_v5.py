#!/usr/bin/env python3
"""Build routing_table_v4 from hybrid winner islands (+ loser-skip rules).

Input:
    research/ohlcv-strategy-library-v0/hybrid_winner_islands_6yr.csv
    research/ohlcv-strategy-library-v0/hybrid_loser_islands_6yr_top1.csv
    (probe versions appended once Phase A.2 finishes)

Output:
    data/routing_table_v4.parquet  +  .csv  +  _summary.md

Schema additions over v3:
    shave_rule       : winner-side entry filter (band-grammar conjunction)
    loser_skip_rule  : death-by-presence rule (mirrored loser island)
    depth, hold_wins, hold_losses : audit columns from the shaver
    window           : '6yr' or '6mo'

Selection criteria:
    winner islands: take top-1 per cell ranked by (losses asc, wr desc, wins desc, hold_wins desc)
    loser islands : keep as supplementary 'loser_skip_rule' column on the same cell;
                    if no winner island in that cell, emit a loser-only row with
                    strategy=None (the row is a pure veto, no attach).

Per Brock 2026-05-15: hybrid output supersedes islands_best_overall + the 261-island
OOS validation as the routing-table source of truth. The hybrid carries era split
(disc/holdout) so we can prefer hold_losses=0 cells as deployable.
"""
from __future__ import annotations
import datetime as dt
from pathlib import Path
import pandas as pd

ROOT = Path('/home/ubuntu/mr-scrooge-v3')
WIN_6YR  = ROOT / 'research' / 'ohlcv-strategy-library-v0' / 'hybrid_winner_islands_6yr.csv'
LOSE_6YR = ROOT / 'research' / 'ohlcv-strategy-library-v0' / 'hybrid_loser_islands_6yr_top1.csv'

PROBE_WIN_6YR  = ROOT / 'research' / 'ohlcv-strategy-library-v0' / 'hybrid_probe_winner_islands_6yr_top1.csv'
PROBE_LOSE_6YR = ROOT / 'research' / 'ohlcv-strategy-library-v0' / 'hybrid_probe_loser_islands_6yr_top1.csv'
OUT_PARQ = ROOT / 'data' / 'routing_table_v5.parquet'
OUT_CSV  = ROOT / 'data' / 'routing_table_v5.csv'
OUT_MD   = ROOT / 'data' / 'routing_table_v5_summary.md'

# Regime53 desc map (same as v3 builder)
REGIME_DESC = {
    'C01':'tight_coil_low_adx','C02':'tight_coil_adx','C03':'compressed_bb_active_atr_low_adx','C04':'compressed_bb_active_atr_adx',
    'O01':'overbought_range','O02':'overbought_trend_caution','O03':'oversold_range','O04':'oversold_trend_caution',
    'O05':'moderately_overbought','O06':'moderately_oversold',
    'B01':'breakout_up_high_vol_trend','B02':'breakout_up_strong_adx_low_vol','B03':'breakout_up_moderate_adx','B04':'breakout_up_weak',
    'B05':'breakout_dn_high_vol_trend','B06':'breakout_dn_strong_adx_low_vol','B07':'breakout_dn_moderate_adx','B08':'breakout_dn_weak',
    'T01':'strong_uptrend_extended','T02':'strong_uptrend_room','T03':'strong_downtrend_extended','T04':'strong_downtrend_room',
    'T05':'moderate_uptrend','T06':'moderate_downtrend','T07':'directional_drift_flat',
    'R01':'wide_volatile_range','R02':'wide_quiet_range','R03':'normal_range','R04':'tight_range',
    'X01':'expansion_strong_uptrend','X02':'expansion_strong_downtrend','X03':'expansion_strong_adx_flat','X04':'expansion_moderate_trend','X05':'expansion_no_trend',
    'M01':'stop_hunt_up_high_adx','M02':'stop_hunt_up_low_adx','M03':'stop_hunt_dn_high_adx','M04':'stop_hunt_dn_low_adx',
    'F01':'false_break_up_strong_trend','F02':'false_break_up','F03':'false_break_dn_strong_trend','F04':'false_break_dn',
    'S01':'quiet_asia','S02':'active_asia','S03':'volatile_asia','S04':'london_midrange_drift','S05':'quiet_ny','S06':'active_ny',
    'Z01':'catch_all',
}

PROBE_FAMILY = {
    'alpha_pullback_v2':'dbb_trend','charlie_pullback_continuation_v2':'dbb_trend',
    'bravo_expansion_continuation':'dbb_trend','alpha_breakout_retest_v2':'direct',
    'charlie_compression_breakout':'direct','delta_tag_and_go_v2':'direct',
    'alpha_extended_fade_v2':'reversal','echo_box_fade_v2':'reversal',
    'echo_failed_breakout_v2':'reversal','bravo_failed_momentum':'reversal',
}
FADE_R_15 = {'alpha_extended_fade_v2','echo_box_fade_v2','echo_failed_breakout_v2','bravo_failed_momentum'}

def family_for(strategy_id: str) -> str:
    if strategy_id in PROBE_FAMILY: return PROBE_FAMILY[strategy_id]
    if strategy_id.startswith('TF'): return 'dbb_trend'
    if strategy_id.startswith('MR'): return 'reversal'
    if strategy_id.startswith('SS'): return 'reversal'
    if strategy_id.startswith('BR'): return 'direct'
    if strategy_id.startswith('CP'): return 'direct'
    if strategy_id.startswith('MO'): return 'direct'
    return 'direct'

def r_target_for(strategy_id: str) -> float:
    return 1.5 if strategy_id in FADE_R_15 else 2.0

def main():
    print(f'[load] {WIN_6YR}')
    w_text = pd.read_csv(WIN_6YR)
    print(f'  textbook winner islands: {len(w_text):,}')
    print(f'[load] {LOSE_6YR}')
    l_text = pd.read_csv(LOSE_6YR)
    print(f'  textbook loser islands: {len(l_text):,}')

    if PROBE_WIN_6YR.exists():
        w_probe = pd.read_csv(PROBE_WIN_6YR)
        print(f'  probe winner islands:    {len(w_probe):,}')
    else:
        w_probe = pd.DataFrame()
        print('  probe winners NOT FOUND (phase A.2 not finished?)')
    if PROBE_LOSE_6YR.exists():
        l_probe = pd.read_csv(PROBE_LOSE_6YR)
        print(f'  probe loser islands:     {len(l_probe):,}')
    else:
        l_probe = pd.DataFrame()
        print('  probe losers NOT FOUND')

    w = pd.concat([w_text, w_probe], ignore_index=True) if not w_probe.empty else w_text
    l = pd.concat([l_text, l_probe], ignore_index=True) if not l_probe.empty else l_text
    print(f'  combined: {len(w):,} winners / {len(l):,} losers')

    cell_keys = ['strategy_id','pair','direction','technical_regime_53']

    # session_bucket: derive from rule if it has session_bucket clause, else from
    # the parent cell's dominant hour (skip for now; sessions are inside the rule itself).
    # For routing-table purposes, sessions are part of the rule; the gate handles it.
    # Default session_bucket to '*' meaning any.
    # NOTE: when session_bucket is in the rule, the gate enforces it; we don't need
    # to also key the routing table on session. Skip session keying for v4 simplicity.
    # ACTUALLY: the existing RoutingTable schema requires session_bucket as part of the
    # cell key. To preserve compatibility, we emit one row per (rule's session) if
    # the rule has session_bucket==X, else one row per session ('any').

    def extract_session(rule: str):
        for clause in rule.split(' AND '):
            c = clause.strip()
            if c.startswith('session_bucket=='):
                return c.split('==', 1)[1].strip()
        return None

    # winner side: one row per cell (top-1 ranked: losses asc, wr desc, wins desc, hold_wins desc, mean_R desc)
    w_sorted = w.sort_values(['losses','wr','wins','hold_wins','mean_R'],
                             ascending=[True, False, False, False, False])
    w_top = w_sorted.drop_duplicates(subset=cell_keys, keep='first').copy()
    print(f'  winner cells (top-1 per parent): {len(w_top)}')

    # build cell-keyed dicts for loser overlay
    l_indexed = {tuple(r[c] for c in cell_keys): r for _, r in l.iterrows()}

    now = dt.datetime.now(dt.timezone.utc).isoformat()
    rows = []

    for _, isl in w_top.iterrows():
        rule = isl['rule']
        session_from_rule = extract_session(rule)
        sessions = [session_from_rule] if session_from_rule else ['asia','asia_late','london_open','ny_open','ny_mid','ny_close','off_hours']

        key = tuple(isl[c] for c in cell_keys)
        loser = l_indexed.get(key)
        loser_rule = str(loser['rule']) if loser is not None else None

        for sess in sessions:
            rows.append({
                'technical_regime_53':   isl['technical_regime_53'],
                'technical_regime_desc': REGIME_DESC.get(isl['technical_regime_53'], 'unknown'),
                'pair':                  isl['pair'],
                'session_bucket':        sess,
                'strategy':              isl['strategy_id'],
                'family':                family_for(isl['strategy_id']),
                'direction':             isl['direction'],
                'r_target':              r_target_for(isl['strategy_id']),
                'score_boost':           round(min(2.0, max(0.5, isl['wr'] / max(0.05, isl['parent_wr']) - 1.0)), 3),
                'n':                     int(isl['n']),
                'wins':                  int(isl['wins']),
                'sum_R':                 round(float(isl['mean_R']) * int(isl['n']), 3),
                'mean_R':                round(float(isl['mean_R']), 3),
                'wr':                    round(float(isl['wr']), 4),
                'source':                'hybrid_v5_winner',
                'last_updated':          now,
                # v4 additions
                'shave_rule':            rule,
                'loser_skip_rule':       loser_rule,
                'depth':                 int(isl['depth']),
                'hold_wins':             int(isl['hold_wins']),
                'hold_losses':           int(isl['hold_losses']),
                'window':                '6yr',
            })

    df = pd.DataFrame(rows)
    df.to_parquet(OUT_PARQ, index=False)
    df.to_csv(OUT_CSV, index=False)
    print(f'[write] {OUT_PARQ}  ({len(df)} rows)')
    print(f'[write] {OUT_CSV}')

    md = []
    md.append('# routing_table_v4 summary')
    md.append('')
    md.append(f'**Built:** {now}')
    md.append(f'**Source:** hybrid shaver winner_islands_6yr (top-1 per parent cell) + loser_islands_6yr_top1 overlay')
    md.append(f'**Schema additions over v3:** shave_rule, loser_skip_rule, depth, hold_wins, hold_losses, window')
    md.append(f'**Rows:** {len(df)}  (one per regime53 x pair x session)')
    md.append(f'**Distinct winner cells:** {len(w_top)}')
    md.append(f'**Cells with loser_skip_rule attached:** {df["loser_skip_rule"].notna().sum()}')
    md.append('')
    md.append('## Family breakdown')
    md.append('')
    for fam, sub in df.groupby('family'):
        md.append(f'- **{fam}**: {len(sub)} rows / {sub.drop_duplicates(subset=["technical_regime_53","pair","strategy"]).shape[0]} unique cells')
    md.append('')
    md.append('## Holdout-clean cells (hold_losses == 0)')
    md.append('')
    hc = df[df['hold_losses'] == 0]
    md.append(f'- {len(hc)} rows ({len(hc)/max(1,len(df)):.0%})')
    md.append('')
    md.append('## To deploy live')
    md.append('')
    md.append('1. Update config ')
    md.append('2. EntryFilterGate is now in src/scrooge_v3/gates/entry_filter_gate.py')
    md.append('   Wire in bootstrap.py after RegimeStrategyRouterGate in OBSERVE mode for first 24-48h')
    md.append('3. Restart mr-scrooge-v3.service; confirm gate logs')
    OUT_MD.write_text('\n'.join(md))
    print(f'[write] {OUT_MD}')

if __name__ == '__main__':
    main()
