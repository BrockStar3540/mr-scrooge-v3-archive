---
type: timeline
status: living
tags: [scrooge, history, V1, V2, V3, institutional-memory]
date: 2026-05-11
trust: high
evidence:
  - exec summary Feb 26, 2026 (scrooge-v1-exec-summary-feb-2026.md)
  - GitHub mr-scrooge repo 50 commits Mar 19 - Apr 15
  - Dropbox archive daily notes (Mar 6, 11, 12, 24)
  - AUDIT.md / NOTES.md / SCORING_V3.md from V1 repo
  - mr-scrooge-v3 commits Apr 15 onward
---

# Mr. Scrooge — Bot Evolution Timeline (V1 → V2 → V3)

Chronological narrative of how the Mr. Scrooge bot family evolved from the original Feb 2026 box-reversal design to the current regime-aware V3 architecture. Drawn from the doctrine doc, GitHub commit log, daily notes, audit log, and the current research arc.

This document is meant to be readable as a narrative (eventual video-series companion), not a dense technical spec. For code-level detail, follow the cross-references.

## TL;DR

| Era | Approx dates | Identity |
|---|---|---|
| **Pre-history** | early Feb 2026 | Doctrine document drafted; bot under development |
| **V1 Genesis** | Feb 26 – Mar 4, 2026 | Initial deployment; multiple audit passes; performance cutoff established |
| **V1 Discipline** | Mar 5 – Mar 19 | Production fixes, RR tuning, Shark Audit transfer, MASTER_THEORY realignment |
| **V1 Crisis** | Mar 19 – Mar 20 | 30m box experiment failed; 17-bug overhaul; revert to baseline |
| **V1 Profitable Window** | Mar 20 – Apr 3 | Restored daily box, fixed pip stops, 50% ratchet — the era ORIGINAL_CONFIG remembers |
| **V1.5 / V2 Bridge** | Apr 3 – Apr 15 | Dual-loop architecture, pair profiles, 4-actor coordination, V3 scoring system |
| **V2** | Mar 21 – Apr 15 (parallel) | Modular rewrite (38/38 modules); coordinator.py architecture; silently decommissioned |
| **V3** | Apr 15 onward | New repo (`mr-scrooge-v3`), regime-aware multi-strategy, Phase-2 minimal walker |

## Pre-history (early Feb 2026)

The doctrine document `trading_bot_exec_summary_v11.docx` is dated **Feb 26, 2026** and captures a fully-formed design before live deployment:

- **Box theory** as core philosophy — PDH/PDL as liquidity magnets, retail vs institutional behavioural pattern, sucker-move terminology
- **Three-timeframe stack**: D for box, H1 for magic lines, M5 for entry
- **Six-gate signal confirmation**: Zone, ATR, Pitchfork, OTR, Sucker move, Trend regime
- **Pitchfork taxonomy** with explicit thresholds:
  - John Wick: wick ≥60% range, body ≤30%, wick ≥2× body
  - Power of Towers: full engulfing including wicks
  - Standard pitchfork: 3-5 directional + reversal close
- **Three bots planned**: Mr. Scrooge (forex/OANDA), Mr. Sprite (crypto/Kraken), Mr. Burns (volatility breakout)
- **Lestat authority matrix** — agent governance for cross-bot decisions
- **Trading universes**: 24 forex pairs, 20 crypto pairs

The doctrine doc records THREE formal audit passes worth of bugs (pre-deployment 9 items, live deployment 12, first-session more), confirming that significant code work happened in February that landed before March 4.

See `wiki/systems/scrooge-v1-doctrine-highlights.md` for the full doctrine snapshot.

## V1 Genesis (Feb 26 – Mar 4, 2026)

Bot deployed live on OANDA practice account. Initial production proved the design but surfaced execution issues that the doctrine doc records resolving across two audit passes.

The most consequential cutoff is established here: **2026-03-04 23:00 UTC** is the "performance cutoff" — pre-cutoff data is declared pre-fix noise and excluded from strategy scoring. This is the line in the sand between "we were debugging the bot" and "the bot was actually trading."

Two backups of `main.py` and `core/fee_calculator.py` from `20260226T2154` and `20260226T2209` survive in the Dropbox archive, capturing the pre-cutoff state.

## V1 Discipline (Mar 5 – Mar 19)

