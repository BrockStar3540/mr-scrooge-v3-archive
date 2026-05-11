---
type: research-proposal
status: proposed
tags: [scrooge, backtest, sampling, methodology, v2-corpus]
date: 2026-05-11
trust: medium
evidence:
  - scrooge-evolution-timeline.md
  - scrooge-bug-catalog.md
  - ORIGINAL_CONFIG.md (V1 profitable parameters)
  - SCORING_V3.md (V1/V2 scoring methodology)
---

# Backtest Sampling Proposal — informed by V1/V2 archive

A proposal for how to slice the v2 corpus output (when it completes ~2026-05-12) and future backtest runs, informed by what we now know about the bot's evolution. Built from the V1 archive (50-commit GitHub history + Dropbox daily notes + Feb 2026 doctrine doc + ORIGINAL_CONFIG.md).

This is methodology, not compute. The proposal answers: **given a single v2 corpus result, what cuts do we make and what do those cuts tell us?**

## Why this matters

The v2 corpus is running ~1.5M hypothetical trades across 2019-2026 with v3 probe logic. The live bot didn't exist for most of that span and produced very different trade quality across its short lived history. A single aggregate truth table averages across many incompatible regimes — both market regimes AND bot regimes.

The V1 archive gives us **dated boundary lines** we couldn't see before:

| Boundary | Date | What it separates |
|---|---|---|
| Bot v1 birth | ~2026-02-15 | Bot exists ↔ Bot doesn't |
| Performance cutoff | 2026-03-04 23:00 UTC | Pre-fix noise ↔ Auditable performance (ADR 1007) |
| MASTER_THEORY realignment | 2026-03-11 | Invented rules ↔ Transcript-faithful rules (ADR 1005) |
| Green-exit redesign | 2026-03-12 | Reactive market exits ↔ SL-advancement only (ADR 1006) |
| 30m experiment / revert | 2026-03-19/20 | Failed experiment ↔ Profitable baseline restored |
| Sprite removal | 2026-03-25 | Multi-bot complexity ↔ Forex-only focus |
| V2 modular rewrite | 2026-03-21 | Monolithic V1 ↔ Modular V2 (ADR 2001) |
| Dual-loop architecture | 2026-04-03 | Slow-only ↔ 5min decisions + 3sec execution (ADR 2002) |
| TradeCoordinator | 2026-04-10 | 4-actor race ↔ Shared state (ADR 1010) |
| V3 scoring system | 2026-04-15 | Old scoring ↔ WR-Lift Hybrid (ADR 2003) |
| V1 retired | 2026-04-15 | V1 code ↔ V3 codebase begins |
| Attribution fix | 2026-05-04 06:38 UTC | strategy=unknown noise ↔ Deterministic attribution (B-064) |

## Three sampling cohorts the corpus output should support

### Cohort A — Bot-era cuts (for understanding V3 logic vs historical bot behaviour)

Slice the v2 corpus output by **what the LIVE bot was doing at the same calendar time** as each trade:

| Slice | Date range | Live bot context |
|---|---|---|
| **Pre-bot** | 2019-07-01 → 2026-02-15 | No bot existed; pure market data |
| **V1 pre-cutoff** | 2026-02-15 → 2026-03-04 | Bot existed but was bug-laden |
| **V1 pre-MASTER_THEORY** | 2026-03-04 → 2026-03-11 | Invented rules era |
| **V1 post-MASTER_THEORY** | 2026-03-11 → 2026-03-12 | Theory-faithful, before green-exit redesign |
| **V1 post-green-exit-fix** | 2026-03-12 → 2026-03-19 | SL-advancement-only era begins |
| **V1 30m experiment** | 2026-03-19 → 2026-03-20 | Strategy broken |
| **V1 profitable window** | 2026-03-20 → 2026-04-03 | The ORIGINAL_CONFIG era (fixed-pip stops, 50% ratchet) |
| **V1.5/V2 bridge** | 2026-04-03 → 2026-04-15 | Dual-loop, TradeCoordinator, V3 scoring deploying |
| **V3 pre-attribution** | 2026-04-15 → 2026-05-04 | V3 architecture, unreliable strategy attribution |
| **V3 post-attribution** | 2026-05-04 → 2026-05-12 | Trustworthy V3 trade data |

**Use:** Compare v3-probe-implied performance on the same days the live bot was running. Where there's overlap, divergence tells us: are v3 probes missing what the bot caught? catching what the bot missed?

