# v4_scorer rebuild spec

Status: design only. v3_scorer remains live but **demoted from hard veto
to soft ranker** for routing-approved candidates (see scan_pipeline.py
`demote_old_scorer`, default True since 2026-05-18). REJECT no longer
drops; BLOCKED still drops (physical hard-blocks like spread).

## Why rebuild

v3_scorer was calibrated on the old candidate universe:
- Pre-regime, pre-routing-table, pre-seed-island architecture
- Hard-coded factor weights (`hr`, `age`, `stp`, `vol`, `mom`, `dc`, `z`,
  `bb`, `e50`, `e20`, `otr`, `adr`, `dur`, `wal`, `bdy`, `bbs`, `rsi`,
  `p_hr_norm`, `p_age_rsi`, `n_z_norm`, etc.)
- Session-aware floors but family-blind
- Not informed by:
  - which (regime, pair, session, direction) leaf the candidate is in
  - whether a routing-table cell exists at that leaf
  - the cell's tier / Wilson LB / n_unique
  - shave-rule distance / margin
  - live shadow pass/veto evidence

Result: scorer was rejecting candidates the routing/island layer
already validated. Surgical fix shipped (demotion); structural fix
needed (rebuild).

## Doctrine the new scorer must follow

1. **Routing/island table decides eligibility.** A candidate that
   reaches the scorer has already cleared sub_regime + entry_filter +
   shave_rule. The scorer must respect that approval.
2. **Gates enforce hard safety / rule match.** Daily circuit,
   cooldown, debounce, spread, position cap. Scorer doesn't duplicate.
3. **Scorer ranks eligible candidates or adjusts size/confidence.**
   It picks the best when multiple candidates compete at the same
   tick, and feeds a confidence into position sizing.
4. **Scorer does not veto routing-approved candidates** on its own
   judgment. BLOCKED for physical issues only.

## Inputs (features)

### Regime / slice features
- `technical_regime_53`         (53-class, one-hot or embedding)
- `parent_regime`               (C01/C02/B01..B08 etc.)
- `sub_regime`                  (C01_0..7 / C02_0..7 etc.)
- `pair`                        (28-class, one-hot or embedding)
- `direction`                   (long/short binary)
- `session_bucket`              (7-class: asia/asia_late/london_open/
                                  ny_open/ny_mid/ny_close/off_hours)
- `hour_utc`                    (0-23 cyclic)
- `day_of_week`                 (0-6 cyclic)

### Candidate factor features
- `ATR_ratio`                   (M5/D20 ratio)
- `ADX14`
- `BB_compress`                 (BB-width / D20 BB-width)
- `BB_width`
- `RSI14`
- `close_pos`                   (close in M5 20-bar range)
- `volume_ratio`
- `bb_position`                 (close in Bollinger Band range)
- `z_score`                     (close vs SMA20)
- `EMA_slope`

### Routing / cell features
- `cell_tier`                   (Probationary / Seed / Standard /
                                  Seed-Pro / Pro / Elite — ordinal)
- `cell_n_unique`               (sample size in unique trades)
- `cell_wr`                     (in-sample WR)
- `cell_wilson_lb`              (evidence-adjusted WR)
- `cell_source_bank`            (probe / textbook / synthesized)
- `cell_oos_status`             (untested / passed / failed)
- `cell_promotion_status`       (candidate / observe / live / demoted)
- `match_kind`                  (exact_strategy / exact_family /
                                  family_loose_override)
- `shave_rule_margin`           (per-clause distance to threshold,
                                  averaged or worst-case)
- `boundary_fragile_flag`       (any clause within 2% of threshold)

### Live evidence features
- `live_shadow_pass_count`      (per-cell, rolling 7 days)
- `live_shadow_veto_count`
- `live_fire_count`             (real LIMIT placements)
- `live_fill_count`
- `live_realized_pnl_R`         (cumulative R since deploy)
- `cell_age_days`               (how long since cell first appeared in
                                  any routing table)

### Microstructure features
- `spread_pips`                 (current spread in pips)
- `box_age_h`                   (zone box age)
- `range_half`                  (half the daily range)
- `total_overhead`

## Targets

Train three separate heads:

### Head A: `should_trade` (binary classification)
- Target: did the trade hit TP2 (full target) without first hitting
  stop?
- Loss: binary cross-entropy
- Threshold: deploy at p ≥ calibrated bar (e.g. 0.55)

### Head B: `expected_r` (regression)
- Target: realized R-multiple of the trade (winners + losers)
- Loss: Huber loss (robust to outliers)
- Used by: position sizing (size proportional to expected_r * confidence)

### Head C: `rank_among_tradeable` (pairwise)
- Target: among multiple candidates at the same tick, which one is
  best?
