# Scoring Formula V3 — Complete Specification

> Built from Factor Bible analysis of 99 raw OANDA trades (50 V1 live + 49 V2 practice).
> Every weight derived from data. No theory-only weights.

---

## Layer 0: Hard Blocks (score = 0, trade rejected)

These fire BEFORE scoring. If any triggers, trade is dead.

| Block | Condition | Evidence | WR when violated |
|-------|-----------|----------|-----------------|
| **Invalid natural stop** | nat_stop <= 0 pips | Candle consumed, SL on wrong side | 43% WR, -$134 |
| **Spread exceeds stop** | spread > nat_stop | Mechanically broken — spread eats entire risk | 50% WR, -$110 |
| **RSI neutral** | 45 <= RSI <= 55 | No directional conviction | 29% WR (z-score), 50% WR (RSI) |
| **STRETCH BB state** | bb_state in (STRETCH_UP, STRETCH_DOWN) | Extended but not exhausted — trend continuation, not reversal | 0% WR, -$136 |

---

## Layer 1: Base Scoring

| Factor | Buckets | Points | Evidence |
|--------|---------|--------|----------|
| **Zone tier** | T1 | +20 | Confirmed: daily-aligned zones are strongest |
| | T2 | +12 | |
| | T3 | +6 | |
| | T4 | +3 | |
| **Pattern type** | wick_rejection (JW) | +15 | April audit: +$1,267 V2 |
| | engulfing (PoT) | +5 | April audit: -$4,086 V2 |
| | standard | +8 | |
| | HIGH confidence | +3 | |

**Base range: 6-38 points**

---

## Layer 2: Market State Modifiers

| Factor | Condition | Points | Evidence |
|--------|-----------|--------|----------|
| **Entry hour** | 0-7 UTC (Sydney/Tokyo/London open) | +8 | 82% WR, +$156 |
| | 8-11 UTC (London session) | 0 | 50% WR |
| | 12-15 UTC (NY afternoon) | -5 | 43% WR, -$282 |
| | 16-19 UTC (late NY) | -5 | 50% WR, -$85 |
| | 20-23 UTC (evening) | -8 | 38% WR |
| **Box age** | <12 hours | +8 | 83% WR, +$159 |
| | 12-24 hours | -8 | 41% WR, -$388 |
| | 24+ hours | -5 | 50% WR |
| **Volume ratio** | 0.9-1.1 (calm) | +5 | 82% WR, +$59 |
| | 0.7-0.9 or 1.1-1.5 | 0 | |
| | <0.7 or >1.5 (volatile) | -8 | 43-47% WR |
| **Ranging** | EMA slope < 0.02% | -20 | PF 0.33 (April audit, 225 trades) |
| **BB state bonus** | REJECTION_LONG/SHORT | +5 | 70% WR |

**Market state range: -41 to +21 points**

---

## Layer 3: Entry Quality Modifiers

| Factor | Condition | Points | Evidence |
|--------|-----------|--------|----------|
| **Directional conviction** | 4+ candles | +20 | 83-100% WR across both datasets |
| | 3 candles | +8 | 57% WR |
| | 2 candles | +3 | 67% WR |
| | 1 candle | 0 | 54% WR |
| | 0 candles | -15 | 50% WR, -$176 |
| **SMA20 distance** | Entry below SMA20 | +5 | 60% WR, +$72 |
| | Entry within ±5p of SMA20 | 0 | |
| | Entry above SMA20 by 5-20p | -8 | 44% WR, -$195 |
| | Entry above SMA20 by 20p+ | -5 | 50% WR |
| **Natural stop** | 4-6 pips | +5 | 70% WR, +$93 |
| | 1-3 or 7-11 pips | 0 | |
| | 12+ pips | -5 | 50% WR |
| **EMA50 proximity** | Distance <20% of box | -8 | 20% WR, -$86 |
| | Distance 20%+ | 0 | |
| **Wall proximity** | <0.20 (at correct wall) | +5 | 60% WR |
| | 0.20-0.50 (near wall) | 0 | |
| | 0.50+ (middle/wrong wall) | -5 | V2: -70% delta on distance |
| **BB middle** | BB position 0.35-0.50 | -10 | 33% WR, -$85 |

**Entry quality range: -46 to +35 points**

---

## Layer 4: Context Modifiers (from April audit, larger dataset)

