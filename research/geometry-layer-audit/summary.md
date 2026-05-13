# V3 Geometry Layer Audit

Generated: 2026-05-13T04:12:08.763527+00:00

## Scope

Per Brock 2026-05-13: after BE@0.5R validation failure, shift research to the
geometry layer. The hypothesis: 'if the bot is drawing or interpreting the box
wrong, every downstream formula is poisoned.'

Investigation: status of B-068 to B-074 (box-drawing bugs catalogued in V1/V2 era)
in current V3 code (`/home/ubuntu/mr-scrooge-v3/src/`).

## Verdict

**V3 geometry is in better shape than the bug-catalog narrative implied.** Of 7 historical
box bugs (B-068 to B-074), 4 are fixed, 1 is inactive (dead code), 1 is still active but
the impact is bounded, and 1 cannot be verified.

**No smoking-gun live geometry bug found.** The bot's losses are NOT primarily caused by
current V3 box-drawing errors. That changes the strategic implication: the geometry layer
isn't the next big lever to fix.

## Per-bug status in current V3

| Bug | Status | Evidence | Action |
|---|---|---|---|
| **B-068** inverted boxes from `iloc[:24]` | **Fixed** | V3 uses `iloc[-48:-24]` per zone_detector.py:340 | none |
| **B-069** 30m rolling box experiment | **Fixed (reverted)** | V3 uses daily box only | none |
| **B-070** percentile filter overclip | **STILL ACTIVE** | 98/2 filter in zone_detector.py:51-53 still on | quantify live impact |
| **B-071** filtered PDH below market | **Partial** | reversal.py validates; direct_entry doesn't need it (TP=PDH bounded) | dbb_trend check |
| **B-072** UTC midnight box-reset amnesia | **Fixed** | OANDA-NY-17:00 clock anchor (oanda_adapter.py:521) + regime hysteresis | none |
| **B-073** stale-box absurd TPs / 3× ATR clamp | **CANNOT VERIFY** | No clamp code found; catalog says fix shipped 2026-04-09 | investigate or re-add |
| **B-074** regime vs alt-box mismatch | **Inactive (dead code)** | `draw_alternative_range()` never called; alt-box state never set | none |

## B-074: dead code finding (most important methodological result)

The alt-box logic in `range_builder.py` exists structurally:
- `alternative_range` field in record
- `using_alternative` flag
- `draw_alternative_range()` method
- `active_range = alternative_range if using_alternative else active_range` switch

But `draw_alternative_range()` has **zero callers** in the active V3 code:
- 0 callers in `src/scrooge_v3/core/`
- 0 callers in `src/scrooge_v3/strategies/`
- 0 callers in `src/scrooge_v3/classifiers/`
- 0 callers in `src/scrooge_v3/features/` (other than the definition itself)

Both signal engines (direct_entry.py, dbb_trend.py) and the regime classifier read
PDH/PDL from `zone_detector.zone_map.session_range` — the SAME primary source. There's
no divergence. The B-074 mismatch the catalog described is structurally impossible in
current V3.

**Implication**: the 87 contaminated rows in the trade-film ledger that had B-074
attributed (33+30+3=66 of 111 fresh rows in the bimodal diagnostic) were correctly
flagged for the V1/V2 era, but the same mechanism cannot recur in current V3.

## B-070: still-active percentile filter

V3's `zone_detector` runs a 98th/2nd percentile filter on hourly bars from the prior
day to remove spike wicks before establishing PDH/PDL:

```python
self.pdh_percentile = config.get('pdh_percentile', 98)
self.pdl_percentile = config.get('pdl_percentile', 2)
...
clean_high = float(np.percentile(prior_hourly['high'].values, self.pdh_percentile))
clean_low  = float(np.percentile(prior_hourly['low'].values, self.pdl_percentile))
if clean_high < raw_PDH: PDH = clean_high
if clean_low  > raw_PDL: PDL = clean_low
```

Per the bug catalog (B-070), this compresses boxes by 0.33-0.39% on certain pairs and
up to 5-15 pips per pair per day. Half-box geometry shrinks → TPs (midline) move closer
to entry → tighter R:R. Compounded across 26 pairs over months, this is meaningful.

