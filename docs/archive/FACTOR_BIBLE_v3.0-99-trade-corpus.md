> **ARCHIVED 2026-05-30** as part of V4 cutover prep. Per-factor WR
> + delta analysis from 99 trades (50 V1 + 49 V2-practice, dated
> 2026-04-15). The scoring weights derived here informed V3.0/V3.1
> hybrid scorer — both subsequently disabled (ADR 3017, 2026-05-28)
> in favor of LightGBM v0 trained on the 838k-trade lab corpus.
> 
> Sample size is two orders of magnitude smaller than the current corpus.
> Preserved for historical-factor-discovery reference; do NOT promote
> its conclusions into live config. For current truth see
> `docs/RESEARCH_METHODOLOGY.md` (V4) and `data/matrix/`.

---

# Factor Bible — Complete Findings for Every Metric

> Source: 50 V1 LIVE trades + 49 V2 practice trades, all from raw OANDA candle data.
> No bot logs used. Every value computed from market data at entry time.
> Last updated: 2026-04-15

---

## How to Read This Document

Each factor shows:
- **Average comparison** (W avg vs L avg, delta %)
- **Distribution buckets** with win rate and net P&L
- **Verdict**: STRONG SIGNAL, MODERATE, WEAK, or NO SIGNAL
- **Recommendation**: what to do in the scoring formula

Factors are sorted by signal strength (strongest first).

---

## 1. SMA20 DISTANCE (pips, signed)

**V1 Live: W avg = -1.1p, L avg = +6.5p, Delta = -116%** ⭐⭐⭐

```
<-20p        1W/0L  WR=100%
-20 to -5    6W/4L  WR= 60%  Net= +$72
-5 to 5    16W/10L  WR= 62%  Net= -$80
5 to 20      4W/5L  WR= 44%  Net=-$195   ← DANGER
>20p         2W/2L  WR= 50%
```

**Finding:** Winners enter AT or BELOW the SMA20 (mean reversion). Losers enter ABOVE it (chasing). Entry above SMA20 by 5-20 pips = 44% WR.

**Verdict:** STRONG SIGNAL — not in current formula.
**Recommendation:** Add to scoring. Entry below SMA20 = +5, entry above SMA20 by 5+ pips = -10.

---

## 2. EMA SLOPE (%)

**V1 Live: W avg = 0.14%, L avg = 0.07%, Delta = +113%** ⭐⭐⭐
**V2 Practice: W avg = 0.10%, L avg = 0.04%, Delta = +184%** ⭐⭐⭐

```
<-0.1%       2W/2L  WR= 50%
-0.1 to -0.02  3W/5L  WR= 38%  ← negative slope + short??
RANGING      3W/2L  WR= 60%
0.02 to 0.1  7W/3L  WR= 70%  Net= -$75
>0.1%       14W/9L  WR= 61%
```

**Finding:** Winners enter when there IS a clear trend (EMA slope > 0.02%). Losers enter when trend is flat or mildly negative. Confirmed across both V1 and V2.

**Verdict:** STRONG SIGNAL — already in formula as ranging penalty (-20).
**Recommendation:** Keep -20 ranging penalty. Consider also penalizing negative slope entries that go WITH the negative slope (already covered by CT logic).

---

## 3. ENTRY HOUR (UTC)

**V1 Live: W avg = 10.2, L avg = 15.1, Delta = -33%** ⭐⭐⭐

```
0-3 UTC      6W/0L  WR=100%  Net= +$112  ← GOLD
4-7 UTC      8W/2L  WR= 80%  Net=  +$44  ← GOLD
8-11 UTC     2W/2L  WR= 50%
12-15 UTC    6W/8L  WR= 43%  Net= -$282  ← DANGER
16-19 UTC    4W/4L  WR= 50%  Net=  -$85
20-23 UTC    3W/5L  WR= 38%  Net=   -$1  ← DANGER
```

**Finding:** Early session entries (0-7 UTC = Sydney/Tokyo/London open) have 82% WR. Late session entries (12-23 UTC = NY afternoon/evening) have 42% WR. Massive separation.

**Verdict:** STRONG SIGNAL — not in current formula.
**Recommendation:** Add to scoring. Entry 0-7 UTC = +8, entry 8-11 = 0, entry 12-19 = -5, entry 20-23 = -8.

---

## 4. BOX AGE (hours since prior day close)

