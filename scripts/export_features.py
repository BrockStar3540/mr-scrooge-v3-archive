#!/usr/bin/env python3
"""
Export raw feature table from OANDA — every trade, every column.
Output: CSV that anyone can verify independently.
Also: split into train/test to check for overfitting.
"""

import os, requests, statistics, time as _t, csv, json, random
from datetime import datetime

API_KEY = os.environ["OANDA_API_KEY"]
ACCT = os.environ["OANDA_ACCOUNT_ID"]
BASE = os.environ.get("OANDA_BASE", "https://api-fxtrade.oanda.com")
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def cndl(pair, gran, to_time, count=50):
    _t.sleep(0.35)
    try:
        r = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS,
                         params={"granularity": gran, "count": str(count), "price": "MBA", "to": to_time}, timeout=10)
        return r.json().get("candles", [])
    except: return []

def ema_c(closes, period):
    if len(closes) < period: return None
    m = 2/(period+1); e = sum(closes[:period])/period
    for p in closes[period:]: e = (p-e)*m + e
    return e

def rsi_c(closes, period=14):
    if len(closes) < period+1: return None
    ch = [closes[i]-closes[i-1] for i in range(1, len(closes))]
    rc = ch[-period:]
    g = sum(c for c in rc if c > 0)/period or 0.0001
    l = sum(-c for c in rc if c < 0)/period or 0.0001
    return round(100-(100/(1+g/l)), 1)

def bb_st(cl):
    if len(cl) < 20: return "UNK"
    s20 = sum(cl[-20:])/20; sd = statistics.stdev(cl[-20:]) if len(cl[-20:])>1 else 0.0001
    ua = s20+2*sd; la = s20-2*sd
    n = min(4,len(cl)); s4 = sum(cl[-n:])/n
    sd4 = statistics.stdev(cl[-n:]) if n>=2 else 0.0001
    ub = s4+4*sd4; lb = s4-4*sd4
    c=cl[-1]; c1=cl[-2] if len(cl)>=2 else c; c2=cl[-3] if len(cl)>=3 else c1
    if c>ub and ub>ua: return "EXT_UP"
    if c<lb and lb<la: return "EXT_DN"
    if c<=ua and (c1>ua or c2>ua): return "REJ_S"
    if c>=la and (c1<la or c2<la): return "REJ_L"
    if c>ua and c1>ua and c>=c1: return "BRK_UP"
    if c<la and c1<la and c<=c1: return "BRK_DN"
    if c>ua: return "STR_UP"
    if c<la: return "STR_DN"
    return "NORM"