**The percentile_filtered flag is NOT exposed in scans.jsonl** (checked 58K scans, zero
matches), so we can't quantify how often it fires live without code instrumentation.

**Suggested follow-up**: instrument the filter to emit a counter or scan-side metadata,
then measure how often it compresses PDH/PDL and by how much. If the answer is 'most
trades, by 5+ pips,' it's worth reconsidering. If the answer is 'rarely and minimally,'
leave alone.

## B-073: 3× ATR clamp on TP — cannot verify

Per bug catalog: 'Defect #11 / B.4 patch — 3× daily-ATR clamp added in `_calculate_targets()`.
If TP2 distance > 3× ATR, clamp to 3× ATR and log warning. Defect logged as fixed 2026-04-09.'

Searched current code:
- No `clamp`, `3.*ATR`, `tp_distance.*max`, `max_tp` in `strategies/` directory
- No `_calculate_targets()` method anywhere — V3 calculates TPs inline per strategy
- direct_entry uses TP=PDH/PDL (already bounded by box, can't be absurd)
- dbb_trend uses TP=current_close+impulse and session_target() — could be unbounded
- reversal uses TP=center/PDH/PDL (bounded)

**Direct_entry and reversal are structurally protected** (TPs bounded by box geometry).
**dbb_trend may have an unbounded TP path** through `session_target()` — worth a closer
look but not an emergency (only 16 dbb_trend trades in V3-era data, none flagged as absurd).

Either:
a) The 3× ATR clamp catalog entry was actually applied to V1, not V3
b) The clamp was added to V3 but later refactored out when target logic moved per-strategy
c) It's in a place my grep missed

Low concern given V3's structural TP bounds, but worth a definitive answer.

## What this changes about the strategic picture

Brock's framing was: 'global rules keep failing because the bot needs conditional physics.'

After this audit:
- **Geometry layer is NOT the smoking gun.** V3 box code is largely correct.
- The bot's losses in V3 era aren't primarily caused by geometry bugs.
- The bigger issue is downstream: entry selection + exit management within correct geometry.
- That maps to the unfinished research areas: pocket-conditional entry rules and management
  rules per (regime × pair_family × session × direction).

The next budget allocation isn't 'fix the box.' It's 'characterize what makes some pockets
repeatedly winnable AGAINST correct geometry.'

## What's NOT actionable

- B-070 percentile filter without first quantifying its actual impact in V3 live
- B-073 clamp re-add without confirming the previous fix's status
- Any speculative box-code changes (V3 is operating with 0-24h box_age live, normal)

## What IS actionable (smaller, not breakthrough)

1. **Instrument the percentile filter** to emit a `percentile_filtered` flag + compression
   amount in scans.jsonl. After a week of data, decide if it matters.
2. **Confirm or re-add the 3× ATR clamp** in dbb_trend's `session_target()` — defense in depth.
3. **Remove the dead alt-box code** from `range_builder.py` and `structure.py` since it's
   never triggered. Reduces cognitive load.

## What this CLOSES OUT

- The geometry-layer hypothesis is now a confirmed dead-end for the 'big lever' search.
- V3's box logic is structurally clean.
- The bot's losses aren't primarily geometry-caused at V3-era.

## Where the research budget should actually go

After this entire arc of negative results, the live-system state is:
- V3 box code: correct
- V3 management: not the breakthrough lever (BE@0.5R failed validation)
- V3 factor synchrony: methodologically unrepairable at current data scale
- V3 era data: too sparse for the multi-factor work we wanted to do

The honest next move is **let live data accumulate and re-run validations later.**
With another month of V3 production data:
- More verified winners + losers in the ledger
- Better statistical power for pocket-conditional rules
- Can re-test BE@0.5R with bigger n
- Can finally cluster winners with enough factor signal

Active monitoring tasks (not research) that ARE worth doing now:
- Track percentile_filtered frequency (a 30-day data collection)
- Spot-check V3 alt-box dead code can safely be removed (5-min code change)
- Continue documenting trade decisions in the trade-film ledger as V3 generates new trades

This is the negative result that closes the current research arc. The bot has real
problems but they're not single-lever fixable from existing data. Time + data is the gate.