**V1 Live: W avg = 15.4h, L avg = 18.6h, Delta = -17%** ⭐⭐

```
<12h        15W/3L  WR= 83%  Net= +$159  ← SWEET SPOT
12-24h      11W/16L WR= 41%  Net= -$388  ← DANGER
24-36h       2W/2L  WR= 50%
48h+         1W/0L  WR=100%
```

**Finding:** Fresh boxes (<12h old) have 83% WR. Stale boxes (12-24h) have 41% WR. The box weakens as the day progresses — by afternoon, the levels have been tested and are losing edge.

**Verdict:** STRONG SIGNAL — not in current formula.
**Recommendation:** Add to scoring. Box age <12h = +8, 12-24h = -8, 24h+ = -5.

---

## 5. VOLUME RATIO (recent 5 bars / older 15 bars range)

**V1 Live: W avg = 1.04, L avg = 1.53, Delta = -32%** ⭐⭐⭐

```
<0.7         4W/2L  WR= 67%
0.7-0.9      7W/8L  WR= 47%  Net= -$118
0.9-1.1      9W/2L  WR= 82%  Net=  +$59  ← SWEET SPOT
1.1-1.5      6W/5L  WR= 55%  Net= -$161
1.5+         3W/4L  WR= 43%  Net=  -$28  ← DANGER
```

**Finding:** Winners enter in CALM markets (vol ratio 0.9-1.1 = 82% WR). Losers enter during volatility expansion (1.5+ = 43% WR). Chasing volatility = losing.

**Verdict:** STRONG SIGNAL — not in current formula.
**Recommendation:** Add to scoring. Vol ratio 0.9-1.1 = +5, vol ratio > 1.5 = -10.

---

## 6. DURATION (minutes)

**V1 Live: W avg = 174 min, L avg = 541 min, Delta = -68%** ⭐⭐⭐

```
<15m         2W/2L  WR= 50%  Net=  -$59
15-60m       3W/2L  WR= 60%  Net=  -$49
1-3h        12W/7L  WR= 63%  Net=  -$51
3-6h         6W/2L  WR= 75%  Net=  +$73  ← SWEET SPOT
6h+          6W/8L  WR= 43%  Net= -$115  ← DANGER
```

**Finding:** 3-6 hour holds are the sweet spot (75% WR). Trades held 6h+ bleed (-$115, 43% WR). This is an EXIT signal, not an entry filter — but confirms the time stop logic.

**Verdict:** STRONG SIGNAL — already partially covered by time stop (6h harvester stagnant timeout).
**Recommendation:** Tighten stagnant timeout. 6h+ = forced evaluation, not just "if profitable by 2 pips."

---

## 7. DIRECTIONAL CANDLES (sucker move strength)

**V1 Live: W avg = 1.79, L avg = 1.19, Delta = +51%** ⭐⭐⭐
**V2 Practice: W avg = 1.04, L avg = 0.54, Delta = +92%** ⭐⭐⭐

```
0 candles    9W/9L  WR= 50%  Net= -$176  ← NO CONVICTION
1 candle     7W/6L  WR= 54%  Net=  +$20
2 candles    4W/2L  WR= 67%  Net=  +$20
3 candles    4W/3L  WR= 57%  Net= -$130
4+ candles   5W/1L  WR= 83%  Net=  +$64  ← STRONG
```

**Finding:** 4+ directional candles = 83% WR on V1 live (100% on V2 practice). Zero candles = 50% WR = coin flip. Confirmed across both accounts.

**Verdict:** STRONG SIGNAL — in current formula (±15 AGG).
**Recommendation:** Keep. Consider raising 4+ bonus to +20 given consistency across both datasets.

---

## 8. MOMENTUM CANDLES (consecutive same-direction before signal)

**V1 Live: W avg = 1.62, L avg = 1.10, Delta = +48%** ⭐⭐

```
0 candles   10W/10L WR= 50%  Net= -$127  ← NO MOMENTUM
1 candle     6W/6L  WR= 50%  Net= -$108
2 candles    6W/2L  WR= 75%  Net=  +$26  ← GOOD
3 candles    4W/1L  WR= 80%  Net=   +$9  ← GREAT
4+ candles   3W/2L  WR= 60%
```

**Finding:** Similar to directional count but measures consecutive candles. 2-3 momentum = 77% WR. 0-1 = 50%.

