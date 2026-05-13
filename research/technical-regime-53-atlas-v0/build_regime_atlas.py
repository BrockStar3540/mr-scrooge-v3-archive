from __future__ import annotations
import pandas as pd, numpy as np
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path('/home/ubuntu/mr-scrooge-v3/research/daily-textbook-trade-encyclopedia-v0/daily_textbook_trade_ledger.parquet')
OUT = Path('/home/ubuntu/mr-scrooge-v3/research/technical-regime-53-atlas-v0')
OUT.mkdir(parents=True, exist_ok=True)

DESC = {
'M01':'stop_hunt_up_high_adx','M02':'stop_hunt_up_low_adx','M03':'stop_hunt_dn_high_adx','M04':'stop_hunt_dn_low_adx',
'F01':'false_break_up_strong_trend','F02':'false_break_up','F03':'false_break_dn_strong_trend','F04':'false_break_dn',
'B01':'breakout_up_high_vol_trend','B02':'breakout_up_strong_trend','B03':'breakout_up_moderate','B04':'breakout_up_weak','B05':'breakout_dn_high_vol_trend','B06':'breakout_dn_strong_trend','B07':'breakout_dn_moderate','B08':'breakout_dn_weak',
'C01':'tight_coil_low_atr_low_adx','C02':'tight_coil_low_atr_trending','C03':'compression_low_adx','C04':'compression_trending',
'X01':'expansion_strong_uptrend','X02':'expansion_strong_downtrend','X03':'expansion_strong_flat','X04':'expansion_moderate_trend','X05':'expansion_no_trend',
'T01':'strong_uptrend_extended','T02':'strong_uptrend_room','T03':'strong_downtrend_extended','T04':'strong_downtrend_room','T05':'moderate_uptrend','T06':'moderate_downtrend','T07':'directional_drift_flat',
'O01':'overbought_range','O02':'overbought_trend','O03':'oversold_range','O04':'oversold_trend','O05':'moderately_overbought','O06':'moderately_oversold',
'R01':'wide_volatile_range','R02':'wide_quiet_range','R03':'normal_range','R04':'tight_range','S01':'quiet_asia','S02':'active_asia','S03':'volatile_asia','S04':'london_midrange_drift','S05':'quiet_ny','S06':'active_ny','Z01':'catch_all'}

# v0 proxy uses existing OHLCV-derived event fields from raw-M5 v2 / daily ledger.
# It preserves the priority structure, while using available proxies:
# ADX proxy = m15/h1 directional strength; ATR_ratio proxy = echo_range_ratio; BB_compress proxy = bbw bin/bps.
def adx_proxy(row):
    h1 = str(row.get('h1_regime',''))
    m15 = str(row.get('m15_trend',''))
    bbw = float(row.get('bbw_a_bps', np.nan))
    if h1 == 'breakout' and m15 in ('up','down'): return 42.0
    if h1 == 'breakout': return 32.0
    if m15 in ('up','down'): return 28.0
    if bbw < 8: return 16.0
    return 22.0

def slope_proxy(row):
    m15 = str(row.get('m15_trend',''))
    if m15 == 'up': return 0.0025
    if m15 == 'down': return -0.0025
    return 0.0

def close_pos_proxy(row):
    bb = str(row.get('bb_pos_bin',''))
    val = row.get('bb_position', np.nan)
    if pd.notna(val):
        try: return max(0.0, min(1.0, float(val)))
        except Exception: pass
    return {'below_band':0.02,'lower_rail':0.08,'lower_band':0.22,'middle':0.50,'upper_band':0.78,'upper_rail':0.92,'above_band':0.98}.get(bb,0.50)

