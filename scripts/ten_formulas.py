#!/usr/bin/env python3
"""
10 DIFFERENT SCORING METHODS — run simultaneously against raw OANDA data.
Goal: find which method best separates winners from losers.

Methods:
  M1: Proportional gap scoring (points = gap%)
  M2: Win-rate weighted (points = WR deviation from 50%)
  M3: Binary classifier (each factor votes +1 or -1)
  M4: Only hard blocks + conviction + box age (minimal)
  M5: Log-odds scoring (ln(WR/(1-WR)))
  M6: Only top 5 factors, maximum weight
  M7: Penalty-heavy (mainly subtract for bad conditions)
  M8: Bonus-heavy (mainly add for good conditions)
  M9: Multiplicative (multiply probabilities instead of adding)
  M10: P&L weighted (points proportional to net PnL in bucket)
"""

import os, requests, statistics, time as _t, math
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
    rc = ch[-period:]; g = sum(c for c in rc if c > 0)/period or 0.0001
    l = sum(-c for c in rc if c < 0)/period or 0.0001
    return round(100-(100/(1+g/l)), 1)

def bb_st(cl):
    if len(cl) < 20: return "UNK"
    s20 = sum(cl[-20:])/20; sd = statistics.stdev(cl[-20:]) if len(cl[-20:])>1 else 0.0001
    ua = s20+2*sd; la = s20-2*sd; c=cl[-1]; c1=cl[-2] if len(cl)>=2 else c; c2=cl[-3] if len(cl)>=3 else c1
    n = min(4,len(cl)); s4 = sum(cl[-n:])/n; sd4 = statistics.stdev(cl[-n:]) if n>=2 else 0.0001
    ub = s4+4*sd4; lb = s4-4*sd4
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
    pdh=float(pd["mid"]["h"]); pdl=float(pd["mid"]["l"]); bx=pdh-pdl; hf=bx/2; bxp=bx/pip
    bpos=(entry-pdl)/bx if bx>0 else 0.5; wp=(entry-pdl)/bx if d=="L" else (pdh-entry)/bx; wp=wp if bx>0 else 1
    atrs=[max(float(daily[i]["mid"]["h"])-float(daily[i]["mid"]["l"]),abs(float(daily[i]["mid"]["h"])-float(daily[i-1]["mid"]["c"])),abs(float(daily[i]["mid"]["l"])-float(daily[i-1]["mid"]["c"]))) for i in range(1,len(daily))]
    atr=sum(atrs)/len(atrs) if atrs else bx; tc=daily[-1]["mid"]; adr=(float(tc["h"])-float(tc["l"]))/atr if atr>0 else 0
    try: pdt=datetime.fromisoformat(pd["time"][:26].replace("Z","+00:00")); bage=(odt-pdt).total_seconds()/3600
    except: bage=24
    la=m5[-1]; ask=float(la.get("ask",{}).get("c",0)); bid=float(la.get("bid",{}).get("c",0))
    sprd=(ask-bid) if ask>0 and bid>0 else pip*2; sp=sprd/pip; otr_pct=2*sprd/hf*100 if hf>0 else 100
    sig=None; dc=0; mom=0
    for i in range(len(m5)-1, max(len(m5)-8,-1), -1):
        mm=m5[i]["mid"]; o,h,l,c=float(mm["o"]),float(mm["h"]),float(mm["l"]),float(mm["c"])
        if sig is None:
            if (d=="L" and c>o) or (d=="S" and c<o):
                body=abs(c-o) or pip*0.1; rng=h-l or pip*0.1; wk=(min(o,c)-l) if d=="L" else (h-max(o,c))
                sig={"low":l,"high":h,"wick_r":wk/body,"body_pct":body/rng}
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
    else: ns=10; bp=0.5
    c1h=[float(c["mid"]["c"]) for c in hourly[-20:]]; mn=sum(c1h)/len(c1h)
    sd=statistics.stdev(c1h) if len(c1h)>1 else 0.0001; zs=(entry-mn)/sd if sd>0 else 0
    ub=mn+2*sd; lb=mn-2*sd; w=ub-lb; bbp=(entry-lb)/w if w>0 else 0.5
    c5m=[float(c["mid"]["c"]) for c in m5[-25:]]; bbs=bb_st(c5m)
    sma20=sum(c5m[-20:])/20 if len(c5m)>=20 else entry; sma_d=(entry-sma20)/pip
    cr5=[float(c["mid"]["c"]) for c in m5[-15:]]; rsi=rsi_c(cr5) or 50
    ah=[float(c["mid"]["c"]) for c in hourly]; e50=ema_c(ah,50); e20=ema_c(ah,20)
    e50d=abs(entry-e50)/bx*100 if e50 and bx>0 else 50; e20d=abs(entry-e20)/bx*100 if e20 and bx>0 else 50
    is_ct=(d=="L" and entry>(e50 or 0)) or (d=="S" and entry<(e50 or 999999)) if e50 else False
    if len(ah)>=10: sl=(sum(ah[-5:])/5-sum(ah[-10:-5])/5)/(sum(ah[-10:-5])/5)*100
    else: sl=0
    is_rng=abs(sl)<0.02
    if len(m5)>=20:
        rr=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-5:]]
        ro=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-20:-5]]
        vr=(sum(rr)/5)/(sum(ro)/15) if sum(ro)>0 else 1
    else: vr=1
    return {"sym":sym,"d":d,"pnl":pnl,"won":pnl>0,"hour":hour,"bage":bage,"vr":vr,
            "is_rng":is_rng,"bbs":bbs,"dc":dc,"mom":mom,"sma_d":sma_d,"ns":ns,
            "e50d":e50d,"e20d":e20d,"wp":wp,"bbp":bbp,"zs":zs,"rsi":rsi,
            "is_ct":is_ct,"adr":adr,"bxp":bxp,"sp":sp,"otr":otr_pct,"bp":bp,
            "dur":dur,"sl":sl,"bpos":bpos}