**Verdict:** MODERATE SIGNAL — partially overlaps with directional count.
**Recommendation:** Use directional count as primary. Momentum as secondary tiebreaker if needed.

---

## 9. DOUBLE BB STATE (5M)

**V1 Live:** ⭐⭐

```
NORMAL          23W/14L WR= 62%  Net=  -$63
REJECTION_LONG   3W/1L  WR= 75%  Net=  +$33  ← GOOD
REJECTION_SHORT  2W/1L  WR= 67%  Net=  -$26
STRETCH_UP       0W/3L  WR=  0%  Net= -$135  ← NEVER TRADE
STRETCH_DOWN     0W/1L  WR=  0%  Net=   -$1  ← AVOID
BREAKOUT_UP      1W/0L  WR=100%
BREAKOUT_DOWN    0W/1L  WR=  0%  Net=  -$14
```

**Finding:** STRETCH_UP = 0% WR (-$135). NEVER enter on STRETCH_UP. REJECTION states = 70% WR. NORMAL = 62% WR (most trades). EXTREME states didn't appear in this sample (too rare).

**Verdict:** STRONG SIGNAL — BB exhaustion gate already blocks reversals in non-EXTREME/REJECTION states. But STRETCH should be an explicit BLOCK, not just "not EXTREME."
**Recommendation:** Add STRETCH_UP/DOWN penalty = -15 pts. REJECTION bonus = +5 pts.

---

## 10. Z-SCORE (1H)

**V1 Live: W avg = 0.63, L avg = 0.56, Delta = +13%** ⭐

```
<-1.5        0W/2L  WR=  0%  Net=  -$36  ← EXTREME OVERSOLD (short side?)
-1.5 to -0.5  6W/2L  WR= 75%  Net= +$107  ← SWEET SPOT
-0.5 to 0.5   2W/5L  WR= 29%  Net= -$154  ← NEUTRAL TRAP
0.5 to 1.5  15W/7L  WR= 68%  Net=  -$69
>1.5         6W/5L  WR= 55%  Net=  -$50
```

**Finding:** Z-score -0.5 to 0.5 (neutral) = 29% WR (-$154). Confirms the neutral RSI/z-score trap. The -1.5 to -0.5 range = 75% WR — moderate oversold/overbought is the sweet spot.

**Verdict:** MODERATE SIGNAL — already in formula (z-align bonus, z-direction validity check).
**Recommendation:** Keep existing z-score logic. The neutral z-score trap is already covered by the RSI 45-55 filter.

---

## 11. RSI (14-period, 5M)

**V1 Live: W avg = 51.1, L avg = 54.5, Delta = -6%** ⭐

```
<25          3W/1L  WR= 75%  Net=  +$40
25-40        5W/3L  WR= 62%  Net=  +$41  ← GOOD
40-50        5W/5L  WR= 50%  Net=  -$30
50-60        7W/4L  WR= 64%  Net=  -$87
60-75        6W/5L  WR= 55%  Net= -$182  ← BLEEDS
75+          3W/3L  WR= 50%  Net=  +$16
```

**Finding:** RSI <40 = 67% WR (+$81). RSI 60-75 = 55% WR (-$182, biggest bleed bracket). The neutral filter (45-55) works but the real danger zone is 60-75, not 45-55.

**Verdict:** MODERATE SIGNAL — in current formula as 45-55 hard block.
**Recommendation:** Consider widening RSI penalty to include 55-75 range with a softer -5 penalty instead of hard block. Keep 45-55 hard block. Add RSI <35 bonus = +5.

---

## 12. BB POSITION (1H)

**V1 Live: W avg = 0.66, L avg = 0.64, Delta = +3%** ❌

```
<0.15        1W/2L  WR= 33%  Net=  -$33
0.15-0.35    5W/2L  WR= 71%  Net= +$104  ← SWEET SPOT
0.35-0.50    1W/2L  WR= 33%  Net=  -$85
0.50-0.65    3W/3L  WR= 50%  Net=  -$61
0.65-0.85   13W/6L  WR= 68%  Net=  -$44
0.85+        6W/6L  WR= 50%  Net=  -$84
```

**Finding:** 0.15-0.35 band = 71% WR (+$104). 0.35-0.50 = 33% WR. But overall averages are nearly identical (0.66 vs 0.64). The distribution has pockets but no clean threshold.

