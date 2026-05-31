# USD_JPY — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,593**  (W=1,570 / L=1,023)  -  WR: **60.5%**

## Session distribution

- ny_open: n=562  W=358/L=204  WR=63.7%
- asia: n=552  W=321/L=231  WR=58.2%
- ny_close: n=390  W=225/L=165  WR=57.7%
- ny_mid: n=386  W=238/L=148  WR=61.7%
- london: n=359  W=222/L=137  WR=61.8%
- london_open: n=305  W=182/L=123  WR=59.7%
- off_hours: n=24  W=14/L=10  WR=58.3%
- asia_late: n=15  W=10/L=5  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=205  W=176/L=29  WR=85.9%
- Refine: exclude H60=H60d drops 17/29 losers (59%)
- **Final: n=165  W=153/L=12  WR=92.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 mildly against

### W02.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=201  W=173/L=28  WR=86.1%
- Refine: exclude H60=H60d drops 17/28 losers (61%)
- **Final: n=161  W=150/L=11  WR=93.2%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF60 mildly against

### W03.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=201  W=173/L=28  WR=86.1%
- Refine: exclude H60=H60d drops 17/28 losers (61%)
- **Final: n=161  W=150/L=11  WR=93.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 mildly against

### W04.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=175  W=157/L=18  WR=89.7%
- Refine: exclude ZS=ZS3 drops 8/18 losers (44%)
- **Final: n=163  W=153/L=10  WR=93.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W05.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=174  W=157/L=17  WR=90.2%
- Refine: exclude ZS=ZS3 drops 8/17 losers (47%)
- **Final: n=162  W=153/L=9  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W06.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=174  W=157/L=17  WR=90.2%
- Refine: exclude ZS=ZS3 drops 8/17 losers (47%)
- **Final: n=162  W=153/L=9  WR=94.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=174  W=150/L=24  WR=86.2%
- Refine: exclude RSI=RSI4 drops 22/24 losers (92%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=170  W=148/L=22  WR=87.1%
- Refine: exclude RSI=RSI4 drops 20/22 losers (91%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=170  W=148/L=22  WR=87.1%
- Refine: exclude RSI=RSI4 drops 20/22 losers (91%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W10.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=161  W=150/L=11  WR=93.2%
- Refine: exclude ZS=ZS3 drops 6/11 losers (55%)
- **Final: n=151  W=146/L=5  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W11.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=161  W=150/L=11  WR=93.2%
- Refine: exclude ZS=ZS3 drops 6/11 losers (55%)
- **Final: n=151  W=146/L=5  WR=96.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W12.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=153  W=140/L=13  WR=91.5%
- Refine: exclude H60=H60d drops 8/13 losers (62%)
- **Final: n=126  W=121/L=5  WR=96.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF60 mildly against

### W13.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=153  W=139/L=14  WR=90.8%
- Refine: exclude H60=H60d drops 8/14 losers (57%)
- **Final: n=126  W=120/L=6  WR=95.2%**
- **Dir: LONG**  •  upper third; session=ny_open  •  AVOID when HTF60 mildly against

### W14.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=152  W=139/L=13  WR=91.4%
- Refine: exclude H60=H60d drops 8/13 losers (62%)
- **Final: n=125  W=120/L=5  WR=96.0%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF60 mildly against

### W15.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=145  W=133/L=12  WR=91.7%
- Refine: exclude H60=H60d drops 8/12 losers (67%)
- **Final: n=124  W=120/L=4  WR=96.8%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 mildly against

### W16.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=145  W=133/L=12  WR=91.7%
- Refine: exclude H60=H60d drops 8/12 losers (67%)
- **Final: n=124  W=120/L=4  WR=96.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 mildly against

### W17.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude H60=H60d drops 8/13 losers (62%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 mildly against

### W18.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude H60=H60d drops 8/13 losers (62%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 mildly against

### W19.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=144  W=132/L=12  WR=91.7%
- Refine: exclude H60=H60d drops 8/12 losers (67%)
- **Final: n=123  W=119/L=4  WR=96.7%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 mildly against

### W20.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=138  W=126/L=12  WR=91.3%
- Refine: exclude H60=H60d drops 8/12 losers (67%)
- **Final: n=111  W=107/L=4  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF60 mildly against

### W21.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=137  W=125/L=12  WR=91.2%
- Refine: exclude H60=H60d drops 8/12 losers (67%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF60 mildly against

### W22.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=130  W=119/L=11  WR=91.5%
- Refine: exclude H60=H60d drops 8/11 losers (73%)
- **Final: n=109  W=106/L=3  WR=97.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 mildly against

### W23.  `T4=T4a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=129  W=118/L=11  WR=91.5%
- Refine: exclude H60=H60d drops 8/11 losers (73%)
- **Final: n=108  W=105/L=3  WR=97.2%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 mildly against

### W24.  `H20=H20a AND H60=H60a AND RSI=RSI6`
- Raw: n=128  W=112/L=16  WR=87.5%
- Refine: exclude session_bucket=london drops 10/16 losers (62%)
- **Final: n=113  W=107/L=6  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when session=london

### W25.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=128  W=112/L=16  WR=87.5%
- Refine: exclude session_bucket=london drops 10/16 losers (62%)
- **Final: n=113  W=107/L=6  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=270  W=91/L=179  WR=33.7%
- Sharpen: sharpest is session_bucket=ny_close (30/179 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L02.  `H20=H20a AND T1=T1c AND ZS=ZS5`
- Raw: n=197  W=59/L=138  WR=29.9%
- Sharpen: sharpest is BBP=BBP6 (60/138 of losers there)
- **Sharp: n=66  W=6/L=60  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L03.  `H20=H20a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=194  W=59/L=135  WR=30.4%
- Sharpen: sharpest is BBP=BBP6 (60/135 of losers there)
- **Sharp: n=66  W=6/L=60  WR=9.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L04.  `H20=H20a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=194  W=59/L=135  WR=30.4%
- Sharpen: sharpest is BBP=BBP6 (60/135 of losers there)
- **Sharp: n=66  W=6/L=60  WR=9.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L05.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=181  W=69/L=112  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=181  W=69/L=112  WR=38.1%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought

### L06.  `T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=178  W=69/L=109  WR=38.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band

### L07.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=178  W=69/L=109  WR=38.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought

### L08.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=165  W=63/L=102  WR=38.2%
- Sharpen: sharpest is T1=T1c (88/102 of losers there)
- **Sharp: n=119  W=31/L=88  WR=26.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L09.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=163  W=56/L=107  WR=34.4%
- Sharpen: sharpest is BBP=BBP6 (41/107 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L10.  `T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=157  W=50/L=107  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (41/107 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L11.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=157  W=50/L=107  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (41/107 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L12.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=157  W=50/L=107  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (41/107 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L13.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=157  W=50/L=107  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (41/107 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L14.  `H20=H20a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=48/L=98  WR=32.9%
- Sharpen: sharpest is BBP=BBP4 (43/98 of losers there)
- **Sharp: n=50  W=7/L=43  WR=14.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_open  •  ONLY when upper third

### L15.  `H20=H20a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=143  W=46/L=97  WR=32.2%
- Sharpen: sharpest is BBP=BBP4 (43/97 of losers there)
- **Sharp: n=50  W=7/L=43  WR=14.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L16.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=143  W=46/L=97  WR=32.2%
- Sharpen: sharpest is BBP=BBP4 (43/97 of losers there)
- **Sharp: n=50  W=7/L=43  WR=14.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L17.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=131  W=36/L=95  WR=27.5%
- Sharpen: sharpest is ZS=ZS4 (64/95 of losers there)
- **Sharp: n=79  W=15/L=64  WR=19.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L18.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=130  W=35/L=95  WR=26.9%
- Sharpen: sharpest is ZS=ZS4 (64/95 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L19.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=130  W=35/L=95  WR=26.9%
- Sharpen: sharpest is ZS=ZS4 (64/95 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L20.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is H60=H60e (65/75 of losers there)
- **Sharp: n=86  W=21/L=65  WR=24.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF60 strongly against

### L21.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=124  W=39/L=85  WR=31.5%
- Sharpen: sharpest is H60=H60e (64/85 of losers there)
- **Sharp: n=80  W=16/L=64  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF60 strongly against

### L22.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=124  W=40/L=84  WR=32.3%
- Sharpen: sharpest is H60=H60e (64/84 of losers there)
- **Sharp: n=81  W=17/L=64  WR=21.0%**
- **Dir: SHORT**  •  upper third; session=ny_open  •  ONLY when HTF60 strongly against

### L23.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=123  W=39/L=84  WR=31.7%
- Sharpen: sharpest is H60=H60e (64/84 of losers there)
- **Sharp: n=80  W=16/L=64  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF60 strongly against

### L24.  `H60=H60d AND T4=T4a AND RSI=RSI5`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (31/73 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L25.  `H20=H20a AND H60=H60d AND T4=T4a AND RSI=RSI5`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (31/73 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(52/45) | H20a(45/51) |
| H60 | H60a(40/35) | H60e(34/42) |
| T1 | T1a(58/40) | T1c(42/60) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(60/40) | short(40/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
