#!/usr/bin/env python3
"""
V3 Formula — Full trade table showing every component for every trade.
Raw OANDA data. Shows the complete breakdown so you can see the recipe.
"""

import os, requests, statistics, time as _t
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

def bb_state(cl):
    if len(cl) < 20: return "UNK"
    s20 = sum(cl[-20:])/20
    sd = statistics.stdev(cl[-20:]) if len(cl[-20:]) > 1 else 0.0001
    ua = s20+2*sd; la = s20-2*sd
    n = min(4, len(cl)); s4 = sum(cl[-n:])/n
    sd4 = statistics.stdev(cl[-n:]) if n >= 2 else 0.0001
    ub = s4+4*sd4; lb = s4-4*sd4
    c = cl[-1]; c1 = cl[-2] if len(cl)>=2 else c; c2 = cl[-3] if len(cl)>=3 else c1
    if c > ub and ub > ua: return "EXT_UP"
    if c < lb and lb < la: return "EXT_DN"
    if c <= ua and (c1 > ua or c2 > ua): return "REJ_S"
    if c >= la and (c1 < la or c2 < la): return "REJ_L"
    if c > ua and c1 > ua and c >= c1: return "BRK_UP"
    if c < la and c1 < la and c <= c1: return "BRK_DN"
    if c > ua: return "STR_UP"
    if c < la: return "STR_DN"
    return "NORM"

