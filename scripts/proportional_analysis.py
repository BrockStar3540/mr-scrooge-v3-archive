#!/usr/bin/env python3
"""
Proportional Analysis — What % of winners vs losers fall into each bucket
for EVERY factor. Shows the actual population distribution, not just averages.

For each factor bucket: what proportion of ALL winners land here vs ALL losers?
This reveals WHERE winners cluster and WHERE losers cluster.
"""

import os, requests, statistics, time as _t, json
from datetime import datetime
from collections import defaultdict

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

def bb_state(cl):
    if len(cl) < 20: return "UNK"
    s20 = sum(cl[-20:])/20; sd = statistics.stdev(cl[-20:]) if len(cl[-20:])>1 else 0.0001
    ua = s20+2*sd; la = s20-2*sd
    n = min(4,len(cl)); s4 = sum(cl[-n:])/n
    sd4 = statistics.stdev(cl[-n:]) if n>=2 else 0.0001
    ub = s4+4*sd4; lb = s4-4*sd4
    c=cl[-1]; c1=cl[-2] if len(cl)>=2 else c; c2=cl[-3] if len(cl)>=3 else c1
    if c>ub and ub>ua: return "EXTREME_UP"
    if c<lb and lb<la: return "EXTREME_DN"
    if c<=ua and (c1>ua or c2>ua): return "REJECT_S"
    if c>=la and (c1<la or c2<la): return "REJECT_L"
    if c>ua and c1>ua and c>=c1: return "BREAK_UP"
    if c<la and c1<la and c<=c1: return "BREAK_DN"
    if c>ua: return "STRETCH_U"
    if c<la: return "STRETCH_D"
    return "NORMAL"

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
    wp=(entry-pdl)/bx if d=="L" else (pdh-entry)/bx
    wp=wp if bx>0 else 1

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
    sprd_hf=sprd/hf*100 if hf>0 else 100
    otr=2*sprd/hf*100 if hf>0 else 100

    sig=None; dc=0; mom=0
    for i in range(len(m5)-1, max(len(m5)-8,-1), -1):
        mm=m5[i]["mid"]; o,h,l,c=float(mm["o"]),float(mm["h"]),float(mm["l"]),float(mm["c"])
        if sig is None:
            if (d=="L" and c>o) or (d=="S" and c<o):
                body=abs(c-o) or pip*0.1; rng=h-l or pip*0.1
                wk=(min(o,c)-l) if d=="L" else (h-max(o,c))
                sig={"low":l,"high":h,"wick_r":wk/body,"body_pct":body/rng,"range":rng}
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
        wr=sig["wick_r"]; bp=sig["body_pct"]; cr=sig["range"]/pip
    else: ns=10; wr=0; bp=0.5; cr=0; stype="?"

    sprd_sl=sp/ns*100 if ns>0 else 999

    c1h=[float(c["mid"]["c"]) for c in hourly[-20:]]
    mn=sum(c1h)/len(c1h); sd=statistics.stdev(c1h) if len(c1h)>1 else 0.0001
    zs=(entry-mn)/sd if sd>0 else 0
    ub=mn+2*sd; lb=mn-2*sd; w=ub-lb; bbp=(entry-lb)/w if w>0 else 0.5

    c5m=[float(c["mid"]["c"]) for c in m5[-25:]]
    bbs=bb_state(c5m)
    sma20=sum(c5m[-20:])/20 if len(c5m)>=20 else entry
    sma_d=(entry-sma20)/pip

    cr5=[float(c["mid"]["c"]) for c in m5[-15:]]
    rsi=rsi_c(cr5) or 50

    ah=[float(c["mid"]["c"]) for c in hourly]
    e20=ema_c(ah,20); e50=ema_c(ah,50)
    e20d=abs(entry-e20)/bx*100 if e20 and bx>0 else 50
    e50d=abs(entry-e50)/bx*100 if e50 and bx>0 else 50
    is_ct=(d=="L" and entry>(e50 or 0)) or (d=="S" and entry<(e50 or 999999)) if e50 else False

    if len(ah)>=10:
        sl=(sum(ah[-5:])/5-sum(ah[-10:-5])/5)/(sum(ah[-10:-5])/5)*100
    else: sl=0
    is_rng=abs(sl)<0.02

    if len(m5)>=20:
        rr=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-5:]]
        ro=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-20:-5]]
        vr=(sum(rr)/5)/(sum(ro)/15) if sum(ro)>0 else 1
    else: vr=1

    tb=abs(pdh)*0.001
    tch=sum(1 for h in hourly[-24:] if abs(float(h["mid"]["h"])-pdh)<=tb or abs(float(h["mid"]["l"])-pdl)<=tb)

    dalign=any(abs(entry-dl)/dl<0.002 for dl in [pdh,pdl])
    zt=1 if dalign else 3

    po=float(pd["mid"]["o"]); pc=float(pd["mid"]["c"]); pbull=pc>po
    rr_tp1=((hf/pip)/2)/ns if ns>0 else 0

    return {
        "sym":sym,"d":d,"pnl":pnl,"won":pnl>0,
        "zt":zt,"stype":stype,"hour":hour,"bage":bage,"vr":vr,"rng":is_rng,
        "bbs":bbs,"dc":dc,"mom":mom,"sma_d":sma_d,"ns":ns,"e50d":e50d,"e20d":e20d,
        "wp":wp,"bbp":bbp,"zs":zs,"rsi":rsi,"is_ct":is_ct,"adr":adr,"rr":rr_tp1,
        "bxp":bxp,"sp":sp,"sprd_hf":sprd_hf,"otr":otr,"sprd_sl":sprd_sl,
        "dur":dur,"sl":sl,"wr":wr,"bp":bp,"cr":cr,"tch":tch,"pbull":pbull,
        "bpos":bpos,
    }