**Caveat:** v3 probes never ran live in 2019-2024. So those slices are pure hypothetical. The bot-era cuts only apply 2026-02-15 onward, and only for ~3 months of overlap.

### Cohort B — Market-regime cuts (already implemented as discovery/holdout)

The locked Stage 5 discipline splits at 2026-01-01:
- Discovery: 2019-07-01 → 2024-12-31 (~5.5 years)
- Holdout: 2025-01-01 → 2026-04-22 (~16 months)

**Refinement proposal:** add a third explicit split at a known macro pivot. Candidates:
- 2020-03 (COVID volatility spike)
- 2022-01 (Fed rate-hike regime begins)
- 2024-09 (Fed pivot / rate-cut era)

A finer split lets us see if cells that survive holdout also survive the 2022 rate-hike regime, or whether holdout success is a 2025-low-vol artifact.

### Cohort C — Config-replay cuts (use V1 archive parameters)

This is the high-leverage idea the archive surfaces. ORIGINAL_CONFIG.md preserves V1's *empirically profitable* parameter set. We can replay the v2 corpus output through V1's stop/TP geometry to compare.

| Variant | Stop | TP1 | TP2 | Management |
|---|---|---|---|---|
| **Baseline (current v2)** | Structure-relative + spread floor | 1.5R | 2.0R | None (timeout 48h) |
| **V1 fixed-pip** | 10 pips | 10 pips | 30 pips | 50% ratchet at 5p BE |
| **V1 hybrid trail** | structure-relative | 10 pips | trail to peak − 1.5×ATR | Hybrid trail after BE |
| **V1 profile-tiered** | per-pair-class | (tight 2p / med 4p / wide 6p) | varies | Per-tier (NOTES.md 2026-04-03) |

**Implementation:** the v2 corpus output stores `feature_snapshot` (full V3 features at entry) and `entry_ts` per trade. We can re-walk forward bars at any historical entry under any management variant **without re-doing the entry decision**. That's exactly what `simulate_trade_multi` was designed for.

The output: a `(cell, management_variant) → realized_r` matrix. For each surviving v2 cell, which management variant maximizes sum-R? Does V1's fixed-pip outperform v3's universal-R on the high-volatility cells?

## Concrete first-cut analyses (in priority order)

### Priority 1 — V1 config replay on v2 corpus survivors

**When:** After v2 corpus aggregator produces survivor list.
**How:** For each surviving `(regime, probe)` cell:
1. Replay forward bars under V1 fixed-pip (10p SL / 10p TP1 / 30p TP2 + 50% ratchet at 5p BE)
2. Replay under V1 hybrid trail (peak − 1.5×ATR after BE)
3. Compare sum-R against v2 universal 1.5R/2.0R
4. **If V1 fixed-pip beats v3 by > 0.2R/trade**, the V3 walker may be giving up signal the V1 management captured.

**Cost:** Single-pass forward walk per trade, no new feature compute. ~30 min on existing v2 ledger.

### Priority 2 — Bot-era overlap for V3 post-attribution

**When:** v2 corpus done + live broker audit (already done).
**How:** Take the 43 V3 post-attribution-fix trades from the live audit. Cross-reference each with the v2 corpus on the same `(symbol, entry_ts)`:
- Did v2 probes also classify those bars in the same regime?
- Did v2 probes fire at the same entry timestamp?
- If v2 said "skip" but the bot said "take", what did v2 imply was the better alternative?

This is the cleanest A/B between v2 hypothetical and v3 actual.

**Cost:** No new compute. CSV math.

### Priority 3 — Market regime sub-splits

**When:** Optional, after Priorities 1+2.
**How:** Slice discovery into pre-2022, 2022-2024 (rate-hike), 2024+ (rate-cut). Recompute aggregator gates per sub-split.

If a cell passes in 2025+ but fails in 2022, the cell is rate-regime-dependent. Helpful for live deployment risk: don't enable a cell whose evidence is dominated by one rate regime when conditions are reversing.

**Cost:** Re-run aggregator with different date filters. ~10 min.

### Priority 4 — Reintroduce V1 strict pitchfork thresholds

**When:** After Priority 1 establishes whether V1 management beats v3.
**How:** v3 probes have loose wick-rejection (e.g. `lower_wick ≥ body`). V1 had explicit thresholds (wick ≥ 60% of range, body ≤ 30%, wick ≥ 2× body). For each v2 surviving cell, simulate a stricter variant.