def analyze(t):
    sym = t["instrument"]; units = float(t["initialUnits"])
    entry = float(t["price"]); pnl = float(t["realizedPL"])
    ot = t["openTime"]; ct = t["closeTime"]
    d = "S" if units < 0 else "L"; pip = 0.01 if "JPY" in sym else 0.0001
    try:
        odt = datetime.fromisoformat(ot[:26].replace("Z","+00:00"))
        cdt = datetime.fromisoformat(ct[:26].replace("Z","+00:00"))
        dur = (cdt-odt).total_seconds()/60; hour = odt.hour
    except: dur = 0; hour = 12

    daily = cndl(sym,"D",ot,15); hourly = cndl(sym,"H1",ot,60); m5 = cndl(sym,"M5",ot,80)
    if len(daily)<3 or len(m5)<20 or len(hourly)<20: return None

    ed = ot[:10]; pd = None
    for c in reversed(daily):
        if c["time"][:10] < ed:
            h,l = float(c["mid"]["h"]),float(c["mid"]["l"])
            if (h-l)/l > 0.0005: pd = c; break
    if not pd: return None

    pdh=float(pd["mid"]["h"]); pdl=float(pd["mid"]["l"]); bx=pdh-pdl; hf=bx/2; bp=bx/pip
    bpos = (entry-pdl)/bx if bx>0 else 0.5
    wp = (entry-pdl)/bx if d=="L" else (pdh-entry)/bx
    wp = wp if bx > 0 else 1

    # ATR
    atrs = [max(float(daily[i]["mid"]["h"])-float(daily[i]["mid"]["l"]),
                abs(float(daily[i]["mid"]["h"])-float(daily[i-1]["mid"]["c"])),
                abs(float(daily[i]["mid"]["l"])-float(daily[i-1]["mid"]["c"])))
            for i in range(1,len(daily))]
    atr = sum(atrs)/len(atrs) if atrs else bx
    tc = daily[-1]["mid"]; adr = (float(tc["h"])-float(tc["l"]))/atr if atr>0 else 0

    # Box age
    try:
        pdt = datetime.fromisoformat(pd["time"][:26].replace("Z","+00:00"))
        bage = (odt-pdt).total_seconds()/3600
    except: bage = 24

    # Spread
    la = m5[-1]; ask=float(la.get("ask",{}).get("c",0)); bid=float(la.get("bid",{}).get("c",0))
    sprd = (ask-bid) if ask>0 and bid>0 else pip*2; sp = sprd/pip

    # Signal candle
    sig=None; dc=0
    for i in range(len(m5)-1, max(len(m5)-8,-1), -1):
        mm=m5[i]["mid"]; o,h,l,c = float(mm["o"]),float(mm["h"]),float(mm["l"]),float(mm["c"])
        if sig is None:
            if (d=="L" and c>o) or (d=="S" and c<o):
                body=abs(c-o) or pip*0.1; wk=(min(o,c)-l) if d=="L" else (h-max(o,c))
                sig={"low":l,"high":h,"wick_ratio":wk/body}
                # Signal type
                if wk/body >= 1.5 and abs(c-o)/(h-l or pip) <= 0.30: stype = "JW"
                else: stype = "STD"
        else:
            if (d=="L" and c<o) or (d=="S" and c>o): dc += 1
            else: break

    if sig:
        if d=="L": ns = (entry-(sig["low"]-2*pip))/pip
        else: ns = ((sig["high"]+2*pip)-entry)/pip
        wr = sig["wick_ratio"]
    else: ns=10; wr=0; stype="?"

    # BB + z
    c1h = [float(c["mid"]["c"]) for c in hourly[-20:]]
    mn=sum(c1h)/len(c1h); sd=statistics.stdev(c1h) if len(c1h)>1 else 0.0001
    zs = (entry-mn)/sd if sd>0 else 0
    ub=mn+2*sd; lb=mn-2*sd; w=ub-lb; bbp=(entry-lb)/w if w>0 else 0.5

    # Double BB
    c5m = [float(c["mid"]["c"]) for c in m5[-25:]]
    bbs = bb_state(c5m)

    # SMA20 distance (from BB calc)
    sma20 = sum(c5m[-20:])/20 if len(c5m)>=20 else entry
    sma_dist = (entry - sma20)/pip

    # RSI
    cr = [float(c["mid"]["c"]) for c in m5[-15:]]
    rsi = rsi_c(cr) or 50

    # EMAs
    ah = [float(c["mid"]["c"]) for c in hourly]
    e50 = ema_c(ah, 50)
    e50d = abs(entry-e50)/bx*100 if e50 and bx>0 else 50
    is_ct = (d=="L" and entry>(e50 or 0)) or (d=="S" and entry<(e50 or 999999)) if e50 else False

    # Slope + ranging
    if len(ah)>=10:
        sl = (sum(ah[-5:])/5-sum(ah[-10:-5])/5)/(sum(ah[-10:-5])/5)*100
    else: sl=0
    rng = abs(sl) < 0.02

    # Volume
    if len(m5)>=20:
        rr=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-5:]]
        ro=[float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-20:-5]]
        vr=(sum(rr)/5)/(sum(ro)/15) if sum(ro)>0 else 1
    else: vr=1

    # Zone tier
    dalign = any(abs(entry-dl)/dl < 0.002 for dl in [pdh,pdl])
    zt = 1 if dalign else 3

    # RR
    tp1 = (hf/pip)/2; rr_tp1 = tp1/ns if ns>0 else 0

    return {
        "sym":sym, "d":d, "pnl":pnl, "won":pnl>0,
        "zt":zt, "stype":stype, "hour":hour, "bage":bage,
        "vr":vr, "rng":rng, "bbs":bbs, "dc":dc, "sma_d":sma_dist,
        "ns":ns, "e50d":e50d, "wp":wp, "bbp":bbp, "zs":zs,
        "rsi":rsi, "is_ct":is_ct, "adr":adr, "rr":rr_tp1,
        "bp":bp, "sp":sp, "dur":dur, "sl":sl,
    }