def proportional(results, key, label, buckets):
    """Show what PROPORTION of winners vs losers fall into each bucket."""
    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    tw = len(winners); tl = len(losers)

    print(f"\n  {label}")
    print(f"  {'Bucket':<16} {'W#':>3} {'W%':>5} {'L#':>3} {'L%':>5} {'WR':>4} {'NetPnL':>9} {'W bar':>20} {'L bar':>20} {'Gap':>6}")

    for lo, hi, bl in buckets:
        w = [r for r in winners if r.get(key) is not None and lo <= r[key] < hi]
        l = [r for r in losers if r.get(key) is not None and lo <= r[key] < hi]
        tot = len(w) + len(l)
        if tot == 0: continue
        wpct = len(w)/tw*100 if tw>0 else 0
        lpct = len(l)/tl*100 if tl>0 else 0
        wr = len(w)/tot*100
        net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
        wbar = "█" * int(wpct/5) + "░" * (20-int(wpct/5))
        lbar = "█" * int(lpct/5) + "░" * (20-int(lpct/5))
        gap = wpct - lpct
        marker = " ←W" if gap > 15 else " ←L" if gap < -15 else ""
        print(f"  {bl:<16} {len(w):>3} {wpct:>4.0f}% {len(l):>3} {lpct:>4.0f}% {wr:>3.0f}% {net:>+8,.0f}  {wbar} {lbar} {gap:>+5.0f}%{marker}")


