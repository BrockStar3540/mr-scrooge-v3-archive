# 1004. Pitchfork entry taxonomy

**Status:** Accepted; precise thresholds active in V1; survives into V3 as wick-rejection conditions
**Date:** ~2026-02-20 (pre-deployment); explicit thresholds in `gates.py:SignalEngine`
**Version scope:** V1 (preserved into V2; loosened in V3)
**Backfilled:** 2026-05-11

## Context

After sucker-move termination at a magic line, the bot needed a precise definition of "the reversal candle that confirms entry." Source theory (Doug & Sylvia) named three patterns. The doctrine doc captured exact numeric thresholds.

## Decision

Three named pitchfork variants, in priority order:

### John Wick
- Wick ≥ 60% of total candle range
- Body ≤ 30% of total range
- Wick ≥ 2× body size
- Long wick points in the direction of the rejected move
- *Theory:* price moved hard one way, completely rejected, closed in opposite direction. Trapped traders' stops become fuel.

### Power of Towers
- Full engulfing candle: candle 2 completely engulfs candle 1 **including the wicks**
- (Not body-to-body. Wicks must be fully contained.)
- *Theory:* in a single candle, market erased everything the prior did and went further. Institutional volume overwhelmed retail direction completely.

### Standard Pitchfork
- 3-5 strong directional candles toward the sucker move
- Then first candle closing in the opposite direction
- *Constraint:* Valid signal but requires strong zone + ATR backing. **Not sufficient alone at marginal OTR levels.**

## Alternatives considered

- **Single reversal pattern (e.g. just engulfing)** — rejected. Three patterns capture different microstructure flavors; one pattern leaves real setups on the table.
- **Looser thresholds (e.g. wick ≥ 50% instead of 60%)** — rejected at V1; introduced gradually in V3 via probe-level wick-rejection conditions (e.g. `echo_box_fade_v2` requires `lower_wick ≥ body`, much looser than V1's 60%/30%/2×).
- **No pattern requirement (just reversal close)** — rejected. Too permissive; produces high-frequency low-quality entries.

## Consequences

**Enabled:**
- Auditable entry signals — every fired trade has one of three named patterns identifying it.
- "John Wick at Tier-1 zone + 80% ATR" is a recognizable high-confidence setup pattern (used in the open-wait exception, ADR 1006).
- Wick-rejection logic survives into V3 probes (`echo_box_fade_v2`, `alpha_extended_fade_v2`).

**Closed:**
- Entries without an identifiable reversal-pattern signature.

**Costs:**
- V3 uses much looser thresholds (no explicit 60%/30%/2× rule). May be giving up signal quality for fire rate. **Future ADR could revisit reintroducing the strict V1 thresholds as an optional tightening.**

## Cross-references

- `[[scrooge-v1-exec-summary-feb-2026]]` §7 (Pitchfork Entry Signals)
- `gates.py` `SignalEngine._check_pitchfork()` and `PitchforkResult` (in `BrockStar3540/mr-scrooge`)
- V3 probes: `scripts/playbook_probes_v2.py` `probe_echo_box_fade_v2`, `probe_alpha_extended_fade_v2`
