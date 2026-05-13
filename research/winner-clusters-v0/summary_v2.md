# Winner-Cluster Discovery v2 — session-quarter granularity

Generated: 2026-05-13T01:57:19.797937+00:00

## What changed from v1

Added finer time axes to the ledger (5 new columns + updated session_bucket):
- : asia / london / overlap / ny_pm / rollover (NEW rollover)
- : <bucket>_q{1..4} (NEW)
- , 
- , 
- : open/early-mid/late-mid/late

UTC hour mapping:
- asia: 22-06 (8 hours, q1=22-23:59, q2=00-01:59, q3=02-03:59, q4=04-05:59)
- london: 06-12 (6 hours)
- overlap: 12-16 (4 hours, the London-NY high-vol window)
- ny_pm: 16-21 (5 hours)
- rollover: 21-22 (1 hour, single quarter)

Ledger is now 155 columns (was 149).

## Session distribution across full ledger

| session_bucket   |   count |
|:-----------------|--------:|
| asia             |     106 |
| london           |      72 |
| overlap          |      51 |
| ny_pm            |      36 |
| rollover         |       1 |

| session_quarter   |   count |
|:------------------|--------:|
| asia_q2           |      44 |
| london_q2         |      27 |
| asia_q3           |      27 |
| london_q1         |      24 |
| asia_q4           |      19 |
| overlap_q1        |      16 |
| asia_q1           |      16 |
| overlap_q2        |      15 |
| ny_pm_q2          |      12 |
| ny_pm_q4          |      11 |
| london_q4         |      11 |
| overlap_q3        |      10 |
| london_q3         |      10 |
| overlap_q4        |      10 |
| ny_pm_q1          |       7 |
| ny_pm_q3          |       6 |
| rollover_q4       |       1 |

## Coarse grain (strategy × pair_family × session_bucket × direction)

Total cells: 50
Cells with n≥2: 18
Cells with n≥5: 4

### Top coarse clusters by n_winners

| cluster_id                 | _strategy   | pair_family      | session_bucket   | direction   |   n_winners |   n_broker |   n_human |   n_ai_curated |   median_realized_r |   median_mfe_r | size_warning   |
|:---------------------------|:------------|:-----------------|:-----------------|:------------|------------:|-----------:|----------:|---------------:|--------------------:|---------------:|:---------------|
| unknow_antipo_asia_short   | unknown     | antipodean_cross | asia             | short       |           8 |          8 |         0 |              0 |                0.22 |         nan    | n<10_noisy     |
| unknow_usd_ba_london_short | unknown     | usd_base         | london           | short       |           7 |          7 |         0 |              0 |                0.11 |         nan    | n<10_noisy     |
| unknow_usd_ba_asia_short   | unknown     | usd_base         | asia             | short       |           5 |          5 |         0 |              0 |                0.57 |         nan    | n<10_noisy     |
| unknow_usd_ba_asia_long    | unknown     | usd_base         | asia             | long        |           5 |          5 |         0 |              0 |                0.21 |         nan    | n<10_noisy     |
| direct_gbp_cr_asia_long    | direct      | gbp_cross        | asia             | long        |           3 |          2 |         1 |              0 |                0.08 |           1.33 | n<5_unstable   |
| unknow_antipo_london_short | unknown     | antipodean_cross | london           | short       |           3 |          3 |         0 |              0 |                0.80 |         nan    | n<5_unstable   |
| dbb_tr_usd_ba_overla_short | dbb_trend   | usd_base         | overlap          | short       |           3 |          0 |         3 |              0 |                0.97 |           1.54 | n<5_unstable   |
| box_usd_ba_ny_pm_short     | box         | usd_base         | ny_pm            | short       |           2 |          0 |         2 |              0 |                1.18 |           1.63 | n<5_unstable   |
| dbb_tr_usd_ba_asia_short   | dbb_trend   | usd_base         | asia             | short       |           2 |          2 |         0 |              0 |                0.80 |         nan    | n<5_unstable   |
| unknow_eur_cr_london_long  | unknown     | eur_cross        | london           | long        |           2 |          2 |         0 |              0 |                1.16 |         nan    | n<5_unstable   |
| direct_antipo_overla_long  | direct      | antipodean_cross | overlap          | long        |           2 |          0 |         2 |              0 |                0.73 |           1.02 | n<5_unstable   |
| unknow_antipo_london_long  | unknown     | antipodean_cross | london           | long        |           2 |          2 |         0 |              0 |                0.28 |         nan    | n<5_unstable   |
| dbb_tr_antipo_ny_pm_short  | dbb_trend   | antipodean_cross | ny_pm            | short       |           2 |          0 |         2 |              0 |                0.71 |           1.10 | n<5_unstable   |
| unknow_eur_cr_asia_long    | unknown     | eur_cross        | asia             | long        |           2 |          2 |         0 |              0 |                1.21 |         nan    | n<5_unstable   |
| unknow_usd_ba_london_long  | unknown     | usd_base         | london           | long        |           2 |          2 |         0 |              0 |                0.08 |         nan    | n<5_unstable   |

## Fine grain (... × session_quarter)

Total cells: 70
Cells with n≥2: 14
Cells with n≥5: 0
**ALL fine-grain cells have n<5 size warning.** Sample size is the binding constraint.

### Top fine-grain clusters (treat as hypotheses, not statistical claims)

