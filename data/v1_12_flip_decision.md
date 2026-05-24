# v1.12 Flip Decision
**Updated:** 2026-05-24 05:21 UTC

## Source of Truth
- `20f5af2` is the authoritative TIER1A/FULL build
- `00cc624` (earlier TIER1A 20-row build) is superseded — disregard

## Routing Tables (as of 20f5af2)
| File | Rows | Leaves | Status |
|------|------|--------|--------|
| `routing_table_v10_fast_current_regime.parquet` | 10 | - | **LIVE (v1.11.5)** |
| `routing_table_v10_fast_v1_12_tier1a.parquet` | 26 | 24 | Staged, not flipped |
| `routing_table_v10_fast_v1_12_full.parquet` | 34 | 32 | Staged, not flipped |

## Flip Sequence

### Preferred Path (Path B — direct to FULL)
1. Reopen on `v1.11.5` — Sunday 22:00 UTC
2. Monitor Monday asia (00:00), london_open (06:00), ny_mid (13:00)
3. If **mechanically clean** → flip straight to `v1.12_FULL` (34 rows)
4. TIER1A is the fallback only

### Fallback Path (Path A — staged via TIER1A)
Use ONLY if Monday telemetry reveals a real mechanical issue specifically in:
- `canonical_lien_dbb` family cells misbehaving
- MTB3 emotional/travel variants (MTB3_pitchfork_*) causing exceptions
- sub_regime NaN rows causing routing mismatches

If fallback triggered: flip to TIER1A (26 rows) first, fix the issue, then promote to FULL.

## Mechanical Clean Definition
All of the following must be true before flipping to FULL:
- No strategy exceptions in telemetry log
- No family_lock weirdness (family_loose_override firing unexpectedly)
- No sub-regime mismatches on the NaN sub_regime rows in TIER1A/FULL
- No silent windows — at least 1 emission in asia and 1 in london_open
- No obviously broken fills (immediate stop-outs across multiple cells)

## Monday Telemetry Report Must Include
1. First emissions by family (reversal / direct / box_master_theory)
2. First approvals by family
3. First fills by family
4. Any exceptions in log
5. Behavior of the 10 DROP cells during v1.11.5 window (do they justify themselves?)
6. canonical_lien_dbb probe first behavior after flip (if FULL path taken)

## Flip Command (FULL path)
```bash
# After confirming Monday telemetry is clean:
# Update bot config routing_table to: routing_table_v10_fast_v1_12_full.parquet
# Restart or hot-reload
```

## Boot Confirmation (both tables)
- TIER1A: rows=26, leaves=24 ✅
- FULL: rows=34, leaves=32 ✅
- canonical_lien_dbb: 2 probes loaded ✅
- MTB DEFAULT_VARIANTS: 21 ✅
