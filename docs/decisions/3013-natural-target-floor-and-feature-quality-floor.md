# 3013. NaturalTargetFloorGate + FeatureQualityFloorGate

**Status:** Partially deprecated (NaturalTargetFloor disabled 2026-05-28)
**Date:** 2026-05-25
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

Two distinct quality problems with the candidate stream:

1. **Natural-target floor:** Some symbols at some moments have a market projection (M5 ATR × 3 vs BB-width/2, MIN) below the 7-pip scalp floor. Trades fired into those windows can't reach even modest TP, regardless of strategy or matrix signal.

2. **Feature-quality floor:** When EMA / RSI / zone_detector returned degraded defaults due to insufficient bars (cold start, gap, data outage), the V3 scorer was silently consuming the defaults as if they were real signal. Trades fired against zeroed-out features.

Both were live-money quality failures that the matrix can't catch — they're pre-matrix issues.

## Decision

Two new HARD gates:

- **`NaturalTargetFloorGate`** — recomputes per-symbol per-cycle market projection from live M5 ticks; blocks all strategies on a symbol whose realistic move-potential is below the 7-pip scalp floor.
- **`FeatureQualityFloorGate`** — blocks candidates on symbols where EMA/RSI/zone_detector returned insufficient-bars defaults. Tracked via `critical_features` config list.

## Alternatives considered

- **Move both checks into individual strategy modules** — rejected. Both are symbol-wide concerns, not strategy-specific. Centralizing in the gate pipeline avoids 13 copies of the same check.
- **Silent skip without logging** — rejected. We want the audit trail when a symbol gets excluded.

## Consequences

- `FeatureQualityFloorGate` kept HARD through subsequent cleanups.
- `NaturalTargetFloorGate` later disabled (2026-05-28) once lab-mined per-pair WIN/LOSE rules incorporated the same quality bar implicitly — see LIVE_SYSTEM_SPEC. Kept registered (config-flippable) for revival.

## Cross-references

- Vault: `wiki/postmortems/fixes/scrooge-bug-fix-arc-2026-05-25.md`
