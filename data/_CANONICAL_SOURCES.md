# Canonical data sources — Mr. Scrooge V3 (as of 2026-06-08)

## LIVE / canonical (the bot + MLs use THESE)
- `data/playbook_ev_pairaware.csv`  — the gate's EV table. Pair x strategy x align x amp-bucket,
  built from the 8-YEAR per-trade corpus `scored_7yr.parquet` (net_ladder). THE strategy EV source.
- `scored_7yr.parquet` (on the MINI, ~/)  — the 8yr per-trade substrate (pair, strategy, align,
  14 factors, net_ladder/sltp/vol-scaled). The canonical training data for the MLs going forward.
- `Brock's Bot Strategy Book.xlsx` (MBP Desktop / Dropbox) — the human source of truth.
- Bucketizer: `data/per_pair_modules/EUR_USD/lib/factor_buckets.py` (md5 == Mini factor_buckets_v3.py).

## ARCHIVED 2026-06-08 (stale — superseded by the 8yr data; in _archive_2026-06-08_pre-8yr-canonical/)
- pip_meal_lookup.csv, matrix_meal_lookup.csv  — the OLD "optimized matrix" EV (6mo, survivorship
  exp_optimized column). Loaded-but-dead in the new gate (evaluate() never reads them). Retired.
- playbook_ev.csv (pair-blind v1), playbook_ev_pairblind_backup.csv  — superseded by pairaware.
- _deploy_pip_eater_gate.py, _playbook_deploy_backup_* — deploy artifacts.

## FLAGGED for a careful next pass (NOT archived — still wired or needs review)
- `data/lab_training/v0/feature_meta.json` is the ML bucket schema (ml_observer reads it) — KEEP.
  The old corpus DATA in lab_training/ (training_corpus_v1, oos/walkforward) can archive once the
  ML reframe re-points training to scored_7yr.
- Dead `_load()` code in pip_eater_gate.py for the matrix lookups — harmless (loads 0), remove later.
- Old routing_table_v4..v10 — separate subsystem; review before touching.

## NEXT: ML reframe — re-point ml_observer (and any armed advisor) to train on scored_7yr (8yr),
## NOT the old corpus/optimized cells. Then archive lab_training corpus data.
