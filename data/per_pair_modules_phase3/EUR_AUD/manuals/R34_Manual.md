# EUR_AUD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,810**  (W=3,020 / L=1,790)  -  WR: **62.8%**

## Session distribution

- asia: n=1703  W=1082/L=621  WR=63.5%
- ny_close: n=784  W=485/L=299  WR=61.9%
- london: n=536  W=349/L=187  WR=65.1%
- london_open: n=503  W=309/L=194  WR=61.4%
- ny_mid: n=399  W=233/L=166  WR=58.4%
- ny_open: n=384  W=248/L=136  WR=64.6%
- asia_late: n=316  W=200/L=116  WR=63.3%
- off_hours: n=185  W=114/L=71  WR=61.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=360  W=307/L=53  WR=85.3%
- Refine: exclude BBP=BBP1 drops 21/53 losers (40%)
- **Final: n=298  W=266/L=32  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched lower band

### W02.  `H60=H60a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=360  W=307/L=53  WR=85.3%
- Refine: exclude BBP=BBP1 drops 21/53 losers (40%)
- **Final: n=298  W=266/L=32  WR=89.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched lower band

### W03.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=289  W=246/L=43  WR=85.1%
- Refine: exclude BBP=BBP1 drops 14/43 losers (33%)
- **Final: n=242  W=213/L=29  WR=88.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched lower band

### W04.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=289  W=246/L=43  WR=85.1%
- Refine: exclude BBP=BBP1 drops 14/43 losers (33%)
- **Final: n=242  W=213/L=29  WR=88.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched lower band

### W05.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=258  W=220/L=38  WR=85.3%
- Refine: exclude BBP=BBP4 drops 26/38 losers (68%)
- **Final: n=152  W=140/L=12  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when upper third

### W06.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=249  W=214/L=35  WR=85.9%
- Refine: exclude BBP=BBP1 drops 16/35 losers (46%)
- **Final: n=192  W=173/L=19  WR=90.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched lower band

### W07.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=219  W=192/L=27  WR=87.7%
- Refine: exclude BBP=BBP4 drops 21/27 losers (78%)
- **Final: n=124  W=118/L=6  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when upper third

### W08.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=217  W=191/L=26  WR=88.0%
- Refine: exclude BBP=BBP1 drops 8/26 losers (31%)
- **Final: n=191  W=173/L=18  WR=90.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched lower band

### W09.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=212  W=184/L=28  WR=86.8%
- Refine: exclude BBP=BBP4 drops 23/28 losers (82%)
- **Final: n=119  W=114/L=5  WR=95.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when upper third

### W10.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=211  W=184/L=27  WR=87.2%
- Refine: exclude BBP=BBP4 drops 21/27 losers (78%)
- **Final: n=120  W=114/L=6  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when upper third

### W11.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=205  W=181/L=24  WR=88.3%
- Refine: exclude BBP=BBP1 drops 8/24 losers (33%)
- **Final: n=179  W=163/L=16  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched lower band