# === SHARED HARD BLOCKS (same for all methods) ===
def hard_blocks(r):
    blocks = []
    if r["ns"] <= 0: blocks.append("INV_SL")
    if r["ns"] > 0 and r["sp"] > r["ns"]: blocks.append("SP>SL")
    if r["bbs"] in ("STR_UP","STR_DN"): blocks.append("STRETCH")
    if 45 <= r["rsi"] <= 55: blocks.append("RSI_N")
    return blocks


# === 10 SCORING METHODS ===

def m1_proportional_gap(r):
    """Points = proportional to gap% magnitude."""
    s = 0
    # Box age: ±38% gap → ±12 pts
    if r["bage"]<12: s+=12
    elif r["bage"]<24: s-=12
    # Entry hour: +39%/-23% → +10/-7
    if r["hour"]<8: s+=10
    elif 12<=r["hour"]<20: s-=7
    elif r["hour"]>=20: s-=8
    # Volume: +22%/-14% → +7/-4
    if 0.9<=r["vr"]<=1.1: s+=7
    elif r["vr"]>1.5: s-=6
    elif r["vr"]<0.9: s-=4
    # OTR: -20% at <8% → -8; +14% at 8-18% → +4
    if r["otr"]<8: s-=8
    elif 8<=r["otr"]<=18: s+=4
    # Nat stop: +20% at 4-6p → +6
    if 4<=r["ns"]<=6: s+=6
    elif r["ns"]>=12: s-=4
    # EMA50: -16% at <20% → -7
    if r["e50d"]<20: s-=7
    elif r["e50d"]>=60: s+=3
    # EMA20: -17% at <15% → -5
    if r["e20d"]<15: s-=5
    elif 15<=r["e20d"]<=30: s+=4
    # Conviction: +12%/-12% → +15/-10
    if r["dc"]>=4: s+=15
    elif r["dc"]==3: s+=5
    elif r["dc"]==2: s+=3
    elif r["dc"]==0: s-=10
    # Momentum: +11%/-13% → +4/-4
    if r["mom"]>=3: s+=5
    elif r["mom"]==2: s+=4
    elif r["mom"]==0: s-=4
    # Z-score: +18%/-17% → +5/-5
    az=abs(r["zs"])
    if 0.5<=az<=1.5: s+=5
    elif az>=2.0: s+=6
    elif az<0.5: s-=5
    # SMA20: -10% above → -5
    if r["sma_d"]<-5: s+=3
    elif 5<r["sma_d"]<=20: s-=5
    # BB: +16%/-10% → +4/-5
    if 0.65<=r["bbp"]<=0.85: s+=4
    elif 0.35<=r["bbp"]<=0.50: s-=5
    # Wall: -17% at 0.15-0.30 → -5
    if 0.15<=r["wp"]<0.30: s-=5
    elif 0.30<=r["wp"]<0.50: s+=3
    # Body%: -22% at 45-65% → -4
    if r["bp"]<0.25: s+=3
    elif 0.45<=r["bp"]<=0.65: s-=4
    # RSI: +9%/-11% → +3/-3
    if r["rsi"]<40: s+=3
    elif 55<=r["rsi"]<75: s-=3
    # BB state
    if r["bbs"] in ("REJ_L","REJ_S"): s+=3
    # Ranging
    if r["is_rng"]: s-=15
    # ADR: +17%/-11% → +4/-3
    if 0.60<=r["adr"]<=0.80: s+=4
    elif 0.80<=r["adr"]<=1.0: s-=3
    # Base
    s += 8 if r["bxp"]<200 else 5  # zone base
    s += 6  # pattern base
    # Slope: -13% → -4
    if -0.1<=r["sl"]<-0.02: s-=4
    elif 0.02<=r["sl"]<=0.1: s+=3
    # Box size
    if r["bxp"]>200: s-=3
    # Spread
    if r["sp"]<1.5: s+=2
    elif r["sp"]>=10: s-=4
    # z-align
    if (r["d"]=="L" and r["zs"]<-0.5) or (r["d"]=="S" and r["zs"]>0.5): s+=3
    return s

