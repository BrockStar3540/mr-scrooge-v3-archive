# 3004. Harvest same-cycle race fix + ratchet 0.7 → 0.5 rollback

**Status:** Accepted
**Date:** 2026-04-30
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

Two issues converged on the same day:

1. **Same-cycle race in `reconcile_pending_orders`:** Orders placed during the same scan cycle as a reconcile read got tagged `broker_side_gone` and cancelled, because the broker-side snapshot was captured before the placement landed.
2. **Ratchet 0.7 live experiment outcome:** Lockup at +5 → +7 (0.7 of 0.5R-anchored MFE) was launched 2026-04-29 (ADR backfill candidate; not granted its own ADR — see scrooge-v3-ratchet-07-experiment vault page). After 27 trades the combined P&L was −$245/trade worse than the 0.5 control. Statistical floor for a real experiment hadn't been hit, but the loss magnitude warranted preemptive rollback.

## Decision

- **Harvest race (commit 373085e, merge 4008e6c):** Option B fix — same-cycle placements are now `union`-merged into `pending_on_broker` before the orphan check runs. 3 regression tests added.
- **Ratchet rollback (commit 73be822):** `ratchet_lock_pct: 0.7` → `0.5`. Single-line config revert. Logged in experiment_tracker as "rolled back early due to magnitude, not sample size."

## Alternatives considered

For the race:
- **Option A — defer all reconcile decisions one cycle** — rejected. Adds avoidable latency to legitimate cancels.
- **Option C — broker-side timestamp gating** — rejected. Broker timestamps aren't sub-cycle reliable enough on OANDA practice.

For the ratchet:
- **Wait for 100-trade floor** — rejected. The point of the experiment was to find out if 0.7 was better, not to keep losing money proving it wasn't. Magnitude-based early stop is the right call when the prior is "0.5 has been live and working."
- **Try ratchet 0.6 instead** — deferred. Worth revisiting only after we've stabilized the upstream admission edge (see ADR 3017).

## Consequences

- Harvest false-cancel rate confirmed dropped to 0 over the next 48h.
- Ratchet pinned at 0.5; future ratchet experiments require pre-registered stop rules.

## Cross-references

- Vault: `wiki/projects/scrooge-v3-harvest-same-cycle-race.md`
- Vault: `wiki/projects/scrooge-v3-ratchet-07-experiment.md`
- Commits: `373085e`, `73be822`, merge `4008e6c`
