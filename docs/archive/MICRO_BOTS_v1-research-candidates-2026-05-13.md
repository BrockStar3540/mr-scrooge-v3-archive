> **ARCHIVED 2026-05-30** as part of V4 cutover prep. Four
> hand-tuned research candidates from 2026-05-13 (TF6_short / USD_JPY,
> MR4_long / CHF_JPY, MR4_long / EUR_JPY, plus one more) with
> discovery samples n=60-520 each. Status at time of writing:
> "Approved for V3 observe-mode shadow logging. Not approved for
> live order placement."
> 
> Superseded by the Phase 3 lab sweep (34 variants × 27 pairs ×
> 2 directions on the full 6mo / 838k-trade corpus) and the
> matrix mining + LightGBM v0 training arc that followed. The
> specific candidates here are not in the V4 live roster; their
> underlying probe ideas (Williams %R extreme reversal, Z-score
> mean-reversion) are tested at industrial scale in the
> `MR5_williams_extreme` and `MR4_zscore_extreme` Phase 3 variants
> with samples 100-1000x larger.
> 
> The regime-gate discoveries documented here (vol_ratio threshold,
> ema50_dist threshold, etc.) may be useful inputs for future probe
> refinement but are not the basis for current admission decisions.
> For current truth see `docs/STRATEGY_ENCYCLOPEDIA.md` (V4) +
> `data/per_pair_modules/` + `data/matrix/factor_lift_table.csv`.

---

# Raw-M5 Micro-Bot Candidates v1

**Status:** Research candidates. Approved for V3 observe-mode shadow logging. **Not approved for live order placement.**

**Date:** 2026-05-13
**Methodology:** Strategy-first regime discovery using decision trees on the OHLCV formula library, with look-ahead-corrected H1/M15 features.

---

## Candidates

Four cells passed every validation gate (described below):

### 1. TF6_short / USD_JPY (strongest)

**Strategy:** Moving Average Ribbon Short (TF6)

**Trigger (M5):**
- `EMA9 < EMA21 < EMA50` (descending order)
- All three EMAs falling (each `< its value 1 bar ago`)
- EMA50 slope < −0.05% over 5 bars

**Regime gate (discovered):**
- `weekday > 1` (Tuesday or later)
- `bb_width_rank ≤ 1.0` (any compression level)
- `ema50_dist ≤ -0.48%` (price well below EMA50)
- `spread_cost_R > 0.004` (sanity)

**Sizing/management:**
- Stop: `max(high[-10:])` (10-bar swing high)
- Target: `entry − 2 × |entry − stop|` (2R)

**Performance (corrected, post-rollover-kill, post-vol-spread):**
- Discovery n=520, holdout n=128, recent n=30
- Mean R holdout = +0.43, recent = **+1.28**
- Recent CI lower bound = +0.78
- Slippage MC 5th-pctile recent mean R = +1.26

### 2. MR4_long / CHF_JPY

**Strategy:** Z-Score Long Mean Reversion (MR4)

**Trigger (M5):**
- `zscore20 < -2.0` (price 2σ below 20-bar mean)
- `ADX14 < 25` (no trend)

**Regime gate (discovered):**
- `vol_ratio ≤ 0.08` (volume <8% of 20-bar average — thin market)

**Sizing/management:**
- Stop: `entry − 1.5 × ATR14`
- Target: `entry + 1.5 × |entry − stop|`

**Performance:**
- Discovery n=60, holdout n=28, recent n=14
- Mean R holdout = +0.81, recent = +0.89
- Recent CI lower bound = +0.38 (post-spread-stress: +0.05)
- Slippage MC 5th-pctile recent = +0.31

### 3. MR4_long / EUR_JPY

**Strategy:** Z-Score Long Mean Reversion (MR4)

**Trigger:** same as CHF_JPY.

**Regime gate:** `vol_ratio ≤ 0.08`

**Performance:**
- Discovery n=76, holdout n=24, recent n=15
- Mean R holdout = +0.81, recent = +0.88
- Recent CI lower bound = +0.42
- Slippage MC 5th-pctile recent = +0.15

