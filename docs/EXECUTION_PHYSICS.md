# Execution Physics — Order Timing and SL Validation

> **Current as of 2026-05-30.** This is doctrine plus the live `StopPlanner`
> implementation. Both have proven durable through the V3 → V4-prep arc.
> Updated to reflect the move from fixed pip thresholds to rolling-mean
> spread comparison.

## The Problem

OANDA doesn't execute stops on mid-price. It uses the execution side:

- **Short positions**: SL triggers on the **ASK** price
- **Long positions**: SL triggers on the **BID** price

During thin sessions (Sunday evening, Sydney-only), JPY pair spreads
blow out to 13-16 pips. The bot calculates a trailing SL from mid-price,
but the ASK is already past the SL. OANDA fills it in the same nanosecond
as the modification:

```
SL replacement: 21:11:30.620570733Z -> new SL 215.442
SL fill:        21:11:30.620570733Z -> filled at 215.518 (7.6 pip slippage)
```

Same nanosecond. Dead on arrival.

## The Correct Order of Operations

### Entry

1. Strategy produces candidate with entry/SL/TP prices
2. Bot fetches LIVE bid/ask from OANDA pricing API
3. `StopPlanner` validates SL against live prices (4 guards, below)
4. If any guard blocks -> entry skipped (wait for spreads to normalize)
5. If all pass -> single MARKET order with `stopLossOnFill` + `takeProfitOnFill`
6. SL+TP are atomic with the entry — no gap without protection

### SL Trailing (every cycle)

1. PositionPipeline calculates new SL from hybrid trail
2. Bot fetches LIVE bid/ask
3. Four guards run BEFORE submitting:
   - **Spread kill switch**: spread > `mean_spread × fast_market_multiplier`
     (default 2.5×) -> SKIP. Replaces the older fixed-pip threshold
     (was 5p JPY / 2p default through April 2026) with a per-pair
     rolling-mean comparison so JPY and non-JPY are gated on the same
     relative-volatility rule.
   - **No-man's zone**: bid < new_sl < ask -> SKIP
   - **Trigger-side check**:
     - Short: `min_safe = ask + spread + (pip × 2)`. If new_sl < min_safe,
       adjust upward to min_safe.
     - Long: `max_safe = bid - spread - (pip × 2)`. If new_sl > max_safe,
       adjust downward to max_safe.
   - **Buffer minimum**: `trigger_buffer_pips` (default 3.0) beyond
     execution side, with `limit_offset_pips` (default 0.5) for the
     proactive harvest limit.
4. Only if all 4 pass -> submit to OANDA
5. If blocked -> original native SL stays as backstop

## What Each Guard Does

| Guard | When It Fires | What It Prevents |
|-------|--------------|-----------------|
| **Spread kill** | `spread > mean_spread × 2.5` | Trailing during wide spreads ejects the trade |
| **No-man's zone** | SL between bid and ask | Instant fill — SL is inside the spread |
| **Trigger-side** | SL on wrong side of execution price | OANDA fills SL atomically on modification |
| **Buffer** | SL too close to execution price | Micro-slippage on tight pairs |

## What Happens When a Guard Blocks

The bot does NOT close the trade. It doesn't move the stop. The original
OANDA native SL (set at entry) remains as the hard backstop. Next cycle
the bot re-evaluates. If spreads tighten or price moves enough, it trails
then.

**The trade survives instead of getting ejected by its own protection.**

## V3 Implementation

Single load-bearing module: `src/scrooge_v3/execution/stop_planner.py`
(~182 lines as of 2026-05-30).

| Function | Role |
|----------|------|
| `validate_stop(direction, proposed_stop, bid, ask, spread)` | Runs trigger-side + no-man's-zone guards, returns (adjusted_stop, reason) |
| `is_entry_spread_hostile(spread, mean_spread)` | Dedicated entry-time spread preflight (does NOT reuse should_trail's geometry checks — that was a 2026-05 bug fix; see commit history) |
| `should_trail(...)` | Trail-time spread + tightness check |

All SL moves in `PositionPipeline` and the entry flow in `runtime.py`
route through the same validation.

## Configuration knobs

In `config/default.json` under `execution`:

| Key | Default | Notes |
|-----|---------|-------|
| `trigger_side_validation` | `true` | Master switch for trigger-side guard |
| `no_mans_zone_guard` | `true` | Master switch for spread-internal SL prevention |
| `spread_aware_trailing` | `true` | Master switch for spread kill |
| `reverse_direction` | `false` | Independent feature flag |

`StopPlanner` constructor knobs (passed via execution section, see
class signature):

| Key | Default | Notes |
|-----|---------|-------|
| `trigger_buffer_pips` | `3.0` | Minimum SL distance beyond execution side |
| `limit_offset_pips` | `0.5` | Proactive harvest limit offset |
| `fallback_buffer_pips` | `10.0` | Fallback when live prices unavailable |
| `fast_market_multiplier` | `2.5` | Spread kill trigger: `spread > mean × this` |

## Audit

Every SL move attempt logged to `data/execution-audit.jsonl` with full
context (bid, ask, spread, reason, outcome). Dashboard Execution tab
shows stats live.

## What changed since the 2026-04-15 revision

- **Spread kill switch:** moved from fixed pip thresholds (5p JPY /
  2p default) to rolling-mean-relative (`fast_market_multiplier × 2.5`).
  Reason: JPY and non-JPY have very different mean spreads, so a fixed
  threshold either over-blocks JPY or under-blocks non-JPY. The
  rolling-mean approach gates both on the same volatility-relative rule.
- **Entry vs trail spread checks decoupled:** `is_entry_spread_hostile`
  is now a dedicated function (does NOT reuse `should_trail`). The old
  reuse caused entry-time spread vetoes to be bypassed when
  `validated_sl == best.stop_price`, which is the common fresh-entry
  case. Fix shipped May 2026.
- **`StopPlanner` itself:** unchanged in core logic — the 4 guards are
  the same physics described in the April revision. The execution
  doctrine is durable.

## Cross-references

- `src/scrooge_v3/execution/stop_planner.py` — load-bearing module
- `docs/LIVE_SYSTEM_SPEC.md` — current admission stack (execution
  section)
- `docs/TRADE_PHYSICS_FIRST_PRINCIPLES.md` — the "stop must be > 2×
  spread" noise-floor rule originates here
- `docs/decisions/1006-sl-advancement-only.md` — the doctrine that
  the bot only advances stops, never gives them back