def m2_winrate_weighted(r):
    """Points = (WR - 50%) * 0.5 for each bucket."""
    s = 0
    # Box age <12h: 83% WR → (83-50)*0.5 = +16.5 → +16
    if r["bage"]<12: s+=16
    elif r["bage"]<24: s-=4  # 41% → (41-50)*0.5 = -4.5
    if r["hour"]<8: s+=19  # 88% → +19
    elif 12<=r["hour"]<20: s-=3  # 45%
    elif r["hour"]>=20: s-=6  # 38%
    if 0.9<=r["vr"]<=1.1: s+=16  # 82%
    elif r["vr"]>1.5: s-=3
    if r["otr"]<8: s-=17  # 17% → -16.5
    elif 8<=r["otr"]<=18: s+=7  # 63%
    if 4<=r["ns"]<=6: s+=10  # 70%
    if r["e50d"]<20: s-=15  # 20%
    if r["e20d"]<15: s-=2  # 47%
    elif 15<=r["e20d"]<=30: s+=10  # 69%
    if r["dc"]>=4: s+=17  # 83%
    elif r["dc"]==0: s+=0  # 50%
    if r["mom"]>=3: s+=15  # 80%
    elif r["mom"]==0: s+=0
    az=abs(r["zs"])
    if az<0.5: s-=11  # 29%
    elif 0.5<=az<=1.5: s+=9  # 68%
    if r["bp"]<0.25: s+=13  # 75%
    elif 0.45<=r["bp"]<=0.65: s-=5  # 40%
    if r["rsi"]<40: s+=9  # 67%
    if r["bbs"] in ("REJ_L","REJ_S"): s+=13  # 75%
    if r["is_rng"]: s-=15
    if 0.60<=r["adr"]<=0.80: s+=13  # 75%
    elif 0.80<=r["adr"]<=1.0: s-=3
    s += 5  # base
    return s