**Verdict:** WEAK SIGNAL — BB position averages don't differentiate. The 0.4-0.6 middle penalty from V2 data may be overfitting.
**Recommendation:** Keep bb_middle penalty but REDUCE from -20 to -10. The signal is noisy.

---

## 13. NATURAL STOP (pips)

**V1 Live: W avg = 9.5p, L avg = 7.0p, Delta = +35%** ⭐⭐

```
<=0 INVALID  3W/4L  WR= 43%  Net= -$134  ← HARD BLOCK
1-3p         6W/5L  WR= 55%  Net=  -$86
4-6p        14W/6L  WR= 70%  Net=  +$93  ← SWEET SPOT
7-11p        4W/4L  WR= 50%  Net=  -$47
12p+         2W/2L  WR= 50%  Net=  -$27
```

**Finding:** 4-6 pip natural stops have 70% WR (+$93). Stops <=0 (invalid — candle consumed) have 43% WR (-$134). This should be a hard block.

**Verdict:** STRONG SIGNAL — partially in formula (tight_stop bonus).
**Recommendation:** HARD BLOCK on natural stop <= 0 (candle already consumed). Keep 4-6p as sweet spot (+5). Stops > 12p = -5.

---

## 14. SPREAD (raw pips)

**V1 Live: W avg = 6.8p, L avg = 9.7p, Delta = -30%** ⭐⭐

```
<1.5p        7W/3L  WR= 70%  Net=  +$13
1.5-3p      16W/12L WR= 57%  Net= -$166
3-5p         4W/2L  WR= 67%  Net=   -$6
10p+         2W/4L  WR= 33%  Net=  -$42  ← DANGER
```

**Finding:** Wide spreads (10p+) = 33% WR. Tight spreads (<1.5p) = 70% WR. Mostly driven by USD_MXN having 50p+ spreads.

**Verdict:** MODERATE SIGNAL — already in formula as spread_pct_half gate (10% threshold).
**Recommendation:** Current spread gate is sufficient. The raw pip difference is mostly pair-dependent (MXN inflates it).

---

## 15. OTR (round-trip spread / half box %)

**V1 Live: W avg = 14.8%, L avg = 18.1%, Delta = -18%** ⭐

```
<8%          1W/5L  WR= 17%  Net=  -$98  ← SURPRISING: low OTR loses!
8-12%       15W/7L  WR= 68%  Net= -$130
12-18%       7W/6L  WR= 54%  Net=  -$17
18-25%       2W/1L  WR= 67%  Net=  +$32
25%+         4W/2L  WR= 67%  Net=  +$11
```

**Finding:** COUNTERINTUITIVE — low OTR (<8%) has 17% WR. The "cheapest" trades lose the most. This may be because very tight spreads relative to range means the box is HUGE (wide, unfocused structure).

**Verdict:** WEAK SIGNAL — OTR doesn't cleanly separate W from L. The distribution is U-shaped, not linear.
**Recommendation:** REMOVE OTR from scoring (confirmed again). It actively misleads.

---

## 16. ATR (pips)

**V1 Live: W avg = 241p, L avg = 373p, Delta = -35%** ⭐⭐

```
<50p         2W/1L  WR= 67%  Net=  +$31
50-80p      10W/7L  WR= 59%  Net=  -$55
80-120p     14W/9L  WR= 61%  Net= -$135
120-200p     1W/1L  WR= 50%  Net=  -$13
200p+        2W/3L  WR= 40%  Net=  -$30
```

**Finding:** High ATR (200p+, mostly exotics) = 40% WR. Low-moderate ATR (<80p) = 63% WR. This mostly reflects pair selection (exotics have wide ATR and lose).

**Verdict:** MODERATE SIGNAL — mostly a pair effect, not an independent factor.
**Recommendation:** Don't score ATR directly. Let pair-level performance handle this.

---

## 17. ATR / BOX RATIO

**V1 Live: W avg = 1.38, L avg = 1.31, Delta = +6%** ❌

```
<0.7         0W/1L  WR=  0%
0.7-0.9      8W/4L  WR= 67%  Net=  +$91  ← GOOD (box captures most of ATR)
0.9-1.1      3W/3L  WR= 50%
1.1-1.5      9W/8L  WR= 53%  Net= -$291  ← ATR exceeds box
1.5+         9W/5L  WR= 64%
```

