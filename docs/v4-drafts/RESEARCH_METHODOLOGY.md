# Research Methodology

How the data corpus, factor signature, matrix, per-pair modules, and
LightGBM model were built. Companion to
[`LAB_REPRODUCTION_GUIDE.md`](LAB_REPRODUCTION_GUIDE.md) (step-by-step
instructions) and [`ARCHITECTURE_DIAGRAM.md`](ARCHITECTURE_DIAGRAM.md)
(visual flow).

Audience: a researcher who wants to understand the design choices
(*why* the pipeline is shaped this way), not just the mechanics. For
"how do I run it myself," see the reproduction guide.

---

## Table of contents

1. [Data acquisition](#1-data-acquisition)
2. [Feature engineering — factor_buckets v3](#2-feature-engineering--factor_buckets-v3)
3. [Lab harness](#3-lab-harness)
4. [Matrix mining](#4-matrix-mining)
5. [Per-pair module building](#5-per-pair-module-building)
6. [LightGBM training](#6-lightgbm-training)
7. [Routing table assembly](#7-routing-table-assembly)
8. [Known limitations](#known-limitations)

---

## 1. Data acquisition

**Source:** OANDA REST API (`/v3/instruments/{instrument}/candles`).

**Universe:** 27 forex pairs. The 26 majors + USD/MXN (originally
included; structurally problematic — see
[Task #51](https://github.com/BrockStar3540/mr-scrooge-v3/issues/51)).

```
USD pairs:   EUR/USD GBP/USD USD/JPY AUD/USD USD/CHF
             USD/CAD NZD/USD USD/MXN
JPY crosses: EUR/JPY GBP/JPY AUD/JPY CAD/JPY CHF/JPY NZD/JPY
GBP crosses: EUR/GBP GBP/CAD GBP/AUD GBP/NZD GBP/CHF
EUR crosses: EUR/CAD EUR/AUD EUR/NZD EUR/CHF
Other:       AUD/CAD AUD/NZD AUD/CHF NZD/CAD NZD/CHF
```

**Timeframes pulled:**

| TF | Use |
|---|---|
| M5 | Primary scan timeframe; bucket signature computation |
| H1 | ATR_1h calculation; HTF alignment |
| D1 | Daily range (ADR); HTF20/HTF60 alignment buckets |

**Date window:** primary lab corpus runs **2025-11-25 → 2026-05-25**
(6 months). Deeper history available (M5 back to 2019-07-01) for
walk-forward validation and regime-comparison work.

**Caching:** All candles cached as parquet files under
`research/replay_lab/cache/`. Filename convention:
`{PAIR}_{TF}_{FROM}_{TO}.parquet`. Cached files are immutable;
re-pulls write to new timestamped files. The cache avoids re-pulling
during repeated experimental sweeps.

**Why OANDA-specific:** the bot is OANDA-only by design (see
[ADR](decisions/) trail on the "no broker abstraction" decision). The
lab inherits this — pip sizes, instrument conventions, and spread
modeling are baked in.

---

## 2. Feature engineering — factor_buckets v3

The system encodes every market moment as a **14-bucket signature**.
Each bucket is a discrete string label derived from a continuous
feature crossing pre-defined thresholds.

Full code: `src/scrooge/features/factor_buckets.py`. The current
revision is `v3`, expanded from v1/v2 per neighbor-WR empirical
validation ([ADR 3010](decisions/3010-factor-buckets-v3-expansion.md)).

### The 14 buckets

| Bucket | What it captures | # values | Sample labels |
|---|---|---|---|
| **BB** | Bollinger width vs stop | 4 | `BB0` (tight) → `BB3` (wide) |
| **BBP** | BB position (price within band) | 7 | `BBP0` (deep below) → `BBP6` (deep above) |
| **A5** | M5 ATR vs stop | 4 | `A5_0` (low vol) → `A5_3` (high vol) |
| **A1** | H1 ATR vs stop | 4 | `A1_0` → `A1_3` |
| **RSI** | RSI(14) zone | 8 | `RSI0` (<20) → `RSI7` (>80) |
| **E20** | EMA20 slope (vs trade direction) | 5 | `E20a` (steep with) → `E20e` (steep against) |
| **E50** | EMA50 slope (vs trade direction) | 5 | `E50a` → `E50e` |
| **ZS** | Price Z-score | 7 | `ZS0` (deep -3) → `ZS6` (deep +3) |
| **SPR** | Spread vs stop | 4 | `SPR0` (cheap) → `SPR3` (expensive) |
| **ADR** | Daily range consumed | 6 | `ADR0` (fresh) → `ADR5` (shock-day) |
| **H20** | HTF20 alignment (vs trade) | 5 | `H20a` (aligned) → `H20e` (against) |
| **H60** | HTF60 alignment (vs trade) | 5 | `H60a` → `H60e` |
| **T1** | 1H trend alignment | 3 | `T1a` (with) / `T1b` (neutral) / `T1c` (counter) |
| **T4** | 4H trend alignment | 3 | `T4a` / `T4b` / `T4c` |

### Why discrete buckets, not continuous features?

Two reasons:

1. **Factor lift requires discrete cells.** The matrix mining computes
   "what's the realized R conditional on this bucket label" — a
   continuous feature would have infinitely many cells with N=1 each,
   meaningless.
2. **Bucket boundaries are *meaningful* boundaries.** RSI 28 vs RSI 32
   isn't a meaningful trading difference; RSI <30 vs RSI 30-40 is. The
   bucket boundaries encode trading-relevant thresholds rather than
   numerical similarity.

### Why these 14?

They evolved through empirical validation. v1 had 11 buckets; v3 added
HTF-alignment buckets (T1/T4) after the HTF king-factor finding (matrix
factor_lift +0.177 for `cand_vs_htf20_mismatch`, three-way confirmed
[here](https://github.com/BrockStar3540/mr-scrooge-v3/commit/535b087)).

### What bucket boundaries are NOT in the signature?

Deliberate omissions:

- **No raw price.** Price is normalized away via pip sizing.
- **No timestamp.** Session is captured by `session_bucket` separately
  in routing rules, not in the signature itself.
- **No volume.** OANDA doesn't ship reliable volume data; using it
  would invite correlation-with-broker-quirks rather than market.
- **No order-book depth.** Practice account doesn't expose it.

---

## 3. Lab harness

The lab is a Python wrapper around the
[`backtesting.py`](https://kernc.github.io/backtesting.py/) library
plus custom dispatch logic for strategy-variant testing.

**Core wrapper:** `research/harness/strategy_wrappers.py`
- `_SingleProbeStrategy` — backtest one isolated strategy at a time
- `instantiate_live_strategy()` — dispatcher mapping strategy_id → probe

**What gets backtested:**

```python
for strategy in [25 variants]:
    for pair in [27 pairs]:
        for direction in [native, reversed]:
            run_backtest(
                strategy=strategy,
                pair=pair,
                direction=direction,
                start=NOV_25,
                end=MAY_25,
                start_equity=$50_000,
                entry_mode="market",       # NOT signal — see harness debug notes
                routing_mode="no_router",  # bypass live routing for lab
                exit_config={
                    "sl_pips": 7,
                    "tp_pips": 12,
                    "ratchet_lock_pct": 0.5,  # rolled back from 0.7 per ADR 3004
                    "harvest_fraction": 0.5,
                },
            )
```

**Output per (strategy × pair × direction):**

- `trades_{PAIR}_{VARIANT}_{DIRECTION}.csv` — one row per trade
  (EntryTime, ExitTime, EntryPrice, ExitPrice, SL, TP, PnL, etc.)

**Aggregated per variant:** `per_variant_{VARIANT}.csv` — one row per
(pair, direction) with `n_trades, wins, losses, wr, pnl_sum, pnl_mean`.

### Critical harness gotchas (preserved here for future-me-or-Claude)

These bit hard during the Phase 3 development arc:

1. **`entry_mode="signal"` at "at-the-money" placed LIMITs the wrong
   side of spread** — `backtesting.py` rejected them silently. Use
   `entry_mode="market"` or shift the LIMIT geometry explicitly.
2. **`routing_mode="no_router"` does NOT bypass routing if
   `load_routing_table(None)` auto-loads the live parquet.** Pass
   `routing_table=None` AND `routing_mode="no_router"` to truly skip.
3. **Compound sizing inflates dollar amounts wildly.** $50k seed
   compounds to $8.6M on a 70%-WR variant over 6mo. The dollar
   magnitudes are correct, but cross-variant $/trade comparisons can
   be misleading. Use WR + pair breadth as the variant-ranking
   comparators.

### Parallelism

`research/harness/run_phase3_sweep_parallel.py` uses
`multiprocessing.Pool(N)`. The Phase 3 sweep ran with N=2 (memory
constraint on a 16GB Mac Mini); fewer workers if memory-tight, more if
swapping doesn't kick in. Each variant takes ~3 hours wall-clock for
27 pairs × 2 directions on M5 / 6mo data.

---

## 4. Matrix mining

For each (pair × strategy × direction × factor) tuple, compute the
**lift in expected R** when filtering to trades that match each
factor's bucket value.

**Output:** `data/matrix/factor_lift_table.csv` (~10k rows)
+ `data/matrix/optimized_matrix.csv` + `data/matrix/optimized_matrix_by_session.csv`.

### factor_lift_table schema

| Column | Meaning |
|---|---|
| `pair`, `strategy`, `direction`, `factor_name` | The cell coordinates |
| `n_base`, `exp_base` | Baseline (all trades in cell) count + expected R |
| `n_kept`, `exp_kept` | Filtered (matching factor bucket) count + expected R |
| `lift_exp` | `exp_kept - exp_base` — the headline metric |
| `kept_pct` | Fraction of base that passes the filter |

A factor with `lift_exp > 0` and `n_kept > 100` is a real edge signal.
The matrix integration arc (May 14-29) made this the central
admission criterion for the live bot.

### optimized_matrix vs optimized_matrix_by_session

- `optimized_matrix.csv` — collapsed across sessions (5 trading
  sessions per day)
- `optimized_matrix_by_session.csv` — stratified by session
  (asia_london_open, london, ny_active, late_ny, dead_late)

Session stratification matters because some strategies have edge
only during specific liquidity windows (e.g., `session_breakout` by
construction).

### Why "kept_pct" matters

A high-lift filter that only passes 0.1% of trades produces 1 admission
per month — unactionable. The matrix uses `kept_pct` as a coverage
floor: filters that admit too few trades are demoted regardless of
their lift magnitude.

---

## 5. Per-pair module building

For each of 27 pairs, mine a self-contained "knowledge library"
folder under `data/per_pair_modules/{PAIR}/`:

```
data/per_pair_modules/EUR_USD/
├── lib/
│   └── factor_buckets.py     # bundled bucketization code
├── regime_centroids.csv       # 20 KMeans regimes, 7-feature centroids
├── trade_serials.csv          # historical trades w/ 14-bucket signatures
└── manuals/
    └── master_rules.csv       # ~1000 WIN/LOSE rules per pair
```

### Regime classification

KMeans on a reduced 7-feature space (BB, BBP, A5, A1, E20, E50, ADR,
SPR) with `n_clusters=20`. Each regime is a centroid in that space;
labeled `R00`-`R19`.

**Why 20?** Empirically: fewer clusters lose meaningful market-state
distinctions; more clusters dilute sample size per cell. 20 hits the
sweet spot in our 6mo corpus (~838k trades / 27 pairs / 20 regimes ≈
1,550 trades per cell on average).

**Why those 7 features and not 14?** RSI, ZS, H20/H60/T1/T4 vary
within-regime — they're per-candidate features, not per-market-state
features. The 7 retained features capture the *macro* regime (vol,
trend slope, range consumption), while the other 7 capture the
*candidate-moment* details.

### Rule mining

For each (pair × regime × session) cell, the mining loop:

1. Pull all historical trades whose timestamp falls in that cell
2. Bucketize each trade's 14-signature
3. Find bucket *combinations* with WR statistically distinguishable
   from baseline:
   - `WIN` rules: combinations with WR > some threshold + min N
   - `LOSE` rules: combinations with WR < threshold + min N
4. Refine via narrowing: for each candidate rule, search for an
   additional bucket constraint that improves WR further
5. Cap at ~50 rules per cell (median across pairs: 50 rules/cell;
   thin cells have fewer)

**Why pinned vs unpinned strategies?** Most rules are *unpinned* (not
strategy-specific) — they apply to whatever strategy is firing. A few
rules are pinned (`strategy_id=box_master_theory`) when the rule
only holds for that strategy. This permissive routing lets new
strategies inherit rules without re-mining.

---

## 6. LightGBM training

The primary admission gate as of May 28, 2026
([ADR 3017](decisions/3017-v3-hybrid-scorer-disabled-lightgbm-primary.md)).

**Training corpus:** ~838k labeled trades from the 6mo lab sweep
across all strategies, pairs, directions.

**Features (~20 per trade):**

- 14-bucket signature (one-hot encoded → ~50 binary features)
- `pair`, `strategy`, `direction`, `session_bucket` (categorical)
- Auxiliary: regime serial, hour of day, day of week

**Target:** binary `win` (1 if trade outcome is positive R, 0 otherwise).
No regression on R magnitude — empirically `win` proved more learnable
than continuous R given the harvest mechanic compresses the dollar
distribution.

**Training:** standard LightGBM binary classifier:

```python
params = {
    "objective": "binary",
    "metric": "auc",
    "learning_rate": 0.05,
    "num_leaves": 31,
    "min_data_in_leaf": 200,
    "feature_fraction": 0.85,
    "bagging_fraction": 0.85,
    "bagging_freq": 5,
}
```

Time-based **80/20 train/holdout split** (no random — financial data
must be temporally ordered for honest validation). Train on
2025-11-25 → ~2026-04-15; holdout 2026-04-15 → 2026-05-25.

### Reported metrics (v0 model)

| Metric | Value |
|---|---|
| Holdout AUC | 0.6025 |
| WR @ top 25% predictions | 72.83% (+10pp vs 62.5% baseline) |
| WR @ top 10% predictions | 78% |
| WR @ top 3% (threshold 0.75) | **~75% sim** |

### Threshold selection arc

The threshold is the *operational* decision (separate from model
quality):

- **First deploy 2026-05-28: threshold = 0.55.** Top ~10% of cohort.
  Sim WR ~55-65% depending on slice. Track A status quo.
- **Decile sweep on full corpus (2026-05-29):** confirmed bottom decile
  36.5% WR (loser kill) AND top decile 82.3% WR (winner pick).
- **Threshold tightened to 0.75 (same day, 2026-05-29):** drops volume
  83% → 3.1% but lifts sim_WR 54.9% → 75.0% and mean PnL 1.96p →
  5.30p. "Quality over volume" per operational call.

`data/lgbm_v0/model.txt` + `data/lgbm_v0/meta.json` are the live
production artifacts.

### Why LightGBM and not transformers / RL / etc.

Three reasons:

1. **Tabular data fits gradient boosting naturally.** 14-bucket
   signatures are exactly the kind of structured input GBMs excel at.
2. **Fast inference matters.** Live scoring needs to fit inside a 5m
   scan budget across 26 pairs × 25 strategies. LightGBM scores in
   microseconds per candidate.
3. **Interpretability.** Tree models expose feature importance and
   single-tree explanations. The audit story matters in a live-money
   system.

Transformer / RL alternatives were considered ([survey
2026-05-29](decisions/) for examples) — rejected on cost-benefit. The
data is tabular; AUC 0.60 is enough edge; complexity isn't free.

---

## 7. Routing table assembly

The live admission artifact: `data/routing_table.parquet` (~40KB).

**Schema (one row per admissible cell):**

| Column | Meaning |
|---|---|
| `pair`, `family`, `direction`, `session` | Cell coordinates |
| `regime` | Regime serial (R00-R19) |
| `tier` | Quality tier (Seed, Seed-Pro, ...) |
| `n_trades`, `wr`, `mean_r` | Per-cell historical performance |
| `shave_rule` | Per-cell band rule (from hybrid shaver) |
| `factor_ids` | Top-K factors driving the admission |

**Promotion criteria** (cell goes into the table):

- Lab-mined WR ≥ 55% AND
- N trades ≥ 100 AND
- LightGBM holdout-confirmed edge AND
- No conflicting LOSE rule with higher N

Current version: `routing_table_v10_fast_v1_14b_full_matrix.parquet`
(1737 rows / 250 leaves) as of [the May 27
promotion](decisions/3016-six-strategy-promotion-and-routing-v1-14b.md).
File rename to `routing_table.parquet` happens at V4 cutover.

---

## Known limitations

In the spirit of "we measure honestly":

1. **One regime window.** The 6mo lab corpus (Nov 2025 → May 2026)
   was a *bearish-friendly* regime — confirmed three ways (matrix
   factor_lift SHORT > LONG across 11/14 V3 families; Phase 3 lab
   reversion families 100% wrong-direction at 27/27 pairs; live
   broker truth LONG WR 17% vs SHORT WR 35%). Strategies tuned on
   this window may underperform when the regime shifts. The
   [HTF gate](decisions/3015-htf-trend-filter-observe-to-hard.md) is
   the system's regime-direction safeguard but is itself learned
   from this window.

2. **Compound sizing inflates lab dollar magnitudes.** A 70%-WR
   variant grows $50k → $8.6M over 6mo of compounding. The dollar
   numbers are correct but reading them as "per-pip edge" is wrong.
   Use WR + pair breadth + per-pip mean for cross-variant
   comparison.

3. **No walk-forward / temporal OOS validation.** Lab is in-sample by
   construction. To claim a variant generalizes, hold out 1-2 months
   and verify there — [§10 of the HTF
   spec](https://github.com/Envxytrades/htf-spec) we'd apply for
   future strategy adds.

4. **No realistic slippage modeling.** Lab assumes fills at quoted
   prices. OANDA practice slippage is ~0.3 pips on majors, more on
   exotics. Live results will be lower than lab by some friction.

5. **USD_MXN is data-thin.** The pair clustered into fewer effective
   regimes, generated fewer historical trades, and as of 2026-05-30
   has an *empty* `master_rules.csv`. [Task #51](https://github.com/BrockStar3540/mr-scrooge-v3/issues/51)
   for the open-position remediation.

6. **9 (pair × regime) cells have <10 rules** (concentrated in
   CHF/exotic pairs). Admission decisions in those cells are
   statistically weaker than median cells. Flagged for thin-cell
   remediation as part of [Task #41](https://github.com/BrockStar3540/mr-scrooge-v3/issues/41).

7. **The lab harness uses simulated SL/TP execution.** Real OANDA
   trigger-side fills (SL on ASK for shorts, on BID for longs) plus
   spread-blow-out events aren't perfectly modeled. The 4-guard
   StopPlanner ([EXECUTION_PHYSICS](EXECUTION_PHYSICS.md)) handles
   live; lab approximates.

---

## What this methodology gets right (the honest case)

- The corpus is **large** (838k labeled trades), **structured**
  (clean 14-bucket signature), and **time-aligned** (M5 boundaries
  consistent across pairs).
- The mining is **multi-method**: matrix factor lift, per-pair
  regime+rule library, LightGBM scoring — three independent passes
  over the same data. Convergent findings across methods is the
  strongest evidence we have.
- The pipeline is **rebuildable**. Every artifact (matrix, modules,
  LightGBM model, routing table) can be regenerated from the cached
  candle data. No manual handoffs.
- The bot's **live decisions are auditable**. `order-attribution.jsonl`
  links every broker fill to its scoring snapshot. The three shadow
  ledgers preserve disagreement between LightGBM, matrix, and
  ml_router.

The lab is a research instrument, not a profit oracle. It tells us
*what was true* in the 6mo corpus — not *what will be true* in the
next quarter. We use it for that and document the gap openly.
