---
type: bug-catalog
status: living
tags: [scrooge, bugs, debugging, institutional-memory, audit]
date: 2026-05-11
trust: high
evidence:
  - exec summary Feb 26 2026 (3 audit passes)
  - AUDIT.md from V1 repo
  - Daily notes Mar 6 / 11 / 12 / 24
  - GitHub commit log
  - postmortem 2026-05-08 (Echo discriminator)
---

# Mr. Scrooge — Bug Catalog (V1 → V3)

Institutional memory of every documented bug across the Mr. Scrooge bot family. Each entry: era, file/area, symptom, root cause, fix, evidence link, lessons. Organized chronologically by era.

**Why this exists:** when current work surfaces an oddity, this catalog answers "have we seen this before?" without re-deriving. Also useful for evaluating whether a current bug shares structure with a past one (recurring patterns → architectural issues).

## Pre-history audits (Feb 2026, before live deployment)

Source: `scrooge-v1-exec-summary-feb-2026.md` §11.1 (the formal pre-deployment audit).

### B-001 — Sucker move termination not at zone
- **Area:** `signal_engine.py`
- **Fix:** Enforce sucker-move termination at pre-identified zone (Gate 4 logic)
- **Lesson:** Behavioural patterns need explicit geometric anchoring; "moves into a zone" is not the same as "moves to a zone."

### B-002 — Tier 1 zone test-count requirement
- **Area:** `zone_detector.py`
- **Fix:** Tier 1 requires daily alignment only, no test count
- **Lesson:** Over-specified zone classification rejected valid setups.

### B-003 — Time exit firing after TP1
- **Area:** `trade_manager.py`
- **Fix:** Time exit only fires before TP1. Trailing winners after TP1 run free.
- **Lesson:** Time-based exits should never cut winning trades short.

### B-004 — Open wait blocked premium setups
- **Area:** `main.py`
- **Fix:** Open wait exception at 50% size for Tier-1 + 80%+ ATR + John Wick or Power of Towers
- **Lesson:** Rules need escape valves for highest-conviction setups.

### B-005 — Gap detection not at boot
- **Area:** `zone_detector.py`
- **Fix:** Gap detection redraws box proactively before first candle is evaluated
- **Lesson:** Boot-time state can't assume "no special conditions."

### B-006 — Box trade counter only incremented on entry
- **Area:** `main.py`
- **Fix:** New box trade counter increments on every close
- **Lesson:** Per-box counters need to track both sides of the lifecycle.

### B-007 — Re-entry not wired
- **Area:** `main.py`
- **Fix:** Re-entry wired via `assess_reentry()` on break-even stops
- **Lesson:** Liquidity-sweep theory needs explicit re-entry logic; absence is silent failure.

(Two more items in the pre-deployment audit were "non-issues on closer inspection — implementation already matched spec intent.")

## Pre-history live deployment audit (Feb 2026)

Source: `scrooge-v1-exec-summary-feb-2026.md` §11.2. Forex (Scrooge) + Crypto (Sprite) issues.

### B-008 — OANDA candle fetcher filtered current forming bar
- **Symptom:** ATR consumed always appeared 100-120%
- **Root cause:** Fetcher excluded the in-progress bar from the ATR window
- **Fix:** Include current bar
- **Lesson:** "Current forming bar" can be valid data depending on use case; default filtering is dangerous.

### B-009 — Limit orders rejected `WOULD_TRIGGER_IMMEDIATELY`
- **Symptom:** Entry limits rejected by OANDA
- **Root cause:** Price had moved past limit between signal fire and order placement
- **Fix:** Switched to OANDA market orders with TP+SL on fill
- **Lesson:** Stale-price problem at order placement is a recurring theme — see B-012.

### B-010 — Missing `register_entry` call → duplicate entries
- **Symptom:** Same signal repeatedly entered each cycle
- **Root cause:** No bookkeeping registered the entry
- **Fix:** Added duplicate-entry guard
- **Lesson:** Every "entry happened" path needs explicit state update.

### B-011 — `session_start = datetime.now()` on restart
- **Symptom:** Open wait reset every bot restart
- **Root cause:** Session start derived from process boot, not actual market open
- **Fix:** `_compute_session_start()` derives from `SESSION_WINDOWS`
- **Lesson:** Time anchors must be world-state, not process-state.

