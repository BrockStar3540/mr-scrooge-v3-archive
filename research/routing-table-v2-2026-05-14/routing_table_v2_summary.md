# Routing Table v2 — built from ungated evidence

Built 2026-05-14.

## Counts
- Attached cells: **1,881**
- Unique (regime, pair, session) leaves: **528**
- v1 → v2 delta: **-923 cells**

## Sources
source
v3_trainer_probe_ungated    1802
textbook                      79

## Families
family
dbb_trend    797
reversal     566
direct       518

## Deny list
26 (probe × regime) cells documented as bleeders (sum_R ≤ −10 over 6mo).
Already auto-excluded by attachment rule; deny list is documentation only.

## Attachment rule
- n >= 10
- sum_R > 0.0
- WR >= 0.3

## Schema
regime53, regime_desc, pair, session_bucket, strategy, family, direction,
r_target, score_boost, n, wins, sum_R, mean_R, wr, source, last_updated