The bot is now live and the first auditable production era begins. AUDIT.md and the daily notes capture the work:

### 2026-03-05 — Initial production audit
- Multiple live bot instances were running concurrently (duplicate log lines confirmed)
- Added non-blocking file lock (`logs/mr-scrooge.lock`)
- Added orphan-process sweep to `start.sh`
- Stale phase-heavy docs replaced with concise operational references

### 2026-03-06 — RR reduction + cooldown policy
- `min_risk_reward`: `1.75 → 1.60`
- Native-close reconciliation policy: profitable closes skip cooldown
- Added `get_trade_realized_pl(trade_id)` to `core/oanda_client.py`
- Naming standardized: `mr-scrooge` (forex) + `mr-sprite` (crypto)
- Hourly green-capital release introduced

### 2026-03-07 — Net floor normalization + green recycle speedup
- `min_net_profit_pips = 7` — pip-normalized floor (was absolute, broke on JPY vs non-JPY)
- `hourly_green_exit_minutes`: `60 → 30`

### 2026-03-08 — Shark Audit Transfer
Execution-accounting rigor copied over from Mr. Sprite:
- `close_position()` accepts `pnl_override`
- `place_market_order()` returns `realized_pl` from OANDA fill components
- `daily_loss` updates from actual `close_pnl` (not pre-close model)

### 2026-03-11 — MASTER_THEORY realignment (HISTORIC PIVOT)

This is one of the most important pivots in the V1 era. A full audit against the source transcripts — *Doug & Sylvia's Liquidity Sweep Reversal Framework* — found the prior implementation had **invented quantitative rules not in the transcripts** (~55-65% rule fidelity, ~30-40% numerical fidelity).

The response:
- Created `MASTER_THEORY.md` — raw quotes from transcripts, no interpretation. Single source of truth.
- Deleted `BOX_THEORY.md` (over-engineered)
- **Sucker move logic rewritten**: strict consecutive-candle counting → flexible window (counts directional candles within `max_candles + 2`, sucker moves can be "messy/choppy")
- **Stop placement standardized**: always at signal candle extreme, never at box wall
- **Trigger prices**: always candle high/low (`h × 1.0001` / `l × 0.9999`), never zone price
- **ATR gate (Gate 3) demoted to advisory** — always passes, logs warning. MASTER_THEORY has no ATR consumption requirement.
- **OTR gate (Gate 6) demoted to advisory** — same reason
- **Trend filter (Gate 2) made tier-aware**: Tier 1/2 zones override trend block ("because we're at the lower part of the box I would prefer to trade long")
- **Time exit**: hard 30-min → 4-hour backstop, only fires if price moved AGAINST trade
- **`max_hold_minutes`**: 30 → 240
- **`max_reentries_per_setup`**: 1 → 3 (transcripts: no hard limit stated)
- **Hybrid trailing stop**: max(candle_trail, profit_lock at 70% of peak, peak − 1.5×ATR)
- **`time_exit_cooldown_minutes`**: 360 → 15 (transcripts: "as soon as I got stopped out, I was looking for re-entry")

The cumulative effect: V1 went from a tight rule-based system that didn't match source theory to a looser system that did. Two of the original six gates became advisory.

### 2026-03-12 — Green-exit crisis & SL-advancement-only redesign

A critical bug: the bot was entering an **infinite retry loop** when trying to set a LIMIT TP order via OANDA after price had already reached/passed the target. OANDA rejects LIMIT orders where the limit price is at/past the market. The `green_exit` / `set_tp` handlers fired every cycle with no escape.

The fix was a complete architectural change:
- **Removed all reactive TP-setting and market-order exit logic**
- Bot becomes **SL-advancement only** — trade management never places market orders
- OANDA's native GTC LIMIT TP (set at entry as TP2) handles the exit without bot intervention
- New 3-stage ratchet-only SL advancement:
  - Stage 1 (Break-even): SL to entry when price reaches 50% to TP1
  - Stage 2 (TP1 lock): SL to TP1 when price passes TP1
  - Stage 3 (Hybrid trail): max(hourly_candle_low, entry + 80% × peak_profit, peak − 1.5×ATR)
- **Ratchet-only — never loosens** (selected as `max(candidates, key='price')` for longs, `min(...)` for shorts)

This is the moment Scrooge's trade management settles into a discipline that survives — in spirit — through V2 and into V3.

