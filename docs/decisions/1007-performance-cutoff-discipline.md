# 1007. Performance cutoff discipline (Mar 4 line)

**Status:** Accepted; pattern survives in V3 as post-attribution-fix cohort
**Date:** 2026-03-05 (cutoff established during initial production audit)
**Version scope:** V1 (pattern preserved into V3)
**Backfilled:** 2026-05-11

## Context

After the first audit pass on live deployment (2026-03-05), it became clear that pre-cutoff data was contaminated:
- Multiple bot instances running concurrently
- Duplicate log lines from racing engines
- Various execution bugs being patched

Performance numbers from this period mixed real signal with pre-fix noise. Using them to judge the strategy was misleading.

## Decision

**Establish a single cutoff timestamp**: `2026-03-04 23:00:00 UTC` (March 4, 2026 6:00 PM New York).

- Data **before** the cutoff is declared pre-fix noise and **excluded** from strategy scoring.
- Data **after** the cutoff is treated as auditable production performance.
- Documented in `AGENTS.md` and `AUDIT.md`: *"Do not claim profitability using pre-cutover data."*

The cutoff is **not negotiable**. It survives bot versions, code refactors, repo migrations.

## Alternatives considered

- **Sliding window (last N days)** — rejected. Loses the "before/after fix" distinction; mixes pre- and post-fix data.
- **No cutoff (use everything)** — rejected. Contaminates performance assessment with bugs you've already fixed.
- **Cutoff per-bug** — rejected. Too noisy; some bugs are subtle and a single line is cleaner discipline.

## Consequences

**Enabled:**
- All performance claims are guarded with "post-cutover." Forces explicit framing.
- New data can be benchmarked against the post-cutover-only baseline without re-deriving every time.

**Closed:**
- "It worked great before we changed it" arguments where "before" is the bug-laden era.

**Costs:**
- Some pre-cutover data was legitimate. Throwing it all out is conservative. Acceptable.

## Survival into V3

V3's live broker reverse-engineering audit (2026-05-10) uses the same pattern with a different date: **2026-05-04T06:38:45Z** (Patch A deployment) is the V3 attribution cutoff. Trades before are `pre_attribution_fix` cohort; after are `post_attribution_fix`. Confidence flags downgrade pre-attribution rows.

The discipline is the same: when telemetry is fundamentally improved, draw the line.

## Cross-references

- `AGENTS.md` and `AUDIT.md` in `BrockStar3540/mr-scrooge`
- `[[scrooge-evolution-timeline]]` V1 Genesis section
- V3 attribution cutoff: `[[v2-post-audit-state-2026-05-10]]`, ADR `3001-regime-aware-not-global-score.md`
