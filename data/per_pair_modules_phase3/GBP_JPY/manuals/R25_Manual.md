# GBP_JPY — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,972**  (W=2,242 / L=1,730)  -  WR: **56.4%**

## Session distribution

- asia: n=1086  W=628/L=458  WR=57.8%
- london_open: n=694  W=393/L=301  WR=56.6%
- ny_close: n=546  W=320/L=226  WR=58.6%
- ny_mid: n=489  W=266/L=223  WR=54.4%
- london: n=430  W=222/L=208  WR=51.6%
- ny_open: n=322  W=174/L=148  WR=54.0%
- asia_late: n=288  W=174/L=114  WR=60.4%
- off_hours: n=117  W=65/L=52  WR=55.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=135  W=120/L=15  WR=88.9%
- Refine: exclude T1=T1c drops 9/15 losers (60%)
- **Final: n=115  W=109/L=6  WR=94.8%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W02.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=135  W=120/L=15  WR=88.9%
- Refine: exclude T1=T1c drops 9/15 losers (60%)
- **Final: n=115  W=109/L=6  WR=94.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W03.  `H20=H20a AND H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude RSI=RSI2 drops 6/16 losers (38%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W04.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude RSI=RSI2 drops 6/16 losers (38%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W05.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude T4=T4c drops 16/17 losers (94%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W06.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=115  W=109/L=6  WR=94.8%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/6 losers (33%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when strategy=bravo_failed_momentum

### W07.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=115  W=109/L=6  WR=94.8%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/6 losers (33%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=bravo_failed_momentum

### W08.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude T1=T1c drops 9/15 losers (60%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W09.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude T1=T1c drops 9/15 losers (60%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W10.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 7/9 losers (78%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 7/9 losers (78%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W12.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 7/9 losers (78%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W13.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 7/9 losers (78%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=london_open  •  AVOID when 4h trend AGAINST trade

### W15.  `T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when 4h trend AGAINST trade

### W16.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london_open  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; session=london_open  •  AVOID when 4h trend AGAINST trade

### W19.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W21.  `H20=H20a AND H60=H60e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W22.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W23.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W24.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude RSI=RSI3 drops 11/12 losers (92%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W25.  `H20=H20e AND T4=T4a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude RSI=RSI3 drops 11/12 losers (92%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=505  W=180/L=325  WR=35.6%
- Sharpen: sharpest is T4=T4c (148/325 of losers there)
- **Sharp: n=193  W=45/L=148  WR=23.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=490  W=152/L=338  WR=31.0%
- Sharpen: sharpest is T4=T4c (161/338 of losers there)
- **Sharp: n=178  W=17/L=161  WR=9.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L03.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=457  W=152/L=305  WR=33.3%
- Sharpen: sharpest is T4=T4c (128/305 of losers there)
- **Sharp: n=145  W=17/L=128  WR=11.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=457  W=152/L=305  WR=33.3%
- Sharpen: sharpest is T4=T4c (128/305 of losers there)
- **Sharp: n=145  W=17/L=128  WR=11.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L05.  `T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=398  W=158/L=240  WR=39.7%
- Sharpen: sharpest is RSI=RSI2 (173/240 of losers there)
- **Sharp: n=234  W=61/L=173  WR=26.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L06.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=398  W=158/L=240  WR=39.7%
- Sharpen: sharpest is RSI=RSI2 (173/240 of losers there)
- **Sharp: n=234  W=61/L=173  WR=26.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L07.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=284  W=104/L=180  WR=36.6%
- Sharpen: sharpest is RSI=RSI2 (61/180 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=271  W=104/L=167  WR=38.4%
- Sharpen: sharpest is RSI=RSI2 (105/167 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L09.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=271  W=104/L=167  WR=38.4%
- Sharpen: sharpest is RSI=RSI2 (105/167 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L10.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=266  W=77/L=189  WR=28.9%
- Sharpen: sharpest is T4=T4c (105/189 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L11.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=266  W=83/L=183  WR=31.2%
- Sharpen: sharpest is T4=T4c (108/183 of losers there)
- **Sharp: n=131  W=23/L=108  WR=17.6%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L12.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=254  W=72/L=182  WR=28.3%
- Sharpen: sharpest is T4=T4c (105/182 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=254  W=72/L=182  WR=28.3%
- Sharpen: sharpest is T4=T4c (105/182 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L14.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=253  W=78/L=175  WR=30.8%
- Sharpen: sharpest is T4=T4c (107/175 of losers there)
- **Sharp: n=130  W=23/L=107  WR=17.7%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L15.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=253  W=78/L=175  WR=30.8%
- Sharpen: sharpest is T4=T4c (107/175 of losers there)
- **Sharp: n=130  W=23/L=107  WR=17.7%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L16.  `T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=251  W=97/L=154  WR=38.6%
- Sharpen: sharpest is T1=T1c (105/154 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L17.  `T4=T4c AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=251  W=97/L=154  WR=38.6%
- Sharpen: sharpest is T1=T1c (105/154 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L18.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=249  W=98/L=151  WR=39.4%
- Sharpen: sharpest is RSI=RSI2 (61/151 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L19.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=247  W=83/L=164  WR=33.6%
- Sharpen: sharpest is T4=T4c (89/164 of losers there)
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=247  W=83/L=164  WR=33.6%
- Sharpen: sharpest is T4=T4c (89/164 of losers there)
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L21.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=246  W=66/L=180  WR=26.8%
- Sharpen: sharpest is T4=T4c (105/180 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L22.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=234  W=61/L=173  WR=26.1%
- Sharpen: sharpest is T4=T4c (105/173 of losers there)
- **Sharp: n=111  W=6/L=105  WR=5.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=234  W=78/L=156  WR=33.3%
- Sharpen: sharpest is T4=T4c (88/156 of losers there)
- **Sharp: n=111  W=23/L=88  WR=20.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L24.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=234  W=78/L=156  WR=33.3%
- Sharpen: sharpest is T4=T4c (88/156 of losers there)
- **Sharp: n=111  W=23/L=88  WR=20.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L25.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=234  W=78/L=156  WR=33.3%
- Sharpen: sharpest is T4=T4c (88/156 of losers there)
- **Sharp: n=111  W=23/L=88  WR=20.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(51/43) | H60a(46/53) |
| T1 | T1a(55/43) | T1c(45/57) |
| T4 | T4a(52/46) | T4c(48/54) |
| BBP | — | — |
| RSI | RSI3(58/53) | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/44) | long(46/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