def score_v3(r):
    """V3 Formula — every component visible."""
    s = 0; bd = {}

    # === LAYER 0: HARD BLOCKS ===
    blocks = []
    if r["ns"] <= 0: blocks.append("INVALID_SL")
    if r["sp"] > r["ns"] and r["ns"] > 0: blocks.append("SPRD>SL")
    if 45 <= r["rsi"] <= 55: blocks.append("RSI_NEUT")
    if r["bbs"] in ("STR_UP","STR_DN"): blocks.append("BB_STRETCH")
    if blocks: return 0, {"BLOCKED": ", ".join(blocks)}, blocks

    # === LAYER 1: BASE ===
    zt = {1:20, 2:12, 3:6, 4:3}.get(r["zt"], 3)
    s += zt; bd["zon"] = zt

    pt = {"JW":15, "STD":8}.get(r["stype"], 8)
    s += pt; bd["pat"] = pt

    # === LAYER 2: MARKET STATE ===
    h = r["hour"]
    if h < 8: hp = 8
    elif h < 12: hp = 0
    elif h < 20: hp = -5
    else: hp = -8
    s += hp; bd["hr"] = hp

    ba = r["bage"]
    if ba < 12: bap = 8
    elif ba < 24: bap = -8
    else: bap = -5
    s += bap; bd["age"] = bap

    v = r["vr"]
    if 0.9 <= v <= 1.1: vp = 5
    elif v > 1.5 or v < 0.7: vp = -8
    else: vp = 0
    s += vp; bd["vol"] = vp

    if r["rng"]: s -= 20; bd["rng"] = -20

    if r["bbs"] in ("REJ_L","REJ_S"): s += 5; bd["bbrej"] = 5

    # === LAYER 3: ENTRY QUALITY ===
    dc = r["dc"]
    if dc >= 4: cp = 20
    elif dc >= 3: cp = 8
    elif dc >= 2: cp = 3
    elif dc == 1: cp = 0
    else: cp = -15
    s += cp; bd["conv"] = cp

    sd = r["sma_d"]
    if sd < -5: smp = 5
    elif -5 <= sd <= 5: smp = 0
    elif 5 < sd <= 20: smp = -8
    else: smp = -5
    s += smp; bd["sma"] = smp

    ns = r["ns"]
    if 4 <= ns <= 6: nsp = 5
    elif ns >= 12: nsp = -5
    else: nsp = 0
    s += nsp; bd["stp"] = nsp

    if r["e50d"] < 20: s -= 8; bd["e50"] = -8

    wp = r["wp"]
    if wp <= 0.20: wpp = 5
    elif wp >= 0.50: wpp = -5
    else: wpp = 0
    s += wpp; bd["wal"] = wpp

    if 0.35 <= r["bbp"] <= 0.50: s -= 10; bd["bbm"] = -10

    # === LAYER 4: CONTEXT ===
    az = abs(r["zs"])
    if az >= 2.0: zp = 10
    elif az >= 1.5: zp = 6
    elif az >= 1.0: zp = 3
    else: zp = 0
    s += zp; bd["z"] = zp

    if (r["d"]=="L" and r["zs"]<-0.5) or (r["d"]=="S" and r["zs"]>0.5):
        s += 5; bd["za"] = 5

    adr = r["adr"]
    if 0.35 <= adr <= 0.75: ap = 4
    elif 0.20 <= adr <= 0.90: ap = 2
    else: ap = 0
    s += ap; bd["adr"] = ap

    rr = r["rr"]
    if rr >= 2.0: rrp = 3
    elif rr >= 1.0: rrp = 2
    else: rrp = 0
    s += rrp; bd["rr"] = rrp

    if r["is_ct"]:
        if r["zt"] == 1: s -= 10; bd["ct1"] = -10
        elif r["zt"] == 2: s += 5; bd["ct2"] = 5

    return s, bd, []

