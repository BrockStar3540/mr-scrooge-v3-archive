# USD_CAD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,848**  (W=1,173 / L=675)  -  WR: **63.5%**

## Session distribution

- ny_mid: n=517  W=335/L=182  WR=64.8%
- ny_open: n=496  W=306/L=190  WR=61.7%
- london_open: n=289  W=187/L=102  WR=64.7%
- london: n=241  W=144/L=97  WR=59.8%
- ny_close: n=189  W=122/L=67  WR=64.6%
- asia: n=68  W=46/L=22  WR=67.6%
- asia_late: n=35  W=23/L=12  WR=65.7%
- off_hours: n=13  W=10/L=3  WR=76.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=226  W=194/L=32  WR=85.8%
- Refine: exclude T1=T1a drops 21/32 losers (66%)
- **Final: n=122  W=111/L=11  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W02.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude ZS=ZS3 drops 9/24 losers (38%)
- **Final: n=154  W=139/L=15  WR=90.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W03.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=169  W=145/L=24  WR=85.8%
- Refine: exclude H20=H20a drops 19/24 losers (79%)
- **Final: n=140  W=135/L=5  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=149  W=135/L=14  WR=90.6%
- Refine: exclude BBP=BBP3 drops 7/14 losers (50%)
- **Final: n=136  W=129/L=7  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when middle of band

### W05.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=148  W=130/L=18  WR=87.8%
- Refine: exclude ZS=ZS3 drops 9/18 losers (50%)
- **Final: n=125  W=116/L=9  WR=92.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=139  W=127/L=12  WR=91.4%
- Refine: exclude H60=H60d drops 7/12 losers (58%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 mildly against

### W07.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/18 losers (56%)
- **Final: n=120  W=112/L=8  WR=93.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=138  W=121/L=17  WR=87.7%
- Refine: exclude ZS=ZS4 drops 8/17 losers (47%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +1 to +2 overbought

### W09.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=136  W=116/L=20  WR=85.3%
- Refine: exclude T4=T4c drops 15/20 losers (75%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W10.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=129  W=114/L=15  WR=88.4%
- Refine: exclude T1=T1a drops 10/15 losers (67%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W11.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=127  W=113/L=14  WR=89.0%
- Refine: exclude ZS=ZS2 drops 12/14 losers (86%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W12.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=126  W=112/L=14  WR=88.9%
- Refine: exclude BBP=BBP3 drops 7/14 losers (50%)
- **Final: n=113  W=106/L=7  WR=93.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when middle of band

### W13.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude session_bucket=london_open drops 5/11 losers (45%)
- **Final: n=116  W=110/L=6  WR=94.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=london_open

### W14.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=122  W=111/L=11  WR=91.0%
- Refine: exclude BBP=BBP3 drops 5/11 losers (45%)
- **Final: n=113  W=107/L=6  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when middle of band

### W15.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=121  W=110/L=11  WR=90.9%
- Refine: exclude session_bucket=london_open drops 5/11 losers (45%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W16.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude T1=T1a drops 9/14 losers (64%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W17.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=114  W=105/L=9  WR=92.1%
- Refine: exclude ZS=ZS2 drops 7/9 losers (78%)
- **Final: n=91  W=89/L=2  WR=97.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W18.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=86  W=84/L=2  WR=97.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when lower third

### W20.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude T1=T1a drops 10/15 losers (67%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W21.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=98  W=91/L=7  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W22.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude T1=T1a drops 9/14 losers (64%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W23.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=98  W=89/L=9  WR=90.8%
- Refine: exclude H20=H20a drops 5/9 losers (56%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W24.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude direction_exec=long drops 8/13 losers (62%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when long

### W25.  `H20=H20e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=97  W=91/L=6  WR=93.8%
- Refine: exclude H60=H60b drops 5/6 losers (83%)
- **Final: n=92  W=91/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=261  W=102/L=159  WR=39.1%
- Sharpen: sharpest is H20=H20a (64/159 of losers there)
- **Sharp: n=84  W=20/L=64  WR=23.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=247  W=97/L=150  WR=39.3%
- Sharpen: sharpest is BBP=BBP2 (64/150 of losers there)
- **Sharp: n=85  W=21/L=64  WR=24.7%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when lower third

### L03.  `H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=173  W=58/L=115  WR=33.5%
- Sharpen: sharpest is session_bucket=london (41/115 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L04.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: sharpest is BBP=BBP2 (47/109 of losers there)
- **Sharp: n=59  W=12/L=47  WR=20.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when lower third

### L05.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=150  W=58/L=92  WR=38.7%
- Sharpen: sharpest is H60=H60e (64/92 of losers there)
- **Sharp: n=85  W=21/L=64  WR=24.7%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=145  W=51/L=94  WR=35.2%
- Sharpen: sharpest is BBP=BBP2 (45/94 of losers there)
- **Sharp: n=56  W=11/L=45  WR=19.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L07.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: sharpest is ZS=ZS4 (18/82 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L08.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=130  W=51/L=79  WR=39.2%
- Sharpen: sharpest is T1=T1c (57/79 of losers there)
- **Sharp: n=74  W=17/L=57  WR=23.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L09.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is H20=H20a (50/80 of losers there)
- **Sharp: n=54  W=4/L=50  WR=7.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L10.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=122  W=39/L=83  WR=32.0%
- Sharpen: sharpest is BBP=BBP2 (39/83 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L11.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (40/74 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L12.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is direction_exec=long (64/73 of losers there)
- **Sharp: n=85  W=21/L=64  WR=24.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when long

### L13.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is H60=H60a (46/71 of losers there)
- **Sharp: n=61  W=15/L=46  WR=24.6%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L14.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=115  W=44/L=71  WR=38.3%
- Sharpen: sharpest is H60=H60a (40/71 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L15.  `H60=H60e AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=114  W=38/L=76  WR=33.3%
- Sharpen: sharpest is H20=H20e (28/76 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is RSI=RSI3 (64/70 of losers there)
- **Sharp: n=85  W=21/L=64  WR=24.7%**
- **Dir: LONG**  •  HTF60 strongly against; lower third  •  ONLY when RSI 40-50 lower neutral

### L17.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (27/67 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L18.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=103  W=35/L=68  WR=34.0%
- Sharpen: sharpest is ZS=ZS1 (23/68 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H60=H60e AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is H20=H20e (26/66 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when HTF20 strongly against

### L20.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is direction_exec=long (55/64 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when long

### L21.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is direction_exec=long (55/64 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when long

### L22.  `H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is session_bucket=london (26/71 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=london

### L23.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=99  W=30/L=69  WR=30.3%
- Sharpen: sharpest is direction_exec=short (24/69 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when short

### L24.  `H60=H60e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is RSI=RSI3 (55/60 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L25.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is RSI=RSI3 (55/60 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(37/31) | H60e(31/38) |
| T1 | — | — |
| T4 | T4a(60/39) | T4c(40/61) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/46) | long(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
