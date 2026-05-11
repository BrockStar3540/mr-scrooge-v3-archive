# 1006. SL-advancement-only (no market-order exits)

**Status:** Accepted (preserved through V2 and V3)
**Date:** 2026-03-12 (green-exit crisis resolution)
**Version scope:** V1 (architectural principle that survives)
**Backfilled:** 2026-05-11

## Context

A critical bug was firing in production: the bot was entering an **infinite retry loop** when trying to set a LIMIT TP order via OANDA after price had already reached or passed the target. OANDA's API rejects LIMIT orders where the limit price is at or past the market. The `green_exit` and `set_tp` handlers fired on every cycle with no escape mechanism.

Beyond the immediate loop bug, the bot's exit logic was sprawling:
- `time_exit` (market order backstop)
- Stop-hit close via market order
- `green_exit` / `set_tp` (reactive LIMIT placement)
- `partial_tp` (partial market close at TP1, TP2)
- Early break-even tied to partial framework

Multiple paths could all fire on the same trade in the same cycle.

## Decision

**Eliminate all reactive TP-setting and market-order exit logic.** Bot becomes **SL-advancement only**:

1. OANDA's native GTC LIMIT TP set at entry as TP2 handles the take-profit exit. Bot never modifies it after entry.
2. Bot never places market orders during a trade. Ever.
3. New 3-stage SL advancement (ratchet-only — never loosens):
   - **Stage 1 (break-even):** SL → entry when price reaches 50% of distance to TP1
   - **Stage 2 (TP1 lock):** SL → TP1 when price passes TP1
   - **Stage 3 (hybrid trail):** `max(hourly_candle_low, entry + 80% × peak_profit, peak − 1.5×ATR)` after break-even achieved
4. Ratchet-only: `move_stop = max(candidates)` for longs, `min` for shorts. Never moves SL adversely.

## Alternatives considered

- **Add retry backoff to `green_exit`** — rejected. Solves the loop but keeps reactive logic and parallel exit paths.
- **Single retry with exception handling** — rejected. Same problem one level deeper.
- **Keep market-order exits but add cycle counter** — rejected. Doesn't address the architectural sprawl.

## Consequences

**Enabled:**
- The bot can't enter infinite loops on TP modification because there is no TP modification.
- Single exit path per trade: SL hits (advancing or original) OR TP2 hits OR position is closed externally.
- Simpler reconciliation: position state is "SL price" + "TP2 price (fixed)" + peak tracking.

**Closed:**
- Bot will never place a market order for an in-flight trade.
- Reactive partial closing.

**Costs:**
- Cannot opportunistically take partial profits during a strong move (must let the trade hit TP1 or be ratcheted).
- Some marginally-green trades that would have been hand-closed in the old system now ratchet through their natural completion.

## Survival into V3

V3's walker (`simulate_trade_multi`) is "Phase-2 minimal": SL, TP, timeout. **Same architectural principle**: management is geometry, not reactivity. The walker doesn't move SL/TP after candidate creation. This trace directly to the Mar 12 decision.

## Cross-references

- `archive/DAILY_NOTES_2026-03-12.md` (Dropbox)
- `[[scrooge-bug-catalog]]` B-033 (the original loop)
- `src/execution_simulator.py:simulate_trade_multi` (V3 inheritor)
- V3 frozen constraint #15 (walker phase-2 minimal)
