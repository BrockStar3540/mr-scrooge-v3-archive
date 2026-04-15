#!/usr/bin/env python3
"""
V3 FINAL FORMULA — Every factor weighted by proportional gap strength.
Points assigned proportionally to how much each factor separates W from L.
Run against ALL raw OANDA trades. Show EVERY component for EVERY trade.
"""

import os, requests, statistics, time as _t, json
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
                if wk/body>=1.5 and body/rng<=0.30: stype="JW"
                else: stype="STD"
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

    c1h=[float(c["mid"]["c"]) for c in hourly[-20:]]
    mn=sum(c1h)/len(c1h); sd=statistics.stdev(c1h) if len(c1h)>1 else 0.0001
    zs=(entry-mn)/sd if sd>0 else 0
    ub=mn+2*sd; lb=mn-2*sd; w=ub-lb; bbp=(entry-lb)/w if w>0 else 0.5

    c5m=[float(c["mid"]["c"]) for c in m5[-25:]]
    bbs=bb_st(c5m)
    sma20=sum(c5m[-20:])/20 if len(c5m)>=20 else entry
    sma_d=(entry-sma20)/pip

    cr5=[float(c["mid"]["c"]) for c in m5[-15:]]; rsi=rsi_c(cr5) or 50

    ah=[float(c["mid"]["c"]) for c in hourly]
    e20=ema_c(ah,20); e50=ema_c(ah,50)
    e20d=abs(entry-e20)/bx*100 if e20 and bx>0 else 50
    e50d=abs(entry-e50)/bx*100 if e50 and bx>0 else 50
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

    return {
        "sym":sym,"d":d,"pnl":pnl,"won":pnl>0,"zt":zt,"stype":stype,
        "hour":hour,"bage":bage,"vr":vr,"is_rng":is_rng,"bbs":bbs,
        "dc":dc,"mom":mom,"sma_d":sma_d,"ns":ns,"e50d":e50d,"e20d":e20d,
        "wp":wp,"bbp":bbp,"zs":zs,"rsi":rsi,"is_ct":is_ct,"adr":adr,
        "bxp":bxp,"sp":sp,"otr":otr_pct,"bp":bp,"dur":dur,"sl":sl,"bpos":bpos,
    }


