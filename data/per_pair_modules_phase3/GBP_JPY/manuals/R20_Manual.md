# GBP_JPY — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **7,344**  (W=4,200 / L=3,144)  -  WR: **57.2%**

## Session distribution

- ny_mid: n=2027  W=1125/L=902  WR=55.5%
- ny_close: n=1407  W=865/L=542  WR=61.5%
- asia: n=1076  W=617/L=459  WR=57.3%
- london_open: n=968  W=542/L=426  WR=56.0%
- ny_open: n=934  W=519/L=415  WR=55.6%
- london: n=569  W=339/L=230  WR=59.6%
- off_hours: n=330  W=175/L=155  WR=53.0%
- asia_late: n=33  W=18/L=15  WR=54.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=170  W=149/L=21  WR=87.6%
- Refine: exclude T4=T4c drops 11/21 losers (52%)
- **Final: n=134  W=124/L=10  WR=92.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W02.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=170  W=149/L=21  WR=87.6%
- Refine: exclude T4=T4c drops 11/21 losers (52%)
- **Final: n=134  W=124/L=10  WR=92.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W03.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=170  W=149/L=21  WR=87.6%
- Refine: exclude T4=T4c drops 11/21 losers (52%)
- **Final: n=134  W=124/L=10  WR=92.5%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W04.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=151  W=135/L=16  WR=89.4%
- Refine: exclude T4=T4c drops 8/16 losers (50%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W05.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=151  W=135/L=16  WR=89.4%
- Refine: exclude T4=T4c drops 8/16 losers (50%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W06.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=151  W=135/L=16  WR=89.4%
- Refine: exclude T4=T4c drops 8/16 losers (50%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W07.  `H60=H60a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W09.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W13.  `H60=H60a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W15.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W16.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W17.  `H20=H20a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W18.  `H60=H60a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W19.  `T1=T1a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W20.  `T4=T4a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W21.  `BBP=BBP4 AND RSI=RSI7 AND direction_exec=long`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: LONG**  •  upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W22.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W23.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W24.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

### W25.  `H20=H20a AND BBP=BBP4 AND RSI=RSI7 AND direction_exec=long`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=435  W=164/L=271  WR=37.7%
- Sharpen: sharpest is BBP=BBP4 (162/271 of losers there)
- **Sharp: n=219  W=57/L=162  WR=26.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when upper third

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=435  W=164/L=271  WR=37.7%
- Sharpen: sharpest is BBP=BBP4 (162/271 of losers there)
- **Sharp: n=219  W=57/L=162  WR=26.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when upper third

### L03.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=435  W=164/L=271  WR=37.7%
- Sharpen: sharpest is BBP=BBP4 (162/271 of losers there)
- **Sharp: n=219  W=57/L=162  WR=26.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when upper third

### L04.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=433  W=170/L=263  WR=39.3%
- Sharpen: sharpest is H20=H20e (116/263 of losers there)
- **Sharp: n=161  W=45/L=116  WR=28.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L05.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=433  W=170/L=263  WR=39.3%
- Sharpen: sharpest is H20=H20e (116/263 of losers there)
- **Sharp: n=161  W=45/L=116  WR=28.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L06.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=433  W=170/L=263  WR=39.3%
- Sharpen: sharpest is H20=H20e (116/263 of losers there)
- **Sharp: n=161  W=45/L=116  WR=28.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L07.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=421  W=168/L=253  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (162/253 of losers there)
- **Sharp: n=219  W=57/L=162  WR=26.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=421  W=168/L=253  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (162/253 of losers there)
- **Sharp: n=219  W=57/L=162  WR=26.0%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

### L09.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=414  W=163/L=251  WR=39.4%
- Sharpen: sharpest is RSI=RSI5 (162/251 of losers there)
- **Sharp: n=219  W=57/L=162  WR=26.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

### L10.  `T4=T4c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=404  W=156/L=248  WR=38.6%
- Sharpen: sharpest is RSI=RSI5 (163/248 of losers there)
- **Sharp: n=225  W=62/L=163  WR=27.6%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L11.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=404  W=156/L=248  WR=38.6%
- Sharpen: sharpest is RSI=RSI5 (163/248 of losers there)
- **Sharp: n=225  W=62/L=163  WR=27.6%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=392  W=149/L=243  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_mid (129/243 of losers there)
- **Sharp: n=172  W=43/L=129  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 60-70 strong  •  ONLY when session=ny_mid

### L13.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=376  W=149/L=227  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (149/227 of losers there)
- **Sharp: n=206  W=57/L=149  WR=27.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L14.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=376  W=149/L=227  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (149/227 of losers there)
- **Sharp: n=206  W=57/L=149  WR=27.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=376  W=149/L=227  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (149/227 of losers there)
- **Sharp: n=206  W=57/L=149  WR=27.7%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=372  W=145/L=227  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (149/227 of losers there)
- **Sharp: n=206  W=57/L=149  WR=27.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=363  W=144/L=219  WR=39.7%
- Sharpen: sharpest is H60=H60e (211/219 of losers there)
- **Sharp: n=309  W=98/L=211  WR=31.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L18.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=363  W=144/L=219  WR=39.7%
- Sharpen: sharpest is H60=H60e (211/219 of losers there)
- **Sharp: n=309  W=98/L=211  WR=31.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=353  W=138/L=215  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (117/215 of losers there)
- **Sharp: n=160  W=43/L=117  WR=26.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L20.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=349  W=135/L=214  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (123/214 of losers there)
- **Sharp: n=157  W=34/L=123  WR=21.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when upper third

### L21.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=349  W=135/L=214  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (123/214 of losers there)
- **Sharp: n=157  W=34/L=123  WR=21.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when upper third

### L22.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=349  W=135/L=214  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (123/214 of losers there)
- **Sharp: n=157  W=34/L=123  WR=21.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when upper third

### L23.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=323  W=123/L=200  WR=38.1%
- Sharpen: sharpest is RSI=RSI5 (123/200 of losers there)
- **Sharp: n=157  W=34/L=123  WR=21.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

### L24.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=323  W=123/L=200  WR=38.1%
- Sharpen: sharpest is RSI=RSI5 (123/200 of losers there)
- **Sharp: n=157  W=34/L=123  WR=21.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

### L25.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=316  W=118/L=198  WR=37.3%
- Sharpen: sharpest is RSI=RSI5 (123/198 of losers there)
- **Sharp: n=157  W=34/L=123  WR=21.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(42/35) | H20e(37/43) |
| H60 | H60a(54/41) | H60e(42/55) |
| T1 | T1a(55/44) | T1c(45/56) |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/43) | short(44/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
