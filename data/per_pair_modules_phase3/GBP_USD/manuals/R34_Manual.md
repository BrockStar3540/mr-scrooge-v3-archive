# GBP_USD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,560**  (W=1,562 / L=998)  -  WR: **61.0%**

## Session distribution

- asia: n=815  W=493/L=322  WR=60.5%
- ny_close: n=656  W=398/L=258  WR=60.7%
- london_open: n=251  W=160/L=91  WR=63.7%
- london: n=232  W=150/L=82  WR=64.7%
- ny_open: n=231  W=137/L=94  WR=59.3%
- ny_mid: n=208  W=127/L=81  WR=61.1%
- asia_late: n=116  W=65/L=51  WR=56.0%
- off_hours: n=51  W=32/L=19  WR=62.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude session_bucket=asia drops 10/21 losers (48%)
- **Final: n=101  W=90/L=11  WR=89.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W02.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude session_bucket=asia drops 10/21 losers (48%)
- **Final: n=101  W=90/L=11  WR=89.1%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W03.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=120  W=115/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=116  W=115/L=1  WR=99.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W04.  `T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=120  W=115/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=116  W=115/L=1  WR=99.1%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W05.  `T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=120  W=115/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=116  W=115/L=1  WR=99.1%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W06.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=120  W=115/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=116  W=115/L=1  WR=99.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W07.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=119  W=114/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W08.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=119  W=114/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W09.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=119  W=114/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W10.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=119  W=114/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W11.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=119  W=114/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W12.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=119  W=114/L=5  WR=95.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W13.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude RSI=RSI5 drops 11/17 losers (65%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 60-70 strong

### W14.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude RSI=RSI5 drops 11/17 losers (65%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 60-70 strong

### W15.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude RSI=RSI5 drops 11/17 losers (65%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 60-70 strong

### W16.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude RSI=RSI5 drops 11/17 losers (65%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W17.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude RSI=RSI5 drops 11/17 losers (65%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 60-70 strong

### W18.  `H20=H20a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid

### W19.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_mid

### W20.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_mid

### W21.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_mid

### W22.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid

### W23.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid

### W24.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid

### W25.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=109  W=108/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=109  W=108/L=1  WR=99.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI6`
- Raw: n=344  W=127/L=217  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (61/217 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L02.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=337  W=127/L=210  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_mid (61/210 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L03.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=337  W=127/L=210  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_mid (61/210 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=317  W=125/L=192  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_mid (61/192 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L05.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=317  W=125/L=192  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_mid (61/192 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=317  W=125/L=192  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_mid (61/192 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L07.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=297  W=105/L=192  WR=35.4%
- Sharpen: sharpest is session_bucket=ny_mid (61/192 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP4`
- Raw: n=291  W=112/L=179  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (95/179 of losers there)
- **Sharp: n=134  W=39/L=95  WR=29.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=272  W=103/L=169  WR=37.9%
- Sharpen: sharpest is RSI=RSI6 (92/169 of losers there)
- **Sharp: n=127  W=35/L=92  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 70-80 overbought

### L10.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=212  W=81/L=131  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_mid (33/131 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L11.  `H20=H20e AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=211  W=82/L=129  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_mid (33/129 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L12.  `T4=T4c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=202  W=76/L=126  WR=37.6%
- Sharpen: sharpest is session_bucket=ny_mid (33/126 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L13.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=202  W=76/L=126  WR=37.6%
- Sharpen: sharpest is session_bucket=ny_mid (33/126 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L14.  `H20=H20e AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=201  W=77/L=124  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (33/124 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L15.  `H20=H20e AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=201  W=77/L=124  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (33/124 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L16.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=194  W=71/L=123  WR=36.6%
- Sharpen: sharpest is session_bucket=ny_mid (33/123 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L17.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=194  W=71/L=123  WR=36.6%
- Sharpen: sharpest is session_bucket=ny_mid (33/123 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L18.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=191  W=76/L=115  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (33/115 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L19.  `H20=H20e AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=191  W=76/L=115  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (33/115 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L20.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=184  W=66/L=118  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (33/118 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L21.  `T4=T4c AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=184  W=66/L=118  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (33/118 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L22.  `H60=H60e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=180  W=68/L=112  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_mid (33/112 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L23.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=173  W=69/L=104  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_mid (28/104 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L24.  `H60=H60e AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=173  W=69/L=104  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_mid (28/104 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L25.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=172  W=61/L=111  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_mid (28/111 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 70-80 overbought  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(56/35) | H20e(38/57) |
| H60 | H60a(49/25) | H60e(28/48) |
| T1 | T1a(58/41) | T1c(42/59) |
| T4 | T4a(59/40) | T4c(41/60) |
| BBP | — | — |
| RSI | — | RSI6(40/45) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/41) | short(42/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
