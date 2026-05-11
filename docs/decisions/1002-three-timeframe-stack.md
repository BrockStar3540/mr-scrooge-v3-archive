# 1002. Three-timeframe stack (D / H1 / M5)

**Status:** Accepted
**Date:** ~2026-02-20 (pre-deployment design)
**Version scope:** V1 (preserved into V2, V3)
**Backfilled:** 2026-05-11

## Context

The box-reversal strategy required answering three different questions about price:
1. Where are the walls? (PDH/PDL)
2. Where within the box are the higher-quality sub-zones?
3. When does price actually reverse at a wall?

Each question lives on a different timeframe with different data characteristics. Using one timeframe for all three loses information.

## Decision

Three timeframes, each with a distinct and **non-interchangeable** role:

| Timeframe | Role |
|---|---|
| **Daily** | Box computation: PDH, PDL, daily ATR, gap detection |
| **H1 (hourly)** | Magic lines: higher-quality zones within the box, polarity-flip levels |
| **M5 (5-min)** | Entry signal: pitchfork (John Wick / Power of Towers / Standard) |

Each timeframe is fetched independently every cycle. Cross-timeframe coherence is checked at the gate level (e.g. don't enter long if H1 magic line is bearish even if M5 pitchfork is bullish).

## Alternatives considered

- **Single timeframe (e.g. M5 only)** — rejected; loses the box context and zone hierarchy.
- **Two timeframes (D + M5)** — rejected; loses the magic-line layer where institutional stop clusters concentrate.
- **Four timeframes (add weekly)** — considered for context; not adopted in V1 (added cost without proportional signal).

## Consequences

**Enabled:**
- Tier-aware zone classification (Tier 1 box-extreme vs Tier 3 mid-box magic line).
- High-volatility exception: skip M5 pitchfork and enter directly on H1 pitchfork when M5 is too noisy.
- Survives into V3: `replay_context.py` `build_snapshot()` pulls D/H1/M5 candles per scan; `_CANDLE_COUNTS_VALIDATION = {"D": 50, "1H": 50, "5M": 50}`.

**Closed:**
- Single-timeframe-only strategies.

**Costs:**
- 3× the data-fetch cost per scan vs single timeframe. Acceptable given OANDA's per-cycle rate limits.

## Cross-references

- `[[scrooge-v1-exec-summary-feb-2026]]` §4 (Three-Timeframe System)
- `Oanda-Bot-Trainer/src/replay_context.py` — V3 implementation
- `[[scrooge-evolution-timeline]]` Pre-history