def classify(row):
    trig = str(row.get('trigger_type',''))
    adx = adx_proxy(row)
    atr = float(row.get('echo_range_ratio', np.nan))
    if not np.isfinite(atr): atr = 1.0
    slope = slope_proxy(row)
    cp = close_pos_proxy(row)
    rsi = float(row.get('rsi', np.nan)) if pd.notna(row.get('rsi', np.nan)) else 50.0
    bbw = float(row.get('bbw_a_bps', np.nan)) if pd.notna(row.get('bbw_a_bps', np.nan)) else 15.0
    bbcomp = {'bbw_tight':0.60,'bbw_mid':0.90,'bbw_wide':1.15,'bbw_explosive':1.60}.get(str(row.get('bbw_bin','')),1.0)
    sess = str(row.get('session_bucket',''))
    hour = {'asia':2,'london':9,'overlap':13,'ny_pm':18,'rollover':21}.get(sess,12)
    breakout_up = trig in ('T8_pdh_failed_breakout','T10_compression_expansion') and str(row.get('direction')) == 'long'
    breakout_dn = trig in ('T8_pdl_failed_breakdown','T10_compression_expansion') and str(row.get('direction')) == 'short'
    false_break_up = trig == 'T8_pdh_failed_breakout'
    false_break_dn = trig == 'T8_pdl_failed_breakdown'
    stop_hunt_up = trig == 'T7_pdl_proximity_reversal'
    stop_hunt_dn = trig == 'T7_pdh_proximity_reversal'
    if stop_hunt_up and adx >= 20: return 'M01'
    if stop_hunt_up and adx < 20: return 'M02'
    if stop_hunt_dn and adx >= 20: return 'M03'
    if stop_hunt_dn and adx < 20: return 'M04'
    if false_break_up and adx >= 30: return 'F01'
    if false_break_up and adx < 30: return 'F02'
    if false_break_dn and adx >= 30: return 'F03'
    if false_break_dn and adx < 30: return 'F04'
    if breakout_up and adx >= 40 and atr >= 1.2: return 'B01'
    if breakout_up and adx >= 40 and atr < 1.2: return 'B02'
    if breakout_up and adx < 40 and adx >= 25: return 'B03'
    if breakout_up and adx < 25: return 'B04'
    if breakout_dn and adx >= 40 and atr >= 1.2: return 'B05'
    if breakout_dn and adx >= 40 and atr < 1.2: return 'B06'
    if breakout_dn and adx < 40 and adx >= 25: return 'B07'
    if breakout_dn and adx < 25: return 'B08'
    if bbcomp <= 0.75 and atr <= 0.8 and adx < 20: return 'C01'
    if bbcomp <= 0.75 and atr <= 0.8 and adx >= 20: return 'C02'
    if bbcomp <= 0.75 and atr > 0.8 and adx < 20: return 'C03'
    if bbcomp <= 0.75 and atr > 0.8 and adx >= 20: return 'C04'
    if atr >= 1.5 and adx >= 40 and slope > 0.002: return 'X01'
    if atr >= 1.5 and adx >= 40 and slope < -0.002: return 'X02'
    if atr >= 1.5 and adx >= 40 and abs(slope) <= 0.002: return 'X03'
    if atr >= 1.5 and adx < 40 and adx >= 25: return 'X04'
    if atr >= 1.5 and adx < 25: return 'X05'
    if adx >= 40 and slope > 0.002 and cp >= 0.8: return 'T01'
    if adx >= 40 and slope > 0.002 and cp < 0.8: return 'T02'
    if adx >= 40 and slope < -0.002 and cp <= 0.2: return 'T03'
    if adx >= 40 and slope < -0.002 and cp > 0.2: return 'T04'
    if adx >= 25 and adx < 40 and slope > 0.001: return 'T05'
    if adx >= 25 and adx < 40 and slope < -0.001: return 'T06'
    if adx >= 25 and adx < 40 and abs(slope) <= 0.001: return 'T07'
    if rsi > 80 and cp > 0.9 and adx < 25: return 'O01'
    if rsi > 80 and cp > 0.9 and adx >= 25: return 'O02'
    if rsi < 20 and cp < 0.1 and adx < 25: return 'O03'
    if rsi < 20 and cp < 0.1 and adx >= 25: return 'O04'
    if rsi > 70 and rsi <= 80 and cp > 0.85: return 'O05'
    if rsi < 30 and rsi >= 20 and cp < 0.15: return 'O06'
    if adx < 20 and bbw >= 30 and atr >= 1.0: return 'R01'
    if adx < 20 and bbw >= 30 and atr < 1.0: return 'R02'
    if adx < 20 and bbw < 30 and bbw >= 10: return 'R03'
    if adx < 20 and bbw < 10: return 'R04'
    if 0 <= hour < 7 and atr < 0.6 and adx < 20: return 'S01'
    if 0 <= hour < 7 and atr >= 0.6 and atr < 1.0: return 'S02'
    if 0 <= hour < 7 and atr >= 1.0: return 'S03'
    if 8 <= hour < 15 and 0.45 <= cp <= 0.55 and adx < 20: return 'S04'
    if 16 <= hour < 23 and atr < 0.7: return 'S05'
    if 16 <= hour < 23 and atr >= 0.7: return 'S06'
    return 'Z01'

