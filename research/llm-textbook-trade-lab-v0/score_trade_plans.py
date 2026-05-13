from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
import numpy as np
CACHE=Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT=Path("/home/ubuntu/mr-scrooge-v3/research/llm-textbook-trade-lab-v0")

def pip_size(pair): return 0.01 if pair.endswith("JPY") else 0.0001

def load(pair):
    path=CACHE/pair/f"{pair}_M5_2025-01-01_2026-01-01.jsonl"; rows=[]
    with path.open() as f:
        for line in f:
            if line.strip(): rows.append(json.loads(line))
    df=pd.DataFrame(rows); df["time"]=pd.to_datetime(df.time,utc=True); return df.sort_values("time").reset_index(drop=True)

def load_index(): return pd.read_csv(OUT/"context_index.csv")

def score(plan, meta, df):
    pair=meta["pair"]; ps=pip_size(pair); ts=pd.Timestamp(meta["timestamp"])
    i=df.index[df.time==ts][0]
    entry_i=i+1
    if entry_i>=len(df): return None
    horizon=df.iloc[entry_i:entry_i+96].copy() # 8h
    first=df.iloc[entry_i]
    direction=plan["direction"]
    stop_pips=float(plan["stop_pips"]); target_R=float(plan.get("target_R",2.0)); target_pips=stop_pips*target_R
    if direction=="long":
        entry=float(first.open_ask); stop=entry-stop_pips*ps; target=entry+target_pips*ps
        mfe_pips=(horizon.high_bid.max()-entry)/ps; mae_pips=(entry-horizon.low_bid.min())/ps
        outcome="time_exit"; realized=None; hit_time=None
        for r in horizon.itertuples(index=False):
            hit_stop=r.low_bid<=stop; hit_target=r.high_bid>=target
            if hit_stop and hit_target: outcome="stop_first_same_bar"; realized=-1.0; hit_time=r.time; break
            if hit_stop: outcome="stop"; realized=-1.0; hit_time=r.time; break
            if hit_target: outcome="target"; realized=target_R; hit_time=r.time; break
        if realized is None:
            realized=(float(horizon.iloc[-1].close_bid)-entry)/(stop_pips*ps)
    else:
        entry=float(first.open_bid); stop=entry+stop_pips*ps; target=entry-target_pips*ps
        mfe_pips=(entry-horizon.low_ask.min())/ps; mae_pips=(horizon.high_ask.max()-entry)/ps
        outcome="time_exit"; realized=None; hit_time=None
        for r in horizon.itertuples(index=False):
            hit_stop=r.high_ask>=stop; hit_target=r.low_ask<=target
            if hit_stop and hit_target: outcome="stop_first_same_bar"; realized=-1.0; hit_time=r.time; break
            if hit_stop: outcome="stop"; realized=-1.0; hit_time=r.time; break
            if hit_target: outcome="target"; realized=target_R; hit_time=r.time; break
        if realized is None:
            realized=(entry-float(horizon.iloc[-1].close_ask))/(stop_pips*ps)
    return {"context_id":plan["context_id"],"pair":pair,"timestamp":meta["timestamp"],"decision":"TAKE","direction":direction,"setup_type":plan["setup_type"],"entry_price":entry,"stop_pips":stop_pips,"target_R":target_R,"mfe_R":mfe_pips/stop_pips,"mae_R":mae_pips/stop_pips,"outcome":outcome,"realized_R":realized,"hit_time":str(hit_time) if hit_time is not None else "","reason":plan["reason"]}

def main():
    idx=load_index().set_index("context_id").to_dict("index")
    plans=[json.loads(x) for x in (OUT/"trade_plans_v0.jsonl").read_text().splitlines() if x.strip()]
    cache={}; rows=[]; skips=[]
    for p in plans:
        if p["decision"]!="TAKE":
            m=idx[p["context_id"]]; skips.append({"context_id":p["context_id"],"pair":m["pair"],"timestamp":m["timestamp"],"decision":"SKIP","reason":p["reason"]}); continue
        pair=idx[p["context_id"]]["pair"]
        if pair not in cache: cache[pair]=load(pair)
        rows.append(score(p,idx[p["context_id"]],cache[pair]))
    scored=pd.DataFrame(rows); skipped=pd.DataFrame(skips)
    scored.to_csv(OUT/"textbook_trade_scores.csv",index=False); skipped.to_csv(OUT/"textbook_skips.csv",index=False)
    print(scored.to_string(index=False))
    print("\nsummary")
    if len(scored): print(scored.groupby(["setup_type","outcome"]).size().to_string())
if __name__=="__main__": main()
