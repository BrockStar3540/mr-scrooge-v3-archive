# 3002. Branch scorer research arc — direct-only shadow scorer prototype

**Status:** Accepted
**Date:** 2026-04-29
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

Three independent investigations through April 2026 (manual tradebook, EUR_CAD #1918 post-mortem, v2 offline scorer build) converged on the same finding: V3's MFE-anchored scoring is misaligned with realized R. The V3 hybrid scorer ranks candidates well by maximum favorable excursion potential, but realized R correlation hovers near zero. A v2 offline scorer trained against realized R (not MFE) reached ρ=0.20 on holdout.

In parallel, per-strategy ML observer audit showed that `dbb_trend` has clean separability (AUC 0.774, 71.8% WR at `p>=0.5`), but `direct` is near-noise. Treating both with one scorer is throwing away signal on the trend side and adding noise on the direct side.

## Decision

Open a branch-specific scoring research arc. The first deliverable is a **direct-only shadow scorer** prototype trained against realized R on the live-captured candidate stream (not historic replay). It runs alongside V3HybridScorer, never gates. If holdout ρ beats V3 by ≥0.15 with stable temporal-OOS performance, promote to a per-branch scoring layer.

Future branches under the same framework: `dbb_trend` realized-R scorer, `box` family realized-R scorer.

## Alternatives considered

- **Patch V3HybridScorer's MFE anchoring** — rejected. Three independent investigations point at the same misalignment; the architecture (single global scorer over all families) is the issue, not weight tuning.
- **Retrain V3HybridScorer on realized R end-to-end** — rejected. Loses the WR-lift hybrid intuition that genuinely works for `dbb_trend`. Per-branch is cleaner.
- **Skip scoring research, double down on the matrix** — partially adopted later (see ADR 3008, 3017). At decision time the matrix wasn't yet integrated, so this wasn't an available alternative.

## Consequences

- 9 research deliverables shipped in Oanda-Bot-Trainer under the branch-scorer arc.
- DBB stop placement found to be too tight for current microstructure (manual tradebook + EUR_CAD #1918) — separately filed as a stop-planner item.
- Stage B (temporal OOS split) gated on infra not yet built.
- This arc was eventually leapfrogged by the LightGBM v0 primary gate (ADR 3017), which subsumes most of what the per-branch direct-only scorer was meant to do. Research artifacts retained for reference; live work paused.

## Cross-references

- Vault: `wiki/projects/scrooge-v3-branch-scorer-research.md`
- Vault: `wiki/projects/scrooge-v3-ml-per-strategy-edge.md`
- Commits: 9 deliverables in `Oanda-Bot-Trainer` repo (research-only, not in main)
- Superseded in practice by ADR 3017 (LightGBM primary gate)
