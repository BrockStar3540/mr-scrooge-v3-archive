# EUR_AUD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,381**  (W=1,482 / L=899)  -  WR: **62.2%**

## Session distribution

- asia: n=934  W=582/L=352  WR=62.3%
- london_open: n=387  W=229/L=158  WR=59.2%
- london: n=284  W=179/L=105  WR=63.0%
- ny_open: n=249  W=158/L=91  WR=63.5%
- ny_close: n=187  W=118/L=69  WR=63.1%
- off_hours: n=138  W=84/L=54  WR=60.9%
- asia_late: n=128  W=86/L=42  WR=67.2%
- ny_mid: n=74  W=46/L=28  WR=62.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND BBP=BBP4`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude session_bucket=asia drops 12/19 losers (63%)
- **Final: n=98  W=91/L=7  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=asia

### W02.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude ZS=ZS2 drops 11/17 losers (65%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W03.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude ZS=ZS2 drops 11/17 losers (65%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W04.  `T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=ny_close drops 5/15 losers (33%)
- **Final: n=90  W=80/L=10  WR=88.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_close

### W05.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=asia drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=asia

### W06.  `H20=H20a AND H60=H60a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude RSI=RSI2 drops 7/11 losers (64%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -1 to +1 neutral; session=asia  •  AVOID when RSI 30-40 weak

### W07.  `H20=H20a AND ZS=ZS3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude RSI=RSI2 drops 7/11 losers (64%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral; session=asia  •  AVOID when RSI 30-40 weak

### W08.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W09.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W10.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W11.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W12.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W13.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP1 drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP1 drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W15.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP1 drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W16.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP1 drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W17.  `H20=H20a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS4 drops 10/11 losers (91%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W18.  `H20=H20a AND RSI=RSI3 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20a AND H60=H60a AND session_bucket=asia_late`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia_late  •  AVOID when 4h trend WITH trade

### W20.  `H20=H20a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia_late  •  AVOID when 4h trend WITH trade

### W22.  `H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when 4h trend WITH trade

### W23.  `H60=H60a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia_late  •  AVOID when 4h trend WITH trade

### W24.  `T1=T1a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia_late  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: sharpest is RSI=RSI2 (35/91 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: sharpest is RSI=RSI2 (35/91 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: sharpest is RSI=RSI2 (35/91 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L04.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (17/84 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L05.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (17/84 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L06.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (17/84 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (17/84 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L08.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (17/84 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L09.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (17/84 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L10.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L11.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is RSI=RSI2 (35/86 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is session_bucket=london_open (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L13.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is session_bucket=london_open (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L14.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is session_bucket=london_open (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L15.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=120  W=45/L=75  WR=37.5%
- Sharpen: sharpest is session_bucket=london_open (17/75 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L16.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=118  W=43/L=75  WR=36.4%
- Sharpen: sharpest is session_bucket=london_open (17/75 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L17.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=118  W=43/L=75  WR=36.4%
- Sharpen: sharpest is session_bucket=london_open (17/75 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L18.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=118  W=43/L=75  WR=36.4%
- Sharpen: sharpest is session_bucket=london_open (17/75 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L19.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=116  W=40/L=76  WR=34.5%
- Sharpen: sharpest is RSI=RSI2 (32/76 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=116  W=40/L=76  WR=34.5%
- Sharpen: sharpest is RSI=RSI2 (32/76 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L21.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (35/71 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 30-40 weak

### L22.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (35/71 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (35/71 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L24.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (35/71 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (35/71 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(63/37) | H20e(37/63) |
| H60 | H60a(59/40) | H60e(41/60) |
| T1 | T1a(57/44) | T1c(43/56) |
| T4 | T4a(55/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(59/40) | long(41/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
