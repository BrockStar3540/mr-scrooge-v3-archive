---
type: fact
status: resolved
tags: [scrooge, trading, postmortem, scoring, audit]
trust:
  score: 95
  confidence: high
  reason: Direct OANDA API evidence from 511 V1 + 58 V2 closed trades, fully reproducible
---

## Summary

On 2026-04-09, two independent OANDA API audits discovered that Mr. Scrooge's scoring system had zero predictive power and was actively selecting for losing trades. Higher scores correlated with worse outcomes. The root cause was four compounding blind spots in the scoring logic. A comprehensive fix was applied the same day, recalibrating the scoring system against empirical OANDA data.

## What Failed

The scoring system was supposed to rank signals so the best opportunities scored highest. Instead, it did the opposite:

| Score Bracket | Win Rate | P/L |
|---|---|---|
| 70-80 | 60% | -$6,138 |
| 60-70 | 80% | +$2,724 |

The system actively selected for losers. Signals the bot rated as its best opportunities were its worst performers.

## Root Cause

Four compounding problems:

### 1. Scoring Blind to Trend Alignment

Ranging markets scored identically to trending markets. OANDA data showed ranging markets had a profit factor of 0.33 across both bots (225 V1 + 27 V2 trades). The scoring system had no mechanism to penalize entries during ranging conditions.

### 2. R:R Computed Against TP2

The reward-to-risk ratio used TP2 (opposite box wall) for scoring. TP2 was hit only 6.6% of the time. This inflated R:R scores for entries that realistically would never reach their scored target. Garbage entries with distant TP2 levels scored well on paper but failed in practice.

### 3. Signal Types Weighted Equally

`john_wick` and `power_of_towers` both received the same score weight despite radically different outcomes. `power_of_towers` bled -$4,086 in V1 data. `john_wick` was consistently profitable (+$1,267 in V2). Equal weighting meant the scoring system could not distinguish between a profitable signal type and a losing one.

### 4. Regime State Not Integrated

The regime system correctly identified NORMAL (77.8% WR, +$5,037) vs CAUTION (57.9% WR, -$5,719) conditions but this information was not fed into scoring. Signals in hostile regimes scored just as high as signals in favorable regimes.

## Discovery

Two independent OANDA API audits:

- **V1 audit:** Pulled 511 closed trades, classified trend direction via 50-period EMA on H1 candles, cross-referenced with entry-context scoring data
- **V2 audit:** Pulled 58 closed trades with the same methodology

The audits were independent (different sessions, different Claude instances) and reached the same conclusions. Bot log P/L data was found to be incorrect for 17 out of 21 currency pairs due to a quote-currency conversion bug, which is why the problem had not been caught earlier through log analysis alone.

## Fix Applied

### Scoring Changes

- **Layer 4 (OANDA truth):** Added ranging penalty (-20), counter-trend combo penalties (CT+PoT -15, CT+JW -5, CT T1 -10), counter-trend tier 2 bonus (+5), z-alignment bonus (+5)
- **Signal reweighting:** john_wick raised to +15, power_of_towers reduced to +5
- **Regime integration:** NORMAL +10, CAUTION/RESTRICTED -10 injected into signal score
- **R:R scoring:** Changed from TP2 to TP1 basis
- **Score floor:** Minimum score of 1 for all_gates_passed signals (prevents regime penalty from zeroing)

### Bug Fixes (Same Session)

- **P/L quote currency conversion:** Bot was reporting P/L in quote currency, not account currency. Fixed for 17/21 non-USD-quote pairs.
- **Overhead cost bug:** Fixed incorrect cost calculation in position tracking
- **OANDA 404 fallback:** Added graceful handling when OANDA returns 404 for instrument data
- **TP2 3x ATR clamp:** Added ceiling to prevent unrealistic TP2 targets
- **Log rotation:** Added RotatingFileHandler for decisions.log and trades.log (10MB, 5 backups)
- **Duplicate log handler:** Fixed duplicate line output in main log

## Prevention Rules

1. **Future scoring changes require OANDA trade data validation, not bot log analysis.** Bot logs lie --- P/L was wrong for 17/21 pairs. Always pull closed trades from the OANDA API and compute P/L independently.

2. **Never trust the bot's own trend classification.** Verify against OANDA candle data independently (e.g., 50-period EMA on H1 candles from OANDA instruments endpoint).

3. **Any new scoring factor must show statistical significance against OANDA realized P/L.** No factor should be added based on theoretical reasoning alone. Pull the trades, classify them, compute the P/L split.

## Data Preservation

Audit files saved to `data/audit/` in both V1 and V2 bot directories on EC2. These contain the raw OANDA trade data, classification results, and P/L computations used to derive the Layer 4 values.

## Key Takeaways

- Scoring systems can invert silently --- higher scores meant worse outcomes, and nothing in the bot's own logging detected this
- Bot logs are secondary data. OANDA API is truth. The P/L bug affecting 17/21 pairs meant log-based analysis would have reached wrong conclusions.
- Ranging markets (PF 0.33) were the single largest source of losses and had zero scoring penalty before this fix
- Equal-weighting signal types masked a 3x difference in profitability between john_wick and power_of_towers
- Two independent audits reaching the same conclusions increases confidence that the findings are correct

## Related

- [[Mr. Scrooge V2 Scoring System]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge V2]]
