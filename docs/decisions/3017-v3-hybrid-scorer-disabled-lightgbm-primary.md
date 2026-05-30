# 3017. V3HybridScorer DISABLED + LightGBM v0 promoted to PRIMARY GATE @ 0.75

**Status:** Accepted
**Date:** 2026-05-28
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

By 2026-05-28 the V3HybridScorer was producing a score that was no longer the load-bearing admission signal. The routing table (ADR 3008) was making the per-cell decision, the matrix factor_lift was the per-factor signal, and LightGBM v0 had been trained on the full 838k corpus with holdout AUC 0.6025.

Keeping the V3 scorer in the pipeline created two problems:
1. It was being treated as ground truth by downstream consumers (DBB candidate audit, dashboards) when it was no longer the gate.
2. Its session-aware threshold logic was duplicating signal the routing table already encoded.

LightGBM at threshold 0.75 admits the top ~3% of lab cohort, which empirically corresponds to ~75% sim WR.

## Decision

- **Disable V3HybridScorer:** `scan_pipeline.scorer = None`. The class stays in the codebase for backward compat in tests, but no live path invokes it.
- **Promote LightGBM v0 to PRIMARY GATE:** threshold `0.75`. Candidates with `p_win < 0.75` are rejected at the admission stage.
- **Demote ml_router to shadow:** ml_router still scores every candidate but its decision logs only to `data/ml_router_shadow.jsonl` — does not gate.

Boot log emits the explicit demotion line:
```
[BOOT] LightGBM PRIMARY GATE enabled (threshold=0.75) — ml_router demoted to shadow
```

## Alternatives considered

- **Keep V3 scorer as a feature into LightGBM** — rejected. LightGBM already trains on the 14-bucket signature directly; the V3 score is a noisy summary.
- **LightGBM as gate but keep ml_router as primary** — rejected. Two primary gates is no primary gate.
- **Threshold 0.55 (Track A status quo from ADR 3005)** — rejected. With matrix routing now upstream, the 0.55 threshold was admitting candidates the matrix would route well but LightGBM wasn't confident on. 0.75 keeps only the high-confidence intersection.
- **Threshold 0.80 or higher** — rejected. Sim WR gain past 0.75 was diminishing; admission rate would have dropped below sustainability for the trade-count target.

## Consequences

- Admission rate drops sharply; admitted slice is materially higher quality.
- ml_router shadow log becomes the cross-validator: when LightGBM admits and ml_router would have rejected, that pair is the interesting audit case.
- V3HybridScorer code retained but inert — flagged for removal at V4 cutover.
- Supersedes ADR 3005 (Track A threshold held at 0.55).

## Cross-references

- Boot log: `[BOOT] V3HybridScorer DISABLED` + `[BOOT] LightGBM PRIMARY GATE enabled (threshold=0.75)`
- Model: `data/lgbm_v0_model.txt` + `data/lgbm_v0_meta.json`
- Vault: `wiki/projects/scrooge-v3-strategy-promotion-2026-05-27.md` (next-day context)
