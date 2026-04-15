#!/usr/bin/env python3
"""
Run your friend's WR-Lift Hybrid formula against the verified raw data CSV.
Uses data/trades_features_verified.csv — no API calls, just math on saved data.
"""

import csv
import sys
from pathlib import Path


def load_trades(path):
    trades = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert types
            for k in ['pnl','entry','hour','bage','dur','bxp','bpos','wp','adr','otr',
                       'sp','ns','dc','mom','sma_d','bbp','zs','rsi','e50d','e20d',
                       'sl','vr','bp']:
                row[k] = float(row[k])
            for k in ['won','is_rng','is_ct','zt','tch']:
                row[k] = int(row[k])
            trades.append(row)
    return trades


def score_hybrid(r):
    """Your friend's WR-Lift Hybrid with Pair Layer."""
    blocks = []

    # === LAYER 0: HARD BLOCKS ===
    if 45 <= r['rsi'] <= 55:
        blocks.append("RSI_NEUT")
    if r['bbs'] == 'STR_UP':
        blocks.append("STR_UP")
    if r['dur'] >= 720:  # 12h
        blocks.append("DUR_12H")
    if r['otr'] < 8 and r['bbs'] == 'NORM':
        blocks.append("OTR<8+NORM")
    if 18 <= r['bage'] <= 24 and r['e20d'] < 15:
        blocks.append("STALE+E20")

    if blocks:
        return 0, blocks, {}

    s = 0
    bd = {}

    # === LAYER 1: SINGLE FACTOR BASE ===

    # Entry hour
    h = r['hour']
    if h < 8: p = 13
    elif h < 12: p = 2
    elif h < 16: p = -8
    elif h < 20: p = -4
    else: p = -7
    s += p; bd['hr'] = p

    # Box age
    a = r['bage']
    if a < 8: p = 13
    elif a < 12: p = 6
    elif a < 18: p = 0
    elif a < 24: p = -12
    else: p = -4
    s += p; bd['age'] = p

    # Natural stop
    ns = r['ns']
    if 4 <= ns <= 6: p = 9
    elif 6 < ns <= 8: p = 3
    elif ns < 4: p = -4
    else: p = -2
    s += p; bd['stp'] = p

    # Volume ratio
    v = r['vr']
    if 0.9 <= v <= 1.1: p = 9
    elif 1.1 < v <= 1.3: p = 2
    elif 0.7 <= v < 0.9: p = -4
    elif v > 1.3: p = -3
    else: p = 0
    s += p; bd['vol'] = p

    # Momentum candles
    m = r['mom']
    if 2 <= m <= 3: p = 8
    elif m == 1: p = 2
    elif m == 0: p = -5
    elif m >= 4: p = 3
    else: p = 0
    s += p; bd['mom'] = p

    # Directional candles
    dc = r['dc']
    if dc >= 4: p = 7
    elif 2 <= dc <= 3: p = 3
    elif dc == 1: p = 0
    else: p = -6
    s += p; bd['dc'] = p

    # Z-score magnitude
    az = abs(r['zs'])
    if 0.5 <= az < 1.0: p = 6
    elif 1.0 <= az < 1.5: p = 5
    elif az >= 1.5: p = 2
    else: p = -9  # <0.5
    s += p; bd['z'] = p

    # BB position
    bb = r['bbp']
    if 0.65 <= bb <= 0.85: p = 5
    elif 0.50 <= bb < 0.65: p = 1
    elif 0.35 <= bb < 0.50: p = -3
    elif bb > 0.85: p = -4
    else: p = -2  # <0.35
    s += p; bd['bb'] = p

    # EMA50 distance
    if r['e50d'] >= 60: p = 5
    elif r['e50d'] < 20: p = -10
    else: p = 0
    s += p; bd['e50'] = p

    # EMA20 distance
    if 15 <= r['e20d'] <= 30: p = 3
    elif r['e20d'] >= 30: p = 1
    elif r['e20d'] < 15: p = -7
    else: p = 0
    s += p; bd['e20'] = p

    # OTR
    o = r['otr']
    if 8 <= o <= 18: p = 4
    elif o < 8: p = -11
    elif o > 30: p = -2
    else: p = 0
    s += p; bd['otr'] = p

    # ADR
    if r['adr'] < 0.8: p = 4
    elif 0.8 <= r['adr'] <= 1.2: p = -3
    else: p = -1
    s += p; bd['adr'] = p

    # Duration
    d = r['dur']
    if 30 <= d <= 120: p = 6
    elif 120 < d <= 360: p = 2
    elif d < 30: p = -2
    elif 360 < d <= 720: p = -5
    else: p = 0
    s += p; bd['dur'] = p

    # Wall proximity
    wp = r['wp']
    if wp < 0.15: p = 2
    elif 0.15 <= wp < 0.30: p = -9
    elif 0.30 <= wp < 0.50: p = 1
    else: p = -2
    s += p; bd['wal'] = p

    # Body %
    bp = r['bp']
    if bp < 0.25: p = 2
    elif 0.25 <= bp < 0.45: p = 0
    elif 0.45 <= bp <= 0.65: p = -8
    else: p = -2
    s += p; bd['bdy'] = p

    # BB state
    bbs = r['bbs']
    if bbs == 'NORM': p = 3
    elif bbs in ('REJ_L', 'REJ_S'): p = 2
    elif bbs in ('BRK_UP', 'BRK_DN'): p = -1
    elif bbs == 'STR_DN': p = -3
    else: p = 0
    s += p; bd['bbs'] = p

    # RSI (outside neutral)
    rsi = r['rsi']
    if rsi < 30: p = 7
    elif 30 <= rsi < 45: p = 3
    elif 55 <= rsi < 70: p = -2
    elif rsi >= 70: p = -3
    else: p = 0
    s += p; bd['rsi'] = p

    # === LAYER 2: PAIRED ASPECT BONUSES ===
    pairs = 0

    # Positive pairs
    if r['hour'] < 8 and bbs == 'NORM':
        pairs += 14; bd['p_hr_norm'] = 14
    if r['hour'] < 8 and r['mom'] == 0:
        pairs += 13; bd['p_hr_mom0'] = 13
    if r['hour'] < 8 and 0.5 <= az < 1.0:
        pairs += 13; bd['p_hr_z'] = 13
    if r['hour'] < 8 and 4 <= ns <= 6:
        pairs += 11; bd['p_hr_ns'] = 11
    if r['hour'] < 8 and r['bage'] < 8:
        pairs += 11; bd['p_hr_age'] = 11
    if 1.0 <= az < 1.5 and bbs == 'NORM':
        pairs += 11; bd['p_z_norm'] = 11
    if r['hour'] < 8 and r['e50d'] >= 60:
        pairs += 11; bd['p_hr_e50'] = 11
    if r['bage'] < 8 and rsi < 45:
        pairs += 9; bd['p_age_rsi'] = 9
    if r['bage'] < 8 and 8 <= r['otr'] <= 18:
        pairs += 9; bd['p_age_otr'] = 9
    if r['bage'] < 8 and bbs == 'NORM':
        pairs += 9; bd['p_age_norm'] = 9

    # Negative pairs
    if 12 <= r['hour'] < 16 and 0.8 <= r['adr'] <= 1.2:
        pairs -= 13; bd['n_hr_adr'] = -13
    if 12 <= r['hour'] < 16 and dc == 0:
        pairs -= 11; bd['n_hr_dc0'] = -11
    if az < 0.5 and 0.8 <= r['adr'] <= 1.2:
        pairs -= 9; bd['n_z_adr'] = -9
    if az < 0.5 and 0.45 <= bp <= 0.65:
        pairs -= 9; bd['n_z_bdy'] = -9
    if r['mom'] == 0 and bb > 0.85:
        pairs -= 9; bd['n_mom_bb'] = -9
    if ns < 4 and 0.7 <= v < 0.9:
        pairs -= 9; bd['n_ns_vr'] = -9
    if dc == 0 and r['otr'] < 8:
        pairs -= 9; bd['n_dc_otr'] = -9
    if az < 0.5 and bbs == 'NORM':
        pairs -= 9; bd['n_z_norm'] = -9

    s += pairs
    bd['pairs_total'] = pairs

    return s, blocks, bd