### B-012 — Missing `timeInForce: FOK` and `positionFill: DEFAULT`
- **Symptom:** OANDA order field errors
- **Root cause:** OANDA's v20 API requires explicit field setting; Burns's working client had these but Scrooge didn't
- **Fix:** Added the fields
- **Lesson:** When a sister bot works and yours doesn't, diff the API payloads.

### B-013 — Units sent as float strings
- **Symptom:** OANDA rejecting orders
- **Root cause:** `"-2430.0"` instead of `"-2430"`
- **Fix:** Format as integer string
- **Lesson:** API field types matter; float-vs-int silently breaks.

### B-014 — `clientExtensions` at order level instead of `tradeClientExtensions`
- **Symptom:** Client ID not associated with the trade
- **Root cause:** Wrong key — `clientExtensions` is for the order; trades need `tradeClientExtensions`
- **Fix:** Use the right key
- **Lesson:** OANDA's v20 API has parallel order vs trade nomenclature; easy to confuse.

### B-015 — `STOP_LOSS_ON_FILL_LOSS` rejection on stale prices
- **Symptom:** OANDA rejected orders if price moved past stop level between signal and placement
- **Fix:** Staleness check — if current price is at or beyond stop, skip entry
- **Lesson:** This is the cousin of B-009. Stale-price-at-placement is structural for any live-trading bot.

### B-016 — Sprite `zone_proximity_pct = 0.3%` (forex default)
- **Symptom:** ATOM at $1.942, PDL at $1.929 (0.67% away) failed zone gate every cycle
- **Fix:** Widen to 1.5% for crypto
- **Lesson:** Strategy parameters that work for one asset class don't transfer; defaults are dangerous.

### B-017 — Sprite `cl_ord_id` rejection (Kraken)
- **Area:** Kraken API integration
- **Lesson:** Each exchange has its own ID rules.

### B-018 — Sprite position size overflow on low-priced coins
- **Symptom:** Tight stops on low-priced coins generating 1,000-3,000 unit orders on a $785 account
- **Lesson:** Sizing math has to account for unit cost as well as risk percentage.

### B-019 — Sprite post-only orders never filling at zone entry
- **Symptom:** Orders queued but never executed
- **Lesson:** Post-only is wrong for entry-at-zone (need to cross spread or pay maker fee).

### B-020 — Sprite Kraken price precision rejection
- **Symptom:** Slippage-buffered prices rejected on precision
- **Lesson:** Each exchange has its own decimal-precision rules per asset.

## V1 Discipline era (Mar 5-19, 2026)

Source: AUDIT.md.

### B-021 — Multiple concurrent bot instances
- **Date:** 2026-03-05
- **Symptom:** Duplicate log lines, two engines writing simultaneously
- **Root cause:** Restart didn't enforce single-process
- **Fix:** Non-blocking file lock `logs/mr-scrooge.lock` + orphan-process sweep in `start.sh`
- **Lesson:** Process-uniqueness must be enforced, not assumed. This is THE classic operational bug.

### B-022 — RR threshold too high
- **Date:** 2026-03-06
- **Fix:** `min_risk_reward 1.75 → 1.60`
- **Lesson:** Theoretical RR thresholds need empirical validation; 1.75 was rejecting profitable setups.

### B-023 — Native-close cooldown applied to wins
- **Date:** 2026-03-06
- **Fix:** Profitable closes skip cooldown; only losses keep it
- **Lesson:** Cooldown is a loss-control mechanism, shouldn't penalize wins.

### B-024 — Net floor not pip-normalized
- **Date:** 2026-03-07
- **Symptom:** Inconsistent profit floor across JPY vs non-JPY pairs
- **Fix:** `min_net_profit_pips = 7` (was absolute value)
- **Lesson:** Pip-normalize all profit/loss thresholds; absolute units break across pair classes.

## V1 MASTER_THEORY realignment (Mar 11, 2026)

Source: `DAILY_NOTES_2026-03-11.md`. Not a bug per se but a category of bugs: **invented rules not in source theory**.

### B-025 — Strict consecutive-candle counting in sucker move
- **Symptom:** Bot rejected valid messy/choppy sucker moves (red green green red green)
- **Fix:** Flexible window — count directional within `max_candles + 2`
- **Lesson:** "Consecutive" was invented; transcripts allowed pattern noise.

### B-026 — Mixed box-wall / candle-extreme stop placement
- **Fix:** Always at signal candle extreme
- **Lesson:** Stop placement was inconsistent; should match the entry signal's anatomy.

### B-027 — Zone-anchored triggers instead of candle-based
- **Fix:** Trigger prices use candle high/low, not zone price
- **Lesson:** Entries trigger on candle behaviour, not zone proximity.

