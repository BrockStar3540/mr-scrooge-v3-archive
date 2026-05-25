"""Bar-data loader for replay lab.

Pulls M5 / H1 / D candles from OANDA (same source as live bot) and caches
to parquet at research/replay_lab/cache/{symbol}_{tf}_{from}_{to}.parquet.

Returns frames in backtesting.py's expected format:
    DatetimeIndex
    Columns: Open, High, Low, Close, Volume
Plus auxiliary columns: spread (estimated, see spread_mode).
"""
from __future__ import annotations
import os
import logging
from pathlib import Path
from datetime import datetime, timezone, timedelta

import pandas as pd
import requests

log = logging.getLogger("replay_lab.data_adapter")

CACHE_DIR = Path("/home/ubuntu/mr-scrooge-v3/research/replay_lab/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

# Read OANDA creds from .env once
def _oanda_env():
    env = {}
    p = Path("/home/ubuntu/mr-scrooge-v3/.env")
    if p.exists():
        for line in p.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env

_ENV = _oanda_env()
_HEADERS = {"Authorization": f"Bearer {_ENV.get('OANDA_API_TOKEN','')}"}
_API = _ENV.get("OANDA_API_URL", "https://api-fxpractice.oanda.com")


def _cache_path(symbol: str, tf: str, dt_from: str, dt_to: str) -> Path:
    safe = lambda s: s.replace(":", "").replace("-", "").replace("T", "_").replace("Z","")
    return CACHE_DIR / f"{symbol}_{tf}_{safe(dt_from)}_{safe(dt_to)}.parquet"


def _fetch_oanda(symbol: str, tf: str, dt_from: str, dt_to: str) -> pd.DataFrame:
    """Fetch in chunks (OANDA limits to 5000 candles per call).

    Outbound chunk size per timeframe: M5 = 10 days, H1 = 60 days,
    D = 365 days. Both bounds passed each call; advance after success.
    """
    chunk_days = {"M5": 10, "M15": 30, "H1": 60, "H4": 240, "D": 365}.get(tf, 30)
    url = f"{_API}/v3/instruments/{symbol}/candles"

    start_dt = pd.Timestamp(dt_from)
    end_dt = pd.Timestamp(dt_to)
    chunks = []
    cur_start = start_dt

    while cur_start < end_dt:
        cur_end = min(cur_start + pd.Timedelta(days=chunk_days), end_dt)
        params = {
            "granularity": tf,
            "from": cur_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": cur_end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "price": "M",
        }
        data = None
        for attempt in range(5):
            try:
                r = requests.get(url, headers=_HEADERS, params=params, timeout=30)
                if r.status_code == 400:
                    log.warning("OANDA 400 (likely chunk too big): %s", r.text[:200])
                    break
                if r.status_code >= 500:
                    log.warning("OANDA %d on attempt %d, retrying...", r.status_code, attempt+1)
                    import time; time.sleep(1 + attempt)
                    continue
                data = r.json()
                break
            except Exception as e:
                log.warning("fetch attempt %d failed: %s", attempt+1, e)
                import time; time.sleep(1 + attempt)
        if data is None:
            log.error("OANDA exhausted retries for %s %s %s", symbol, tf, cur_start)
            cur_start = cur_end
            continue
        candles = data.get("candles", [])
        rows = []
        for c in candles:
            if not c.get("complete", True):
                continue
            m = c["mid"]
            rows.append({
                "time": pd.Timestamp(c["time"]).tz_convert("UTC"),
                "Open": float(m["o"]), "High": float(m["h"]),
                "Low": float(m["l"]), "Close": float(m["c"]),
                "Volume": int(c.get("volume", 0)),
            })
        if rows:
            chunks.append(pd.DataFrame(rows).set_index("time"))
        cur_start = cur_end
    if not chunks:
        return pd.DataFrame(columns=["Open","High","Low","Close","Volume"])
    df = pd.concat(chunks)
    df = df[~df.index.duplicated(keep="first")].sort_index()
    return df


def load_symbol_ohlc(
    symbol: str,
    timeframe: str = "M5",
    date_from: str | None = None,
    date_to: str | None = None,
    use_cache: bool = True,
) -> pd.DataFrame:
    """Load OHLC bars for one symbol/timeframe across a date range.

    date_from / date_to default to last 30 days if None.
    """
    if date_to is None:
        date_to = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if date_from is None:
        date_from = (datetime.now(timezone.utc) - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    cache = _cache_path(symbol, timeframe, date_from, date_to)
    if use_cache and cache.exists():
        log.info("cache hit: %s", cache.name)
        return pd.read_parquet(cache)
    log.info("fetching OANDA: %s %s %s -> %s", symbol, timeframe, date_from, date_to)
    df = _fetch_oanda(symbol, timeframe, date_from, date_to)
    if not df.empty:
        df.to_parquet(cache)
    return df


def attach_spread_column(
    df: pd.DataFrame,
    symbol: str,
    spread_mode: str = "realistic",
) -> pd.DataFrame:
    """Add a 'spread' column in pips."""
    if df.empty:
        return df
    pip = 0.01 if any(j in symbol for j in ("JPY", "MXN")) else 0.0001
    if spread_mode == "idealized":
        spread_pips = 0.0
    elif spread_mode == "wide":
        spread_pips = 3.0
    else:  # realistic
        # Crude per-pair estimate matching OANDA practice account typical spreads
        spread_map = {
            "EUR_USD": 0.8, "GBP_USD": 1.4, "USD_JPY": 0.8, "USD_CHF": 1.6,
            "USD_CAD": 1.4, "AUD_USD": 1.0, "NZD_USD": 1.4,
            "EUR_JPY": 1.2, "GBP_JPY": 1.8, "CHF_JPY": 2.0, "AUD_JPY": 1.6,
            "CAD_JPY": 1.8, "NZD_JPY": 2.2,
            "EUR_GBP": 1.4, "EUR_CHF": 1.8, "EUR_AUD": 1.8, "EUR_CAD": 2.0,
            "GBP_AUD": 2.4, "GBP_CHF": 2.6, "AUD_CAD": 2.2, "AUD_NZD": 2.4,
        }
        spread_pips = spread_map.get(symbol, 2.0)
    out = df.copy()
    out["spread"] = spread_pips * pip
    return out


def load_symbol_replay_bundle(
    symbol: str,
    date_from: str | None = None,
    date_to: str | None = None,
    spread_mode: str = "realistic",
) -> dict:
    """Load all timeframes needed for one symbol replay."""
    bundle = {}
    for tf in ("M5", "H1", "D"):
        df = load_symbol_ohlc(symbol, tf, date_from, date_to)
        bundle[tf] = df
    if not bundle["M5"].empty:
        bundle["M5"] = attach_spread_column(bundle["M5"], symbol, spread_mode)
    return bundle
