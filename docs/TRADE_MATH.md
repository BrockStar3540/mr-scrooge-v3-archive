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

## 6. The Decoupled Model

### Stop Loss: Tied to STRUCTURE, not price

```python
# The stop is the signal candle extreme + buffer
# No percentage floor needed if entry is valid
SL = natural_stop

# Only safety check: is the stop inside the spread?
if SL_distance < spread × 2:
    BLOCK  # stop is inside execution noise — not a real level
```

The theory says "stop at the candle extreme." If the candle extreme is 3 pips away, that IS the stop. A 40-pip floor overwrites the market's own structure with an arbitrary number.

The REAL protection against fakeout stops isn't a pip floor — it's the OTHER gates (sucker move conviction, zone tier quality, BB exhaustion state). If those pass, the candle stop IS the right stop.

### Risk/Reward: Tied to REALISTIC TARGET, not TP2 fantasy

```python
# TP2 hit rate: 6.6% (audit data)
# TP1 hit rate: much higher
# Harvester T1: this is what actually gets clipped

# Don't gate on RR at all (theory doesn't specify one)
# Instead, gate on PROFITABILITY:

expected_profit = (win_rate × avg_clip) - ((1 - win_rate) × SL_distance)
round_trip = 2 × spread

if expected_profit < round_trip:
    BLOCK  # can't make money after costs
```

Or simpler: replace the RR gate with a **profitability gate**:

```python
# Can the harvester profit after spread?
T1_distance = half_box × 0.30  # conservative: 30% of half box
net_after_spread = T1_distance - (2 × spread)

if net_after_spread <= 0:
    BLOCK  # harvester can't clear costs
elif net_after_spread < spread:
    WARN   # marginal, reduce size
else:
    PASS   # healthy margin above costs
```

### Spread: Tied to BOX, not fixed pips

```python
# Current: block if spread > 5p (JPY) or 2p (default)
# Problem: 2p on a 200p box is nothing; 2p on a 20p box is 10%

# Better: spread as percentage of half_box
spread_pct = spread / half_box

if spread_pct > 0.15:   # spread > 15% of reward = toxic
    BLOCK
elif spread_pct > 0.08:  # spread > 8% = elevated
    WARN + reduce size
else:
    PASS
```

### Harvest Viability: Tied to SPREAD CLEARANCE

```python
# Current: harvest at 1.5% equity gain
# Problem: this translates to different pip distances per pair/size

# Better: also verify the T1 clip distance exceeds spread
T1_pips = (equity × 0.015) / (units × pip_value)

if T1_pips < (2 × spread_pips × 1.5):  # need 1.5x spread clearance
    # Harvester can't profit — either reduce units or skip trade
    WARN
```

### Position Size: Already correct (dual constraint)

```python
margin_units = (equity × margin_util) / (base_price × margin_rate)
risk_units = (equity × max_risk_pct) / (SL_pips × pip_value)
units = min(margin_units, risk_units)
```

This is fine. The risk cap naturally produces smaller positions when SL is wide and larger when SL is tight.

---

## 7. The Unified Viability Check

Instead of 4 separate gates (spread, RR, OTR, SL floor) that each reference different frames, ONE viability check:

```python
def is_trade_viable(box_range, spread, natural_stop, half_box):
    """
    Single check: can this trade produce net profit after all costs?
    Replaces: SL floor, RR gate, OTR gate, spread gate.
    """

    # 1. Is the stop a real structural level?
    if natural_stop < spread * 2:
        return False, "stop_inside_noise"

    # 2. Is the box wide enough relative to costs?
    spread_pct = spread / half_box
    if spread_pct > 0.15:
        return False, "spread_consumes_box"

    # 3. Can we profit after round-trip spread?
    round_trip = 2 * spread
    conservative_target = half_box * 0.40  # 40% of half box (realistic clip)
    net_profit = conservative_target - round_trip
    if net_profit <= 0:
        return False, "no_profit_after_costs"

    # 4. Is the overhead ratio acceptable?
    otr = round_trip / half_box
    if otr > 0.25:
        return False, "overhead_too_high"

    return True, f"viable (net={net_profit:.4f}, otr={otr:.1%})"
```

---

## 8. What Today's USD_JPY Looks Like Under This Model

```
Box:          51 pips
Half box:     25.5 pips
Spread:       1.6 pips
Round trip:   3.2 pips
Natural stop: 3-11 pips (from actual candles)

Spread % of half box: 1.6 / 25.5 = 6.3%  → PASS (< 15%)
Conservative target: 25.5 × 0.40 = 10.2 pips
Net after costs: 10.2 - 3.2 = 7.0 pips  → PASS (> 0)
OTR: 3.2 / 25.5 = 12.5%  → PASS (< 25%)

TRADE IS VIABLE.

The 10:30 short (wick rejection, 4 green candles, natural SL = 3 pips):
  RR to center: 25.5 / 3 = 8.5
  RR to TP2: 51 / 3 = 17.0
  Harvest: even a 5-pip clip nets 5 - 3.2 = 1.8 pips above spread

This trade should have fired.
```

---

## 9. What the Old Model Blocked

```
SL floor: 0.25% × 159 = 39.8 pips  ← IMPOSED, not from market
RR: 25.5 / 39.8 = 0.64  ← below 1.35 minimum
Result: BLOCKED

But the actual candle stop was 3 pips.
The actual RR was 8.5 to center, 17.0 to wall.
The SL floor destroyed the math by replacing market structure with a fixed percentage.
```

---

## 10. Summary of Changes for V3

| Old Gate | Problem | V3 Replacement |
|----------|---------|----------------|
| SL floor (% of price) | Overwrites candle structure, kills RR on tight boxes | Remove. Use natural stop. Guard: stop must be > 2× spread (noise floor) |
| RR gate (TP2/SL > 1.35) | TP2 is fantasy (6.6% hit rate), SL inflated by floor | Replace with profitability gate: can harvester clip above spread? |
| Spread gate (fixed pips) | 2p on 200p box ≠ 2p on 20p box | Spread as % of half_box (15% threshold) |
| OTR gate (spread/half_box) | Already correct reference frame | Keep, already viable |

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

## 11. Risk This Creates

Removing the SL floor means some stops will be very tight (3-5 pips). Risks:

1. **Noise stops**: price wiggles 3 pips and you're out. Mitigation: the OTHER gates (sucker move, zone tier, BB exhaustion) ensure you're only entering at high-conviction reversal points. If conviction is high, a tight stop is correct — the trade thesis is invalidated if price moves past the candle extreme.

2. **Spread spikes**: a 3-pip stop on a pair that suddenly spreads to 4 pips = instant fill. Mitigation: the noise floor check (stop > 2× spread) catches this. If spread is 4 pips and natural stop is 3 pips, the trade is blocked — correctly.

3. **Win rate may drop**: tighter stops = more stopouts on valid trades that just need room. Mitigation: position size via risk cap will be LARGER on tight stops (same dollar risk, fewer pips = more units). So each winner earns more. The math may actually improve.

The real question is whether the conviction gates (sucker move + pitchfork + zone + BB exhaustion) are strong enough to ensure tight stops are at genuine invalidation levels. The OANDA audit showed 75-78% WR on NORMAL regime trades — that conviction exists.