### B-028 — ATR gate (Gate 3) was a hard reject
- **Fix:** Demoted to advisory
- **Lesson:** MASTER_THEORY had no ATR consumption requirement; the gate was over-engineered.

### B-029 — OTR gate (Gate 6) was a hard reject
- **Fix:** Demoted to advisory
- **Lesson:** Same as B-028. Two of six gates were inventions.

### B-030 — Trend filter blocked Tier-1 zones
- **Fix:** Tier 1/2 zones override trend block
- **Lesson:** Box-extreme entries are valid even against trend (per transcripts).

### B-031 — Hard 30-min time exit cut winners
- **Fix:** 4-hour backstop, only fires if price moved against trade
- **Lesson:** Time exits should be safety nets, not arbitrary cuts.

### B-032 — `max_reentries_per_setup = 1`
- **Fix:** Raised to 3 (transcripts: no hard limit)
- **Lesson:** Limits had to come from source theory, not gut feel.

## V1 Green-exit crisis (Mar 12, 2026)

Source: `DAILY_NOTES_2026-03-12.md`. The most architecturally significant V1 bug.

### B-033 — Infinite retry loop on LIMIT TP rejection [CRITICAL]
- **Symptom:** Bot tried to set LIMIT TP after price had already reached/passed target. OANDA rejected. `green_exit` / `set_tp` handlers fired every cycle with no escape.
- **Root cause:** Reactive TP-setting + OANDA's "limit price already at/past market" rejection + no exit-once-rejected logic
- **Fix:** **Removed all reactive TP-setting and market-order exit logic**. Bot becomes SL-advancement only. OANDA's native GTC LIMIT TP at entry as TP2 handles exit.
- **Lesson:** Reactive order modifications in live markets are infinite-loop landmines. Anything that retries a same-cycle rejection needs explicit backoff or removal.

### B-034 — Stop-hit close via market order
- **Eliminated** in same redesign.

### B-035 — `partial_tp` market close
- **Eliminated** in same redesign.

### B-036 — Early break-even tied to old partial framework
- **Eliminated.** Replaced with `Stage 1: SL to entry when price reaches 50% to TP1`.

## V1 30m box experiment + 17-bug overhaul (Mar 19-20, 2026)

Source: AUDIT.md. The experiment failed; reverting introduced 17 incidental fixes.

### B-037 — `pkill` + `Popen` left orphan processes
- **Fix:** `systemctl --user restart`
- **Lesson:** Use the OS supervisor.

### B-038 — `authHeaders()` ReferenceError in dashboard.html
- **Console error.** Fix: removed orphan call.

### B-039 — Timeframe toggle buttons broken in dashboard
- **Fix:** Re-wired the toggle handlers.

### B-040 — SL/TP set in equity-% mode produced inconsistent risk
- **Fix:** Migrated to fixed-pip: `sl_pips=10`, `tp1_pips=10`, `tp2_pips=30`
- **Lesson:** Pip-based stops give consistent risk across pairs; equity-% drifts.

### B-041 — `max_trade_risk_pct`, `target_profit_pct`, `tp1_allocation_pct` were dead code
- **Fix:** Removed (sizing-ref only).
- **Lesson:** Dead config keys are dangerous — they look like they do something.

### B-042 — `_is_tp_reached()`, `get_position_size_multiplier()` dead code
- **Fix:** Removed.
- **Lesson:** Same as B-041.

### B-043 — ON DECK badge didn't show at max positions
- **Symptom:** Early return suppressed scoring
- **Fix:** Removed early return; signals still score when position cap full

### B-044 — Zone cache poisoning
- **Symptom:** Cache written on signal evaluation, not on actual order fire
- **Fix:** Cache write moved into `_fire_entry_candidate()`
- **Lesson:** Caches should only be authoritative on confirmed state changes.

### B-045 — JPY margin sizing wrong [CRITICAL]
- **Date:** 2026-03-20
- **Symptom:** All JPY pair trades blocked
- **Root cause:** Formula was `current_price * margin_rate` (wrong for cross pairs — current_price is in JPY, margin_rate is USD)
- **Fix:** `base_price_usd * margin_rate`
- **Lesson:** Cross-pair pricing requires explicit base currency normalization.

### B-046 — `equity = NAV` (included unrealized PnL)
- **Symptom:** Sizing inflated by unrealized winners
- **Fix:** `equity = balance` (excludes unrealized PnL)
- **Lesson:** Sizing should be on realized cash, not paper gains.

