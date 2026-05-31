#!/usr/bin/env python3
"""Per-trade regime enrichment scaffold (Task #52, partial).

SCOPE: 3 representative pairs (EUR_USD, GBP_USD, USD_JPY).
COMPUTABLE FEATURES from M5 OHLCV-only cache: BB, A5, E20, E50, ADR (5 of 7).
SKIPPED FEATURES: A1 (would need H1 cache lookup), SPR (no spread in cache).

For each Phase 3 trade in these pairs:
  1. Look up M5 bar at EntryTime
  2. Compute 5-of-7 bucket signature
  3. Hamming-distance match to nearest regime centroid (5-of-7 partial match)
  4. Tag trade with assigned regime

Then aggregate (variant × pair × regime) — which variants fire in
which regimes? Are wrong-direction asymmetries regime-uniform or
concentrated?

CAVEAT: 5-of-7 partial match is degraded vs the full 7-feature live
classification. Use directionally; do not promote any (regime ×
variant) cell to live based solely on this analysis.
"""
from pathlib import Path
import pandas as pd
import numpy as np

CACHE = Path("/Volumes/Alien Device/mr-scrooge-v3/research/replay_lab/cache")
RESULTS = Path("/Volumes/Alien Device/mr-scrooge-v3/research/replay_lab/results/spec_sweep_phase3_20260528T181820Z")
MODULES = Path("/home/ubuntu/mr-scrooge-v3/data/per_pair_modules")

PAIRS = ["EUR_USD", "GBP_USD", "USD_JPY"]
STOP_PIPS_DEFAULT = 7.0


def pip_size(pair: str) -> float:
    return 0.01 if "JPY" in pair else 0.0001


def load_m5(pair: str) -> pd.DataFrame:
    """Load full M5 history for a pair."""
    p = CACHE / f"{pair}_M5_20190701_000000_20260525_000000.parquet"
    df = pd.read_parquet(p).reset_index()
    df.columns = [c.lower() if c != "time" else "ts" for c in df.columns]
    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    return df[["ts", "open", "high", "low", "close", "volume"]].sort_values("ts").reset_index(drop=True)


def compute_features(df: pd.DataFrame, pair: str) -> pd.DataFrame:
    """Compute 5 rolling features for bucket assignment."""
    pip = pip_size(pair)
    # ATR(14) on M5
    high_low = df["high"] - df["low"]
    high_pc = (df["high"] - df["close"].shift()).abs()
    low_pc = (df["low"] - df["close"].shift()).abs()
    tr = pd.concat([high_low, high_pc, low_pc], axis=1).max(axis=1)
    df["atr_5m"] = tr.ewm(alpha=1/14, adjust=False).mean()
    df["atr_5m_pips"] = df["atr_5m"] / pip
    # Bollinger (20, 2)
    df["bb_mid"] = df["close"].rolling(20, min_periods=20).mean()
    df["bb_std"] = df["close"].rolling(20, min_periods=20).std()
    df["bb_width_pips"] = (4 * df["bb_std"]) / pip  # upper-lower in pips
    # EMA20 + slope
    df["ema20"] = df["close"].ewm(span=20, adjust=False).mean()
    df["ema20_slope"] = (df["ema20"] - df["ema20"].shift(5)) / pip / 5.0
    # EMA50 + slope
    df["ema50"] = df["close"].ewm(span=50, adjust=False).mean()
    df["ema50_slope"] = (df["ema50"] - df["ema50"].shift(5)) / pip / 5.0
    # ADR consumed (rough — daily range vs 14-day rolling mean range)
    df["date"] = df["ts"].dt.date
    daily = df.groupby("date").agg(daily_hi=("high","max"), daily_lo=("low","min")).reset_index()
    daily["daily_range"] = (daily["daily_hi"] - daily["daily_lo"]) / pip
    daily["adr_14"] = daily["daily_range"].rolling(14, min_periods=14).mean().shift(1)
    df = df.merge(daily[["date","daily_hi","daily_lo","daily_range","adr_14"]], on="date", how="left")
    df["adr_consumed"] = (df[["high","low"]].diff().abs().fillna(0).max(axis=1).cumsum().groupby(df["date"]).cummax() / pip) / df["adr_14"]
    # Cap weirdness
    df["adr_consumed"] = df["adr_consumed"].clip(0, 3.0)
    return df


def bucket_bb(bb_width_pips, stop=STOP_PIPS_DEFAULT):
    if bb_width_pips is None or stop <= 0: return None
    r = bb_width_pips / stop
    if r < 0.7: return "BB0"
    if r < 2.0: return "BB1"
    if r < 2.5: return "BB2"
    return "BB3"

def bucket_a5(atr_5m_pips, stop=STOP_PIPS_DEFAULT):
    if atr_5m_pips is None or stop <= 0: return None
    r = atr_5m_pips / stop
    if r < 0.33: return "A5_0"
    if r < 0.80: return "A5_1"
    if r < 1.20: return "A5_2"
    return "A5_3"

def bucket_e(slope, stop=STOP_PIPS_DEFAULT, prefix="E20"):
    if slope is None or stop <= 0: return None
    norm = slope / stop
    if norm >= 0.50:  return f"{prefix}a"
    if norm >= 0.15:  return f"{prefix}b"
    if norm >= -0.15: return f"{prefix}c"
    if norm >= -0.50: return f"{prefix}d"
    return f"{prefix}e"

def bucket_adr(consumed):
    if consumed is None or pd.isna(consumed): return None
    if consumed < 0.30: return "ADR0"
    if consumed < 0.60: return "ADR1"
    if consumed < 0.90: return "ADR2"
    if consumed < 1.10: return "ADR3"
    if consumed < 1.50: return "ADR4"
    return "ADR5"


