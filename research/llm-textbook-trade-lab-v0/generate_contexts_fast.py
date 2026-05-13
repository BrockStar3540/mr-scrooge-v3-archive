from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd
CACHE=Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT=Path("/home/ubuntu/mr-scrooge-v3/research/llm-textbook-trade-lab-v0")
OUT.mkdir(parents=True, exist_ok=True); (OUT/"contexts").mkdir(exist_ok=True)
PAIRS=["EUR_USD","GBP_USD","AUD_USD","USD_JPY"]

def pip_size(pair): return 0.01 if pair.endswith("JPY") else 0.0001
def pair_family(pair): return "usd_base"
def session_bucket(ts):
    h=ts.hour
    if h>=22 or h<6: return "asia"
    if h<12: return "london"
    if h<16: return "overlap"
    if h<21: return "ny_pm"
    return "rollover"
def session_quarter(ts):
    h,m=ts.hour,ts.minute; minute=h*60+m; shifted=minute+(1440 if h<6 else 0); b=session_bucket(ts)
    ranges={"asia":(1320,1800),"london":(360,720),"overlap":(720,960),"ny_pm":(960,1260),"rollover":(1260,1320)}
    st,en=ranges[b]
    if b!="asia": shifted=minute
    q=min(4,max(1,int((shifted-st)//((en-st)/4))+1)); return f"{b}_q{q}"
def rsi(close,n=14):
    d=close.diff(); up=d.clip(lower=0).ewm(alpha=1/n,adjust=False).mean(); dn=(-d.clip(upper=0)).ewm(alpha=1/n,adjust=False).mean(); return 100-(100/(1+up/dn.replace(0,np.nan)))
def load(pair):
    path=CACHE/pair/f"{pair}_M5_2025-01-01_2026-01-01.jsonl"; rows=[]
    with path.open() as f:
        for line in f:
            if line.strip(): rows.append(json.loads(line))
    df=pd.DataFrame(rows); df["time"]=pd.to_datetime(df.time,utc=True); df=df.sort_values("time").reset_index(drop=True); ps=pip_size(pair)
    for k in ["open","high","low","close"]: df[f"mid_{k[0]}"]=(df[f"{k}_bid"]+df[f"{k}_ask"])/2
    df["spread_pips"]=(df.close_ask-df.close_bid)/ps; df["ema20"]=df.mid_c.ewm(span=20,adjust=False).mean(); df["ema50"]=df.mid_c.ewm(span=50,adjust=False).mean()
    ma=df.mid_c.rolling(20).mean(); sd=df.mid_c.rolling(20).std(); df["bb_mid"]=ma; df["bb_upper"]=ma+2*sd; df["bb_lower"]=ma-2*sd; df["bb_pos"]=(df.mid_c-df.bb_lower)/(df.bb_upper-df.bb_lower); df["bb_width_pips"]=(df.bb_upper-df.bb_lower)/ps
    df["rsi14"]=rsi(df.mid_c); tr=pd.concat([(df.mid_h-df.mid_l),(df.mid_h-df.mid_c.shift()).abs(),(df.mid_l-df.mid_c.shift()).abs()],axis=1).max(axis=1); df["atr14_pips"]=tr.rolling(14).mean()/ps; df["ema20_dist_pips"]=(df.mid_c-df.ema20)/ps
    day=df.time.dt.floor("D"); daily=df.groupby(day).agg(day_high=("mid_h","max"), day_low=("mid_l","min")); prev=daily.shift(1); df["day"]=day; df=df.join(prev,on="day"); df["dist_pdh_pips"]=(df.day_high-df.mid_c)/ps; df["dist_pdl_pips"]=(df.mid_c-df.day_low)/ps; df["prior_range_pips"]=(df.day_high-df.day_low)/ps
    return df
def events_for_row(r,p):
    ev=[]
    if r.bb_pos<0.15 and r.rsi14<45: ev.append("lower_band_pressure")
    if r.bb_pos>0.85 and r.rsi14>55: ev.append("upper_band_pressure")
    if abs(r.ema20_dist_pips)<=max(2,0.18*r.atr14_pips): ev.append("ema20_decision")
    if 0<=r.dist_pdh_pips<=max(4,0.25*r.atr14_pips): ev.append("near_pdh_rail")
    if 0<=r.dist_pdl_pips<=max(4,0.25*r.atr14_pips): ev.append("near_pdl_rail")
    return ev
def trend(df, ps):
    if len(df)<2: return "flat"
    d=(df.mid_c.iloc[-1]-df.mid_c.iloc[0])/ps; atr=10
    return "up" if d>atr else "down" if d<-atr else "range"
def context(pair,df,i,cid):
    ps=pip_size(pair); r=df.iloc[i]; ts=r.time; last=df.iloc[i-24:i+1]
    h1=df.set_index("time").iloc[:i+1].resample("1h").agg({"mid_o":"first","mid_h":"max","mid_l":"min","mid_c":"last"}).dropna().tail(12)
    m15=df.set_index("time").iloc[:i+1].resample("15min").agg({"mid_o":"first","mid_h":"max","mid_l":"min","mid_c":"last"}).dropna().tail(16)
    lines=[f"# {cid} {pair} {ts.isoformat()}","","No future candles are included. Decide TAKE/SKIP from this context only.","","## Metadata",f"- pair: {pair}",f"- pair_family: {pair_family(pair)}",f"- session_bucket: {session_bucket(ts)}",f"- session_quarter: {session_quarter(ts)}","- candidate_events: " + ";".join(events_for_row(r,ps)),f"- spread_pips_now: {r.spread_pips:.2f}","","## Current Indicators",f"- close: {r.mid_c:.5f}",f"- BB pos: {r.bb_pos:.3f}",f"- BB width: {r.bb_width_pips:.1f} pips",f"- RSI14: {r.rsi14:.1f}",f"- EMA20 distance: {r.ema20_dist_pips:.1f} pips",f"- ATR14 M5: {r.atr14_pips:.1f} pips",f"- Prior-day high distance: {r.dist_pdh_pips:.1f} pips",f"- Prior-day low distance: {r.dist_pdl_pips:.1f} pips",f"- Prior-day range: {r.prior_range_pips:.1f} pips",f"- M15 context: {trend(m15,ps)}",f"- H1 context: {trend(h1,ps)}","","## Last 25 M5 Candles","time,open,high,low,close,bb_pos,rsi,ema20_dist_pips,spread_pips"]
    for x in last.itertuples(index=False): lines.append(f"{x.time.isoformat()},{x.mid_o:.5f},{x.mid_h:.5f},{x.mid_l:.5f},{x.mid_c:.5f},{x.bb_pos:.2f},{x.rsi14:.1f},{x.ema20_dist_pips:.1f},{x.spread_pips:.1f}")
    return "\n".join(lines)+"\n"
def main():
    rng=np.random.default_rng(7); meta=[]; cidn=1
    for pair in PAIRS:
        print("loading",pair,flush=True); df=load(pair); valid=df.dropna(subset=["bb_pos","rsi14","atr14_pips","day_high","day_low"])
        mask=(valid.time.dt.hour!=21)&(valid.spread_pips<=valid.spread_pips.quantile(.75))
        evmask=((valid.bb_pos<.15)&(valid.rsi14<45))|((valid.bb_pos>.85)&(valid.rsi14>55))|(valid.ema20_dist_pips.abs()<=np.maximum(2,.18*valid.atr14_pips))|((valid.dist_pdh_pips>=0)&(valid.dist_pdh_pips<=np.maximum(4,.25*valid.atr14_pips)))|((valid.dist_pdl_pips>=0)&(valid.dist_pdl_pips<=np.maximum(4,.25*valid.atr14_pips)))
        idx=valid[mask&evmask].index.to_numpy(); idx=idx[(idx>300)&(idx<len(df)-1000)]
        chosen=rng.choice(idx,size=min(3,len(idx)),replace=False)
        for i in chosen:
            cid=f"CTX-{cidn:03d}"; cidn+=1; r=df.iloc[int(i)]
            (OUT/"contexts"/f"{cid}.md").write_text(context(pair,df,int(i),cid))
            meta.append({"context_id":cid,"pair":pair,"timestamp":r.time.isoformat(),"session_bucket":session_bucket(r.time),"session_quarter":session_quarter(r.time),"events":";".join(events_for_row(r,pip_size(pair)))})
    pd.DataFrame(meta).to_csv(OUT/"context_index.csv",index=False); print(pd.DataFrame(meta).to_string(index=False),flush=True)
if __name__=="__main__": main()
