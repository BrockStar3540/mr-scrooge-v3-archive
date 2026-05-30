# 3005. Track A — LightGBM threshold held at 0.55, not promoted to 0.75 yet

**Status:** Superseded by 3017
**Date:** 2026-05-04
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

After the 60d broker-truth pull (152 trades / 39.6% WR / mean −$203/trade, sum −$30,958) and 47-factor audit (15 factor sign-flips between DBB and Direct families), the question was whether to tighten the LightGBM admission gate from 0.55 (Track A status quo) to 0.75 (Track B aspirational).

At 0.55, top ~10% of lab cohort → ~62% sim WR. At 0.75, top ~3% → ~75% sim WR. The tighter threshold throws away more trades but admits a higher-quality slice.

## Decision

**Hold at 0.55 for the May 4 decision window.** Track A continues. Re-evaluate after:
- B-1 attribution patches A + B.right land (so per-trade attribution is reliable; see ADR 3006)
- ≥30-50 closed trades at 0.55 to baseline realized vs sim WR
- Lab matrix integration completes (so the threshold decision incorporates per-pair signal, not just global LightGBM)

## Alternatives considered

- **Promote to 0.75 immediately** — rejected. We didn't have reliable per-trade attribution yet to confirm which threshold the realized losers were sitting at.
- **Drop to 0.45 to widen admission** — rejected outright. The broker-truth pull was unambiguously bad.
- **Disable the gate entirely pending matrix integration** — rejected. 0.55 was at least narrowing the bad slice somewhat.

## Consequences

- Held threshold at 0.55 until 2026-05-28.
- Promoted to 0.75 in ADR 3017 once the matrix routing was live and per-trade attribution was clean.

## Cross-references

- Vault: `wiki/projects/scrooge-v3-attribution-brokertruth-factors.md`
- Superseded by ADR 3017 (LightGBM PRIMARY GATE @ 0.75)
