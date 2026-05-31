# EUR_JPY — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,140**  (W=2,234 / L=1,906)  -  WR: **54.0%**

## Session distribution

- ny_mid: n=934  W=510/L=424  WR=54.6%
- asia: n=895  W=460/L=435  WR=51.4%
- london_open: n=615  W=353/L=262  WR=57.4%
- ny_close: n=514  W=303/L=211  WR=58.9%
- ny_open: n=508  W=294/L=214  WR=57.9%
- london: n=496  W=226/L=270  WR=45.6%
- asia_late: n=144  W=74/L=70  WR=51.4%
- off_hours: n=34  W=14/L=20  WR=41.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 7/7 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W02.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 7/7 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W03.  `H20=H20a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W04.  `H20=H20a AND H60=H60e AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W05.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W06.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W07.  `H20=H20a AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=short`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W08.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W09.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W10.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=short`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold  •  AVOID when session=asia

### W11.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude ZS=ZS5 drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore +2 to +3 deep overbought

### W12.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/8 losers (38%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=ny_mid  •  AVOID when strategy=RG1_range_bound_scalp_long

### W13.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/8 losers (38%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when strategy=RG1_range_bound_scalp_long

### W14.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude H20=H20d drops 6/6 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W15.  `BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude H20=H20d drops 6/6 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W16.  `H20=H20a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W17.  `H20=H20a AND H60=H60e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W18.  `H20=H20a AND T1=T1a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W19.  `H20=H20a AND T4=T4a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W20.  `H20=H20a AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W21.  `H20=H20a AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W22.  `H60=H60e AND T1=T1a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W23.  `H60=H60e AND T4=T4a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W24.  `H60=H60e AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=asia

### W25.  `H60=H60e AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=54  W=49/L=5  WR=90.7%
- Refine: exclude RSI=RSI1 drops 5/5 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=ny_open  •  AVOID when RSI 20-30 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=342  W=134/L=208  WR=39.2%
- Sharpen: sharpest is ZS=ZS1 (89/208 of losers there)
- **Sharp: n=117  W=28/L=89  WR=23.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=324  W=126/L=198  WR=38.9%
- Sharpen: sharpest is ZS=ZS1 (89/198 of losers there)
- **Sharp: n=117  W=28/L=89  WR=23.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=324  W=126/L=198  WR=38.9%
- Sharpen: sharpest is ZS=ZS1 (89/198 of losers there)
- **Sharp: n=117  W=28/L=89  WR=23.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=268  W=106/L=162  WR=39.6%
- Sharpen: sharpest is RSI=RSI1 (88/162 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L05.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=267  W=99/L=168  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (88/168 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L06.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=266  W=103/L=163  WR=38.7%
- Sharpen: sharpest is RSI=RSI1 (88/163 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: LONG**  •  just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L07.  `T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=256  W=99/L=157  WR=38.7%
- Sharpen: sharpest is RSI=RSI1 (88/157 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L08.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=256  W=99/L=157  WR=38.7%
- Sharpen: sharpest is RSI=RSI1 (88/157 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L09.  `H60=H60a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=255  W=86/L=169  WR=33.7%
- Sharpen: sharpest is RSI=RSI1 (88/169 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L10.  `T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=255  W=96/L=159  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (88/159 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L11.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=255  W=96/L=159  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (88/159 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L12.  `T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=245  W=92/L=153  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (88/153 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L13.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=245  W=92/L=153  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (88/153 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L14.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=245  W=92/L=153  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (88/153 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L15.  `H60=H60a AND T4=T4c AND BBP=BBP1`
- Raw: n=241  W=85/L=156  WR=35.3%
- Sharpen: sharpest is RSI=RSI1 (82/156 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L16.  `H60=H60a AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=241  W=85/L=156  WR=35.3%
- Sharpen: sharpest is RSI=RSI1 (82/156 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L17.  `H60=H60a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=240  W=86/L=154  WR=35.8%
- Sharpen: sharpest is RSI=RSI1 (82/154 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L18.  `H60=H60a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=240  W=86/L=154  WR=35.8%
- Sharpen: sharpest is RSI=RSI1 (82/154 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L19.  `H60=H60a AND T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=235  W=85/L=150  WR=36.2%
- Sharpen: sharpest is RSI=RSI1 (82/150 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L20.  `H60=H60a AND T1=T1c AND BBP=BBP1`
- Raw: n=230  W=82/L=148  WR=35.7%
- Sharpen: sharpest is RSI=RSI1 (82/148 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L21.  `H60=H60a AND T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=230  W=82/L=148  WR=35.7%
- Sharpen: sharpest is RSI=RSI1 (82/148 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L22.  `H60=H60a AND T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=230  W=82/L=148  WR=35.7%
- Sharpen: sharpest is RSI=RSI1 (82/148 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L23.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=225  W=81/L=144  WR=36.0%
- Sharpen: sharpest is RSI=RSI1 (82/144 of losers there)
- **Sharp: n=106  W=24/L=82  WR=22.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L24.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=208  W=76/L=132  WR=36.5%
- Sharpen: sharpest is session_bucket=london (61/132 of losers there)
- **Sharp: n=63  W=2/L=61  WR=3.2%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=london

### L25.  `H60=H60a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=208  W=83/L=125  WR=39.9%
- Sharpen: sharpest is BBP=BBP1 (88/125 of losers there)
- **Sharp: n=112  W=24/L=88  WR=21.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/27) | H20e(30/36) |
| H60 | H60e(50/43) | H60a(44/51) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(56/44) | T4c(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