### W12.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=188  W=160/L=28  WR=85.1%
- Refine: exclude T4=T4a drops 17/28 losers (61%)
- **Final: n=99  W=88/L=11  WR=88.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=188  W=160/L=28  WR=85.1%
- Refine: exclude T4=T4a drops 17/28 losers (61%)
- **Final: n=99  W=88/L=11  WR=88.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W14.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=175  W=154/L=21  WR=88.0%
- Refine: exclude BBP=BBP4 drops 16/21 losers (76%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when upper third

### W15.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=157  W=135/L=22  WR=86.0%
- Refine: no further refinement
- **Final: n=157  W=135/L=22  WR=86.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia

### W16.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=144  W=123/L=21  WR=85.4%
- Refine: exclude T4=T4a drops 14/21 losers (67%)
- **Final: n=76  W=69/L=7  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W17.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=138  W=125/L=13  WR=90.6%
- Refine: exclude H60=H60e drops 8/13 losers (62%)
- **Final: n=111  W=106/L=5  WR=95.5%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 strongly against

### W18.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=135  W=122/L=13  WR=90.4%
- Refine: exclude T4=T4c drops 8/13 losers (62%)
- **Final: n=109  W=104/L=5  WR=95.4%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W19.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=123  W=113/L=10  WR=91.9%
- Refine: exclude T4=T4c drops 7/10 losers (70%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W20.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=119  W=108/L=11  WR=90.8%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=94  W=89/L=5  WR=94.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W21.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=114  W=102/L=12  WR=89.5%
- Refine: exclude T4=T4c drops 7/12 losers (58%)
- **Final: n=94  W=89/L=5  WR=94.7%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W22.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude T1=T1c drops 9/16 losers (56%)
- **Final: n=76  W=69/L=7  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 1h trend AGAINST trade

### W23.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W24.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude H60=H60a drops 3/5 losers (60%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W25.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude T4=T4c drops 7/10 losers (70%)
- **Final: n=86  W=83/L=3  WR=96.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=225  W=82/L=143  WR=36.4%
- Sharpen: sharpest is ZS=ZS2 (50/143 of losers there)
- **Sharp: n=54  W=4/L=50  WR=7.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -2 to -1 oversold

### L02.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=204  W=81/L=123  WR=39.7%
- Sharpen: sharpest is T1=T1c (112/123 of losers there)
- **Sharp: n=165  W=53/L=112  WR=32.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L03.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=201  W=70/L=131  WR=34.8%
- Sharpen: sharpest is ZS=ZS5 (64/131 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=193  W=73/L=120  WR=37.8%
- Sharpen: sharpest is ZS=ZS2 (47/120 of losers there)
- **Sharp: n=49  W=2/L=47  WR=4.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -2 to -1 oversold

### L05.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=189  W=73/L=116  WR=38.6%
- Sharpen: sharpest is T1=T1c (105/116 of losers there)
- **Sharp: n=158  W=53/L=105  WR=33.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=186  W=73/L=113  WR=39.2%
- Sharpen: sharpest is T1=T1c (105/113 of losers there)
- **Sharp: n=158  W=53/L=105  WR=33.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L07.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=185  W=74/L=111  WR=40.0%
- Sharpen: sharpest is ZS=ZS5 (29/111 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=185  W=74/L=111  WR=40.0%
- Sharpen: sharpest is ZS=ZS5 (29/111 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=185  W=74/L=111  WR=40.0%
- Sharpen: sharpest is ZS=ZS5 (29/111 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=181  W=66/L=115  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (27/115 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L11.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=181  W=66/L=115  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (27/115 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L12.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=180  W=63/L=117  WR=35.0%
- Sharpen: sharpest is session_bucket=asia (50/117 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L13.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=168  W=63/L=105  WR=37.5%
- Sharpen: sharpest is ZS=ZS5 (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=168  W=63/L=105  WR=37.5%
- Sharpen: sharpest is ZS=ZS5 (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=166  W=56/L=110  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (52/110 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=166  W=62/L=104  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (21/104 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L17.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=165  W=53/L=112  WR=32.1%
- Sharpen: sharpest is ZS=ZS5 (55/112 of losers there)
- **Sharp: n=59  W=4/L=55  WR=6.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=163  W=54/L=109  WR=33.1%
- Sharpen: sharpest is ZS=ZS5 (52/109 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H20=H20a AND T1=T1c AND BBP=BBP5`
- Raw: n=159  W=62/L=97  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (38/97 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_close

### L20.  `H20=H20a AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=159  W=62/L=97  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (38/97 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L21.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=157  W=50/L=107  WR=31.8%
- Sharpen: sharpest is session_bucket=asia (46/107 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=asia

### L22.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=157  W=62/L=95  WR=39.5%
- Sharpen: sharpest is session_bucket=ny_mid (21/95 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L23.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=151  W=54/L=97  WR=35.8%
- Sharpen: sharpest is T4=T4c (26/97 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L24.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=148  W=51/L=97  WR=34.5%
- Sharpen: sharpest is BBP=BBP3 (18/97 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when middle of band

### L25.  `H20=H20a AND H60=H60e AND T1=T1a`
- Raw: n=145  W=50/L=95  WR=34.5%
- Sharpen: sharpest is session_bucket=asia (34/95 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(52/43) | H20a(43/52) |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
