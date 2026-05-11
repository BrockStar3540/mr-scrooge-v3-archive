---
type: dead-ends-catalog
status: living
tags: [scrooge, dead-ends, rejected-ideas, reverted-experiments, possibly-wrong-fixes, institutional-memory]
date: 2026-05-11
trust: high
evidence:
  - 19 Claude session transcripts (Mar 9 - Apr 13, 2026)
  - AUDIT.md + NOTES.md from V1 repo
  - GitHub commit log
---

# Mr. Scrooge — Dead Ends Graveyard

The catalog of ideas that *didn't* make it into the bot — or did, but possibly shouldn't have. Different from the bug catalog (which is fixes for problems) and the ADRs (which are decisions standing today). This is the **rejected, the reverted, and the doubtful**.

Critical framing: **some applied fixes could have been wrong.** Some abandoned ideas might have been correct. The bot's current state is a path through a much larger decision tree, and the rejected branches contain lessons + reconsideration candidates.

## Why this exists

When current research surfaces a question like "what if we had used X instead?", this note answers "X was tried/proposed, here's what happened and why we chose Y." Saves re-running discarded experiments. Also flags fixes worth empirically testing for whether they were right.

## How to use

- **Investigating an old decision:** check Category 1 (rejected) or Category 2 (reverted) for similar prior thinking.
- **Considering reverting a fix:** check Category 3 (possibly-wrong fixes) for evidence + test design.
- **Reconciling a parameter discrepancy:** check Category 4 (ping-pong) for value history.
- **Reading Claude session transcripts:** Category 5 indexes explicit self-corrections by Claude — good ground truth for "we tried this and it was wrong."

---

## Category 1: Proposals rejected at conversation time

Ideas considered but not adopted.

### 1.1 OTR gate — widen instead of demote

**Date:** 2026-03-11 (MASTER_THEORY audit session)
**Proposer:** Claude (in 2026-03-11_d66ae964.md, line ~2638)
**Proposal:** "Medium: OTR gate — demote **or widen threshold**" — widening (raise `otr_marginal` from 0.25 to a higher value) was offered as an alternative to demoting.
**Why rejected:** MASTER_THEORY had no OTR gate at all. Widening would keep the invented rule; demoting brought it closer to advisory.
**Worth reconsidering?** Yes if the live broker audit shows v3 probes producing entries that V1's OTR gate would have caught as cost-inefficient. Live data shows 196 trades with -56R; some of those losses might be OTR-flag-worthy.

### 1.2 Rolling 30m box experiment — claude pushed back, user proceeded

**Date:** 2026-03-19 (2026-03-19_4ac1dfc3.md, line 3483)
**Initial Claude position:** *"A 30-minute box would still reset 48 times a day. The levels carry no special meaning to other participants — they're arbitrary slices of time."*
**What changed:** Claude then suggested an alternative: rolling 8-16 thirty-minute bars (the "last 4-8 hours" as the box). User adopted.
**Outcome:** Failed within 24 hours. Reverted Mar 20.
**Worth reconsidering?** The original Claude pushback was correct — arbitrary time slices have no order-cluster basis. The alternative ("rolling 8-bar 30m as the box") still had the same conceptual problem. **Don't reconsider this; it's the canonical example of "Claude was right the first time."**

### 1.3 Keep Mr. Sprite (don't remove entirely)

**Date:** 2026-03-25 (sessions `559a3c94` + `b7895d34`)
**Proposal:** Multiple "disable" verbs in the conversation (disable for breakout/trend, disable overlapping control, disable stagnant timeout). At least implicitly: keep Sprite running with selective disabling vs full removal.
**Why rejected:** Maintenance cost > expected value. Per ADR 1009.
**Worth reconsidering?** Yes if crypto market conditions change AND we have spare attention. The Feb 26 doctrine had explicit Kraken fee tier modeling and 20 crypto pairs catalogued. A clean restart with a separate codebase would carry less cost than maintaining a forked V1.

