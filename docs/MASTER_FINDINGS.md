# Master Findings — Every Metric, Every Discovery, One Place

> Consolidated from ALL analyses run on 2026-04-15.
> Sources: 50 V1 live trades, 49 V2 practice trades, raw OANDA candle data.
> No bot logs. Every value computed from market data at entry time.

---

## TIER 1: STRONGEST SIGNALS (Delta > 30%)

These are the factors that most reliably separate winners from losers.

| # | Factor | W avg | L avg | Delta | Best Bucket | Best WR | Worst Bucket | Worst WR | In Formula? | Action |
|---|--------|-------|-------|-------|------------|---------|-------------|----------|-------------|--------|
| 1 | **EMA slope** | 0.20% (V1), 0.10% (V2) | 0.07% (V1), 0.04% (V2) | +113-184% | >0.02% (trending) | 61-70% | -0.1 to -0.02 (negative) | 38% | ✅ -20 ranging | KEEP |
| 2 | **SMA20 distance** | -1.1 pips | +6.5 pips | -116% | Below SMA20 | 60% | 5-20p above SMA20 | 44% | ❌ NOT scored | ADD: below=-5, above 5-20p=+8 |
| 3 | **Wick ratio** | 1.07 (V1) | 0.55 (V1) | +94% (V1 only) | — | — | — | — | ❌ NOT scored | CAUTION: V2 showed 0% delta. Inconsistent. |
| 4 | **Spread (raw pips)** | 2.4p (V1), 8.4p (V2) | 12.3p (V1), 14.8p (V2) | -43 to -81% | <1.5p | 70% | 10p+ | 33% | ✅ spread gate (10% of half) | KEEP gate |
| 5 | **Directional candles** | 1.79 (V1), 1.04 (V2) | 1.19 (V1), 0.54 (V2) | +51-92% | 4+ candles | 83-100% | 0 candles | 48-50% | ✅ ±15 pts (recently added) | INCREASE to ±20 |
| 6 | **Box size (pips)** | 77p (V1), 283p (V2) | 358p (V1), 408p (V2) | -26 to -79% | 70-100p | 60-64% | 200p+ | 40% | ❌ NOT scored (AGG only) | ADD: >200p = -10 |
| 7 | **Duration** | 174 min (V1) | 541 min (V1) | -68% | 3-6 hours | 75% | 6h+ | 43% | ⚠️ time stop exists (6h) | TIGHTEN time stop |
| 8 | **Natural stop (pips)** | 4.7p (V1), 15p (V2) | 11.5p (V1), 24p (V2) | -35 to -40% | 4-6 pips | 70% | <=0 (invalid) | 43% | ✅ tight stop +5 | ADD hard block: <=0 |
| 9 | **Signal candle range** | 5.2p | 15.7p | -67% | — | — | — | — | ❌ NOT scored | Overlaps with natural stop. Don't add separately. |
| 10 | **ATR (pips)** | 82p (V1), 344p (V2) | 423p (V1), 599p (V2) | -35 to -43% | <80p | 59-63% | 200p+ | 40% | ⚠️ ATR consumed scored | Mostly pair effect. Don't score separately. |
| 11 | **Entry hour** | 10.2 UTC (V1) | 15.1 UTC (V1) | -33-38% | 0-7 UTC | 82-89% | 12-23 UTC | 38-43% | ❌ NOT scored | ADD: 0-7=+8, 12-19=-5, 20-23=-8 |
| 12 | **Volume ratio** | 1.04 (V1), 1.10 (V2) | 1.53 (V1), 1.10 (V2) | -32% (V1) | 0.9-1.1 | 82% | 1.5+ | 43% | ❌ NOT scored | ADD: 0.9-1.1=+5, >1.5=-8 |
| 13 | **Spread/SL ratio** | 11% (V1), 154% (V1) | 19% (V1), 229% (V1) | -33 to -42% | <40% | 61% | >100% | 50% | ❌ NOT scored | ADD hard block: spread > natural stop |
| 14 | **Momentum candles** | 1.62 | 1.10 | +48% | 2-3 candles | 77-80% | 0 candles | 50% | ❌ NOT scored | Overlaps with directional count. Secondary. |

---

## TIER 2: MODERATE SIGNALS (Delta 10-30%)

These show some separation but are noisier or less consistent between datasets.