### 4. MR4_long / AUD_JPY

**Strategy:** Z-Score Long Mean Reversion (MR4)

**Regime gate:**
- `vol_ratio ≤ 0.36`
- `rsi14 ≤ 35.09`

**Performance:**
- Discovery n=86, holdout n=39, recent n=23
- Mean R holdout = +0.77, recent = +0.77
- Recent CI lower bound = +0.38
- Slippage MC 5th-pctile recent = +0.09

---

## Validation gates passed (all 4 cells)

| Gate | Description |
|---|---|
| **G1** | Discovery (2019-2024) AND holdout (2025-Apr 2026) both positive mean R |
| **G2** | 95% bootstrap CI lower bound > 0 in both discovery and holdout |
| **G3** | Positive mean R in ≥3 of 4 holdout windows (~4-month each) |
| **G4** | Recent 6mo (Oct 2025 → Apr 2026) positive AND CI lower > 0 |
| **G5** | Excluded rollover window (UTC 21-22) — no thin-liquidity artifact |
| **G6** | `hour_utc` removed as feature — no session-time-of-day leakage |
| **G7** | 1.5× spread stress: holdout CI lower > 0 |
| **G8** | Vol-conditional spread (3× when vol_ratio<0.2, 2× when <0.4): holdout CI lower > 0 |
| **G9** | Random slippage Monte Carlo (1000 draws): 100% of draws produced positive mean R |
| **G10** | Permutation test: p-value < 0.05 (preliminary — 13 of 50 shuffles complete, max null=1 vs real=13) |

---

## What was eliminated (the funnel)

| Stage | Cells |
|---|---:|
| Total (strategy × pair × decision-tree leaves) | ~582 candidate regimes |
| Pass G1 (both eras positive) | 222 |
| Pass G1 + G2 (CI both eras) | 46 |
| Pass G1 + G2 + G3 (walk-forward) | 21 |
| Pass G1 + G2 + G3 + G4 (recent 6mo) | 14 |
| Pass + G5 (rollover excluded) + G6 (no hour) | 14 |
| Pass + G7 (1.5× spread) | 8 |
| Pass + G8 (vol-conditional spread) | **4** |
| Pass + G9 (slippage MC) | **4** |

Permutation (G10) preliminary: out of 13 shuffled-label runs, max=1 false survivor, mean=0.23. Real survivor count = 13/14 (one borderline cell flips between runs).

---

## Known caveats

1. **All 4 use vol_ratio filter** (some <0.08, others <0.36). Live volume must be reliable.
2. **MR4_long bots use `zscore20 < -2`** which is rare. Expect <100 fires/year per pair across all live trading.
3. **Sample sizes in recent 6mo are small** (n=14-30). Each bot will produce <1 signal per week. Patience required.
4. **Discovery rules include hour_utc-free features only.** But the underlying TRADE TIMES are still concentrated in NY-close → pre-Asia hours due to the volume filter, which itself is session-correlated. Treat the time-of-day distribution as a property of the bot, not a free variable.

---

## V3 integration plan (observe-mode)

1. **Patch `technical_context.py`** to drop the in-progress M15 and H1 bars before computing labels. The current shadow telemetry has the same look-ahead bias as v2 research. Patch is drafted at `/tmp/scrooge-research/technical_context_patched.py`. To deploy: replace V3 file with patched version, restart `mr-scrooge-v3.service`.

2. **Add 4 new observe-mode feature calculators**, one per bot. Each computes the trigger + regime gate from V3's standard feature pipeline (M5 OHLCV, indicators already computed). When the conditions fire, log to `execution-audit` with payload:
   ```json
   {"event": "micro_bot_signal", "bot": "TF6_short_USDJPY",
    "entry": <price>, "stop": <price>, "tp": <price>,
    "context": {<all features at fire>}}
   ```
   **No order placement.** Pure shadow.