**Finding:** The 0.7-0.9 range (box captures 70-90% of daily range) = 67% WR. When ATR far exceeds the box (1.1-1.5x), the range may be expanding beyond the box structure.

**Verdict:** WEAK SIGNAL — noisy, no clean threshold.
**Recommendation:** Don't add to formula. The box age factor captures the freshness aspect better.

---

## 18. ADR CONSUMED

**V1 Live: W avg = 0.80, L avg = 0.83, Delta = -4%** ❌

```
<40%         2W/1L  WR= 67%
40-60%       6W/5L  WR= 55%
60-80%       9W/3L  WR= 75%  Net=  -$49
80-100%      5W/6L  WR= 45%  Net= -$202  ← DANGER
100%+        7W/6L  WR= 54%  Net=  +$18
```

**Finding:** ADR 80-100% = 45% WR (-$202). The day's range is almost used up. But averages are nearly identical (0.80 vs 0.83). The 60-80% range is interesting (75% WR) — move is underway but not exhausted.

**Verdict:** WEAK SIGNAL — noisy overall. The 80-100% danger zone is real but small.
**Recommendation:** Reduce ADR points from current 0-20 to 0-8 (already done in NEW formula). Don't increase.

---

## 19. BOX SIZE (pips)

**V1 Live: W avg = 209p, L avg = 281p, Delta = -26%** ⭐⭐

```
<40p         3W/2L  WR= 60%
40-70p      11W/7L  WR= 61%  Net=  -$90
70-100p      9W/5L  WR= 64%  Net= -$120
100-200p     4W/4L  WR= 50%  Net=  +$28
200p+        2W/3L  WR= 40%  Net=  -$30
```

**Finding:** Smaller boxes (<100p) have 62% WR. Large boxes (200p+) have 40% WR. Partly pair effect (MXN boxes are 1500p+).

**Verdict:** MODERATE SIGNAL — mostly pair-driven.
**Recommendation:** Already in AGG formula as box size penalty (-5/-10 for >100p/150p). Keep.

---

## 20. WALL PROXIMITY (0=at wall, 1=far)

**V1 Live: W avg = 0.39, L avg = 0.39, Delta = -1%** ❌

```
<0.15        6W/4L  WR= 60%  Net=  +$88
0.15-0.30    2W/5L  WR= 29%  Net= -$110  ← DANGER ZONE??
0.30-0.50    4W/1L  WR= 80%  Net=  +$53
0.50-0.70   14W/9L  WR= 61%  Net= -$193
0.70+        2W/1L  WR= 67%
```

**Finding:** AVERAGES ARE IDENTICAL (0.39 vs 0.39). The distribution is messy — 0.15-0.30 has 29% WR but 0.30-0.50 has 80% WR. This is noisy and unreliable.

**Verdict:** NO SIGNAL on V1 live data. The V2 data showed -70% delta but V1 doesn't confirm.
**Recommendation:** REDUCE wall proximity points from ±15 to ±8. The signal doesn't hold across both datasets.

---

## 21. WICK RATIO

**V1 Live: W avg = 1.31, L avg = 2.23, Delta = -41%** ⭐⭐

```
<0.3        15W/8L  WR= 65%  Net= -$123
0.3-0.7      7W/5L  WR= 58%  Net=  -$12
0.7-1.2      2W/2L  WR= 50%  Net=  -$46
1.2-2.0      1W/3L  WR= 25%  Net=  -$53  ← DANGER
2.0+         4W/3L  WR= 57%  Net=  +$33
```

**Finding:** REVERSED from V2 data. V1 live shows LOWER wick ratios win more (65% at <0.3). The 1.2-2.0 range is 25% WR. But very high wicks (2.0+) recover. This is inconsistent between V1 and V2.

**Verdict:** INCONSISTENT — V1 says low wick wins, V2 said high wick wins. Cannot rely on this.
**Recommendation:** DON'T add wick ratio to scoring. The signal flips between datasets. Unreliable.

---

## 22. BODY % OF CANDLE RANGE

**V1 Live: W avg = 0.50, L avg = 0.51, Delta = -3%** ❌

```
<25%         6W/2L  WR= 75%  Net=  +$53  ← small body = indecision candle
25-40%       5W/4L  WR= 56%
40-55%       5W/4L  WR= 56%
55-70%       5W/7L  WR= 42%  Net= -$174  ← big body = momentum, NOT reversal
70%+         8W/4L  WR= 67%
```

