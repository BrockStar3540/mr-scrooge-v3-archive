# NZD_USD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,588**  (W=2,264 / L=1,324)  -  WR: **63.1%**

## Session distribution

- ny_mid: n=916  W=576/L=340  WR=62.9%
- asia: n=759  W=485/L=274  WR=63.9%
- london_open: n=719  W=454/L=265  WR=63.1%
- ny_open: n=440  W=277/L=163  WR=63.0%
- ny_close: n=317  W=203/L=114  WR=64.0%
- london: n=268  W=163/L=105  WR=60.8%
- off_hours: n=94  W=56/L=38  WR=59.6%
- asia_late: n=75  W=50/L=25  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=167  W=145/L=22  WR=86.8%
- Refine: exclude T4=T4c drops 19/22 losers (86%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when 4h trend AGAINST trade

### W02.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=158  W=136/L=22  WR=86.1%
- Refine: exclude session_bucket=asia drops 9/22 losers (41%)
- **Final: n=121  W=108/L=13  WR=89.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W03.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=129  W=113/L=16  WR=87.6%
- Refine: exclude ZS=ZS5 drops 11/16 losers (69%)
- **Final: n=96  W=91/L=5  WR=94.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W04.  `T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude H60=H60c drops 6/18 losers (33%)
- **Final: n=115  W=103/L=12  WR=89.6%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london_open  •  AVOID when HTF60 neutral

### W05.  `T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H60=H60c drops 6/17 losers (35%)
- **Final: n=109  W=98/L=11  WR=89.9%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 neutral

### W06.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H60=H60c drops 6/17 losers (35%)
- **Final: n=109  W=98/L=11  WR=89.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 neutral

### W07.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude H60=H60e drops 7/17 losers (41%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W08.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude H60=H60e drops 8/17 losers (47%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W09.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude H60=H60c drops 6/13 losers (46%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF60 neutral

### W10.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude T1=T1a drops 7/8 losers (88%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend WITH trade

### W11.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude RSI=RSI5 drops 4/14 losers (29%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W12.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=97  W=87/L=10  WR=89.7%
- Refine: exclude BBP=BBP6 drops 8/10 losers (80%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when deep above upper band

### W13.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude H60=H60c drops 6/13 losers (46%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 neutral

### W14.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude T4=T4c drops 11/12 losers (92%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when 4h trend AGAINST trade

### W15.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=87  W=84/L=3  WR=96.6%
- Refine: exclude BBP=BBP4 drops 3/3 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  AVOID when upper third

### W17.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude T4=T4a drops 7/13 losers (54%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W18.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=london_open drops 7/12 losers (58%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W19.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude T1=T1a drops 7/8 losers (88%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  AVOID when 1h trend WITH trade

### W20.  `H20=H20a AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude BBP=BBP6 drops 8/9 losers (89%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when deep above upper band

### W21.  `H60=H60a AND T4=T4a AND BBP=BBP5`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T1=T1c drops 6/11 losers (55%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when 1h trend AGAINST trade

### W22.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W23.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T1=T1c drops 6/11 losers (55%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W24.  `H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=79  W=74/L=5  WR=93.7%
- Refine: exclude BBP=BBP2 drops 5/5 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade  •  AVOID when lower third

### W25.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude BBP=BBP2 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=165  W=65/L=100  WR=39.4%
- Sharpen: sharpest is H20=H20e (60/100 of losers there)
- **Sharp: n=87  W=27/L=60  WR=31.0%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L02.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=152  W=51/L=101  WR=33.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=152  W=51/L=101  WR=33.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade

### L03.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=134  W=49/L=85  WR=36.6%
- Sharpen: sharpest is H60=H60a (65/85 of losers there)
- **Sharp: n=91  W=26/L=65  WR=28.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L04.  `H20=H20e AND H60=H60a AND session_bucket=london_open`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is T1=T1a (35/73 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london_open  •  ONLY when 1h trend WITH trade

### L05.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is H60=H60a (35/71 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L06.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is T1=T1a (37/69 of losers there)
- **Sharp: n=51  W=14/L=37  WR=27.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 1h trend WITH trade

### L07.  `BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (20/65 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L08.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is ZS=ZS5 (20/64 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is session_bucket=ny_mid (22/62 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L10.  `H20=H20e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is T1=T1c (36/62 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band  •  ONLY when 1h trend AGAINST trade

### L11.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=96  W=36/L=60  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (55/60 of losers there)
- **Sharp: n=79  W=24/L=55  WR=30.4%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L12.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60e (24/54 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L13.  `T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is H20=H20a (26/54 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=88  W=23/L=65  WR=26.1%
- Sharpen: sharpest is H20=H20e (35/65 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when HTF20 strongly against

### L15.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (21/54 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=87  W=27/L=60  WR=31.0%
- Sharpen: sharpest is T1=T1c (36/60 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L17.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=83  W=31/L=52  WR=37.3%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; session=ny_mid

### L18.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is direction_exec=short (18/51 of losers there)
- **Sharp: n=23  W=5/L=18  WR=21.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when short

### L19.  `H20=H20e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=79  W=24/L=55  WR=30.4%
- Sharpen: sharpest is session_bucket=ny_close (16/55 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L20.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is H60=H60a (11/52 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L21.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=77  W=27/L=50  WR=35.1%
- Sharpen: sharpest is session_bucket=london (16/50 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=76  W=21/L=55  WR=27.6%
- Sharpen: sharpest is BBP=BBP4 (22/55 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when upper third

### L23.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is T1=T1c (29/48 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20e AND H60=H60a AND T4=T4c AND ZS=ZS3`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (27/45 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=74  W=26/L=48  WR=35.1%
- Sharpen: sharpest is T1=T1c (21/48 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

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
| direction_exec | short(54/44) | long(46/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
