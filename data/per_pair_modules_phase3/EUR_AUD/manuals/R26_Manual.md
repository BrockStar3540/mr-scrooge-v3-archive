# EUR_AUD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,136**  (W=3,785 / L=2,351)  -  WR: **61.7%**

## Session distribution

- asia: n=1379  W=845/L=534  WR=61.3%
- london_open: n=1264  W=817/L=447  WR=64.6%
- ny_mid: n=1170  W=713/L=457  WR=60.9%
- ny_open: n=864  W=499/L=365  WR=57.8%
- london: n=599  W=376/L=223  WR=62.8%
- ny_close: n=567  W=356/L=211  WR=62.8%
- asia_late: n=204  W=129/L=75  WR=63.2%
- off_hours: n=89  W=50/L=39  WR=56.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=242  W=212/L=30  WR=87.6%
- Refine: exclude RSI=RSI4 drops 22/30 losers (73%)
- **Final: n=116  W=108/L=8  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W02.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=205  W=176/L=29  WR=85.9%
- Refine: exclude H60=H60a drops 13/29 losers (45%)
- **Final: n=166  W=150/L=16  WR=90.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W03.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=177  W=160/L=17  WR=90.4%
- Refine: exclude RSI=RSI3 drops 4/17 losers (24%)
- **Final: n=172  W=159/L=13  WR=92.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W04.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=177  W=160/L=17  WR=90.4%
- Refine: exclude RSI=RSI3 drops 4/17 losers (24%)
- **Final: n=172  W=159/L=13  WR=92.4%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W05.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude ZS=ZS3 drops 16/24 losers (67%)
- **Final: n=131  W=123/L=8  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=171  W=153/L=18  WR=89.5%
- Refine: exclude RSI=RSI3 drops 5/18 losers (28%)
- **Final: n=158  W=145/L=13  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=167  W=144/L=23  WR=86.2%
- Refine: exclude T4=T4c drops 12/23 losers (52%)
- **Final: n=123  W=112/L=11  WR=91.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=152  W=134/L=18  WR=88.2%
- Refine: exclude RSI=RSI4 drops 13/18 losers (72%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W09.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=147  W=125/L=22  WR=85.0%
- Refine: exclude RSI=RSI4 drops 11/22 losers (50%)
- **Final: n=123  W=112/L=11  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W10.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=147  W=125/L=22  WR=85.0%
- Refine: exclude RSI=RSI4 drops 11/22 losers (50%)
- **Final: n=123  W=112/L=11  WR=91.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=146  W=129/L=17  WR=88.4%
- Refine: exclude RSI=RSI4 drops 13/17 losers (76%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W12.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=146  W=129/L=17  WR=88.4%
- Refine: exclude RSI=RSI4 drops 13/17 losers (76%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W13.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude RSI=RSI4 drops 9/20 losers (45%)
- **Final: n=123  W=112/L=11  WR=91.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W14.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W15.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W16.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W17.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W22.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W23.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W24.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=133  W=120/L=13  WR=90.2%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=110  W=105/L=5  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W25.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=133  W=120/L=13  WR=90.2%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=110  W=105/L=5  WR=95.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=243  W=97/L=146  WR=39.9%
- Sharpen: sharpest is T4=T4c (112/146 of losers there)
- **Sharp: n=147  W=35/L=112  WR=23.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=231  W=89/L=142  WR=38.5%
- Sharpen: sharpest is direction_exec=long (112/142 of losers there)
- **Sharp: n=147  W=35/L=112  WR=23.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when long

### L03.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=200  W=79/L=121  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=79/L=121  WR=39.5%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral

### L04.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=199  W=58/L=141  WR=29.1%
- Sharpen: sharpest is H20=H20a (112/141 of losers there)
- **Sharp: n=138  W=26/L=112  WR=18.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L05.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=191  W=61/L=130  WR=31.9%
- Sharpen: sharpest is T1=T1a (112/130 of losers there)
- **Sharp: n=147  W=35/L=112  WR=23.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=190  W=61/L=129  WR=32.1%
- Sharpen: sharpest is T1=T1a (111/129 of losers there)
- **Sharp: n=146  W=35/L=111  WR=24.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L07.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=181  W=65/L=116  WR=35.9%
- Sharpen: sharpest is H60=H60e (100/116 of losers there)
- **Sharp: n=144  W=44/L=100  WR=30.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L08.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=181  W=66/L=115  WR=36.5%
- Sharpen: sharpest is T1=T1c (106/115 of losers there)
- **Sharp: n=128  W=22/L=106  WR=17.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L09.  `H20=H20a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=181  W=66/L=115  WR=36.5%
- Sharpen: sharpest is T1=T1c (106/115 of losers there)
- **Sharp: n=128  W=22/L=106  WR=17.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=178  W=71/L=107  WR=39.9%
- Sharpen: sharpest is T4=T4c (66/107 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=178  W=71/L=107  WR=39.9%
- Sharpen: sharpest is T4=T4c (66/107 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: LONG**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is T1=T1c (96/109 of losers there)
- **Sharp: n=121  W=25/L=96  WR=20.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L13.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is T1=T1c (96/109 of losers there)
- **Sharp: n=121  W=25/L=96  WR=20.7%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L14.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is T1=T1c (96/109 of losers there)
- **Sharp: n=121  W=25/L=96  WR=20.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60a AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is T1=T1c (96/109 of losers there)
- **Sharp: n=121  W=25/L=96  WR=20.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L16.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is T1=T1c (96/109 of losers there)
- **Sharp: n=121  W=25/L=96  WR=20.7%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L17.  `H20=H20a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=171  W=59/L=112  WR=34.5%
- Sharpen: sharpest is T1=T1c (100/112 of losers there)
- **Sharp: n=126  W=26/L=100  WR=20.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L18.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=171  W=59/L=112  WR=34.5%
- Sharpen: sharpest is T1=T1c (100/112 of losers there)
- **Sharp: n=126  W=26/L=100  WR=20.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L19.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=170  W=55/L=115  WR=32.4%
- Sharpen: sharpest is H20=H20a (103/115 of losers there)
- **Sharp: n=129  W=26/L=103  WR=20.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=163  W=49/L=114  WR=30.1%
- Sharpen: sharpest is RSI=RSI5 (47/114 of losers there)
- **Sharp: n=47  W=0/L=47  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L21.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=163  W=49/L=114  WR=30.1%
- Sharpen: sharpest is RSI=RSI5 (47/114 of losers there)
- **Sharp: n=47  W=0/L=47  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L22.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=163  W=55/L=108  WR=33.7%
- Sharpen: sharpest is T4=T4c (69/108 of losers there)
- **Sharp: n=88  W=19/L=69  WR=21.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=162  W=57/L=105  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (48/105 of losers there)
- **Sharp: n=48  W=0/L=48  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

### L24.  `T4=T4a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=162  W=57/L=105  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (48/105 of losers there)
- **Sharp: n=48  W=0/L=48  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; session=ny_mid  •  ONLY when RSI 60-70 strong

### L25.  `BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=162  W=63/L=99  WR=38.9%
- Sharpen: sharpest is T4=T4c (64/99 of losers there)
- **Sharp: n=87  W=23/L=64  WR=26.4%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(53/46) | H60e(44/51) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/48) | long(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