### Daily notes Mar 06–24 capture the texture
The Dropbox `archive/DAILY_NOTES_*` files preserve day-by-day records of what was tried and what worked. These are the kind of operational notes that don't make it into commit messages.

## V1 Crisis (Mar 19 – Mar 20)

The 30-Minute Box Experiment. AUDIT.md records it bluntly: **"Rolling 12-hour box was too unstable — zones shifted constantly, entries lost alignment with daily structure. 23 commits introduced. Bot stopped making money."**

Everything was reverted to commit `1c99ae2` (the original profitable version) over a 2-day overhaul. **17 bug fixes** were applied during the revert process, ranging from JPY margin sizing (formula was using `current_price × margin_rate`, wrong for cross pairs — fixed to `base_price_usd × margin_rate`) to equity source change (`NAV → balance`) to fill-anchored SL/TP recalculation after OANDA fill.

What was kept from the failed 23 commits:
- Opportunity scoring (0-100 pts) on `SignalResult`
- Ranked entry selection
- `_fire_entry_candidate()` extraction
- ON DECK dashboard display
- Dashboard improvements (gate chips, config tab, alltime/daily PnL)
- All dead-code removal from the audit

The 17 fixes are catalogued in detail in `scrooge-bug-catalog`.

## V1 Profitable Window (Mar 20 – Apr 3)

After the revert, the bot enters what `ORIGINAL_CONFIG.md` later calls "the settings that were performing well before the March 25-26 changes":

- `margin_utilization_pct = 0.50`, `max_concurrent_positions = 1`
- `min_risk_reward = 1.60`, `max_eur_positions = 2`
- `zone_proximity_pct = 0.25%`, `sl_floor_pct = 0.50%`
- Fixed pip stops: `SL=10`, `TP1=10`, `TP2=30`
- Harvester tiers at 1.5% / 3.0% / 4.5% equity (~4.5p / 9p / 13p)
- 50% ratchet at 5-pip breakeven trigger

This is the only V1-era configuration explicitly preserved as a rollback target. It represents the system at its empirically-best.

## V2 (Mar 21 – Apr 15, parallel track)

On **2026-03-21 23:38**, commit `d28e98b`: *"mr-scrooge-v2 initial build — all 6 phases complete, 38/38 modules clean"*. A complete modular rewrite happened in parallel to V1's bug fixes:

- New file structure: `box/`, `experiments/`, `coordinator.py`, `alerts.py`
- Removed monolithic `dashboard.html` / `dashboard.py`, consolidated `AUDIT.md` / `README.md` / `SCROOGE.md`
- Refactored `core/execution_router.py` (-37%), `core/oanda_client.py` (-3% but cleaner)
- 632-line `coordinator.py` replaces large chunks of `main.py`

V2 ran in parallel to V1 during late March and early April. Notable V2-specific bug:

### 2026-03-24 — V2 silent skip (4.5 hours)
Commit `3203cfe`: a single `return None` at 8-space indent in `coordinator.py:process_instrument()` should have been at 12-space. **The bot returned for every symbol on every cycle for ~4.5 hours, silently skipping all signal evaluation.** No errors, no log gaps — appeared healthy.

V2 has only one branch in the GitHub `mr-scrooge` repo (no unique commits ahead of main visible in the snapshot we recovered). It was effectively a parallel track that fed back into the main V1 repo's evolution rather than diverging.

## V1.5 / V2 Bridge (Apr 3 – Apr 15)

NOTES.md records sophisticated additions in this era:

### 2026-04-03 — Fast Execution Loop + Pair Profiles
- **3-tier pair profiles** (tight/medium/wide) with per-pair SL limit trigger, offset, fallback, fast-market multiplier, green offset
  - Tight (EUR_USD, AUD_USD, EUR_CAD): trig=2p, offset=1.0, fallback=3.0, fast_mult=2.5×
  - Medium (GBP_USD, USD_JPY, NZD_USD, USD_CHF, USD_CAD, EUR_JPY): trig=4p, offset=1.5, fallback=5.0
  - Wide (GBP_JPY, CHF_JPY, NZD_JPY, AUD_JPY, AUD_CHF): trig=6p, offset=2.0, fallback=7.0