def assign_regime(buckets: dict, centroid_df: pd.DataFrame, factors: list[str]) -> str:
    """Hamming-distance match on the 5 available buckets."""
    best_regime, best_matches = None, -1
    for _, row in centroid_df.iterrows():
        matches = sum(1 for f in factors if row[f] == buckets.get(f))
        if matches > best_matches:
            best_matches = matches
            best_regime = row["regime"]
    return best_regime


def load_centroids(pair: str) -> pd.DataFrame:
    """Load per-pair regime centroids."""
    p = MODULES / pair / "regime_centroids.csv"
    return pd.read_csv(p)


# =================================================================
# Main
# =================================================================
print("=" * 100)
print("PER-TRADE REGIME ENRICHMENT SCAFFOLD (Task #52, 5-of-7 features)")
print("=" * 100)

all_enriched = []
for pair in PAIRS:
    print(f"\n{pair}:")
    m5 = load_m5(pair)
    print(f"  M5 bars: {len(m5):,}")
    m5 = compute_features(m5, pair)
    # Bucketize
    m5["BB"] = m5["bb_width_pips"].apply(bucket_bb)
    m5["A5"] = m5["atr_5m_pips"].apply(bucket_a5)
    m5["E20"] = m5["ema20_slope"].apply(lambda s: bucket_e(s, prefix="E20"))
    m5["E50"] = m5["ema50_slope"].apply(lambda s: bucket_e(s, prefix="E50"))
    m5["ADR"] = m5["adr_consumed"].apply(bucket_adr)
    centroids = load_centroids(pair)
    factors = ["BB", "A5", "E20", "E50", "ADR"]  # 5 of 7
    # Assign regime per bar
    m5["regime"] = m5.apply(
        lambda r: assign_regime({f: r[f] for f in factors}, centroids, factors), axis=1
    )
    print(f"  bars with regime tags: {m5['regime'].notna().sum():,}")
    print(f"  regime distribution (% of bars):")
    rd = m5["regime"].value_counts(normalize=True).head(5)
    print(rd.to_string())

    # Load Phase 3 trade outcomes for this pair
    trade_files = list(RESULTS.glob(f"trades_{pair}_*.csv"))
    print(f"  loading {len(trade_files)} variant×direction trade files...")
    pair_trades = []
    for tf in trade_files:
        df = pd.read_csv(tf)
        if len(df) == 0: continue
        parts = tf.stem.split("_")
        # trades_<PAIR1>_<PAIR2>_<VARIANT>_<DIRECTION>.csv
        # PAIR is parts[1]+_+parts[2], DIRECTION is last token
        variant = "_".join(parts[3:-1])
        direction = parts[-1]
        df["variant"] = variant
        df["direction"] = direction
        df["pair"] = pair
        df["EntryTime"] = pd.to_datetime(df["EntryTime"], utc=True)
        pair_trades.append(df[["EntryTime","PnL","variant","pair","direction"]])
    if not pair_trades: continue
    trades = pd.concat(pair_trades, ignore_index=True)

    # Join each trade with the regime of its M5 bar
    merged = pd.merge_asof(
        trades.sort_values("EntryTime"),
        m5[["ts","regime"]].sort_values("ts"),
        left_on="EntryTime", right_on="ts",
        direction="backward", tolerance=pd.Timedelta(minutes=15),
    )
    matched = merged.dropna(subset=["regime"])
    print(f"  trades regime-matched: {len(matched):,}/{len(trades):,} "
          f"({len(matched)/len(trades):.0%})")
    all_enriched.append(matched)

# Aggregate across pairs
enriched = pd.concat(all_enriched, ignore_index=True)
print()
print("=" * 100)
print(f"AGGREGATE: {len(enriched):,} regime-tagged trades across {len(PAIRS)} pairs")
print("=" * 100)

# (variant × pair × regime) firing counts
firing = enriched.groupby(["variant","pair","regime"]).size().reset_index(name="n_trades")
print(f"\nDistinct (variant × pair × regime) cells with firings: {len(firing)}")
print(f"Average n_trades per cell: {firing['n_trades'].mean():.1f}")

# Regime coverage per variant — does each variant fire in many regimes?
breadth = enriched.groupby(["variant","pair"])["regime"].nunique().reset_index(name="n_regimes_fired")
breadth["breadth_pct"] = breadth["n_regimes_fired"] / 20
print(f"\nREGIME BREADTH per (variant × pair):")
print(breadth.groupby("variant")["n_regimes_fired"].agg(["min","mean","max"]).round(1).to_string())

# Wrong-direction asymmetry per regime — does it hold uniformly?
print(f"\nWRONG-DIRECTION ASYMMETRY by regime (for known wrong-dir variants):")
wrong_dir_bases = ["RG1_range_bound_scalp","MR2_bb_reversion","MR5_williams_extreme"]
for base in wrong_dir_bases:
    sub = enriched[enriched["variant"].str.startswith(base)]
    if sub.empty: continue
    by_regime = sub.pivot_table(
        index="regime", columns="direction", values="PnL", aggfunc="sum"
    ).fillna(0)
    if "native" not in by_regime.columns or "reversed" not in by_regime.columns: continue
    by_regime["asym"] = by_regime["reversed"] - by_regime["native"]
    by_regime["reversed_wins"] = by_regime["asym"] > 0
    n_reversed_wins = by_regime["reversed_wins"].sum()
    n_total = len(by_regime)
    print(f"\n  {base}: {n_reversed_wins}/{n_total} regimes prefer reversed")
    print(f"    top-3 regimes by asymmetry:")
    print(by_regime.sort_values("asym", ascending=False).head(3)[["native","reversed","asym"]].round(0).to_string())