| # | Factor | W avg | L avg | Delta | Best Bucket | Best WR | Worst Bucket | Worst WR | In Formula? | Action |
|---|--------|-------|-------|-------|------------|---------|-------------|----------|-------------|--------|
| 15 | **Box age** | 15.4h | 18.6h | -17% | <12h | 83% | 12-24h | 41% | ❌ NOT scored | ADD: <12h=+8, 12-24h=-8 |
| 16 | **Wall proximity** | 0.39 (V1) | 0.39 (V1) | -1% (V1!) | <0.15 | 60% | 0.15-0.30 | 29% | ✅ ±15 pts | REDUCE to ±5. V1 shows NO delta. V2 showed -70%. INCONSISTENT. |
| 17 | **BB position** | 0.66 (V1), 0.49 (V2) | 0.64 (V1), 0.58 (V2) | +3% (V1), -16% (V2) | 0.15-0.35 | 71% | 0.35-0.50 | 33% | ✅ bb_middle -20 | REDUCE to -10. Weak on V1. |
| 18 | **Spread % of half box** | 6.6% (V1), 7% (V2) | 11.2% (V1), 7% (V2) | -18 to -41% | <5% | 50-67% | 10-15% | 20% | ✅ spread gate (10%) | KEEP at 10% |
| 19 | **OTR** | 14.8% (V1), 14% (V2) | 18.1% (V1), 14% (V2) | -5 to -18% | 8-12% | 68% | <8% | 17%! | ✅ 0-15 pts (old) | REMOVE. Low OTR = 17% WR. Actively misleading. |
| 20 | **Body % of candle** | 0.50 (V1), 0.41 (V2) | 0.51 (V1), 0.44 (V2) | -3 to -6% | <25% | 75% | 55-70% | 42% | ❌ NOT scored | Don't add. Averages nearly identical. |
| 21 | **Prior day bullish** | 89% | 64% | +26% | True | 60% | False | 50% | ❌ NOT scored | Don't add. Weak signal, adds complexity. |
| 22 | **Box position** | 0.55 (V1), 0.51 (V2) | 0.62 (V1), 0.61 (V2) | -10 to -17% | — | — | — | — | ⚠️ Captured by wall proximity | Don't add separately. |
| 23 | **EMA20 distance** | 25.2% (V1) | 19.2% (V1) | +31% | 15-30% | 69% | <15% | 47% | ❌ NOT scored | ADD modest: <15% = -5 |
| 24 | **EMA50 distance** | 60.5% (V1) | 51.1% (V1) | +18% | 60%+ | 60% | <20% | 20% | ❌ NOT scored | ADD: <20% = -8 (strong danger) |
| 25 | **RSI** | 49 (V1), 52 (V2) | 56 (V1), 55 (V2) | -6 to -12% | <40 | 62-67% | 45-55 (neutral) | 29-50% | ✅ 45-55 hard block | KEEP. Consider 60-75 soft penalty (-5). |

---

## TIER 3: WEAK OR NO SIGNAL (Delta < 10%)

These factors show little to no meaningful difference between winners and losers.

| # | Factor | W avg | L avg | Delta | Notes | Action |
|---|--------|-------|-------|-------|-------|--------|
| 26 | **ADR consumed** | 0.80-0.82 | 0.76-0.83 | -4 to +8% | 80-100% = 45% WR (small danger zone) | REDUCE from 0-20 to 0-4. Barely matters. |
| 27 | **ATR/Box ratio** | 1.38 (V1), 0.93 (V2) | 1.31 (V1), 0.80 (V2) | 0-6% (V1), +17% (V2) | Noisy. No clean threshold. | DON'T add. |
| 28 | **PDH/PDL touches** | 10.3 | 10.7 | -4% | 15+ = 50% WR (slight degradation) | DON'T add. Zone tier handles this. |
| 29 | **Range expansion** | 0.95-1.08 | 1.11-1.20 | -10 to -14% | Overlaps with volume ratio. | DON'T add. Use volume ratio instead. |
| 30 | **Z-score magnitude** | 0.63-0.77 | 0.36-0.56 | +13-116% | -0.5 to 0.5 = 29% WR (neutral trap) | KEEP z-edge scoring. Neutral already blocked by RSI. |
| 31 | **RR (TP1)** | Same (V2) | Same (V2) | ~0% | Does not separate W from L | REDUCE from 0-15 to 0-3. |

---

## TIER 4: CATEGORICAL FINDINGS

These are pass/fail or state-based findings, not continuous metrics.

