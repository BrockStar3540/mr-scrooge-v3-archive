# Lab Reproduction Guide

Step-by-step instructions to reproduce the Mr. Scrooge V4 lab
pipeline from scratch. If you can follow these end-to-end, you can
rebuild the 838k-trade corpus, mine your own matrix, train your own
LightGBM, and assemble your own routing table.

Companion to [`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md)
(the design rationale — *why* the pipeline is shaped this way).
This doc is *how* to actually run it.

**Audience:** a researcher with Python + pandas + LightGBM fluency.
Expected time: ~4-8 hours wall-clock for a first full rebuild on
a 6-month window, depending on hardware.

---

## Prerequisites

### Hardware

| Component | Minimum | Recommended |
|---|---|---|
| RAM | 8 GB | 16 GB (lab sweep uses ~2 GB per parallel worker) |
| Disk | 20 GB free (corpus + caches) | 50 GB free |
| CPU | 4 cores | 8+ cores (parallelizes the lab sweep) |

The reference build was on an Apple M4 Mac Mini, 10 cores / 16 GB.
EC2 `t3.medium` works but slower.

### Software

```bash
python3.11+
pandas >= 2.0
numpy >= 1.24
lightgbm >= 4.0
scikit-learn (KMeans)
backtesting.py >= 0.3
requests (OANDA REST)
pyarrow (parquet I/O)
```

Install in a clean venv:

```bash
python3 -m venv ~/scrooge_env
source ~/scrooge_env/bin/activate
pip install -r requirements.txt
```

### OANDA account

Practice account is sufficient for the data pull (read-only
transactions and candles). [Create one here](https://www.oanda.com/);
generate a Personal Access Token from the account settings.

```bash
export OANDA_ACCOUNT_ID=101-001-XXXXXXXX-001
export OANDA_API_TOKEN=<your-token>
export OANDA_ENV=practice  # or 'live'
```

---

## Step 1 — Pull candle data

Script: `research/sample_corpus/pull_oanda_candles.py`

Pulls M5, H1, D1 candles for the 27 pair universe over a configurable
date window. Caches to `research/replay_lab/cache/{PAIR}_{TF}_{FROM}_{TO}.parquet`.

```bash
# Full 6-month corpus (matches the reference build)
python research/sample_corpus/pull_oanda_candles.py \
    --pairs all \
    --timeframes M5 H1 D1 \
    --from 2025-11-25 \
    --to 2026-05-25 \
    --cache research/replay_lab/cache/

# Or: 1-month smoke test (faster iteration)
python research/sample_corpus/pull_oanda_candles.py \
    --pairs EUR_USD GBP_USD USD_JPY \
    --timeframes M5 \
    --from 2026-04-25 \
    --to 2026-05-25
```

**Expected output:**
- 27 pairs × 3 timeframes = 81 parquet files
- M5 file for one pair / 6 months ≈ 50 MB (~52k bars)
- Total cache size for full pull: ~4 GB

**Verification:**
```python
import pandas as pd
df = pd.read_parquet("research/replay_lab/cache/EUR_USD_M5_20251125_20260525.parquet")
assert len(df) > 40_000, "expected ~52k M5 bars over 6 months"
assert (df['time'].diff().dt.total_seconds().median() == 300), "expected 5-minute spacing"
print(f"OK: {len(df)} M5 bars, {df['time'].min()} → {df['time'].max()}")
```

---

## Step 2 — Compute 14-bucket factor signatures

The corpus's per-bar 14-bucket signature is the foundation of the
matrix mining + routing table.

Module: `src/scrooge/features/factor_buckets.py` (the same module the
live bot uses — same bucketization logic offline as live).

```bash
python research/matrix_mining/bucketize_corpus.py \
    --cache research/replay_lab/cache/ \
    --out research/replay_lab/bucketized/
```

This produces per-pair parquet files with each M5 bar augmented with
14-bucket labels:

```
research/replay_lab/bucketized/EUR_USD.parquet
```

Columns:
```
time, o, h, l, c, v,
BB, BBP, A5, A1, RSI, E20, E50, ZS, SPR, ADR, H20, H60, T1, T4
```

**Expected output:** 27 parquet files, ~50-60 MB each.

**Verification:**
```python
df = pd.read_parquet("research/replay_lab/bucketized/EUR_USD.parquet")
# Every bar should have a bucket label for each of 14 factors
for col in ["BB", "BBP", "A5", "A1", "RSI", "E20", "E50",
            "ZS", "SPR", "ADR", "H20", "H60", "T1", "T4"]:
    assert df[col].notna().all(), f"{col} has nulls"
    print(f"  {col}: {df[col].nunique()} distinct buckets, "
          f"top={df[col].value_counts().head(3).to_dict()}")
```

---

## Step 3 — Run lab harness (smoke test first)

Always smoke test ONE strategy on ONE pair before launching the
full sweep. The Phase 3 development arc had 3 stacked bugs
(`_SingleProbeStrategy` dispatch, entry-mode LIMIT-at-market,
`routing_mode="no_router"` not honored) that the smoke test
discovered immediately and the full sweep would have masked for hours.

Smoke test:

```bash
python research/harness/run_single_backtest.py \
    --strategy BR2_vcb_short \
    --pair EUR_USD \
    --direction native \
    --from 2025-11-25 \
    --to 2026-05-25 \
    --entry-mode market \
    --routing-mode no_router \
    --out /tmp/smoke_BR2_EUR_USD.csv
```

**Expected smoke output:** ~900-1000 trades, 60-65% WR. If you see
zero trades, **STOP** and check:
- `entry_mode=market` (not "signal" — LIMITs-at-market get silently rejected)
- `routing_mode=no_router` AND `routing_table=None` (both — otherwise auto-loads live parquet)
- The `_SingleProbeStrategy` dispatch is in `instantiate_live_strategy()`

Once smoke passes, launch the full sweep:

```bash
python research/harness/run_phase3_sweep_parallel.py \
    --workers 4 \
    --variants all \
    --pairs all \
    --directions native reversed \
    --from 2025-11-25 \
    --to 2026-05-25 \
    --out research/replay_lab/results/sweep_$(date +%Y%m%dT%H%M%SZ)/
```

**Expected sweep output:**
- 34 variants × 27 pairs × 2 directions = 1,836 backtests
- ~3h per variant × 34 variants / 4 workers ≈ 25h wall-clock
- Output dir contains `per_variant_{VARIANT}.csv` (aggregated) +
  `trades_{PAIR}_{VARIANT}_{DIRECTION}.csv` per cell (full trade-by-trade)
- Total output size: ~3-4 GB

**Memory note:** Each worker holds the corpus + strategy state in
memory (~2 GB per worker). With 16 GB RAM, 4 workers is the limit
before swap kicks in.

---

## Step 4 — Mine the factor matrix

For each (pair × strategy × direction × factor) cell, compute the
lift in expected R when filtering trades to that factor's bucket value.

```bash
python research/matrix_mining/build_factor_lift_table.py \
    --sweep research/replay_lab/results/sweep_LATEST/ \
    --out data/matrix/factor_lift_table.csv

python research/matrix_mining/build_optimized_matrix.py \
    --sweep research/replay_lab/results/sweep_LATEST/ \
    --factor-lift data/matrix/factor_lift_table.csv \
    --out data/matrix/optimized_matrix.csv \
    --out-by-session data/matrix/optimized_matrix_by_session.csv
```

**Expected output:**
- `factor_lift_table.csv` ≈ 1.5 MB, ~10k rows
- `optimized_matrix.csv` ≈ 160 KB, ~600-700 cells
- `optimized_matrix_by_session.csv` ≈ 900 KB, ~3-4k cells (×5 sessions)

**Verification:**
```python
lift = pd.read_csv("data/matrix/factor_lift_table.csv")
# Headline factor that should be present: cand_vs_htf20_mismatch
# with positive lift across many cells
htf = lift[lift["factor_name"] == "cand_vs_htf20_mismatch"]
assert len(htf) > 0, "HTF king-factor missing"
assert (htf["lift_exp"] > 0).mean() > 0.7, "HTF should dominate >70% of cells"
print(f"OK: HTF king-factor present in {len(htf)} cells, "
      f"{(htf['lift_exp']>0).mean():.0%} positive-lift")
```

---

## Step 5 — Build per-pair modules

For each of the 27 pairs, mine a "knowledge library" folder
containing KMeans-clustered regimes + WIN/LOSE rule library.

```bash
python research/matrix_mining/build_per_pair_modules.py \
    --bucketized research/replay_lab/bucketized/ \
    --sweep research/replay_lab/results/sweep_LATEST/ \
    --n-regimes 20 \
    --out data/per_pair_modules/
```

Produces 27 pair-folders:

```
data/per_pair_modules/EUR_USD/
├── lib/factor_buckets.py     # bundled bucketization code (same as src/)
├── regime_centroids.csv      # 20 KMeans centroids, 7-feature mode buckets
├── trade_serials.csv         # historical trades w/ signatures
└── manuals/master_rules.csv  # ~1000 WIN/LOSE rules per pair
```

**Expected output:**
- 27 pair-folders, ~5-15 MB each (varies by pair's trade density)
- 540 (pair × regime) cells total
- Median ~50 rules per cell

**Verification:**
```python
from pathlib import Path
n_empty = 0
for pdir in Path("data/per_pair_modules").iterdir():
    if not pdir.is_dir(): continue
    rules = pdir / "manuals" / "master_rules.csv"
    if rules.stat().st_size < 100:
        n_empty += 1
        print(f"  EMPTY: {pdir.name}")
assert n_empty <= 1, "more than 1 empty pair module — pipeline issue"
# USD_MXN may be empty due to data-thin corpus (known issue, Task #51)
```

---

## Step 6 — Train LightGBM v0

Train a binary classifier on the per-trade outcomes. Produces the
primary admission scorer used at the live admission gate (`p_win ≥ 0.75`).

```bash
python research/lightgbm_training/train_lgbm_v0.py \
    --bucketized research/replay_lab/bucketized/ \
    --sweep research/replay_lab/results/sweep_LATEST/ \
    --train-window 2025-11-25 2026-04-15 \
    --holdout-window 2026-04-15 2026-05-25 \
    --out data/lgbm_v0/

# Outputs:
#   data/lgbm_v0/model.txt           — the trained LightGBM model
#   data/lgbm_v0/meta.json           — training metadata + holdout metrics
#   data/lgbm_v0/feature_importance.csv
#   data/lgbm_v0/decile_analysis.csv — per-decile WR distribution
```

**Expected output:**
- Holdout AUC: 0.58-0.62 range (target ≥0.60)
- WR @ top decile: 75-85%
- WR @ top 3% (threshold 0.75): ~75% sim WR
- Model file: ~1.3 MB

**Verification:**
```python
import json
meta = json.load(open("data/lgbm_v0/meta.json"))
assert meta["holdout_auc"] >= 0.58, "holdout AUC too low — check time split"
deciles = pd.read_csv("data/lgbm_v0/decile_analysis.csv")
top_decile_wr = deciles.iloc[-1]["wr"]
bot_decile_wr = deciles.iloc[0]["wr"]
print(f"AUC {meta['holdout_auc']:.3f}, top decile WR {top_decile_wr:.1%}, "
      f"bottom decile WR {bot_decile_wr:.1%}")
assert top_decile_wr > 0.70 and bot_decile_wr < 0.45, \
    "decile spread too narrow — model not discriminating"
```

---

## Step 7 — Assemble the routing table

Promote matrix cells into the live routing table parquet.

```bash
python research/matrix_mining/assemble_routing_table.py \
    --optimized-matrix data/matrix/optimized_matrix_by_session.csv \
    --factor-lift data/matrix/factor_lift_table.csv \
    --per-pair-modules data/per_pair_modules/ \
    --min-n 100 \
    --min-wr 0.55 \
    --out data/routing_table.parquet
```

**Expected output:**
- 1500-2000 rows / 200-300 leaves
- File size: ~30-50 KB

**Verification:**
```python
rt = pd.read_parquet("data/routing_table.parquet")
assert len(rt) > 1000, "too few cells — promotion threshold too tight"
assert len(rt) < 5000, "too many cells — promotion threshold too loose"
print(f"routing table: {len(rt)} rows, {rt['leaf_id'].nunique()} leaves, "
      f"{rt['pair'].nunique()} pairs, {rt['strategy'].nunique()} strategies")
```

---

## Step 8 — Validate against held-out slice

Final sanity check: run the live admission stack (routing table +
LightGBM) against the held-out window and verify the slice matches
expected performance.

```bash
python research/lightgbm_training/validate_holdout.py \
    --bucketized research/replay_lab/bucketized/ \
    --routing-table data/routing_table.parquet \
    --lgbm-model data/lgbm_v0/model.txt \
    --threshold 0.75 \
    --holdout-window 2026-04-15 2026-05-25 \
    --out /tmp/holdout_validation.csv
```

**Expected output:**
- Admission rate: ~3-5% of candidates pass the 0.75 gate
- Held-out WR on admitted slice: 70-78%
- If WR < 65% on holdout: **the routing table is overfit** —
  re-mine with stricter promotion thresholds

---

## Troubleshooting

### Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| Smoke test returns 0 trades | `entry_mode="signal"` rejected silently by backtesting.py | Use `entry_mode="market"` |
| Smoke test returns 0 trades | `routing_mode="no_router"` ignored because `load_routing_table(None)` auto-loads | Pass `routing_table=None` explicitly too |
| `_SingleProbeStrategy` not found | Dispatcher not registered | Verify `instantiate_live_strategy()` has the dispatch case |
| Sweep OOM | Too many workers vs RAM | Reduce `--workers` to `RAM_GB / 3` |
| Matrix has empty `regime` column | Optimization pass collapses regimes | Expected — use per-pair modules for regime-level analysis |
| USD_MXN empty `master_rules.csv` | Pair data-thin in corpus | Known issue (Task #51). Either re-mine or exclude pair |
| LightGBM AUC < 0.55 | Time split bug (random split instead of temporal) | Verify train/holdout are time-ordered, no leakage |
| Holdout WR much worse than train | Overfitting | Tighten promotion thresholds in Step 7 |

### What success looks like end-to-end

After running all 8 steps on a fresh corpus, you should have:

- ~4 GB of cached OANDA candles
- 27 bucketized per-pair parquet files
- 1 sweep results dir with ~3 GB of trade CSVs
- 3 matrix CSVs (factor_lift + optimized_matrix + optimized_matrix_by_session)
- 27 per-pair module folders with regime centroids + master rules
- 1 LightGBM model file (model.txt + meta.json)
- 1 routing table parquet

The bot can boot off these artifacts. From `bootstrap.py`'s perspective,
your fresh-built lab is indistinguishable from the reference build.

---

## Walk-forward / temporal OOS extension

The reference build is in-sample (train + validate on the same
6mo window with an 80/20 internal split). For honest forward
validation, extend with:

```bash
# Train on 2024 H2 + 2025 H1
python research/lightgbm_training/train_lgbm_v0.py \
    --train-window 2024-07-01 2025-06-30 \
    --holdout-window 2025-07-01 2025-12-31 \
    --out data/lgbm_walkforward_v0/

# Then validate that walkforward model on the V4 reference window
python research/lightgbm_training/validate_holdout.py \
    --routing-table data/routing_table.parquet \
    --lgbm-model data/lgbm_walkforward_v0/model.txt \
    --threshold 0.75 \
    --holdout-window 2026-01-01 2026-05-25
```

If the walk-forward model degrades sharply on the V4 reference window,
the V4 routing table is regime-overfit — same caveat as documented in
[`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md#known-limitations)
limitation #1.

---

## Cross-references

- [`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md) — design rationale
- [`ARCHITECTURE_DIAGRAM.md`](ARCHITECTURE_DIAGRAM.md) — visual pipeline (Data flow diagram covers Steps 1-7)
- [`STRATEGY_ENCYCLOPEDIA.md`](STRATEGY_ENCYCLOPEDIA.md) — per-strategy probe code references
- `research/` directory in the repo — all the scripts referenced above

---

## What this guide does NOT cover

- **Live bot deployment** — see `ops/deploy/` for systemd unit setup,
  config templates, Telegram alerter installation
- **Real-time data quality** — assumes OANDA candle data is clean;
  spread spikes, weekend gaps, and broker artifacts are handled by
  `src/scrooge/execution/stop_planner.py` in the live path, not in
  the lab harness
- **Multi-broker support** — V4 is OANDA-only (deliberate scope choice;
  see ADRs for the reasoning)
- **Strategy authoring** — see `STRATEGY_ENCYCLOPEDIA.md` for the
  template + existing entries to copy from
