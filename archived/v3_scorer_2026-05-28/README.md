# V3HybridScorer archive — 2026-05-28

Archived per Brock directive: "remove it from the fucking bot, send it
to the damn archive."

## What was here

- `v3_scorer.py` — the V3HybridScorer module (live scorer used Mar–May 2026)
- `v3_scorer_parser.py` — log-line parser used by ml-observer to back-fill
  scorer features into shadow training data
- `_stripped_call_sites/scan_pipeline_scorer_block.py.txt` — verbatim copy
  of the scorer call block that was excised from `core/scan_pipeline.py`,
  for reference if anyone needs to understand what it used to do

## Why archived

Bot architecture moved to ML-routing-only admission via per-pair WIN rules
(2026-05-28 Phase 1-2 ship). V3 scorer's purpose — heuristic re-ranking +
veto — is fully subsumed by:

  - **Admission**: ml_router.get_allowed_or_all() reads per-pair WIN rules
    and returns the set of approved strategies. ML alone decides GO/NO-GO.
  - **Ranking**: strategies emit candidates with their own .score; the
    pipeline picks best-by-score directly. No re-scoring layer.

The 2026-05-27 "demoted to ranker" half-measure was a transition state.
This archive is the final state.

## Legacy droppings left in active source

These are harmless and were left to avoid breaking state-recovery of
currently-open positions:

  - `execution/position_tracker.py:38` — `v3_score: int = 0` field on
    tracked positions; defaults to 0 when not provided.
  - `core/execution_coordinator.py` — passes `v3_score=int(best.score)`
    to the tracker (best.score is now the strategy's emitted score).
  - `dashboard/live_state.py:35` — `v3_score: int = 0` column shown in
    dashboard; reflects the strategy's score now.
  - `services/state_recovery.py:389` — reads `v3_score` from saved
    metadata with default 0.

These should be renamed `strategy_score` in a follow-up commit when no
live positions are held.

## How to revive

If you ever need it back:
1. `git mv archived/v3_scorer_2026-05-28/v3_scorer.py src/scrooge_v3/strategies/v3_scorer.py`
2. `git mv archived/v3_scorer_2026-05-28/v3_scorer_parser.py src/scrooge_v3/advisors/ml_observer/v3_scorer_parser.py`
3. Re-add `V3HybridScorer` to `src/scrooge_v3/strategies/__init__.py` exports
4. Reinstate the scorer construction in `core/bootstrap.py`
5. Restore the scorer call block in `core/scan_pipeline.py` from
   `_stripped_call_sites/scan_pipeline_scorer_block.py.txt`