def m3_binary_vote(r):
    """Each factor votes +1 or -1. Simple count of favorable vs unfavorable."""
    votes = 0
    if r["bage"]<12: votes+=1
    elif r["bage"]<24: votes-=1
    if r["hour"]<8: votes+=1
    elif r["hour"]>=12: votes-=1
    if 0.9<=r["vr"]<=1.1: votes+=1
    elif r["vr"]>1.5 or r["vr"]<0.7: votes-=1
    if r["otr"]<8: votes-=1
    elif 8<=r["otr"]<=18: votes+=1
    if 4<=r["ns"]<=6: votes+=1
    elif r["ns"]>=12: votes-=1
    if r["e50d"]<20: votes-=1
    elif r["e50d"]>=60: votes+=1
    if r["e20d"]<15: votes-=1
    elif 15<=r["e20d"]<=30: votes+=1
    if r["dc"]>=3: votes+=1
    elif r["dc"]==0: votes-=1
    if r["mom"]>=2: votes+=1
    elif r["mom"]==0: votes-=1
    az=abs(r["zs"])
    if az<0.5: votes-=1
    elif az>=1.0: votes+=1
    if 5<r["sma_d"]<=20: votes-=1
    elif r["sma_d"]<-5: votes+=1
    if 0.35<=r["bbp"]<=0.50: votes-=1
    elif 0.65<=r["bbp"]<=0.85: votes+=1
    if r["bp"]<0.25: votes+=1
    elif 0.45<=r["bp"]<=0.65: votes-=1
    if r["rsi"]<40: votes+=1
    elif 55<=r["rsi"]<75: votes-=1
    if r["bbs"] in ("REJ_L","REJ_S"): votes+=1
    if r["is_rng"]: votes-=1
    if 0.60<=r["adr"]<=0.80: votes+=1
    elif 0.80<=r["adr"]<=1.0: votes-=1
    if r["hour"]<8 and r["bage"]<12: votes+=1  # combo bonus
    if r["sp"]>=10: votes-=1
    return votes * 5  # scale to comparable range

def m4_minimal(r):
    """Only the top 3 factors + hard blocks. Simplest possible."""
    s = 0
    if r["bage"]<12: s+=15
    elif r["bage"]<24: s-=15
    if r["hour"]<8: s+=12
    elif r["hour"]>=12: s-=8
    if r["dc"]>=4: s+=20
    elif r["dc"]==0: s-=15
    s += 10  # base
    return s

def m5_log_odds(r):
    """Points = ln(WR/(1-WR)) * 10. Logarithmic odds ratio."""
    s = 0
    def lo(wr): return round(math.log(max(wr,0.01)/(1-max(wr,0.01)+0.01)) * 10, 1) if wr < 1 else 20
    if r["bage"]<12: s+=lo(0.83)  # +15.7
    elif r["bage"]<24: s+=lo(0.41)  # -3.6
    if r["hour"]<8: s+=lo(0.88)  # +19.8
    elif 12<=r["hour"]<20: s+=lo(0.45)  # -2.0
    elif r["hour"]>=20: s+=lo(0.38)  # -4.9
    if 0.9<=r["vr"]<=1.1: s+=lo(0.82)  # +15.0
    elif r["vr"]>1.5: s+=lo(0.43)  # -2.8
    if r["otr"]<8: s+=lo(0.17)  # -15.9
    elif 8<=r["otr"]<=18: s+=lo(0.63)  # +5.3
    if 4<=r["ns"]<=6: s+=lo(0.70)  # +8.5
    if r["e50d"]<20: s+=lo(0.20)  # -13.9
    if r["dc"]>=4: s+=lo(0.83)  # +15.7
    elif r["dc"]==0: s+=lo(0.50)  # 0
    if r["mom"]>=3: s+=lo(0.80)  # +13.9
    az=abs(r["zs"])
    if az<0.5: s+=lo(0.29)  # -9.0
    elif 0.5<=az<=1.5: s+=lo(0.68)  # +7.5
    if r["bbs"] in ("REJ_L","REJ_S"): s+=lo(0.75)  # +11.0
    if r["is_rng"]: s+=lo(0.35)  # -6.2
    return s

