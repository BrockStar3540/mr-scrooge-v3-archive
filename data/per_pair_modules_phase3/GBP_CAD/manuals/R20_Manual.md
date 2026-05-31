# GBP_CAD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,219**  (W=1,955 / L=1,264)  -  WR: **60.7%**

## Session distribution

- ny_mid: n=982  W=608/L=374  WR=61.9%
- ny_close: n=551  W=345/L=206  WR=62.6%
- london_open: n=539  W=330/L=209  WR=61.2%
- ny_open: n=505  W=295/L=210  WR=58.4%
- london: n=334  W=203/L=131  WR=60.8%
- asia: n=182  W=119/L=63  WR=65.4%
- off_hours: n=93  W=37/L=56  WR=39.8%
- asia_late: n=33  W=18/L=15  WR=54.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=179  W=153/L=26  WR=85.5%
- Refine: exclude H20=H20d drops 15/26 losers (58%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W02.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=145  W=126/L=19  WR=86.9%
- Refine: exclude H60=H60a drops 16/19 losers (84%)
- **Final: n=91  W=88/L=3  WR=96.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W03.  `T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=119  W=111/L=8  WR=93.3%
- Refine: exclude H60=H60e drops 7/8 losers (88%)
- **Final: n=87  W=86/L=1  WR=98.9%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 strongly against

### W04.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude H20=H20d drops 11/16 losers (69%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W05.  `T1=T1c AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W06.  `H20=H20e AND T1=T1c AND ZS=ZS4`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude H60=H60e drops 10/15 losers (67%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W07.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude H60=H60e drops 10/15 losers (67%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W08.  `T1=T1c AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T4=T4c drops 12/13 losers (92%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W09.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T4=T4c drops 12/13 losers (92%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W10.  `H20=H20d AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=90  W=88/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched lower band

### W11.  `T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20b drops 9/14 losers (64%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 slightly aligned

### W12.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20b drops 9/14 losers (64%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W13.  `H20=H20e AND T1=T1c AND RSI=RSI4`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude T4=T4a drops 9/11 losers (82%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude T4=T4a drops 9/11 losers (82%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W15.  `T4=T4c AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude T1=T1a drops 10/14 losers (71%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W16.  `T4=T4c AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude T1=T1a drops 10/14 losers (71%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W17.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude T4=T4c drops 11/11 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W18.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=87  W=80/L=7  WR=92.0%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 strongly against

### W19.  `H20=H20e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI3 drops 6/11 losers (55%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20d AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude H60=H60e drops 10/11 losers (91%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W21.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI3 drops 6/11 losers (55%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W22.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude H20=H20e drops 4/12 losers (33%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W23.  `H20=H20b AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude ZS=ZS3 drops 7/12 losers (58%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20b AND ZS=ZS2 AND direction_exec=short`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude RSI=RSI4 drops 10/12 losers (83%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=176  W=70/L=106  WR=39.8%
- Sharpen: sharpest is H20=H20d (42/106 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when HTF20 mildly against

### L02.  `H20=H20b AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=165  W=62/L=103  WR=37.6%
- Sharpen: sharpest is H60=H60e (83/103 of losers there)
- **Sharp: n=95  W=12/L=83  WR=12.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L03.  `H20=H20b AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is T1=T1c (83/92 of losers there)
- **Sharp: n=95  W=12/L=83  WR=12.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L04.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=141  W=53/L=88  WR=37.6%
- Sharpen: sharpest is H60=H60d (28/88 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  ONLY when HTF60 mildly against

### L05.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is H20=H20a (27/80 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L06.  `T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=132  W=45/L=87  WR=34.1%
- Sharpen: sharpest is H60=H60a (45/87 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L07.  `T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is H20=H20a (36/74 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=38/L=81  WR=31.9%
- Sharpen: sharpest is ZS=ZS2 (52/81 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  ONLY when zscore -2 to -1 oversold

### L09.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_open (51/71 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L10.  `H60=H60e AND T4=T4a AND ZS=ZS4`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_close (26/68 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L11.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_close (26/68 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L12.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=111  W=33/L=78  WR=29.7%
- Sharpen: sharpest is H60=H60a (39/78 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L13.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: sharpest is T1=T1a (65/68 of losers there)
- **Sharp: n=90  W=25/L=65  WR=27.8%**
- **Dir: SHORT**  •  just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L14.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is H20=H20a (36/64 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L15.  `H20=H20c AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is direction_exec=short (37/64 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when short

### L16.  `H20=H20d AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is RSI=RSI3 (48/63 of losers there)
- **Sharp: n=57  W=9/L=48  WR=15.8%**
- **Dir: ?**  •  HTF20 mildly against; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L17.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is H60=H60a (38/62 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L18.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=96  W=32/L=64  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (25/64 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H20=H20b AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=95  W=12/L=83  WR=12.6%
- Sharpen: sharpest is RSI=RSI5 (37/83 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L20.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is H20=H20d (28/57 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 mildly against

### L21.  `H20=H20d AND T1=T1a AND ZS=ZS2`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is RSI=RSI3 (44/57 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L22.  `H20=H20d AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is RSI=RSI3 (44/57 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L23.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=93  W=24/L=69  WR=25.8%
- Sharpen: sharpest is H60=H60e (35/69 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L24.  `T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is ZS=ZS2 (32/59 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore -2 to -1 oversold

### L25.  `H20=H20a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is ZS=ZS4 (31/56 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(52/47) | T4a(48/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
