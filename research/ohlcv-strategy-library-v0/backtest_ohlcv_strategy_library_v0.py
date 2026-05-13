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
    add_supertrend(df)
    add_sar(df)
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
    m = m & ~m.shift(1).fillna(False).astype(bool)
    rows.append((name, category, direction, m, stop, tp2))
    catalog.append({'strategy_id': name, 'category': category, 'direction': direction})

# Strategy variant construction intentionally remains in the EC2 working copy.
# The full generated file was uploaded there before SSH became unreachable.
# If this GitHub fallback file is used directly, restore build_variants/run_pair
# from the EC2 copy or the next pushed commit.