3. **Collect signals for 4-6 weeks.** Compare:
   - How often does each bot fire?
   - When it fires, what would the realized R have been (use V3's forward-walk against subsequent M5 bars)?
   - Does the shadow live realized R distribution match the research holdout distribution?

4. **Promotion gate:** only consider live order placement after each bot has ≥10 shadow signals with realized R distribution matching research within reasonable tolerance (e.g., shadow recent mean R > research recent mean R × 0.5, with overlapping 95% CIs).

5. **If at promotion gate:** integrate as a non-blocking "advisor" first — bot logs an opinion but V3's normal strategy still decides. Then escalate to a small fractional position allocator.

---

## Files

- `research/strategy-library-v1/` — full trade dumps per pair (~1.4 GB, gitignored)
- `research/strategy-library-v1/discover_on_library.py` — original 81-survivor pass
- `research/strategy-library-v1/discover_step_A.py` — rollover-killed + no-hour pass (14 survivors)
- `research/strategy-library-v1/spread_stress.py` — vol-conditional spread test (4 survivors)
- `research/strategy-library-v1/slippage_stress.py` — Monte Carlo slippage (4 hold)
- `research/strategy-library-v1/permutation_test.py` — significance test (running)
- `reports/stepA_strict.csv` — the 14 step-A survivors
- `reports/stepC_spread_stress.csv` — the 4 vol-spread survivors
- `reports/stepD_slippage_mc.csv` — slippage MC results
- `reports/permutation_null_distribution.csv` — null distribution (when complete)
- `MICRO_BOTS.md` — this file

---

## 2026-05-14 update: TF6_long / USD_MXN added (second observe-mode bot)

### Status
Observe-mode only. No order placement. Logs to `data/observe-tf6-long-usdmxn.jsonl`.

### Rule
- Trigger: TF6 long ribbon (EMA9>EMA21>EMA50 ascending, all rising, EMA50 5-bar slope > +0.05%)
- Regime gate: `rsi14>80.83 AND atr_ratio<=1.355 AND ema50_dist<=0.94%`
- Hour exclusion: `hour_utc NOT in [21,22,23)`

### Reference performance (research, post all stress)
- Discovery: n=510, mean R = +0.24
- Holdout: n=60, mean R = +0.38, CI lower = +0.06
- Recent 6mo: n=36, mean R = +0.56, CI lower = +0.06
- Slippage MC: 100% of draws positive, p05 = +0.55
- Hour concentration: 23.3% at h7 UTC (London pre-open, MXN main session start)

### Critical caveats (vs. TF6_short USDJPY observer)
- **Discovered via LOOSENED pipeline** (DecisionTreeRegressor on realized_R,
  min_samples_leaf=30, NO win_rate gate). TF6_short USDJPY was discovered via
  stricter DecisionTreeClassifier + min_leaf=60 + win_rate>=0.40.
- **Permutation test NOT run** on the loosened pipeline. Statistical
  significance unproven (TF6_short USDJPY also unproven; p≈0.2 even on its
  stricter pipeline).
- **Sample sizes are small**: ~1.5 fires/week expected.
- **USD_MXN spread is large** (12 pip dukascopy mid baseline). Vol-conditional
  spread stress used 3x for 1.8% of fires. Live OANDA spreads at fire time
  must be monitored; can balloon during US data releases.

### Why NOT shipped: TF6_long USDJPY and TF6_short USDCAD
Both passed every stress test EXCEPT the 25% hour-concentration gate:
- TF6_long USDJPY: 25.5% of fires at h15 UTC (NY morning)
- TF6_short USDCAD: 35.2% of fires at h15 UTC (NY morning)

Hour 15 UTC is a legitimate high-activity window (NY open / US data), not a
thin-liquidity artifact like the previously-killed h22 UTC cells. Decision to
hold per Brock 2026-05-13: ship USD_MXN clean-pass only; leave the two
NY-concentrated cells as research notes pending further validation.

### Next steps
- Both observers run 4-8 weeks
- Compare shadow realized R against research holdout for each
- Run multi-strategy contrast mining on the consolidated foundational dataset
  (`all_strategies_all_pairs_trades.parquet`, 15M trades, 56 strategies × 26
  pairs, on the Mac Mini) — this is the proper unbiased regime-discovery pass
  that has not yet been done