- **Hybrid SL Limit System**: proactive REDUCE_ONLY limit when price approaches stop within `trigger_buffer`. OANDA native SL kept as hard backstop. Fast-market detection skips limit when candle range ≥ `fast_mult × avg`.
- **Green Exit → LIMIT order**: REDUCE_ONLY limit at `bid − green_offset` (long) / `ask + green_offset` (short), 300s expiry
- **Fast Execution Loop**: 3-second daemon thread for SL-limit placement + fill monitoring; 5-minute slow loop for decisions. `threading.Lock` prevents race conditions. Implemented in both V1 and V2.
- **Regime visibility on dashboard**: REGIME_BLOCKED, REGIME_FLOOR, REGIME_HYSTERESIS action types with red banners on signal cards AND box cards (was silent blocking before)

### 2026-04-10 — 4-Actor Trade Coordination (Phase 1)
Trade audit found **4 independent actors** (bot, ratchet, SL-limit, harvester) modifying the same OANDA trade with NO SHARED STATE. SL-limit spammed 46 API calls on a dead position. Ratchet/harvester raced on SL moves.

The fix introduced `TradeCoordinator` — file-backed cross-process state at a shared coordination file:
- Bot registers trades at entry, marks dead on vanished detection
- Fast loop checks `is_trade_alive` gate before SL-limit placement
- Ratchet checks `sl_owner` before pushing SL
- Ratchet reads `tiers_hit` from coordination file to sync `partial_1_taken`
- `place_opposing_limit` detects `NO_POSITION_TO_REDUCE` cancels (fixed the 46-order spam)

This is a watershed: **multi-process trade state** is real. The lesson carries directly into V3's architecture.

### 2026-04-15 — V3 scoring system goes live
Commit `c5b5cc3`: *"V3 scoring system: hybrid formula with pair layer, regime/BB gates loosened, dashboard updated"*. The `SCORING_V3.md` doc records the methodology:

- 10 scoring formulas tested simultaneously (M1-M10)
- Selected: **WR-Lift Hybrid with Pair Layer**
- 100% WR at threshold ≥ 5 on OOS test (9W/0L from 20 trades)
- The OLD formula (V1/V2 pre-fix) had separation of +0.5 pts and was never profitable at any threshold

This is the moment the bot graduates from rule-based gates to learned scoring.

## V3 (Apr 15 – present)

After commit `c5b5cc3`, work moves to a new repo: `mr-scrooge-v3`. V1's repo is decommissioned 2026-04-15 (per memory). The new V3 architecture:

- 232-line `runtime.py` conductor + 8 extracted modules (`bootstrap`, `runtime_context`, `scan_coordinator`, `execution_coordinator`, `position_coordinator`, `services/`)
- 5 strategies registered: reversal, trend (disabled), direct, dbb_trend, plus the V3HybridScorer
- 4 classifiers: bb_state, regime, opening, structure
- Regime-aware routing as first-class architecture (ADR 3001 captures this decision)

Then in rapid succession:

### Late April — branched scorer research
Per-strategy ML edge found 2026-04-28: dbb_trend AUC 0.774 / 71.8% WR at p ≥ 0.5. Direct strategy near-noise. ML hard-filter mode adopted.

### 2026-04-29 — Ratchet 0.7 experiment
Single-line config test, `ratchet_lock_pct 0.5 → 0.7`. Rolled back 2026-04-30 after 27 trades / −$245/trade.

### 2026-04-30 — Stale harvest race + ratchet rollback
Two-pass hotfix shipped. 9 regression tests added.

### 2026-05-04 — Strategy attribution patches A + B.right
- Patch A (`492a999`, 06:38:45 UTC): `strategy` field threaded through `AuditEvent`
- Patch B.right (`73f1e41`, 06:50:53 UTC): deterministic `(order_id) → (strategy, scan_cycle)` linkage via `OrderAttributionWriter`

These two patches close the largest data-quality gap of V3 era — before them, strategy attribution was fundamentally unreliable on losers and most trades.

### 2026-05-04 — Drawdown alerts armed
`scrooge-drawdown-alert.timer` live. Daily ≤ −2.7%, circuit trip, cumulative ≤ −6.5% from rollback baseline.

### 2026-05-05 — Close-out + frozen constraints
12 constraints locked into `scrooge-frozen-constraints.md`. Charlie marked SKIP. Session put in HOLD.

