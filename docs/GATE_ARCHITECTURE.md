# V3 Gate Architecture — How Regime, Gates, and Scorer Work Together

> Three layers, three jobs, zero overlap.

```
Layer 1: REGIME  — "Is the market broken?"
Layer 2: GATES   — "Is this mechanically valid?"
Layer 3: SCORER  — "Is this a good trade?"
```

Each layer answers ONE question. No layer does another layer's job.

---

## Layer 1: Regime (Broad Filter)

Regime is the macro circuit breaker. It only asks: *"Is the market environment so hostile that NO trade can work right now?"*

- **Only blocks on BLOCKED state** (composite score < -4). This means multiple failure signals are stacking — qualified failures, box acceptance, rejection decay, breadth all firing negative simultaneously.
- **CAUTION and RESTRICTED pass through.** The old system blocked at score >= -1 which killed winners in mild adverse conditions. The V3 scorer handles those — a strong setup can override a mildly negative regime.
- **Regime should NEVER evaluate individual trade quality.** That's the scorer's job.

---

## Layer 2: Gates (Mechanical Validity)

Gates check things that are structurally impossible to trade profitably **regardless of setup quality**. Only two mechanical gates remain in the pipeline:

| Gate | Why it exists | Why the scorer can't handle it |
|------|--------------|-------------------------------|
| **Debounce** | Prevents re-entering the same zone within 20 minutes | Scorer has no memory of what happened 20 minutes ago |
| **Zone Entry Cap** | Max 3 entries per zone+direction per day | Scorer evaluates each trade independently without knowing the day's history at that zone |

**Everything else that was a gate is now scored by the V3 scorer:**

| Former Gate | Now Scored As |
|-------------|--------------|
| Spread quality | OTR factor (-11 to +4 pts) |
| Risk/reward | R:R factor (0-3 pts, minimal weight — dead signal) |
| BB exhaustion | BB State factor (+3 NORM, +2 REJ, STR_UP blocked) |
| OTR threshold | OTR factor **INVERTED** (<8% = -11 penalty, was positive before) |
| ATR consumed | ADR factor (0-4 pts, was 0-20) |
| Regime floor | REMOVED (regime only blocks on BLOCKED) |
| Directional pressure | Momentum (±8) + Directional candles (±7) |
| Entry confirmation | Body% (±8) + entry candle analysis |
| Zone proximity | Wall proximity (-9 to +2 pts) |
| Trend filter | Z-score (±9) + EMA distances |

**Why gates were reduced:** The old system had 12+ gates that each independently decided pass/fail with no awareness of the other gates. A trade could have perfect conviction, perfect timing, perfect structure — but one gate with a threshold 0.01 too tight would kill it. The scorer evaluates ALL 43 factors together and makes ONE decision.

---

## Layer 3: V3 Hybrid Scorer (Precision Filter)

The scorer evaluates each trade on 43 factors weighted by proportional gap data from 50 V1 live trades. It has three sub-layers:

### Hard Blocks (score = 0, instant reject)

| Block | Condition | Evidence |
|-------|-----------|----------|
| RSI neutral | RSI 45-55 | 29% WR, no conviction |
| BB Stretch | STRETCH_UP or STRETCH_DOWN | 0% WR |
| Duration | >= 12h | Trade stagnated |
| OTR + NORM | OTR < 8% AND BB NORM | Wide box trap, 17% WR |
| Stale + EMA | Box age 18-24h AND EMA20 < 15% | Stale box + battle zone |

### Single Factor Points (17 factors)

| Strength | Factors | Point Range |
|----------|---------|-------------|
| Strongest | Entry hour, Box age | ±13 |
| Strong | Volume ratio, Natural stop | ±9 |
| Moderate | Momentum, Directional candles, Z-score, Wall proximity, Body% | ±5 to ±9 |
| Weak | ADR consumed, EMA distances, OTR, BB position, BB state, RSI, R:R | ±2 to ±7 |

### Paired Aspect Points (10 positive, 8 negative)

Winner clusters fire ON TOP of single factors when two conditions are true simultaneously:
- `00-07 UTC + BB NORM` → +14 (9W/0L)
- `box age <8h + RSI <45` → +9 (6W/0L)

Loser traps penalize dangerous combinations:
- `12-15 UTC + ADR 0.8-1.2` → -13 (0W/6L)
- `|z| < 0.5 + ADR 0.8-1.2` → -9 (0W/4L)

### Decision Rule

```
FINAL_SCORE = Layer 1 points + Layer 2 pair points

TAKE if score >= 65  (A-tier, high confidence)
TAKE if score >= 50  (B-tier, borderline)
REJECT if score < 50
```

---

## The One Rule

**If you're tempted to add a gate, add a scoring factor instead.**

Gates are binary (pass/fail) and can't weigh one factor against another. The scorer can. A trade with bad spread but perfect conviction and timing might still be worth taking — the scorer can make that tradeoff, a gate can't.

The only things that should be gates are:
1. Mechanical constraints the scorer can't see (zone cap, debounce)
2. Conditions so catastrophic that no factor can compensate (regime BLOCKED)

These catastrophic conditions are already the scorer's Layer 0 hard blocks.

---

## Configuration Values (from raw data)

These were derived from raw OANDA candle analysis, not theory:

| Setting | Value | Old Value | Why |
|---------|-------|-----------|-----|
| R:R threshold | 1.0 | 1.35 | R:R doesn't separate W from L |
| SL floor | 0.10% | 0.25% | Tighter stops win more |
| OTR scoring | INVERTED | Positive for low | <8% = 17% WR (worst bracket) |
| ATR weight | 0-4 pts | 0-20 pts | Only 4% delta between W and L |
| Regime floor | -4 (BLOCKED only) | -1 | Was killing winners in CAUTION |
| Scorer threshold | 50 | N/A | 100% WR on 20-trade test set |
