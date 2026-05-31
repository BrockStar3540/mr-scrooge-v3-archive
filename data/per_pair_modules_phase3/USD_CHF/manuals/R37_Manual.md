# USD_CHF — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,220**  (W=1,414 / L=806)  -  WR: **63.7%**

## Session distribution

- ny_mid: n=537  W=352/L=185  WR=65.5%
- ny_open: n=413  W=256/L=157  WR=62.0%
- asia: n=411  W=277/L=134  WR=67.4%
- london_open: n=385  W=240/L=145  WR=62.3%
- ny_close: n=213  W=132/L=81  WR=62.0%
- london: n=137  W=91/L=46  WR=66.4%
- off_hours: n=69  W=37/L=32  WR=53.6%
- asia_late: n=55  W=29/L=26  WR=52.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=151  W=132/L=19  WR=87.4%
- Refine: exclude H20=H20d drops 10/19 losers (53%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF20 mildly against

### W02.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=149  W=130/L=19  WR=87.2%
- Refine: exclude ZS=ZS4 drops 11/19 losers (58%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W03.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=137  W=122/L=15  WR=89.1%
- Refine: exclude BBP=BBP5 drops 6/15 losers (40%)
- **Final: n=125  W=116/L=9  WR=92.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when just touched upper band

### W04.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude ZS=ZS4 drops 11/19 losers (58%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W05.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=135  W=117/L=18  WR=86.7%
- Refine: exclude session_bucket=asia drops 7/18 losers (39%)
- **Final: n=115  W=104/L=11  WR=90.4%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

### W06.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=125  W=110/L=15  WR=88.0%
- Refine: exclude BBP=BBP5 drops 6/15 losers (40%)
- **Final: n=113  W=104/L=9  WR=92.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when just touched upper band

### W07.  `T4=T4c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude session_bucket=asia drops 7/16 losers (44%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

### W08.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude BBP=BBP2 drops 6/15 losers (40%)
- **Final: n=88  W=79/L=9  WR=89.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when lower third

### W09.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak  •  AVOID when HTF60 strongly against

### W10.  `BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude session_bucket=asia drops 6/11 losers (55%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: LONG**  •  middle of band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W11.  `BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude session_bucket=asia drops 6/11 losers (55%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: LONG**  •  middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

### W12.  `T4=T4a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude T1=T1c drops 4/10 losers (40%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W13.  `T1=T1a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude H60=H60e drops 10/12 losers (83%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF60 strongly against

### W14.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude BBP=BBP2 drops 5/13 losers (38%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when lower third

### W15.  `T4=T4a AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF20 aligned WITH trade

### W16.  `T1=T1a AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude H60=H60e drops 6/8 losers (75%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF60 strongly against

### W17.  `RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W18.  `BBP=BBP4 AND RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W19.  `T4=T4a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude H60=H60e drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W20.  `T4=T4a AND BBP=BBP4 AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude H60=H60e drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W21.  `T1=T1a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude H60=H60e drops 10/12 losers (83%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W22.  `T1=T1a AND BBP=BBP4 AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude H60=H60e drops 10/12 losers (83%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W23.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP5 drops 3/10 losers (30%)
- **Final: n=77  W=70/L=7  WR=90.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when just touched upper band

### W24.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF20 aligned WITH trade

### W25.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=22  W=21/L=1  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (24/86 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L02.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=105  W=35/L=70  WR=33.3%
- Sharpen: sharpest is H20=H20a (38/70 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L03.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=103  W=33/L=70  WR=32.0%
- Sharpen: sharpest is H20=H20a (38/70 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L04.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is H20=H20a (32/64 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L05.  `T1=T1c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H20=H20e (31/57 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L06.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H20=H20e (31/57 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L07.  `T1=T1c AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H20=H20e (31/57 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L08.  `T4=T4c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is H20=H20e (31/56 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L09.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=91  W=25/L=66  WR=27.5%
- Sharpen: sharpest is H20=H20a (38/66 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is H20=H20e (31/56 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L11.  `T4=T4c AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is H20=H20e (31/56 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L12.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=87  W=26/L=61  WR=29.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/61 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L13.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=85  W=25/L=60  WR=29.4%
- Sharpen: sharpest is H20=H20a (32/60 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L14.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is RSI=RSI3 (38/50 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L15.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is RSI=RSI3 (38/50 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L16.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is RSI=RSI3 (38/50 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L17.  `T4=T4a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is session_bucket=ny_mid (21/52 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L18.  `H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=72  W=24/L=48  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (10/48 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=72  W=24/L=48  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (10/48 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is H60=H60c (19/44 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when HTF60 neutral

### L21.  `T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=69  W=22/L=47  WR=31.9%
- Sharpen: sharpest is H60=H60e (30/47 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L22.  `T1=T1c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is H60=H60e (24/45 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L23.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=68  W=20/L=48  WR=29.4%
- Sharpen: sharpest is H60=H60e (28/48 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: LONG**  •  upper third; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L24.  `BBP=BBP3 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=63  W=16/L=47  WR=25.4%
- Sharpen: sharpest is session_bucket=ny_mid (18/47 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: SHORT**  •  middle of band; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L25.  `BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=63  W=16/L=47  WR=25.4%
- Sharpen: sharpest is session_bucket=ny_mid (18/47 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: SHORT**  •  middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
