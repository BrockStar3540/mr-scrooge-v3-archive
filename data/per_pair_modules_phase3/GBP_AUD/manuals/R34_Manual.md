# GBP_AUD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **5,286**  (W=3,167 / L=2,119)  -  WR: **59.9%**

## Session distribution

- asia: n=1638  W=993/L=645  WR=60.6%
- london_open: n=971  W=592/L=379  WR=61.0%
- ny_mid: n=772  W=463/L=309  WR=60.0%
- london: n=572  W=351/L=221  WR=61.4%
- ny_open: n=458  W=260/L=198  WR=56.8%
- ny_close: n=458  W=265/L=193  WR=57.9%
- asia_late: n=318  W=188/L=130  WR=59.1%
- off_hours: n=99  W=55/L=44  WR=55.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=london drops 6/15 losers (40%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=london

### W02.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H20=H20e drops 11/14 losers (79%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 strongly against

### W03.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude H20=H20e drops 13/16 losers (81%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 strongly against

### W04.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude H20=H20e drops 13/16 losers (81%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 strongly against

### W05.  `H60=H60a AND BBP=BBP6 AND RSI=RSI3`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude T1=T1a drops 15/15 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W06.  `BBP=BBP6 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude T1=T1a drops 15/15 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60a AND BBP=BBP6 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude T1=T1a drops 15/15 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W08.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=london

### W09.  `T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band  •  AVOID when session=london

### W10.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=london

### W11.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND RSI=RSI3`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=81  W=75/L=6  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 40-50 lower neutral  •  AVOID when session=london

### W12.  `T4=T4a AND BBP=BBP6 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=81  W=75/L=6  WR=92.6%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band; RSI 40-50 lower neutral  •  AVOID when session=london

### W13.  `H60=H60a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W15.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W16.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W20.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W22.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W23.  `H20=H20a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4c drops 7/13 losers (54%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W24.  `H60=H60a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W25.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=328  W=126/L=202  WR=38.4%
- Sharpen: sharpest is H20=H20e (121/202 of losers there)
- **Sharp: n=156  W=35/L=121  WR=22.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L02.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=328  W=126/L=202  WR=38.4%
- Sharpen: sharpest is H20=H20e (121/202 of losers there)
- **Sharp: n=156  W=35/L=121  WR=22.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L03.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=316  W=123/L=193  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=316  W=123/L=193  WR=38.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=277  W=103/L=174  WR=37.2%
- Sharpen: sharpest is H20=H20e (113/174 of losers there)
- **Sharp: n=148  W=35/L=113  WR=23.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L05.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=277  W=103/L=174  WR=37.2%
- Sharpen: sharpest is H20=H20e (113/174 of losers there)
- **Sharp: n=148  W=35/L=113  WR=23.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L06.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=249  W=98/L=151  WR=39.4%
- Sharpen: sharpest is T4=T4c (133/151 of losers there)
- **Sharp: n=197  W=64/L=133  WR=32.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=249  W=98/L=151  WR=39.4%
- Sharpen: sharpest is T4=T4c (133/151 of losers there)
- **Sharp: n=197  W=64/L=133  WR=32.5%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20e AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=246  W=87/L=159  WR=35.4%
- Sharpen: sharpest is T4=T4c (121/159 of losers there)
- **Sharp: n=156  W=35/L=121  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=246  W=87/L=159  WR=35.4%
- Sharpen: sharpest is T4=T4c (121/159 of losers there)
- **Sharp: n=156  W=35/L=121  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=223  W=78/L=145  WR=35.0%
- Sharpen: sharpest is H20=H20e (93/145 of losers there)
- **Sharp: n=125  W=32/L=93  WR=25.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L11.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=207  W=64/L=143  WR=30.9%
- Sharpen: sharpest is ZS=ZS4 (121/143 of losers there)
- **Sharp: n=156  W=35/L=121  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when zscore +1 to +2 overbought

### L12.  `H20=H20e AND T4=T4c AND ZS=ZS4`
- Raw: n=204  W=72/L=132  WR=35.3%
- Sharpen: sharpest is RSI=RSI3 (121/132 of losers there)
- **Sharp: n=156  W=35/L=121  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L13.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=204  W=72/L=132  WR=35.3%
- Sharpen: sharpest is RSI=RSI3 (121/132 of losers there)
- **Sharp: n=156  W=35/L=121  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L14.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=196  W=72/L=124  WR=36.7%
- Sharpen: sharpest is RSI=RSI3 (113/124 of losers there)
- **Sharp: n=148  W=35/L=113  WR=23.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L15.  `H20=H20e AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=196  W=72/L=124  WR=36.7%
- Sharpen: sharpest is RSI=RSI3 (113/124 of losers there)
- **Sharp: n=148  W=35/L=113  WR=23.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=195  W=65/L=130  WR=33.3%
- Sharpen: sharpest is T4=T4c (113/130 of losers there)
- **Sharp: n=148  W=35/L=113  WR=23.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=195  W=65/L=130  WR=33.3%
- Sharpen: sharpest is T4=T4c (113/130 of losers there)
- **Sharp: n=148  W=35/L=113  WR=23.6%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=177  W=64/L=113  WR=36.2%
- Sharpen: sharpest is T4=T4c (93/113 of losers there)
- **Sharp: n=125  W=32/L=93  WR=25.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=173  W=69/L=104  WR=39.9%
- Sharpen: sharpest is RSI=RSI3 (93/104 of losers there)
- **Sharp: n=125  W=32/L=93  WR=25.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L20.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=156  W=35/L=121  WR=22.4%
- Sharpen: sharpest is session_bucket=asia (42/121 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L21.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=147  W=50/L=97  WR=34.0%
- Sharpen: sharpest is BBP=BBP6 (51/97 of losers there)
- **Sharp: n=66  W=15/L=51  WR=22.7%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L22.  `H60=H60e AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=144  W=50/L=94  WR=34.7%
- Sharpen: sharpest is BBP=BBP6 (48/94 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L23.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=144  W=50/L=94  WR=34.7%
- Sharpen: sharpest is BBP=BBP6 (48/94 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L24.  `H60=H60e AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=144  W=50/L=94  WR=34.7%
- Sharpen: sharpest is BBP=BBP6 (48/94 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L25.  `H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is H20=H20c (18/86 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
