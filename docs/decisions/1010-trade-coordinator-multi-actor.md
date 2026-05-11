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

---

## Conversation evidence — 2026-04-10 session

Source: `/Users/brock-mini-mac/Dropbox/LLM Sessions/Claude Sessions/trading - Mr Scrooge/2026-04-10_54314085.md`

Context: while auditing live trades, Claude noticed a closed NZD_JPY position
generating 46 limit-order placements + cancels over 5 minutes. The
investigation surfaces a four-actor architecture where each loop has its own
view of "is this trade alive" and the fastest actor (3-second SL-limit thread)
acts on stale data.

**The smoking gun (line ~2654):**

> Claude: "There's a **critical bug** right in front of us. Look at tickets
> 6007 through 6094: **The harvester is spam-looping limit orders for a
> position that's already closed.** … 44 order+cancel cycles, every ~6
> seconds, from 1:17:31 PM to 1:22:13 PM — all trying to close 20,891 NZD/JPY
> units that were already closed by ticket 6000."

**Refined diagnosis — it's the SL limit subsystem, not the harvester (line
~2702):**

> Claude: "Found it. **It's not the harvester — it's the SL limit system in the
> main bot.**"

**The full four-actor map (line ~2799–2810):**

> | Actor | Loop | Interval | What It Does |
> |-------|------|----------|-------------|
> | Bot (slow loop) | Main thread | 5 min (candle close) | Signal detection, entries, ratchet SL management, green exits |
> | Ratchet (TradeManager) | Inside slow loop | 5 min | Advances SL: BE → TP1 → hybrid trail |
> | Harvester | Separate daemon | 30 sec | Partial profit extraction at T1/T2/T3 tiers |
> | SL Limit (fast loop) | Separate thread | 3 sec | Places limit orders near SL to capture stops as maker fills |

**The structural problem in Claude's words (line ~2812):**

> Claude: "The SL Limit system is a 3-second thread running inside the bot
> process. It's the fastest actor — 100x faster than the slow loop. But it
> only learns about position closures from `trade_manager.get_all_open()`,
> which only gets updated by the **5-minute slow loop**."

**The shared-state diagram (line ~2838):**

> ```
>                     OANDA (source of truth)
>                    /    |    \        \
>             Bot(5m)  Ratchet  Harvester(30s)  SL-Limit(3s)
>               ↕         ↕         ↕              ↕
>          trade_mgr  trade_mgr  own state     trade_mgr
>          (shared)   (shared)   (separate)    (shared, stale)
> ```

> Claude: "None of the four actors talk to each other except through OANDA
> state (which only gets polled at different intervals) … The harvester is the
> only one with its **own state file** — completely isolated. The other three
> share `trade_manager.open_positions` but only the slow loop updates it from
> OANDA. The SL limit thread reads stale data for up to 5 minutes after any
> external close." *(line ~2836, ~2847)*

**Brock's reaction confirming the framing (line ~2762):**

> Brock: "wow, 4th actor, i didnt think of that"

**Alternative considered and rejected — write a "closed" marker file or have
the SL-limit thread do its own OANDA GET (line ~2853):**

> Claude: "Harvester → Bot notification: After the harvester closes the final
> partial (all tiers hit, remaining units = 0), it should signal the bot.
> Options: write a 'closed' marker file the fast loop checks, or just have the
> fast loop do a lightweight OANDA `GET /trades/{id}` check before placing SL
> limits."

The chosen immediate fix was narrower: detect the
`NO_POSITION_TO_REDUCE` cancel and mark the position closed locally instead of
waiting for the 5-minute reconciliation (line ~2851):

> Claude: "SL Limit spam (immediate): When `place_opposing_limit` returns a
> cancel with `NO_POSITION_TO_REDUCE`, mark the position as closed in
> trade_manager right there. Don't wait 5 minutes. One-line fix."

**Key technical detail informing the ADR — the failure mode is rate-limit risk,
not just messy logs (line ~2738):**

> Claude: "**46 wasted API calls in 5 minutes on a dead trade.** This is a
> rate-limit risk on live, and it's the exact kind of bot/harvester desync we
> identified earlier."

**The principle that carries forward into V3's TradeCoordinator (line ~2757):**

> Claude: "This is the third component interaction problem: **the SL limit
> system is a fourth actor** (not just bot + ratchet + harvester) and it has no
> awareness of what the harvester did."

The V3 TradeCoordinator design — single shared state, single owner of SL,
explicit handoff between harvester partials and the ratchet — is the direct
answer to this session's diagnosis.
