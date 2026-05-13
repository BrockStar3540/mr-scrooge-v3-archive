"""Generate blind historical chart-context dossiers for LLM textbook trade design.

Only pre-decision data is written to contexts. Outcomes are intentionally not
included here; scoring happens after trade plans are written.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np
import pandas as pd

CACHE = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/llm-textbook-trade-lab-v0")
OUT.mkdir(parents=True, exist_ok=True)

PAIRS = ["EUR_USD", "GBP_USD", "AUD_USD", "NZD_USD", "USD_JPY", "USD_CHF", "AUD_JPY", "EUR_JPY", "GBP_JPY", "AUD_NZD"]
YEAR_FILE = "{pair}_M5_2025-01-01_2026-01-01.jsonl"
PIP = {"JPY": 0.01}

def pip_size(pair: str) -> float:
    return 0.01 if pair.endswith("JPY") else 0.0001

def pair_family(pair: str) -> str:
    if pair in {"EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN"}: return "usd_base"
    if pair.startswith("EUR_"): return "eur_cross"
    if pair.startswith("GBP_"): return "gbp_cross"
    if pair in {"AUD_NZD","AUD_CAD","AUD_CHF","AUD_JPY","NZD_JPY","CAD_JPY","CHF_JPY"}: return "antipodean_cross"
    return "other"

def session_bucket(ts):
    h=ts.hour
    if h>=22 or h<6: return "asia"
    if h<12: return "london"
    if h<16: return "overlap"
    if h<21: return "ny_pm"
    return "rollover"

def session_quarter(ts):
    h,m=ts.hour,ts.minute
    minute=h*60+m
    shifted=minute+(24*60 if h<6 else 0)
    b=session_bucket(ts)
    ranges={"asia":(22*60,30*60),"london":(6*60,12*60),"overlap":(12*60,16*60),"ny_pm":(16*60,21*60),"rollover":(21*60,22*60)}
    st,en=ranges[b]
    if b!="asia": shifted=minute
    q=min(4,max(1,int((shifted-st)//((en-st)/4))+1))
    return f"{b}_q{q}"

def rsi(close, n=14):
    d=close.diff()
    up=d.clip(lower=0).ewm(alpha=1/n, adjust=False).mean()
    dn=(-d.clip(upper=0)).ewm(alpha=1/n, adjust=False).mean()
    rs=up/dn.replace(0,np.nan)
    return 100-(100/(1+rs))

def load_pair(pair):
    path=CACHE/pair/YEAR_FILE.format(pair=pair)
    rows=[]
    with path.open() as f:
        for line in f:
            if line.strip(): rows.append(json.loads(line))
    df=pd.DataFrame(rows)
    df["time"]=pd.to_datetime(df["time"], utc=True)
    df=df.sort_values("time").reset_index(drop=True)
    df["mid_o"]=(df.open_bid+df.open_ask)/2
    df["mid_h"]=(df.high_bid+df.high_ask)/2
    df["mid_l"]=(df.low_bid+df.low_ask)/2
    df["mid_c"]=(df.close_bid+df.close_ask)/2
    ps=pip_size(pair)
    df["spread_pips"]=(df.close_ask-df.close_bid)/ps
    df["ema20"]=df.mid_c.ewm(span=20, adjust=False).mean()
    df["ema50"]=df.mid_c.ewm(span=50, adjust=False).mean()
    ma=df.mid_c.rolling(20).mean(); sd=df.mid_c.rolling(20).std()
    df["bb_mid"]=ma; df["bb_upper"]=ma+2*sd; df["bb_lower"]=ma-2*sd
    df["bb_pos"]=(df.mid_c-df.bb_lower)/(df.bb_upper-df.bb_lower)
    df["bb_width_pips"]=(df.bb_upper-df.bb_lower)/ps
    df["rsi14"]=rsi(df.mid_c)
    tr=pd.concat([(df.mid_h-df.mid_l),(df.mid_h-df.mid_c.shift()).abs(),(df.mid_l-df.mid_c.shift()).abs()],axis=1).max(axis=1)
    df["atr14_pips"]=tr.rolling(14).mean()/ps
    df["ema20_dist_pips"]=(df.mid_c-df.ema20)/ps
    # Prior UTC day range, good enough for this lab.
    day=df.time.dt.floor("D")
    daily=df.groupby(day).agg(day_high=("mid_h","max"), day_low=("mid_l","min"))
    prev=daily.shift(1)
    df["day"]=day
    df=df.join(prev, on="day")
    df["dist_pdh_pips"]=(df.day_high-df.mid_c)/ps
    df["dist_pdl_pips"]=(df.mid_c-df.day_low)/ps
    df["prior_range_pips"]=(df.day_high-df.day_low)/ps
    return df

def event_type(df, i, ps):
    r=df.iloc[i]; p=df.iloc[i-1]
    events=[]
    if p.bb_pos < 0 and 0.05 <= r.bb_pos <= 0.35: events.append("lower_band_reclaim_long")
    if p.bb_pos > 1 and 0.65 <= r.bb_pos <= 0.95: events.append("upper_band_reject_short")
    if abs(r.ema20_dist_pips) <= max(2, 0.15*r.atr14_pips): events.append("ema20_touch_decision")
    if 0 <= r.dist_pdh_pips <= max(3, 0.20*r.atr14_pips): events.append("near_pdh_rail")
    if 0 <= r.dist_pdl_pips <= max(3, 0.20*r.atr14_pips): events.append("near_pdl_rail")
    if r.bb_width_pips <= df.bb_width_pips.iloc[max(0,i-288):i].quantile(0.25) and abs(r.ema20_dist_pips) < 0.25*r.atr14_pips: events.append("compression_decision")
    return events

def summarize_context(pair, df, i, context_id):
    ps=pip_size(pair); r=df.iloc[i]; ts=r.time
    last=df.iloc[i-24:i+1].copy()
    h1=df.set_index("time").iloc[:i+1].resample("1h").agg({"mid_o":"first","mid_h":"max","mid_l":"min","mid_c":"last"}).dropna().tail(12)
    m15=df.set_index("time").iloc[:i+1].resample("15min").agg({"mid_o":"first","mid_h":"max","mid_l":"min","mid_c":"last"}).dropna().tail(16)
    def trend(block):
        if len(block)<2: return "flat"
        delta=(block.mid_c.iloc[-1]-block.mid_c.iloc[0])/ps
        return "up" if delta>0.5*r.atr14_pips else "down" if delta<-0.5*r.atr14_pips else "range"
    events=event_type(df,i,ps)
    lines=[]
    lines.append(f"# {context_id} {pair} {ts.isoformat()}")
    lines.append("")
    lines.append("No future candles are included. Decide TAKE/SKIP from this context only.")
    lines.append("")
    lines.append("## Metadata")
    lines.append(f"- pair: {pair}")
    lines.append(f"- pair_family: {pair_family(pair)}")
    lines.append(f"- session_bucket: {session_bucket(ts)}")
    lines.append(f"- session_quarter: {session_quarter(ts)}")
    lines.append("- candidate_events: " + ", ".join(events))
    lines.append(f"- spread_pips_now: {r.spread_pips:.2f}")
    lines.append("")
    lines.append("## Current Indicators")
    lines.append(f"- close: {r.mid_c:.5f}")
    lines.append(f"- BB pos: {r.bb_pos:.3f} (lower<0.35, middle 0.35-0.65, upper>0.65)")
    lines.append(f"- BB width: {r.bb_width_pips:.1f} pips")
    lines.append(f"- RSI14: {r.rsi14:.1f}")
    lines.append(f"- EMA20 distance: {r.ema20_dist_pips:.1f} pips")
    lines.append(f"- ATR14 M5: {r.atr14_pips:.1f} pips")
    lines.append(f"- Prior-day high distance: {r.dist_pdh_pips:.1f} pips")
    lines.append(f"- Prior-day low distance: {r.dist_pdl_pips:.1f} pips")
    lines.append(f"- Prior-day range: {r.prior_range_pips:.1f} pips")
    lines.append(f"- M15 context: {trend(m15)}")
    lines.append(f"- H1 context: {trend(h1)}")
    lines.append("")
    lines.append("## Last 25 M5 Candles")
    lines.append("time,open,high,low,close,bb_pos,rsi,ema20_dist_pips,spread_pips")
    for x in last.itertuples(index=False):
        lines.append(f"{x.time.isoformat()},{x.mid_o:.5f},{x.mid_h:.5f},{x.mid_l:.5f},{x.mid_c:.5f},{x.bb_pos:.2f},{x.rsi14:.1f},{x.ema20_dist_pips:.1f},{x.spread_pips:.1f}")
    return "\n".join(lines)+"\n"

def main():
    rng=np.random.default_rng(42)
    contexts=[]; meta=[]
    per_pair_target=3
    for pair in PAIRS:
        print("loading", pair)
        df=load_pair(pair)
        valid=df.dropna(subset=["bb_pos","rsi14","atr14_pips","day_high","day_low"]).copy()
        valid=valid[(valid.time.dt.hour != 21) & (valid.spread_pips <= valid.spread_pips.quantile(0.85))]
        idx=[]
        for i in valid.index[300:-2000:3]:
            ev=event_type(df,i,pip_size(pair))
            if ev and session_bucket(df.iloc[i].time) != "rollover": idx.append(i)
        if not idx: continue
        chosen=rng.choice(idx, size=min(per_pair_target,len(idx)), replace=False)
        for i in chosen:
            cid=f"CTX-{len(contexts)+1:03d}"
            text=summarize_context(pair,df,int(i),cid)
            contexts.append((cid,text))
            r=df.iloc[int(i)]
            meta.append({"context_id":cid,"pair":pair,"timestamp":r.time.isoformat(),"session_bucket":session_bucket(r.time),"session_quarter":session_quarter(r.time),"events":";".join(event_type(df,int(i),pip_size(pair)))})
    (OUT/"contexts").mkdir(exist_ok=True)
    for cid,text in contexts:
        (OUT/"contexts"/f"{cid}.md").write_text(text)
    pd.DataFrame(meta).to_csv(OUT/"context_index.csv", index=False)
    print(f"wrote {len(contexts)} contexts")
    print(pd.DataFrame(meta).to_string(index=False))

if __name__ == "__main__": main()