def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state":"CLOSED","count":"50"})
    trades = r.json().get("trades",[])
    print(f"Scoring {len(trades)} trades with V3 formula (raw OANDA data)...")

    results = []
    for i,t in enumerate(trades):
        sym = t.get("instrument","")
        print(f"  [{i+1}/{len(trades)}] {sym}...", end="", flush=True)
        try:
            a = analyze(t)
            if a:
                sc, bd, blk = score_v3(a)
                a["score"] = sc; a["bd"] = bd; a["blk"] = blk
                results.append(a)
                mark = "W" if a["won"] else "L"
                if blk: print(f" {mark} ${a['pnl']:+,.0f} BLOCKED:{','.join(blk)}")
                else: print(f" {mark} ${a['pnl']:+,.0f} score={sc}")
            else: print(" skip")
        except Exception as e: print(f" err: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]

    # === FULL TABLE ===
    print()
    print("=" * 200)
    print("COMPLETE V3 SCORING TABLE — Every trade, every component")
    print("=" * 200)

    hdr = f"{'#':<3} {'Pair':<8} {'D':<2} {'PnL':>8} {'W':>1} {'SC':>4} |"
    hdr += f" {'zon':>3} {'pat':>3} | {'hr':>3} {'age':>3} {'vol':>3} {'rng':>3} {'bbr':>3} |"
    hdr += f" {'cnv':>3} {'sma':>3} {'stp':>3} {'e50':>3} {'wal':>3} {'bbm':>3} |"
    hdr += f" {'z':>3} {'za':>3} {'adr':>3} {'rr':>3} {'ct':>3} |"
    hdr += f" {'BBS':<6} {'RSI':>4} {'BB':>5} {'DC':>2} {'NS':>4} {'SP':>4} {'HR':>3} {'AGE':>4} {'VR':>4} | {'VERDICT':<12}"
    print(hdr)
    print("-" * 200)

    for i, r in enumerate(sorted(results, key=lambda x: x["pnl"], reverse=True)):
        bd = r["bd"]
        blk = r["blk"]
        mark = "W" if r["won"] else "L"

        if blk:
            verdict = f"BLOCK:{blk[0]}"
        elif r["score"] >= 25:
            verdict = "PASS"
        else:
            verdict = "SCORE_LOW"

        row = f"{i+1:<3} {r['sym']:<8} {r['d']:<2} {r['pnl']:>+8,.0f} {mark:>1} {r['score']:>4} |"
        row += f" {bd.get('zon',''):>3} {bd.get('pat',''):>3} |"
        row += f" {bd.get('hr',''):>3} {bd.get('age',''):>3} {bd.get('vol',''):>3} {bd.get('rng',''):>3} {bd.get('bbrej',''):>3} |"
        row += f" {bd.get('conv',''):>3} {bd.get('sma',''):>3} {bd.get('stp',''):>3} {bd.get('e50',''):>3} {bd.get('wal',''):>3} {bd.get('bbm',''):>3} |"
        row += f" {bd.get('z',''):>3} {bd.get('za',''):>3} {bd.get('adr',''):>3} {bd.get('rr',''):>3} {bd.get('ct1',bd.get('ct2','')):>3} |"
        row += f" {r['bbs']:<6} {r['rsi']:>4.0f} {r['bbp']:>5.2f} {r['dc']:>2} {r['ns']:>4.0f} {r['sp']:>4.1f} {r['hour']:>3} {r['bage']:>4.0f} {r['vr']:>4.2f} | {verdict:<12}"
        print(row)

    # Summary
    passed = [r for r in results if r["score"] >= 25 and not r["blk"]]
    blocked_hard = [r for r in results if r["blk"]]
    blocked_score = [r for r in results if r["score"] < 25 and not r["blk"]]

    pw = [r for r in passed if r["won"]]; pl = [r for r in passed if not r["won"]]
    bw = [r for r in blocked_hard + blocked_score if r["won"]]
    bl = [r for r in blocked_hard + blocked_score if not r["won"]]

    print()
    print("=" * 100)
    print("V3 FORMULA RESULTS")
    print("=" * 100)
    print(f"  Total trades: {len(results)} ({len(winners)}W / {len(losers)}L)")
    print(f"  Net P&L all:  ${sum(r['pnl'] for r in results):+,.2f}")
    print()
    print(f"  PASSED (score >= 25, no blocks): {len(passed)} trades")
    print(f"    Winners: {len(pw)}  Losers: {len(pl)}  WR: {len(pw)/len(passed)*100 if passed else 0:.0f}%")
    print(f"    Net P&L: ${sum(r['pnl'] for r in passed):+,.2f}")
    print()
    print(f"  BLOCKED (hard blocks): {len(blocked_hard)} trades")
    for r in blocked_hard:
        print(f"    {r['sym']:<10} ${r['pnl']:>+8,.0f} {'W' if r['won'] else 'L'}  {r['bd'].get('BLOCKED','')}")
    print()
    print(f"  BLOCKED (score < 25): {len(blocked_score)} trades")
    for r in sorted(blocked_score, key=lambda x: x["score"]):
        print(f"    {r['sym']:<10} ${r['pnl']:>+8,.0f} {'W' if r['won'] else 'L'}  score={r['score']}")
    print()
    print(f"  Blocked winners: {len(bw)} (${sum(r['pnl'] for r in bw):+,.2f} lost)")
    print(f"  Blocked losers:  {len(bl)} (${sum(r['pnl'] for r in bl):+,.2f} avoided)")

if __name__ == "__main__":
    main()
