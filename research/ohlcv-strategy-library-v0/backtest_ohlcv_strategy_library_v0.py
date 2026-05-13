"""OHLCV Strategy Library v0.

Implements Brock's explicit formula library as executable M5 strategies and
backtests each strategy independently, one open trade at a time, conditioned by
bar-true Technical Regime 53 labels.

Outputs are aggregate-first. Full trade logs are generated on EC2 but ignored by
git because they can become large.
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

ROOT = Path("/home/ubuntu/mr-scrooge-v3")
DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = ROOT / "research/ohlcv-strategy-library-v0"
OUT.mkdir(parents=True, exist_ok=True)
REGIME_MOD_PATH = ROOT / "research/technical-regime-53-atlas-v1/build_regime_atlas_v1.py"
DISCOVERY_END = pd.Timestamp("2025-01-01", tz="UTC")
MAX_HOLD_BARS = 300

spec = importlib.util.spec_from_file_location("regime53", REGIME_MOD_PATH)
regime53 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(regime53)  # type: ignore

PAIRS_ALL = ['AUD_CAD','AUD_CHF','AUD_JPY','AUD_NZD','AUD_USD','CAD_JPY','CHF_JPY','EUR_AUD','EUR_CAD','EUR_CHF','EUR_GBP','EUR_JPY','EUR_NZD','EUR_USD','GBP_AUD','GBP_CAD','GBP_CHF','GBP_JPY','GBP_NZD','GBP_USD','NZD_JPY','NZD_USD','USD_CAD','USD_CHF','USD_JPY','USD_MXN']
SMOKE_PAIRS = ['EUR_USD','GBP_USD','AUD_USD','USD_JPY']

PAIR_FAMILY = {
    'EUR_USD':'usd_base','GBP_USD':'usd_base','AUD_USD':'usd_base','NZD_USD':'usd_base','USD_JPY':'usd_base','USD_CHF':'usd_base','USD_CAD':'usd_base','USD_MXN':'usd_base',
    'AUD_CAD':'antipodean_cross','AUD_CHF':'antipodean_cross','AUD_JPY':'antipodean_cross','AUD_NZD':'antipodean_cross','CAD_JPY':'antipodean_cross','CHF_JPY':'antipodean_cross','NZD_JPY':'antipodean_cross',
    'EUR_AUD':'eur_cross','EUR_CAD':'eur_cross','EUR_CHF':'eur_cross','EUR_GBP':'eur_cross','EUR_JPY':'eur_cross','EUR_NZD':'eur_cross',
    'GBP_AUD':'gbp_cross','GBP_CAD':'gbp_cross','GBP_CHF':'gbp_cross','GBP_JPY':'gbp_cross','GBP_NZD':'gbp_cross',
}


def load_pair(pair: str) -> pd.DataFrame:
    rows = []
    for f in sorted(glob.glob(str(DUKA / pair / f"{pair}_M5_*.jsonl"))):
        with open(f) as fh:
            for line in fh:
                d = json.loads(line)
                rows.append({
                    'ts': pd.Timestamp(d['time']),
                    'open_bid': d['open_bid'], 'high_bid': d['high_bid'], 'low_bid': d['low_bid'], 'close_bid': d['close_bid'],
                    'open_ask': d['open_ask'], 'high_ask': d['high_ask'], 'low_ask': d['low_ask'], 'close_ask': d['close_ask'],
                    'volume': (d.get('volume_bid', 0.0) + d.get('volume_ask', 0.0)) / 2.0,
                })
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df['ts'] = pd.to_datetime(df['ts'], utc=True)
    df = df.sort_values('ts').drop_duplicates('ts').reset_index(drop=True)
    for col in ['open','high','low','close']:
        df[col] = (df[f'{col}_bid'] + df[f'{col}_ask']) / 2.0
    df['spread'] = df['close_ask'] - df['close_bid']
    return df


def atr(high, low, close, n=14):
    tr = pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()


def compute_indicators(pair: str, df: pd.DataFrame) -> pd.DataFrame:
    c,h,l,o = df['close'], df['high'], df['low'], df['open']
    df['ATR14'] = atr(h,l,c,14)
    df['ATR10'] = atr(h,l,c,10)
    for p in [9,20,21,50]:
        df[f'EMA{p}'] = c.ewm(span=p, adjust=False).mean()
    mid = c.rolling(20).mean(); std = c.rolling(20).std(ddof=0)
    df['bb_mid'] = mid; df['bb_upper'] = mid + 2*std; df['bb_lower'] = mid - 2*std
    df['BB_width'] = (df['bb_upper'] - df['bb_lower']) / mid
    df['z20'] = (c - mid) / std.replace(0, np.nan)
    df['ADX14'] = regime53.compute_adx(h,l,c)
    df['RSI14'] = regime53.compute_rsi(c)
    df['volume_sma20'] = df['volume'].rolling(20).mean()
    df['volume_ratio'] = df['volume'] / df['volume_sma20'].replace(0, np.nan)
    df['max20_prior'] = h.shift(1).rolling(20).max()
    df['min20_prior'] = l.shift(1).rolling(20).min()
    df['max20_prior2'] = h.shift(2).rolling(19).max()
    df['min20_prior2'] = l.shift(2).rolling(19).min()
    max20 = h.rolling(20).max(); min20 = l.rolling(20).min()
    df['price_pos'] = ((c - min20) / (max20 - min20).replace(0, np.nan)).clip(0,1)
    df['EMA50_slope5'] = (df['EMA50'] - df['EMA50'].shift(5)) / df['EMA50'].shift(5)
    df['EMA50_slope10'] = (df['EMA50'] - df['EMA50'].shift(10)) / df['EMA50'].shift(10)
    df['EMA20_slope5_abs'] = df['EMA20'] - df['EMA20'].shift(5)
    df['EMA20_slope5'] = (df['EMA20'] - df['EMA20'].shift(5)) / df['EMA20'].shift(5)
    df['WilliamsR14'] = ((h.rolling(14).max() - c) / (h.rolling(14).max() - l.rolling(14).min()).replace(0, np.nan)) * -100
    df['KC_mid'] = df['EMA20']; df['KC_upper'] = df['KC_mid'] + 1.5*df['ATR14']; df['KC_lower'] = df['KC_mid'] - 1.5*df['ATR14']; df['KC_width'] = df['KC_upper'] - df['KC_lower']
    bases = regime53.compute_daily_baselines(pair)
    df['date'] = df['ts'].dt.floor('D')
    df = df.merge(bases, on='date', how='left')
    df['ATR_ratio'] = df['ATR14'] / df['daily_atr20_avg']
    df['BB_compress'] = df['BB_width'] / df['daily_bbwidth20_avg']
    df['hour'] = df['ts'].dt.hour
    df['minute'] = df['ts'].dt.minute
    df['minute_of_day'] = df['hour']*60 + df['minute']
    df['session_id'] = np.select([df['hour'] < 8, df['hour'] < 16], ['asia','london'], default='ny')
    start_min = np.select([df['session_id'].eq('asia'), df['session_id'].eq('london')], [0, 8*60], default=16*60)
    df['minutes_since_open'] = df['minute_of_day'] - start_min
    typical = (df['high'] + df['low'] + df['close']) / 3
    df['session_key'] = df['date'].astype(str) + '_' + df['session_id'].astype(str)
    df['VWAP'] = (typical * df['volume']).groupby(df['session_key']).cumsum() / df['volume'].groupby(df['session_key']).cumsum().replace(0, np.nan)
    # Opening ranges.
    df['bar_in_day'] = df.groupby('date').cumcount()
    asia_first4 = (df['hour'] >= 0) & (df['hour'] < 4)
    asia_range = df[asia_first4].groupby('date').agg(asia_high=('high','max'), asia_low=('low','min'))
    df = df.merge(asia_range, on='date', how='left')
    lon_first6 = (df['hour'].eq(8)) & (df['minute'] < 30)
    lon_range = df[lon_first6].groupby('date').agg(lon_high=('high','max'), lon_low=('low','min'))
    df = df.merge(lon_range, on='date', how='left')
    first60 = ((df['hour'].eq(8)) | (df['hour'].eq(16)))
    or_key = df['date'].astype(str) + '_' + np.where(df['hour'].between(8,15), 'london', np.where(df['hour'].between(16,23), 'ny', 'other'))
    tmp = df[first60].assign(or_key=or_key[first60]).groupby('or_key').agg(or_high=('high','max'), or_low=('low','min'))
    df['or_key'] = or_key
    df = df.merge(tmp, on='or_key', how='left')
    # SuperTrend and SAR.
    add_supertrend(df)
    add_sar(df)
    # Regime labels.
    reg_input = df.copy()
    reg_input['EMA_slope'] = reg_input['EMA50_slope10']
    reg_input['close_pos'] = reg_input['price_pos']
    reg_input['max_20'] = df['max20_prior']; reg_input['min_20'] = df['min20_prior']
    reg_input['breakout_up'] = c > df['max20_prior'] * 1.002
    reg_input['breakout_dn'] = c < df['min20_prior'] * 0.998
    bo_up_recent = reg_input['breakout_up'].shift(1).rolling(2).max().fillna(0).astype(bool)
    bo_dn_recent = reg_input['breakout_dn'].shift(1).rolling(2).max().fillna(0).astype(bool)
    reg_input['false_break_up'] = bo_up_recent & (c <= df['max20_prior'])
    reg_input['false_break_dn'] = bo_dn_recent & (c >= df['min20_prior'])
    sweep_up = l < df['min20_prior'] * 0.998
    sweep_dn = h > df['max20_prior'] * 1.002
    reg_input['stop_hunt_up'] = sweep_up.rolling(2).max().fillna(0).astype(bool) & (c > df['min20_prior'])
    reg_input['stop_hunt_dn'] = sweep_dn.rolling(2).max().fillna(0).astype(bool) & (c < df['max20_prior'])
    labels = regime53.assign_regimes(reg_input)
    df['technical_regime_53'] = labels['technical_regime_53'].values
    df['technical_regime_desc'] = labels['technical_regime_desc'].values
    return df


def add_supertrend(df: pd.DataFrame, n=10, mult=3.0) -> None:
    hl2 = (df['high'] + df['low']) / 2
    atr10 = df['ATR10']
    upper = hl2 + mult * atr10
    lower = hl2 - mult * atr10
    final_upper = upper.copy(); final_lower = lower.copy()
    st_dir = np.ones(len(df), dtype=float); st_level = np.full(len(df), np.nan)
    close = df['close'].values
    fu = final_upper.to_numpy(copy=True); fl = final_lower.to_numpy(copy=True); bu = upper.to_numpy(copy=True); bl = lower.to_numpy(copy=True)
    for i in range(1, len(df)):
        fu[i] = bu[i] if (bu[i] < fu[i-1] or close[i-1] > fu[i-1]) else fu[i-1]
        fl[i] = bl[i] if (bl[i] > fl[i-1] or close[i-1] < fl[i-1]) else fl[i-1]
        if st_dir[i-1] == -1 and close[i] > fu[i]:
            st_dir[i] = 1
        elif st_dir[i-1] == 1 and close[i] < fl[i]:
            st_dir[i] = -1
        else:
            st_dir[i] = st_dir[i-1]
        st_level[i] = fl[i] if st_dir[i] == 1 else fu[i]
    df['ST_dir'] = st_dir; df['ST_level'] = st_level


def add_sar(df: pd.DataFrame, step=0.02, max_step=0.2) -> None:
    n = len(df)
    sar = np.full(n, np.nan); trend = np.ones(n, dtype=int)
    high = df['high'].values; low = df['low'].values
    if n < 3:
        df['SAR'] = sar; return
    trend[1] = 1 if df['close'].iloc[1] >= df['close'].iloc[0] else -1
    ep = high[1] if trend[1] == 1 else low[1]
    sar[1] = low[0] if trend[1] == 1 else high[0]
    af = step
    for i in range(2, n):
        sar[i] = sar[i-1] + af * (ep - sar[i-1])
        if trend[i-1] == 1:
            sar[i] = min(sar[i], low[i-1], low[i-2])
            if low[i] < sar[i]:
                trend[i] = -1; sar[i] = ep; ep = low[i]; af = step
            else:
                trend[i] = 1
                if high[i] > ep:
                    ep = high[i]; af = min(max_step, af + step)
        else:
            sar[i] = max(sar[i], high[i-1], high[i-2])
            if high[i] > sar[i]:
                trend[i] = 1; sar[i] = ep; ep = high[i]; af = step
            else:
                trend[i] = -1
                if low[i] < ep:
                    ep = low[i]; af = min(max_step, af + step)
    df['SAR'] = sar


def add_variant(rows, name, direction, mask, stop, tp2, catalog, category):
    m = mask.fillna(False).astype(bool)
    # v0 uses edge entries: fire only when the exact formula becomes true.
    # This avoids duplicate entries on every bar of long-lived state formulas.
    m = m & ~m.shift(1).fillna(False).astype(bool)
    rows.append((name, category, direction, m, stop, tp2))
    catalog.append({'strategy_id': name, 'category': category, 'direction': direction})


def build_variants(df: pd.DataFrame) -> Tuple[List[Tuple], pd.DataFrame]:
    rows = []; catalog = []
    c,h,l,o = df['close'], df['high'], df['low'], df['open']
    A = df['ATR14']; vr = df['volume_ratio']; adx = df['ADX14']; rsi = df['RSI14']; pp = df['price_pos']
    entry_long = df['close_ask']; entry_short = df['close_bid']
    min5 = l.rolling(5).min(); max5 = h.rolling(5).max(); min10 = l.rolling(10).min(); max10 = h.rolling(10).max()
    # Trend following.
    add_variant(rows,'TF1_EMA9_gt_EMA21','long',(df['EMA9']>df['EMA21'])&(adx>=25), entry_long-1.5*A, entry_long+3*A, catalog,'trend')
    add_variant(rows,'TF1_EMA9_lt_EMA21','short',(df['EMA9']<df['EMA21'])&(adx>=25), entry_short+1.5*A, entry_short-3*A, catalog,'trend')
    add_variant(rows,'TF2_pullback_EMA20_long','long',(c>df['EMA20'])&(l<df['EMA20'])&(l>df['EMA20']*0.998)&(vr>0.7), min5, entry_long+2*(entry_long-min5), catalog,'trend')
    add_variant(rows,'TF2_pullback_EMA20_short','short',(c<df['EMA20'])&(h>df['EMA20'])&(h<df['EMA20']*1.002)&(vr>0.7), max5, entry_short-2*(max5-entry_short), catalog,'trend')
    add_variant(rows,'TF3_supertrend_long','long',df['ST_dir'].eq(1), df['ST_level'], entry_long+2*(entry_long-df['ST_level']), catalog,'trend')
    add_variant(rows,'TF3_supertrend_short','short',df['ST_dir'].eq(-1), df['ST_level'], entry_short-2*(df['ST_level']-entry_short), catalog,'trend')
    london_ny = df['hour'].between(8,22)
    add_variant(rows,'TF4_sar_long','long',(df['SAR']<l)&london_ny, df['SAR'], entry_long+2*(entry_long-df['SAR']), catalog,'trend')
    add_variant(rows,'TF4_sar_short','short',(df['SAR']>h)&london_ny, df['SAR'], entry_short-2*(df['SAR']-entry_short), catalog,'trend')
    add_variant(rows,'TF5_donchian_breakout_long','long',(c>df['max20_prior']*1.002)&(adx>=30)&(vr>1.2), entry_long-2*A, entry_long+3*A, catalog,'trend')
    add_variant(rows,'TF5_donchian_breakout_short','short',(c<df['min20_prior']*0.998)&(adx>=30)&(vr>1.2), entry_short+2*A, entry_short-3*A, catalog,'trend')
    rising = (df['EMA9']>df['EMA9'].shift(1))&(df['EMA21']>df['EMA21'].shift(1))&(df['EMA50']>df['EMA50'].shift(1))
    falling = (df['EMA9']<df['EMA9'].shift(1))&(df['EMA21']<df['EMA21'].shift(1))&(df['EMA50']<df['EMA50'].shift(1))
    add_variant(rows,'TF6_ma_ribbon_long','long',(df['EMA9']>df['EMA21'])&(df['EMA21']>df['EMA50'])&rising&(df['EMA50_slope5']>0.0005), min10, entry_long+2*(entry_long-min10), catalog,'trend')
    add_variant(rows,'TF6_ma_ribbon_short','short',(df['EMA9']<df['EMA21'])&(df['EMA21']<df['EMA50'])&falling&(df['EMA50_slope5']<-0.0005), max10, entry_short-2*(max10-entry_short), catalog,'trend')
    # Mean reversion.
    add_variant(rows,'MR1_rsi_extreme_long','long',(rsi<25)&(adx<20), entry_long-1.5*A, entry_long+3*A, catalog,'mean_reversion')
    add_variant(rows,'MR1_rsi_extreme_short','short',(rsi>75)&(adx<20), entry_short+1.5*A, entry_short-3*A, catalog,'mean_reversion')
    add_variant(rows,'MR2_bb_reversion_long','long',(c<df['bb_lower'])&(vr<1.5), entry_long-2*A, df['bb_mid'], catalog,'mean_reversion')
    add_variant(rows,'MR2_bb_reversion_short','short',(c>df['bb_upper'])&(vr<1.5), entry_short+2*A, df['bb_mid'], catalog,'mean_reversion')
    add_variant(rows,'MR3_vwap_reversion_long','long',(c<df['VWAP']*0.998)&(df['minutes_since_open']<=120), entry_long-0.75*A, df['VWAP'], catalog,'mean_reversion')
    add_variant(rows,'MR3_vwap_reversion_short','short',(c>df['VWAP']*1.002)&(df['minutes_since_open']<=120), entry_short+0.75*A, df['VWAP'], catalog,'mean_reversion')
    add_variant(rows,'MR4_zscore_extreme_long','long',(df['z20']<-2.0)&(adx<25), entry_long-1.5*A, entry_long+2.25*A, catalog,'mean_reversion')
    add_variant(rows,'MR4_zscore_extreme_short','short',(df['z20']>2.0)&(adx<25), entry_short+1.5*A, entry_short-2.25*A, catalog,'mean_reversion')
    add_variant(rows,'MR5_williams_extreme_long','long',df['WilliamsR14']<-90, entry_long-1.2*A, entry_long+2.4*A, catalog,'mean_reversion')
    add_variant(rows,'MR5_williams_extreme_short','short',df['WilliamsR14']>-10, entry_short+1.2*A, entry_short-2.4*A, catalog,'mean_reversion')
    # Breakouts.
    add_variant(rows,'BR1_range_breakout_long','long',(c>df['max20_prior']*1.002)&(adx>=20)&(vr>1.1), entry_long-2*A, entry_long+3*A, catalog,'breakout')
    add_variant(rows,'BR1_range_breakout_short','short',(c<df['min20_prior']*0.998)&(adx>=20)&(vr>1.1), entry_short+2*A, entry_short-3*A, catalog,'breakout')
    add_variant(rows,'BR2_vcb_long','long',(df['BB_width']<0.02)&(c>h.shift(1).rolling(5).max())&(df['ATR_ratio']<0.8), entry_long-1.5*A, entry_long+2*A, catalog,'breakout')
    add_variant(rows,'BR2_vcb_short','short',(df['BB_width']<0.02)&(c<l.shift(1).rolling(5).min())&(df['ATR_ratio']<0.8), entry_short+1.5*A, entry_short-2*A, catalog,'breakout')
    inside = (h.shift(1)<h.shift(2))&(l.shift(1)>l.shift(2))
    add_variant(rows,'BR3_inside_bar_long','long',inside&(c>h.shift(1)), l.shift(1), entry_long+2*(entry_long-l.shift(1)), catalog,'breakout')
    add_variant(rows,'BR3_inside_bar_short','short',inside&(c<l.shift(1)), h.shift(1), entry_short-2*(h.shift(1)-entry_short), catalog,'breakout')
    pivot_h = h.where((h>=h.shift(1))&(h>=h.shift(-1))).shift(1).rolling(5).max()
    pivot_l = l.where((l<=l.shift(1))&(l<=l.shift(-1))).shift(1).rolling(5).min()
    add_variant(rows,'BR4_pivot_breakout_long','long',(c>pivot_h)&(adx>=30), entry_long-1.5*A, entry_long+3.75*A, catalog,'breakout')
    add_variant(rows,'BR4_pivot_breakout_short','short',(c<pivot_l)&(adx>=30), entry_short+1.5*A, entry_short-3.75*A, catalog,'breakout')
    after_or = (df['hour'].between(9,15)) | (df['hour'].between(17,23))
    add_variant(rows,'BR5_opening_range_breakout_long','long',after_or&(c>df['or_high']), entry_long-1.5*A, entry_long+3*A, catalog,'breakout')
    add_variant(rows,'BR5_opening_range_breakout_short','short',after_or&(c<df['or_low']), entry_short+1.5*A, entry_short-3*A, catalog,'breakout')
    # False breakout / stop hunts.
    fb_up = (c.shift(1)>df['max20_prior2']*1.002)&(c<df['max20_prior2'])
    fb_dn = (c.shift(1)<df['min20_prior2']*0.998)&(c>df['min20_prior2'])
    add_variant(rows,'FB1_false_breakout_reversal_short','short',fb_up&(vr.shift(1)>1.5), entry_short+1.5*A, entry_short-2.25*A, catalog,'false_breakout')
    add_variant(rows,'FB1_false_breakout_reversal_long','long',fb_dn&(vr.shift(1)>1.5), entry_long-1.5*A, entry_long+2.25*A, catalog,'false_breakout')
    add_variant(rows,'FB2_stop_hunt_reversal_long','long',(l.shift(1)<df['min20_prior2']*0.998)&(c>df['min20_prior2'])&(rsi<40), entry_long-1.2*A, entry_long+2.4*A, catalog,'false_breakout')
    add_variant(rows,'FB3_stop_hunt_reversal_short','short',(h.shift(1)>df['max20_prior2']*1.002)&(c<df['max20_prior2'])&(rsi>60), entry_short+1.2*A, entry_short-2.4*A, catalog,'false_breakout')
    add_variant(rows,'FB4_2bar_fakeout_short','short',fb_up, entry_short+1.5*A, entry_short-3*A, catalog,'false_breakout')
    add_variant(rows,'FB4_2bar_fakeout_long','long',fb_dn, entry_long-1.5*A, entry_long+3*A, catalog,'false_breakout')
    # Compression.
    compressed3 = (df['BB_compress']<=0.75)&(df['BB_compress'].shift(1)<=0.75)&(df['BB_compress'].shift(2)<=0.75)
    add_variant(rows,'CP1_coil_breakout_long','long',compressed3&(c>h.shift(1).rolling(5).max())&(vr>1.2), entry_long-1.5*A, entry_long+2*A, catalog,'compression')
    add_variant(rows,'CP1_coil_breakout_short','short',compressed3&(c<l.shift(1).rolling(5).min())&(vr>1.2), entry_short+1.5*A, entry_short-2*A, catalog,'compression')
    squeeze = ((df['bb_upper']-df['bb_lower']) < df['KC_width'])
    add_variant(rows,'CP2_squeeze_momentum_long','long',squeeze&(c>h.shift(1).rolling(5).max()), entry_long-1.5*A, entry_long+2*A, catalog,'compression')
    add_variant(rows,'CP2_squeeze_momentum_short','short',squeeze&(c<l.shift(1).rolling(5).min()), entry_short+1.5*A, entry_short-2*A, catalog,'compression')
    midcoil = (df['BB_compress']<=0.7)&(pp.between(0.4,0.6))&(adx<20)
    add_variant(rows,'CP3_vol_coil_fade_long','long',midcoil, entry_long-1.0*A, entry_long+1.5*A, catalog,'compression')
    add_variant(rows,'CP3_vol_coil_fade_short','short',midcoil, entry_short+1.0*A, entry_short-1.5*A, catalog,'compression')
    # Expansion.
    add_variant(rows,'EX1_momentum_expansion_long','long',(df['ATR_ratio']>=1.5)&(c>df['EMA50'])&(c>o*1.002)&(adx>=40), entry_long-2*A, entry_long+3*A, catalog,'expansion')
    add_variant(rows,'EX2_expansion_pullback_long','long',(df['ATR_ratio']>=1.3)&(rsi<50)&(c<df['EMA20'])&(df['EMA20_slope5']>0.001), entry_long-1.5*A, entry_long+3*A, catalog,'expansion')
    add_variant(rows,'EX3_vol_spike_fade_short','short',(df['ATR_ratio']>=2.0)&(c>df['bb_upper'])&(adx<30), entry_short+1.2*A, entry_short-2.4*A, catalog,'expansion')
    # Range.
    add_variant(rows,'RG1_range_bound_scalp_short','short',(adx<20)&(pp>0.85), entry_short+1.0*A, entry_short-1.5*A, catalog,'range')
    add_variant(rows,'RG2_range_support_bounce_long','long',(adx<20)&(pp<0.15), entry_long-1.0*A, entry_long+1.5*A, catalog,'range')
    add_variant(rows,'RG3_midrange_drift_fade_short','short',(adx<20)&pp.between(0.45,0.55)&(rsi>55)&(df['hour'].between(8,15)), entry_short+0.8*A, entry_short-0.96*A, catalog,'range')
    # Session.
    asia_after4 = (df['hour']>=4)&(df['hour']<8)
    add_variant(rows,'SS1_asian_range_breakout_long','long',asia_after4&(c>df['asia_high'])&(df['ATR_ratio']<0.8), entry_long-1.5*A, entry_long+3*(entry_long-(entry_long-1.5*A)), catalog,'session')
    add_variant(rows,'SS1_asian_range_breakout_short','short',asia_after4&(c<df['asia_low'])&(df['ATR_ratio']<0.8), entry_short+1.5*A, entry_short-3*(entry_short+1.5*A-entry_short), catalog,'session')
    london_after = (df['hour']>=8)&(df['hour']<16)&((df['hour']>8)|(df['minute']>=30))
    broke_up = (h.where(london_after).groupby(df['date']).cummax() > df['lon_high'])
    broke_dn = (l.where(london_after).groupby(df['date']).cummin() < df['lon_low'])
    add_variant(rows,'SS2_london_open_reversal_short','short',london_after&broke_up&(c<df['lon_high']), entry_short+1.2*A, entry_short-1.8*A, catalog,'session')
    add_variant(rows,'SS2_london_open_reversal_long','long',london_after&broke_dn&(c>df['lon_low']), entry_long-1.2*A, entry_long+1.8*A, catalog,'session')
    lunch = df['hour'].eq(17)
    add_variant(rows,'SS3_ny_lunch_drift_long','long',lunch&(df['EMA20_slope5_abs']>0)&(adx<20), entry_long-0.8*A, entry_long+0.8*A, catalog,'session')
    add_variant(rows,'SS3_ny_lunch_drift_short','short',lunch&(df['EMA20_slope5_abs']<0)&(adx<20), entry_short+0.8*A, entry_short-0.8*A, catalog,'session')
    # Hybrid / momentum.
    add_variant(rows,'HY1_trend_pullback_reversal_long','long',(df['EMA20_slope5_abs']>0)&(rsi<40)&(pp<0.4)&(adx>=25), entry_long-1.5*A, entry_long+3.75*A, catalog,'hybrid')
    breakout3 = h.shift(1).rolling(3).max() > h.shift(4).rolling(17).max()*1.002
    retest = (c > h.shift(4).rolling(17).max()*0.998) & (c < h.shift(4).rolling(17).max()*1.002)
    add_variant(rows,'HY2_breakout_retest_long','long',breakout3&retest&(vr.shift(1)>1.2), entry_long-1.5*A, entry_long+3*A, catalog,'hybrid')
    add_variant(rows,'HY3_overbought_pullback_uptrend_long','long',(df['EMA20_slope5_abs']>0)&(rsi>70)&(c<df['EMA20'])&(adx>=25), entry_long-1.2*A, entry_long+2.4*A, catalog,'hybrid')
    add_variant(rows,'MO1_exhaustion_after_spike_short','short',(c.shift(1)>df['bb_upper'].shift(1))&(vr.shift(1)>2.0)&(c<c.shift(1)), entry_short+1.2*A, entry_short-1.8*A, catalog,'momentum_exhaustion')
    add_variant(rows,'MO2_momentum_divergence_short','short',(h.shift(1)>h.shift(2))&(rsi.shift(1)<rsi.shift(2))&(adx>=20), entry_short+1.5*A, entry_short-3*A, catalog,'momentum_exhaustion')
    bearish_engulf = (c.shift(1)>o.shift(1))&(o<c.shift(1))&(c<o)&(pp>0.9)&(rsi>70)
    add_variant(rows,'MO3_candle_exhaustion_short','short',bearish_engulf, entry_short+1.0*A, entry_short-1.5*A, catalog,'momentum_exhaustion')
    return rows, pd.DataFrame(catalog).drop_duplicates()


def forward_walk(df, i, direction, entry, stop, tp):
    if not np.isfinite(entry) or not np.isfinite(stop) or not np.isfinite(tp):
        return None
    if direction == 'long':
        risk = entry - stop; reward = tp - entry
        if risk <= 0 or reward <= 0: return None
        end = min(i + MAX_HOLD_BARS, len(df)-1)
        mfe = 0.0; mae = 0.0
        for j in range(i+1, end+1):
            mfe = max(mfe, df['high_bid'].iat[j] - entry)
            mae = max(mae, entry - df['low_bid'].iat[j])
            if df['low_bid'].iat[j] <= stop:
                return j, -1.0, mfe/risk, mae/risk, 'stop'
            if df['high_bid'].iat[j] >= tp:
                return j, reward/risk, mfe/risk, mae/risk, 'tp'
        exit_px = df['close_bid'].iat[end]
        return end, (exit_px-entry)/risk, mfe/risk, mae/risk, 'time'
    else:
        risk = stop - entry; reward = entry - tp
        if risk <= 0 or reward <= 0: return None
        end = min(i + MAX_HOLD_BARS, len(df)-1)
        mfe = 0.0; mae = 0.0
        for j in range(i+1, end+1):
            mfe = max(mfe, entry - df['low_ask'].iat[j])
            mae = max(mae, df['high_ask'].iat[j] - entry)
            if df['high_ask'].iat[j] >= stop:
                return j, -1.0, mfe/risk, mae/risk, 'stop'
            if df['low_ask'].iat[j] <= tp:
                return j, reward/risk, mfe/risk, mae/risk, 'tp'
        exit_px = df['close_ask'].iat[end]
        return end, (entry-exit_px)/risk, mfe/risk, mae/risk, 'time'



def future_roll(s: pd.Series, fn: str, n: int = MAX_HOLD_BARS) -> pd.Series:
    shifted = s.shift(-1).iloc[::-1]
    if fn == 'max':
        out = shifted.rolling(n, min_periods=1).max().iloc[::-1]
    else:
        out = shifted.rolling(n, min_periods=1).min().iloc[::-1]
    return out


def run_pair(pair: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = load_pair(pair)
    if df.empty:
        return pd.DataFrame(), pd.DataFrame()
    df = compute_indicators(pair, df)
    variants, catalog = build_variants(df)
    # Conservative path-agnostic forward screen. If TP and stop both occur in the
    # next window, score stop. This is intentionally harsh for discovery.
    fut_high_bid = future_roll(df['high_bid'], 'max')
    fut_low_bid = future_roll(df['low_bid'], 'min')
    fut_high_ask = future_roll(df['high_ask'], 'max')
    fut_low_ask = future_roll(df['low_ask'], 'min')
    exit_bid = df['close_bid'].shift(-MAX_HOLD_BARS).fillna(df['close_bid'].iloc[-1])
    exit_ask = df['close_ask'].shift(-MAX_HOLD_BARS).fillna(df['close_ask'].iloc[-1])
    trades = []
    base_cols = ['pair','pair_family','strategy_id','category','direction','entry_ts','entry_price','stop_loss','tp2','target_R','realized_R','mfe_R','mae_R','exit_reason','technical_regime_53','technical_regime_desc','session_bucket','hour_utc','ADX14','ATR_ratio','BB_compress','RSI14','price_pos','volume_ratio']
    for strategy_id, category, direction, mask, stop_s, tp_s in variants:
        idxs = np.flatnonzero(mask.to_numpy())
        if len(idxs) == 0:
            continue
        # Drop warmup and last max-hold bars where future window is incomplete.
        idxs = idxs[(idxs >= 250) & (idxs < len(df)-2)]
        if len(idxs) == 0:
            continue
        if direction == 'long':
            entry = df['close_ask'].iloc[idxs].to_numpy()
            stop = stop_s.iloc[idxs].to_numpy(dtype=float)
            tp = tp_s.iloc[idxs].to_numpy(dtype=float)
            risk = entry - stop
            reward = tp - entry
            valid = np.isfinite(risk) & np.isfinite(reward) & (risk > 0) & (reward > 0)
            if not valid.any():
                continue
            idxs = idxs[valid]; entry = entry[valid]; stop = stop[valid]; tp = tp[valid]; risk = risk[valid]; reward = reward[valid]
            stop_hit = fut_low_bid.iloc[idxs].to_numpy() <= stop
            tp_hit = fut_high_bid.iloc[idxs].to_numpy() >= tp
            mfe = (fut_high_bid.iloc[idxs].to_numpy() - entry) / risk
            mae = (entry - fut_low_bid.iloc[idxs].to_numpy()) / risk
            time_r = (exit_bid.iloc[idxs].to_numpy() - entry) / risk
        else:
            entry = df['close_bid'].iloc[idxs].to_numpy()
            stop = stop_s.iloc[idxs].to_numpy(dtype=float)
            tp = tp_s.iloc[idxs].to_numpy(dtype=float)
            risk = stop - entry
            reward = entry - tp
            valid = np.isfinite(risk) & np.isfinite(reward) & (risk > 0) & (reward > 0)
            if not valid.any():
                continue
            idxs = idxs[valid]; entry = entry[valid]; stop = stop[valid]; tp = tp[valid]; risk = risk[valid]; reward = reward[valid]
            stop_hit = fut_high_ask.iloc[idxs].to_numpy() >= stop
            tp_hit = fut_low_ask.iloc[idxs].to_numpy() <= tp
            mfe = (entry - fut_low_ask.iloc[idxs].to_numpy()) / risk
            mae = (fut_high_ask.iloc[idxs].to_numpy() - entry) / risk
            time_r = (entry - exit_ask.iloc[idxs].to_numpy()) / risk
        target_r = reward / risk
        realized = np.where(stop_hit, -1.0, np.where(tp_hit, target_r, time_r))
        reason = np.where(stop_hit, 'stop', np.where(tp_hit, 'tp', 'time'))
        part = pd.DataFrame({
            'pair': pair,
            'pair_family': PAIR_FAMILY.get(pair, 'other'),
            'strategy_id': strategy_id,
            'category': category,
            'direction': direction,
            'entry_ts': df['ts'].iloc[idxs].to_numpy(),
            'entry_price': entry,
            'stop_loss': stop,
            'tp2': tp,
            'target_R': target_r,
            'realized_R': realized,
            'mfe_R': mfe,
            'mae_R': mae,
            'exit_reason': reason,
            'technical_regime_53': df['technical_regime_53'].iloc[idxs].to_numpy(),
            'technical_regime_desc': df['technical_regime_desc'].iloc[idxs].to_numpy(),
            'session_bucket': df['session_id'].iloc[idxs].to_numpy(),
            'hour_utc': df['hour'].iloc[idxs].to_numpy(dtype=int),
            'ADX14': df['ADX14'].iloc[idxs].to_numpy(),
            'ATR_ratio': df['ATR_ratio'].iloc[idxs].to_numpy(),
            'BB_compress': df['BB_compress'].iloc[idxs].to_numpy(),
            'RSI14': df['RSI14'].iloc[idxs].to_numpy(),
            'price_pos': df['price_pos'].iloc[idxs].to_numpy(),
            'volume_ratio': df['volume_ratio'].iloc[idxs].to_numpy(),
        }, columns=base_cols)
        trades.append(part)
    if not trades:
        return pd.DataFrame(columns=base_cols), catalog
    return pd.concat(trades, ignore_index=True), catalog



def enrich_trades(trades: pd.DataFrame) -> pd.DataFrame:
    trades = trades.copy()
    trades['entry_ts'] = pd.to_datetime(trades['entry_ts'], utc=True)
    trades['era'] = np.where(trades['entry_ts'] < DISCOVERY_END, 'discovery', 'holdout')
    trades['is_win'] = trades['realized_R'] > 0
    trades['clean_2r'] = trades['realized_R'] >= 1.8
    trades['gave_back_green'] = (trades['mfe_R'] >= 0.5) & (trades['realized_R'] < 0)
    trades['pos_R'] = trades['realized_R'].clip(lower=0)
    trades['neg_R_abs'] = (-trades['realized_R'].clip(upper=0))
    return trades


def summarize_trades(trades: pd.DataFrame, scope: str) -> pd.DataFrame:
    if trades.empty:
        return pd.DataFrame()
    group = ['technical_regime_53','technical_regime_desc','strategy_id','pair_family','session_bucket','direction']
    base = trades.groupby(group).agg(
        n=('realized_R','size'),
        win_n=('is_win','sum'),
        sum_R=('realized_R','sum'),
        pos_R=('pos_R','sum'),
        neg_R_abs=('neg_R_abs','sum'),
        clean_2r_n=('clean_2r','sum'),
        gave_back_n=('gave_back_green','sum'),
        mean_mfe=('mfe_R','mean'),
        mean_mae=('mae_R','mean'),
    ).reset_index()
    disc = trades[trades['era'].eq('discovery')].groupby(group).agg(
        n_discovery=('realized_R','size'),
        sum_R_discovery=('realized_R','sum'),
        win_n_discovery=('is_win','sum'),
    ).reset_index()
    hold = trades[trades['era'].eq('holdout')].groupby(group).agg(
        n_holdout=('realized_R','size'),
        sum_R_holdout=('realized_R','sum'),
        win_n_holdout=('is_win','sum'),
    ).reset_index()
    out = base.merge(disc, on=group, how='left').merge(hold, on=group, how='left')
    for col in ['n_discovery','sum_R_discovery','win_n_discovery','n_holdout','sum_R_holdout','win_n_holdout']:
        out[col] = out[col].fillna(0)
    out['scope'] = scope
    return out


def finalize_summary(parts: list[pd.DataFrame], catalog: pd.DataFrame, scope: str) -> pd.DataFrame:
    if not parts:
        raise SystemExit('no summary parts generated')
    group = ['technical_regime_53','technical_regime_desc','strategy_id','pair_family','session_bucket','direction']
    raw = pd.concat(parts, ignore_index=True)
    summary = raw.groupby(group).agg(
        n=('n','sum'), win_n=('win_n','sum'), sum_R=('sum_R','sum'),
        pos_R=('pos_R','sum'), neg_R_abs=('neg_R_abs','sum'),
        clean_2r_n=('clean_2r_n','sum'), gave_back_n=('gave_back_n','sum'),
        mean_mfe_num=('mean_mfe', lambda x: np.nan),
        mean_mae_num=('mean_mae', lambda x: np.nan),
        n_discovery=('n_discovery','sum'), sum_R_discovery=('sum_R_discovery','sum'), win_n_discovery=('win_n_discovery','sum'),
        n_holdout=('n_holdout','sum'), sum_R_holdout=('sum_R_holdout','sum'), win_n_holdout=('win_n_holdout','sum'),
    ).reset_index()
    # Recompute weighted MFE/MAE from raw part-level means.
    weighted = raw.copy()
    weighted['mfe_weighted'] = weighted['mean_mfe'] * weighted['n']
    weighted['mae_weighted'] = weighted['mean_mae'] * weighted['n']
    wm = weighted.groupby(group).agg(mfe_weighted=('mfe_weighted','sum'), mae_weighted=('mae_weighted','sum')).reset_index()
    summary = summary.drop(columns=['mean_mfe_num','mean_mae_num']).merge(wm, on=group, how='left')
    summary['win_rate'] = summary['win_n'] / summary['n']
    summary['mean_R'] = summary['sum_R'] / summary['n']
    summary['clean_2r_rate'] = summary['clean_2r_n'] / summary['n']
    summary['gave_back_rate'] = summary['gave_back_n'] / summary['n']
    summary['mean_mfe'] = summary['mfe_weighted'] / summary['n']
    summary['mean_mae'] = summary['mae_weighted'] / summary['n']
    summary['profit_factor'] = np.where(summary['neg_R_abs'] > 0, summary['pos_R'] / summary['neg_R_abs'], np.inf)
    summary['mean_R_discovery'] = np.where(summary['n_discovery'] > 0, summary['sum_R_discovery'] / summary['n_discovery'], np.nan)
    summary['win_rate_discovery'] = np.where(summary['n_discovery'] > 0, summary['win_n_discovery'] / summary['n_discovery'], np.nan)
    summary['mean_R_holdout'] = np.where(summary['n_holdout'] > 0, summary['sum_R_holdout'] / summary['n_holdout'], np.nan)
    summary['win_rate_holdout'] = np.where(summary['n_holdout'] > 0, summary['win_n_holdout'] / summary['n_holdout'], np.nan)
    summary = summary.sort_values(['mean_R_holdout','mean_R_discovery','n'], ascending=[False, False, False])
    summary.to_csv(OUT / f'strategy_x_regime_summary_{scope}.csv', index=False)
    candidates = summary[
        (summary['n_discovery'] >= 30) &
        (summary['n_holdout'] >= 10) &
        (summary['mean_R_discovery'] > 0) &
        (summary['mean_R_holdout'] > 0) &
        (summary['profit_factor'] > 1.1)
    ].copy().sort_values(['mean_R_holdout','n_holdout'], ascending=[False, False])
    candidates.to_csv(OUT / f'candidate_strategy_regime_cells_{scope}.csv', index=False)
    catalog.to_csv(OUT / 'strategy_catalog.csv', index=False)
    with open(OUT / f'summary_{scope}.md', 'w') as f:
        f.write(f'# OHLCV Strategy Library v0 ({scope})\n\n')
        f.write('Executable formula backtest of Brock\'s strategy library. Each strategy uses edge entries: a trade opens when the exact formula flips from false to true. Longs enter at ask and exit at bid; shorts enter at bid and exit at ask, so spread is included.\n\n')
        f.write('## Coverage\n\n')
        f.write(f'- Trades screened: {int(summary["n"].sum()):,}\n')
        f.write(f'- Strategy variants: {catalog["strategy_id"].nunique()}\n')
        f.write(f'- Regime x strategy cells: {len(summary):,}\n')
        f.write(f'- Candidate cells passing discovery+holdout positive gate: {len(candidates):,}\n\n')
        f.write('## Top Candidate Cells\n\n')
        if len(candidates):
            cols = ['technical_regime_53','technical_regime_desc','strategy_id','pair_family','session_bucket','direction','n','mean_R','win_rate','n_discovery','mean_R_discovery','n_holdout','mean_R_holdout','profit_factor']
            f.write(candidates[cols].head(30).to_markdown(index=False))
        else:
            f.write('No cells passed the positive discovery+holdout gate.\n')
        f.write('\n\n## Top Overall Cells By Mean R (n>=50)\n\n')
        top = summary[summary['n'] >= 50].sort_values('mean_R', ascending=False).head(30)
        cols = ['technical_regime_53','technical_regime_desc','strategy_id','pair_family','session_bucket','direction','n','mean_R','win_rate','profit_factor','n_holdout','mean_R_holdout']
        f.write(top[cols].to_markdown(index=False))
        f.write('\n\n## Notes\n\n')
        f.write('- This is not using the old point score. It uses explicit OHLCV formulas.\n')
        f.write('- v0 uses conservative path-agnostic screening: if TP and stop are both touched inside the forward window, the trade is scored as a stop.\n')
        f.write('- Full exact order-of-events replay should be applied only to candidate survivors.\n')
    return summary



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scope', choices=['smoke','all'], default='smoke')
    ap.add_argument('--pair', action='append', help='Optional pair override; can be supplied multiple times.')
    args = ap.parse_args()
    pairs = args.pair if args.pair else (SMOKE_PAIRS if args.scope == 'smoke' else PAIRS_ALL)
    summary_parts = []
    catalogs = []
    print(f'OHLCV strategy library v0 starting: scope={args.scope} pairs={pairs}', flush=True)
    for pair in pairs:
        print(f'[{pair}] loading, computing indicators, simulating formulas...', flush=True)
        trades, catalog = run_pair(pair)
        print(f'  trades={len(trades):,} strategies={catalog.strategy_id.nunique() if len(catalog) else 0}', flush=True)
        if len(catalog):
            catalogs.append(catalog)
        if trades.empty:
            continue
        trades = enrich_trades(trades)
        safe_pair = pair.lower()
        trades.to_parquet(OUT / f'trade_log_{args.scope}_{safe_pair}.parquet', index=False)
        pair_summary = summarize_trades(trades, f'{args.scope}_{safe_pair}')
        pair_summary.to_csv(OUT / f'strategy_x_regime_summary_{args.scope}_{safe_pair}.csv', index=False)
        summary_parts.append(pair_summary)
        del trades
    if not summary_parts:
        raise SystemExit('no trades generated')
    catalog = pd.concat(catalogs, ignore_index=True).drop_duplicates('strategy_id') if catalogs else pd.DataFrame()
    final = finalize_summary(summary_parts, catalog, args.scope)
    print(f'Done: {int(final["n"].sum()):,} screened trades. Outputs in {OUT}', flush=True)

if __name__ == '__main__':
    main()
