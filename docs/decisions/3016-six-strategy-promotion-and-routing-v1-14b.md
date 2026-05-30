# 3016. 6-strategy promotion + routing_table v1.14b

**Status:** Accepted
**Date:** 2026-05-27
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

Six research strategies (ifvg, session_breakout, compression_expansion, trend_pullback, chaikin_macd_atr, compression_reversion) had completed sufficient lab validation to enter live admission. The prior routing table (`v10_fast_v1.13`) didn't include cells for them — they were registered in `bootstrap.py` but had no routable surface.

Promotion gated on:
- LightGBM v0 holdout AUC ≥ 0.60 (achieved: 0.6025)
- Matrix factor_lift coverage for all 6 families
- Per-pair WIN/LOSE rules for at least the top 10 pairs per family
- B-1 attribution Patch C (commit 64410a3) to fix scan-dashboard JSON-stripping that was blinding ML observer + broker attribution

## Decision

Build and activate `routing_table_v10_fast_v1_14b_full_matrix.parquet` — 1737 rows, 250 leaves. Adds cells for all 6 promoted strategies + retains legacy reversal / dbb_trend / direct / box_master_theory coverage. Sets the file as the live routing table at next reboot.

Two strategies deferred to a later version (`v1.14c` candidate):
- `compression_expansion` BE config A/B lab sweep
- `compression_reversion` matrix rebuild

## Alternatives considered

- **Promote 4 strongest only (skip CE + CR)** — rejected. Better to admit them with conservative routing and let live data inform refinement than to delay.
- **Promote without B-1 Patch C** — rejected. Without the attribution fix, we couldn't measure whether the promoted strategies were over- or under-performing.
- **Promote all 6 with matched lab parameters even if matrix-poor** — rejected for CE + CR; their lab signal needed the rebuild.

## Consequences

- 13 strategies registered, 7+ actively routable.
- Daily circuit tripped same day until 2026-05-28 00:00 UTC (carry-over from prior streak); recovery began with the new routing live.
- Set up the matrix wiring as shadow advisor (ADR 3019) by establishing the matrix as canonical.

## Cross-references

- Vault: `wiki/postmortems/fixes/scrooge-v3-strategy-promotion-2026-05-27.md`
- Commits: `64410a3` (Patch C), `6db6a4d` (promotion), `04814c9` (matrix advisor wiring), `535b087` (HTF gate observe→hard), `14b` parquet build