### 2026-05-08 to 2026-05-10 — v2 research arc + live broker audit
- v1 full corpus run completed 2026-05-08 (1.45M trades, 0 survivors under locked Stage 5 gates)
- v2 threshold freeze: Echo discriminator timeframe-mismatch bug caught + fixed via Option 1 (current_M5_range / mean_prior_20_M5_ranges); see postmortem 2026-05-08
- Live broker forensic audit: 196 trades, 6-class taxonomy, winner clusters identified
- Charlie reintroduced from SKIP based on audit evidence (15 winners across 2 Charlie probes)
- Two v2 probes promoted: `charlie_pullback_continuation_v2` + `alpha_extended_fade_v2`. Parents retired.
- v2 full corpus run launched 2026-05-10 13:01 UTC (in flight, ~57hr)

See [[v2-post-audit-state-2026-05-10]] for the current state.

## Threads that survive across versions

A few design decisions persist through every transition:

| Idea | V1 expression | V2 expression | V3 expression |
|---|---|---|---|
| **Box theory** | PDH/PDL with percentile filter | Same with refactored modules | Bollinger band rails (smooth analog) — Echo regime |
| **Pitchfork signal** | John Wick / Power of Towers / Standard | Same | Wick-rejection condition in echo_box_fade_v2 (looser thresholds) |
| **Multi-timeframe** | D/H1/M5 explicit | Same | `replay_context` builds D/H1/M5 snapshot per scan |
| **Six-gate discipline** | 6 sequential gates, no overrides | Same (2 advisory after MASTER_THEORY) | Per-probe 3-5 deterministic conditions |
| **SL-advancement-only** | Established Mar 12 | Inherited | Phase-2 minimal walker (no BE/ratchet in current research) |
| **Performance cutoff discipline** | Mar 4 cutoff | Same | Live broker audit window = post-attribution-fix cohort |
| **Ratchet-only (never loosens)** | Mar 12 | Same | Implicit in walker design |
| **Re-entry on liquidity sweep** | Mar 11 — 1/setup raised to 3 | Inherited | NOT in v3 walker — potential feature gap |

## Threads that died

| Idea | Why dropped |
|---|---|
| **Mr. Sprite (crypto)** | Removed entirely 2026-03-25. Crypto-specific bugs (zone_proximity, position size overflow on low-priced coins, Kraken precision) burdened the codebase. |
| **30m rolling box** | Failed Mar 19-20 experiment. Daily PDH/PDL restored. |
| **Reactive market-order exits** | Green-exit crisis 2026-03-12 eliminated all `time_exit` / `set_tp` / `partial_tp` market orders. Bot never places market orders again. |
| **Global score / single weights** | V3 ADR 3001 closed this direction permanently. |
| **Strict ATR + OTR gates** | Demoted to advisory 2026-03-11 (MASTER_THEORY audit said transcripts have no such requirement). |
| **Decompressors (sizing multipliers)** | Removed Mar 19-20 overhaul. Sizing is straight 80%. |
| **Universal R-multiple in v2 probes** | Refined to per-probe target_hypothesis 2026-05-10 (live audit evidence). |

## Pivots worth video-series treatment

For a future evolution video, these are the highest-narrative pivots:

1. **The 30m box experiment failure (Mar 19-20)** — 23 commits over 2 days that broke profitability, the discipline of reverting all of them, the 17 incidental fixes kept from the failed experiment
2. **MASTER_THEORY realignment (Mar 11)** — discovering that the code had invented rules not in the source transcripts, deleting BOX_THEORY.md, demoting two of six gates
3. **Green-exit crisis (Mar 12)** — infinite retry loop in production, decision to remove all reactive TP-setting and become SL-advancement-only
4. **4.5-hour silent V2 outage (Mar 24)** — single indentation error, no logs, no alerts, healthy-looking bot, four and a half hours of zero signals
5. **4-actor coordination revelation (Apr 10)** — finding that the bot, ratchet, SL-limit, and harvester were all modifying the same OANDA trade with no shared state, and the 46-order API spam that revealed it
6. **V3 scoring system (Apr 15)** — testing 10 formulas, picking WR-Lift Hybrid with Pair Layer because it was 100% WR at threshold ≥5 on a 9-trade OOS validation
7. **Charlie's death and resurrection (May 5 → May 10)** — frozen as SKIP based on theory-clean replay evidence, then reintroduced 5 days later based on 90-day live broker audit showing 15 winners

