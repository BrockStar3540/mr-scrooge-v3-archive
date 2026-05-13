# Box Freshness — Bimodal Diagnostic

Generated: 2026-05-13T03:10:41.637826+00:00

## Verdict: VALIDATION REVERSED

box_age_hours is **NOT an independently useful market-physics signal**. It is a
**proxy for bot-version era**. The previous validation's '+30 WR pt gap fresh vs
stale' is the gap between pre-V3 broker trades (fresh) and V3-era broker trades
(stale), not a market-physics effect.

**ADR rejected on box_age_hours as a filter.** The bimodality has a structural cause,
not an information-content cause.

## What the diagnostic actually found

### H1: Weekend gap — REJECTED

Monday entries are MORE fresh (29 fresh vs 7 stale) — opposite of the weekend-gap
hypothesis. Tuesday similar. Stale skews to Wednesday (14 fresh vs 28 stale).
Weekend gap is NOT the mechanism.

### H2: alt-box ctx_box_age signal — DATA DEAD

`factor_ctx_box_age_hours` is **all zeros** (min=0, median=0, max=0 across 196 rows).
The field exists in the schema but doesn't carry usable alt-box state from the broker
audit. Can't test H2 this way. (Note: same problem with `factor_box_range` — all zeros.)

### H3: Bug-window correlation — REVEALING

| Box age bucket | No bug context | Has bug context |
|---|---|---|
| fresh<48 | 45 | **66** |
| middle_48_168 | 9 | 0 |
| **stale>168** | **76** | **0** |

**ZERO stale rows are in known bug windows. 66 of 111 fresh rows ARE.**

Specifically the fresh-bucket bug context distribution:
- 33 trades had B-074 (alt-box mismatch)
- 30 had B-072+B-074 (UTC midnight amnesia + alt-box mismatch)
- 3 had B-073+B-074 (stale-box absurd TPs + alt-box)

**B-072 (UTC midnight amnesia) LITERALLY CREATES FRESH BOXES.** It resets at
midnight UTC. So the bug exposure positively correlates with fresh box_age. The fresh
trades are partly artifacts of the box bugs.

### H4: repair_taxonomy correlation — STRUCTURAL

| repair_taxonomy | fresh<48 | middle | stale>168 |
|---|---|---|---|
| actual_winner | 40 | 2 | 22 |
| **correct_box_replay_required** | **41** | 0 | **0** |
| **direction_repair_or_skip** | 29 | 7 | **52** |
| management_repair | 0 | 0 | 2 |

**ALL 41 contaminated (box-bug) rows are fresh.** **52 of 88 V3-era direction_repair_or_skip**
rows are stale. The bucket is essentially capturing bot-era, not market state.

### H6 (key): bot_actual_strategy × bucket — SMOKING GUN

| bot_actual_strategy | fresh<48 | middle | stale>168 |
|---|---|---|---|
| **direct** | **0** | 0 | **27** |
| **dbb_trend** | **0** | 0 | **16** |
| **unknown** (pre-V3-strategy era) | **111** | 9 | **33** |

**ZERO of the 43 V3-named-strategy trades (direct/dbb_trend) are fresh.** All 43
have box_age > 168h. Conversely, ALL 111 fresh trades have `bot_actual_strategy = unknown`
(the pre-V3-strategy era when the bot didn't yet label trades).

**This is definitive: fresh-vs-stale is bot-era, not market-physics.**

### Time-period split confirmed by repair taxonomy

- fresh<48 = pre-Apr-13 broker trades (in bug-window era, often contaminated)
- stale>168 = post-Apr-13 V3-era trades (post-bug-fix era, no bug exposure)

## The TRUE finding

The bimodal distribution is the **fingerprint of V3's new box code persisting boxes
longer than V2's did**. Specifically:

- **Pre-V3**: B-072 (UTC midnight amnesia) literally reset boxes daily. Plus other
  bug-era code that recomputed frequently. Box_age values clustered <48h.

- **V3**: post-bug-fix box code holds boxes for days/weeks. Min box_age in this
  population is 168h+ = 1+ week. Max is 428h = 17.8 days. This means V3 is either:
  - Genuinely waiting for a fresh box-formation event (rare market structure)
  - Or stuck on a stale reference that should have been recomputed

## The actual structural concern

**V3 box_age values of 168-428 hours (1-18 days) are suspicious.** Box-fade strategies
typically assume boxes form on daily price action (PDH/PDL from the prior day).
A box that's 18 days old is NOT yesterday's box — it's old structure that may not
represent current market liquidity walls.

This is a **code question** about V3's box logic, not a market-physics filter question.
Possible explanations:
- V3 may be using a 'first-touch' or 'session-anchored' box that persists once formed
- Alt-box logic (per B-074) may be holding an old reference
- The bot may be intentionally tracking weekly/monthly walls (not daily)
- Or: V3 has a real bug where boxes don't recompute

**The bot's WR drop in V3 era could be partly explained by trading off boxes that
are too old to be relevant.** That's a hypothesis worth confirming via V3 code review.

## What this changes

- `box_age_hours` filter: **REJECTED**. Not an independent signal. Don't ADR.
- The Step 8 'box_age is strongest signal' interpretation: **DEMOTED**. It was a
  bot-era proxy, not a market-physics signal.
- The +30 WR pt gap: **explained**. Pre-V3 trades happened in different market
  conditions / different probes / different bug exposure than V3 trades. Apples-oranges.

- **NEW V3 code concern surfaced**: V3 box_age values cluster 168-428 hours. If V3
  is supposed to use daily-anchored boxes, those values are too high. Worth a code
  review of V3's box-formation logic.

## What this VALIDATES about the methodology

Brock's correction was exactly right: **'if box_age is actually a proxy for two
different box code paths, then the whole freshness filter interpretation changes.'**

The diagnostic took ~30 minutes and prevented an ADR that would have implemented a
filter measuring bot version rather than market physics.

## What's queued (per scope)

- **V3 box-code review**: why are V3 box_age values 168-428h? Is the box recomputing
  on the expected cadence? This is a structural fix, not a filter.
- **Re-run Step 8 factor synchrony WITHIN bot-era** — split fresh (pre-V3) vs stale
  (V3-era) and ask: do other factors STILL show synchrony when you remove the
  bot-era confound? Box_age was just the strongest false positive. Other factors
  may have similar issues.
- **Sister-factor independence tests** on `wall_proximity`, `current_volume`,
  `spread_pips` — apply the same diagnostic. They MIGHT also be bot-era proxies.
- **Then ADR consideration** for whichever factor survives the era-split test.