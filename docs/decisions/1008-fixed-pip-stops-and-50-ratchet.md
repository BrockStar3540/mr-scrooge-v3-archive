# 1008. Fixed-pip stops + 50% ratchet (the profitable config)

**Status:** Accepted; preserved in `ORIGINAL_CONFIG.md` as rollback target
**Date:** 2026-03-20 (after the 30m box experiment revert)
**Version scope:** V1
**Backfilled:** 2026-05-11

## Context

The 30m box experiment (Mar 19) introduced 23 commits exploring rolling boxes, zone-anchored stops, equity-% sizing, etc. It broke profitability. The Mar 20 revert restored commit `1c99ae2` ("original profitable version") as the baseline.

During the revert, 17 incidental fixes were kept. The cumulative configuration after the revert + fixes was the empirically-best V1 state. `ORIGINAL_CONFIG.md` preserves it as the explicit rollback target.

## Decision

The V1 profitable configuration:

| Parameter | Value |
|---|---|
| `margin_utilization_pct` | 0.50 (50% equity as margin per trade) |
| `max_concurrent_positions` | 1 |
| `min_risk_reward` | 1.60 |
| `max_eur_positions` | 2 (EUR concentration cap) |
| `zone_proximity_pct` | 0.0025 (0.25% of PDH/PDL) |
| `sl_floor_pct` | 0.0050 (0.50% minimum SL distance) |
| `sl_pips` | 10 (fixed pip stop) |
| `tp1_pips` | 10 (fixed pip TP1) |
| `tp2_pips` | 30 (fixed pip TP2) |
| Harvester T1 | 1.5% equity (~4.5 pips), close 25% |
| Harvester T2 | 3.0% equity (~9 pips), close 25%, SL → +1.5% |
| Harvester T3 | 4.5% equity (~13 pips), close 25%, SL → +3.0% |
| Runner | 25% rides to TP2 (OANDA native) |
| Ratchet Stage 0 | Reconciled trade +5 pips → SL to entry |
| Ratchet Stage 1 | 50% of way to TP1 → SL to entry (breakeven) |
| Ratchet Stage 2 | Price passes TP1 → SL to TP1 level |
| Ratchet Stage 3 | After BE → `max(1H candle_low, entry + 80% × peak, peak − 1.5×ATR)` |

Key principle: **stops and TPs are fixed pips from FILL price**, not zone price. Recalculated post-fill via `modify_trade_stop()` / `modify_trade_tp()`.

## Alternatives considered

- **Equity-%-based stops** — rejected. Drifted across pair classes (JPY vs non-JPY). Pip-normalization gives consistent risk.
- **Zone-anchored stops** — rejected (per ADR 1005). Stop placement must match signal candle anatomy, not arbitrary zone.
- **Wider TPs (e.g. TP1=30, TP2=60)** — rejected. Empirically the 10/30 pip pair was the profitable configuration. Tinkering past the revert point regressed.

## Consequences

**Enabled:**
- A documented, replayable "known good" V1 configuration. If V2/V3 work goes off the rails, `ORIGINAL_CONFIG.md` is the literal rollback target.
- Per-pair consistency in pip-normalized risk.

**Closed:**
- Equity-%-as-primary stop sizing.

## Costs

The fixed-pip approach doesn't adapt to volatility. JPY pair with 50-pip ATR vs EUR/CHF with 8-pip ATR both get SL=10 → very different probabilities of stop-out. Mitigated partly by `sl_floor_pct` (0.50% minimum), but a true volatility-adaptive stop would be a separate ADR (deferred).

V3's `simulate_trade_multi` uses structure-relative stops (`stop_distance = max(structure_offset + 0.25×ATR_pips, spread_floor)`) — a more adaptive approach. The V1 fixed-pip target is preserved as evidence of an empirical sweet spot.

## Cross-references

- `ORIGINAL_CONFIG.md` in `BrockStar3540/mr-scrooge`
- `AUDIT.md` 2026-03-19/20 (overhaul section)
- `[[scrooge-bug-catalog]]` B-040, B-052
- ADR `1005-master-theory-realignment.md` — stop placement at signal candle extreme

---

## Conversation evidence — 2026-03-24 session

Source: `/Users/brock-mini-mac/Dropbox/LLM Sessions/Claude Sessions/trading - Mr Scrooge/2026-03-24_2766c2e9.md`

> **Note for the ADR author.** This session is *not* primarily about
> establishing fixed-pip stops + 50% ratchet (that decision is in the 2026-03-20
> session above). It is about a 4.5-hour diagnostic where V1 stopped entering
> after a 3:32pm ET restart and V2 had silently been losing every entry all day
> due to the same `name 'new_stop' is not defined` bug in `oanda_client.py`.
> The relevance to ADR 1008 is **negative evidence**: it shows why the entry
> path needs to be defensive — silent name-errors in the order placement layer
> can disable the bot for an entire session and still log scoring/regime data
> that *looks* healthy. If ADR 1008 codifies fixed-pip stops + 50% ratchet, the
> closest in-session material is the regime/coordinator follow-on; the
> fixed-pip + ratchet decision itself was made on 2026-03-20 (see ADR 1006
> evidence above).

**Brock's opening question — observed symptom (line ~12):**

> Brock: "what was changed in scrooge around 3pm eastern time, it is no longer
> taking positions"

**The bug (line ~144):**

> Claude: "Found the bug. In `oanda_client.py`, `place_entry_order()` and
> `place_market_order()` both use `new_stop` on their decimal calculation line
> but that variable doesn't exist in those functions — the parameter is called
> `stop_loss`. This crashes every time a trade fires."

**Why it stayed hidden — the dormant-bug principle (line ~168):**

> Claude: "The backup has the same bug — it was already there before 3pm. The
> bot restart at 3:32pm ET is what exposed it (previously there was a live
> position that didn't need to fire new entries, so the bug was dormant)."

**Why V2 had silently produced nothing all day (line ~467, ~489):**

> Claude: "V2 **did** find candidates to fire — GBP_CAD repeatedly, USD_JPY,
> GBP_USD — but the `new_stop` bug was silently crashing every single one of
> those entry attempts all day."

> Claude: "The bug killed every entry attempt — V2 found valid candidates
> (GBP_CAD repeatedly, USD_JPY, GBP_USD) and reached the fire stage, but `name
> 'new_stop' is not defined` crashed each one."

**Brock's framing/principle for the fix flow (line ~323):**

> Brock: "need to fix V2 also"

**Key technical detail — the dormant-bug + silent-crash pattern motivates a
fixed-pip, defensive entry path (the eventual V3 ADR 1008 stance):**
parameter-name errors in `place_entry_order` / `place_market_order` /
`place_opposing_limit` killed every entry without surfacing in the decision
log. The decision-log layer kept showing healthy ranking and regime output —
only the order-placement layer was failing. The takeaway carried forward: the
SL/TP pip structure must be computed in a single, well-tested place so a typo
can't silently disable trading.

**Closest in-session material that touches the ratchet behavior the ADR
codifies (line ~3632, audit of a profitable AUD_CAD trade under the working
fixed-pip + 50% ratchet structure):**

> Claude: "Stop moved to breakeven (0.95823) at 07:01 when price hit 0.96098
> (~50% to TP1) … Closed 07:21 via OANDA native close (TP hit) — **+$2,563.87**"

That is the structure performing as designed once the entry path was no longer
silently crashing — i.e. ADR 1008's structure validated end-to-end on a single
clean trade after the bug was patched.