**Finding:** Body <25% (doji/indecision candles) = 75% WR. Body 55-70% (momentum candles) = 42% WR. But averages are identical.

**Verdict:** WEAK SIGNAL — distribution has pockets but averages don't separate.
**Recommendation:** Don't add to formula. Too noisy.

---

## 23. PDH/PDL TOUCHES (24h hourly)

**V1 Live: W avg = 10.3, L avg = 10.7, Delta = -4%** ❌

```
0-2          2W/1L  WR= 67%
3-5          4W/3L  WR= 57%
6-9          8W/5L  WR= 62%
10-14        8W/5L  WR= 62%
15+          7W/7L  WR= 50%  Net= -$123
```

**Finding:** High touch count (15+) = 50% WR (-$123). Moderate touches (6-14) = 62% WR. The "more touches = weaker level" theory is weakly supported.

**Verdict:** WEAK SIGNAL — slight degradation at 15+ touches but not dramatic.
**Recommendation:** Don't add to scoring formula. The existing structure score (touch count from zone tier) handles this.

---

## 24. SPREAD / NATURAL SL RATIO

**V1 Live: W avg = 154%, L avg = 229%, Delta = -33%** ⭐⭐

```
<20%         0W/0L  (no trades)
20-40%      11W/7L  WR= 61%  Net=  -$73
40-60%       7W/5L  WR= 58%  Net=  +$50
60-100%      5W/3L  WR= 62%  Net=  -$68
100%+        6W/6L  WR= 50%  Net= -$110  ← spread exceeds stop
```

**Finding:** When spread exceeds the natural stop (100%+), WR drops to 50% and nets -$110. Spread eating more of the stop = worse outcomes.

**Verdict:** MODERATE SIGNAL — partially captured by spread gate.
**Recommendation:** Add hard block when spread > natural stop (100%+ ratio). If spread is bigger than your stop, the trade is mechanically broken.

---

## 25. GAP DETECTION

**V1 Live:**

```
NONE        29W/21L WR= 58%  Net= -$202
```

**Finding:** No gap trades in this sample. Cannot evaluate.

**Verdict:** INSUFFICIENT DATA.
**Recommendation:** Keep gap logic but can't calibrate from this data.

---

## 26. COUNTER-TREND

**V1 Live:**

```
False       26W/20L WR= 57%  Net= -$268
True         3W/1L  WR= 75%  Net=  +$66
```

**Finding:** Counter-trend trades actually WON more (75%) but tiny sample (4 trades). This contradicts the V2 finding (CT was neutral). Too few CT trades to draw conclusions.

**Verdict:** INSUFFICIENT DATA on V1 live for CT. Keep existing CT penalties from April audit (larger dataset).
**Recommendation:** Keep CT penalties as-is. Don't change based on 4 trades.

---

## 27. PRIOR DAY BULLISH

**V1 Live:**

```
False        5W/5L  WR= 50%  Net= -$105
True        24W/16L WR= 60%  Net=  -$96
```

**Finding:** Prior bullish day → 60% WR. Prior bearish → 50% WR. Moderate signal.

**Verdict:** WEAK SIGNAL.
**Recommendation:** Don't add to formula. Not strong enough to justify complexity.

---

## 28. EMA20 DISTANCE (% of box)

**V1 Live: W avg = 25.2%, L avg = 19.2%, Delta = +31%** ⭐⭐

```
<15%         9W/10L WR= 47%  Net= -$159  ← TOO CLOSE to EMA
15-30%      11W/5L  WR= 69%  Net=  -$59  ← SWEET SPOT
30-50%       7W/6L  WR= 54%  Net=  -$15
50-80%       1W/0L  WR=100%
80%+         1W/0L  WR=100%
```

**Finding:** Too close to EMA20 (<15% of box) = 47% WR. 15-30% distance = 69% WR. This is the pullback distance — too close means no room for the pullback to develop.

**Verdict:** MODERATE SIGNAL — not in current formula.
**Recommendation:** Add modest penalty for EMA20 distance <15% = -5. Being right on the EMA with no room = bad.

---

## 29. EMA50 DISTANCE (% of box)

**V1 Live: W avg = 60.5%, L avg = 51.1%, Delta = +18%** ⭐

