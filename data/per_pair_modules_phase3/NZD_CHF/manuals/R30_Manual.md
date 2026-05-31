# NZD_CHF — R30 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **975**  (W=650 / L=325)  -  WR: **66.7%**

## Session distribution

- ny_mid: n=317  W=210/L=107  WR=66.2%
- asia: n=271  W=188/L=83  WR=69.4%
- london_open: n=154  W=111/L=43  WR=72.1%
- london: n=76  W=49/L=27  WR=64.5%
- ny_close: n=58  W=33/L=25  WR=56.9%
- ny_open: n=49  W=27/L=22  WR=55.1%
- off_hours: n=32  W=21/L=11  WR=65.6%
- asia_late: n=18  W=11/L=7  WR=61.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W02.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W04.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: no further refinement
- **Final: n=94  W=81/L=13  WR=86.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid

### W05.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: no further refinement
- **Final: n=94  W=81/L=13  WR=86.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid

### W06.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W07.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude BBP=BBP2 drops 8/9 losers (89%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude BBP=BBP2 drops 8/9 losers (89%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W09.  `T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude BBP=BBP2 drops 6/9 losers (67%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W10.  `H60=H60b AND T1=T1c AND direction_exec=long`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude BBP=BBP2 drops 6/11 losers (55%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade  •  AVOID when lower third

### W11.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude ZS=ZS1 drops 6/10 losers (60%)
- **Final: n=44  W=40/L=4  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W12.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude ZS=ZS1 drops 6/10 losers (60%)
- **Final: n=44  W=40/L=4  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W13.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS1 drops 5/9 losers (56%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W16.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude ZS=ZS1 drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -3 to -2 deep oversold

### W17.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude ZS=ZS1 drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -3 to -2 deep oversold

### W18.  `H60=H60b AND RSI=RSI3 AND direction_exec=long`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude session_bucket=ny_mid drops 5/5 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W19.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60b AND T4=T4c AND direction_exec=long`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20e AND T1=T1a AND ZS=ZS1`
- Raw: n=60  W=53/L=7  WR=88.3%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W22.  `H20=H20a AND H60=H60c AND T1=T1a`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

### W23.  `H20=H20a AND H60=H60c AND direction_exec=short`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral  •  AVOID when 4h trend WITH trade

### W24.  `H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20a AND H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is T4=T4c (23/36 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L02.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is T4=T4c (23/36 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L03.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is T4=T4c (23/36 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is T4=T4c (31/35 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is T4=T4c (31/35 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20e (31/34 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L07.  `H20=H20a AND T1=T1c AND ZS=ZS1`
- Raw: n=50  W=16/L=34  WR=32.0%
- Sharpen: sharpest is session_bucket=london_open (14/34 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L08.  `H20=H20e AND H60=H60c AND T1=T1c`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is T4=T4a (24/31 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when 4h trend WITH trade

### L09.  `H20=H20e AND H60=H60c AND direction_exec=long`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is T4=T4a (24/31 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral  •  ONLY when 4h trend WITH trade

### L10.  `H20=H20e AND H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is T4=T4a (24/31 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when 4h trend WITH trade

### L11.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (14/30 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is H60=H60e (21/30 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L13.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is H60=H60e (21/30 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L14.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is T4=T4c (20/29 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L15.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=46  W=16/L=30  WR=34.8%
- Sharpen: sharpest is H60=H60e (21/30 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L16.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H60=H60e (14/28 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H60=H60e (14/28 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=44  W=12/L=32  WR=27.3%
- Sharpen: sharpest is ZS=ZS1 (14/32 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H20=H20a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is RSI=RSI2 (17/28 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20a AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is RSI=RSI2 (17/28 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L21.  `H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is RSI=RSI3 (15/26 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L22.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (9/26 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L23.  `H60=H60c AND T1=T1c AND T4=T4a`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is H20=H20e (24/25 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L24.  `H60=H60c AND T4=T4a AND direction_exec=long`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is H20=H20e (24/25 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L25.  `H60=H60c AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is H20=H20e (24/25 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(34/41) |
| H60 | H60b(15/4) | H60d(6/13) |
| T1 | T1a(55/43) | T1c(45/57) |
| T4 | — | — |
| BBP | — | — |
| RSI | RSI3(51/46) | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/45) | long(48/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
