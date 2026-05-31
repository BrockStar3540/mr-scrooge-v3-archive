# EUR_USD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,567**  (W=1,022 / L=545)  -  WR: **65.2%**

## Session distribution

- asia: n=984  W=649/L=335  WR=66.0%
- ny_close: n=285  W=188/L=97  WR=66.0%
- off_hours: n=128  W=89/L=39  WR=69.5%
- asia_late: n=103  W=66/L=37  WR=64.1%
- ny_open: n=25  W=11/L=14  WR=44.0%
- london_open: n=20  W=7/L=13  WR=35.0%
- london: n=14  W=7/L=7  WR=50.0%
- ny_mid: n=8  W=5/L=3  WR=62.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=153  W=132/L=21  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/21 losers (57%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W02.  `H20=H20e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=142  W=123/L=19  WR=86.6%
- Refine: exclude H60=H60a drops 7/19 losers (37%)
- **Final: n=131  W=119/L=12  WR=90.8%**
- **Dir: ?**  •  HTF20 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when HTF60 aligned WITH trade

### W03.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude BBP=BBP1 drops 12/17 losers (71%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W04.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude ZS=ZS2 drops 10/15 losers (67%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W05.  `H20=H20e AND BBP=BBP0 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=108  W=98/L=10  WR=90.7%
- Refine: exclude H60=H60a drops 5/10 losers (50%)
- **Final: n=101  W=96/L=5  WR=95.0%**
- **Dir: ?**  •  HTF20 strongly against; deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when HTF60 aligned WITH trade

### W06.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=107  W=101/L=6  WR=94.4%
- Refine: exclude ZS=ZS1 drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS2 drops 10/15 losers (67%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W08.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS2 drops 10/15 losers (67%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W09.  `H20=H20e AND T4=T4a AND ZS=ZS1`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude H60=H60b drops 3/14 losers (21%)
- **Final: n=100  W=89/L=11  WR=89.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W10.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude H60=H60a drops 8/15 losers (53%)
- **Final: n=62  W=55/L=7  WR=88.7%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W11.  `H20=H20e AND H60=H60e AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude RSI=RSI3 drops 9/13 losers (69%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band; session=asia  •  AVOID when RSI 40-50 lower neutral

### W12.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H60=H60b drops 3/14 losers (21%)
- **Final: n=94  W=83/L=11  WR=88.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W13.  `H20=H20e AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H60=H60b drops 3/14 losers (21%)
- **Final: n=94  W=83/L=11  WR=88.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W14.  `H20=H20e AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=96  W=87/L=9  WR=90.6%
- Refine: exclude session_bucket=off_hours drops 2/9 losers (22%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=off_hours

### W15.  `T1=T1a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 5/14 losers (36%)
- **Final: n=79  W=70/L=9  WR=88.6%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when strategy=charlie_pullback_continuation_v2

### W16.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude ZS=ZS2 drops 9/11 losers (82%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W17.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI2`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude ZS=ZS2 drops 9/14 losers (64%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W18.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude ZS=ZS2 drops 9/14 losers (64%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W19.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=93  W=87/L=6  WR=93.5%
- Refine: exclude ZS=ZS1 drops 6/6 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H20=H20e AND H60=H60e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=92  W=88/L=4  WR=95.7%
- Refine: exclude strategy_id=BR2_vcb_short drops 2/4 losers (50%)
- **Final: n=82  W=80/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when strategy=BR2_vcb_short

### W21.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 5/13 losers (38%)
- **Final: n=73  W=65/L=8  WR=89.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when strategy=charlie_pullback_continuation_v2

### W22.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 5/13 losers (38%)
- **Final: n=73  W=65/L=8  WR=89.0%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when strategy=charlie_pullback_continuation_v2

### W23.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude H60=H60b drops 3/11 losers (27%)
- **Final: n=86  W=78/L=8  WR=90.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W24.  `T1=T1a AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 5/12 losers (42%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when strategy=charlie_pullback_continuation_v2

### W25.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=86  W=77/L=9  WR=89.5%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=108  W=43/L=65  WR=39.8%
- Sharpen: sharpest is BBP=BBP0 (42/65 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L02.  `H20=H20a AND H60=H60a AND T4=T4c`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (56/64 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L03.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=74  W=18/L=56  WR=24.3%
- Sharpen: sharpest is BBP=BBP0 (25/56 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L04.  `H20=H20a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=71  W=18/L=53  WR=25.4%
- Sharpen: sharpest is H60=H60a (37/53 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L05.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=66  W=17/L=49  WR=25.8%
- Sharpen: sharpest is session_bucket=asia (36/49 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L06.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=66  W=17/L=49  WR=25.8%
- Sharpen: sharpest is session_bucket=asia (36/49 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L07.  `H20=H20a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is T4=T4c (30/42 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60a (19/38 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L09.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=58  W=20/L=38  WR=34.5%
- Sharpen: sharpest is T1=T1c (36/38 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L10.  `T1=T1c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (19/35 of losers there)
- **Sharp: n=26  W=7/L=19  WR=26.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L11.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: sharpest is H20=H20d (7/37 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 mildly against

### L12.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=55  W=14/L=41  WR=25.5%
- Sharpen: sharpest is session_bucket=asia (33/41 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L13.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=55  W=14/L=41  WR=25.5%
- Sharpen: sharpest is session_bucket=asia (33/41 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=asia

### L14.  `H20=H20a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=53  W=11/L=42  WR=20.8%
- Sharpen: sharpest is H60=H60a (27/42 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L15.  `T1=T1c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is H20=H20d (7/34 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 mildly against

### L16.  `T1=T1a AND T4=T4c AND RSI=RSI2`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (11/33 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L17.  `T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (11/33 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L18.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI2`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (11/33 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L19.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (11/33 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L20.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (11/33 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L21.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=51  W=7/L=44  WR=13.7%
- Sharpen: sharpest is H20=H20a (37/44 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L22.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (16/33 of losers there)
- **Sharp: n=21  W=5/L=16  WR=23.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L23.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (16/33 of losers there)
- **Sharp: n=21  W=5/L=16  WR=23.8%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L24.  `H20=H20e AND T1=T1a AND T4=T4c`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is H60=H60e (17/32 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L25.  `H20=H20a AND T4=T4c AND BBP=BBP0`
- Raw: n=50  W=17/L=33  WR=34.0%
- Sharpen: sharpest is H60=H60a (26/33 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(39/45) |
| H60 | — | — |
| T1 | T1a(58/44) | T1c(42/56) |
| T4 | T4a(62/38) | T4c(38/61) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(58/44) | long(42/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
