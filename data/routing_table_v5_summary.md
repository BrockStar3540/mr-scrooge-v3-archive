# routing_table_v4 summary

**Built:** 2026-05-15T21:37:44.663689+00:00
**Source:** hybrid shaver winner_islands_6yr (top-1 per parent cell) + loser_islands_6yr_top1 overlay
**Schema additions over v3:** shave_rule, loser_skip_rule, depth, hold_wins, hold_losses, window
**Rows:** 3945  (one per regime53 x pair x session)
**Distinct winner cells:** 765
**Cells with loser_skip_rule attached:** 3913

## Family breakdown

- **dbb_trend**: 1806 rows / 206 unique cells
- **direct**: 1051 rows / 101 unique cells
- **reversal**: 1088 rows / 115 unique cells

## Holdout-clean cells (hold_losses == 0)

- 3659 rows (93%)

## To deploy live

1. Update config 
2. EntryFilterGate is now in src/scrooge_v3/gates/entry_filter_gate.py
   Wire in bootstrap.py after RegimeStrategyRouterGate in OBSERVE mode for first 24-48h
3. Restart mr-scrooge-v3.service; confirm gate logs