def proportional_cat(results, key, label):
    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    tw = len(winners); tl = len(losers)
    cats = sorted(set(str(r[key]) for r in results if r.get(key) is not None))

    print(f"\n  {label}")
    print(f"  {'Value':<16} {'W#':>3} {'W%':>5} {'L#':>3} {'L%':>5} {'WR':>4} {'NetPnL':>9} {'Gap':>6}")

    for cat in cats:
        w = [r for r in winners if str(r[key]) == cat]
        l = [r for r in losers if str(r[key]) == cat]
        tot = len(w)+len(l)
        if tot == 0: continue
        wpct = len(w)/tw*100 if tw>0 else 0
        lpct = len(l)/tl*100 if tl>0 else 0
        wr = len(w)/tot*100
        net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
        gap = wpct - lpct
        marker = " ←W" if gap > 10 else " ←L" if gap < -10 else ""
        print(f"  {cat:<16} {len(w):>3} {wpct:>4.0f}% {len(l):>3} {lpct:>4.0f}% {wr:>3.0f}% {net:>+8,.0f} {gap:>+5.0f}%{marker}")


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state":"CLOSED","count":"50"})
    trades = r.json().get("trades",[])
    print(f"Pulling raw data for {len(trades)} trades...")

    results = []
    for i,t in enumerate(trades):
        sym = t.get("instrument","")
        print(f"  [{i+1}/{len(trades)}] {sym}...", end="", flush=True)
        try:
            a = extract(t)
            if a: results.append(a); print(f" {'W' if a['won'] else 'L'}")
            else: print(" skip")
        except Exception as e: print(f" err")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    print(f"\nTotal: {len(results)} ({len(winners)}W / {len(losers)}L)")
    print(f"Net: ${sum(r['pnl'] for r in results):+,.2f}")

    print("\n" + "=" * 110)
    print("PROPORTIONAL DISTRIBUTION: What % of winners vs % of losers land in each bucket")
    print("W% = what proportion of ALL winners are in this bucket")
    print("L% = what proportion of ALL losers are in this bucket")
    print("Gap = W% - L% (positive = winners cluster here, negative = losers cluster here)")
    print("=" * 110)

    # Every factor with proportional breakdown
    proportional(results, "dc", "1. DIRECTIONAL CANDLES (sucker move)",
        [(0,1,"0 candles"), (1,2,"1 candle"), (2,3,"2 candles"), (3,4,"3 candles"), (4,99,"4+ candles")])

    proportional(results, "sma_d", "2. SMA20 DISTANCE (pips from SMA20)",
        [(-999,-20,"<-20p (well below)"), (-20,-5,"-20 to -5p (below)"), (-5,5,"-5 to +5p (at SMA)"),
         (5,20,"+5 to +20p (above)"), (20,999,">+20p (well above)")])

    proportional(results, "hour", "3. ENTRY HOUR (UTC)",
        [(0,4,"0-3 UTC"), (4,8,"4-7 UTC"), (8,12,"8-11 UTC"),
         (12,16,"12-15 UTC"), (16,20,"16-19 UTC"), (20,24,"20-23 UTC")])

    proportional(results, "bage", "4. BOX AGE (hours since prior day)",
        [(0,12,"<12h (fresh)"), (12,24,"12-24h (aging)"), (24,48,"24-48h (stale)"), (48,999,"48h+ (very stale)")])

    proportional(results, "vr", "5. VOLUME RATIO (recent/older activity)",
        [(0,0.7,"<0.7 (quiet)"), (0.7,0.9,"0.7-0.9"), (0.9,1.1,"0.9-1.1 (calm)"),
         (1.1,1.5,"1.1-1.5 (active)"), (1.5,99,"1.5+ (volatile)")])

    proportional(results, "ns", "6. NATURAL STOP (pips)",
        [(-99,1,"<=0 (INVALID)"), (1,4,"1-3p (very tight)"), (4,7,"4-6p (tight)"),
         (7,12,"7-11p (moderate)"), (12,999,"12p+ (wide)")])

    proportional(results, "rsi", "7. RSI (14-period 5M)",
        [(0,25,"<25 (very oversold)"), (25,40,"25-40 (oversold)"), (40,50,"40-50"),
         (50,60,"50-60 (neutral)"), (60,75,"60-75"), (75,100,"75+ (very overbought)")])

    proportional(results, "bbp", "8. BB POSITION (1H bands, 0=lower, 1=upper)",
        [(0,0.15,"<0.15 (extreme low)"), (0.15,0.35,"0.15-0.35 (lower)"), (0.35,0.50,"0.35-0.50"),
         (0.50,0.65,"0.50-0.65"), (0.65,0.85,"0.65-0.85 (upper)"), (0.85,1.5,"0.85+ (extreme high)")])

    proportional_cat(results, "bbs", "9. DOUBLE BB STATE (5M)")

    proportional(results, "wp", "10. WALL PROXIMITY (0=at correct wall, 1=far)",
        [(-.5,0.15,"<0.15 (at wall)"), (0.15,0.30,"0.15-0.30"), (0.30,0.50,"0.30-0.50"),
         (0.50,0.70,"0.50-0.70"), (0.70,1.5,"0.70+ (wrong side)")])

    proportional(results, "e50d", "11. EMA50 DISTANCE (% of box)",
        [(0,20,"<20% (at EMA50)"), (20,40,"20-40%"), (40,60,"40-60%"),
         (60,100,"60-100%"), (100,999,"100%+ (far)")])

    proportional(results, "e20d", "12. EMA20 DISTANCE (% of box)",
        [(0,15,"<15% (at EMA20)"), (15,30,"15-30%"), (30,50,"30-50%"), (50,999,"50%+ (far)")])

    proportional(results, "sl", "13. EMA SLOPE (%)",
        [(-99,-0.1,"<-0.1 (strong dn)"), (-0.1,-0.02,"-0.1 to -0.02"), (-0.02,0.02,"RANGING"),
         (0.02,0.1,"0.02-0.1 (mild up)"), (0.1,99,">0.1 (strong up)")])

    proportional(results, "zs", "14. Z-SCORE (1H)",
        [(-99,-1.5,"<-1.5 (extreme dn)"), (-1.5,-0.5,"-1.5 to -0.5"), (-0.5,0.5,"NEUTRAL"),
         (0.5,1.5,"0.5-1.5"), (1.5,99,">1.5 (extreme up)")])

    proportional(results, "otr", "15. OTR (round-trip spread / half box %)",
        [(0,8,"<8%"), (8,12,"8-12%"), (12,18,"12-18%"), (18,25,"18-25%"), (25,999,"25%+")])

    proportional(results, "adr", "16. ADR CONSUMED",
        [(0,0.4,"<40%"), (0.4,0.6,"40-60%"), (0.6,0.8,"60-80%"),
         (0.8,1.0,"80-100%"), (1.0,99,"100%+")])

    proportional(results, "sprd_sl", "17. SPREAD / NATURAL SL %",
        [(0,20,"<20%"), (20,40,"20-40%"), (40,60,"40-60%"),
         (60,100,"60-100%"), (100,9999,"100%+ (spread>stop)")])

    proportional(results, "bxp", "18. BOX SIZE (pips)",
        [(0,40,"<40p"), (40,70,"40-70p"), (70,100,"70-100p"),
         (100,200,"100-200p"), (200,9999,"200p+")])

    proportional(results, "wr", "19. WICK RATIO (wick/body of signal candle)",
        [(0,0.3,"<0.3 (tiny wick)"), (0.3,0.7,"0.3-0.7"), (0.7,1.2,"0.7-1.2"),
         (1.2,2.0,"1.2-2.0"), (2.0,99,"2.0+ (big wick)")])

    proportional(results, "bp", "20. BODY % OF CANDLE",
        [(0,0.25,"<25% (doji)"), (0.25,0.45,"25-45%"), (0.45,0.65,"45-65%"),
         (0.65,1.01,"65%+ (strong body)")])

    proportional(results, "dur", "21. DURATION (minutes)",
        [(0,15,"<15m"), (15,60,"15-60m"), (60,180,"1-3h"),
         (180,360,"3-6h"), (360,9999,"6h+")])

    proportional(results, "tch", "22. PDH/PDL TOUCHES (24h)",
        [(0,3,"0-2"), (3,6,"3-5"), (6,10,"6-9"), (10,15,"10-14"), (15,999,"15+")])

    proportional(results, "mom", "23. MOMENTUM CANDLES (consecutive)",
        [(0,1,"0"), (1,2,"1"), (2,3,"2"), (3,4,"3"), (4,99,"4+")])

    proportional(results, "sp", "24. SPREAD (raw pips)",
        [(0,1.5,"<1.5p"), (1.5,3,"1.5-3p"), (3,5,"3-5p"), (5,10,"5-10p"), (10,999,"10p+")])

    proportional(results, "rr", "25. R:R vs TP1",
        [(0,0.5,"<0.5"), (0.5,1.0,"0.5-1.0"), (1.0,2.0,"1.0-2.0"),
         (2.0,5.0,"2.0-5.0"), (5.0,999,"5.0+")])

    proportional_cat(results, "is_ct", "26. COUNTER-TREND")
    proportional_cat(results, "rng", "27. RANGING")
    proportional_cat(results, "pbull", "28. PRIOR DAY BULLISH")
    proportional_cat(results, "stype", "29. SIGNAL TYPE")

    proportional(results, "cr", "30. SIGNAL CANDLE RANGE (pips)",
        [(0,3,"<3p"), (3,6,"3-6p"), (6,10,"6-10p"), (10,20,"10-20p"), (20,999,"20p+")])

    proportional(results, "sprd_hf", "31. SPREAD % OF HALF BOX",
        [(0,5,"<5%"), (5,8,"5-8%"), (8,12,"8-12%"), (12,20,"12-20%"), (20,999,"20%+")])

    proportional_cat(results, "zt", "32. ZONE TIER")

    # Final summary: strongest proportional gaps
    print("\n" + "=" * 110)
    print("TOP PROPORTIONAL GAPS (where winners and losers diverge most)")
    print("=" * 110)
    print("These are the buckets where the W% vs L% gap is largest.\n")

    # Collect all gaps
    all_gaps = []
    def collect_gaps(results, key, label, buckets):
        winners = [r for r in results if r["won"]]
        losers = [r for r in results if not r["won"]]
        tw = len(winners); tl = len(losers)
        for lo, hi, bl in buckets:
            w = [r for r in winners if r.get(key) is not None and lo <= r[key] < hi]
            l = [r for r in losers if r.get(key) is not None and lo <= r[key] < hi]
            if len(w)+len(l) == 0: continue
            wpct = len(w)/tw*100 if tw>0 else 0
            lpct = len(l)/tl*100 if tl>0 else 0
            gap = wpct - lpct
            wr = len(w)/(len(w)+len(l))*100
            all_gaps.append((abs(gap), f"{label}: {bl}", wpct, lpct, gap, wr, len(w), len(l)))

    collect_gaps(results, "dc", "Dir candles", [(0,1,"0"),(1,2,"1"),(2,3,"2"),(3,4,"3"),(4,99,"4+")])
    collect_gaps(results, "sma_d", "SMA20 dist", [(-999,-5,"below"),(-5,5,"at SMA"),(5,20,"above 5-20"),(20,999,"above 20+")])
    collect_gaps(results, "hour", "Entry hour", [(0,8,"0-7 UTC"),(8,12,"8-11"),(12,20,"12-19"),(20,24,"20-23")])
    collect_gaps(results, "bage", "Box age", [(0,12,"<12h"),(12,24,"12-24h"),(24,999,"24h+")])
    collect_gaps(results, "vr", "Vol ratio", [(0,0.9,"<0.9"),(0.9,1.1,"0.9-1.1"),(1.1,1.5,"1.1-1.5"),(1.5,99,"1.5+")])
    collect_gaps(results, "ns", "Nat stop", [(-99,1,"<=0"),(1,7,"1-6p"),(7,99,"7p+")])
    collect_gaps(results, "rsi", "RSI", [(0,40,"<40"),(40,55,"40-55"),(55,75,"55-75"),(75,100,"75+")])
    collect_gaps(results, "bbp", "BB pos", [(0,0.35,"<0.35"),(0.35,0.65,"0.35-0.65"),(0.65,1.5,"0.65+")])
    collect_gaps(results, "e50d", "EMA50 dist", [(0,20,"<20%"),(20,60,"20-60%"),(60,999,"60%+")])
    collect_gaps(results, "otr", "OTR", [(0,8,"<8%"),(8,18,"8-18%"),(18,999,"18%+")])
    collect_gaps(results, "dur", "Duration", [(0,60,"<1h"),(60,360,"1-6h"),(360,9999,"6h+")])
    collect_gaps(results, "bxp", "Box size", [(0,70,"<70p"),(70,200,"70-200p"),(200,9999,"200p+")])

    all_gaps.sort(key=lambda x: x[0], reverse=True)
    print(f"  {'Factor: Bucket':<40} {'W%':>5} {'L%':>5} {'GAP':>6} {'WR':>4} {'Trades':>7}")
    print(f"  {'-'*72}")
    for g in all_gaps[:30]:
        direction = "←WIN" if g[4] > 0 else "←LOSE"
        print(f"  {g[1]:<40} {g[2]:>4.0f}% {g[3]:>4.0f}% {g[4]:>+5.0f}% {g[5]:>3.0f}% {g[6]:>2}W/{g[7]:<2}L  {direction}")


if __name__ == "__main__":
    main()