def main():
    ledger = pd.read_parquet(LEDGER)
    print('loaded ledger', len(ledger))
    ledger['technical_regime_53'] = ledger.apply(classify, axis=1)
    ledger['technical_regime_desc'] = ledger['technical_regime_53'].map(DESC)
    ledger.to_csv(OUT/'daily_trade_ledger_with_regime53.csv', index=False)
    ledger.to_parquet(OUT/'daily_trade_ledger_with_regime53.parquet', index=False)
    repairs = ledger[ledger.record_type == 'repaired_winner']
    first = ledger[ledger.record_type == 'first_pass']
    strat = repairs.groupby(['technical_regime_53','technical_regime_desc','strategy_name','pair_family','direction']).agg(
        repaired_winners=('ledger_id','size'),
        median_R=('realized_at_2R_net','median'),
        median_mfe=('mfe_r_net','median'),
        median_mae=('mae_r','median'),
    ).reset_index().sort_values('repaired_winners', ascending=False)
    strat.to_csv(OUT/'strategy_x_regime53_repaired_winners.csv', index=False)
    fp = first.groupby(['technical_regime_53','technical_regime_desc','strategy_name','pair_family','direction']).agg(
        first_pass_n=('ledger_id','size'),
        first_pass_win_rate=('realized_at_2R_net', lambda x: float((x>0).mean())),
        mean_R=('realized_at_2R_net','mean'),
    ).reset_index().sort_values('first_pass_n', ascending=False)
    fp.to_csv(OUT/'strategy_x_regime53_first_pass.csv', index=False)
    counts = ledger.technical_regime_53.value_counts().rename_axis('technical_regime_53').reset_index(name='ledger_rows')
    counts['description'] = counts.technical_regime_53.map(DESC)
    counts.to_csv(OUT/'regime53_ledger_coverage.csv', index=False)
    lines = []
    lines.append('# Technical Regime 53 Atlas v0')
    lines.append('')
    lines.append(f'Generated: {datetime.now(timezone.utc).isoformat()}')
    lines.append('')
    lines.append('## What This Is')
    lines.append('')
    lines.append('Brock provided a 53-regime OHLCV decision tree. This v0 attaches a mutually exclusive technical_regime_53 label to every row in the Daily Textbook Trade Encyclopedia, then summarizes which repaired-winning strategies cluster inside which regimes.')
    lines.append('')
    lines.append('## Important v0 Caveat')
    lines.append('')
    lines.append('This first pass uses event-level OHLCV-derived proxies already present in the raw-M5 v2 ledger: BB/RSI/EMA/BBW/echo, M15 trend, H1 regime, session, and trigger type. It preserves the priority structure and regime semantics, but it is not yet a full bar-by-bar ADX/ATR-ratio recomputation. That can be v1.')
    lines.append('')
    lines.append('## Coverage')
    lines.append('')
    lines.append(f'- Ledger rows labeled: {len(ledger):,}')
    lines.append(f'- Repaired winners labeled: {len(repairs):,}')
    lines.append(f'- Regimes represented: {ledger.technical_regime_53.nunique()}')
    lines.append('')
    lines.append('## Top Repaired Winner Synchrony')
    lines.append('')
    lines.append(strat.head(30).to_markdown(index=False, floatfmt='.3f'))
    lines.append('')
    lines.append('## First-Pass Strategy x Regime')
    lines.append('')
    lines.append(fp.head(20).to_markdown(index=False, floatfmt='.3f'))
    lines.append('')
    lines.append('## Next Step')
    lines.append('')
    lines.append('Use the top strategy/regime clusters as named technique candidates, then run deterministic raw-M5 backtests per cluster. v1 should recompute full ADX14/ATR_ratio/BB_compress from bars and compare labels against this proxy v0.')
    (OUT/'summary.md').write_text('\n'.join(lines)+'\n')
    print(strat.head(20).to_string(index=False))

if __name__ == '__main__':
    main()