**Hypothesis:** v3 may have given up signal quality for fire-rate. Tighter pitchfork conditions on `echo_box_fade_v2` could improve win rate at the cost of trade frequency.

**Cost:** Smoke-test on each cell's existing trade pool. Probably ~30 min.

### Priority 5 — Re-entry protocol on liquidity sweep

**When:** Last in line; V1 had this and V3 doesn't.
**How:** For each v2-trade that hit SL, check if a re-entry within 30m at the same zone would have produced a winner. V1 allowed `max_reentries_per_setup = 3` (per ADR 1005). V3 walker has no re-entry concept.

**Hypothesis:** Adding re-entry to V3 walker could recover a meaningful R-fraction on cells where SL is "liquidity sweep" rather than thesis failure.

**Cost:** Forward-walk per SL trade. Maybe 1-2 hours on the full corpus.

## Priority 6 — Box-contamination exclusion zones (discipline rule, not a test)

Added 2026-05-11 from Claude-sessions archive sweep. Full forensic in [[scrooge-box-bugs-and-validation-targets]]; catalogued as B-068 through B-074 in [[scrooge-bug-catalog]].

The box is the foundational reference. Seven distinct box-drawing failures across V1/V2 mean entire windows of "live truth" comparison data are unreliable. **These windows must be excluded** from any backtest that compares simulated PnL against live PnL:

| Exclude | Reason | Bug |
|---|---|---|
| Pre-2026-03-09 EUR-pair longs | Inverted boxes (PDL > PDH), wrong-direction entries | B-068 |
| 2026-03-19 evening → 2026-03-20 afternoon | 30m rolling box experiment broke profitability | B-069 |
| First ~2h of every UTC day from regime activation (~03-22 V2 / ~03-31 V1) → 2026-03-29 fix, for pairs BLOCKED in prior 24h | Box-reset amnesia → fake +1 score on bad setups | B-072 |
| 2026-03-31 → 2026-04-09 USD/CHF + GBP/CAD entries | Stale-box absurd TPs (7,883+ pips) | B-073 |
| All `signal.score == 1` entries through 2026-04-13 | Regime vs alt-box mismatch → fake-valid scores at the floor | B-074 |
| 2026-03-24 → V1/V2 lifetime, all longs with filtered PDH < current market | Percentile filter overclip → OANDA rejections / compressed TPs | B-070, B-071 |

**Clean filter for any "score-as-conviction" replay:** `signal.score >= 20`. This preserves the documented winners while killing the known-contaminated `score==1` cohort.

## Priority 7 — Validation-target winning sessions (replay these or you're worse)

Three documented "good day" sessions from the V1/V2 era. Any proposed config change should reproduce these. **If a candidate config does NOT also win these days, it's a regression — independent of whatever it does on the broader corpus.**

### 7a — 2026-04-07 V1 antipodean complex (+$74.17 / 5 winners + 1 SL)

5 wins, 1 loss, 1 open. Net closed +$74.17 on ~$1,669 equity (~+4.4% day).
- AUD_JPY long +$27.98, NZD_USD short +$4.08 / +$4.29, AUD_USD long +$5.09 / +$46.92, AUD_CHF long -$14.19
- Power_of_towers signal on 5 of 7 trades. Harvester took partials on the +$46.92 winner.
- Config: V1 post-`3f14762e` (B-054 fixed), pre-04-09 TP clamp. Standard daily box drawing.
- **Window to replay:** 2026-04-07 04:00 → 22:00 UTC across AUD/NZD/JPY pairs.
- **Why it works (hypothesis):** clean regime fit — directional JPY-cross flow + risk-on antipodean strength fading to box edges. The bot was structurally right for the day.

### 7b — 2026-03-23 V2 CAD-cross winners (+$5,654 across 3 trades)

- AUD/CAD +$2,564 (single biggest trade of V1/V2 era), CAD_JPY +$2,627, GBP/CAD +$463
- Config: V2 ~$88K practice. Regime supervisor in observe-then-half-size mode. RESTRICTED entries at half size. Post-B-068 box fix.
- **Window to replay:** 2026-03-23 15:00 → 18:00 UTC.
- **Macro setup:** CAD-cross strength + USD weakness. Bot caught it 3 times. Validates the box+regime stack when both are right.

