# USD_JPY — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,621**  (W=1,622 / L=999)  -  WR: **61.9%**

## Session distribution

- asia: n=878  W=544/L=334  WR=62.0%
- ny_close: n=443  W=277/L=166  WR=62.5%
- london_open: n=370  W=226/L=144  WR=61.1%
- ny_mid: n=340  W=203/L=137  WR=59.7%
- ny_open: n=280  W=170/L=110  WR=60.7%
- london: n=209  W=133/L=76  WR=63.6%
- off_hours: n=65  W=43/L=22  WR=66.2%
- asia_late: n=36  W=26/L=10  WR=72.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=140  W=123/L=17  WR=87.9%
- Refine: exclude H20=H20a drops 13/17 losers (76%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude session_bucket=ny_close drops 9/17 losers (53%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W03.  `T4=T4a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H20=H20a drops 13/17 losers (76%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W05.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude session_bucket=ny_close drops 6/11 losers (55%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W06.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude session_bucket=ny_close drops 6/11 losers (55%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W07.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude H20=H20a drops 7/9 losers (78%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W08.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W09.  `T4=T4a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude session_bucket=london drops 3/10 losers (30%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=london

### W10.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude H20=H20a drops 7/9 losers (78%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H20=H20e drops 12/13 losers (92%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W12.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W13.  `T4=T4a AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude H60=H60b drops 6/11 losers (55%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W14.  `T4=T4a AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=london drops 3/9 losers (33%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london

### W15.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude session_bucket=london drops 3/11 losers (27%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=london

### W16.  `T1=T1a AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 6/11 losers (55%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W17.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20a drops 7/9 losers (78%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W18.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W19.  `H20=H20c AND T4=T4a AND RSI=RSI3`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude T1=T1c drops 10/11 losers (91%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

### W20.  `H60=H60a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W22.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W24.  `H60=H60a AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=69  W=66/L=3  WR=95.7%
- Refine: exclude session_bucket=ny_open drops 2/3 losers (67%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W25.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 9/10 losers (90%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=159  W=58/L=101  WR=36.5%
- Sharpen: sharpest is H20=H20b (34/101 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

### L02.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=159  W=58/L=101  WR=36.5%
- Sharpen: sharpest is H20=H20b (34/101 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

### L03.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=103  W=34/L=69  WR=33.0%
- Sharpen: sharpest is ZS=ZS1 (32/69 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=96  W=27/L=69  WR=28.1%
- Sharpen: sharpest is H60=H60e (61/69 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L05.  `H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=95  W=26/L=69  WR=27.4%
- Sharpen: sharpest is T1=T1c (45/69 of losers there)
- **Sharp: n=48  W=3/L=45  WR=6.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

### L06.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=95  W=26/L=69  WR=27.4%
- Sharpen: sharpest is T1=T1c (45/69 of losers there)
- **Sharp: n=48  W=3/L=45  WR=6.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

### L07.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (38/58 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L08.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (38/58 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L09.  `T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is H20=H20d (15/57 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 mildly against

### L10.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H20=H20e (18/58 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L11.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (24/58 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L12.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is H20=H20d (17/62 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L13.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is T4=T4c (42/57 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (17/57 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when upper third

### L15.  `T1=T1a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is H20=H20d (17/55 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 mildly against

### L16.  `H60=H60e AND T1=T1c AND ZS=ZS2`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (36/54 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

### L17.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (36/54 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS3`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is BBP=BBP4 (15/52 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when upper third

### L19.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is T4=T4c (24/52 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L20.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is ZS=ZS1 (31/54 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `T4=T4c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=84  W=27/L=57  WR=32.1%
- Sharpen: sharpest is H60=H60e (50/57 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L22.  `H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is RSI=RSI3 (32/51 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L23.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is RSI=RSI3 (32/51 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L24.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=81  W=26/L=55  WR=32.1%
- Sharpen: sharpest is H20=H20d (17/55 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L25.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is RSI=RSI4 (36/51 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(46/39) | H60a(39/46) |
| T1 | — | — |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/45) | long(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
