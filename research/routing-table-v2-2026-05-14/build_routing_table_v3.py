#!/usr/bin/env python3
"""Build routing_table_v3 from OOS-validated A-survivors.

Selection criterion: oos_status == 'ok' AND A_post_WR >= 0.25 AND A_n_kept >= 20
                     (~157 cells with proven holdout edge from 2026-05-15 OOS run).

Schema mirrors routing_table_v2 + adds:
  - shave_rule         : per-cell entry filter (the deployable artifact for stage 2)
  - oos_test_n         : test_n on holdout
  - oos_test_post_WR   : holdout post_WR with the shave rule applied
  - oos_lift_retention : test_lift / in_sample_lift  (close to 1.0 = preserved)

Writes data/routing_table_v3.parquet + .csv + summary md.
Does NOT flip the live config — Brock can swap routing_table_path manually.
"""
from __future__ import annotations
import datetime as dt
from pathlib import Path
import pandas as pd

ROOT = Path('/home/ubuntu/mr-scrooge-v3')
OOS_CSV = ROOT / 'research' / 'routing-table-v2-2026-05-14' / 'oos_validation_strong_islands.csv'
OUT_PARQ = ROOT / 'data' / 'routing_table_v3.parquet'
OUT_CSV  = ROOT / 'data' / 'routing_table_v3.csv'
OUT_MD   = ROOT / 'data' / 'routing_table_v3_summary.md'

# regime53 -> human description (from features/technical_regime_53.py)
REGIME_DESC = {
    'M01':'stop_hunt_up_high_adx','M02':'stop_hunt_up_low_adx','M03':'stop_hunt_dn_high_adx','M04':'stop_hunt_dn_low_adx',
    'F01':'false_break_up_strong_trend','F02':'false_break_up','F03':'false_break_dn_strong_trend','F04':'false_break_dn',
    'B01':'breakout_up_high_vol_trend','B02':'breakout_up_strong_adx_low_vol','B03':'breakout_up_moderate_adx','B04':'breakout_up_weak',
    'B05':'breakout_dn_high_vol_trend','B06':'breakout_dn_strong_adx_low_vol','B07':'breakout_dn_moderate_adx','B08':'breakout_dn_weak',
    'C01':'tight_coil_low_adx','C02':'tight_coil_adx','C03':'compressed_bb_active_atr_low_adx','C04':'compressed_bb_active_atr_adx',
    'X01':'expansion_strong_uptrend','X02':'expansion_strong_downtrend','X03':'expansion_strong_adx_flat','X04':'expansion_moderate_trend','X05':'expansion_no_trend',
    'T01':'strong_uptrend_extended','T02':'strong_uptrend_room','T03':'strong_downtrend_extended','T04':'strong_downtrend_room',
    'T05':'moderate_uptrend','T06':'moderate_downtrend','T07':'directional_drift_flat',
    'O01':'overbought_range','O02':'overbought_trend_caution','O03':'oversold_range','O04':'oversold_trend_caution',
    'O05':'moderately_overbought','O06':'moderately_oversold',
    'R01':'wide_volatile_range','R02':'wide_quiet_range','R03':'normal_range','R04':'tight_range',
    'S01':'quiet_asia','S02':'active_asia','S03':'volatile_asia','S04':'london_midrange_drift','S05':'quiet_ny','S06':'active_ny',
    'Z01':'catch_all',
}

# Strategy -> family map (textbook by prefix + V3 probes).
# Reuses the conventions established in routing_table_v2.
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
    # textbook by prefix
    if strategy_id.startswith('TF'): return 'dbb_trend'
    if strategy_id.startswith('MR'): return 'reversal'
    if strategy_id.startswith('SS'): return 'reversal'
    if strategy_id.startswith('BR'): return 'direct'
    if strategy_id.startswith('CP'): return 'direct'
    if strategy_id.startswith('MO'): return 'direct'
    return 'direct'  # fallback

def r_target_for(strategy_id: str) -> float:
    return 1.5 if strategy_id in FADE_R_15 else 2.0