- Loss: pairwise ranking (margin loss)
- Used by: "best candidate" selection in scan_pipeline

A single-model multi-task with shared base + 3 heads is the cleanest
implementation. XGBoost or a small MLP. Avoid deep architectures —
the dataset is small relative to feature count.

## Training data sources

### Source 1: textbook OOS survivors
- 10 cells from oos-2026-05-18/v10_honest_candidates.csv
- Real corpus train < 2025-01-01 / test ≥ 2025-01-01 evidence
- Use for `should_trade` ground truth

### Source 2: probe cells with live shadow evidence
- Cells with shadow `shave_rule_satisfied` count ≥ 2 in
  data/seed-telemetry.jsonl
- Use shadow_pass count as a proxy for "rule fires correctly on
  live data" (necessary condition for `should_trade=True`)

### Source 3: live fills (the actual prize)
- data/execution-audit.jsonl + OANDA closed trades
- Realized R per trade, attributed to specific routing cell via the
  order_id → telemetry approval row → cell_label join
- Use for both Head A (target = TP hit?) and Head B (target = R)
- Will be sparse early; this is what makes the rebuild worth doing
  incrementally as live data accumulates

### Source 4: corpus-replay augmentation
- The ml_training_corpus.parquet (15.27M rows) for textbook cells with
  pre-2025 data
- Apply the cell's shave_rule, take matched trades, compute realized R
- Use as augmented training data; flag with `source=corpus_replay` so
  we can weight differently vs live data

## Data pipeline

```
research/ohlcv-strategy-library-v0/v4_scorer/
  build_v4_training_set.py          assembles features + targets from
                                     sources 1-4
  v4_training_set_YYYY-MM-DD.parquet  one row per trade with full
                                       feature/target columns
  train_v4_scorer.py                  fit XGBoost / MLP, calibrate
                                       per-session
  v4_scorer_model.bin                 the trained artifact
  evaluate_v4_scorer.py               OOS evaluation + calibration plots
  v4_scorer_calibration_report.md     AUC, Brier, calibration curve
                                       per session/family
```

## Live integration plan

Phase 1 (current state):
- v3_scorer in DEMOTED mode (REJECT no longer drops)
- Routing/gates are the decision authority
- Best-by-score uses v3 score for ranking only

Phase 2 (when v4 trained):
- v4_scorer registered alongside v3
- Both run; v4's `should_trade` probability is recorded but doesn't gate
- v4's `expected_r` feeds position sizing (via metadata)
- v3 score still used as legacy ranker

Phase 3 (when v4 is calibrated):
- v4 replaces v3 in best-by-score selection
- v3 deprecated / removed
- v4's BLOCKED (if we keep that concept) replaces v3's

## Evaluation criteria for promoting v4 → live

1. AUC on Head A (should_trade) ≥ 0.65 on holdout
2. Calibration: predicted p vs actual win-rate within ±3% across
   deciles
3. Expected_R has positive correlation with realized R on holdout
   (Pearson r ≥ 0.20)
4. Per-session, per-family stratified — no session/family with AUC <
   0.55 (would mean v4 is worse than random in that slice)

## Timeline estimate

| step | effort |
|---|---|
| Build training set (sources 1-4) | 1-2 days |
| Train + tune model | 2-3 days |
| Evaluate + calibrate per session/family | 1-2 days |
| Live shadow integration (Phase 2) | 1 day |
| Promotion to live ranker (Phase 3) | depends on AUC numbers |

Total to Phase 2: ~1 week of focused research time.

## What does NOT change

- Gates remain as-is (sub_regime, entry_filter, etc.) with their
  overrides
- Routing tables remain primary decision authority
- Position sizing safety net (max_open_positions, margin_utilization,
  daily_loss_pct) remains
- Daily circuit and cooldown remain

## Risk

The v4 rebuild relies on the ASSUMPTION that live fills + corpus replay
data contains enough signal to learn a generalizable ranking. If the
data is too thin (which is likely true for V3 probes especially), the
v4 scorer will overfit. Mitigation: heavy regularization, per-slice
stratified training, and Phase 2's shadow-only deployment lets us
compare v4 predictions to actual outcomes BEFORE giving v4 veto/sizing
authority.

## Decision to make

Two concurrent paths:

1. **Phase 1 only, for now** — leave v3 demoted, let routing/gates be
   the brain, don't rebuild yet. Wait for ~1 month of live data, then
   re-evaluate whether v4 is worth building.

2. **Phase 1 + start v4 build** — kick off the training-set assembly
   immediately, accept that the first v4 model will be weak (sparse
   live data), iterate as data accumulates.

Brock's earlier framing favored option 2 (don't be passive, build the
new infrastructure). But the model quality will be data-bounded for
weeks. Defensible either way.
