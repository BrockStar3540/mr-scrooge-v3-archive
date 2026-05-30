# Architecture Decision Records

This directory holds the institutional memory for major design pivots across the Mr. Scrooge bot family (V1, V2, V3). Other BrockStar projects (Claim Donkey, NRD, etc.) maintain their own decision logs separately if needed. Each ADR captures a decision that's expensive to reverse, plus the alternatives that were considered and rejected.

## Why this exists

Without a decision log, a fresh session (Claude or human) has no canonical place to learn:
- What we used to believe and changed our mind about, and why
- Which approaches were tried and dismissed (don't re-run discarded experiments)
- The reasoning behind locked constraints in [scrooge-frozen-constraints](https://github.com/BrockStar3540/mr-scrooge-v3/tree/main) (vault) and similar standing rules

State-of-union notes capture *what's true now*. ADRs capture *how we got here and why we didn't go elsewhere*.

## Numbering scheme

Version-bucketed so V1/V2/V3 pivots are easy to identify and backfill:

| Range | Scrooge version | Status |
|---|---|---|
| 1001-1999 | Scrooge V1 (decommissioned 2026-04-15) | Backfill as needed; historical only |
| 2001-2999 | Scrooge V2 (decommissioned prior to V1) | Backfill as needed; historical only |
| 3001-3999 | Scrooge V3 (active) | Current - adopt as decisions land |
| 4001+ | Reserved for future Scrooge major version | - |

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
| [1001](1001-box-reversal-core-philosophy.md) | Box reversal as core philosophy | Accepted | 2026-02-15 |
| [1002](1002-three-timeframe-stack.md) | Three-timeframe stack (D / H1 / M5) | Accepted | 2026-02-20 |
| [1003](1003-six-gate-signal-confirmation.md) | Six-gate signal confirmation | Accepted (gates 3+4 demoted in 1005) | 2026-02-20 |
| [1004](1004-pitchfork-entry-taxonomy.md) | Pitchfork entry taxonomy | Accepted | 2026-02-20 |
| [1005](1005-master-theory-realignment.md) | MASTER_THEORY realignment | Accepted | 2026-03-11 |
| [1006](1006-sl-advancement-only.md) | SL-advancement-only (no market exits) | Accepted | 2026-03-12 |
| [1007](1007-performance-cutoff-discipline.md) | Performance cutoff discipline | Accepted | 2026-03-05 |
| [1008](1008-fixed-pip-stops-and-50-ratchet.md) | Fixed-pip stops + 50% ratchet | Accepted | 2026-03-20 |
| [1009](1009-mr-sprite-removal.md) | Mr. Sprite crypto bot removal | Reverted | 2026-03-25 |
| [1010](1010-trade-coordinator-multi-actor.md) | TradeCoordinator multi-actor state | Accepted | 2026-04-10 |
| [2001](2001-modular-rewrite-v2.md) | V2 modular rewrite | Accepted (V2 retired) | 2026-03-21 |
| [2002](2002-dual-loop-architecture.md) | Dual-loop architecture (5min + 3sec) | Accepted | 2026-04-03 |
| [2003](2003-v3-scoring-system.md) | V3 Scoring System (WR-Lift Hybrid) | Accepted (superseded primary role by 3001) | 2026-04-15 |
| [3001](3001-regime-aware-not-global-score.md) | Regime-aware not global score | Accepted | 2026-04-15 |
| [3002](3002-branch-scorer-research-arc.md) | Branch scorer research arc — direct-only shadow scorer prototype | Accepted | 2026-04-29 |
| [3003](3003-harvest-orphan-two-pass-safety.md) | Stale-harvest LIMIT two-pass orphan safety | Accepted | 2026-04-29 |
| [3004](3004-harvest-same-cycle-race-and-ratchet-rollback.md) | Harvest same-cycle race fix + ratchet 0.7 → 0.5 rollback | Accepted | 2026-04-30 |
| [3005](3005-track-a-threshold-held-at-055.md) | LightGBM threshold held at 0.55 (Track A) | Superseded by 3017 | 2026-05-04 |
| [3006](3006-b1-attribution-architecture.md) | B-1 attribution architecture — OrderAttributionWriter + lookup | Accepted | 2026-05-04 |
| [3007](3007-drawdown-alerting-telegram-timer.md) | Telegram drawdown alerting via 5-min systemd timer | Accepted | 2026-05-04 |
| [3008](3008-matrix-router-replaces-regime-and-routing-stack.md) | MatrixRouter replaces regime + routing-table gate stack | Superseded by 3017 + 3019 | 2026-05-14 |
| [3009](3009-ml-observer-learns-cluster-serials.md) | ML observer learns cluster serials, not regime labels | Accepted | 2026-05-18 |
| [3010](3010-factor-buckets-v3-expansion.md) | factor_buckets v3 — expand RSI / BBP / ZS / ADR resolution | Accepted | 2026-05-22 |
| [3011](3011-decision-forest-per-combo-and-global.md) | Decision forest — per-combo + global trees | Accepted | 2026-05-23 |
| [3012](3012-matrix-router-loser-veto.md) | MatrixRouter loser-veto policy | Superseded by 3019 | 2026-05-25 |
| [3013](3013-natural-target-floor-and-feature-quality-floor.md) | NaturalTargetFloorGate + FeatureQualityFloorGate | Partially deprecated (NaturalTargetFloor disabled 2026-05-28) | 2026-05-25 |
| [3014](3014-entry-filter-family-loose-override-off.md) | EntryFilter.enable_family_loose_override default OFF | Accepted (gate retired with 3008) | 2026-05-25 |
| [3015](3015-htf-trend-filter-observe-to-hard.md) | HTF trend filter — observe → HARD | Superseded by 3008 (MatrixRouter) | 2026-05-27 |
| [3016](3016-six-strategy-promotion-and-routing-v1-14b.md) | 6-strategy promotion + routing_table v1.14b | Accepted | 2026-05-27 |
| [3017](3017-v3-hybrid-scorer-disabled-lightgbm-primary.md) | V3HybridScorer DISABLED + LightGBM v0 PRIMARY GATE @ 0.75 | Accepted | 2026-05-28 |
| [3018](3018-daily-circuit-gate-config-disabled.md) | DailyCircuitGate config-disabled — alerting carries the safety | Accepted | 2026-05-28 |
| [3019](3019-matrix-wiring-as-shadow-advisor.md) | Matrix wired as shadow advisor (not gate) alongside LightGBM | Accepted | 2026-05-29 |

