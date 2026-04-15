# gates/atr_budget — Dev Log

> ATR budget gate: evaluates remaining daily range budget for a pair.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — ATR gate is advisory, not mandatory
**Source:** gates/atr_gate/NOTES.md, DAILY_NOTES_2026-03-11
**Type:** rule
**Detail:** Per MASTER_THEORY: "set your expectations" not a hard gate. Does NOT block trades. Logs strength for metadata/scoring only. V2 demoted to advisory — always passes.

### [2026-04-15] [V1 LIVE] — ATR consumed shows only 4% delta between W and L
**Source:** Raw OANDA candle analysis, docs/FACTOR_BIBLE.md
**Type:** correction
**Detail:** V1 live: W avg = 0.80, L avg = 0.83 (delta -4%). Nearly identical. Old scoring weighted ATR consumed at 0-20 pts — this is dead weight. Reduced to 0-4 pts. The 60-80% bucket has 75% WR but the averages barely differ. Keep as advisory, don't weight heavily.