def m6_top5_heavy(r):
    """Only top 5 factors with maximum weight (25 pts each)."""
    s = 0
    # 1. Box age
    if r["bage"]<12: s+=25
    elif r["bage"]<24: s-=25
    # 2. Entry hour
    if r["hour"]<8: s+=25
    elif r["hour"]>=12: s-=15
    # 3. Volume ratio
    if 0.9<=r["vr"]<=1.1: s+=20
    elif r["vr"]>1.5 or r["vr"]<0.7: s-=15
    # 4. Conviction
    if r["dc"]>=4: s+=25
    elif r["dc"]==0: s-=20
    # 5. OTR inverted
    if r["otr"]<8: s-=20
    elif 8<=r["otr"]<=18: s+=10
    s += 10  # base
    return s

def m7_penalty_heavy(r):
    """Focus on penalties. Start at 50, subtract for red flags."""
    s = 50
    if r["bage"]>=12: s-=15
    if r["hour"]>=12: s-=10
    if r["vr"]>1.5: s-=10
    if r["vr"]<0.7: s-=5
    if r["otr"]<8: s-=12
    if r["ns"]>=12: s-=5
    if r["e50d"]<20: s-=10
    if r["e20d"]<15: s-=8
    if r["dc"]==0: s-=12
    if r["mom"]==0: s-=5
    if abs(r["zs"])<0.5: s-=8
    if 5<r["sma_d"]<=20: s-=8
    if 0.35<=r["bbp"]<=0.50: s-=6
    if 0.45<=r["bp"]<=0.65: s-=5
    if 55<=r["rsi"]<75: s-=4
    if r["is_rng"]: s-=15
    if 0.80<=r["adr"]<=1.0: s-=5
    if r["bxp"]>200: s-=5
    if r["sp"]>=10: s-=8
    if -0.1<=r["sl"]<-0.02: s-=5
    if 0.15<=r["wp"]<0.30: s-=6
    return s

def m8_bonus_heavy(r):
    """Focus on bonuses. Start at -20, add for green flags."""
    s = -20
    if r["bage"]<12: s+=18
    if r["hour"]<8: s+=15
    if 0.9<=r["vr"]<=1.1: s+=12
    if 8<=r["otr"]<=18: s+=8
    if 4<=r["ns"]<=6: s+=10
    if r["e50d"]>=60: s+=6
    if 15<=r["e20d"]<=30: s+=8
    if r["dc"]>=4: s+=20
    elif r["dc"]>=3: s+=10
    if r["mom"]>=2: s+=8
    az=abs(r["zs"])
    if az>=1.0: s+=8
    if r["sma_d"]<-5: s+=5
    if 0.65<=r["bbp"]<=0.85: s+=6
    if r["bp"]<0.25: s+=6
    if r["rsi"]<40: s+=6
    if r["bbs"] in ("REJ_L","REJ_S"): s+=8
    if 0.60<=r["adr"]<=0.80: s+=6
    if r["sp"]<1.5: s+=4
    if 0.02<=r["sl"]<=0.1: s+=5
    if 0.30<=r["wp"]<0.50: s+=5
    return s

def m9_multiplicative(r):
    """Multiply probability factors. Convert to score at end."""
    prob = 0.58  # base rate (29W/50L)
    # Each factor adjusts probability
    if r["bage"]<12: prob*=1.4  # 83/58
    elif r["bage"]<24: prob*=0.7  # 41/58
    if r["hour"]<8: prob*=1.5  # 88/58
    elif r["hour"]>=20: prob*=0.65  # 38/58
    if 0.9<=r["vr"]<=1.1: prob*=1.4  # 82/58
    elif r["vr"]>1.5: prob*=0.74
    if r["otr"]<8: prob*=0.29  # 17/58
    elif 8<=r["otr"]<=18: prob*=1.09
    if 4<=r["ns"]<=6: prob*=1.2
    if r["e50d"]<20: prob*=0.34  # 20/58
    if r["dc"]>=4: prob*=1.4
    elif r["dc"]==0: prob*=0.86
    if abs(r["zs"])<0.5: prob*=0.50  # 29/58
    if r["bbs"] in ("REJ_L","REJ_S"): prob*=1.3
    if r["is_rng"]: prob*=0.60
    if 0.80<=r["adr"]<=1.0: prob*=0.78
    # Convert probability to score (0-100 scale)
    return int(max(0, min(100, prob * 50)))

