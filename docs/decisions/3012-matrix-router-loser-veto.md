# 3012. MatrixRouter loser-veto policy

**Status:** Superseded by 3019
**Date:** 2026-05-25
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

Initial `MatrixRouter` (ADR 3008) admitted any cell that matched a WIN rule. But the matrix also surfaces **LOSE rules** — high-confidence signatures that lose at sample sizes large enough to trust. The original admission policy ignored LOSE rules: if a candidate matched both a WIN rule and a LOSE rule, the WIN rule won.

Empirically the LOSE side is more reliable signal than the WIN side at the matrix's confidence levels.

## Decision

Upgrade `MatrixRouter` to **loser-veto**: any candidate matching a LOSE rule at the matrix's confidence threshold is rejected regardless of WIN-side matches. Specifically:
- If LOSE rule fires at `n_kept ≥ 20` and realized WR ≤ 35%, veto.
- WIN rule fires only matter if no LOSE rule vetoes.

Asymmetric by design — LOSE rules are the more reliable side.

## Alternatives considered

- **Tie-break by sample size** — rejected. Sample size correlation with reliability is weaker than the WR-floor cutoff.
- **Weight WIN vs LOSE rules and sum** — rejected. Loses the categorical clarity ("did the matrix say avoid?") and introduces tuning surface.
- **Move loser-veto to a separate gate** — partially adopted later (4-layer matrix cascade, briefly), then collapsed back into the router.

## Consequences

- Admission rate dropped modestly; realized WR on admitted candidates improved.
- Set up the cleanup for the 4-layer cascade (briefly tried, then collapsed 2026-05-28 — see ADR 3019 retired list).

## Cross-references

- Task #35
- Superseded by ADR 3019 once matrix shifted to a shadow advisor
