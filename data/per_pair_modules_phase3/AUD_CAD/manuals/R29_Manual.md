# AUD_CAD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,192**  (W=1,405 / L=787)  -  WR: **64.1%**

## Session distribution

- ny_mid: n=656  W=427/L=229  WR=65.1%
- asia: n=529  W=341/L=188  WR=64.5%
- london_open: n=309  W=202/L=107  WR=65.4%
- ny_close: n=295  W=185/L=110  WR=62.7%
- ny_open: n=212  W=134/L=78  WR=63.2%
- london: n=134  W=82/L=52  WR=61.2%
- asia_late: n=54  W=31/L=23  WR=57.4%
- off_hours: n=3  W=3/L=0  WR=100.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=219  W=191/L=28  WR=87.2%
- Refine: exclude H60=H60e drops 28/28 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W02.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=210  W=182/L=28  WR=86.7%
- Refine: exclude H60=H60e drops 28/28 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W03.  `T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=205  W=175/L=30  WR=85.4%
- Refine: exclude H20=H20a drops 9/30 losers (30%)
- **Final: n=173  W=152/L=21  WR=87.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W04.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=202  W=174/L=28  WR=86.1%
- Refine: exclude H60=H60e drops 28/28 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W05.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=173  W=152/L=21  WR=87.9%
- Refine: exclude H60=H60e drops 21/21 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W06.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=165  W=144/L=21  WR=87.3%
- Refine: exclude H60=H60e drops 21/21 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W07.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=141  W=120/L=21  WR=85.1%
- Refine: exclude BBP=BBP1 drops 10/21 losers (48%)
- **Final: n=101  W=90/L=11  WR=89.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when just touched lower band

### W08.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=135  W=118/L=17  WR=87.4%
- Refine: exclude ZS=ZS1 drops 12/17 losers (71%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=135  W=118/L=17  WR=87.4%
- Refine: exclude ZS=ZS1 drops 12/17 losers (71%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W10.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=127  W=110/L=17  WR=86.6%
- Refine: exclude ZS=ZS1 drops 12/17 losers (71%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W11.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude ZS=ZS1 drops 12/17 losers (71%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W12.  `H60=H60e AND T1=T1a AND ZS=ZS4`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W13.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia

### W14.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W15.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W16.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI4 drops 10/11 losers (91%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W17.  `T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when zscore <-3 extreme

### W18.  `H20=H20e AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF60 strongly against

### W19.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF60 strongly against

### W20.  `T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W21.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W22.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude session_bucket=london drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=london

### W23.  `T1=T1a AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20d drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W24.  `T4=T4c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude session_bucket=london drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=london

### W25.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=160  W=48/L=112  WR=30.0%
- Sharpen: sharpest is RSI=RSI3 (74/112 of losers there)
- **Sharp: n=95  W=21/L=74  WR=22.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L02.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=159  W=49/L=110  WR=30.8%
- Sharpen: sharpest is RSI=RSI3 (69/110 of losers there)
- **Sharp: n=90  W=21/L=69  WR=23.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L03.  `T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=152  W=48/L=104  WR=31.6%
- Sharpen: sharpest is RSI=RSI3 (72/104 of losers there)
- **Sharp: n=93  W=21/L=72  WR=22.6%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L04.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=149  W=48/L=101  WR=32.2%
- Sharpen: sharpest is RSI=RSI3 (69/101 of losers there)
- **Sharp: n=90  W=21/L=69  WR=23.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L05.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=136  W=42/L=94  WR=30.9%
- Sharpen: sharpest is RSI=RSI3 (72/94 of losers there)
- **Sharp: n=93  W=21/L=72  WR=22.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L06.  `H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=136  W=48/L=88  WR=35.3%
- Sharpen: sharpest is RSI=RSI3 (67/88 of losers there)
- **Sharp: n=88  W=21/L=67  WR=23.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L07.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=134  W=48/L=86  WR=35.8%
- Sharpen: sharpest is RSI=RSI3 (65/86 of losers there)
- **Sharp: n=86  W=21/L=65  WR=24.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L08.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=133  W=42/L=91  WR=31.6%
- Sharpen: sharpest is RSI=RSI3 (69/91 of losers there)
- **Sharp: n=90  W=21/L=69  WR=23.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=131  W=48/L=83  WR=36.6%
- Sharpen: sharpest is RSI=RSI3 (62/83 of losers there)
- **Sharp: n=83  W=21/L=62  WR=25.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L10.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=120  W=42/L=78  WR=35.0%
- Sharpen: sharpest is RSI=RSI3 (67/78 of losers there)
- **Sharp: n=88  W=21/L=67  WR=23.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L11.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=101  W=35/L=66  WR=34.7%
- Sharpen: sharpest is BBP=BBP0 (24/66 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L12.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=95  W=21/L=74  WR=22.1%
- Sharpen: sharpest is BBP=BBP2 (28/74 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when lower third

### L13.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=93  W=21/L=72  WR=22.6%
- Sharpen: sharpest is ZS=ZS3 (20/72 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L14.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=90  W=21/L=69  WR=23.3%
- Sharpen: sharpest is ZS=ZS3 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L15.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=88  W=21/L=67  WR=23.9%
- Sharpen: sharpest is ZS=ZS3 (18/67 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L16.  `H20=H20a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T4=T4a (40/45 of losers there)
- **Sharp: n=52  W=12/L=40  WR=23.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L18.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L19.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L20.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L21.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L22.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L23.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L24.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20d (12/41 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L25.  `H20=H20a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is RSI=RSI3 (24/38 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(59/41) | T4a(41/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
