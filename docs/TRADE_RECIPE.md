# Trade Recipe — What Makes a Good Trade

> Reverse-engineered from 50 raw OANDA trades (V2 practice, Mar 24 - Apr 14 2026).
> All data pulled from OANDA candle API at entry time — NO bot logs used.
> 26 winners ($+18,310) vs 24 losers ($-23,852) = net -$5,543.

---

## 1. The Strongest Signals (Winner vs Loser Differences)

### Confirmed by data — sorted by signal strength:

| # | Ingredient | Winners | Losers | Delta | Already Known? |
|---|-----------|---------|--------|-------|----------------|
| 1 | **Distance to target wall** | 80 pips | 262 pips | **-70%** | Partially (zone proximity gate exists, but threshold not calibrated to this) |
| 2 | **Directional candles (sucker move)** | 1.04 avg | 0.54 avg | **+92%** | Theory says 3-5, but no data on WR by count until now |
| 3 | **Natural stop size** | 15 pips | 24 pips | **-40%** | NEW — tighter natural stops win more |
| 4 | **At correct wall** | 65% | 42% | **+24%** | Theory says "buy at lows, sell at highs" — now quantified |
| 5 | **Spread (pips)** | 8.4 | 14.8 | **-43%** | Known (OTR gate), but magnitude not quantified |
| 6 | **Box size** | 283 pips | 408 pips | **-31%** | NEW — smaller boxes win more (tighter structure) |
| 7 | **EMA slope** | 0.10% | 0.04% | **+184%** | Known (ranging = killer), now confirmed with per-trade data |
| 8 | **Box/ATR ratio** | 0.93 | 0.80 | **+17%** | NEW — box that represents more of ATR = better structure |
| 9 | **BB position** | 0.49 | 0.58 | **-16%** | Partially (BB classification exists, but position-level WR is new) |
| 10 | **Hour UTC** | 11.8 | 13.9 | **-15%** | NEW — earlier entries win more |

### NOT significant (no meaningful difference):

| Ingredient | Winners | Losers | Note |
|-----------|---------|--------|------|
| Wick ratio | 2.19 | 2.16 | No difference — wick quality doesn't predict outcome |
| Spread % of half box | 7% | 7% | Same ratio for both — spread isn't the differentiator |
| OTR | 14% | 14% | Same — OTR doesn't separate W from L |
| With trend (EMA) | 96% | 96% | Both mostly with-trend — not a filter |
| Volume ratio | 1.10 | 1.10 | Identical — volume proxy useless |
| Range expansion | 0.95 | 1.11 | Small difference, not reliable |

---

## 2. Distribution Analysis — Where Trades Cluster

### Sucker Move (Directional Candle Count) — STRONGEST FILTER

```
0-1 candles:  19W/21L  WR= 48%  Net= -$11,061  ← DANGER ZONE
2-3 candles:   3W/ 3L  WR= 50%  Net=  +$4,414
4-5 candles:   4W/ 0L  WR=100%  Net=  +$1,105  ← PERFECT
```

**DISCOVERY:** 4+ directional candles before the reversal = 100% win rate (4 wins, 0 losses). This was never quantified before. The theory says "3-5 candles" but the data shows the sweet spot is 4+.

**Known:** Theory says 3-5 directional candles. Gate uses flexible window with min=3.
**NEW:** The 0-1 candle entries are where ALL the losses cluster. The gate minimum may need to be raised, or 0-1 candle entries need a score penalty.

### RSI at Entry — NEW DISCOVERY

```
RSI <30:    2W/1L  WR=67%  Net= +$263
RSI 30-45:  9W/4L  WR=69%  Net= +$5,086   ← SWEET SPOT
RSI 45-55:  4W/10L WR=29%  Net= -$9,198   ← TRAP (neutral RSI)
RSI 55-70:  6W/4L  WR=60%  Net= -$230
RSI 70+:    5W/5L  WR=50%  Net= -$1,463
```