```
<20%         1W/4L  WR= 20%  Net=  -$86  ← TOO CLOSE to EMA50
20-40%       8W/4L  WR= 67%  Net= -$106
40-60%       3W/3L  WR= 50%
60-100%     15W/10L WR= 60%
100%+        2W/0L  WR=100%
```

**Finding:** EMA50 distance <20% of box = 20% WR (-$86). Being right on top of the 50-period EMA is dangerous. Price often reacts to EMA50 as support/resistance — entering right there means your entry IS the battle zone.

**Verdict:** MODERATE SIGNAL — not in current formula.
**Recommendation:** Add penalty for EMA50 distance <20% = -8. This is a strong danger signal (20% WR).

---

## 30. INSIDE BOX

**V1 Live:**

```
True        28W/20L WR= 58%
False        1W/1L  WR= 50%
```

**Finding:** Almost all trades are inside the box. Not a differentiator in practice.

**Verdict:** NO SIGNAL.
**Recommendation:** Keep as gate (don't trade outside box) but don't score.

---

## 31. RANGING (EMA slope < 0.02%)

**V1 Live:**

```
False       26W/19L WR= 58%  Net= -$214
True         3W/2L  WR= 60%  Net=  +$12
```

**Finding:** Only 5 trades classified as ranging in V1. Sample too small. The -20 penalty is based on the April audit (225 V1 trades with PF 0.33).

**Verdict:** ALREADY VALIDATED on larger dataset.
**Recommendation:** Keep -20 penalty. This sample is too small to change it.

---

## SIGNAL TYPE (wick_rejection / engulfing / standard)

**V1 Live:**

```
engulfing       3W/1L  WR= 75%  Net=  +$41
standard       22W/15L WR= 59%  Net= -$204
wick_rejection   4W/5L  WR= 44%  Net=  -$39
```

**Finding:** Engulfing = 75% WR. Wick rejection = 44% WR on V1 live. This REVERSES the V2 finding (JW profitable, PoT bleeds). Small sample warning.

**Verdict:** INCONSISTENT between V1 and V2 datasets. Signal type alone is unreliable.
**Recommendation:** Keep existing JW/PoT scoring from April audit (larger dataset). Don't change based on 8 trades.

---

## SUMMARY: What to Add to the Scoring Formula

### ADD (strong, consistent signal):
| Factor | Points | Evidence |
|--------|--------|----------|
| **Entry hour** | 0-7 UTC = +8, 12-23 UTC = -5 to -8 | 82% vs 42% WR, V1 live |
| **Box age** | <12h = +8, 12-24h = -8 | 83% vs 41% WR, V1 live |
| **Volume ratio** | 0.9-1.1 = +5, >1.5 = -10 | 82% vs 43% WR, V1 live |
| **SMA20 distance** | Below SMA = +5, Above 5-20p = -10 | 60% vs 44% WR, V1 live |
| **Natural stop <=0** | HARD BLOCK | 43% WR (-$134), invalid candle |
| **Spread > nat stop** | HARD BLOCK | 50% WR (-$110), mechanically broken |
| **BB STRETCH state** | -15 penalty | 0% WR (-$135) on STRETCH_UP |
| **EMA50 <20% of box** | -8 penalty | 20% WR (-$86), V1 live |

### KEEP AS-IS (confirmed):
| Factor | Current | Evidence |
|--------|---------|----------|
| Directional conviction | ±15 | 83%/50% WR, both datasets |
| Ranging penalty | -20 | Confirmed April audit + V1 live slope data |
| RSI neutral | -15 (45-55 block) | 29% WR on z-score neutral, V1 live |
| CT tier penalties | -10/+5 | Confirmed April audit |
| z-align bonus | +5 | Confirmed both datasets |

### REDUCE (weaker than expected):
| Factor | Current → Proposed | Evidence |
|--------|-------------------|----------|
| Wall proximity | ±15 → ±8 | W=0.39, L=0.39 on V1 live (NO signal) |
| BB middle penalty | -20 → -10 | BB position barely differs between W and L |
| ATR consumed | 0-8 → 0-4 | W=0.80, L=0.83, -4% delta |

### REMOVE (no signal):
| Factor | Current | Evidence |
|--------|---------|----------|
| OTR scoring | 0-15 pts | <8% OTR = 17% WR! Actively misleading |
| Wick ratio scoring | Not scored | Flips between V1 and V2 datasets |
