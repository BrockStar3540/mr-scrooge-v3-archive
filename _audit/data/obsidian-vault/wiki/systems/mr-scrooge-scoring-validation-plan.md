# Mr. Scrooge Scoring Validation Plan

type: system
status: active
tags: [scrooge, trading, scoring, validation]

trust:
  score: 85
  confidence: medium
  evidence:
    - source: OANDA audit 2026-04-09, scoring deployed same day
      type: firsthand

## Summary
The scoring system was recalibrated on 2026-04-09 from OANDA trade data. The calibration is based on historical patterns (511 V1 + 58 V2 trades). It needs live validation — we don't yet know if the new scores predict winners in forward-looking conditions.

## Current State
- Scoring deployed on both V1 and V2 (2026-04-09)
- Layer 4 OANDA truth adjustments: ranging -20, CT+PoT -15, CT+JW -5, CT T1 -10, CT T2 +5, z-align +5
- Signal reweighting: john_wick +15, power_of_towers +5
- Regime integration: NORMAL +10, CAUTION/RESTRICTED -10
- R:R scoring uses TP1 (realistic target)
- Score does NOT disqualify — it ranks. Any gate-passed signal can fire if it's the best available.
- No minimum score threshold yet.

## What We Need To Validate
After 50-100 trades on each bot with the new scoring:

1. **Does score predict outcome?** Group trades by score range (0-30, 30-50, 50-70, 70+). Compare win rate and P/L per bucket. If higher scores = better outcomes, the calibration works.

2. **Should there be a minimum score threshold?** If trades below score 30 consistently lose, add a hard gate. The data will tell us where to draw the line.

3. **Are the Layer 4 weights still correct?** Market conditions change. The -20 ranging penalty was calibrated from Feb-Apr 2026 data. Re-audit quarterly.

4. **Do the signal type weights hold?** john_wick +15 vs power_of_towers +5 was based on historical P/L. Verify with forward data.

5. **Is the regime integration too aggressive?** NORMAL +10 / CAUTION -10 is a 20-point swing. Check if CAUTION trades are actually worse under the new scoring or if the penalty is double-counting.

## How To Validate
1. Let both bots trade for 2-4 weeks undisturbed
2. Pull all closed trades from OANDA API (source of truth, not bot logs)
3. Cross-reference with entry-context.jsonl (has score, score_detail, regime_state, signal_type, z_score, etc.)
4. Run the same analysis as the 2026-04-09 audit: score vs P/L correlation, combo analysis, regime breakdown
5. Compare results to the calibration baseline

## Data Sources
- OANDA trades API: realized P/L (truth)
- entry-context.jsonl: score, score_detail, all indicator snapshots (bot's view)
- Both must agree — if they don't, the P/L calculation bug may have regressed

## Decision Points
- **Score predicts winners (r > 0.3 with P/L):** Keep calibration. Consider adding minimum score threshold where data shows consistent losses.
- **Score is neutral (r near 0):** Recalibrate weights. Something changed or the historical pattern doesn't hold forward.
- **Score inversely predicts (r < 0):** Stop, re-audit from scratch. Don't trade on a broken scorer.

## Timeline
- **Now (2026-04-09):** Scoring deployed. Logging active. Do not touch weights.
- **After 50 trades (~2-3 weeks):** Preliminary check. Is the direction right?
- **After 100 trades (~4-6 weeks):** Full validation audit. Decide on minimum threshold.
- **Quarterly:** Re-audit weights against fresh OANDA data.

## Rules
- Do NOT change scoring weights without running the OANDA audit first
- Do NOT trust bot logs for P/L — always verify against OANDA API
- Do NOT add a minimum score threshold until the data supports it
- Log everything — the entry-context.jsonl is the dataset for the next audit

## Key Takeaways
- The scoring system is an experiment, not a proven system
- 50-100 forward trades will tell us if the calibration works
- The bot logs scores and outcomes automatically — the data will be there when we need it
- Patience. Let it trade. Then audit.

## Related
- [[Mr. Scrooge V1 Scoring System]]
- [[Mr. Scrooge V2 Scoring System]]
- [[Mr. Scrooge Scoring Inversion Postmortem]]
- [[Mr. Scrooge Known Defects]]