### 1.4 Stop loss recalculated from fill (TWO mechanisms identified)

**Date:** 2026-03-20 (revert session `1c92abef`, lines 242-258)
**Two competing mechanisms proposed** for why the 30m + fill-anchored stops broke the bot:
- Mechanism A: "Stop loss recalculated from fill price — discards the zone-based stop and instead sets it 10 pips from the fill price. This puts the stop INSIDE the box, causing it to be hit by normal price noise."
- Mechanism B: separate from the 30m geometry itself
**Resolution:** Both mechanisms were unwound together; not clear which was the dominant culprit.
**Worth reconsidering?** Yes — the revert tossed both potentially-good and potentially-bad changes together. Mechanism A's specific argument (stop inside box) is testable. v3 probes use structure-relative stops; might revisit fill-anchored variants once v2 corpus survivors are identified.

### 1.5 Keep TP1 = 5 pips, change ratchet logic instead

**Date:** 2026-03-20 (line 2057-2083)
**The exchange:** *"Ah — you want to keep the 50% ratchet behavior but make it work correctly. So instead of changing the ratchet logic, change TP1 to 10 pips."*
**Two paths existed:** (A) keep TP1=5, modify ratchet to trigger at fixed pip distance, or (B) keep ratchet logic (50%-to-TP1), change TP1 to 10 to get +5 pip BE trigger. Chose B.
**Worth reconsidering?** A would have decoupled TP1 sizing from BE trigger. Possibly more flexible for different volatility regimes. Live broker audit could reveal whether TP1=5 with explicit-pip ratchet trigger outperforms TP1=10 with 50% logic.

### 1.6 In-memory shared state for actor coordination

**Date:** 2026-04-10 (TradeCoordinator session, alternatives implicit)
**Proposal:** Multi-actor coordination via Python `multiprocessing.Manager` (in-memory).
**Why rejected:** Process boundaries didn't align with actor boundaries. Bot, fast loop (separate thread), and harvester (separate process) couldn't all share a Manager instance cleanly.
**Worth reconsidering?** In V3's single-process architecture (per-runtime), in-memory state IS viable. The file-backed approach is V1-era constraint. V3 may not need it.

### 1.7 OANDA streaming endpoint for live prices

**Date:** Implicit in 2026-04-03 fast-loop design (NOTES.md)
**Proposal:** Use OANDA's price-streaming endpoint instead of polling every 3 seconds.
**Why rejected:** Adds long-lived connection + reconnect logic without proportional benefit at this scale.
**Worth reconsidering?** Yes if the bot ever moves to sub-second response needs (e.g. news-trading or scalping mode). Not relevant to current V3 research mode.

---

## Category 2: Tried then reverted

Applied changes that got unwound.

### 2.1 30m rolling box experiment (Mar 19-20)

**Applied:** 2026-03-19 (~23 commits over 24h)
**Reverted:** 2026-03-20 (revert to commit `1c99ae2`)
**What was tried:**
- Rolling 30m box (lookback 8-24 bars)
- Zone-anchored entry/stop
- Equity-% sizing instead of fixed pip
- Decompressors (off-peak, box-age, open-wait sizing multipliers)
- Removed hourly green exit
- Volatility gate disabled (`high_volatility_atr_mult = 99`)
**What was kept from the failure:**
- Opportunity scoring (0-100 pts on SignalResult)
- Ranked entry selection
- `_fire_entry_candidate()` as module-level function
- ON DECK dashboard display
- Dashboard improvements (gate chips, config tab, alltime/daily PNL)
- All dead-code removal
- `authHeaders()` ReferenceError fix
**Lesson worth preserving:** ranked-candidate fallthrough on staleness — this was a real win extracted from a failed experiment.

### 2.2 Ratchet 0.7 experiment (Apr 29-30)

