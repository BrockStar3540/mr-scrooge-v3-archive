"""MS-001 v2: try prior-20-bar rolling (excludes current bar) for BB/SMA.

The corpus's feature_snapshot may compute SMA/std on bars STRICTLY BEFORE
the current one. Test if that aligns with corpus distribution.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path

DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")

def load_pair_m5(pair):
    bars = []
    for f in sorted(Path(DUKA / pair).glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({"time": d["time"], "open": (d["open_bid"] + d["open_ask"]) / 2,
                             "high": (d["high_bid"] + d["high_ask"]) / 2,
                             "low":  (d["low_bid"]  + d["low_ask"])  / 2,
                             "close":(d["close_bid"]+ d["close_ask"])/ 2})
            except: pass
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)


def compute_indicators_v2(df, prior_only=True):
    """Compute indicators. If prior_only, SMA/std/EMA use bars STRICTLY before
    the current one (shift(1).rolling(20))."""
    c = df["close"]
    if prior_only:
        sma = c.shift(1).rolling(20).mean()
        std = c.shift(1).rolling(20).std(ddof=0)
        ema20 = c.shift(1).ewm(span=20, adjust=False).mean()
        ema50 = c.shift(1).ewm(span=50, adjust=False).mean()
    else:
        sma = c.rolling(20).mean()
        std = c.rolling(20).std(ddof=0)
        ema20 = c.ewm(span=20, adjust=False).mean()
        ema50 = c.ewm(span=50, adjust=False).mean()
    df["bb_upper"] = sma + 2*std
    df["bb_lower"] = sma - 2*std
    df["sma_20"] = sma
    band_width = df["bb_upper"] - df["bb_lower"]
    df["bb_position"] = (c - df["bb_lower"]) / band_width
    df["bbw_a_bps"] = (band_width / sma) * 10000.0
    delta = c.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    rs = gain / loss
    df["rsi"] = 100 - 100/(1+rs)
    df["ema20"] = ema20
    df["ema20_dist_pct"] = (c - df["ema20"]) / df["ema20"] * 10000.0
    rng = df["high"] - df["low"]
    df["echo_range_ratio"] = rng / rng.shift(1).rolling(20).mean()
    return df


print("EUR_USD: comparing prior-window vs current-window indicators")
df = load_pair_m5("EUR_USD")
for label, prior in [("current_window", False), ("prior_window", True)]:
    d2 = compute_indicators_v2(df.copy(), prior_only=prior)
    d2["hour"] = d2["ts"].dt.hour
    oq2 = d2[d2["hour"] == 13]
    print(f"\n[{label}] overlap_q2 distributions:")
    for k in ['bb_position', 'rsi', 'bbw_a_bps', 'ema20_dist_pct', 'echo_range_ratio']:
        v = pd.to_numeric(oq2[k], errors='coerce').dropna()
        if len(v) > 0:
            print(f"  {k}: median={v.median():.2f}  IQR=[{v.quantile(0.25):.2f}, {v.quantile(0.75):.2f}]")

# How many corpus rows are in MS-001 bin combination?
print("\n=== Corpus rows matching MS-001 bins (EUR_USD only as example) ===")
import glob
def parse_feat(s):
    try: return json.loads(s)
    except: return {}
matches_total = 0
years_checked = []
for f in sorted(glob.glob("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v3_full_corpus/v2_2.0R/EUR_USD_*.parquet")):
    cdf = pd.read_parquet(f)
    feats = cdf['feature_snapshot'].apply(parse_feat)
    bb = pd.to_numeric(feats.apply(lambda x: x.get('bb_position')), errors='coerce')
    rsi = pd.to_numeric(feats.apply(lambda x: x.get('rsi')), errors='coerce')
    bbw = pd.to_numeric(feats.apply(lambda x: x.get('bbw_a_bps')), errors='coerce')
    edp = pd.to_numeric(feats.apply(lambda x: x.get('ema20_dist_pct')), errors='coerce').abs()
    err = pd.to_numeric(feats.apply(lambda x: x.get('echo_range_ratio')), errors='coerce')
    mask = (
        (cdf['direction'] == 'short') &
        (cdf['session_label'] == 'overlap') &
        (bb >= 0.10) & (bb < 0.35) &
        (rsi >= 30) & (rsi < 45) &
        (edp >= 10) & (edp < 30) &
        (bbw >= 5) & (bbw < 15) &
        (err >= 1.0) & (err < 1.4)
    )
    n = int(mask.sum())
    if n: matches_total += n; years_checked.append((Path(f).stem, n))
print(f"  Total EUR_USD corpus rows matching MS-001 strict bins: {matches_total}")
for y, n in years_checked:
    print(f"    {y}: {n}")