| Factor | Condition | Points | Evidence |
|--------|-----------|--------|----------|
| **z-score edge** | abs(z) >= 2.0 | +10 | Strong directional extension |
| | abs(z) >= 1.5 | +6 | |
| | abs(z) >= 1.0 | +3 | |
| **z-align bonus** | Entry direction matches z | +5 | r=0.38 with P&L |
| **CT + engulfing** | Counter-trend + PoT type | -15 | -$4,086 V2 |
| **CT + wick_reject** | Counter-trend + JW type | -5 | Near breakeven |
| **CT Tier 1** | Counter-trend at PDH/PDL | -10 | Worst CT category |
| **CT Tier 2** | Counter-trend at PHH/PHL | +5 | 66-100% WR |
| **ADR consumed** | 35-75% | +4 | Sweet spot |
| | 20-35% or 75-90% | +2 | |
| | Other | 0 | |
| **RR (TP1)** | >= 2.0 | +3 | Weak signal but keeps minimum quality |
| | >= 1.0 | +2 | |

**Context range: -25 to +28 points**

---

## Layer 5: Regime Integration

| Factor | Condition | Points | Evidence |
|--------|-----------|--------|----------|
| **Regime NORMAL** | Score >= 0 | +10 | 77.8% WR, +$5,037 |
| **Regime CAUTION** | Score -1 to -2 | -5 | 57.9% WR, -$5,719 |
| **Regime RESTRICTED** | Score -3 to -4 | -10 | 50% WR |
| **Regime BLOCKED** | Score < -4 | BLOCK | Suppress entirely |

**Regime range: -10 to +10 points**

---

## Total Scoring Range

```
Minimum possible:  6 + (-41) + (-46) + (-25) + (-10) = -116
Maximum possible: 38 + (+21) + (+35) + (+28) + (+10) = +132

Typical winner:   20 + 8 + 15 + 8 + 10 = ~61
Typical loser:    12 + (-8) + (-15) + 3 + (-5) = ~-13
Target separation: ~30-40 points between W and L averages
```

---

## Minimum Entry Score Threshold

| Threshold | Expected Behavior |
|-----------|-------------------|
| **>= 25** | Conservative — blocks marginal trades, 61% WR, +$1,016 (AGG backtest) |
| **>= 15** | Moderate — more trades, 58% WR |
| **>= 0** | Permissive — most trades pass, 54% WR |

**Recommended: >= 25** (start conservative, lower if too few trades)

---

## Complete Flow

```
ENTRY SIGNAL DETECTED
    │
    ▼
LAYER 0: HARD BLOCKS
    ├── nat_stop <= 0?          → REJECT "invalid_candle"
    ├── spread > nat_stop?      → REJECT "spread_exceeds_stop"
    ├── RSI 45-55?              → REJECT "neutral_rsi"
    ├── BB STRETCH?             → REJECT "bb_stretch"
    └── Regime BLOCKED?         → REJECT "regime_blocked"
    │
    ▼ (all clear)
LAYER 1: BASE SCORE
    score = zone_tier + pattern_type
    │
    ▼
LAYER 2: MARKET STATE
    score += entry_hour + box_age + volume_ratio + ranging + bb_state_bonus
    │
    ▼
LAYER 3: ENTRY QUALITY
    score += conviction + sma20_dist + nat_stop_quality + ema50_prox
             + wall_prox + bb_middle
    │
    ▼
LAYER 4: CONTEXT
    score += z_edge + z_align + ct_combos + adr + rr_tp1
    │
    ▼
LAYER 5: REGIME
    score += regime_modifier
    │
    ▼
THRESHOLD CHECK
    score >= 25?  → PASS (fire entry)
    score < 25?   → BLOCK (log score_blocked)
```

---

## Comparison with OLD Formula

| Aspect | OLD | V3 |
|--------|-----|-----|
| Score separation (W-L) | +0.5 pts | +12.5 pts |
| Best P&L at any threshold | Always negative | +$1,016 to +$3,526 |
| OTR weight | 0-15 pts | REMOVED (17% WR at low OTR) |
| ATR consumed weight | 0-20 pts | 0-4 pts (reduced 80%) |
| RR weight | 0-15 pts | 0-3 pts (reduced 80%) |
| Entry hour | Not scored | ±8 pts |
| Box age | Not scored | ±8 pts |
| Volume ratio | Not scored | +5/-8 pts |
| SMA20 distance | Not scored | +5/-8 pts |
| EMA50 proximity | Not scored | -8 pts |
| Conviction | Not scored (added recently at ±10) | ±20 pts (doubled) |
| BB STRETCH | Not blocked | HARD BLOCK |
| Invalid nat stop | Not blocked | HARD BLOCK |
| Spread > nat stop | Not blocked | HARD BLOCK |