def score_v3_final(r):
    """
    V3 FINAL FORMULA — every factor weighted by proportional gap data.
    Points are proportional to the gap magnitude from the analysis.
    Sorted by signal strength (strongest factors get most points).
    """
    s = 0
    bd = {}  # breakdown
    blocks = []

    # ================================================================
    # LAYER 0: HARD BLOCKS (data-proven kill zones)
    # ================================================================
    # Natural stop invalid (43% WR, -9% gap)
    if r["ns"] <= 0:
        blocks.append("INVALID_SL")
    # Spread exceeds stop (50% WR, -8% gap)
    if r["ns"] > 0 and r["sp"] > r["ns"]:
        blocks.append("SPRD>SL")
    # BB STRETCH (0% WR, -14% loser gap, -5% loser gap)
    if r["bbs"] in ("STR_UP", "STR_DN"):
        blocks.append("BB_STRETCH")
    # RSI neutral 45-55 (29% WR z-score, -7% gap on 40-50 bucket)
    if 45 <= r["rsi"] <= 55:
        blocks.append("RSI_NEUT")

    if blocks:
        return 0, {"BLOCKED": ",".join(blocks)}, blocks

    # ================================================================
    # FACTOR 1: BOX AGE — Gap: +37% / -38% (STRONGEST)
    # 52% of W in <12h vs 14% of L → +37% gap
    # 38% of W in 12-24h vs 76% of L → -38% gap
    # ================================================================
    if r["bage"] < 12:
        p = 12  # proportional to 37% gap
    elif r["bage"] < 24:
        p = -12  # proportional to 38% gap
    elif r["bage"] < 48:
        p = -5
    else:
        p = -3
    s += p; bd["age"] = p

    # ================================================================
    # FACTOR 2: ENTRY HOUR — Gap: +39% / -23%
    # 48% of W at 0-7 UTC vs 10% of L → +39% gap (88% WR)
    # 34% of W at 12-19 vs 57% of L → -23% gap (45% WR)
    # ================================================================
    h = r["hour"]
    if h < 8:
        p = 10  # proportional to 39% gap
    elif h < 12:
        p = 0
    elif h < 20:
        p = -7  # proportional to 23% gap
    else:
        p = -8  # 20-23: -13% gap, 38% WR
    s += p; bd["hr"] = p

    # ================================================================
    # FACTOR 3: VOLUME RATIO — Gap: +22% / -14%
    # 31% of W at 0.9-1.1 vs 10% of L → +22% gap (82% WR)
    # 38% of W at 0.7-0.9 vs 48% of L → -14% gap (47% WR)
    # ================================================================
    v = r["vr"]
    if 0.9 <= v <= 1.1:
        p = 7  # proportional to 22% gap
    elif v > 1.5:
        p = -6  # proportional to 9% gap + 43% WR
    elif v < 0.7:
        p = -3
    elif 0.7 <= v < 0.9:
        p = -4  # proportional to 14% gap
    else:  # 1.1-1.5
        p = -1
    s += p; bd["vol"] = p

    # ================================================================
    # FACTOR 4: OTR — Gap: -20% at <8% (LOSERS cluster at low OTR!)
    # Only 3% of W at <8% vs 24% of L → -20% gap (17% WR!!)
    # 76% of W at 8-18% vs 62% of L → +14% gap
    # ================================================================
    o = r["otr"]
    if o < 8:
        p = -8  # proportional to 20% gap, 17% WR — DANGER
    elif 8 <= o <= 18:
        p = 4  # proportional to 14% gap
    elif o > 25:
        p = 1  # small sample but 67% WR
    else:
        p = 0
    s += p; bd["otr"] = p

    # ================================================================
    # FACTOR 5: NATURAL STOP — Gap: +20% at 1-6p / -9% at <=0
    # 69% of W at 1-6p vs 52% of L → +17% gap (65% WR)
    # Sweet spot 4-6p: 48% of W vs 29% of L → +20% gap (70% WR)
    # ================================================================
    ns = r["ns"]
    if 4 <= ns <= 6:
        p = 6  # proportional to 20% gap
    elif 1 <= ns < 4:
        p = 2
    elif 7 <= ns <= 11:
        p = -1
    elif ns >= 12:
        p = -4  # -3% gap but 50% WR
    else:
        p = 0  # should be blocked above
    s += p; bd["stp"] = p

    # ================================================================
    # FACTOR 6: EMA50 DISTANCE — Gap: -16% at <20%
    # Only 3% of W at <20% vs 19% of L → -16% gap (20% WR!)
    # 59% of W at 60%+ vs 48% of L → +11% gap
    # ================================================================
    if r["e50d"] < 20:
        p = -7  # proportional to 16% gap, 20% WR
    elif r["e50d"] >= 60:
        p = 3  # proportional to 11% gap
    else:
        p = 0
    s += p; bd["e50"] = p

    # ================================================================
    # FACTOR 7: EMA20 DISTANCE — Gap: -17% at <15%
    # 31% of W at <15% vs 48% of L → -17% gap (47% WR)
    # 38% of W at 15-30% vs 24% of L → +14% gap (69% WR)
    # ================================================================
    if r["e20d"] < 15:
        p = -5  # proportional to 17% gap
    elif 15 <= r["e20d"] <= 30:
        p = 4  # proportional to 14% gap
    else:
        p = 0
    s += p; bd["e20"] = p

    # ================================================================
    # FACTOR 8: DIRECTIONAL CANDLES — Gap: +12% at 4+ / -12% at 0
    # 17% of W at 4+ vs 5% of L → +12% gap (83% WR)
    # 31% of W at 0 vs 43% of L → -12% gap (50% WR)
    # ================================================================
    dc = r["dc"]
    if dc >= 4:
        p = 15  # +12% gap but 83% WR makes this high-value
    elif dc == 3:
        p = 5
    elif dc == 2:
        p = 3
    elif dc == 1:
        p = 0
    else:  # 0
        p = -10  # -12% gap, 50% WR = coin flip
    s += p; bd["cnv"] = p

    # ================================================================
    # FACTOR 9: MOMENTUM CANDLES — Gap: +11% at 2 / -13% at 0
    # 21% of W at 2 vs 10% of L → +11% gap (75% WR)
    # 34% of W at 0 vs 48% of L → -13% gap (50% WR)
    # ================================================================
    mm = r["mom"]
    if mm >= 3:
        p = 5
    elif mm == 2:
        p = 4  # proportional to 11% gap
    elif mm == 0:
        p = -4  # proportional to 13% gap (but overlaps with dc=0)
    else:
        p = 0
    s += p; bd["mom"] = p

    # ================================================================
    # FACTOR 10: Z-SCORE — Gap: +18% at 0.5-1.5 / -17% NEUTRAL
    # 52% of W at 0.5-1.5 vs 33% of L → +18% gap (68% WR)
    # 7% of W at neutral vs 24% of L → -17% gap (29% WR)
    # ================================================================
    az = abs(r["zs"])
    if 0.5 <= az <= 1.5:
        p = 5  # proportional to 18% gap
    elif az >= 2.0:
        p = 6  # strong extension
    elif az >= 1.5:
        p = 4
    elif az < 0.5:
        p = -5  # proportional to 17% gap, 29% WR
    else:
        p = 0
    s += p; bd["z"] = p

    # ================================================================
    # FACTOR 11: SMA20 DISTANCE — Gap: -10% above 5-20p
    # 14% of W above 5-20p vs 24% of L → -10% gap (44% WR)
    # 55% of W at SMA vs 48% of L → +8% gap
    # ================================================================
    sd = r["sma_d"]
    if sd < -5:
        p = 3  # below SMA = good
    elif -5 <= sd <= 5:
        p = 2  # at SMA = slightly good
    elif 5 < sd <= 20:
        p = -5  # proportional to 10% gap, 44% WR
    else:
        p = -3  # well above
    s += p; bd["sma"] = p

    # ================================================================
    # FACTOR 12: BB POSITION — Gap: +16% at 0.65+ / -10% at 0.35-0.65
    # 45% of W at 0.65-0.85 vs 29% of L → +16% gap (68% WR)
    # 14% of W at 0.35-0.65 vs 24% of L → -10% gap (44% WR)
    # ================================================================
    bb = r["bbp"]
    if 0.15 <= bb <= 0.35:
        p = 3  # +8% gap, 71% WR
    elif 0.35 <= bb <= 0.50:
        p = -5  # -6% gap, 33% WR
    elif 0.65 <= bb <= 0.85:
        p = 4  # +16% gap, 68% WR
    elif bb > 0.85:
        p = -2  # -8% gap, 50% WR
    elif bb < 0.15:
        p = -3  # -6% gap, 33% WR
    else:  # 0.50-0.65
        p = -2
    s += p; bd["bb"] = p

    # ================================================================
    # FACTOR 13: WALL PROXIMITY — Gap: -17% at 0.15-0.30
    # 7% of W at 0.15-0.30 vs 24% of L → -17% gap (29% WR!)
    # 14% of W at 0.30-0.50 vs 5% of L → +9% gap (80% WR)
    # ================================================================
    wp = r["wp"]
    if wp < 0.15:
        p = 1  # 55% WR, small positive
    elif 0.15 <= wp < 0.30:
        p = -5  # -17% gap, 29% WR — DANGER
    elif 0.30 <= wp < 0.50:
        p = 3  # +9% gap, 80% WR
    else:
        p = 0  # 0.50-0.70 is neutral
    s += p; bd["wal"] = p

    # ================================================================
    # FACTOR 14: BODY % — Gap: -22% at 45-65%
    # 21% of W at 45-65% vs 43% of L → -22% gap (40% WR!)
    # 21% of W at <25% vs 10% of L → +11% gap (75% WR)
    # ================================================================
    if r["bp"] < 0.25:
        p = 3  # doji = +11% gap
    elif 0.45 <= r["bp"] <= 0.65:
        p = -4  # -22% gap, 40% WR — momentum candle, not reversal
    else:
        p = 0
    s += p; bd["bdy"] = p

    # ================================================================
    # FACTOR 15: RSI (beyond hard block) — Gap: +9% at <40
    # 28% of W at <40 vs 19% of L → +9% gap (67% WR)
    # 28% of W at 55-75 vs 38% of L → -11% gap (50% WR)
    # ================================================================
    rsi = r["rsi"]
    if rsi < 30:
        p = 4
    elif 30 <= rsi < 40:
        p = 3  # +9% gap
    elif 55 <= rsi < 75:
        p = -3  # -11% gap
    elif rsi >= 75:
        p = 1  # overbought for shorts
    else:
        p = 0
    s += p; bd["rsi"] = p

    # ================================================================
    # FACTOR 16: BB STATE BONUS — Gap: +6% REJECTION
    # 10% of W at REJ_L vs 5% of L → +6% gap (75% WR)
    # ================================================================
    if r["bbs"] in ("REJ_L", "REJ_S"):
        p = 3
        s += p; bd["bbr"] = p

    # ================================================================
    # FACTOR 17: RANGING — PF 0.33 from April audit (225 trades)
    # Only 10% of trades are ranging in V1 sample — keep large penalty
    # ================================================================
    if r["is_rng"]:
        p = -15
        s += p; bd["rng"] = p

    # ================================================================
    # FACTOR 18: ADR CONSUMED — Gap: +17% at 60-80%
    # 31% of W at 60-80% vs 14% of L → +17% gap (75% WR)
    # 17% of W at 80-100% vs 29% of L → -11% gap (45% WR)
    # ================================================================
    adr = r["adr"]
    if 0.60 <= adr <= 0.80:
        p = 4
    elif 0.80 <= adr <= 1.0:
        p = -3
    elif 0.35 <= adr < 0.60:
        p = 1
    else:
        p = 0
    s += p; bd["adr"] = p

    # ================================================================
    # FACTOR 19: ZONE TIER — Gap: ~0% (doesn't differentiate on V1!)
    # But theory says T1 > T2 > T3. Keep modest weight.
    # ================================================================
    zt = {1: 8, 2: 5, 3: 3, 4: 1}.get(r["zt"], 1)
    s += zt; bd["zon"] = zt

    # ================================================================
    # FACTOR 20: PATTERN TYPE — Gap: -10% JW on V1 (reversed from V2!)
    # Keep from April audit (511 trades) — JW=+15, STD=+8
    # V1 live sample too small and contradicts larger dataset
    # ================================================================
    pt = {"JW": 10, "STD": 6}.get(r["stype"], 6)
    s += pt; bd["pat"] = pt

    # ================================================================
    # FACTOR 21: Z-ALIGN BONUS — r=0.38 with P&L (April audit)
    # ================================================================
    if (r["d"]=="L" and r["zs"]<-0.5) or (r["d"]=="S" and r["zs"]>0.5):
        s += 3; bd["za"] = 3

    # ================================================================
    # FACTOR 22: COUNTER-TREND (from April audit, 511 trades)
    # V1 live: only 4 CT trades, can't calibrate. Keep audit weights.
    # ================================================================
    if r["is_ct"]:
        if r["zt"] == 1:
            s -= 7; bd["ct1"] = -7
        elif r["zt"] == 2:
            s += 3; bd["ct2"] = 3

    # ================================================================
    # FACTOR 23: EMA SLOPE — Gap: +10% mild up / -13% mild down
    # 24% of W at 0.02-0.1 vs 14% of L → +10% gap (70% WR)
    # 10% of W at -0.1 to -0.02 vs 24% of L → -13% gap (38% WR)
    # ================================================================
    if 0.02 <= r["sl"] <= 0.1:
        p = 3
    elif -0.1 <= r["sl"] < -0.02:
        p = -4  # -13% gap, 38% WR
    elif r["sl"] < -0.1:
        p = -1
    else:
        p = 0
    s += p; bd["slp"] = p

    # ================================================================
    # FACTOR 24: BOX SIZE — Gap: -7% at 200p+
    # 7% of W at 200p+ vs 14% of L → -7% gap (40% WR)
    # ================================================================
    if r["bxp"] > 200:
        p = -3
    elif r["bxp"] > 100:
        p = -1
    else:
        p = 0
    s += p; bd["bxs"] = p

    # ================================================================
    # FACTOR 25: SPREAD (raw pips) — Gap: +10% at <1.5p / -12% at 10p+
    # 24% of W at <1.5p vs 14% of L → +10% gap (70% WR)
    # 7% of W at 10p+ vs 19% of L → -12% gap (33% WR)
    # ================================================================
    if r["sp"] < 1.5:
        p = 2
    elif r["sp"] >= 10:
        p = -4
    else:
        p = 0
    s += p; bd["spd"] = p

    # ================================================================
    # FACTOR 26: PDH/PDL TOUCHES — Gap: -9% at 15+
    # 24% of W at 15+ vs 33% of L → -9% gap (50% WR)
    # ================================================================
    # Very weak signal, not adding

    # ================================================================
    # FACTOR 27: R:R vs TP1 — Gap: ~0% (doesn't differentiate!)
    # 48% of W at 2.0-5.0 vs 48% of L → +1% gap
    # Confirmed dead weight. Minimal token points only.
    # ================================================================
    rr = ((r["bxp"]/2)/2) / r["ns"] if r["ns"] > 0 else 0
    if rr >= 2.0:
        p = 2
    elif rr >= 1.0:
        p = 1
    else:
        p = 0
    s += p; bd["rr"] = p

    # ================================================================
    # FACTOR 28: PRIOR DAY BULLISH — Gap: +7%
    # 83% of W bullish vs 76% of L → +7% gap. Weak but consistent.
    # ================================================================
    # Too weak and adds complexity. Not adding.

    # ================================================================
    # FACTOR 29: SIGNAL CANDLE RANGE — Gap: -11% at 10-20p
    # 3% of W at 10-20p vs 14% of L → -11% gap (25% WR)
    # ================================================================
    # Overlaps with natural stop. Not adding separately.

    return s, bd, blocks


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state":"CLOSED","count":"50"})
    trades = r.json().get("trades",[])
    print(f"V3 FINAL FORMULA — Scoring {len(trades)} trades (raw OANDA data)")
    print(f"Every factor weighted by proportional gap strength")
    print()

    results = []
    for i,t in enumerate(trades):
        sym = t.get("instrument","")
        pnl = float(t.get("realizedPL",0))
        print(f"  [{i+1}/{len(trades)}] {sym} ${pnl:+,.0f}...", end="", flush=True)
        try:
            a = extract(t)
            if a:
                sc, bd, blk = score_v3_final(a)
                a["score"]=sc; a["bd"]=bd; a["blk"]=blk
                results.append(a)
                if blk: print(f" BLOCKED:{','.join(blk)}")
                else: print(f" score={sc}")
            else: print(" skip")
        except Exception as e: print(f" err: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    w_scores = [r["score"] for r in winners]
    l_scores = [r["score"] for r in losers]

    # === FULL TABLE ===
    print()
    print("=" * 220)
    fmt = f"{'#':<3} {'Pair':<8} {'D':<2} {'PnL':>8} {'W':>1} {'SC':>5} |"
    fmt += f" {'age':>4} {'hr':>3} {'vol':>3} {'otr':>4} {'stp':>3} {'e50':>3} {'e20':>3} {'cnv':>4} {'mom':>3} {'z':>3} {'sma':>3} {'bb':>3} {'wal':>3} {'bdy':>3} {'rsi':>3} {'rng':>3} {'adr':>3} {'zon':>3} {'pat':>3} {'slp':>3} {'bxs':>3} {'spd':>3} {'rr':>2} |"
    fmt += f" {'BBS':<6} {'RSI':>4} {'DC':>2} {'NS':>5} {'VR':>4} {'HR':>3} {'AGE':>4} | {'VERDICT'}"
    print(fmt)
    print("-" * 220)

    for i, r in enumerate(sorted(results, key=lambda x: x["pnl"], reverse=True)):
        bd = r["bd"]
        blk = r["blk"]
        mark = "W" if r["won"] else "L"

        if blk: verdict = f"BLOCK:{blk[0]}"
        elif r["score"] >= 25: verdict = "PASS"
        else: verdict = f"SCORE_LOW({r['score']})"

        row = f"{i+1:<3} {r['sym']:<8} {r['d']:<2} {r['pnl']:>+8,.0f} {mark:>1} {r['score']:>5} |"
        for k in ['age','hr','vol','otr','stp','e50','e20','cnv','mom','z','sma','bb','wal','bdy','rsi','rng','adr','zon','pat','slp','bxs','spd','rr']:
            v = bd.get(k, '')
            if isinstance(v, int):
                row += f" {v:>3}" if k != 'cnv' else f" {v:>4}"
            elif isinstance(v, str) and 'BLOCK' in v:
                row += f" {'BLK':>3}"
            else:
                row += f" {'':>3}" if k != 'cnv' else f" {'':>4}"
        row += f" | {r['bbs']:<6} {r['rsi']:>4.0f} {r['dc']:>2} {r['ns']:>5.0f} {r['vr']:>4.2f} {r['hour']:>3} {r['bage']:>4.0f} | {verdict}"
        print(row)

    # === SUMMARY ===
    passed = [r for r in results if r["score"] >= 25 and not r["blk"]]
    blocked_hard = [r for r in results if r["blk"]]
    blocked_score = [r for r in results if r["score"] < 25 and not r["blk"]]

    pw = [r for r in passed if r["won"]]; pl = [r for r in passed if not r["won"]]

    print()
    print("=" * 100)
    print("V3 FINAL FORMULA RESULTS")
    print("=" * 100)
    print(f"  Total: {len(results)} trades ({len(winners)}W / {len(losers)}L)")
    print(f"  Net P&L (all): ${sum(r['pnl'] for r in results):+,.2f}")

    if w_scores and l_scores:
        w_avg = sum(w_scores)/len(w_scores)
        l_avg = sum(l_scores)/len(l_scores)
        print(f"\n  Score separation: W avg={w_avg:.1f}, L avg={l_avg:.1f}, GAP={w_avg-l_avg:+.1f}")

    print(f"\n  PASSED (score >= 25): {len(passed)} trades")
    if passed:
        print(f"    Winners: {len(pw)}  Losers: {len(pl)}  WR: {len(pw)/len(passed)*100:.0f}%")
        print(f"    Net P&L: ${sum(r['pnl'] for r in passed):+,.2f}")
        print(f"    Avg winner: ${sum(r['pnl'] for r in pw)/len(pw):+,.2f}" if pw else "")
        print(f"    Avg loser: ${sum(r['pnl'] for r in pl)/len(pl):+,.2f}" if pl else "")

    print(f"\n  HARD BLOCKED: {len(blocked_hard)} trades")
    bh_w = sum(1 for r in blocked_hard if r["won"])
    bh_l = sum(1 for r in blocked_hard if not r["won"])
    print(f"    {bh_w}W / {bh_l}L  (W$ lost: ${sum(r['pnl'] for r in blocked_hard if r['won']):+,.2f})")

    print(f"\n  SCORE BLOCKED (<25): {len(blocked_score)} trades")
    bs_w = sum(1 for r in blocked_score if r["won"])
    bs_l = sum(1 for r in blocked_score if not r["won"])
    print(f"    {bs_w}W / {bs_l}L  (W$ lost: ${sum(r['pnl'] for r in blocked_score if r['won']):+,.2f})")

    # Threshold sweep
    print(f"\n  THRESHOLD SWEEP:")
    print(f"  {'Thresh':>6} {'Taken':>6} {'W':>3} {'L':>3} {'WR':>5} {'Net$':>10}")
    for thr in range(-10, 60, 5):
        p = [r for r in results if r["score"] >= thr and not r["blk"]]
        pw2 = [r for r in p if r["won"]]; pl2 = [r for r in p if not r["won"]]
        tot = len(pw2)+len(pl2)
        if tot == 0: continue
        wr = len(pw2)/tot*100
        net = sum(r["pnl"] for r in p)
        marker = " <<<" if net > 0 else ""
        print(f"  {thr:>6} {tot:>6} {len(pw2):>3} {len(pl2):>3} {wr:>4.0f}% {net:>+9,.0f}{marker}")

    # Component contribution
    print(f"\n  COMPONENT CONTRIBUTION (avg pts for W vs L):")
    all_keys = set()
    for r in results:
        if not r["blk"]:
            all_keys.update(r["bd"].keys())
    all_keys -= {"BLOCKED"}

    scored_comp = []
    for k in sorted(all_keys):
        wv = [r["bd"].get(k, 0) for r in winners if not r["blk"]]
        lv = [r["bd"].get(k, 0) for r in losers if not r["blk"]]
        if not wv or not lv: continue
        wa = sum(wv)/len(wv); la = sum(lv)/len(lv)
        delta = wa - la
        scored_comp.append((abs(delta), k, wa, la, delta))

    scored_comp.sort(reverse=True)
    print(f"  {'Factor':<8} {'W avg':>7} {'L avg':>7} {'Delta':>7}")
    for _, k, wa, la, d in scored_comp:
        sig = " ***" if abs(d) > 3 else " **" if abs(d) > 1.5 else " *" if abs(d) > 0.5 else ""
        print(f"  {k:<8} {wa:>+7.1f} {la:>+7.1f} {d:>+7.1f}{sig}")


if __name__ == "__main__":
    main()