### B-047 — Config tab had obsolete fields
- **Fix:** Cleaned up.

### B-048 — Stale candidate fallthrough
- **Symptom:** Top-ranked candidate going stale blocked all entries that cycle
- **Fix:** Ranking loop iterates all candidates until one fires
- **Lesson:** Ranked selection needs explicit fallthrough on staleness.

### B-049 — Dead `leverage` config key
- **Fix:** Removed.

### B-050 — Fill-anchored SL/TP not recalculated
- **Symptom:** SL/TP placed pre-fill drifted from actual fill price
- **Fix:** After OANDA fill, recalc SL/TP from fill price and update via `modify_trade_stop()` / `modify_trade_tp()`
- **Lesson:** Pre-fill prices are estimates; post-fill prices are truth.

### B-051 — RR sanity check missing
- **Symptom:** Entries firing where actual RR was below `min_risk_reward`
- **Fix:** Block at fire time.

### B-052 — TP1 = 5 pips triggered breakeven too tight
- **Symptom:** 50% ratchet triggered breakeven at +2.5 pips — too close to entry, scratch trades constant
- **Fix:** TP1 = 10 pips → 50% ratchet at +5 pips
- **Lesson:** Tiny TPs cascade into tiny ratchet triggers; widen all together.

### B-053 — Sizing decompressors compounding
- **Symptom:** `get_position_size_multiplier()` applying box-age, off-peak, open-wait multipliers
- **Fix:** Removed — sizing is straight 80%
- **Lesson:** Multipliers compound; if you can't predict the final value, you don't control it.

## V2 era (Mar 21 - Apr 15, 2026)

### B-054 — V2 silent skip from `return None` indentation [CRITICAL — 4.5 hr outage]
- **Date:** 2026-03-24 (caught morning)
- **Commit:** `3203cfe`
- **Symptom:** No signals evaluated for ~4.5 hours. Bot looked healthy. Logs continued. Positions managed normally.
- **Root cause:** `return None` at 8-space indent in `coordinator.py:process_instrument()` should have been at 12-space (inside `if not tradeable:` guard). Python parsed it as unconditional return at function level.
- **Fix:** Re-indent.
- **Lesson:** Whitespace bugs in Python are dangerous — silent, no warning, no log gap. **Indent-based block structure means single-character changes can completely alter behaviour.** Mitigation: linters that flag suspicious early returns, code review on coordinator-level logic.

### B-055 — 46-order API spam on dead position
- **Date:** 2026-04-10
- **Symptom:** SL-limit placement firing 46 times on a trade that no longer existed
- **Root cause:** 4 actors (bot, ratchet, SL-limit, harvester) modifying same OANDA trade with no shared state. SL-limit couldn't see that position had vanished.
- **Fix:** Introduced `TradeCoordinator` cross-process state file. `is_trade_alive` gate before SL-limit placement. `NO_POSITION_TO_REDUCE` cancel detection.
- **Lesson:** Multi-actor systems need shared truth. State scattered across processes will produce phantom-action bugs.

### B-056 — Ratchet/harvester SL race
- **Date:** 2026-04-10 (same audit as B-055)
- **Symptom:** Ratchet and harvester both moving SL without coordination
- **Fix:** `sl_owner` field in coordination file; ratchet checks before pushing SL
- **Lesson:** Single-resource ownership requires explicit handoff protocol.

### B-057 — Ratchet didn't see harvester tier state
- **Date:** 2026-04-10
- **Symptom:** Ratchet's Stage 2 logic didn't know if T1 had been taken
- **Fix:** Ratchet reads `tiers_hit` from coordination file to sync `partial_1_taken`
- **Lesson:** Cross-actor state must be read every cycle, not assumed.

## V3 era (Apr 15 - present)

### B-058 — `_update_sessions` not updating `_last_screen`
- **Date:** 2026-04-09 (commit `28d0642`)
- **Symptom:** Session rescan updated `active_instruments` but not `_last_screen`. Dashboard showed stale spread/OTR data from prior scan.
- **Fix:** One-line fix in `main.py` to update both.
- **Lesson:** Per-cycle state has dependencies that aren't enforced by types.

### B-059 — `client_id` NameError in `trade_state.py mark_dead()` [CRASHING]
- **Date:** 2026-04-15 (commit `8e7f7fa`)
- **Symptom:** Harvester crashing on mark_dead.
- **Fix:** Variable scoping fix.