def main():
    csv_path = Path(__file__).parent.parent / "data" / "trades_features_verified.csv"
    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found")
        sys.exit(1)

    trades = load_trades(csv_path)
    print(f"Loaded {len(trades)} trades from {csv_path}")
    print(f"Source: raw OANDA candle data, verified pipeline")
    print()

    # Score all trades
    for t in trades:
        t['score'], t['blocks'], t['bd'] = score_hybrid(t)

    winners = [t for t in trades if t['won']]
    losers = [t for t in trades if not t['won']]

    # Full table
    print("=" * 200)
    print("HYBRID FORMULA (friend's version) — FULL SCORING TABLE")
    print("=" * 200)

    hdr = f"{'#':<3} {'Pair':<8} {'D':<2} {'PnL':>8} {'W':>1} {'SC':>5} |"
    hdr += f" {'hr':>3} {'age':>4} {'stp':>3} {'vol':>3} {'mom':>3} {'dc':>3} {'z':>3} {'bb':>3} {'e50':>4} {'e20':>3} {'otr':>4} {'adr':>3} {'dur':>3} {'wal':>3} {'bdy':>3} {'bbs':>3} {'rsi':>3} |"
    hdr += f" {'pairs':>5} | {'BBS':<6} {'RSI':>4} {'DC':>2} {'NS':>5} {'HR':>3} {'AGE':>5} {'VR':>4} | {'VERDICT'}"
    print(hdr)
    print("-" * 200)

    for i, t in enumerate(sorted(trades, key=lambda x: x['pnl'], reverse=True)):
        bd = t['bd']
        mark = "W" if t['won'] else "L"

        if t['blocks']:
            verdict = f"BLOCK:{t['blocks'][0]}"
        elif t['score'] >= 65:
            verdict = f"TAKE(A)" if t['score'] >= 80 else f"TAKE(B)"
        elif t['score'] >= 50:
            verdict = f"BORDER({t['score']})"
        else:
            verdict = f"REJECT({t['score']})"

        row = f"{i+1:<3} {t['sym']:<8} {t['d']:<2} {t['pnl']:>+8,.0f} {mark:>1} {t['score']:>5} |"
        for k in ['hr','age','stp','vol','mom','dc','z','bb','e50','e20','otr','adr','dur','wal','bdy','bbs','rsi']:
            v = bd.get(k, '')
            row += f" {v:>3}" if isinstance(v, int) else f" {'':>3}"
        row += f" | {bd.get('pairs_total',0):>5}"
        row += f" | {t['bbs']:<6} {t['rsi']:>4.0f} {int(t['dc']):>2} {t['ns']:>5.0f} {int(t['hour']):>3} {t['bage']:>5.1f} {t['vr']:>4.2f} | {verdict}"
        print(row)

    # Summary
    passed = [t for t in trades if t['score'] >= 65 and not t['blocks']]
    border = [t for t in trades if 50 <= t['score'] < 65 and not t['blocks']]
    rejected = [t for t in trades if t['score'] < 50 and not t['blocks']]
    blocked = [t for t in trades if t['blocks']]

    pw = [t for t in passed if t['won']]; pl = [t for t in passed if not t['won']]
    bw = [t for t in border if t['won']]; bl = [t for t in border if not t['won']]
    rw = [t for t in rejected if t['won']]; rl = [t for t in rejected if not t['won']]
    hw = [t for t in blocked if t['won']]; hl = [t for t in blocked if not t['won']]

    print()
    print("=" * 100)
    print("HYBRID FORMULA RESULTS")
    print("=" * 100)
    print(f"  Total: {len(trades)} trades ({len(winners)}W / {len(losers)}L)")
    print(f"  Net P&L (all): ${sum(t['pnl'] for t in trades):+,.2f}")

    w_scores = [t['score'] for t in winners if not t['blocks']]
    l_scores = [t['score'] for t in losers if not t['blocks']]
    if w_scores and l_scores:
        print(f"\n  SEPARATION: W avg={sum(w_scores)/len(w_scores):.1f}, L avg={sum(l_scores)/len(l_scores):.1f}, GAP={sum(w_scores)/len(w_scores)-sum(l_scores)/len(l_scores):+.1f}")

    print(f"\n  TAKE (score >= 65): {len(passed)} trades")
    if passed:
        print(f"    {len(pw)}W / {len(pl)}L | WR: {len(pw)/len(passed)*100:.0f}% | Net: ${sum(t['pnl'] for t in passed):+,.2f}")

    print(f"\n  BORDERLINE (50-64): {len(border)} trades")
    if border:
        print(f"    {len(bw)}W / {len(bl)}L | WR: {len(bw)/len(border)*100:.0f}% | Net: ${sum(t['pnl'] for t in border):+,.2f}")

    print(f"\n  REJECT (score < 50): {len(rejected)} trades")
    if rejected:
        print(f"    {len(rw)}W / {len(rl)}L | WR: {len(rw)/len(rejected)*100:.0f}% | Net: ${sum(t['pnl'] for t in rejected):+,.2f}")

    print(f"\n  HARD BLOCKED: {len(blocked)} trades")
    if blocked:
        print(f"    {len(hw)}W / {len(hl)}L")
        for t in blocked:
            print(f"      {t['sym']:<10} ${t['pnl']:>+8,.2f} {'W' if t['won'] else 'L'}  {','.join(t['blocks'])}")

    # Threshold sweep
    print(f"\n  THRESHOLD SWEEP:")
    print(f"  {'Thresh':>6} {'Taken':>6} {'W':>3} {'L':>3} {'WR':>5} {'Net$':>10} {'BlkW$':>9}")
    for thr in range(0, 100, 5):
        p = [t for t in trades if t['score'] >= thr and not t['blocks']]
        pw2 = [t for t in p if t['won']]; pl2 = [t for t in p if not t['won']]
        bw2 = [t for t in trades if (t['score'] < thr or t['blocks']) and t['won']]
        tot = len(pw2) + len(pl2)
        if tot < 3: continue
        wr = len(pw2) / tot * 100
        net = sum(t['pnl'] for t in p)
        bwp = sum(t['pnl'] for t in bw2)
        marker = " <<<" if net > 0 else ""
        print(f"  {thr:>6} {tot:>6} {len(pw2):>3} {len(pl2):>3} {wr:>4.0f}% {net:>+9,.0f} {bwp:>+8,.0f}{marker}")


if __name__ == "__main__":
    main()
