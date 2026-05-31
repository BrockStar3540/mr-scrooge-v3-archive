# AUD_USD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,363**  (W=1,440 / L=923)  -  WR: **60.9%**

## Session distribution

- ny_mid: n=601  W=350/L=251  WR=58.2%
- asia: n=485  W=306/L=179  WR=63.1%
- ny_close: n=419  W=262/L=157  WR=62.5%
- london_open: n=320  W=193/L=127  WR=60.3%
- ny_open: n=287  W=170/L=117  WR=59.2%
- london: n=124  W=77/L=47  WR=62.1%
- asia_late: n=64  W=44/L=20  WR=68.8%
- off_hours: n=63  W=38/L=25  WR=60.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=95  W=87/L=8  WR=91.6%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W02.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=95  W=87/L=8  WR=91.6%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: LONG**  •  lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=95  W=87/L=8  WR=91.6%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W04.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude H60=H60e drops 2/9 losers (22%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when HTF60 strongly against

### W05.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=london drops 7/12 losers (58%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london

### W06.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H20=H20d drops 7/13 losers (54%)
- **Final: n=62  W=56/L=6  WR=90.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 mildly against

### W07.  `T4=T4a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H20=H20d drops 7/13 losers (54%)
- **Final: n=62  W=56/L=6  WR=90.3%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 mildly against

### W08.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=88  W=81/L=7  WR=92.0%
- Refine: exclude ZS=ZS3 drops 3/7 losers (43%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W09.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=88  W=81/L=7  WR=92.0%
- Refine: exclude ZS=ZS3 drops 3/7 losers (43%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W10.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=london drops 7/12 losers (58%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london

### W13.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=london drops 7/12 losers (58%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london

### W14.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude strategy_id=CP1_coil_breakout_short drops 2/6 losers (33%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when strategy=CP1_coil_breakout_short

### W15.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude strategy_id=CP1_coil_breakout_short drops 2/6 losers (33%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when strategy=CP1_coil_breakout_short

### W16.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude ZS=ZS3 drops 3/7 losers (43%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W17.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H60=H60e drops 2/7 losers (29%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W18.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20d drops 6/11 losers (55%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 mildly against

### W19.  `T4=T4a AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20d drops 6/11 losers (55%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 mildly against

### W20.  `H60=H60e AND T4=T4a AND session_bucket=london`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS3 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W21.  `H60=H60e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS3 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS3 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  AVOID when zscore -1 to +1 neutral

### W23.  `T4=T4a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS3 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when zscore -1 to +1 neutral

### W24.  `T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS3 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W25.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS3 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND RSI=RSI2`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=asia

### L02.  `H20=H20a AND T1=T1c AND RSI=RSI2`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L03.  `H20=H20a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=asia

### L04.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L05.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L06.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=asia

### L07.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L08.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L09.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L10.  `H20=H20a AND H60=H60a AND ZS=ZS4`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (29/64 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L11.  `H20=H20a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (29/64 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L12.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (29/64 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L13.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (29/64 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L14.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (29/64 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L15.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_mid (27/62 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L16.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_mid (27/62 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L17.  `H60=H60e AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_open (25/62 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L24.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_open (25/62 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L25.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_open (25/62 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(43/37) | — |
| H60 | H60e(53/46) | H60a(47/54) |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