### B-060 — Execution timing: instant-fill slippage
- **Date:** 2026-04-15 (commit `f28134f`)
- **Symptom:** Stop-loss filling instantly on order placement due to fast price movement
- **Fix:** 4 SL guardrails added.
- **Lesson:** Order placement isn't atomic with intent; defenses needed.

### B-061 — Stale harvest LIMITs fired as naked positions
- **Date:** 2026-04-29 (commits `4ad40b3` + `143247d`)
- **Symptom:** Two-pass safety fix. Orphan harvest LIMITs fired without parent positions.
- **Fix:** Pass 1: GTD + ledger + cancel hooks. Pass 2: orphan sweep walks broker pending orders, not just ledger.
- **Lesson:** Ledger != broker truth. Orphan detection must reconcile both.

### B-062 — Harvest same-cycle race (false `broker_side_gone` cancels)
- **Date:** 2026-04-30 (commits `373085e` + `73be822`)
- **Symptom:** `reconcile_pending_orders` cancelled new harvest LIMITs placed in same cycle they were created
- **Fix:** Option B — same-cycle placements union'd into `pending_on_broker`. 3 regression tests added.
- **Lesson:** Reconciliation logic must understand same-cycle creates.

### B-063 — Ratchet 0.7 experiment regression
- **Date:** Started 2026-04-29, rolled back 2026-04-30
- **Symptom:** `ratchet_lock_pct 0.5 → 0.7` produced -$245/trade across 27 trades
- **Action:** Rolled back to 0.5.
- **Lesson:** Single-config experiments need pre-defined rollback criteria.

### B-064 — Strategy attribution fundamentally unreliable [CRITICAL]
- **Date:** Existed pre-2026-05-04
- **Symptom:** `AuditEvent.strategy` field missing or unpopulated. Scan-cycle lookup window only 800 lines / ~60 sec. Many trades classified `strategy=unknown`.
- **Fix:** 
  - Patch A (`492a999` @ 06:38:45 UTC): `strategy` field threaded through AuditEvent
  - Patch B.right (`73f1e41` @ 06:50:53 UTC): deterministic `(order_id) → (strategy, scan_cycle)` linkage via `OrderAttributionWriter`
- **Lesson:** Attribution telemetry has to be designed in, not bolted on. Lookback windows that "should be enough" usually aren't.

### B-065 — V2 Echo discriminator timeframe mismatch
- **Date:** 2026-05-08 (postmortem)
- **Symptom:** Echo split-point spread = 2.11 across pairs (should cluster near 0.30)
- **Root cause:** `atr_pips / atr_pips_mean_20` ratio was comparing H1 ATR (from V3 feature pipeline) to M5 trailing TR (computed locally). Different timeframes.
- **Fix:** Option 1 — `current_M5_range / mean(prior_20_M5_ranges)` (same timeframe, naturally near 1.0)
- **Lesson:** When two metrics compose into a ratio, name the source timeframe of each at design time. Generic feature names ("atr_pips", "atr_pips_mean_20") are not enough.

### B-066 — V2 corpus parquet engine missing (OOM-adjacent)
- **Date:** 2026-05-05
- **Symptom:** v1 corpus run completed all 18 min of compute but crashed on parquet write: `Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'`
- **Root cause:** Used system `python3` (no pyarrow), should have used `~/mr_burns_env/bin/python3`
- **Fix:** Switched interpreter + added preflight check + CSV fallback + sidecar JSONL append
- **Lesson:** Defense-in-depth on persistence. Long compute should never lose final output.

### B-067 — V2 corpus aggregator OOM on bootstrap CI [CRITICAL]
- **Date:** 2026-05-08
- **Symptom:** Aggregator process killed mid-CI computation
- **Root cause:** `numpy.random.choice(values, size=(n_boot, len(values)))` allocated 5.7 GB for one 360k-trade cell. Box had 3.7 GB RAM.
- **Fix:** Normal approximation CI for n≥1000 (saves ~5GB per large cell). Bootstrap for n<1000.
- **Lesson:** Bootstrap memory cost is O(n_boot × n). At corpus scale, switch to analytical CI.

## Recurring patterns (architectural lessons)

These bug families repeat across versions:

