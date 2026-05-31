# GBP_JPY — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,803**  (W=2,842 / L=1,961)  -  WR: **59.2%**

## Session distribution

- asia: n=1930  W=1153/L=777  WR=59.7%
- london_open: n=1054  W=601/L=453  WR=57.0%
- ny_open: n=433  W=278/L=155  WR=64.2%
- ny_mid: n=355  W=194/L=161  WR=54.6%
- asia_late: n=352  W=213/L=139  WR=60.5%
- london: n=298  W=174/L=124  WR=58.4%
- ny_close: n=215  W=134/L=81  WR=62.3%
- off_hours: n=166  W=95/L=71  WR=57.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=154  W=134/L=20  WR=87.0%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W02.  `RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=154  W=134/L=20  WR=87.0%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W03.  `T1=T1a AND BBP=BBP4 AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=154  W=134/L=20  WR=87.0%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W04.  `T1=T1a AND RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=154  W=134/L=20  WR=87.0%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W05.  `BBP=BBP4 AND RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=154  W=134/L=20  WR=87.0%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W06.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=143  W=123/L=20  WR=86.0%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W07.  `T4=T4a AND RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=143  W=123/L=20  WR=86.0%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W08.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=london_open drops 7/18 losers (39%)
- **Final: n=102  W=91/L=11  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W09.  `H60=H60e AND RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=london_open drops 7/18 losers (39%)
- **Final: n=102  W=91/L=11  WR=89.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W10.  `H20=H20a AND H60=H60a AND RSI=RSI3`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude session_bucket=london_open drops 9/15 losers (60%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W11.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude session_bucket=london_open drops 9/15 losers (60%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W12.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude session_bucket=london_open drops 9/15 losers (60%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W13.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude H20=H20e drops 6/10 losers (60%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W14.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W15.  `H20=H20e AND RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W16.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude session_bucket=london_open drops 7/14 losers (50%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W17.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude session_bucket=london_open drops 9/14 losers (64%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W18.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude T4=T4c drops 14/14 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude ZS=ZS3 drops 5/13 losers (38%)
- **Final: n=73  W=65/L=8  WR=89.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W20.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude ZS=ZS3 drops 5/13 losers (38%)
- **Final: n=73  W=65/L=8  WR=89.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude ZS=ZS3 drops 5/13 losers (38%)
- **Final: n=73  W=65/L=8  WR=89.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=91  W=85/L=6  WR=93.4%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W23.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=88  W=82/L=6  WR=93.2%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W24.  `T1=T1a AND BBP=BBP4 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W25.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=293  W=117/L=176  WR=39.9%
- Sharpen: sharpest is session_bucket=london_open (64/176 of losers there)
- **Sharp: n=81  W=17/L=64  WR=21.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=london_open

### L02.  `H60=H60a AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=293  W=117/L=176  WR=39.9%
- Sharpen: sharpest is session_bucket=london_open (64/176 of losers there)
- **Sharp: n=81  W=17/L=64  WR=21.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 20-30 oversold  •  ONLY when session=london_open

### L03.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=276  W=106/L=170  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (61/170 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L04.  `H60=H60a AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=276  W=106/L=170  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (61/170 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L05.  `T1=T1c AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=270  W=98/L=172  WR=36.3%
- Sharpen: sharpest is H20=H20a (96/172 of losers there)
- **Sharp: n=133  W=37/L=96  WR=27.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L06.  `RSI=RSI1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=270  W=98/L=172  WR=36.3%
- Sharpen: sharpest is H20=H20a (96/172 of losers there)
- **Sharp: n=133  W=37/L=96  WR=27.8%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L07.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=270  W=98/L=172  WR=36.3%
- Sharpen: sharpest is H20=H20a (96/172 of losers there)
- **Sharp: n=133  W=37/L=96  WR=27.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=247  W=98/L=149  WR=39.7%
- Sharpen: sharpest is H20=H20a (96/149 of losers there)
- **Sharp: n=133  W=37/L=96  WR=27.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L09.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=247  W=98/L=149  WR=39.7%
- Sharpen: sharpest is H20=H20a (96/149 of losers there)
- **Sharp: n=133  W=37/L=96  WR=27.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L10.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=208  W=81/L=127  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (32/127 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L11.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=197  W=62/L=135  WR=31.5%
- Sharpen: sharpest is BBP=BBP4 (66/135 of losers there)
- **Sharp: n=80  W=14/L=66  WR=17.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L12.  `H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=170  W=42/L=128  WR=24.7%
- Sharpen: sharpest is ZS=ZS4 (53/128 of losers there)
- **Sharp: n=63  W=10/L=53  WR=15.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore +1 to +2 overbought

### L13.  `T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=164  W=63/L=101  WR=38.4%
- Sharpen: sharpest is ZS=ZS4 (80/101 of losers there)
- **Sharp: n=113  W=33/L=80  WR=29.2%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when zscore +1 to +2 overbought

### L14.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=161  W=41/L=120  WR=25.5%
- Sharpen: sharpest is ZS=ZS4 (50/120 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore +1 to +2 overbought

### L15.  `T1=T1c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=159  W=52/L=107  WR=32.7%
- Sharpen: sharpest is ZS=ZS4 (86/107 of losers there)
- **Sharp: n=108  W=22/L=86  WR=20.4%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when zscore +1 to +2 overbought

### L16.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=159  W=52/L=107  WR=32.7%
- Sharpen: sharpest is ZS=ZS4 (86/107 of losers there)
- **Sharp: n=108  W=22/L=86  WR=20.4%**
- **Dir: LONG**  •  upper third; RSI 30-40 weak  •  ONLY when zscore +1 to +2 overbought

### L17.  `T1=T1c AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=159  W=52/L=107  WR=32.7%
- Sharpen: sharpest is ZS=ZS4 (86/107 of losers there)
- **Sharp: n=108  W=22/L=86  WR=20.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when zscore +1 to +2 overbought

### L18.  `H20=H20e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=154  W=53/L=101  WR=34.4%
- Sharpen: sharpest is H60=H60e (66/101 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=154  W=53/L=101  WR=34.4%
- Sharpen: sharpest is H60=H60e (66/101 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L20.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=153  W=52/L=101  WR=34.0%
- Sharpen: sharpest is ZS=ZS4 (80/101 of losers there)
- **Sharp: n=102  W=22/L=80  WR=21.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when zscore +1 to +2 overbought

### L21.  `T4=T4c AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=153  W=52/L=101  WR=34.0%
- Sharpen: sharpest is ZS=ZS4 (80/101 of losers there)
- **Sharp: n=102  W=22/L=80  WR=21.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when zscore +1 to +2 overbought

### L22.  `H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=152  W=38/L=114  WR=25.0%
- Sharpen: sharpest is ZS=ZS4 (48/114 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore +1 to +2 overbought

### L23.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=152  W=38/L=114  WR=25.0%
- Sharpen: sharpest is ZS=ZS4 (48/114 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore +1 to +2 overbought

### L24.  `H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=148  W=54/L=94  WR=36.5%
- Sharpen: sharpest is BBP=BBP2 (44/94 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when lower third

### L25.  `H20=H20e AND T1=T1a AND RSI=RSI3`
- Raw: n=145  W=52/L=93  WR=35.9%
- Sharpen: sharpest is H60=H60e (58/93 of losers there)
- **Sharp: n=76  W=18/L=58  WR=23.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