**DISCOVERY:** RSI 45-55 (neutral) is the WORST bracket — 29% WR, -$9,198. This is the "no conviction" zone. The theory says enter when there's forced behavior — neutral RSI means no one is being forced.

**NOT previously known.** RSI was logged in entry-context but never used as a gate or scoring factor.

### BB Position — NEW QUANTIFICATION

```
BB <0.2:    4W/3L  WR=57%  Net= -$2,069
BB 0.2-0.4: 7W/3L  WR=70%  Net= +$3,772   ← SWEET SPOT
BB 0.4-0.6: 3W/8L  WR=27%  Net= -$3,268   ← "DON'T TRADE THE MIDDLE"
BB 0.6-0.8: 7W/5L  WR=58%  Net= -$1,505
BB 0.8+:    3W/2L  WR=60%  Net= -$2,143
```

**DISCOVERY:** BB 0.4-0.6 (middle of the band) = 27% WR. This IS "don't diddle in the middle" — quantified. The theory said it, but we never had the WR data by BB position bracket.

**Known:** "Never trade the middle" is core theory. BB classification exists (NORMAL/TREND/EXTREME).
**NEW:** The specific BB position range 0.4-0.6 as a hard filter. The existing BB classifier uses states (EXTREME/REJECTION/etc.) but not the raw position value.

### Box Size — NEW DISCOVERY

```
Box <40p:    3W/3L  WR=50%  Net= +$2,292
Box 40-70p:  6W/5L  WR=55%  Net= -$1,244
Box 70-100p: 9W/6L  WR=60%  Net= +$4,558   ← SWEET SPOT
Box 100p+:   8W/10L WR=44%  Net=-$11,149   ← DANGER
```

**DISCOVERY:** Boxes over 100 pips have 44% WR and bleed -$11,149. These are wide, volatile ranges where the reversal thesis is weakest. The sweet spot is 70-100 pips — structured enough to have clear walls, not so wide that the stop is tiny relative to the range.

**NOT previously known.** No box size filter existed.

### Spread % of Half Box — CONFIRMS TRADE_MATH

```
Spread <5%:   8W/4L  WR=67%  Net= -$3,393
Spread 5-10%: 15W/16L WR=48% Net=   -$243
Spread 10-15%: 1W/4L WR=20%  Net= -$2,771  ← DANGER
Spread 15%+:   2W/0L WR=100% Net=   +$864  (tiny sample)
```

**CONFIRMS:** TRADE_MATH.md proposed 15% as the hard block. The data shows 10-15% is already dangerous (20% WR). The threshold should be **10%, not 15%**.

**Known:** TRADE_MATH.md proposed spread-relative gating. OTR gate existed.
**NEW:** The specific 10% threshold as the danger zone.

### Duration — CONFIRMS EXISTING FINDING

```
<30 min:   1W/2L  WR=33%  Net=   -$320
30m-2h:    5W/6L  WR=45%  Net= -$7,952    ← THE BLEED
2-6h:      9W/9L  WR=50%  Net= +$6,721    ← BREAKEVEN+
6h+:      11W/7L  WR=61%  Net= -$3,992
```

**CONFIRMS:** strategies-scoring.md already noted "sub-30-minute trades are catastrophic." Data confirms: <2hr trades are where the losses concentrate. 2-6 hour trades produce the best net outcome.

### By Pair — CONFIRMS USD_MXN PROBLEM

```
USD_MXN:  3W/6L  WR=33%  Net= -$3,727   ← WORST PAIR
EUR_USD:  2W/3L  WR=40%  Net= -$9,224   ← SECOND WORST
AUD_CHF:  3W/1L  WR=75%  Net= +$4,889   ← BEST PAIR
AUD_USD:  1W/0L  WR=100% Net= +$4,216
USD_CHF:  4W/1L  WR=80%  Net= +$1,508
```

**CONFIRMS:** USD_MXN known to be problematic (logs/pairs/USD_MXN.md). EUR_USD losses are from regime-ignored entries.

