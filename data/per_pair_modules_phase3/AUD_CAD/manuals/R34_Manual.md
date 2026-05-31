# AUD_CAD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,177**  (W=2,005 / L=1,172)  -  WR: **63.1%**

## Session distribution

- asia: n=1055  W=677/L=378  WR=64.2%
- ny_close: n=555  W=352/L=203  WR=63.4%
- london_open: n=519  W=322/L=197  WR=62.0%
- london: n=366  W=235/L=131  WR=64.2%
- ny_open: n=252  W=152/L=100  WR=60.3%
- ny_mid: n=172  W=103/L=69  WR=59.9%
- asia_late: n=136  W=87/L=49  WR=64.0%
- off_hours: n=122  W=77/L=45  WR=63.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=214  W=187/L=27  WR=87.4%
- Refine: exclude RSI=RSI4 drops 21/27 losers (78%)
- **Final: n=138  W=132/L=6  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W02.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=214  W=187/L=27  WR=87.4%
- Refine: exclude RSI=RSI4 drops 21/27 losers (78%)
- **Final: n=138  W=132/L=6  WR=95.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W03.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude RSI=RSI3 drops 17/22 losers (77%)
- **Final: n=118  W=113/L=5  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W04.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude RSI=RSI3 drops 17/22 losers (77%)
- **Final: n=118  W=113/L=5  WR=95.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=146  W=127/L=19  WR=87.0%
- Refine: exclude session_bucket=ny_close drops 11/19 losers (58%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W06.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=146  W=127/L=19  WR=87.0%
- Refine: exclude session_bucket=ny_close drops 11/19 losers (58%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W07.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=131  W=114/L=17  WR=87.0%
- Refine: exclude BBP=BBP2 drops 11/17 losers (65%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W08.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=131  W=114/L=17  WR=87.0%
- Refine: exclude BBP=BBP2 drops 11/17 losers (65%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W09.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=131  W=114/L=17  WR=87.0%
- Refine: exclude BBP=BBP2 drops 11/17 losers (65%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W10.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude T4=T4c drops 7/13 losers (54%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W11.  `T1=T1c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude T4=T4c drops 7/13 losers (54%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W12.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H60=H60e drops 13/17 losers (76%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W13.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H60=H60e drops 13/17 losers (76%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W14.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=116  W=108/L=8  WR=93.1%
- Refine: exclude BBP=BBP2 drops 7/8 losers (88%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W15.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=109  W=99/L=10  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 6/10 losers (60%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W16.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=109  W=99/L=10  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 6/10 losers (60%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W17.  `T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=102  W=91/L=11  WR=89.2%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W18.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude session_bucket=off_hours drops 9/14 losers (64%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W19.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude ZS=ZS1 drops 7/15 losers (47%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude ZS=ZS1 drops 7/15 losers (47%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude session_bucket=london drops 4/10 losers (40%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W22.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=92  W=84/L=8  WR=91.3%
- Refine: exclude RSI=RSI4 drops 7/8 losers (88%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=84/L=8  WR=91.3%
- Refine: exclude RSI=RSI4 drops 7/8 losers (88%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=89  W=83/L=6  WR=93.3%
- Refine: exclude session_bucket=london drops 4/6 losers (67%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W25.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=88  W=83/L=5  WR=94.3%
- Refine: exclude session_bucket=london drops 2/5 losers (40%)
- **Final: n=86  W=83/L=3  WR=96.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (64/141 of losers there)
- **Sharp: n=84  W=20/L=64  WR=23.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L02.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (64/141 of losers there)
- **Sharp: n=84  W=20/L=64  WR=23.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L03.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (64/141 of losers there)
- **Sharp: n=84  W=20/L=64  WR=23.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L04.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: sharpest is RSI=RSI5 (37/105 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=162  W=63/L=99  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (33/99 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (35/96 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L07.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=157  W=45/L=112  WR=28.7%
- Sharpen: sharpest is H20=H20a (55/112 of losers there)
- **Sharp: n=66  W=11/L=55  WR=16.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=157  W=45/L=112  WR=28.7%
- Sharpen: sharpest is H20=H20a (55/112 of losers there)
- **Sharp: n=66  W=11/L=55  WR=16.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L09.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=145  W=55/L=90  WR=37.9%
- Sharpen: sharpest is H60=H60a (43/90 of losers there)
- **Sharp: n=57  W=14/L=43  WR=24.6%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L10.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=144  W=54/L=90  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (37/90 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L11.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=144  W=54/L=90  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (37/90 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L12.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=144  W=54/L=90  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (37/90 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=143  W=53/L=90  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (37/90 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=143  W=53/L=90  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (37/90 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is T1=T1a (62/90 of losers there)
- **Sharp: n=76  W=14/L=62  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend WITH trade

### L16.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is T1=T1a (62/90 of losers there)
- **Sharp: n=76  W=14/L=62  WR=18.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend WITH trade

### L17.  `H60=H60a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is T1=T1a (45/73 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L18.  `BBP=BBP1 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is T1=T1a (45/73 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L19.  `H60=H60a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is T1=T1a (45/73 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L20.  `H60=H60a AND BBP=BBP1 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is T1=T1a (45/73 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L21.  `BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is T1=T1a (45/73 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L22.  `T1=T1a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is session_bucket=ny_open (13/69 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_open

### L23.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is RSI=RSI5 (37/69 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L24.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: sharpest is BBP=BBP1 (23/65 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when just touched lower band

### L25.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: sharpest is BBP=BBP1 (23/65 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when just touched lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(54/45) | H60a(46/55) |
| T1 | — | — |
| T4 | T4a(56/44) | T4c(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/45) | long(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
