# EUR_CAD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,309**  (W=2,058 / L=1,251)  -  WR: **62.2%**

## Session distribution

- ny_mid: n=1331  W=839/L=492  WR=63.0%
- ny_open: n=535  W=323/L=212  WR=60.4%
- ny_close: n=458  W=297/L=161  WR=64.8%
- asia: n=455  W=285/L=170  WR=62.6%
- london_open: n=333  W=202/L=131  WR=60.7%
- london: n=141  W=79/L=62  WR=56.0%
- off_hours: n=53  W=31/L=22  WR=58.5%
- asia_late: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=314  W=275/L=39  WR=87.6%
- Refine: exclude session_bucket=ny_close drops 20/39 losers (51%)
- **Final: n=232  W=213/L=19  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W02.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=253  W=217/L=36  WR=85.8%
- Refine: exclude BBP=BBP4 drops 14/36 losers (39%)
- **Final: n=206  W=184/L=22  WR=89.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W03.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=214  W=186/L=28  WR=86.9%
- Refine: exclude BBP=BBP4 drops 14/28 losers (50%)
- **Final: n=176  W=162/L=14  WR=92.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=188  W=168/L=20  WR=89.4%
- Refine: exclude ZS=ZS5 drops 11/20 losers (55%)
- **Final: n=145  W=136/L=9  WR=93.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W05.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=174  W=156/L=18  WR=89.7%
- Refine: exclude T4=T4c drops 14/18 losers (78%)
- **Final: n=105  W=101/L=4  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=169  W=147/L=22  WR=87.0%
- Refine: exclude BBP=BBP4 drops 14/22 losers (64%)
- **Final: n=137  W=129/L=8  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W07.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=164  W=142/L=22  WR=86.6%
- Refine: exclude T1=T1c drops 15/22 losers (68%)
- **Final: n=121  W=114/L=7  WR=94.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W08.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=144  W=134/L=10  WR=93.1%
- Refine: exclude T4=T4c drops 10/10 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W09.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=140  W=123/L=17  WR=87.9%
- Refine: exclude ZS=ZS5 drops 8/17 losers (47%)
- **Final: n=106  W=97/L=9  WR=91.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W10.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude session_bucket=ny_close drops 12/18 losers (67%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=136  W=116/L=20  WR=85.3%
- Refine: exclude direction_exec=short drops 17/20 losers (85%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when short

### W12.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=136  W=116/L=20  WR=85.3%
- Refine: exclude direction_exec=short drops 17/20 losers (85%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when short

### W13.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/19 losers (68%)
- **Final: n=105  W=99/L=6  WR=94.3%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W14.  `BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/19 losers (68%)
- **Final: n=105  W=99/L=6  WR=94.3%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W15.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=130  W=121/L=9  WR=93.1%
- Refine: exclude ZS=ZS5 drops 4/9 losers (44%)
- **Final: n=103  W=98/L=5  WR=95.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore +2 to +3 deep overbought

### W16.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=129  W=116/L=13  WR=89.9%
- Refine: exclude ZS=ZS5 drops 10/13 losers (77%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W17.  `T1=T1a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=128  W=117/L=11  WR=91.4%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=109  W=107/L=2  WR=98.2%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W18.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude T1=T1c drops 14/17 losers (82%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude T1=T1c drops 14/17 losers (82%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=126  W=116/L=10  WR=92.1%
- Refine: exclude T4=T4c drops 10/10 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude RSI=RSI3 drops 9/17 losers (53%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 13/17 losers (76%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W23.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude direction_exec=short drops 13/16 losers (81%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when short

### W24.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=118  W=107/L=11  WR=90.7%
- Refine: exclude H20=H20b drops 9/11 losers (82%)
- **Final: n=107  W=105/L=2  WR=98.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W25.  `H20=H20a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 10/16 losers (62%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched upper band  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=207  W=62/L=145  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_mid (67/145 of losers there)
- **Sharp: n=74  W=7/L=67  WR=9.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L02.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=186  W=63/L=123  WR=33.9%
- Sharpen: sharpest is H20=H20e (87/123 of losers there)
- **Sharp: n=112  W=25/L=87  WR=22.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=186  W=63/L=123  WR=33.9%
- Sharpen: sharpest is H20=H20e (87/123 of losers there)
- **Sharp: n=112  W=25/L=87  WR=22.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L04.  `T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is RSI=RSI4 (95/110 of losers there)
- **Sharp: n=125  W=30/L=95  WR=24.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=171  W=65/L=106  WR=38.0%
- Sharpen: sharpest is direction_exec=short (26/106 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when short

### L06.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=166  W=46/L=120  WR=27.7%
- Sharpen: sharpest is H60=H60e (87/120 of losers there)
- **Sharp: n=112  W=25/L=87  WR=22.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L07.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=163  W=60/L=103  WR=36.8%
- Sharpen: sharpest is direction_exec=short (58/103 of losers there)
- **Sharp: n=60  W=2/L=58  WR=3.3%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when short

### L08.  `H20=H20e AND T1=T1c AND RSI=RSI4`
- Raw: n=161  W=63/L=98  WR=39.1%
- Sharpen: sharpest is ZS=ZS5 (48/98 of losers there)
- **Sharp: n=51  W=3/L=48  WR=5.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=158  W=63/L=95  WR=39.9%
- Sharpen: sharpest is T1=T1c (53/95 of losers there)
- **Sharp: n=63  W=10/L=53  WR=15.9%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=151  W=54/L=97  WR=35.8%
- Sharpen: sharpest is direction_exec=short (24/97 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when short

### L11.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is direction_exec=short (51/92 of losers there)
- **Sharp: n=53  W=2/L=51  WR=3.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when short

### L12.  `T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (77/84 of losers there)
- **Sharp: n=97  W=20/L=77  WR=20.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L13.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (77/84 of losers there)
- **Sharp: n=97  W=20/L=77  WR=20.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L14.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=134  W=33/L=101  WR=24.6%
- Sharpen: sharpest is session_bucket=london_open (18/101 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L15.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=132  W=47/L=85  WR=35.6%
- Sharpen: sharpest is T1=T1c (48/85 of losers there)
- **Sharp: n=51  W=3/L=48  WR=5.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L16.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=130  W=46/L=84  WR=35.4%
- Sharpen: sharpest is H20=H20e (77/84 of losers there)
- **Sharp: n=99  W=22/L=77  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L17.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=130  W=46/L=84  WR=35.4%
- Sharpen: sharpest is H20=H20e (77/84 of losers there)
- **Sharp: n=99  W=22/L=77  WR=22.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=125  W=30/L=95  WR=24.0%
- Sharpen: sharpest is session_bucket=ny_mid (62/95 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L19.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=125  W=34/L=91  WR=27.2%
- Sharpen: sharpest is session_bucket=ny_mid (58/91 of losers there)
- **Sharp: n=60  W=2/L=58  WR=3.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L20.  `H20=H20e AND H60=H60e AND ZS=ZS5`
- Raw: n=122  W=38/L=84  WR=31.1%
- Sharpen: sharpest is T1=T1c (52/84 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L21.  `H20=H20e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=122  W=38/L=84  WR=31.1%
- Sharpen: sharpest is T1=T1c (52/84 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20e AND H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=122  W=38/L=84  WR=31.1%
- Sharpen: sharpest is T1=T1c (52/84 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L23.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (62/71 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L24.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (26/69 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L25.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=112  W=25/L=87  WR=22.3%
- Sharpen: sharpest is ZS=ZS1 (31/87 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/31) | H20e(30/38) |
| H60 | H60a(46/40) | H60e(38/46) |
| T1 | T1a(57/44) | T1c(43/56) |
| T4 | T4a(58/45) | T4c(42/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