## Cross-references

- [[scrooge-v1-exec-summary-feb-2026]] — original doctrine document (verbatim)
- [[scrooge-v1-doctrine-highlights]] — scannable doctrine index
- [[scrooge-bug-catalog]] — every documented bug, organized by era
- [[scrooge-current-state-2026-05-05]] — superseded snapshot
- [[v2-post-audit-state-2026-05-10]] — current state of V3 research arc
- [[scrooge-frozen-constraints]] — currently locked design decisions
- [[scrooge-strategy-regime-playbook-matrix]] — v0.1 (V1/V2-era) and v0.2 (current)
- GitHub: `BrockStar3540/mr-scrooge` — V1/V2 history (50 commits)
- GitHub: `BrockStar3540/mr-scrooge-v3` — V3 active development
- Dropbox: `/Users/brock-mini-mac/Dropbox/SCROOGE V3/archives/mr-scrooge-v1/` — local working copy
- mr-scrooge-v3 repo: `docs/decisions/` — ADRs (1001+ V1, 2001+ V2, 3001+ V3)

---

# Era 5 — Matrix integration & ML routing (2026-05-11 → 2026-05-30)

The arc that took V3 from a 14-gate hand-tuned admission stack to a
lab-mined ML-routed system. Three months of mining produced an 838k-trade
corpus; the May 11 → May 30 window is when that mining finally became
the live admission signal instead of an offline reference.

## Why this era happened

By early May the gate pipeline had accumulated 14 gates encoding overlapping
slices of the same per-(pair × family × direction × session) decision. Each
gate had its own bucketing, its own log format, its own audit trail. A
single candidate could be evaluated against the same factual question 4× under
4 different rule sets, with diverging verdicts.

Meanwhile the matrix-mined optimized cells + factor lift tables encoded all
of that decision-making in one place, learned from the corpus, with per-cell
explainability. The matrix was sitting offline being correct; the gates were
in production being approximately correct in seven different ways.

The May 11 → May 30 arc is the collapse of that duplication into a single
routing-table + LightGBM gate, with the raw matrix wired in alongside as a
shadow advisor for cross-validation.

## Chapter 1 — The losing streak and the diagnostic arc (April 28 → May 4)

A 48h losing streak (16 trades, 6.2% WR, 11/11 long disasters into JPY
downtrend, −$5,350 total) forced a stop-the-bleeding investigation. The
arc:

