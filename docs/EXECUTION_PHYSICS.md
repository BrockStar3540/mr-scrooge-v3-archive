# Execution Physics — Order Timing and SL Validation

> Proven with OANDA nanosecond timestamps. Every SL move goes through
> 4 guards before submission. If any guard blocks, the original native
> SL stays in place as backstop.

## The Problem

OANDA doesn't execute stops on mid-price. It uses the execution side:

- **Short positions**: SL triggers on the **ASK** price
- **Long positions**: SL triggers on the **BID** price

During thin sessions (Sunday evening, Sydney-only), JPY pair spreads
blow out to 13-16 pips. The bot calculates a trailing SL from mid-price,
but the ASK is already past the SL. OANDA fills it in the same nanosecond
as the modification:

```
SL replacement: 21:11:30.620570733Z → new SL 215.442
SL fill:        21:11:30.620570733Z → filled at 215.518 (7.6 pip slippage)
```

Same nanosecond. Dead on arrival.

## The Correct Order of Operations

### Entry

1. Strategy produces candidate with entry/SL/TP prices
2. Bot fetches LIVE bid/ask from OANDA pricing API
3. StopPlanner validates SL against live prices (4 guards)
4. If any guard blocks → entry skipped (wait for spreads to normalize)
5. If all pass → single MARKET order with `stopLossOnFill` + `takeProfitOnFill`
6. SL+TP are atomic with the entry — no gap without protection

### SL Trailing (every cycle)

1. PositionPipeline calculates new SL from hybrid trail
2. Bot fetches LIVE bid/ask
3. Four guards run BEFORE submitting:
   - **Spread kill switch**: spread > 5p (JPY) / 2p (default) → SKIP
   - **No-man's zone**: bid < new_sl < ask → SKIP
   - **Trigger-side check**:
     - Short: new_sl must be > ask + (spread × 1.5)
     - Long: new_sl must be < bid - (spread × 1.5)
   - **Buffer minimum**: at least 2 pips beyond execution side
4. Only if all 4 pass → submit to OANDA
5. If blocked → original native SL stays as backstop

## What Each Guard Does

| Guard | When It Fires | What It Prevents |
|-------|--------------|-----------------|
| **Spread kill** | Spread > 5p JPY / 2p default | Trailing during wide spreads ejects the trade |
| **No-man's zone** | SL between bid and ask | Instant fill — SL is inside the spread |
| **Trigger-side** | SL on wrong side of execution price | OANDA fills SL atomically on modification |
| **Buffer** | SL too close to execution price | Micro-slippage on tight pairs |

## What Happens When a Guard Blocks

The bot does NOT close the trade. It doesn't move the stop. The original
OANDA native SL (set at entry) remains as the hard backstop. Next cycle
the bot re-evaluates. If spreads tighten or price moves enough, it trails then.

**The trade survives instead of getting ejected by its own protection.**

## V3 Implementation

- `execution/stop_planner.py` — `validate_stop()` runs all 4 guards
- `execution/stop_planner.py` — `should_trail()` checks spread kill switch
- `core/runtime.py` — Entry flow fetches live quote and validates SL before placing
- All SL moves in PositionPipeline go through the same validation

## Audit

Every SL move attempt logged to `data/execution-audit.jsonl` with full context
(bid, ask, spread, reason, outcome). Dashboard Execution tab shows stats live.
