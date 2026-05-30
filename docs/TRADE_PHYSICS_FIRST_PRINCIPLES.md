# Trade Physics — First Principles

> **Canonical doctrine 2026-05-30.** This is the first-principles
> coupling analysis that the V3 implementation work was built on.
> Specific implementation details (gate replacements, the V3 unified
> viability function, the USD_JPY worked example) have been moved to
> `docs/archive/TRADE_MATH_v3.0-implementation.md` because they describe
> a gate stack that has since been retired (ADR 3017).
>
> What remains here is **evergreen**: the coupling diagnosis, the
> independent vs derived variables, and the five rules that any trade
> must satisfy. These outlast any particular implementation.
>
> Source: `docs/TRADE_MATH.md` sections 1-5 + the closing "Doctrine" box,
> archived 2026-05-30.

---

# Trade Math — First Principles Parameter Analysis

> **NOTE:** This is the first-principles analysis that identified the coupling
> problems. Specific thresholds proposed here were refined by the Factor Bible
> analysis and the proportional gap analysis. The deployed formula is in
> `SCORING_V3_LIVE.md`. The unified viability check proposed here was replaced
> by the V3 Hybrid Scorer with its pair layer.

> "If changing one parameter breaks another, they're coupled wrong."

---

## 1. The Problem

V1/V2 has 7 setups today with RR 2.0-5.3 on natural stops, ALL blocked because the SL floor (0.25% of price = 40 pips on JPY) inflates the stop to consume 78% of the box. This isn't a threshold tuning problem. It's a coupling problem.

Parameters are tied to the WRONG reference frames:

| Parameter | Currently tied to | Should be tied to |
|-----------|------------------|-------------------|
| SL floor | % of PRICE (0.25%) | Signal candle, or % of BOX |
| RR gate | TP2 / SL | Realistic target / actual risk |
| Harvest trigger | % of EQUITY | Must clear spread in PIPS |
| OTR gate | spread / half_box | Already correct |
| Spread gate | fixed pip threshold | % of box range |
| Position size | margin utilization | margin AND risk cap |

When these reference frames mismatch, changing one parameter can't fix the system — it just moves the pathology somewhere else.

---

## 2. Independent Variables (Market Gives Us These)

These are inputs. We don't control them.

```
B  = box_range     = PDH - PDL          (today's trading range)
H  = half_box      = B / 2              (max realistic reward)
S  = spread        = ask - bid           (current execution cost)
N  = natural_stop  = signal candle extreme + buffer  (what theory says)
A  = ATR           = 14-period true range (daily movement budget)
P  = price         = current mid price
```

---

## 3. Derived Variables (We Calculate These)

```
SL = actual stop distance used
RT = round_trip_cost = 2 × S           (spread paid on entry + exit)
T1 = harvest_distance                   (first partial take profit)
RR = reward / risk                      (ratio)
U  = position_units                     (size)
```

---

## 4. The Coupling Map

```
         price (P)
           |
     [SL FLOOR]  ← WRONG anchor: SL = P × 0.25% = 40p on JPY
           |
          SL
         / | \
        /  |  \
      RR  risk  sizing
      |    |      |
    [GATE] |   [margin]
           |
     [harvest viable?]
           |
      RT = 2×S
```

The SL floor anchored to PRICE poisons everything downstream:
- RR = H / SL → killed because SL is inflated
- Risk per trade = SL × U × pip_value → inflated
- Harvest viability = T1 distance vs RT → unrelated to SL but can't fire if RR gate blocks entry

---

## 5. First Principles: What Must Be True for a Trade to Work?

### Rule 1: The trade must be able to profit after costs

```
net_profit = gross_move - round_trip_cost
           = (T1 or H) - (2 × S)

MINIMUM: net_profit > 0
HEALTHY: net_profit > 2 × S  (profit exceeds cost by 2x)
```

### Rule 2: The stop must reflect the structure being traded

```
SL = natural_stop  (signal candle extreme + buffer)

The stop is WHERE the trade thesis is invalidated.
Not a percentage of price. Not a percentage of ATR.
The candle tells you where you're wrong.
```

### Rule 3: You must be able to harvest above the spread

```
harvest_T1_pips = (equity × tier_pct) / (units × pip_value)

MINIMUM: harvest_T1_pips > 2 × S_pips
```

If the harvester can't clip a profit above the round-trip spread cost, the entire management model breaks down — you're paying spread to harvest nothing.

### Rule 4: Position size must not risk more than X% of equity

```
max_loss = SL_pips × units × pip_value
max_loss ≤ equity × max_risk_pct  (e.g., 4%)

units = min(margin_units, risk_cap_units)
```

### Rule 5: The box must be wide enough to trade

```
tradeable = B > (2 × S × safety_factor) + min_viable_stop
         = the box must accommodate spread costs AND a meaningful stop
```

---

---

## The Doctrine (preserved verbatim from the 2026-04-15 analysis)

### The Doctrine

```
The STOP is set by the MARKET (signal candle extreme).
The REWARD is set by the STRUCTURE (box range).
The COST is set by the BROKER (spread).
The VIABILITY is: can the structure's reward clear the broker's cost
                   with the market's stop?

If yes → trade.
If no → the box is too tight for this pair right now. Wait.

Never overwrite market structure with arbitrary percentages.
```


---

## Cross-references

- `docs/LIVE_SYSTEM_SPEC.md` — current executable truth (admission stack,
  routing, management profiles)
- `docs/EXECUTION_PHYSICS.md` — OANDA trigger-side execution + StopPlanner
  guards (the "stop must be > 2× spread" noise-floor rule from this doc
  is implemented there)
- `docs/MASTER_THEORY.md` — canonical theory doc (Box reversal, sucker
  move, zone tiers, BB exhaustion gates)
- `docs/decisions/` — architectural decision records, especially:
  - ADR 3008 (MatrixRouter replacing the gate stack)
  - ADR 3017 (V3HybridScorer disabled, LightGBM PRIMARY GATE @ 0.75)
- `docs/archive/TRADE_MATH_v3.0-implementation.md` — original V3 gate
  replacement proposals (historical only)
