# GBP_NZD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,034**  (W=3,018 / L=2,016)  -  WR: **60.0%**

## Session distribution

- asia: n=2218  W=1386/L=832  WR=62.5%
- ny_close: n=1530  W=915/L=615  WR=59.8%
- off_hours: n=608  W=296/L=312  WR=48.7%
- asia_late: n=256  W=158/L=98  WR=61.7%
- london: n=140  W=81/L=59  WR=57.9%
- london_open: n=103  W=66/L=37  WR=64.1%
- ny_open: n=96  W=63/L=33  WR=65.6%
- ny_mid: n=83  W=53/L=30  WR=63.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude H60=H60a drops 17/24 losers (71%)
- **Final: n=97  W=90/L=7  WR=92.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W02.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=153  W=134/L=19  WR=87.6%
- Refine: exclude H60=H60a drops 16/19 losers (84%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W03.  `T4=T4c AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=150  W=131/L=19  WR=87.3%
- Refine: exclude T1=T1a drops 17/19 losers (89%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when 1h trend WITH trade

### W04.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude T1=T1a drops 17/20 losers (85%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when 1h trend WITH trade

### W05.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=136  W=117/L=19  WR=86.0%
- Refine: exclude BBP=BBP6 drops 9/19 losers (47%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when deep above upper band

### W06.  `H20=H20d AND RSI=RSI4 AND direction_exec=long`
- Raw: n=133  W=126/L=7  WR=94.7%
- Refine: exclude BBP=BBP5 drops 3/7 losers (43%)
- **Final: n=117  W=113/L=4  WR=96.6%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 50-60 upper neutral  •  AVOID when just touched upper band

### W07.  `H60=H60a AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude RSI=RSI4 drops 11/16 losers (69%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20e AND H60=H60a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: no further refinement
- **Final: n=130  W=111/L=19  WR=85.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia

### W09.  `H20=H20d AND T1=T1a AND RSI=RSI4`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude direction_exec=short drops 11/16 losers (69%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when short

### W10.  `H20=H20d AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude RSI=RSI5 drops 11/16 losers (69%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; session=ny_close  •  AVOID when RSI 60-70 strong

### W11.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude H60=H60d drops 6/15 losers (40%)
- **Final: n=106  W=97/L=9  WR=91.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 mildly against

### W12.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude ZS=ZS5 drops 5/15 losers (33%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W13.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude H20=H20b drops 9/14 losers (64%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W14.  `H20=H20d AND H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude RSI=RSI5 drops 11/15 losers (73%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when RSI 60-70 strong

### W15.  `H20=H20d AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI5 drops 10/14 losers (71%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade; session=ny_close  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20d AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude direction_exec=short drops 10/14 losers (71%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 mildly against; upper third; RSI 50-60 upper neutral  •  AVOID when short

### W17.  `T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude H20=H20b drops 12/15 losers (80%)
- **Final: n=94  W=91/L=3  WR=96.8%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W18.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude H20=H20b drops 9/14 losers (64%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W19.  `H20=H20d AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=101  W=96/L=5  WR=95.0%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when just touched upper band

### W20.  `H20=H20d AND H60=H60a AND RSI=RSI4`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude BBP=BBP5 drops 3/7 losers (43%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when just touched upper band

### W21.  `H20=H20d AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=99  W=94/L=5  WR=94.9%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when just touched upper band

### W22.  `H20=H20d AND H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=98  W=91/L=7  WR=92.9%
- Refine: exclude BBP=BBP5 drops 3/7 losers (43%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when just touched upper band

### W23.  `H20=H20d AND H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude RSI=RSI5 drops 10/14 losers (71%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when RSI 60-70 strong

### W24.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI2`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude T4=T4c drops 7/12 losers (58%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

### W25.  `H20=H20a AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude T4=T4c drops 7/12 losers (58%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=319  W=127/L=192  WR=39.8%
- Sharpen: sharpest is BBP=BBP4 (88/192 of losers there)
- **Sharp: n=106  W=18/L=88  WR=17.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when upper third

### L02.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=226  W=76/L=150  WR=33.6%
- Sharpen: sharpest is H20=H20b (60/150 of losers there)
- **Sharp: n=65  W=5/L=60  WR=7.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 slightly aligned

### L03.  `H20=H20e AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=220  W=85/L=135  WR=38.6%
- Sharpen: sharpest is T1=T1c (88/135 of losers there)
- **Sharp: n=106  W=18/L=88  WR=17.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when 1h trend AGAINST trade

### L04.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=215  W=69/L=146  WR=32.1%
- Sharpen: sharpest is T1=T1c (99/146 of losers there)
- **Sharp: n=126  W=27/L=99  WR=21.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L05.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=202  W=74/L=128  WR=36.6%
- Sharpen: sharpest is session_bucket=ny_close (62/128 of losers there)
- **Sharp: n=77  W=15/L=62  WR=19.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L06.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=197  W=77/L=120  WR=39.1%
- Sharpen: sharpest is H60=H60e (38/120 of losers there)
- **Sharp: n=43  W=5/L=38  WR=11.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L07.  `T4=T4c AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=193  W=64/L=129  WR=33.2%
- Sharpen: sharpest is RSI=RSI5 (45/129 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 60-70 strong

### L08.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=193  W=64/L=129  WR=33.2%
- Sharpen: sharpest is RSI=RSI5 (45/129 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 60-70 strong

### L09.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=192  W=70/L=122  WR=36.5%
- Sharpen: sharpest is H60=H60a (103/122 of losers there)
- **Sharp: n=141  W=38/L=103  WR=27.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=190  W=74/L=116  WR=38.9%
- Sharpen: sharpest is T4=T4c (104/116 of losers there)
- **Sharp: n=150  W=46/L=104  WR=30.7%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=190  W=74/L=116  WR=38.9%
- Sharpen: sharpest is T4=T4c (104/116 of losers there)
- **Sharp: n=150  W=46/L=104  WR=30.7%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=184  W=69/L=115  WR=37.5%
- Sharpen: sharpest is T1=T1c (74/115 of losers there)
- **Sharp: n=84  W=10/L=74  WR=11.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L13.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=179  W=58/L=121  WR=32.4%
- Sharpen: sharpest is H60=H60e (62/121 of losers there)
- **Sharp: n=77  W=15/L=62  WR=19.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L14.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=177  W=66/L=111  WR=37.3%
- Sharpen: sharpest is session_bucket=off_hours (40/111 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=off_hours

### L15.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=170  W=57/L=113  WR=33.5%
- Sharpen: sharpest is T4=T4c (103/113 of losers there)
- **Sharp: n=141  W=38/L=103  WR=27.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20e AND H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=170  W=63/L=107  WR=37.1%
- Sharpen: sharpest is T4=T4c (88/107 of losers there)
- **Sharp: n=106  W=18/L=88  WR=17.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: sharpest is ZS=ZS4 (43/101 of losers there)
- **Sharp: n=56  W=13/L=43  WR=23.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L18.  `H20=H20b AND T4=T4c AND session_bucket=ny_close`
- Raw: n=166  W=52/L=114  WR=31.3%
- Sharpen: sharpest is direction_exec=short (63/114 of losers there)
- **Sharp: n=68  W=5/L=63  WR=7.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=ny_close  •  ONLY when short

### L19.  `H20=H20b AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=166  W=59/L=107  WR=35.5%
- Sharpen: sharpest is H60=H60e (53/107 of losers there)
- **Sharp: n=64  W=11/L=53  WR=17.2%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L20.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=163  W=52/L=111  WR=31.9%
- Sharpen: sharpest is T1=T1a (28/111 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend WITH trade

### L21.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=160  W=62/L=98  WR=38.8%
- Sharpen: sharpest is H60=H60e (62/98 of losers there)
- **Sharp: n=91  W=29/L=62  WR=31.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L22.  `H20=H20b AND T1=T1c AND direction_exec=short`
- Raw: n=159  W=56/L=103  WR=35.2%
- Sharpen: sharpest is session_bucket=ny_close (70/103 of losers there)
- **Sharp: n=77  W=7/L=70  WR=9.1%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L23.  `T1=T1c AND T4=T4a AND session_bucket=off_hours`
- Raw: n=157  W=57/L=100  WR=36.3%
- Sharpen: sharpest is H20=H20a (53/100 of losers there)
- **Sharp: n=69  W=16/L=53  WR=23.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 aligned WITH trade

### L24.  `H20=H20b AND T4=T4c AND RSI=RSI4`
- Raw: n=152  W=56/L=96  WR=36.8%
- Sharpen: sharpest is direction_exec=short (58/96 of losers there)
- **Sharp: n=62  W=4/L=58  WR=6.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when short

### L25.  `T1=T1c AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=151  W=54/L=97  WR=35.8%
- Sharpen: sharpest is H60=H60c (32/97 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=off_hours  •  ONLY when HTF60 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(16/10) | H20b(10/16) |
| H60 | — | — |
| T1 | T1a(55/47) | T1c(45/53) |
| T4 | T4a(52/47) | T4c(48/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/43) | short(43/57) |
| session_bucket | — | off_hours(10/15) |

*Read: `bucket(winner%/loser%)`.*
