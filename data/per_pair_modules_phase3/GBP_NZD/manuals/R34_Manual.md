# GBP_NZD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,908**  (W=2,200 / L=1,708)  -  WR: **56.3%**

## Session distribution

- asia: n=1328  W=733/L=595  WR=55.2%
- ny_close: n=719  W=440/L=279  WR=61.2%
- ny_mid: n=581  W=327/L=254  WR=56.3%
- ny_open: n=395  W=197/L=198  WR=49.9%
- london: n=377  W=207/L=170  WR=54.9%
- london_open: n=230  W=133/L=97  WR=57.8%
- off_hours: n=181  W=110/L=71  WR=60.8%
- asia_late: n=97  W=53/L=44  WR=54.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60e AND T1=T1a AND ZS=ZS3`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude strategy_id=CP1_coil_breakout_short drops 3/10 losers (30%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when strategy=CP1_coil_breakout_short

### W02.  `H20=H20a AND H60=H60e AND ZS=ZS3 AND direction_exec=short`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude strategy_id=CP1_coil_breakout_short drops 3/10 losers (30%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore -1 to +1 neutral  •  AVOID when strategy=CP1_coil_breakout_short

### W03.  `T4=T4c AND BBP=BBP0 AND session_bucket=ny_close`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H20=H20a drops 8/10 losers (80%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; session=ny_close  •  AVOID when HTF20 strongly against

### W05.  `H60=H60a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; session=ny_close  •  AVOID when HTF20 strongly against

### W06.  `H60=H60a AND T4=T4c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude H20=H20d drops 4/8 losers (50%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  AVOID when HTF20 mildly against

### W07.  `H60=H60a AND T1=T1c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  AVOID when HTF20 strongly against

### W08.  `H60=H60a AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_close  •  AVOID when HTF20 strongly against

### W09.  `H60=H60e AND BBP=BBP3 AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude RSI=RSI3 drops 5/9 losers (56%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W10.  `H60=H60e AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude RSI=RSI3 drops 5/9 losers (56%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W11.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W12.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W13.  `H60=H60e AND BBP=BBP3 AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=52  W=48/L=4  WR=92.3%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=19  W=19/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; RSI 30-40 weak; session=ny_mid  •  AVOID when HTF20 strongly against

### W14.  `T1=T1c AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=off_hours  •  AVOID when middle of band

### W15.  `T4=T4c AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=off_hours  •  AVOID when middle of band

### W16.  `RSI=RSI3 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=off_hours  •  AVOID when middle of band

### W17.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=off_hours  •  AVOID when middle of band

### W18.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=off_hours  •  AVOID when middle of band

### W19.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=off_hours  •  AVOID when middle of band

### W20.  `H20=H20a AND BBP=BBP0 AND session_bucket=off_hours`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude ZS=ZS1 drops 5/5 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; session=off_hours  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `H60=H60a AND BBP=BBP0 AND session_bucket=off_hours`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude ZS=ZS1 drops 5/5 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; session=off_hours  •  AVOID when zscore -3 to -2 deep oversold

### W22.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND session_bucket=off_hours`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude ZS=ZS1 drops 5/5 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; session=off_hours  •  AVOID when zscore -3 to -2 deep oversold

### W23.  `H20=H20a AND RSI=RSI0 AND ZS=ZS3`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold; zscore -1 to +1 neutral  •  AVOID when upper third

### W24.  `H60=H60e AND RSI=RSI0 AND ZS=ZS3`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI<20 extreme oversold; zscore -1 to +1 neutral  •  AVOID when upper third

### W25.  `T1=T1a AND RSI=RSI0 AND ZS=ZS3`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI<20 extreme oversold; zscore -1 to +1 neutral  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=266  W=99/L=167  WR=37.2%
- Sharpen: sharpest is BBP=BBP0 (75/167 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=266  W=99/L=167  WR=37.2%
- Sharpen: sharpest is BBP=BBP0 (75/167 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L03.  `H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=266  W=99/L=167  WR=37.2%
- Sharpen: sharpest is BBP=BBP0 (75/167 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold  •  ONLY when deep below lower band

### L04.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=266  W=99/L=167  WR=37.2%
- Sharpen: sharpest is BBP=BBP0 (75/167 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=266  W=99/L=167  WR=37.2%
- Sharpen: sharpest is BBP=BBP0 (75/167 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=266  W=99/L=167  WR=37.2%
- Sharpen: sharpest is BBP=BBP0 (75/167 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L07.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=258  W=92/L=166  WR=35.7%
- Sharpen: sharpest is ZS=ZS1 (69/166 of losers there)
- **Sharp: n=85  W=16/L=69  WR=18.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=258  W=92/L=166  WR=35.7%
- Sharpen: sharpest is ZS=ZS1 (69/166 of losers there)
- **Sharp: n=85  W=16/L=69  WR=18.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=231  W=82/L=149  WR=35.5%
- Sharpen: sharpest is ZS=ZS1 (61/149 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is ZS=ZS1 (58/137 of losers there)
- **Sharp: n=65  W=7/L=58  WR=10.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H20=H20a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H20=H20a AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H20=H20a AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20a AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=220  W=74/L=146  WR=33.6%
- Sharpen: sharpest is ZS=ZS1 (61/146 of losers there)
- **Sharp: n=65  W=4/L=61  WR=6.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=211  W=80/L=131  WR=37.9%
- Sharpen: sharpest is RSI=RSI1 (75/131 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 20-30 oversold

### L22.  `H60=H60e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=208  W=77/L=131  WR=37.0%
- Sharpen: sharpest is RSI=RSI1 (75/131 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band  •  ONLY when RSI 20-30 oversold

### L23.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=208  W=77/L=131  WR=37.0%
- Sharpen: sharpest is RSI=RSI1 (75/131 of losers there)
- **Sharp: n=94  W=19/L=75  WR=20.2%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 20-30 oversold

### L24.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=194  W=63/L=131  WR=32.5%
- Sharpen: sharpest is H20=H20a (51/131 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 aligned WITH trade

### L25.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=194  W=63/L=131  WR=32.5%
- Sharpen: sharpest is H20=H20a (51/131 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/46) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | RSI1(18/25) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