| Pattern | Examples | Mitigation |
|---|---|---|
| **Stale price at order placement** | B-009, B-015 | Staleness check before send |
| **Multi-actor race on shared resource** | B-055, B-056, B-057 | Shared state + ownership protocol (TradeCoordinator) |
| **Reactive market-order loop** | B-033 | Bot never places market orders; OANDA native handles exits |
| **Pip-normalization across pair classes** | B-024, B-040, B-045 | All thresholds in pips, never raw price units |
| **Cross-pair / cross-asset parameter defaults** | B-016 (Sprite vs Scrooge), B-045 (JPY margin) | Parameter classes per pair-class |
| **Silent zero-signal outages** | B-054 | Add cycle-level scan counters + alert on zero-signals-for-N-cycles |
| **Dead config keys** | B-041, B-042, B-049 | Periodic audit; type-check config loader |
| **Stale telemetry / cache** | B-058 (V3), B-044 (V1) | Centralize state update on confirmed events |
| **Per-trade attribution gaps** | B-064 (Patch A/B.right) | Design attribution in from day 1; explicit `(order_id) → strategy` mapping |
| **Pre-fill vs post-fill prices** | B-050 | Always recompute on fill |

## Bugs that informed current architectural decisions

| Bug | Decision it triggered |
|---|---|
| B-033 (infinite retry loop) | Bot never places market orders — V1 doctrine since Mar 12 |
| B-045 (JPY margin) | Cross-pair sizing math explicit in V3 |
| B-054 (silent V2 skip) | Live signal counters / dashboard skip-rate visibility |
| B-055 (46-order spam) | TradeCoordinator pattern → influences V3 actor coordination |
| B-064 (attribution unreliable) | Live broker forensic audit window dated post-attribution-fix |
| B-065 (Echo timeframe) | Spread-check rule on freezes |
| B-067 (aggregator OOM) | Streaming-only constraint #11 in scrooge-frozen-constraints |

## How to add to this catalog

When a new bug is found:
1. Get a unique ID (next sequential `B-NNN`)
2. Capture: date, area, symptom, root cause, fix, lessons
3. Cross-link to commit/postmortem if applicable
4. Add to the recurring-patterns section if it matches an existing family

## Cross-references

- [[scrooge-evolution-timeline]] — the broader narrative this catalog grounds
- [[scrooge-v1-exec-summary-feb-2026]] — verbatim doctrine doc (source for B-001 to B-020)
- [[scrooge-v1-doctrine-highlights]] — scannable index
- AUDIT.md in `BrockStar3540/mr-scrooge` repo — source for B-021 onward
- `archive/DAILY_NOTES_2026-03-*.md` in Dropbox archive — source for B-025 to B-036
- [[v2-echo-discriminator-timeframe-bug-2026-05-08]] — B-065 postmortem
- [[scrooge-frozen-constraints]] — current locked decisions, several traced back to specific bugs here
- `mr-scrooge-v3/docs/decisions/` — ADRs that close categories of bug

## Box-drawing bug family (B-068 to B-074) — added 2026-05-11

Surfaced during Claude-sessions archive sweep (2026-05-11). These were live and discussed but not previously catalogued. Full forensic detail: [[scrooge-box-bugs-and-validation-targets]].

The box (daily PDH/PDL liquidity zone) is the foundational reference for every trade. When it draws wrong, every trade off it is contaminated. **Seven distinct failure modes** identified across V1/V2:

### B-068 — Inverted boxes from stale 200-bar slice (pre-2026-03-09)

`zone_detector._get_prior_day_hourly()` used `iloc[:24]` (OLDEST 24 of 200 bars), pulling data from 8+ days prior. Percentile filter "cleaned" yesterday's PDH/PDL using ancient bars, producing wildly wrong levels and on several pairs fully inverted boxes (PDL > PDH). Bot took longs in clear EUR downtrends.

- **Affected:** USD_CAD, EUR_NZD, GBP_CAD inverted; EUR/USD PDH inflated +900 pips. All EUR-pair longs in lead-up suspect.
- **Fix:** `iloc[:24]` → `iloc[-48:-24]` + PDH>PDL sanity guard. 2026-03-09.
- **Contaminated window:** unknown start through 2026-03-09 fix.

### B-069 — 30m rolling box experiment broke profitability (2026-03-19 → 03-20)

Replaced daily PDH/PDL with 12hr rolling `_build_30m_box()`. Box shifted every cycle. ATR/OTR/sucker-move gates calibrated for daily geometry — incompatible. Bot bled.

- **Fix:** Commit `59e83b9` 2026-03-20 — full revert to daily box.
- **Contaminated window:** 2026-03-19 evening → 2026-03-20 afternoon (~18-24h). **HARD EXCLUDE from any live-truth backtest.**