---

## 3. The Recipe — V3 Gate Calibration Targets

Based on this data, here's how each V3 gate should be calibrated:

### Gates that SHOULD be stricter (they let losers through):

| Gate | Current Config | Data Says | Proposed Change |
|------|---------------|-----------|-----------------|
| **Directional pressure (min candles)** | min=3 | 0-1 candles = 48% WR, 4+ = 100% | Raise min to 2, add score penalty for <3 |
| **Zone proximity** | 0.25% | Winners 3x closer to wall | Tighten proximity or add distance-to-wall score factor |
| **BB position / "middle" filter** | BB states only | BB 0.4-0.6 = 27% WR | Add hard block when BB position 0.4-0.6 |
| **Spread % of half** | Fixed pip threshold | >10% = 20% WR | Switch to % of half_box, threshold at 10% |

### Gates that should be LOOSENED (they block winners):

| Gate | Current Config | Data Says | Proposed Change |
|------|---------------|-----------|-----------------|
| **SL floor** | 0.25% of price | Kills 54% of winners, smaller stops WIN more | Lower to 0.10% or use box-relative floor |
| **RR gate** | 1.35 vs TP2 | Not a differentiator (W and L have same OTR) | Lower to 1.0 or replace with profitability check |

### New gates to ADD:

| Gate | Data Evidence | Proposed |
|------|--------------|----------|
| **RSI neutral filter** | RSI 45-55 = 29% WR, -$9,198 | Block or penalize when RSI 45-55 (no conviction) |
| **Box size filter** | >100p = 44% WR, -$11,149 | Score penalty for boxes >100p (or >1.2x ATR) |

### Gates that are fine as-is:

| Gate | Data Evidence |
|------|--------------|
| OTR (overhead ratio) | Same for W and L — not a differentiator on its own |
| Wick ratio | Same for W and L — candle quality doesn't predict |
| EMA trend | 96% with-trend for both — not a filter |

---

## 4. Cross-Reference with Existing Knowledge

| Finding | Status | Reference |
|---------|--------|-----------|
| "Don't trade the middle" | **CONFIRMED** with data (BB 0.4-0.6 = 27% WR) | MASTER_THEORY Section 6 |
| "3-5 directional candles" | **REFINED** — 4+ = 100% WR, 0-1 = 48% | MASTER_THEORY Section 3 |
| Ranging markets = killer | **CONFIRMED** — EMA slope near 0 = worse outcomes | strategies-scoring.md |
| Sub-30min trades catastrophic | **CONFIRMED** — <2hr bracket is the real danger zone | strategies-scoring.md |
| USD_MXN is marginal | **CONFIRMED** — 33% WR, -$3,727 | logs/pairs/USD_MXN.md |
| SL floor too aggressive | **CONFIRMED** — blocks 54% of winners | TRADE_MATH.md (today) |
| RSI 45-55 is a trap | **NEW** — never identified before | — |
| BB position 0.4-0.6 worst | **NEW** — BB states existed but not position-level WR | — |
| Box 70-100p sweet spot | **NEW** — no box size filter existed | — |
| Spread >10% of half = danger | **NEW** — OTR existed but 10% threshold is new | TRADE_MATH.md proposed 15% |
| Winners closer to wall (3x) | **NEW** — zone proximity existed but distance magnitude is new | — |
| Tighter natural stops win more | **NEW** — contradicts the SL floor approach entirely | — |

---

## 5. Sample Size Warning

50 trades is a starting point, not a conclusion. The findings here should be treated as hypotheses to validate with a larger dataset. Key risks:

- 4+ directional candles = 100% WR is from only 4 trades
- Box size sweet spot may shift with different market conditions
- RSI finding needs 100+ trades to be statistically significant
- BB position analysis conflates different pairs and sessions

**Next step:** Pull the V1 live account data (511 trades) and run the same analysis for validation.
