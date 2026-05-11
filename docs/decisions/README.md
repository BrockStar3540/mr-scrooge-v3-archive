# Architecture Decision Records

This directory holds the institutional memory for major design pivots across the Mr. Scrooge bot family. Each ADR captures a decision that's expensive to reverse, plus the alternatives that were considered and rejected.

## Why this exists

Without a decision log, a fresh session (Claude or human) has no canonical place to learn:
- What we used to believe and changed our mind about, and why
- Which approaches were tried and dismissed (don't re-run discarded experiments)
- The reasoning behind locked constraints in [scrooge-frozen-constraints](https://github.com/BrockStar3540/mr-scrooge-v3/tree/main) (vault) and similar standing rules

State-of-union notes capture *what's true now*. ADRs capture *how we got here and why we didn't go elsewhere*.

## Numbering scheme

Version-bucketed so V1/V2/V3 pivots are easy to identify and backfill:

| Range | Version | Status |
|---|---|---|
| 1001–1999 | V1 (decommissioned 2026-04-15) | Backfill as needed; historical only |
| 2001–2999 | V2 (decommissioned prior to V1) | Backfill as needed; historical only |
| 3001–3999 | V3 (active) | Current — adopt as decisions land |
| 4001+ | reserved for future major version | — |

Within each version, number chronologically by **decision date**, not write date. (Backfilled V1 ADR 1001 may be written in 2026 but covers a 2024 decision.)

## File naming

`<NNNN>-<short-kebab-case-title>.md`

Examples:
- `3001-regime-aware-not-global-score.md`
- `3002-charlie-skip-then-reintroduced.md`
- `1001-v1-single-scorer-architecture.md` (backfilled)

## ADR format

Every ADR must have:

```
# <NNNN>. <Title>

**Status:** Accepted | Superseded by NNNN | Deprecated | Reverted
**Date:** YYYY-MM-DD (decision date, not write date)
**Version scope:** V1 | V2 | V3
**Author:** (optional)

## Context
What we believed before, the evidence that prompted reconsideration.

## Decision
What we chose. Concrete and unambiguous.

## Alternatives considered
What we explicitly rejected, and why each one wasn't picked. This is the load-bearing section — it preserves "don't retry this" knowledge.

## Consequences
What this enables, what this closes off. Both positive and negative.

## Cross-references
Links to vault notes, code commits, related ADRs.
```

## Status semantics

- **Accepted** — the decision is live and current
- **Superseded by NNNN** — newer ADR replaces this one (link forward)
- **Deprecated** — no longer relevant but kept for history
- **Reverted** — was Accepted, then unwound; note the why in Consequences

When a decision is superseded, **do not edit the old ADR's Decision section**. Only update its Status and add a "Superseded by NNNN" line. The historical reasoning stays intact.

## How to write a new ADR

1. Pick the next number in the version range (look at existing files).
2. Use the format template above.
3. Be concrete in Alternatives Considered — vague "we thought about other things" entries aren't useful.
4. Link to evidence (commits, vault notes, audit CSVs) — don't restate them.
5. Submit as a regular commit; don't try to gate ADRs behind review separately.

## When to write an ADR

Write one if the decision:
- Closes off a category of future work (e.g., "no more global-score experiments")
- Establishes a constraint that will be enforced (`scrooge-frozen-constraints` items often need ADR backing)
- Costs more than ~1 hour to reverse if changed
- Is one a fresh session might re-litigate without context

Don't write one for:
- Small bugfixes (commit message is enough)
- Tactical refactors that don't change architecture
- Experiments that haven't been adopted yet

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [3001](3001-regime-aware-not-global-score.md) | Regime-aware not global score | Accepted | 2026-04-15 |

(Add new entries here when you write them.)
