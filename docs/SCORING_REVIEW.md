# Scoring System Review — Recipe vs Current Points

> Current scoring analyzed against 50-trade raw OANDA recipe data.
> Each component rated: KEEP, ADJUST, REMOVE, or NEW based on evidence.

---

## Current Scoring Breakdown

### Layer 2: Base Scoring (always applied)

| Component | Current Points | Recipe Evidence | Verdict |
|-----------|---------------|-----------------|---------|
| **Zone tier** (T1=30, T2=20, T3=12, T4=6) | 6-30 pts | Winners at correct wall 65% vs 42%. Tier matters. | **KEEP** but distance-to-wall matters more than tier number |
| **ATR consumed** (35-75%=20, edges=12, >90%=4) | 0-20 pts | ADR consumed: W=0.82 vs L=0.76. NOT a differentiator (+8%). | **REDUCE** — ADR barely differs between W and L. Drop to 0-10 range |
| **OTR** (≥2.0=15, ≥1.5=10, ≥1.2=5) | 0-15 pts | OTR: W=14% vs L=14%. IDENTICAL. Zero signal. | **REMOVE** — OTR doesn't separate W from L at all. Dead weight. |
| **R:R (TP1)** (≥2.0=15, ≥1.5=10, ≥1.0=5) | 0-15 pts | R:R same for both. Natural stop: W=15p vs L=24p (tighter wins). | **RETHINK** — reward/risk ratio is the same. Tighter STOP is the signal, not higher R:R. |
| **Pattern type** (JW=15+conf, PoT=5+conf, std=5+conf) | 5-20 pts | Wick ratio: W=2.19 vs L=2.16. NO DIFFERENCE. | **ADJUST** — wick quality doesn't predict. BUT JW vs PoT profitability difference is real (from April audit). Keep signal type differentiation, remove confidence bonus. |

**Layer 2 total range: 11-100 pts**
**Problem:** 50 pts of potential scoring (OTR + R:R + ATR) are based on metrics that DON'T separate winners from losers.

### Layer 3: Contextual Modifiers

| Component | Current Points | Recipe Evidence | Verdict |
|-----------|---------------|-----------------|---------|
| **z-score edge** (≥2.0=10, ≥1.5=6, ≥1.0=3) | 0-10 pts | z-score already used in Layer 1 validity. Moderate value in scoring. | **KEEP** — z-align bonus (r=0.38) already captures this |
| **BB edge** (extreme≥0.85=8, ≥0.70=4) | 0-8 pts | BB extreme: W=19% vs L=21%. NOT a strong signal alone. | **REDUCE** — BB extreme occurrence is similar for both. Drop to 0-4 |
| **Structure (touch count)** (≥10=8, ≥6=4) | 0-8 pts | Not directly in recipe data (different metric). | **KEEP** for now — structural validation has theoretical basis |
| **Gap aligned** | 0 or 6 pts | Not enough gap trades in sample to evaluate. | **KEEP** |
| **Ranging penalty** | -20 pts | EMA slope: W=0.10% vs L=0.04%. Confirms ranging is bad. | **KEEP** — ranging is confirmed #1 killer |
| **CT + PoT** | -15 pts | PoT bleeds. Confirmed. | **KEEP** |
| **CT + JW** | -5 pts | JW near breakeven on CT. Confirmed. | **KEEP** |
| **CT Tier 1** | -10 pts | Confirmed worst CT category. | **KEEP** |
| **CT Tier 2** | +5 pts | Confirmed profitable CT. | **KEEP** |
| **z-align bonus** | +5 pts | z-score alignment r=0.38. Moderate signal. | **KEEP** |
| **BB middle penalty** (NEW) | -15 pts | BB 0.4-0.6 = 27% WR. STRONG signal. | **KEEP** — just added |
| **Conviction bonus** (NEW) | ±10 pts | 4+ candles = 100% WR. STRONGEST signal. | **KEEP** — just added, might need to be LARGER |

---

