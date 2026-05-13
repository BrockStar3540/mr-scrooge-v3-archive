# V3 Live Detection Feasibility for Raw-M5 v2 Survivors

Date: 2026-05-13

## Verdict

The raw-M5 v2 survivor gate is live-detectable in V3 with a small shadow feature
adapter. No new broker feed is required.

The strongest blind edge is:

```text
trigger in {T1, T2, T7, T8}
AND H1 regime == breakout
AND M15 trend aligns with trade direction
AND session_quarter / pair_family pocket is a double-survivor
```

The current V3 runtime already fetches:

- `M5` candles
- `H1` candles
- `D` candles
- bid/ask spread
- zone detector output including PDH/PDL-style range context

What is missing is not market data. What is missing is the exact research label
adapter:

- `m15_trend`
- `h1_regime`
- `h1_range_rank_48`
- raw-M5 trigger family tag for T1/T2/T7/T8

## Current V3 Coverage

| Requirement | V3 current support | Status |
|---|---|---|
| M5 bars | `scan_coordinator` fetches `M5` into `snapshot.candles["5M"]` | yes |
| H1 bars | `scan_coordinator` fetches `H1` into `snapshot.candles["1H"]` | yes |
| Daily bars | `scan_coordinator` fetches `D` into `snapshot.candles["D"]` | yes |
| M15 trend | can be derived from M5 resample; not currently logged | missing adapter |
| H1 breakout label | H1 bars exist; exact 48-hour range-rank not currently computed | missing adapter |
| T1/T2 BB reclaim/reject | Bollinger feature computes M5 Band A; near parity with factory | feasible |
| T7/T8 PDH/PDL proximity/failed break | zone detector has daily range context; exact formula should use D bars directly | feasible |
| spread-aware filtering | live bid/ask spread already present | yes |

## Exact Research Definitions to Port

### M15 Trend

From `research/raw-m5-winner-factory-v2/raw_m5_winner_factory_v2.py`:

```python
m15 = m5.resample("15min").agg({
    "open": "first",
    "high": "max",
    "low": "min",
    "close": "last",
}).dropna()
m15_ema20 = m15["close"].ewm(span=20, adjust=False).mean()

if m15_close > m15_ema20 * 1.0005:
    m15_trend = "up"
elif m15_close < m15_ema20 * 0.9995:
    m15_trend = "down"
else:
    m15_trend = "flat"
```

Aligned means:

```text
long  -> m15_trend == up
short -> m15_trend == down
```

### H1 Regime

From the same factory:

```python
h1 = m5.resample("1h").agg({
    "open": "first",
    "high": "max",
    "low": "min",
    "close": "last",
}).dropna()
h1_range = h1["high"] - h1["low"]
h1_range_rank_48 = h1_range.rolling(48).rank(pct=True)

if h1_range_rank_48 < 0.25:
    h1_regime = "consolidation"
elif h1_range_rank_48 > 0.75:
    h1_regime = "breakout"
else:
    h1_regime = "in_range"
```

The blind-survivor edge requires:

```text
h1_regime == breakout
```

### Trigger Families

Use the v2 raw-M5 formulas exactly.

```python
# T1: BB lower reclaim, long
prev_low <= prev_bb_lower and close > bb_lower

# T2: BB upper reject, short
prev_high >= prev_bb_upper and close < bb_upper

# T7: PDL/PDH proximity reversal
long:  prev_low near PDL within 10 pips and close > prev_close
short: prev_high near PDH within 10 pips and close < prev_close

# T8: failed PDL/PDH breakout
long:  prev_low < PDL and close > PDL
short: prev_high > PDH and close < PDH
```

## Feasibility Decision

This is feasible as a shadow-only V3 feature first:

1. Add a small feature module, e.g. `technical_context`, that computes:
   - `m15_trend`
   - `m15_ema20`
   - `h1_range_rank_48`
   - `h1_regime`
2. Add a shadow detector that tags each scan/candidate with:
   - `raw_m5_v2_trigger_family`
   - `raw_m5_v2_structural_gate_pass`
   - `raw_m5_v2_survivor_cell_key`
3. Log those fields to `scans.jsonl` / observer features.
4. Do not block or place trades from this yet.
5. After one live day, verify that the labels populate correctly and line up
   with the historical survivor definitions.

## Why This Matters

The synchrony check showed:

- 335 / 335 raw-M5 double survivors share a repaired/textbook winner pocket.
- 315 / 335 have trigger-matched repaired-winner synchrony.
- 168 / 335 also carry the structural `H1 breakout + M15 aligned` gate.

That means the blind historical cells are not isolated optimizer artifacts. They
land in the same market-state neighborhoods as the repaired textbook winners.

The next correct step is not a production strategy flip. The next correct step is
live shadow detection of the exact labels that define those survivor cells.

## Non-Goals

- No new live trade entries.
- No management rule changes.
- No use of the old 47-point score.
- No deployment of a broad textbook formula library.
- No BE-at-0.5R rule.

## Recommended Next Artifact

Build `technical_context` as a V3 shadow feature and emit it in observer logs.
Then run a one-day shadow audit:

```text
Which live scans matched a raw-M5 survivor cell?
Which one became a real trade?
Which one was blocked by a gate?
Which one reached +1R / +2R afterward?
```

This directly connects the blind historical discovery to live bot behavior.
