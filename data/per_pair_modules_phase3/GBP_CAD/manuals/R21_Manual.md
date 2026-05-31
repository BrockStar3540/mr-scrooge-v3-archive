# GBP_CAD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,602**  (W=2,250 / L=1,352)  -  WR: **62.5%**

## Session distribution

- asia: n=1194  W=754/L=440  WR=63.1%
- ny_close: n=868  W=548/L=320  WR=63.1%
- london_open: n=440  W=268/L=172  WR=60.9%
- london: n=358  W=219/L=139  WR=61.2%
- asia_late: n=256  W=161/L=95  WR=62.9%
- ny_open: n=251  W=155/L=96  WR=61.8%
- off_hours: n=195  W=123/L=72  WR=63.1%
- ny_mid: n=40  W=22/L=18  WR=55.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude ZS=ZS3 drops 7/16 losers (44%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W02.  `H60=H60e AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude ZS=ZS3 drops 7/16 losers (44%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W03.  `H20=H20b AND T1=T1c AND RSI=RSI3`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude direction_exec=short drops 10/14 losers (71%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when short

### W04.  `T1=T1c AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=115  W=103/L=12  WR=89.6%
- Refine: exclude H20=H20a drops 10/12 losers (83%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W05.  `ZS=ZS1 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=114  W=105/L=9  WR=92.1%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when just touched lower band

### W06.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=112  W=103/L=9  WR=92.0%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when just touched lower band

### W07.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude BBP=BBP3 drops 6/13 losers (46%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when middle of band

### W08.  `H20=H20a AND H60=H60e AND RSI=RSI3`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude ZS=ZS5 drops 9/15 losers (60%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when zscore +2 to +3 deep overbought

### W09.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude ZS=ZS5 drops 9/15 losers (60%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when zscore +2 to +3 deep overbought

### W10.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude session_bucket=ny_close drops 6/11 losers (55%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W11.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude BBP=BBP3 drops 6/13 losers (46%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when middle of band

### W12.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude RSI=RSI2 drops 12/13 losers (92%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=ny_close  •  AVOID when RSI 30-40 weak

### W13.  `H20=H20b AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude direction_exec=short drops 10/14 losers (71%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when short

### W14.  `H20=H20a AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W15.  `H60=H60e AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=92  W=90/L=2  WR=97.8%
- Refine: exclude H20=H20d drops 2/2 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when HTF20 mildly against

### W16.  `H60=H60e AND T1=T1c AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=92  W=90/L=2  WR=97.8%
- Refine: exclude H20=H20d drops 2/2 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when HTF20 mildly against

### W17.  `H60=H60e AND ZS=ZS1 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=92  W=90/L=2  WR=97.8%
- Refine: exclude H20=H20d drops 2/2 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when HTF20 mildly against

### W18.  `H20=H20b AND RSI=RSI3 AND direction_exec=long`
- Raw: n=92  W=88/L=4  WR=95.7%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 40-50 lower neutral  •  AVOID when middle of band

### W19.  `H20=H20b AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=92  W=88/L=4  WR=95.7%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when middle of band

### W20.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude RSI=RSI2 drops 12/13 losers (92%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; session=ny_close  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20b AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude BBP=BBP0 drops 9/12 losers (75%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W22.  `H20=H20b AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude BBP=BBP0 drops 9/12 losers (75%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W23.  `H20=H20b AND T4=T4c AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H60=H60d drops 9/13 losers (69%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 mildly against

### W24.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 strongly against

### W25.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=176  W=67/L=109  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (48/109 of losers there)
- **Sharp: n=61  W=13/L=48  WR=21.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when lower third

### L02.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=176  W=67/L=109  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (48/109 of losers there)
- **Sharp: n=61  W=13/L=48  WR=21.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when lower third

### L03.  `H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: sharpest is ZS=ZS1 (23/112 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=151  W=55/L=96  WR=36.4%
- Sharpen: sharpest is ZS=ZS1 (23/96 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is BBP=BBP1 (20/76 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when just touched lower band

### L06.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=123  W=38/L=85  WR=30.9%
- Sharpen: sharpest is ZS=ZS1 (23/85 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is BBP=BBP1 (20/73 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when just touched lower band

### L08.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is BBP=BBP1 (20/73 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when just touched lower band

### L09.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is BBP=BBP1 (20/73 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when just touched lower band

### L10.  `T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=118  W=46/L=72  WR=39.0%
- Sharpen: sharpest is H20=H20a (24/72 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L11.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L12.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=111  W=39/L=72  WR=35.1%
- Sharpen: sharpest is H60=H60a (54/72 of losers there)
- **Sharp: n=72  W=18/L=54  WR=25.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L13.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is H20=H20a (35/74 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L14.  `T1=T1a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=108  W=34/L=74  WR=31.5%
- Sharpen: sharpest is T4=T4c (32/74 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60a AND T1=T1a AND session_bucket=london`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is BBP=BBP2 (24/66 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  ONLY when lower third

### L16.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is H20=H20a (35/67 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L17.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H60=H60a (54/64 of losers there)
- **Sharp: n=72  W=18/L=54  WR=25.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L18.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is T1=T1a (31/63 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak; session=ny_close  •  ONLY when 1h trend WITH trade

### L19.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is H60=H60a (48/60 of losers there)
- **Sharp: n=69  W=21/L=48  WR=30.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 aligned WITH trade

### L20.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is H20=H20a (33/59 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is H20=H20a (33/59 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L22.  `T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=97  W=33/L=64  WR=34.0%
- Sharpen: sharpest is BBP=BBP2 (19/64 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L23.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is BBP=BBP2 (31/62 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when lower third

### L24.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is BBP=BBP2 (31/62 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when lower third

### L25.  `T1=T1a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=96  W=28/L=68  WR=29.2%
- Sharpen: sharpest is T4=T4c (29/68 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(41/30) | H60a(30/42) |
| T1 | T1c(53/47) | T1a(47/53) |
| T4 | T4c(53/46) | T4a(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