def m10_pnl_weighted(r):
    """Points proportional to actual net P&L in each bucket."""
    s = 0
    # Box age <12h: +$159 → +8 pts; 12-24h: -$388 → -19 pts
    if r["bage"]<12: s+=8
    elif r["bage"]<24: s-=19
    # Hour 0-7: +$156 → +8; 12-15: -$282 → -14
    if r["hour"]<8: s+=8
    elif 12<=r["hour"]<16: s-=14
    elif 16<=r["hour"]<20: s-=4
    elif r["hour"]>=20: s-=0  # -$1 → 0
    # Vol 0.9-1.1: +$59 → +3; 0.7-0.9: -$118 → -6
    if 0.9<=r["vr"]<=1.1: s+=3
    elif 0.7<=r["vr"]<0.9: s-=6
    elif r["vr"]>1.5: s-=1
    # OTR <8%: -$98 → -5
    if r["otr"]<8: s-=5
    # Nat stop 4-6p: +$93 → +5; <=0: -$134 → -7
    if 4<=r["ns"]<=6: s+=5
    elif r["ns"]>=12: s-=1
    # EMA50 <20%: -$86 → -4
    if r["e50d"]<20: s-=4
    # EMA20 <15%: -$159 → -8
    if r["e20d"]<15: s-=8
    # Conviction 4+: +$64 → +3; 0: -$176 → -9
    if r["dc"]>=4: s+=3
    elif r["dc"]==0: s-=9
    # Z neutral: -$154 → -8
    if abs(r["zs"])<0.5: s-=8
    # BB 0.35-0.50: -$85 → -4
    if 0.35<=r["bbp"]<=0.50: s-=4
    elif 0.15<=r["bbp"]<=0.35: s+=5  # +$104
    # Body% 45-65%: -$120 → -6
    if 0.45<=r["bp"]<=0.65: s-=6
    # RSI <40: +$81 → +4; 60-75: -$182 → -9
    if r["rsi"]<40: s+=4
    elif 55<=r["rsi"]<75: s-=9
    # BB state STRETCH: -$135 → already blocked
    if r["bbs"] in ("REJ_L","REJ_S"): s+=2
    # Ranging: -$214 proj → -11
    if r["is_rng"]: s-=11
    # ADR 60-80%: -$49 but 75% WR → +2; 80-100%: -$202 → -10
    if 0.60<=r["adr"]<=0.80: s+=2
    elif 0.80<=r["adr"]<=1.0: s-=10
    # Spread 10+: -$42 → -2
    if r["sp"]>=10: s-=2
    # Duration 6h+: -$115 → -6
    # (can't use duration as entry filter, but note it)
    # Base
    s += 15
    return s