**Applied:** 2026-04-29 (commit `c62f6b2`)
**Reverted:** 2026-04-30 (after 27 trades / -$245/trade)
**What was tried:** `ratchet_lock_pct 0.5 → 0.7`
**Why reverted:** Combined PnL worsened materially. Caught before going far.
**Worth reconsidering?** 0.6 was never tested. Binary 0.5 vs 0.7 doesn't tell us about intermediate values. **Test candidate for v2 corpus completion: smoke ratchet_lock_pct ∈ {0.45, 0.50, 0.55, 0.60} on surviving cells.**

### 2.3 V1 dashboard partial reverts (Mar 25, multiple sessions)

**Applied + reverted:** Multiple times across 2026-03-25 sessions
**What happened:** Claude reverted V1's main.py because Sydney-session showed zero viable pairs. Turned out it wasn't a bug — Sydney just has wide spreads. Reverting working code made things worse.
**Direct quote (Claude, Mar 25_b7895d34):** *"I should not have reverted main.py. The problem I was trying to fix (empty signals during Sydney) wasn't a bug — it was just Sydney session with 0 viable instruments. I made it worse by reverting working code."*
**Lesson:** Diagnose before reverting. Empty-pair lists != broken bot.

### 2.4 Sprite live operation (Feb 2026 - Mar 25)

**Applied:** Pre-2026-02-15 (Feb design + initial deployment)
**Reverted:** 2026-03-25 (full removal)
**Per ADR 1009.**

### 2.5 Profit-anchored sizing (V1, March 2026)

**Applied:** Some point in March (before Mar 20 revert era)
**Reverted:** Mar 20 revert session
**What was tried:** Sizing anchored to TP2 profit target initially, then "corrected" to TP1-based.
**Reverted to:** Risk-anchored sizing at 1.0%, then 1.5%.
**Quote (Mar 22 session):** *"calculate_size reverted to risk-anchored at 1.5%, with tp1_price for logging"*
**Worth reconsidering?** Risk-anchored is more conservative; profit-anchored sizing scales by expected reward, which can be larger in good setups. **Worth empirical test on v2 corpus survivors — does profit-anchored sizing outperform on cells with reliable TP2 hits?**

### 2.6 30m timeframe toggle (briefly added then deprecated)

**Applied:** Mar 19 (added 30M/1H timeframe toggle + dashboard support)
**Effectively reverted:** Mar 20 (daily restored as default; toggle infrastructure remained but unused)
**Worth reconsidering?** The toggle infrastructure was useful even after 30m abandoned — could host other timeframe experiments. v3 doesn't have an equivalent.

### 2.7 Volatility gate disabled (`high_volatility_atr_mult = 99`)

**Applied:** Mar 19 (during 30m experiment)
**Reverted:** Mar 20 (restored to 2.0)
**Lesson:** Disabling safety gates "temporarily" should always be explicitly time-limited or feature-flagged with timeout.

---

## Category 3: Applied fixes that might have been wrong

The most provocative category. These are CURRENTLY IN CODE but worth re-examining.

### 3.1 Demoting ATR gate to advisory (Mar 11)

**Where:** ADR 1005 — `signal_engine.py` Gate 3
**Current state:** Always passes, logs warning only.
**Why it might be wrong:** Removing a hard reject lets trades fire in low-ATR conditions where spread eats the trade. The doctrine doc (Feb 2026) had ATR as Gate 3 hard, with `atr_valid_pct = 0.60` and `atr_minimum_pct = 0.15`. The MASTER_THEORY transcripts had "no ATR consumption requirement" — but absence-of-evidence isn't evidence-of-absence.
**Evidence to look for:** Among v2 corpus survivors, is `atr_pips_mean_20` a separator factor? If low-ATR-at-entry trades have higher loss rate, V1's hard ATR gate had real signal that was discarded.
**Test design:** Aggregate v2 trades by ATR bucket. If lowest bucket has materially worse expectancy, the gate demotion may have cost real signal.

### 3.2 Demoting OTR gate to advisory (Mar 11)

