# Mr. Scrooge V1 OANDA Audit — 2026-04-09

type: fact
status: resolved
tags: [scrooge, trading, postmortem, audit, v1]

trust:
  score: 95
  confidence: high
  evidence:
    - source: OANDA API data — 511 closed trades, 1077 ORDER_FILL transactions
      type: dataset
    - source: independent cross-audit with V2 session confirmed identical findings
      type: reproducible

## Summary
The V1 scoring system had zero predictive power — higher scores correlated with worse outcomes. The bot was blind to ranging markets (PF 0.33, the #1 profit killer) and over-weighted counter-trend entries at Tier 1 zones (the worst category). P/L calculations were wrong for 17 of 21 instruments. Two independent audits (V1 and V2) converged on the same findings using OANDA API data, not bot logs.

## What Failed

1. **Scoring system inversely correlated with outcomes** — ranking score had r ≈ 0 with P/L. The 70-79 score bracket was the biggest loser (-$340 on 40 trades). The 60-69 bracket was the most profitable.

2. **Ranging markets scored identically to with-trend** — the trend gate only asked "is this counter-trend?" If the answer was no (because there was no trend), it scored 1.0 — same as a strong with-trend entry. Ranging trades produced PF 0.33 in both bots.

3. **Counter-trend Tier 1 was the worst category, not the best** — the "Tier 1 zone overrides uptrend" theory was disproven. CT at Tier 1 (PDH/PDL): 45.7% WR, -$537. CT at Tier 2 (PHH/PHL): 66.7% WR, +$140.

4. **R:R calculated against TP2 (fantasy)** — TP2 (opposite box wall) was hit on only 6.6% of 500 trades. R:R against TP1 had r=0.68 with P/L — the strongest single predictor.

5. **P/L calculation in quote currency** — `(exit - entry) * qty` gives result in quote currency, not USD. For USD/MXN, bot logged -$124.90 vs OANDA actual -$22.09.

## Root Cause

- The scoring system was built on theory ("Tier 1 zones are strongest") rather than calibrated against outcomes
- Ranging detection existed in the trend gate but was never surfaced to the scoring function
- The P/L bug was masked when OANDA's `get_trade_realized_pl()` succeeded, but fired when the endpoint returned 404 for closed trades

## Discovery

Two parallel Claude Code sessions independently audited V1 (511 trades, live account) and V2 (58 trades, practice account) by pulling data directly from the OANDA API. Key methodology:
- Used OANDA H1 candle data + 50H EMA slope to classify trend/ranging independently of bot logs
- Cross-referenced OANDA `realizedPL` with bot-logged P/L to find discrepancies
- Joined OANDA fill data with bot decision logs via client ID (scrooge_xxx)

Both audits converged on the same findings: ranging = killer (PF 0.33), CT ≈ breakeven (PF 1.03), with-trend = edge (PF 1.91).

## Fix Applied

**Scoring (gates.py `_calculate_score()`):**
- Layer 3b OANDA truth modifiers: ranging -20, CT+PoT -15, CT+JW -5, CT T1 -10, CT T2 +5, z-align +5
- Signal reweighting: john_wick +15 (was +10), power_of_towers +5 (was +10)
- R:R scoring uses TP1 (buckets: >=2.0 +15, >=1.5 +10, >=1.0 +5)
- Score floor: min=1

**Regime (main.py):**
- NORMAL +10, CAUTION -10 applied to signal score before ranking

**Bugs (multiple files):**
- P/L currency conversion via pip_value_per_unit
- Overhead cost USD conversion
- OANDA 404 fallback to transactions API
- TP sanity clamp at 3x ATR
- Entry-context null outcomes
- Log duplicate handler fix

## Prevention

- Future scoring changes must be validated against OANDA trade data (not bot logs)
- Audit data preserved: `data/audit/scrooge_v1_audit.csv`, `data/audit/oanda_v1_fills.json`
- Changelog process established: every change documented with evidence

## Key Takeaways

- Bot logs can lie — OANDA API is the only source of truth for trade outcomes
- Theory-based scoring ("Tier 1 is strongest") must be validated against data before production
- Two independent audits catching the same bugs builds confidence in the fix
- The scoring system needs re-auditing periodically as market conditions change

## Related
- [[Mr. Scrooge V1 Scoring System]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge V1 Changelog]]
- [[Mr. Scrooge V1]]
