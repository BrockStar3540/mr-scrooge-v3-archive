# GBP_NZD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,229**  (W=3,137 / L=2,092)  -  WR: **60.0%**

## Session distribution

- asia: n=1476  W=884/L=592  WR=59.9%
- ny_mid: n=895  W=533/L=362  WR=59.6%
- ny_close: n=828  W=508/L=320  WR=61.4%
- london_open: n=535  W=340/L=195  WR=63.6%
- ny_open: n=532  W=309/L=223  WR=58.1%
- london: n=415  W=256/L=159  WR=61.7%
- off_hours: n=363  W=188/L=175  WR=51.8%
- asia_late: n=185  W=119/L=66  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=194  W=176/L=18  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 5/18 losers (28%)
- **Final: n=172  W=159/L=13  WR=92.4%**
- **Dir: SHORT**  •  middle of band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W02.  `BBP=BBP3 AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=194  W=176/L=18  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 5/18 losers (28%)
- **Final: n=172  W=159/L=13  WR=92.4%**
- **Dir: SHORT**  •  middle of band; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W03.  `T1=T1a AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=193  W=172/L=21  WR=89.1%
- Refine: exclude H20=H20e drops 11/21 losers (52%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 30-40 weak  •  AVOID when HTF20 strongly against

### W04.  `T1=T1a AND BBP=BBP3 AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=193  W=172/L=21  WR=89.1%
- Refine: exclude H20=H20e drops 11/21 losers (52%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W05.  `T1=T1a AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=190  W=172/L=18  WR=90.5%
- Refine: exclude session_bucket=ny_mid drops 5/18 losers (28%)
- **Final: n=168  W=155/L=13  WR=92.3%**
- **Dir: SHORT**  •  1h trend WITH trade; middle of band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W06.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=158  W=139/L=19  WR=88.0%
- Refine: exclude session_bucket=ny_mid drops 13/19 losers (68%)
- **Final: n=120  W=114/L=6  WR=95.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W07.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=128  W=116/L=12  WR=90.6%
- Refine: exclude session_bucket=ny_mid drops 12/12 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W08.  `H20=H20a AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=118  W=108/L=10  WR=91.5%
- Refine: exclude session_bucket=ny_mid drops 5/10 losers (50%)
- **Final: n=96  W=91/L=5  WR=94.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; middle of band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND T1=T1a AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=114  W=104/L=10  WR=91.2%
- Refine: exclude session_bucket=ny_mid drops 5/10 losers (50%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; middle of band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W10.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 5/15 losers (33%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when strategy=bravo_expansion_continuation

### W11.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band; RSI 30-40 weak  •  AVOID when HTF20 strongly against

### W12.  `T4=T4c AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude H60=H60b drops 4/10 losers (40%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band; RSI 30-40 weak  •  AVOID when HTF60 slightly aligned

### W13.  `T4=T4a AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=96  W=88/L=8  WR=91.7%
- Refine: exclude session_bucket=ny_mid drops 4/8 losers (50%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: SHORT**  •  4h trend WITH trade; middle of band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W14.  `T1=T1a AND T4=T4a AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=92  W=84/L=8  WR=91.3%
- Refine: exclude session_bucket=ny_mid drops 4/8 losers (50%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W15.  `H60=H60d AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W16.  `H60=H60d AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W17.  `H60=H60d AND T1=T1c AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W18.  `H60=H60d AND BBP=BBP1 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  HTF60 mildly against; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W19.  `H60=H60e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude session_bucket=ny_mid drops 6/11 losers (55%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W20.  `T1=T1a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude session_bucket=ny_close drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W21.  `H60=H60a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 3/12 losers (25%)
- **Final: n=82  W=73/L=9  WR=89.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_open

### W22.  `H20=H20a AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude RSI=RSI2 drops 9/11 losers (82%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when RSI 30-40 weak

### W23.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 3/12 losers (25%)
- **Final: n=78  W=69/L=9  WR=88.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_open

### W24.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude direction_exec=short drops 11/11 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when short

### W25.  `T1=T1a AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=283  W=113/L=170  WR=39.9%
- Sharpen: sharpest is T4=T4c (93/170 of losers there)
- **Sharp: n=129  W=36/L=93  WR=27.9%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L02.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=265  W=92/L=173  WR=34.7%
- Sharpen: sharpest is T4=T4c (83/173 of losers there)
- **Sharp: n=99  W=16/L=83  WR=16.2%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L03.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=249  W=91/L=158  WR=36.5%
- Sharpen: sharpest is T4=T4c (81/158 of losers there)
- **Sharp: n=97  W=16/L=81  WR=16.5%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L04.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=213  W=71/L=142  WR=33.3%
- Sharpen: sharpest is T4=T4c (59/142 of losers there)
- **Sharp: n=66  W=7/L=59  WR=10.6%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L05.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=213  W=71/L=142  WR=33.3%
- Sharpen: sharpest is T4=T4c (59/142 of losers there)
- **Sharp: n=66  W=7/L=59  WR=10.6%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L06.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=199  W=71/L=128  WR=35.7%
- Sharpen: sharpest is T4=T4c (57/128 of losers there)
- **Sharp: n=64  W=7/L=57  WR=10.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=174  W=68/L=106  WR=39.1%
- Sharpen: sharpest is T4=T4c (34/106 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L08.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=154  W=56/L=98  WR=36.4%
- Sharpen: sharpest is T4=T4c (42/98 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=154  W=58/L=96  WR=37.7%
- Sharpen: sharpest is BBP=BBP2 (27/96 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L10.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=149  W=56/L=93  WR=37.6%
- Sharpen: sharpest is T4=T4c (42/93 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L11.  `T1=T1c AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=147  W=37/L=110  WR=25.2%
- Sharpen: sharpest is H20=H20e (68/110 of losers there)
- **Sharp: n=84  W=16/L=68  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND BBP=BBP3 AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=147  W=37/L=110  WR=25.2%
- Sharpen: sharpest is H20=H20e (68/110 of losers there)
- **Sharp: n=84  W=16/L=68  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L13.  `BBP=BBP3 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=146  W=33/L=113  WR=22.6%
- Sharpen: sharpest is T4=T4c (59/113 of losers there)
- **Sharp: n=71  W=12/L=59  WR=16.9%**
- **Dir: LONG**  •  middle of band; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L14.  `BBP=BBP3 AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=146  W=33/L=113  WR=22.6%
- Sharpen: sharpest is T4=T4c (59/113 of losers there)
- **Sharp: n=71  W=12/L=59  WR=16.9%**
- **Dir: LONG**  •  middle of band; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L15.  `H20=H20e AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=145  W=56/L=89  WR=38.6%
- Sharpen: sharpest is BBP=BBP3 (71/89 of losers there)
- **Sharp: n=87  W=16/L=71  WR=18.4%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when middle of band

### L16.  `H20=H20e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is ZS=ZS4 (63/87 of losers there)
- **Sharp: n=84  W=21/L=63  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; upper third  •  ONLY when zscore +1 to +2 overbought

### L17.  `T1=T1c AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=143  W=33/L=110  WR=23.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=143  W=33/L=110  WR=23.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; middle of band; RSI 30-40 weak

### L18.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is BBP=BBP3 (68/86 of losers there)
- **Sharp: n=84  W=16/L=68  WR=19.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when middle of band

### L19.  `H20=H20e AND H60=H60a AND BBP=BBP4`
- Raw: n=136  W=50/L=86  WR=36.8%
- Sharpen: sharpest is session_bucket=off_hours (24/86 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third  •  ONLY when session=off_hours

### L20.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=129  W=36/L=93  WR=27.9%
- Sharpen: sharpest is direction_exec=short (81/93 of losers there)
- **Sharp: n=97  W=16/L=81  WR=16.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when short

### L21.  `H20=H20e AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is direction_exec=long (56/81 of losers there)
- **Sharp: n=76  W=20/L=56  WR=26.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when long

### L22.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is direction_exec=long (56/81 of losers there)
- **Sharp: n=76  W=20/L=56  WR=26.3%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when long

### L23.  `T4=T4c AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is BBP=BBP3 (59/78 of losers there)
- **Sharp: n=71  W=12/L=59  WR=16.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when middle of band

### L24.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is H60=H60a (36/78 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when HTF60 aligned WITH trade

### L25.  `T1=T1a AND BBP=BBP2 AND ZS=ZS3`
- Raw: n=123  W=48/L=75  WR=39.0%
- Sharpen: sharpest is H60=H60e (39/75 of losers there)
- **Sharp: n=56  W=17/L=39  WR=30.4%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

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
