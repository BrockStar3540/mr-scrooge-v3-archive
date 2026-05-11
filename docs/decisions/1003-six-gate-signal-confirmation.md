# 1003. Six-gate signal confirmation (no overrides)

**Status:** Accepted; modified 2026-03-11 (gates 3 & 6 demoted to advisory via ADR 1005)
**Date:** ~2026-02-20 (pre-deployment); enumerated in `gates.py` SignalEngine
**Version scope:** V1 (preserved structurally into V2; reframed per-probe in V3)
**Backfilled:** 2026-05-11

## Context

The bot needed an explicit, sequential validation pipeline so every entry could be audited end-to-end. The Feb 2026 doctrine doc says it plainly: "no discretion, no overrides."

## Decision

Every potential trade passes through **6 sequential gates**. Failed gate → immediate reject + log reason. Order matters (cheap gates first).

The final V1 gate order, as enumerated in `gates.py:SignalEngine`:

| # | Gate | Hard / Advisory |
|---|---|---|
| 1 | Zone proximity (within `zone_proximity_pct` of PDH/PDL) | Hard |
| 2 | Trend regime filter (Tier 3/4 zones only — Tier 1/2 box-extreme overrides) | Hard |
| 3 | ATR | Advisory (post-Mar 11) |
| 4 | OTR (round-trip spread vs half-box) | Advisory (post-Mar 11) |
| 5 | Sucker move (3-5 directional + reversal) | Hard |
| 6 | Pitchfork (John Wick / Power of Towers / Standard) | Hard |

(Pre-Mar 11, gates 3 and 4 were also hard rejects — see ADR 1005.)

## Alternatives considered

- **Single composite score** — rejected. V1 doctrine wanted auditability per-gate; one score loses "why this trade?"
- **Discretionary override** — rejected. "No discretion, no overrides" was a design principle.
- **Parallel evaluation (all gates simultaneously)** — rejected. Sequential lets cheap gates short-circuit early; logs show exact rejection reason.

## Consequences

**Enabled:**
- Every rejection has a single auditable reason. `logs/decisions.log` lists gate-by-gate rejections.
- Adding/removing gates is a localized change (one `if` block in `SignalEngine`).
- The structural discipline survives into V3 per-probe condition lists (each v3 probe has 3-5 deterministic conditions, same spirit).

**Closed:**
- Discretionary trade entry. Forever.

**Costs:**
- A genuinely good setup that fails one marginal gate is missed. Mitigated by the "open wait exception" at 50% size for Tier-1 + 80% ATR + premium pitchfork (ADR 1006).

## Cross-references

- `[[scrooge-v1-exec-summary-feb-2026]]` §8 (Six-Gate Signal Confirmation)
- `gates.py:1604-1693` (SignalEngine gate enumeration) in `BrockStar3540/mr-scrooge`
- ADR `1005-master-theory-realignment.md` — what happened to gates 3 and 4
- `[[scrooge-strategy-regime-playbook-matrix]]` v0.2 — V3 per-probe conditions inherit this spirit
