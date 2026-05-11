# 1001. Box reversal as core philosophy

**Status:** Accepted (superseded in spirit by 3001's regime-aware approach; preserved in v3 Echo regime)
**Date:** ~2026-02-15 (pre-deployment design; documented in Feb 26 exec summary)
**Version scope:** V1
**Backfilled:** 2026-05-11

## Context

The bot needed a core thesis. The author's source theory (Doug & Sylvia's Liquidity Sweep Reversal Framework, captured later in `MASTER_THEORY.md`) argued that prior-day high (PDH) and prior-day low (PDL) act as liquidity magnets — institutional stop orders cluster just beyond, retail traders see "breakouts" and chase, institutions fade.

The empirical claim: price reaches a wall, triggers stops on both sides, briefly spikes, then reverses. That spike is the "sucker move" — and the entry signal is the *reversal candle* that follows it, not the spike itself.

## Decision

Build the entire entry system around prior-day box reversal:

1. **Box = `[PDL, PDH]` computed once per UTC midnight** from prior-session hourly candles.
2. **Trade only at the walls**, not the centre. Centre has no edge.
3. **Enter the reversal**, not the move into the wall.
4. **Fade chase, not trend-follow** the move toward the wall.

## Alternatives considered

- **Trend-following / momentum strategy** — rejected; transcripts explicitly framed price action as fade-the-extremes, not chase-the-move.
- **Mean reversion to intra-day mid** — rejected; lacks the institutional-order-cluster justification at any specific price.
- **Multi-zone confluence (Fibonacci / pivot points)** — rejected as over-engineered; PDH/PDL are the cleanest single-source-of-truth zones.
- **Random walk assumption (no edge)** — rejected; the bot existed because we believed there was structure.

## Consequences

**Enabled:**
- The entire V1 architecture is anchored to this. Zone detection, magic lines, sucker move detection, pitchfork entry triggers all flow from "trade reversals at walls."
- Survives structurally into V3 as the **Echo regime** in the v2 probe library — Bollinger bands (BB) are a smooth statistical analog of PDH/PDL hard walls. `echo_box_fade_v2` is the direct philosophical descendant.

**Closed:**
- Trend-following strategies in V1/V2 universe. (V3 reintroduces trend continuation via Charlie regime probes.)

**Costs:**
- Bot does nothing in centre-of-box conditions, which can be most of the trading day. Patience is a feature, not a bug.

## Cross-references

- `[[scrooge-v1-exec-summary-feb-2026]]` §2 (Box Theory — Core Philosophy)
- `MASTER_THEORY.md` in old `mr-scrooge` repo
- `[[scrooge-evolution-timeline]]` Pre-history + V1 Genesis
- ADR `3001-regime-aware-not-global-score.md` — V3 abstracts this into regime classifier