def extract(t):
    sym=t["instrument"]; units=float(t["initialUnits"]); entry=float(t["price"])
    pnl=float(t["realizedPL"]); ot=t["openTime"]; ct=t["closeTime"]
    d="S" if units<0 else "L"; pip=0.01 if "JPY" in sym else 0.0001
    try:
        odt=datetime.fromisoformat(ot[:26].replace("Z","+00:00"))
        cdt=datetime.fromisoformat(ct[:26].replace("Z","+00:00"))
        dur=(cdt-odt).total_seconds()/60; hour=odt.hour
    except: dur=0; hour=12
    daily=cndl(sym,"D",ot,15); hourly=cndl(sym,"H1",ot,60); m5=cndl(sym,"M5",ot,80)
    if len(daily)<3 or len(m5)<20 or len(hourly)<20: return None
    ed=ot[:10]; pd=None
    for c in reversed(daily):
        if c["time"][:10]<ed:
            h,l=float(c["mid"]["h"]),float(c["mid"]["l"])
            if (h-l)/l>0.0005: pd=c; break
    if not pd: return None
    pdh=float(pd["mid"]["h"]); pdl=float(pd["mid"]["l"]); bx=pdh-pdl; hf=bx/2
    bxp=bx/pip; bpos=(entry-pdl)/bx if bx>0 else 0.5
    wp=(entry-pdl)/bx if d=="L" else (pdh-entry)/bx; wp=wp if bx>0 else 1
    atrs=[max(float(daily[i]["mid"]["h"])-float(daily[i]["mid"]["l"]),
              abs(float(daily[i]["mid"]["h"])-float(daily[i-1]["mid"]["c"])),
              abs(float(daily[i]["mid"]["l"])-float(daily[i-1]["mid"]["c"])))
          for i in range(1,len(daily))]
    atr=sum(atrs)/len(atrs) if atrs else bx
    tc=daily[-1]["mid"]; adr=(float(tc["h"])-float(tc["l"]))/atr if atr>0 else 0
    try:
        pdt=datetime.fromisoformat(pd["time"][:26].replace("Z","+00:00"))
        bage=(odt-pdt).total_seconds()/3600
    except: bage=24
    la=m5[-1]; ask=float(la.get("ask",{}).get("c",0)); bid=float(la.get("bid",{}).get("c",0))
    sprd=(ask-bid) if ask>0 and bid>0 else pip*2; sp=sprd/pip
    otr_pct=2*sprd/hf*100 if hf>0 else 100
    sig=None; dc=0; mom=0
    for i in range(len(m5)-1, max(len(m5)-8,-1), -1):
        mm=m5[i]["mid"]; o,h,l,c=float(mm["o"]),float(mm["h"]),float(mm["l"]),float(mm["c"])
        if sig is None:
            if (d=="L" and c>o) or (d=="S" and c<o):
                body=abs(c-o) or pip*0.1; rng=h-l or pip*0.1
                wk=(min(o,c)-l) if d=="L" else (h-max(o,c))
                sig={"low":l,"high":h,"wick_r":wk/body,"body_pct":body/rng}
                stype="JW" if wk/body>=1.5 and body/rng<=0.30 else "STD"
        else:
            if (d=="L" and c<o) or (d=="S" and c>o): dc+=1
            else: break
    for i in range(len(m5)-2, max(len(m5)-12,-1), -1):
        mm=m5[i]["mid"]; c,o=float(mm["c"]),float(mm["o"])
        if (d=="L" and c<o) or (d=="S" and c>o): mom+=1
        else: break
    if sig:
        if d=="L": ns=(entry-(sig["low"]-2*pip))/pip
        else: ns=((sig["high"]+2*pip)-entry)/pip
        bp=sig["body_pct"]
    else: ns=10; bp=0.5; stype="?"
    c1h=[float(c["mid"]["c"]) for c in hourly[-20:]]; mn=sum(c1h)/len(c1h)
    sd=statistics.stdev(c1h) if len(c1h)>1 else 0.0001; zs=(entry-mn)/sd if sd>0 else 0
    ub=mn+2*sd; lb=mn-2*sd; w=ub-lb; bbp=(entry-lb)/w if w>0 else 0.5
    c5m=[float(c["mid"]["c"]) for c in m5[-25:]]; bbs=bb_st(c5m)
    sma20=sum(c5m[-20:])/20 if len(c5m)>=20 else entry; sma_d=(entry-sma20)/pip
    cr5=[float(c["mid"]["c"]) for c in m5[-15:]]; rsi=rsi_c(cr5) or 50
    ah=[float(c["mid"]["c"]) for c in hourly]; e50=ema_c(ah,50); e20=ema_c(ah,20)
    e50d=abs(entry-e50)/bx*100 if e50 and bx>0 else 50
    e20d=abs(entry-e20)/bx*100 if e20 and bx>0 else 50
    is_ct=(d=="L" and entry>(e50 or 0)) or (d=="S" and entry<(e50 or 999999)) if e50 else False
    if len(ah)>=10: sl=(sum(ah[-5:])/5-sum(ah[-10:-5])/5)/(sum(ah[-10:-5])/5)*100
    else: sl=0
    is_rng=abs(sl)<0.02
    if len(m5)>=20:
        rr=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-5:]]
        ro=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-20:-5]]
        vr=(sum(rr)/5)/(sum(ro)/15) if sum(ro)>0 else 1
    else: vr=1
    dalign=any(abs(entry-dl)/dl<0.002 for dl in [pdh,pdl]); zt=1 if dalign else 3
    tch_buf=abs(pdh)*0.001
    tch=sum(1 for h in hourly[-24:] if abs(float(h["mid"]["h"])-pdh)<=tch_buf or abs(float(h["mid"]["l"])-pdl)<=tch_buf)

    return {
        "trade_id": t.get("id",""), "sym": sym, "d": d, "entry": entry,
        "pnl": round(pnl,2), "won": 1 if pnl>0 else 0,
        "open_time": ot[:19], "close_time": ct[:19],
        "hour": hour, "bage": round(bage,1), "dur": round(dur,1),
        "bxp": round(bxp,1), "bpos": round(bpos,3), "wp": round(wp,3),
        "adr": round(adr,3), "otr": round(otr_pct,1), "sp": round(sp,2),
        "ns": round(ns,1), "dc": dc, "mom": mom,
        "sma_d": round(sma_d,2), "bbp": round(bbp,3), "zs": round(zs,3),
        "rsi": round(rsi,1), "bbs": bbs, "stype": stype,
        "e50d": round(e50d,1), "e20d": round(e20d,1),
        "sl": round(sl,4), "is_rng": 1 if is_rng else 0,
        "is_ct": 1 if is_ct else 0, "vr": round(vr,2),
        "bp": round(bp,3), "zt": zt, "tch": tch,
    }


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state":"CLOSED","count":"50"})
    trades = r.json().get("trades",[])
    print(f"Extracting features for {len(trades)} trades from raw OANDA data...")

    results = []
    for i,t in enumerate(trades):
        sym = t.get("instrument","")
        print(f"  [{i+1}/{len(trades)}] {sym}...", end="", flush=True)
        try:
            a = extract(t)
            if a: results.append(a); print(" OK")
            else: print(" skip")
        except Exception as e: print(f" err: {e}")

    # Write full CSV
    outpath = "/tmp/trades_features.csv"
    if results:
        keys = list(results[0].keys())
        with open(outpath, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(results)
        print(f"\nExported {len(results)} trades to {outpath}")
        print(f"Columns: {', '.join(keys)}")

    # Also write JSONL
    jsonpath = "/tmp/trades_features.jsonl"
    with open(jsonpath, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    print(f"Also exported to {jsonpath}")

    # Train/test split (chronological — first 60% train, last 40% test)
    results_sorted = sorted(results, key=lambda x: x["open_time"])
    split = int(len(results_sorted) * 0.6)
    train = results_sorted[:split]
    test = results_sorted[split:]

    train_path = "/tmp/trades_train.csv"
    test_path = "/tmp/trades_test.csv"
    for data, path in [(train, train_path), (test, test_path)]:
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(data)

    tw = sum(1 for r in train if r["won"]); tl = len(train) - tw
    tsw = sum(1 for r in test if r["won"]); tsl = len(test) - tsw
    print(f"\nTrain set: {len(train)} trades ({tw}W/{tl}L) → {train_path}")
    print(f"Test set:  {len(test)} trades ({tsw}W/{tsl}L) → {test_path}")
    print(f"Split: chronological (train=older, test=newer)")


if __name__ == "__main__":
    main()