### 7c — 2026-04-10 V1 score>1 cohort all winners

- GBP/USD +$8.52 (score 44), NZD/JPY +$2.14 (score 51), NZD/JPY open +$32.23 (score 31). Three of three.
- The two score=1 trades that day (AUD/CAD +$4.22, USD/MXN -$40.41) are the B-074 contamination cohort — exclude.
- Config: V1 post-04-09 TP clamp, regime active.
- **Replay test:** apply `signal.score >= 20` filter to candidate config. Should enter only the 3 winners; should NOT enter the score=1 trades.
- **Validates:** the score threshold itself, not just the trade-by-trade replay.

### What "passes validation" means

For each candidate config (V1-replay, ATR/OTR re-enable, ratchet/TP1 sweep, etc.):

1. Run on the 3 validation windows above.
2. Compute: did the same direction-correct entries fire? Did SL/TP placement keep them as winners? Net P/L for the window?
3. **Hard floor:** at least 2 of 3 windows must turn green, and 7a must produce ≥3 of the 5 documented wins.
4. **Soft floor:** any config that improves discovery but loses validation is a tradeoff to be flagged explicitly, not auto-promoted.

This is not a substitute for the existing aggregator gates (density / CI / concentration / diversity). It's an additional pass-or-fail check on top.


## What NOT to do

These are tempting but low-yield given current state:

- **Re-run v2 corpus with different probe parameters.** Wait for the current run to finish first. The marginal info from a parameter sweep is small relative to a 57-hour cost. If a probe needs tuning, do it as a targeted smoke (10-30 min) on the existing audit's candidate set.

- **Build a "V3-on-live-bot-trades-only" backtest.** Tempting because it answers "what if v3 had been live?", but unsound — V3 with 100% hindsight (knowing the next bar) outperforms anything fair. The post-attribution audit (which is what this would be) is already done with proper window-search methodology.

- **Optimize the V3 scoring formula directly.** ADR 3001 closes this direction. Per-strategy ML is allowed as a satellite (dbb_trend AUC 0.774); global score is rejected.

## Cross-sampling discipline (locked rules)

If implementing any of the above:

1. **Don't change the existing aggregator gates** (Stage 5 density / CI / concentration / diversity floors). Add new filters on TOP of survivor lists, not as replacements.

2. **Don't peek at holdout** when comparing management variants on discovery. If V1 fixed-pip beats v3 universal-R on discovery, that's a hypothesis for holdout to validate — not a conclusion.

3. **Use the bug catalog as a sanity guard.** Many "performance differences" between eras are explained by known bugs (B-064 attribution, B-054 silent skip, B-055 46-call spam). Cross-reference before drawing strategy conclusions.

4. **Preserve V1 era boundaries verbatim.** If a cell's performance differs between V1-pre-cutoff (B-021 concurrent instances) and V1-post-cutoff, that's a bug-era artifact, not a strategy signal.

## Open questions this proposal doesn't answer

1. **Spread-adjusted vs raw R** — v2 corpus uses raw R (no spread cost in walker). V1's OTR ratio was explicit cost-aware. Should the aggregator's CI gate use spread-adjusted R for the live-realistic comparison?

2. **Per-pair-class management** — V1's 3-tier pair profiles (tight/medium/wide) had per-pair stop trigger / offset. v3 has uniform. Worth ADR-ing as a Priority-4 candidate variant?

3. **Re-entry as first-class** — V1 had it (capped at 3/setup, ADR 1005), V3 doesn't. Is this a feature gap or a deliberate v3 simplification?

These are inputs for whichever priority lands as the next compute pass after the v2 corpus completes.

## Cross-references

- [[scrooge-evolution-timeline]] — era boundaries for Cohort A
- [[scrooge-bug-catalog]] — cross-reference for cohort-explained anomalies
- [[v2-post-audit-state-2026-05-10]] — current state-of-union
- [[v2-corpus-run-manifest-2026-05-10]] — locked run spec (Stage 5 gates)
- `mr-scrooge-v3/docs/decisions/1008-fixed-pip-stops-and-50-ratchet.md` — V1 management variant
- `mr-scrooge-v3/docs/decisions/2002-dual-loop-architecture.md` — V1.5 per-pair tiering source
- ORIGINAL_CONFIG.md in `BrockStar3540/mr-scrooge` — V1 profitable config (replay source)
