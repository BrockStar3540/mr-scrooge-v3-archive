# GBP_CAD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,239**  (W=1,321 / L=918)  -  WR: **59.0%**

## Session distribution

- ny_mid: n=1028  W=590/L=438  WR=57.4%
- ny_open: n=415  W=239/L=176  WR=57.6%
- london_open: n=412  W=261/L=151  WR=63.3%
- london: n=150  W=89/L=61  WR=59.3%
- asia: n=108  W=63/L=45  WR=58.3%
- ny_close: n=76  W=51/L=25  WR=67.1%
- off_hours: n=50  W=28/L=22  WR=56.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=128  W=109/L=19  WR=85.2%
- Refine: exclude H60=H60e drops 18/19 losers (95%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  AVOID when HTF60 strongly against

### W02.  `H20=H20e AND T4=T4c AND ZS=ZS2`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI2 drops 13/16 losers (81%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 30-40 weak

### W03.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI2 drops 13/16 losers (81%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 30-40 weak

### W04.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude session_bucket=london drops 7/13 losers (54%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=london

### W05.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude H60=H60a drops 11/11 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W06.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude session_bucket=ny_open drops 6/6 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W07.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude session_bucket=ny_mid drops 11/11 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W08.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H20=H20a drops 9/12 losers (75%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H20=H20a drops 9/12 losers (75%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude session_bucket=ny_open drops 6/6 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W11.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude strategy_id=bravo_failed_momentum drops 3/11 losers (27%)
- **Final: n=72  W=64/L=8  WR=88.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when strategy=bravo_failed_momentum

### W12.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W13.  `H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W14.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W15.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W16.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W17.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude session_bucket=london drops 4/6 losers (67%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W19.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20b drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W20.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=66  W=61/L=5  WR=92.4%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=66  W=60/L=6  WR=90.9%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W22.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W23.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W24.  `T4=T4a AND RSI=RSI3 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60d drops 6/9 losers (67%)
- **Final: n=36  W=33/L=3  WR=91.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF60 mildly against

### W25.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=60  W=60/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=149  W=56/L=93  WR=37.6%
- Sharpen: sharpest is RSI=RSI3 (66/93 of losers there)
- **Sharp: n=94  W=28/L=66  WR=29.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  ONLY when RSI 40-50 lower neutral

### L02.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=127  W=45/L=82  WR=35.4%
- Sharpen: sharpest is H20=H20e (56/82 of losers there)
- **Sharp: n=72  W=16/L=56  WR=22.2%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L03.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=123  W=42/L=81  WR=34.1%
- Sharpen: sharpest is H20=H20e (65/81 of losers there)
- **Sharp: n=92  W=27/L=65  WR=29.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L04.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=123  W=42/L=81  WR=34.1%
- Sharpen: sharpest is H20=H20e (65/81 of losers there)
- **Sharp: n=92  W=27/L=65  WR=29.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L05.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=116  W=37/L=79  WR=31.9%
- Sharpen: sharpest is H20=H20a (33/79 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L06.  `H60=H60a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is RSI=RSI3 (37/75 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L07.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=109  W=41/L=68  WR=37.6%
- Sharpen: sharpest is RSI=RSI3 (30/68 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L08.  `H20=H20e AND T4=T4c AND BBP=BBP4`
- Raw: n=108  W=37/L=71  WR=34.3%
- Sharpen: sharpest is RSI=RSI3 (56/71 of losers there)
- **Sharp: n=72  W=16/L=56  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=107  W=38/L=69  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=107  W=38/L=69  WR=35.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third

### L10.  `H20=H20a AND T4=T4a AND BBP=BBP2`
- Raw: n=106  W=29/L=77  WR=27.4%
- Sharpen: sharpest is RSI=RSI3 (33/77 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L11.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=106  W=38/L=68  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=106  W=38/L=68  WR=35.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third

### L12.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (39/62 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L13.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (39/62 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L14.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=101  W=34/L=67  WR=33.7%
- Sharpen: sharpest is RSI=RSI3 (52/67 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when RSI 40-50 lower neutral

### L15.  `H20=H20a AND H60=H60a AND ZS=ZS2`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is T4=T4a (48/60 of losers there)
- **Sharp: n=61  W=13/L=48  WR=21.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is T4=T4a (48/60 of losers there)
- **Sharp: n=61  W=13/L=48  WR=21.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is ZS=ZS1 (37/60 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is ZS=ZS1 (37/60 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is ZS=ZS2 (48/59 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L20.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=96  W=36/L=60  WR=37.5%
- Sharpen: sharpest is H60=H60d (28/60 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when HTF60 mildly against

### L21.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=95  W=26/L=69  WR=27.4%
- Sharpen: sharpest is RSI=RSI3 (33/69 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L22.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=94  W=28/L=66  WR=29.8%
- Sharpen: sharpest is H20=H20e (52/66 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L23.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is H20=H20e (50/57 of losers there)
- **Sharp: n=74  W=24/L=50  WR=32.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L24.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is H60=H60e (48/59 of losers there)
- **Sharp: n=68  W=20/L=48  WR=29.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=92  W=27/L=65  WR=29.3%
- Sharpen: sharpest is RSI=RSI3 (50/65 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/47) | T1c(46/53) |
| T4 | T4c(54/46) | T4a(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