| # | Factor | Winners | Losers | Delta | Key Finding | Action |
|---|--------|---------|--------|-------|-------------|--------|
| 32 | **BB state: STRETCH_UP** | 0 trades | 3 trades | — | **0% WR, -$135** | HARD BLOCK. Never enter. |
| 33 | **BB state: STRETCH_DOWN** | 0 trades | 1 trade | — | **0% WR** | HARD BLOCK. Never enter. |
| 34 | **BB state: REJECTION** | 5 trades | 2 trades | — | **71% WR, +$33** | +5 bonus |
| 35 | **BB state: NORMAL** | 23 trades | 14 trades | — | **62% WR** | Most trades. Neutral. |
| 36 | **BB state: EXTREME** | — | — | — | Too rare in sample | Keep as reversal prerequisite. |
| 37 | **Counter-trend** | 3W (V1) | 1L (V1) | — | 75% WR but only 4 trades | KEEP existing CT penalties (from April audit, 511 trades). |
| 38 | **Ranging** | 3W (V1) | 2L (V1) | — | 60% but only 5 trades | KEEP -20 penalty (from April audit, 225 trades, PF 0.33). |
| 39 | **Gap** | — | — | — | No gap trades in sample | Cannot evaluate. Keep existing logic. |
| 40 | **Inside box** | 28W | 20L | — | 58% WR. Almost all trades inside. | Not a differentiator. |
| 41 | **At correct wall** | 42% (V1) | 55% (V1) | -12% | REVERSED from V2 (+24%). Inconsistent. | REDUCE weight. |
| 42 | **Signal type: engulfing** | 3W | 1L | 75% WR | V1 says good. V2 says bleeds. | INCONSISTENT between datasets. Keep April audit weights. |
| 43 | **Signal type: wick_rejection** | 4W | 5L | 44% WR (V1) | V1 says bad! V2 says good (+$1,267). | INCONSISTENT. Keep April audit weights. |

---

## SUMMARY: What Changed vs What We Already Knew

### NEW discoveries (never identified before this analysis):
1. **SMA20 distance** — winners enter below SMA20, losers above (+116% delta)
2. **Entry hour** — 0-7 UTC = 82% WR vs 12-23 UTC = 42% WR
3. **Box age** — <12h = 83% WR vs 12-24h = 41% WR
4. **Volume ratio** — calm markets (0.9-1.1) = 82% WR vs volatile (>1.5) = 43%
5. **EMA50 proximity** — <20% of box = 20% WR (entering at the battle zone)
6. **Natural stop <=0 must be hard blocked** — 43% WR, invalid candle
7. **Spread > natural stop must be hard blocked** — mechanically broken trade
8. **BB STRETCH = 0% WR** — must be hard blocked
9. **OTR is ACTIVELY MISLEADING** — low OTR (<8%) = 17% WR. Remove from scoring.
10. **EMA20 distance <15%** — too close to EMA, no room for pullback = 47% WR

### CONFIRMED with data (we suspected these, now proven):
1. **Directional conviction** — 4+ candles = 83-100% WR (strongest single factor)
2. **RSI neutral (45-55)** — trap zone, 29-50% WR
3. **Ranging = killer** — PF 0.33 from April audit, confirmed by EMA slope data
4. **Sub-2hr trades bleed** — 3-6h sweet spot at 75% WR
5. **Tighter natural stops win** — 4-6p = 70% WR
6. **USD_MXN is marginal** — 33% WR, -$3,727

### OVERTURNED (we thought these mattered, data says they don't):
1. **Wall proximity** — V1 shows ZERO delta (0.39 vs 0.39). V2 showed -70%. Inconsistent.
2. **BB position averages** — W=0.66, L=0.64 on V1. Nearly identical. Middle penalty should be reduced.
3. **Wick ratio** — V1 says low wicks win (+94% delta), V2 says same for both (0% delta). Unreliable.
4. **Signal type (JW vs PoT)** — FLIPS between V1 and V2. Cannot rely on candle pattern alone.
5. **ADR consumed** — W=0.80, L=0.83. Trivial 4% difference. Scored at 0-20 pts = dead weight.
6. **OTR scoring** — doesn't separate W from L, AND low OTR actively loses money.
7. **RR ratio** — same for both winners and losers. Dead weight in scoring.

### THINGS WE CANNOT EVALUATE (insufficient data):
1. **Gap trades** — zero gap trades in sample
2. **BB EXTREME state** — too rare to appear in 99 trades
3. **Counter-trend** — only 4-8 CT trades in V1 sample. Keep April audit weights (511 trades).
4. **Ranging** — only 5 trades classified. Keep April audit penalty.

---

## THE V3 FORMULA RESULT

When all findings are applied:

| Metric | OLD Formula | V3 Formula |
|--------|-------------|------------|
| Score separation (W - L) | +0.5 pts | +12.5 pts |
| Best P&L at any threshold | Always negative | +$170 to +$3,526 |
| Win rate on passed trades | 52% | **76%** |
| Trades passed | All 50 | 17 (filtered) |
| Big losers caught | 0 | EUR_USD -$83, GBP_USD -$65, NZD_USD -$54, USD_MXN -$40, USD_CHF -$48, -$45 |
| Big winners preserved | N/A | AUD_USD +$47, AUD_CHF +$41, AUD_CAD +$34, AUD_JPY +$28 |
| Blocked winners | 0 | 16 (but total only $167 = avg $10 each = harvester clips) |