## What the Recipe Says Should Be Weighted Heavily

### Top 5 differentiators (by delta between W and L):

| Rank | Factor | W vs L Delta | Current Weight | Should Be |
|------|--------|-------------|----------------|-----------|
| 1 | **Distance to target wall** | -70% (W=80p, L=262p) | Not scored! (only zone gate) | **+15 to -15 based on proximity** |
| 2 | **Directional candles** | +92% (W=1.04, L=0.54) | ±10 pts (just added) | **Should be ±15 or more** |
| 3 | **Natural stop tightness** | -40% (W=15p, L=24p) | Not scored! (SL floor overrides) | **+5 for tight natural stops** |
| 4 | **At correct wall** | +24% (W=65%, L=42%) | Zone tier (30/20/12/6) | **Partially captured but not the right metric** |
| 5 | **EMA slope (trend clarity)** | +184% (W=0.10, L=0.04) | -20 ranging | **Good — already strongest penalty** |

### Factors that DON'T matter but get big points:

| Factor | Current Weight | W vs L Delta | Action |
|--------|---------------|-------------|--------|
| OTR | 0-15 pts | 0% (identical) | **Remove from scoring** |
| R:R ratio | 0-15 pts | ~0% (same for both) | **Reduce to 0-5 or remove** |
| ATR consumed | 0-20 pts | +8% (trivial) | **Reduce to 0-8** |
| Wick ratio | Part of pattern score | +1% (nothing) | **Don't score wick quality** |
| BB extreme | 0-8 pts | -2% (nothing) | **Reduce to 0-4** |

---

## Proposed Revised Scoring

### Layer 2 (Base): Focus on what MATTERS

```
Zone tier:          T1=25, T2=15, T3=8, T4=4     (was 30/20/12/6 — compressed)
Wall proximity:     NEW — within 20% of correct wall = +15
                    NEW — in middle 40-60% = 0
                    NEW — at wrong wall = -10
ATR consumed:       35-75% = 8, edges = 4          (was 20/12 — halved)
RR (TP1):           >= 2.0 = 5, >= 1.0 = 3        (was 15/10/5 — sharply reduced)
Pattern type:       JW = 15, PoT = 5, std = 8     (keep — confirmed difference)
Confidence:         HIGH = 3, MODERATE = 0          (was 5/3 — reduced)
```

### Layer 3 (Modifiers): Amplify real signals

```
Directional conviction:  4+ candles = +15          (was +10 — increased, 100% WR)
                         2-3 candles = +5
                         0-1 candles = -15          (was -10 — increased, 48% WR)
BB middle penalty:       0.4-0.6 = -20             (was -15 — increased, 27% WR)
RSI neutral filter:      45-55 = BLOCK (Layer 1)   (keep as hard block)
Ranging:                 -20                        (keep)
z-score edge:            keep as-is (0-10)
z-align bonus:           keep (+5)
CT combos:               keep as-is
Structure:               keep as-is (0-8)
Gap:                     keep (+6)
```

### REMOVE from scoring:
```
OTR scoring:             REMOVE (0% signal)
```

---

## Impact Estimate

Current system: ~50 pts come from metrics that don't predict outcomes (OTR 15 + RR 15 + ATR 20).
Proposed system: those 50 pts redistributed to conviction (+15), wall proximity (+15), and tighter penalties for the middle (-20).

The scoring system should be dominated by:
1. Where you are in the box (wall proximity + BB position)
2. How much conviction exists (directional candles + RSI)
3. Whether the market is hostile (ranging + regime + CT combos)

NOT by:
- How much of the ATR has been consumed
- What the overhead ratio is
- What the R:R ratio says

---

## Sample Size Warning

This is based on 50 V2 practice trades. The April 9 audit had 511 V1 + 58 V2 trades and some findings may override these on larger samples. The conviction finding (100% WR on 4 trades) is the most fragile. The BB middle (27% on 11 trades) needs more data. The OTR finding (identical for W and L) is robust across the full sample.