| _strategy   | pair_family      | session_bucket   | session_quarter   | direction   |   n_winners |   n_broker |   n_human |   n_ai_curated |   median_realized_r |   median_mfe_r | size_warning   |
|:------------|:-----------------|:-----------------|:------------------|:------------|------------:|-----------:|----------:|---------------:|--------------------:|---------------:|:---------------|
| unknown     | usd_base         | london           | london_q2         | short       |           4 |          4 |         0 |              0 |                0.16 |         nan    | n<5_unstable   |
| unknown     | antipodean_cross | asia             | asia_q3           | short       |           3 |          3 |         0 |              0 |                0.18 |         nan    | n<5_unstable   |
| unknown     | usd_base         | asia             | asia_q2           | long        |           3 |          3 |         0 |              0 |                0.09 |         nan    | n<5_unstable   |
| dbb_trend   | antipodean_cross | ny_pm            | ny_pm_q2          | short       |           2 |          0 |         2 |              0 |                0.71 |           1.10 | n<5_unstable   |
| unknown     | antipodean_cross | asia             | asia_q2           | short       |           2 |          2 |         0 |              0 |                0.69 |         nan    | n<5_unstable   |
| unknown     | antipodean_cross | asia             | asia_q1           | short       |           2 |          2 |         0 |              0 |                0.34 |         nan    | n<5_unstable   |
| unknown     | usd_base         | london           | london_q1         | short       |           2 |          2 |         0 |              0 |                0.57 |         nan    | n<5_unstable   |
| unknown     | eur_cross        | london           | london_q2         | long        |           2 |          2 |         0 |              0 |                1.16 |         nan    | n<5_unstable   |
| unknown     | usd_base         | asia             | asia_q3           | short       |           2 |          2 |         0 |              0 |                0.34 |         nan    | n<5_unstable   |
| unknown     | usd_base         | asia             | asia_q2           | short       |           2 |          2 |         0 |              0 |                0.93 |         nan    | n<5_unstable   |
| unknown     | antipodean_cross | london           | london_q1         | short       |           2 |          2 |         0 |              0 |                0.66 |         nan    | n<5_unstable   |
| unknown     | antipodean_cross | london           | london_q1         | long        |           2 |          2 |         0 |              0 |                0.28 |         nan    | n<5_unstable   |
| direct      | gbp_cross        | asia             | asia_q2           | long        |           2 |          2 |         0 |              0 |                0.08 |         nan    | n<5_unstable   |
| dbb_trend   | usd_base         | asia             | asia_q4           | short       |           2 |          2 |         0 |              0 |                0.80 |         nan    | n<5_unstable   |
| box         | gbp_cross        | ny_pm            | ny_pm_q2          | short       |           1 |          0 |         1 |              0 |                1.50 |           3.46 | n<5_unstable   |

## What the session_quarter view shows even at thin n

Top fine-grain cells by quarter (where winners are clustering even though n<5):

| session_quarter   |   count |
|:------------------|--------:|
| asia_q2           |      14 |
| london_q2         |      13 |
| asia_q3           |      10 |
| ny_pm_q2          |       8 |
| london_q1         |       8 |
| asia_q4           |       7 |
| london_q4         |       5 |
| overlap_q2        |       5 |
| asia_q1           |       5 |
| overlap_q3        |       4 |
| ny_pm_q4          |       3 |
| ny_pm_q3          |       2 |
| overlap_q1        |       2 |
| overlap_q4        |       1 |
| ny_pm_q1          |       1 |

Winners cluster heavily in **asia_q2** (Tokyo open, 00-02 UTC), **london_q1-q2** (06-09 UTC), and **asia_q3-q4** (mid-Asia, 02-06 UTC).

## Weekday × session winners

| weekday   |   asia |   london |   ny_pm |   overlap |
|:----------|-------:|---------:|--------:|----------:|
| Fri       |     10 |        2 |       2 |         1 |
| Mon       |      5 |        2 |       2 |         3 |
| Sun       |      1 |        0 |       0 |         0 |
| Thu       |      7 |        8 |       5 |         4 |
| Tue       |      4 |        4 |       4 |         2 |
| Wed       |      9 |       10 |       1 |         2 |

## What this answers

Brock's hypothesis: 'Asia direct antipodean' might be two different things —
Tokyo-open rail reversal vs late-Asia pre-London fakeout.

Finding: WITHIN asia, the bot's direct/antipodean shorts spread across q1-q4
with similar median R but the n is too small to statistically distinguish them.
Pattern is present (different quarters have different setups visible) but each
quarter cell has only 2-3 winners.

## What v2 cannot resolve

- Sample size: 110 winners ÷ 70 fine cells = 1.6 winners/cell average.
  Need ~5x more winning trades to make fine-grain statistically supportable.
- The corpus has 2.5M trades but only 11 features. Adding session_quarter at
  corpus scale (10x denser n per cell) would let us confirm or reject these
  fine-grain patterns. Requires extending feature extraction to corpus (v1 work).
- Naming clusters is still on hold per scope.

## Honest verdict

Session_bucket granularity is the right working level for THIS dataset.
Session_quarter is captured for future bigger-n work but is currently a
hypothesis substrate, not a statistical finding.

## Constraints

- No regime/strategy naming yet
- No backtest
- ready_for_backtest = FALSE everywhere