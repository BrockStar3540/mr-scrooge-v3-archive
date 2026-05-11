# 2002. Dual-loop execution architecture

**Status:** Accepted (shipped in both V1 and V2 simultaneously on 2026-04-03)
**Date:** 2026-04-03
**Version scope:** V1 and V2 (cross-version pattern)
**Backfilled:** 2026-05-11

## Context

The bot ran on a 5-minute decision cycle (M5 candles). But once a trade was open, certain actions needed faster response:
- Stop-loss limit placement when price approaches SL (needs sub-minute reaction)
- SL-limit fill monitoring (a fill closes the position immediately)
- Fast-market detection (don't place SL-limit during a flash candle expansion)

5-minute cadence was too slow for these. But the decision loop (signal evaluation, entry candidate ranking, gate evaluation) is correctly paced at 5 min — faster would just retry identical work.

## Decision

Split the bot into a **dual-loop architecture**:

| Loop | Cadence | Responsibility |
|---|---|---|
| **Slow loop** | 5 min (candle-anchored) | Decisions: scan, signal evaluation, gates, entry candidate ranking |
| **Fast loop** | 3 sec (daemon thread) | Execution: SL-limit placement, fill monitoring, fast-market detection |

Implementation:
- `threading.Lock` (`_exec_lock`) prevents race conditions between loops
- `_cached_bars` dict stores latest `bars_5m` from slow loop; fast loop reuses without refetch
- Fast loop fetches live prices via single batch `get_prices(symbols)` call per cycle
- Position management loop in slow loop wrapped with `with _exec_lock:`
- Dead position guard: existence check before `_manage_sl_limit` in fast loop
- Log tag: `[FAST_LOOP]` on thread start and errors

Shipped simultaneously in V1 (`main.py`) and V2 (`coordinator.py`) on 2026-04-03.

## Alternatives considered

- **Single 3-second loop doing everything** — rejected. 5-minute decisions firing every 3 seconds is wasted compute (no new candle).
- **Polling at adjustable cadence based on position state** — rejected as over-engineered.
- **Use OANDA's streaming endpoint** — explored, but adds infrastructure complexity (long-lived connection, reconnect logic) without proportional benefit at this scale.

## Consequences

**Enabled:**
- SL-limit system (ADR-adjacent, see NOTES.md 2026-04-03) — proactive REDUCE_ONLY limits near stop
- Fast-market detection skips limit placement when candle range ≥ `fast_mult × avg`
- Cleaner reasoning about which thread owns which state at which moment

**Costs:**
- Lock contention: if slow loop holds `_exec_lock` too long, fast loop is starved. Mitigated by keeping slow loop's lock window short (just position management).
- More state to reason about (bars cache, price cache, lock).

## Architectural note

NOTES.md from 2026-04-03 frames it: **"This is the same pattern used in professional trading systems."** The 5-min decision / 3-sec execution split is industry-standard.

## Survival into V3

V3 currently has a unified runtime cadence (research mode replay context, not live trading). When V3 returns to live execution, this dual-loop pattern is the architectural target.

## Cross-references

- `NOTES.md` 2026-04-03 section in `BrockStar3540/mr-scrooge`
- ADR `1010-trade-coordinator-multi-actor.md` — TradeCoordinator was the cross-loop sync primitive added 7 days later
