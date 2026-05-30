# 3003. Stale-harvest LIMIT two-pass orphan safety

**Status:** Accepted
**Date:** 2026-04-29
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

A Track 1 management failure audit surfaced harvest LIMITs that survived after their parent position closed, then fired as **naked positions** on the next price spike. Two failure modes:
1. The harvest ledger (`harvest-order-ledger.json`) had the orphan but the cancel-on-parent-close hook didn't fire.
2. The broker had pending harvest LIMITs that weren't in the ledger at all (e.g., placed during the same scan cycle as a reconcile pass that consumed an older parent-side snapshot).

Either path leads to "broker has order, V3 doesn't know, order fires as a naked entry."

## Decision

Two-pass safety in `reconcile_pending_orders`:
- **Pass 1 (2026-04-29 commit 4ad40b3):** Add GTD to all harvest LIMITs + extend the ledger to track parent-side state + wire cancel hooks on parent-close events.
- **Pass 2 (2026-04-30 commit 143247d):** Extend the orphan sweep to walk **broker pending orders directly** — not just the ledger — and cancel anything that doesn't have a live parent regardless of ledger state.

Ledger remains the primary record. Broker-side walk is the safety net for "ledger lost track" cases.

## Alternatives considered

- **GTD only, no ledger walk** — rejected. The same-cycle race (placed + reconcile in one cycle) doesn't show up in the ledger before reconcile reads it.
- **Stop placing harvest LIMITs entirely, manage TP1 in-band** — rejected. Pre-placed harvest LIMITs survive bot downtime, which is a Track 1 requirement.
- **Single-pass with broker-side walk only** — rejected. The ledger is still authoritative for "did we place this on purpose," and we want both views for audit.

## Consequences

- 9 regression tests added across both passes.
- Surfaced a related issue: `reconcile_pending_orders` was emitting false `broker_side_gone` cancels for orders placed in the same cycle. Fixed separately in ADR 3004.

## Cross-references

- Vault: `wiki/projects/scrooge-v3-stale-harvest-hotfix.md`
- Commits: `4ad40b3` (Pass 1), `143247d` (Pass 2)
