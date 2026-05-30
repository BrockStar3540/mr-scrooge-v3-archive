# 3014. EntryFilter.enable_family_loose_override default OFF

**Status:** Accepted (gate retired with ADR 3008)
**Date:** 2026-05-25
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

P2 audit finding: `EntryFilterGate` was permitting cross-family cell approvals at the live trade-tier when `enable_family_loose_override=true`. Practical effect: a `dbb_trend` candidate could be approved against a `direct`-family routing cell because the family check was relaxed.

The "loose" override was meant for early lab-tier exploration where family signal was uncertain. By May 25 the trade-tier matrix was confident enough that this override was producing cross-family false positives in live.

## Decision

Flip default to `enable_family_loose_override: false`. Trade-tier admissions require exact family match. Lab-tier sweeps can still re-enable per-job.

## Alternatives considered

- **Remove the override entirely** — rejected. Lab-tier sweeps still want it for exploration runs.
- **Keep default `true` but tighten elsewhere** — rejected. The audit finding was specifically that this was the live-impact lever.

## Consequences

- Live admission rate dropped slightly (cross-family false positives gone).
- Gate later retired entirely as part of `MatrixRouterGate` collapse — see ADR 3008. The override mechanism survives in the lab harness.

## Cross-references

- Vault: `wiki/postmortems/fixes/scrooge-bug-fix-arc-2026-05-25.md`
