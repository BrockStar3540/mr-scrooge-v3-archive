# EUR_CAD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,482**  (W=2,076 / L=1,406)  -  WR: **59.6%**

## Session distribution

- ny_mid: n=955  W=559/L=396  WR=58.5%
- ny_close: n=778  W=456/L=322  WR=58.6%
- ny_open: n=538  W=306/L=232  WR=56.9%
- london_open: n=483  W=307/L=176  WR=63.6%
- asia: n=355  W=209/L=146  WR=58.9%
- london: n=190  W=121/L=69  WR=63.7%
- off_hours: n=129  W=85/L=44  WR=65.9%
- asia_late: n=54  W=33/L=21  WR=61.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=180  W=154/L=26  WR=85.6%
- Refine: exclude RSI=RSI7 drops 10/26 losers (38%)
- **Final: n=158  W=142/L=16  WR=89.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W02.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude RSI=RSI7 drops 10/18 losers (56%)
- **Final: n=141  W=133/L=8  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W03.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude RSI=RSI7 drops 10/18 losers (56%)
- **Final: n=141  W=133/L=8  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W04.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=163  W=139/L=24  WR=85.3%
- Refine: exclude RSI=RSI7 drops 10/24 losers (42%)
- **Final: n=149  W=135/L=14  WR=90.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W05.  `H20=H20e AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=146  W=130/L=16  WR=89.0%
- Refine: exclude RSI=RSI7 drops 10/16 losers (62%)
- **Final: n=132  W=126/L=6  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W06.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=146  W=130/L=16  WR=89.0%
- Refine: exclude RSI=RSI7 drops 10/16 losers (62%)
- **Final: n=132  W=126/L=6  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W07.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude session_bucket=london drops 14/16 losers (88%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=london

### W08.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude session_bucket=london drops 14/16 losers (88%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=london

### W09.  `H20=H20e AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude session_bucket=london drops 14/16 losers (88%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 70-80 overbought  •  AVOID when session=london

### W10.  `H20=H20e AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=105  W=99/L=6  WR=94.3%
- Refine: exclude H60=H60b drops 4/6 losers (67%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 slightly aligned

### W11.  `H20=H20e AND T1=T1a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=london drops 14/15 losers (93%)
- **Final: n=85  W=84/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=london

### W12.  `H20=H20e AND T4=T4a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=london drops 14/15 losers (93%)
- **Final: n=85  W=84/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=london

### W13.  `H20=H20e AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=london drops 14/15 losers (93%)
- **Final: n=85  W=84/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=london

### W14.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=99  W=97/L=2  WR=98.0%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W15.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude H60=H60e drops 7/8 losers (88%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W16.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude T4=T4a drops 3/11 losers (27%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=81  W=79/L=2  WR=97.5%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W18.  `H20=H20e AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=81  W=79/L=2  WR=97.5%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W19.  `H20=H20e AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=81  W=79/L=2  WR=97.5%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W20.  `H20=H20e AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=81  W=79/L=2  WR=97.5%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W21.  `H60=H60e AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=81  W=79/L=2  WR=97.5%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W22.  `H60=H60e AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=81  W=79/L=2  WR=97.5%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W23.  `H60=H60e AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=81  W=79/L=2  WR=97.5%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W24.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude H60=H60e drops 7/8 losers (88%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W25.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 60-70 strong

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=218  W=86/L=132  WR=39.4%
- Sharpen: sharpest is BBP=BBP4 (71/132 of losers there)
- **Sharp: n=94  W=23/L=71  WR=24.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  ONLY when upper third

### L02.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=189  W=74/L=115  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=189  W=74/L=115  WR=39.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 70-80 overbought

### L03.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=189  W=74/L=115  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=189  W=74/L=115  WR=39.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 70-80 overbought

### L04.  `H20=H20e AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=189  W=74/L=115  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=189  W=74/L=115  WR=39.2%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 70-80 overbought

### L05.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=179  W=66/L=113  WR=36.9%
- Sharpen: sharpest is RSI=RSI5 (71/113 of losers there)
- **Sharp: n=94  W=23/L=71  WR=24.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 60-70 strong

### L06.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is RSI=RSI5 (67/109 of losers there)
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: SHORT**  •  upper third; session=ny_close  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=173  W=60/L=113  WR=34.7%
- Sharpen: sharpest is T4=T4c (87/113 of losers there)
- **Sharp: n=122  W=35/L=87  WR=28.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L08.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=172  W=66/L=106  WR=38.4%
- Sharpen: sharpest is RSI=RSI5 (64/106 of losers there)
- **Sharp: n=87  W=23/L=64  WR=26.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 60-70 strong

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=171  W=65/L=106  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=171  W=65/L=106  WR=38.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=171  W=65/L=106  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=171  W=65/L=106  WR=38.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought

### L11.  `H20=H20e AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=171  W=65/L=106  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=171  W=65/L=106  WR=38.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought

### L12.  `T1=T1c AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=170  W=65/L=105  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (69/105 of losers there)
- **Sharp: n=92  W=23/L=69  WR=25.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 60-70 strong

### L13.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=170  W=65/L=105  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (69/105 of losers there)
- **Sharp: n=92  W=23/L=69  WR=25.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 60-70 strong

### L14.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=169  W=56/L=113  WR=33.1%
- Sharpen: sharpest is RSI=RSI6 (37/113 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_close  •  ONLY when RSI 70-80 overbought

### L15.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=165  W=56/L=109  WR=33.9%
- Sharpen: sharpest is T4=T4c (87/109 of losers there)
- **Sharp: n=122  W=35/L=87  WR=28.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=164  W=59/L=105  WR=36.0%
- Sharpen: sharpest is T4=T4c (81/105 of losers there)
- **Sharp: n=115  W=34/L=81  WR=29.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=164  W=59/L=105  WR=36.0%
- Sharpen: sharpest is T4=T4c (81/105 of losers there)
- **Sharp: n=115  W=34/L=81  WR=29.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=163  W=65/L=98  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (62/98 of losers there)
- **Sharp: n=85  W=23/L=62  WR=27.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=160  W=51/L=109  WR=31.9%
- Sharpen: sharpest is RSI=RSI5 (67/109 of losers there)
- **Sharp: n=89  W=22/L=67  WR=24.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 60-70 strong

### L20.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=160  W=51/L=109  WR=31.9%
- Sharpen: sharpest is RSI=RSI5 (67/109 of losers there)
- **Sharp: n=89  W=22/L=67  WR=24.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=160  W=55/L=105  WR=34.4%
- Sharpen: sharpest is RSI=RSI6 (36/105 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 70-80 overbought

### L22.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=160  W=55/L=105  WR=34.4%
- Sharpen: sharpest is RSI=RSI6 (36/105 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 70-80 overbought

### L23.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (45/96 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_close

### L24.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (45/96 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_close

### L25.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (45/96 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(50/44) | H20a(43/49) |
| H60 | — | H60a(33/38) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(51/45) | short(49/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