- **2026-04-28** — Initial diagnosis (#17). Found per-strategy ML observer
  edge varied wildly — `dbb_trend` had AUC 0.774 / 71.8% WR at p≥0.5, but
  `direct` was near-noise.
- **2026-04-29 → 04-30** — Two infrastructure hotfixes shipped in
  parallel: stale-harvest LIMIT two-pass orphan safety (ADR 3003), harvest
  same-cycle race fix + ratchet 0.7 → 0.5 rollback (ADR 3004). Neither
  addressed the streak directly; both removed compounding failure modes
  that had been masking the upstream signal issue.
- **2026-05-04** — Three-front coordinated work: branch-scorer research
  arc opened (ADR 3002), B-1 attribution architecture diagnosed and
  Patches A + B.right shipped (ADR 3006), Telegram drawdown alerter went
  live (ADR 3007). 60d broker-truth pull surfaced 152 trades / 39.6% WR /
  −$30,958. 47-factor audit found 15 factor sign-flips between DBB and
  Direct — concrete evidence that branched scoring was the right
  direction.
- **Decision:** Hold LightGBM at threshold 0.55 (Track A; ADR 3005)
  pending matrix integration. Don't tighten until we can measure properly.

## Chapter 2 — MatrixRouter and the cell-level architecture (May 11 → May 25)

By May 11 the matrix was mature enough to replace the gate stack. The
two-week arc:

- **2026-05-14** — MatrixRouter architecture decision (ADR 3008): one gate
  reads one parquet table, encoding what 7 gates had encoded separately.
- **2026-05-18** — ML observer retrained on cluster serials, not regime
  labels (ADR 3009). Cluster serials are the matrix's primary key;
  regime labels were a derived view.
- **2026-05-22** — `factor_buckets v3` (ADR 3010): RSI 4→8, BBP 4→7,
  ZS 4→7, ADR 4→6 buckets, driven by neighbor-WR validation.
- **2026-05-23** — Decision forest built (ADR 3011): per-combo + global
  trees on top of factor_lift, capturing pairwise interactions.
- **2026-05-25** — Three same-day cleanups: loser-veto policy upgrade for
  MatrixRouter (ADR 3012), two new quality gates (ADR 3013), and
  EntryFilter.enable_family_loose_override default flipped OFF (ADR 3014).

## Chapter 3 — The collapse to ML routing (May 27 → May 29)

Three days of structural work that effectively redefined the system:

- **2026-05-27** — Strategy promotion day (ADR 3016):
  - HTF gate promoted observe → HARD (ADR 3015), then retired same day in
    favor of MatrixRouter cell-level enforcement.
  - 6 research strategies promoted to live (ifvg, session_breakout,
    compression_expansion, trend_pullback, chaikin_macd_atr,
    compression_reversion).
  - New routing table `v10_fast_v1_14b_full_matrix.parquet`: 1737 rows,
    250 leaves.
  - B-1 Patch C (commit 64410a3) fixed scan-dashboard JSON-stripping
    that was blinding the ML observer + broker attribution — the third
    attribution patch in a month.
- **2026-05-28** — V3HybridScorer disabled (ADR 3017). LightGBM v0
  promoted to PRIMARY GATE at threshold 0.75. ml_router demoted to
  shadow. DailyCircuitGate config-disabled (ADR 3018). 4-layer matrix
  cascade and monolith MatrixRouterGate commented out — "ML router
  supersedes — strategies pre-filtered by per-pair rules."
- **2026-05-29** — Matrix wired as shadow advisor (ADR 3019). Raw matrix
  CSVs (`optimized_matrix_by_session.csv`, `factor_lift_table.csv`)
  loaded at boot; `matrix_shadow.observe()` fires alongside
  `lightgbm_shadow.observe()` on every picked candidate. Three parallel
  observers: LightGBM (gate), matrix shadow, ml_router shadow.

## What the system looks like at end of era

See `LIVE_SYSTEM_SPEC.md` (2026-05-30 rev) for the executable truth.
Headline shifts from the V3.1 doctrine:

| V3.1 (April spec) | V3 May 30 |
|---|---|
| 14 gates | 7 active gates (5 retired, 6 commented out) |
| V3HybridScorer = primary edge call | V3HybridScorer DISABLED |
| Session × family threshold tiering | LightGBM v0 @ 0.75 = primary gate |
| BB-state → strategy routing | routing_table_v10_fast_v1_14b parquet (1737 rows) |
| 3 active strategies | 13 registered, 7+ actively routed |
| 1 audit JSONL (execution-audit) | 7 JSONLs incl. 3 parallel ML observer streams |

## Pivots worth video-series treatment (additions to the Era 4 list)

8. **The $5,350 losing streak (April 28 → May 4)** — 48h, 16 trades, 6.2%
   WR, 11/11 long disasters into JPY downtrend; the diagnostic arc that
   pulled out B-1 attribution, harvest race, ratchet rollback, drawdown
   alerter, and the matrix integration thesis in a single coordinated
   response.
9. **MatrixRouter collapse (May 14 → May 28)** — 14 gates to 7, the
   moment the matrix mining became the live admission decision instead
   of an offline reference. Two weeks; 7 retirements, 4 commented out,
   the V3 scorer disabled at the end.
10. **LightGBM PRIMARY GATE (May 28)** — single config commit ending a
    year of hand-tuned scoring. Threshold 0.75 = top ~3% of lab cohort
    = ~75% sim WR.

## Cross-references

- ADRs 3002 through 3019 — full decision trail for this era
- `LIVE_SYSTEM_SPEC.md` — current executable truth (2026-05-30 rev)
- `matrix-integration-era-may-2026.md` (this directory) — focused arc retrospective
- Vault project pages:
  - `wiki/projects/scrooge-v3-attribution-brokertruth-factors.md`
  - `wiki/projects/scrooge-v3-branch-scorer-research.md`
  - `wiki/projects/scrooge-v3-dbb-loser-audit.md`
  - `wiki/projects/scrooge-v3-harvest-same-cycle-race.md`
  - `wiki/projects/scrooge-v3-stale-harvest-hotfix.md`
  - `wiki/postmortems/fixes/scrooge-v3-strategy-promotion-2026-05-27.md`
