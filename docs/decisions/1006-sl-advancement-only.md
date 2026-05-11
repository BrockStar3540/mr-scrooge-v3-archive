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

---

## Conversation evidence — 2026-03-20 session

Source: `/Users/brock-mini-mac/Dropbox/LLM Sessions/Claude Sessions/trading - Mr Scrooge/2026-03-20_1c92abef.md`

Context: the bot had been profitable on the `1c99ae2` commit, then 23 commits
rolled in over an evening that converted it to a 30-minute rolling box with
fixed-pip stops anchored to fill price. The bot started bleeding. This session
identifies the working commit, lists six structural regressions, and walks them
back while keeping the legitimate additions (scoring, ranking, dashboard).

**The diagnosis (line ~202):**

> Claude: "OK, here's the full picture. There are **major structural changes**
> between the profitable version and what's running now … The bot is basically
> running a completely different strategy now."

The six breaking changes (line ~204–224):

> 1. Box mode: Daily → 30m rolling window
> 2. TP levels: Box-relative → Fixed pips
> 3. Entry/Stop pricing: Candle-based → Zone-anchored with fixed pip stops
> 4. Sizing: 50% margin with decompressors → 80% margin, no decompressors
> 5. Green exit removed
> 6. high_volatility_atr_mult = 99 — effectively disabled the volatility gate

**Brock's decision (line ~238):**

> Brock: "yeah, lets get rid of the 30 minute bushit, and fix our bot back to
> making money like it was, 1-6."

**External reviewer alternative considered and partially rejected:** another
agent suggested keeping the fill-anchored stops but restoring the ATR gate
(line ~239–246). Claude flagged the review as partly wrong on the facts (line
~320: "Good analysis from them, but let me fact-check against the actual diff
before we act") and pursued the wider revert instead.

**The crisis trade that triggered the second pass — ratchet too tight on a
5-pip TP1 (line ~1963):**

> ```
> 15:35:33 — ENTRY SHORT @ 0.58407, SL 0.58507 (10p), TP1 0.58357 (5p)
> 15:45:33 — Stop moved to 0.58407 (breakeven) — "price 0.58380 is 50% of way to TP1"
> 15:50:23 — OANDA NATIVE CLOSE at SL 0.58407 (breakeven) — +$3.11
> ```

> Claude: "The harvester's **ratchet stage 1** killed it. Price hit +2.7 pips
> (0.58380), which is 50% of the way to TP1. The harvester moved the SL to
> breakeven (0.58407). Then price bounced back to 0.58407 and got stopped out at
> breakeven … The problem: the ratchet is too aggressive. Moving SL to breakeven
> at only +2.5 pips means any normal pullback kills the trade before it can
> reach TP1 at +5 pips."

**Brock's framing — green-exit + harvester resolve the management problem
without changing the ratchet logic (line ~1065):**

> Brock: "this was what we want in some form, with the harvester and hourly
> profit taker: SL / TP — Fixed Pip Structure. All SL/TP values are measured
> from the actual fill price. Stop Loss 10 / TP1 — Ratchet Trigger 5 / TP2 —
> Full Exit 30. Ratchet stages: 1. At +2.5 pips (50% to TP1): SL advances to
> break-even. 2. At +5 pips (TP1 hit): SL locks to entry+5. 3. Above TP1:
> hybrid trailing stop (80% profit lock, hourly candle trail, 1.5×ATR)."

**Alternative considered and rejected** — change the ratchet trigger from "50%
to TP1" to "TP1 hit" (Claude implemented this first, line ~2037). Brock pushed
back: keep the ratchet behavior, widen TP1 to 10 pips instead (line ~2057):

> Claude: "Ah — you want to keep the 50% ratchet behavior but make it work
> correctly. So instead of changing the ratchet logic, change TP1 to 10 pips.
> Then: at +5 pips (50% of TP1): SL moves to breakeven — **secures the 5 pips
> you want** … That's cleaner — the ratchet logic was fine, TP1 was just too
> tight."

**Key technical detail informing the decision:** Claude pulled `1c99ae2` from
git (line ~158: "The Initial release commit (`1c99ae2`) from March 19 at 2:13
PM is the version that was making money") and used it as a literal source of
truth to diff and revert file-by-file, rather than reasoning forward from
symptoms.