### B-070 — Percentile filter over-clipping shrinks daily boxes (ongoing V1/V2)

Percentile filter on spike wicks clipped 0.33-0.39% of real range. Half-box geometry shrank → TPs closer to entry → tighter R:R. Also caused crypto box rejection on low-vol days (looked like a "bot off" bug).

- **Fix:** Flagged 2026-03-20, never fully removed in V1/V2.
- **Contaminated window:** ongoing through V1/V2 lifetime. ~5-15 pips per pair per day of compressed TPs.

### B-071 — Filtered PDH below market → OANDA 400 rejection cascade (2026-03-25)

Percentile filter clipped USD/CHF PDH from 0.79248 → 0.78939. Long signal fired with TP2 = filtered PDH while market was 0.790+. OANDA rejected 5 market orders (BUY TP must be > current market). `_calculate_targets()` validated `tp2 > entry_price` only, not vs current market.

- **Affected:** USD/CHF LONG 2026-03-25 (5 rejections V1+V2). Structural for any long with filtered PDH < current market.
- **Fix:** Diagnosis 03-25; structural fix = validate TP vs current market + cap percentile filter.
- **Contaminated window:** 2026-03-24 (commit `3f14762e` unmasked this) through V1/V2 lifetime.

### B-072 — Box-reset amnesia at UTC midnight (regime era → 2026-03-29)

At 00:00 UTC daily box recomputes. Pair BLOCKED for hours (score -6) instantly resets: new PDH/PDL → price "inside" → `box_contained(+1)` → prior negative signals forgotten → score jumps -6 → +1 → entry permitted → loss.

- **Affected:** USD/MXN (-$1,197), EUR/CHF (bad 14:02 UTC entry after 06:31 BLOCKED), NZD/JPY (-$53). Pattern likely hit many pairs across many UTC midnights.
- **Fix:** Hysteresis tightened — after BLOCKED (score ≤ -3), recovery requires score ≥ +2. Tag `REGIME_HYSTERESIS`. 2026-03-29.
- **Contaminated window:** every UTC midnight from regime activation (~03-22 V2, ~03-31 V1) through 2026-03-29. **EXCLUDE first ~2h of every UTC day for pairs BLOCKED in prior 24h on that window.**

### B-073 — Stale-box snapshot → 7,883-pip absurd TPs (2026-04-09)

USD/CHF (×2) + GBP/CAD (×1) showed TP2 of 7,883 / 18,400 pips. Box snapshot in `_calculate_targets()` not refreshed; old box carried into target math.