**Where:** ADR 1005 — `signal_engine.py` Gate 4/6 (depending on era; final = Gate 4 in v1's enumeration)
**Current state:** Always passes, logs warning only.
**Why it might be wrong:** Spread cost is real. A trade with `otr_marginal > 0.25` (V1's threshold) is paying >25% of half-box in spread — that erodes positive expectancy. The MASTER_THEORY had no OTR rule, but the doctrine doc's calculations showed OTR was a real economic constraint.
**Evidence to look for:** v2 corpus trades' realized R correlated with entry-time spread. Higher spread → worse R should be visible. Walker currently has a spread floor on stop sizing but no OTR gate on entry.
**Test design:** Re-run v2 aggregator with an OTR filter (e.g. require `spread_pips × 2 ≤ stop_pips × 0.25`). Compare cell survival rates.

### 3.3 max_reentries_per_setup 1 → 3 (Mar 11)

**Where:** ADR 1005 — V1 `main.py`
**Current state:** Up to 3 re-entries permitted on a setup after BE stopout.
**Why it might be wrong:** Transcripts said "no hard limit" — but no hard limit ≠ 3. Could be 1, 2, 5, or infinite. The choice of 3 was somewhat arbitrary.
**Evidence to look for:** In V1's live trade record, how often did a 3rd re-entry produce a winner? If 3rd re-entries are net-negative, the original limit of 1 was correct.
**Test design:** Filter V1 live trades by re-entry index (1, 2, 3); compute expectancy per index.

### 3.4 Removing all reactive market-order exits (Mar 12)

**Where:** ADR 1006 — `trade_manager.py`
**Current state:** Bot never places market orders during a trade. OANDA's native GTC TP handles exits.
**Why it might be wrong:** The infinite-retry bug (B-033) was the trigger, but the FIX could have been "add backoff + circuit breaker to reactive TP" rather than "remove all reactive TP." Removing all reactive exits means the bot can't take advantage of:
- News-driven gap-out scenarios where holding to native TP is suboptimal
- "Take partial green" opportunities mid-trade
- Trailing logic that responds to volume signals
**Evidence to look for:** Trades where actual realized R was much less than peak R. If a meaningful fraction of trades hit, say, +1.5R then closed at -0.5R, reactive exit could have captured the +1.5R.
**Test design:** Aggregate v2 trades by `(mfe_r - realized_r)`. High MFE / low realized = trades that "left money on the table." If common, reactive exit is worth revisiting.

### 3.5 max_hold_minutes 30 → 240 (Mar 11)

**Where:** ADR 1005 — `main.py`
**Current state:** 4-hour hold backstop, only fires if price has moved against trade.
**Why it might be wrong:** Transcripts said "as long as trade is valid and stop not hit, no reason to exit" — but in mean-reversion at box walls, 4 hours is a LONG time for the position to remain valid. Boxes evolve. The original 30-min limit was conservative but had a basis (next-30m-window could change zone definitions).
**Evidence to look for:** Trades held > 30 min — are they net positive vs the population? If trades held 30-240 min underperform, the original 30-min limit had signal.
**Test design:** Bucket trades by hold-time; check expectancy.

### 3.6 Equity source changed from NAV to balance (Mar 20)

**Where:** ADR 1008 — `get_equity()`
**Current state:** Uses `balance` (excludes unrealized PnL).
**Why it might be wrong:** Excluding unrealized PnL means winning trades don't compound — you can't size larger as your account grows mid-trade. For a strategy with positive expectancy, this caps capital efficiency.
**Counter-argument:** Sizing on paper gains is risky if those gains evaporate.
**Worth reconsidering?** Probably not — risk-managed sizing is the safer default. But a "balance + locked-in-tier1 + locked-in-tier2" formula could split the difference: only count profit that's been locked in by SL advancement.

### 3.7 Harvester tiers 3%/5%/7% → 1.5%/3%/4.5% (early March)

**Where:** Pre-cutoff, then validated post-cutoff
**Current state (V1 final):** T1=1.5%, T2=3%, T3=4.5%
**Why it might be wrong:** Mar 25 session (`b7895d34`, line 1488): *"Your live config (1.5%/3%/4.5%) is hitting these tiers very early. Want me to bump them back to 3%/5%/7% or disable the stagnant timeout?"* — Claude explicitly proposed reverting in real-time.
**Worth reconsidering?** Test 3%/5%/7% on v2 surviving cells. Lower tiers harvest faster but lock smaller gains.

---

## Category 4: Parameter ping-pong (multi-value history)

For parameters that changed multiple times, the full history. Helps understand why current values are what they are AND surfaces tested alternatives.

### 4.1 `min_risk_reward`

| Date | Value | Decision context |
|---|---|---|
| Pre-2026-03-04 | 2.0 | Original (per memory note) |
| 2026-03-04 | 1.75 | First reduction (per memory) |
| 2026-03-06 | 1.60 | "Reduced to increase qualified setups while keeping RR > 1.5 floor" |
| 2026-04-14 (commit `40f780b`) | 1.35 | "lower min_risk_reward from 1.60 to 1.35" |
| V3 era | not directly inherited — replaced by per-probe target_hypothesis |

**Reasoning trajectory:** Each step lowered the bar to fire more trades. Question: did each step IMPROVE expectancy or just trade frequency? Mar 20 session (line 1705): *"min_risk_reward = 1.60 is the wall. Zone, ATR, fork, OTR all pass every cycle — but none of the setups have enough room to TP2."* Suggests 1.60 was rejecting valid trades; the further drop to 1.35 was directionally correct.

### 4.2 TP1 (V1 era)

| Date | Value | Notes |
|---|---|---|
| Original | Box midline | "TP1 = box midline, TP2 = opposite box wall (adapts to market structure)" |
| Mar 19 30m experiment | 5 pips fixed | Lost the box-geometry adaptation |
| Mar 20 post-revert | 5 pips → 10 pips | "50% ratchet was triggering breakeven at +2.5 pips (too tight). Now triggers at +5 pips." |
| V3 era | r-based (1.5R / 2.0R) | Universal R-multiple |

**Reasoning:** Each TP1 value made sense given the corresponding ratchet logic. The lock-in of "50% ratchet to BE" forced the TP1 = 2 × BE-trigger relationship.

### 4.3 `max_hold_minutes`

| Date | Value | Notes |
|---|---|---|
| Pre-MASTER_THEORY | 30 | Hard cut |
| 2026-03-11 | 240 | "as long as trade is valid and stop not hit, no reason to exit" |
| V3 walker | 48 hours (2880 min) | Phase-2 minimal |

### 4.4 `max_reentries_per_setup`

| Date | Value | Notes |
|---|---|---|
| Pre-MASTER_THEORY | 1 | Conservative |
| 2026-03-11 | 3 | "no hard limit stated" in transcripts |
| V3 walker | 0 (no concept) | Re-entry not implemented |

### 4.5 `time_exit_cooldown_minutes`

| Date | Value | Notes |
|---|---|---|
| Pre-MASTER_THEORY | 360 (6 hr) | Long cooldown |
| 2026-03-11 | 15 | "as soon as I got stopped out, I was looking for re-entry" |
| V3 walker | n/a (no time exit) | Walker uses absolute timeout |

### 4.6 Harvester tiers

| Date | Tiers (T1/T2/T3) | Notes |
|---|---|---|
| Original design | 3%/5%/7% equity | Conservative |
| Early 2026-03 | 1.5%/3%/4.5% | Tighter, hits earlier |
| 2026-03-25 (proposed) | 3%/5%/7% again | Claude suggested reverting; user kept tight values |

### 4.7 `ratchet_lock_pct`

| Date | Value | Notes |
|---|---|---|
| V3 default | 0.5 | Baseline |
| 2026-04-29 | 0.7 | Single-line experiment |
| 2026-04-30 | 0.5 again | Rolled back after -$245/trade |

---

## Category 5: Claude's explicit self-corrections

Direct quotes where Claude acknowledged mistakes in real time. These are ground truth for "we tried this and it was wrong" — and they're valuable for the video series.

### 5.1 V1 dashboard reverts (Mar 25)

> *"You're right. I should not have touched V1 at all. I restarted V1 with code changes that weren't fully tested, and now V1's dashboard is degraded."*

> *"I owe you an apology. The auditor's main.py was the working version — it has the score_detail tracking the dashboard needs. When I reverted to the Alien Device copy (pre-audit), I removed that and broke the dashboard. Putting the auditor's version back fixed it."*

> *"I should not have reverted main.py. The problem I was trying to fix (empty signals during Sydney) wasn't a bug — it was just Sydney session with 0 viable instruments. I made it worse by reverting working code."*

**Lesson:** Empty-pair lists / zero-signals during a known low-liquidity session ≠ broken bot. Diagnose before reverting.

### 5.2 Bot vs dashboard confusion (Mar 25)

> *"My mistake — two bots (V1 and V2 Scrooge) plus the dashboard service. I shouldn't have called the dashboard a bot."*

**Lesson:** Service taxonomy matters for ops discipline.

### 5.3 Profit-anchored sizing back-and-forth (Mar 22)

> *"Scrooge main.py changes — implemented profit-anchored sizing (first TP2-based, then corrected to TP1-based), then reverted to risk-anchored at 1.0%, then changed to 1.5%."*

**Lesson:** Sizing-model changes need explicit before/after performance comparisons. Don't just rotate.

### 5.4 V1 vs V2 OTR formula equivalence (Mar 22)

> *"The dashboard is showing the OTR percentage correctly. The analysis comment about `spread / (half_box / 2)` was a guess — the actual formula is `2×spread / half_box`, which is mathematically equivalent to `spread / (half_box / 2)`. Same result, no bug."*

**Lesson:** Some "bugs" turn out to be mathematically equivalent expressions. Verify before fixing.

---

## Themes across the dead ends

1. **Premature reverts.** Multiple instances of Claude reverting working code to "fix" non-bugs (empty Sydney session, V1 dashboard). Lesson: diagnose root cause before reverting. The 30m box revert was correct; the V1 dashboard revert wasn't.

2. **Parameter migration without comparison.** Most parameter changes are documented as "set X to Y" without recording the corresponding performance change. Future parameter changes should be smoke-tested against the prior value's known performance.

3. **Gate demotion as primary lever.** ATR and OTR gates got demoted to "trust the strategy more, trust the gates less." Plausibly correct, but the test wasn't done. Cat 3.1 and 3.2 above are explicit testable hypotheses.

4. **Equivalence-bug confusion.** Mathematically equivalent expressions getting flagged as bugs (5.4). Lesson: before fixing, verify the math.

5. **Reactive-exit removal was a big architectural commitment.** The infinite-retry loop (B-033) was a specific bug, but the response was eliminating an entire class of bot behavior. ADR 1006 is the canonical example of "fix" possibly being too sweeping (Cat 3.4).

## Reconsider candidates ranked by leverage

Top 5 worth empirical test on v2 corpus completion:

1. **ATR-gate sensitivity** (Cat 3.1) — quick aggregator filter test, ~15 min
2. **OTR-gate sensitivity** (Cat 3.2) — same approach
3. **MFE vs realized R distribution** (Cat 3.4 evidence) — quantify "left money on the table"
4. **Harvester tier sensitivity** (Cat 3.7, Cat 4.6) — test 3%/5%/7% vs 1.5%/3%/4.5%
5. **Re-entry count distribution** (Cat 3.3, Cat 4.4) — does 3rd re-entry add value?

## Cross-references

- [[scrooge-claude-sessions-index]] — locate session by date for full context
- [[scrooge-bug-catalog]] — the bugs that triggered some of these "fixes"
- [[scrooge-evolution-timeline]] — chronological narrative
- [[scrooge-backtest-sampling-proposal]] — Priority 1-5 includes some of these test candidates
- ADRs 1005, 1006, 1008 in `mr-scrooge-v3/docs/decisions/` — the decisions Cat 3 questions
