# 1010. TradeCoordinator — multi-actor shared state

**Status:** Accepted (V1 Phase 1 shipped 2026-04-10); informs V3 architecture
**Date:** 2026-04-10
**Version scope:** V1 (architecturally formative for V3)
**Backfilled:** 2026-05-11

## Context

A trade audit on 2026-04-10 found that **four independent actors** were modifying the same OANDA trade with **no shared state**:

1. **Bot** (entry, management of position-level decisions)
2. **Ratchet** (SL advancement via stages)
3. **SL-limit** (proactive REDUCE_ONLY limit placement near stop)
4. **Harvester** (tier-based partial closes)

Symptoms:
- SL-limit spammed **46 API calls** on a position that no longer existed (no one told it the trade had vanished)
- Ratchet and harvester raced on SL moves
- Ratchet didn't know harvester's tier state — couldn't sync `partial_1_taken`

## Decision

Introduce `TradeCoordinator` — file-backed cross-process state shared by all four actors.

Schema (per trade):
- `trade_id`
- `is_alive` (set by bot on entry, false on vanished detection)
- `sl_owner` ("ratchet" or "harvester" — handoff after final tier close)
- `current_sl` (last-known SL price)
- `tiers_hit` (which harvester tiers have fired)

Protocol:
- Bot registers trade at entry, marks dead on vanished detection
- Fast loop checks `is_trade_alive` gate before SL-limit placement
- Ratchet checks `sl_owner` before pushing SL
- Ratchet reads `tiers_hit` to sync `partial_1_taken`
- `place_opposing_limit` detects `NO_POSITION_TO_REDUCE` cancels

## Alternatives considered

- **In-memory shared state via Python `multiprocessing.Manager`** — rejected. Process boundaries don't always align with actor boundaries; file-backed is more portable across the bot, the fast loop (separate thread), and the harvester (separate process).
- **Centralize all actors into one process** — rejected. Fast loop (3-sec cadence) and slow loop (5-min cadence) had different cadence requirements; collapsing them lost the dual-loop benefit.
- **Have OANDA be the source of truth (always re-fetch)** — partial adoption (we do check OANDA), but the latency was too high for the 3-sec fast loop.

## Consequences

**Enabled:**
- Zero false SL-limit placements on dead positions (the 46-call spam pattern doesn't repeat).
- Ratchet and harvester coordinate explicitly via `sl_owner`.
- Cross-actor visibility into tier completions.

**Closed:**
- Implicit state sharing between actors. Anything new that modifies trade state must register with TradeCoordinator.

## Survival into V3

V3 inherits the pattern but reframes it:
- `data/order-attribution.jsonl` is the V3 analog (Patch B.right) — explicit `(order_id) → strategy` linkage.
- `execution-audit.jsonl` is the cross-actor event log.
- The principle stands: **multi-actor systems on the same resource need a shared truth.**

## Lesson preserved

**State scattered across actors produces phantom-action bugs.** The 46-order spam is the canonical example: each actor was doing what it thought was right; no one had the truth.

## Cross-references

- `archive/DAILY_NOTES_2026-04-10.md` (Dropbox) AND `NOTES.md` 2026-04-10 section in repo
- `[[scrooge-bug-catalog]]` B-055, B-056, B-057
- V3 attribution patches: ADR `3001-regime-aware-not-global-score.md` (cross-reference to attribution work)