- **Fix:** 3× daily-ATR clamp on TP2 distance (Defect #11 / B.4 patch). Guard, not root-cause fix. 2026-04-09.
- **Contaminated window:** unknown earlier extent. **Conservative: USD/CHF + GBP/CAD entries 2026-03-31 → 2026-04-09 suspect.**

### B-074 — Regime supervisor judges against original box during alt-box state (open 2026-04-13)

When `using_alternative=True`, signal engine trades alt-box PDH/PDL but regime supervisor evaluates against **original (broken) box**. Two boxes of truth for same instrument.

- **Affected:** USD_CHF, AUD_CAD, USD_MXN `score=1` trades on V1+V2 were ALL alt-box trades — got fake-valid scores near the floor.
- **Fix:** Score=1 floor (Phase 3A) = band-aid. Structural fix flagged for follow-up. **Open as of 2026-04-13.**
- **Contaminated window:** any alt-box trade through 2026-04-13. **Backtest filter: treat `signal.score == 1` as known-contaminated cohort. Clean filter: `signal.score >= 20`.**

### Source

[[scrooge-box-bugs-and-validation-targets]] — forensic detail + validation-target winning days.


## Era 5 — Matrix integration & ML routing (May 2026)

### B-075 — Stale harvest LIMITs survive parent close → fire as naked positions (2026-04-28 → 2026-04-30)

Track 1 management failure audit surfaced harvest LIMITs that survived after their parent position closed, then fired as naked positions on the next price spike. Two failure modes:
1. Harvest ledger (`harvest-order-ledger.json`) had the orphan but the cancel-on-parent-close hook didn't fire.
2. Broker had pending harvest LIMITs that weren't in the ledger at all (placed in same scan cycle as a reconcile pass that consumed an older parent-side snapshot).

- **Affected:** Trade 4146 (orphan-harvest parent_vanished diagnosis #27) plus unknown earlier extent.
- **Fix:** Two-pass safety (ADR 3003). Pass 1 commit `4ad40b3` (2026-04-29): GTD on harvest LIMITs + ledger + cancel hooks. Pass 2 commit `143247d` (2026-04-30): orphan sweep walks broker pending orders directly. 9 regression tests.
- **Contaminated window:** unknown earlier extent through 2026-04-30. **Conservative: any harvest-fired trade where parent isn't traceable in ledger is suspect through 2026-04-30.**

### B-076 — `reconcile_pending_orders` same-cycle false `broker_side_gone` cancels (2026-04-30)

When an order was placed and `reconcile_pending_orders` ran in the same scan cycle, the broker-side snapshot used for the orphan check had been captured before the placement landed. Result: legitimate just-placed orders got tagged `broker_side_gone` and cancelled.

- **Affected:** ~hours of false cancels surrounding the harvest hotfix deploy 2026-04-29.
- **Fix:** Option B (ADR 3004) commit `373085e` + merge `4008e6c`. Same-cycle placements now union-merged into `pending_on_broker` before the orphan check. 3 regression tests.
- **Contaminated window:** 2026-04-29 evening → 2026-04-30 fix deploy. False-cancel rate confirmed dropped to 0 over next 48h.

### B-077 — Ratchet 0.7 experiment cost −$245/trade (2026-04-29 → 2026-04-30)

Single-line config experiment: `ratchet_lock_pct: 0.5 → 0.7`. After 27 trades the combined P&L was −$245/trade worse than the 0.5 control. Statistical floor for a real experiment hadn't been hit, but the loss magnitude warranted preemptive rollback.

- **Affected:** 27 trades 2026-04-29 → 2026-04-30.
- **Fix:** Rollback (ADR 3004) commit `73be822` — `ratchet_lock_pct` reverted to 0.5.
- **Contaminated window:** 2026-04-29 ratchet-0.7 deploy → 2026-04-30 rollback. Approximately −$6,615 cumulative attributable to the experiment over the 27 trades.
- **Note:** Not a bug per se — controlled experiment with early stop. Catalogued because the cohort is contaminated for backtest purposes and "ratchet 0.7" is a closed-off direction.

### B-078 — Attribution lost via 800-line scan-log window (2026-04-28 → 2026-05-04)

30%+ of journal events had `strategy=unknown`. Two root causes:
1. `AuditEvent` schema was missing `strategy` field — attribution inferred at journal-write time by scanning back through scoring logs.
2. Scan-lookup window was only the last 800 log lines (~60 seconds of activity), so any candidate scored more than ~60s before order fill lost its attribution.

Downstream impact: broker-truth audits, ML observer training, and per-strategy WR breakdowns all unreliable.

- **Affected:** ~30%+ of all live trades pre-2026-05-04 fix; specifically masked the per-strategy WR breakdown for the 48h losing-streak diagnosis.
- **Fix:** Two-patch architecture (ADR 3006). Patch A commit `492a999` — add `strategy` field to AuditEvent. Patch B.right commit `73f1e41` — `OrderAttributionWriter` + `lookup_attribution(order_id)` + `attribution_source` field tracking.
- **Contaminated window:** all live trades pre-2026-05-04. **Backtest filter: pre-2026-05-04 strategy attribution is unreliable; broker-truth audits before that date should treat `strategy=unknown` rows as un-attributable.**

### B-079 — Scan-dashboard JSON stripping blinded ML observer + broker attribution (2026-05-27)

After Patches A + B.right (ADR 3006), a subtle leak remained: the scan dashboard endpoint was stripping the `candidate` field from its JSON output. ML observer + broker attribution both relied on reading this field from the dashboard JSON. Result: post-Patch-B.right attribution still showed gaps that looked like Patch B.right was incomplete.

Diagnosis took weeks because Patches A + B.right *were* working correctly; the missing data was at a different layer.

- **Affected:** ML observer + broker attribution 2026-05-04 → 2026-05-27.
- **Fix:** B-1 Patch C commit `64410a3` (2026-05-27) — dashboard JSON includes candidate field.
- **Contaminated window:** 2026-05-04 (Patch B.right deploy) → 2026-05-27 (Patch C deploy). **Backtest filter: ML observer training set from this window has missing-attribution holes that aren't reflected in attribution_source = field_native counts.**

## Source

[[scrooge-v3-attribution-brokertruth-factors]] — full B-1 arc.
[[scrooge-v3-harvest-same-cycle-race]] — B-076 + B-077 detail.
[[scrooge-v3-stale-harvest-hotfix]] — B-075 detail.
