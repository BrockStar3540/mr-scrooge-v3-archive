# v4 scorer — v0 build status + retrain backlog

## What shipped tonight (2026-05-18)

1. `research/ohlcv-strategy-library-v0/v4_scorer/build_v4_training_set.py`
   — assembles per-trade rows from `ml_training_corpus.parquet` joined
   to `routing_table_v9_observe.parquet` cells at tier >= Seed. Applies
   probe 2× dedup. Splits by entry_ts < / >= 2025-01-01.

2. `research/ohlcv-strategy-library-v0/v4_scorer/v4_training_set_2026-05-18.parquet`
   — first training set. **260,853 rows / 439 cells**.

3. `research/ohlcv-strategy-library-v0/v4_scorer/train_v4_scorer.py`
   — XGBoost trainer. Head A (binary `is_win`), Head B (regression on
   `realized_R`). Saves models + features manifest + metrics.

4. `research/ohlcv-strategy-library-v0/v4_scorer/v4_scorer_model_A.json`
   — first v4 binary classifier.

5. `research/ohlcv-strategy-library-v0/v4_scorer/v4_scorer_model_B.json`
   — first v4 regressor.

6. `src/scrooge_v3/strategies/v4_scorer.py` — runtime class
   `V4HybridScorer`. Loads the trained model, extracts features from
   `(ctx, candidate)`, predicts `p_win` + `expected_r` + `rank_score`.
   Currently NOT wired into `scan_pipeline`. Mode default = `shadow`.

## v0 result: BELOW promotion bar

| head | metric | result | bar | status |
|---|---|---:|---:|---|
| A `should_trade` | AUC test | 0.497 | ≥ 0.60 | **BELOW** |
| A `should_trade` | Brier test | 0.255 | low is good | high (random-ish) |
| B `expected_r` | Pearson r test | 0.016 | ≥ 0.10 | **BELOW** |
| B `expected_r` | RMSE test | 1.252 | low is good | acceptable noise floor |

The calibration table is flat — actual WR ≈ 0.377 across all
prediction deciles. The model is essentially random on holdout.

## Why v0 failed (honest diagnosis)

1. **Train/test contamination**. Train (pre-2025) is textbook-only
   because V3 probe replay data is entirely 2025+. Test (2025+) is
   half probes, half textbook. The model learns textbook patterns
   on train, then sees a different distribution on test.

2. **Leaky features**. `cell_wr` and `cell_wilson_lb` are computed
   from the FULL corpus (including test rows). The model can see
   the answer for in-sample rows but those features are
   computed-from-target for test rows too. Should be omitted or
   recomputed train-only.

3. **Per-cell stratification missing**. The 439 cells have
   wildly different WRs (Seed cells at 0.40, Pro at 0.65). The
   model needs to learn within-cell features, not cell-identity.

## Retrain backlog (Phase 1.1)

Three concrete fixes to try in order:

1. **Drop leaky cell features.** Remove `cell_wr`, `cell_wilson_lb`,
   `cell_n_unique` from features. Keep `cell_tier_rank` and
   `cell_source_bank` only. These leak less because they're
   ordinal/categorical assignments rather than direct win-rates.

2. **Stratified split.** Within each cell, hold out the last 20% of
   trades by entry_ts. Avoids the "probes only in test" problem.
   Each cell contributes train + test rows.

3. **Within-cell normalization for factors.** Compute z-score of
   each numeric factor *within* its cell-bucket before training.
   The model learns "this trade's ATR is unusually high for THIS
   cell," not "this trade's ATR is high overall."

If retraining with all 3 still gives AUC < 0.60, the next move is:
- Add more features (live shadow pass count, time-since-cell-creation)
- Switch to LightGBM with categorical handling
- Or accept that 439 cells with avg ~600 rows each is too thin and
  wait for live fills to add real OOS data

## Live integration (Phase 2 -- NOT YET, gated on retrain success)

When a v4 model passes AUC >= 0.60:
1. Wire `V4HybridScorer` instance into `ScanPipeline.__init__`
2. After v3 scorer block in `scan_pipeline.py`, run v4 in shadow:
   ```python
   v4_result = self.v4_scorer.score(ctx, candidate)
   log.info("[V4_SCORER] p_win=%.3f expected_r=%.3f rank=%.3f symbol=%s strategy=%s",
            v4_result.p_win, v4_result.expected_r, v4_result.rank_score,
            symbol, candidate.strategy)
   candidate.metadata["v4_p_win"] = v4_result.p_win
   candidate.metadata["v4_expected_r"] = v4_result.expected_r
   ```
3. v4 still does NOT affect best-by-score or sizing. Just logs.

## Live-only-promotion (Phase 3) and retirement (Phase 4)

Per v4_scorer_rebuild_spec.md:
- Phase 3: after 30 days of v4-vs-v3 shadow + AUC >= 0.65 on live OOS,
  flip best-by-score to key on v4's rank_score.
- Phase 4: after 60 days stable, delete v3 codepath entirely.

## Tomorrow's next step

Decision: retrain immediately with the 3 fixes (drop leaky features +
stratified split + within-cell normalization), OR wait for some live
fills to add real recent data first. v0 confirms the pipeline works
end-to-end; the model just needs cleaner data.

My recommendation: **retrain in the morning** with the 3 fixes. The
stratified split alone should lift AUC noticeably (it eliminates the
contamination). If that crosses 0.60, wire Phase 2 shadow that
afternoon.