METHODS = {
    "M1_gap": m1_proportional_gap,
    "M2_wr": m2_winrate_weighted,
    "M3_vote": m3_binary_vote,
    "M4_min": m4_minimal,
    "M5_odds": m5_log_odds,
    "M6_top5": m6_top5_heavy,
    "M7_pen": m7_penalty_heavy,
    "M8_bon": m8_bonus_heavy,
    "M9_mult": m9_multiplicative,
    "M10_pnl": m10_pnl_weighted,
}


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state":"CLOSED","count":"50"})
    trades = r.json().get("trades",[])
    print(f"10 SCORING METHODS — {len(trades)} trades, raw OANDA data\n")

    results = []
    for i,t in enumerate(trades):
        sym = t.get("instrument",""); pnl = float(t.get("realizedPL",0))
        print(f"  [{i+1}/{len(trades)}] {sym} ${pnl:+,.0f}...", end="", flush=True)
        try:
            a = extract(t)
            if a:
                blk = hard_blocks(a)
                a["blk"] = blk
                for name, fn in METHODS.items():
                    if blk:
                        a[name] = 0
                    else:
                        a[name] = fn(a)
                results.append(a)
                print(f" OK")
            else: print(" skip")
        except Exception as e: print(f" err: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    print(f"\nTotal: {len(results)} ({len(winners)}W / {len(losers)}L)")

    # === FULL TABLE ===
    print()
    print("=" * 180)
    hdr = f"{'#':<3} {'Pair':<8} {'D':<2} {'PnL':>8} {'W':>1} |"
    for name in METHODS: hdr += f" {name[-4:]:>5}"
    hdr += f" | {'Blocks'}"
    print(hdr)
    print("-" * 180)

    for i, r in enumerate(sorted(results, key=lambda x: x["pnl"], reverse=True)):
        row = f"{i+1:<3} {r['sym']:<8} {r['d']:<2} {r['pnl']:>+8,.0f} {'W' if r['won'] else 'L':>1} |"
        for name in METHODS:
            row += f" {r[name]:>5}"
        row += f" | {','.join(r['blk']) if r['blk'] else ''}"
        print(row)

    # === SEPARATION ===
    print()
    print("=" * 100)
    print("SEPARATION: Winner avg - Loser avg (higher = better discrimination)")
    print("=" * 100)
    print(f"  {'Method':<12} {'W avg':>8} {'L avg':>8} {'SEP':>8} {'W med':>8} {'L med':>8}")
    seps = []
    for name in METHODS:
        ws = [r[name] for r in winners if not r["blk"]]
        ls = [r[name] for r in losers if not r["blk"]]
        if not ws or not ls: continue
        wa = sum(ws)/len(ws); la = sum(ls)/len(ls)
        wm = sorted(ws)[len(ws)//2]; lm = sorted(ls)[len(ls)//2]
        sep = wa - la
        seps.append((sep, name, wa, la, wm, lm))

    seps.sort(key=lambda x: x[0], reverse=True)
    for sep, name, wa, la, wm, lm in seps:
        bar = "█" * int(max(0, sep))
        print(f"  {name:<12} {wa:>8.1f} {la:>8.1f} {sep:>+7.1f} {wm:>8} {lm:>8}  {bar}")

    # === THRESHOLD SIMULATION ===
    print()
    print("=" * 120)
    print("BEST THRESHOLD FOR EACH METHOD (max P&L with >= 5 trades)")
    print("=" * 120)
    print(f"  {'Method':<12} {'Thresh':>7} {'Taken':>6} {'W':>3} {'L':>3} {'WR':>5} {'Net$':>10} {'BlkW$':>9} {'BlkL$':>9}")

    for name in METHODS:
        best_pnl = -999999; best_thr = 0; best_row = ""
        for thr in range(-50, 80, 5):
            p = [r for r in results if r[name] >= thr and not r["blk"]]
            b = [r for r in results if (r[name] < thr or r["blk"])]
            pw = [r for r in p if r["won"]]; pl = [r for r in p if not r["won"]]
            bw = [r for r in b if r["won"]]; bl = [r for r in b if not r["won"]]
            tot = len(pw)+len(pl)
            if tot < 5: continue
            net = sum(r["pnl"] for r in p)
            if net > best_pnl:
                best_pnl = net
                wr = len(pw)/tot*100
                bw_pnl = sum(r["pnl"] for r in bw)
                bl_pnl = sum(r["pnl"] for r in bl)
                best_row = f"  {name:<12} {thr:>7} {tot:>6} {len(pw):>3} {len(pl):>3} {wr:>4.0f}% {net:>+9,.0f} {bw_pnl:>+8,.0f} {bl_pnl:>+8,.0f}"
        print(best_row)

    # === PERFECT FILTER ANALYSIS ===
    print()
    print("=" * 100)
    print("PERFECT FILTER: How close does each method get to 0 false positives?")
    print("=" * 100)
    for name in METHODS:
        # Find threshold where ALL passed trades are winners (WR=100%)
        for thr in range(80, -50, -1):
            p = [r for r in results if r[name] >= thr and not r["blk"]]
            if not p: continue
            pw = [r for r in p if r["won"]]; pl = [r for r in p if not r["won"]]
            if len(pl) == 0 and len(pw) >= 1:
                pnl = sum(r["pnl"] for r in pw)
                print(f"  {name:<12} 100% WR at thresh={thr}: {len(pw)}W/${pnl:+,.0f}  (blocks {len(winners)-len(pw)} other winners)")
                break
        else:
            print(f"  {name:<12} Never achieves 100% WR")


if __name__ == "__main__":
    main()