def main():
    print(f'[load] {OOS_CSV}')
    o = pd.read_csv(OOS_CSV)
    print(f'  rows: {len(o)}')

    survivors = o[
        (o['oos_status'] == 'ok') &
        (o['A_post_WR'] >= 0.25) &
        (o['A_n_kept']  >= 20)
    ].copy()
    print(f'  A-survivors (>=25% test post_WR, n_kept>=20): {len(survivors)}')

    rows = []
    now_iso = dt.datetime.now(dt.timezone.utc).isoformat()
    for _, isl in survivors.iterrows():
        strategy = isl['strategy_id']
        family   = family_for(strategy)
        r_target = r_target_for(strategy)
        # Score boost: relative lift on holdout (A_post_WR / test_pre_WR), clipped [0.5, 2.0].
        # Mirrors v2's score_boost range (0.6-1.2 typical, up to 1.5+).
        test_pre = isl['test_pre_WR'] if isl['test_pre_WR'] and isl['test_pre_WR'] > 0 else 0.10
        relative_lift = float(isl['A_post_WR']) / float(test_pre)
        score_boost = max(0.5, min(2.0, relative_lift - 1.0))
        # Estimated mean_R from holdout wr + r_target: wr*r_target - (1-wr)*1
        wr = float(isl['A_post_WR'])
        mean_R_est = wr * r_target - (1.0 - wr)
        n_kept = int(isl['A_n_kept'])
        w_kept = int(isl['A_w_kept'])
        rows.append({
            'technical_regime_53':   isl['regime'],
            'technical_regime_desc': REGIME_DESC.get(isl['regime'], 'unknown'),
            'pair':                  isl['pair'],
            'session_bucket':        isl['session'],
            'strategy':              strategy,
            'family':                family,
            'direction':             isl['direction'],
            'r_target':              r_target,
            'score_boost':           round(score_boost, 3),
            'n':                     n_kept,
            'wins':                  w_kept,
            'sum_R':                 round(mean_R_est * n_kept, 3),
            'mean_R':                round(mean_R_est, 3),
            'wr':                    round(wr, 3),
            'source':                'oos_validated_2026-05-15',
            'last_updated':          now_iso,
            # New v3 columns
            'shave_rule':            isl['rule'],
            'oos_test_n':            int(isl['test_n']),
            'oos_test_post_WR':      round(wr, 3),
            'oos_lift_retention':    round(float(isl['A_post_WR']) / float(isl['post_WR']), 3),
        })

    df = pd.DataFrame(rows)
    df.to_parquet(OUT_PARQ, index=False)
    df.to_csv(OUT_CSV, index=False)
    print(f'[write] {OUT_PARQ}  ({len(df)} rows)')
    print(f'[write] {OUT_CSV}')

    # Summary md
    md = []
    md.append('# routing_table_v3 summary')
    md.append('')
    md.append(f'**Built:** {now_iso}')
    md.append(f'**Source:** A-survivors from OOS validation (oos_validation_strong_islands.csv)')
    md.append(f'**Filter:** oos_status==ok AND A_post_WR>=0.25 AND A_n_kept>=20')
    md.append(f'**Rows:** {len(df)}')
    md.append(f'**Unique leaves (regime53 x pair x session):** {df.groupby(["technical_regime_53","pair","session_bucket"]).ngroups}')
    md.append('')
    md.append('## Compared to v2 (1,881 rows, 528 leaves)')
    md.append('')
    md.append(f'- v3 is **{len(df)/1881:.0%} the size** — much tighter cell list')
    md.append(f'- v3 is **OOS-validated**: every cell holds at test post_WR >= 0.25 on the 2025-01-01+ holdout')
    md.append(f'- v3 carries the deployable **shave_rule** per cell for stage-2 entry filtering')
    md.append('')
    md.append('## Family composition')
    md.append('')
    for fam, sub in df.groupby('family'):
        md.append(f'- **{fam}**: {len(sub)} cells')
    md.append('')
    md.append('## Direction composition')
    md.append('')
    for d, sub in df.groupby('direction'):
        md.append(f'- **{d}**: {len(sub)} cells')
    md.append('')
    md.append('## Top regimes')
    md.append('')
    top = df.groupby('technical_regime_53').size().sort_values(ascending=False).head(10)
    md.append('| regime | desc | cells |')
    md.append('|---|---|---:|')
    for r, n in top.items():
        md.append(f'| {r} | {REGIME_DESC.get(r,"unknown")} | {n} |')
    md.append('')
    md.append('## Top sessions')
    md.append('')
    for s, sub in df.groupby('session_bucket'):
        md.append(f'- {s}: {len(sub)} cells')
    md.append('')
    md.append('## Top strategies')
    md.append('')
    sgrp = df.groupby('strategy').size().sort_values(ascending=False).head(15)
    md.append('| strategy | family | cells |')
    md.append('|---|---|---:|')
    for s, n in sgrp.items():
        md.append(f'| {s} | {family_for(s)} | {n} |')
    md.append('')
    md.append('## To deploy live')
    md.append('')
    md.append('1. Verify the parquet loads: `python3 -c "from scrooge_v3.strategies.routing_table import RoutingTable; rt = RoutingTable(); rt.load(\"data/routing_table_v3.parquet\")"`')
    md.append('2. Update config: `strategies.routing_table_path = "data/routing_table_v3.parquet"`  (currently points to v2)')
    md.append('3. Restart `mr-scrooge-v3.service`')
    md.append('4. Confirm `[ROUTING_TABLE] loaded routing_table_v3.parquet — rows=N leaves=M` in journal')
    md.append('5. Existing routing_table_mode=hard will enforce the v3 cell list immediately')
    md.append('')
    md.append('## Stage-2 follow-on')
    md.append('')
    md.append('The shave_rule column is stored but NOT yet enforced by routing_table.py — it currently only attaches strategies. Stage 2 work: extend RoutingTable lookup to also return the per-cell rule, and add an entry-filter gate that evaluates the rule against current SymbolContext features. That work is independent of this ship.')
    OUT_MD.write_text('\n'.join(md))
    print(f'[write] {OUT_MD}')
    print()
    print('='*60)
    print(f'routing_table_v3: {len(df)} cells, {df.groupby(["technical_regime_53","pair","session_bucket"]).ngroups} leaves')
    print(f'Families: {df["family"].value_counts().to_dict()}')

if __name__ == '__main__':
    main()
