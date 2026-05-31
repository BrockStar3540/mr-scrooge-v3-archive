# GBP_JPY — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,531**  (W=1,458 / L=1,073)  -  WR: **57.6%**

## Session distribution

- ny_mid: n=696  W=410/L=286  WR=58.9%
- asia: n=552  W=325/L=227  WR=58.9%
- london_open: n=497  W=287/L=210  WR=57.7%
- ny_open: n=326  W=173/L=153  WR=53.1%
- london: n=162  W=96/L=66  WR=59.3%
- asia_late: n=116  W=67/L=49  WR=57.8%
- off_hours: n=111  W=60/L=51  WR=54.1%
- ny_close: n=71  W=40/L=31  WR=56.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude session_bucket=london drops 4/15 losers (27%)
- **Final: n=103  W=92/L=11  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london

### W02.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude session_bucket=london drops 4/15 losers (27%)
- **Final: n=103  W=92/L=11  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london

### W03.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude session_bucket=london drops 4/15 losers (27%)
- **Final: n=103  W=92/L=11  WR=89.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london

### W04.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=london drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london

### W05.  `T4=T4a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude RSI=RSI3 drops 13/13 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W06.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP1 drops 6/11 losers (55%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when just touched lower band

### W08.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP1 drops 6/11 losers (55%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  AVOID when just touched lower band

### W09.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP1 drops 6/11 losers (55%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when just touched lower band

### W10.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude ZS=ZS3 drops 9/10 losers (90%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude ZS=ZS3 drops 9/10 losers (90%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60e AND RSI=RSI2 AND session_bucket=london`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W13.  `T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W14.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W15.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W16.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W17.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=london`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20e AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; session=london  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20a AND H60=H60e AND RSI=RSI2`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W22.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W23.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W24.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI2`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W25.  `H20=H20a AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=225  W=88/L=137  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=88/L=137  WR=39.1%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open

### L02.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=209  W=82/L=127  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (53/127 of losers there)
- **Sharp: n=74  W=21/L=53  WR=28.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L03.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=209  W=82/L=127  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (53/127 of losers there)
- **Sharp: n=74  W=21/L=53  WR=28.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L04.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=205  W=81/L=124  WR=39.5%
- Sharpen: sharpest is T4=T4c (78/124 of losers there)
- **Sharp: n=112  W=34/L=78  WR=30.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L05.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=205  W=81/L=124  WR=39.5%
- Sharpen: sharpest is T4=T4c (82/124 of losers there)
- **Sharp: n=116  W=34/L=82  WR=29.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L06.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=205  W=81/L=124  WR=39.5%
- Sharpen: sharpest is T4=T4c (82/124 of losers there)
- **Sharp: n=116  W=34/L=82  WR=29.3%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L07.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=205  W=81/L=124  WR=39.5%
- Sharpen: sharpest is T4=T4c (82/124 of losers there)
- **Sharp: n=116  W=34/L=82  WR=29.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L08.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=171  W=61/L=110  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_mid (41/110 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L09.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=164  W=65/L=99  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (38/99 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (18/76 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L11.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is RSI=RSI2 (56/73 of losers there)
- **Sharp: n=62  W=6/L=56  WR=9.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20e AND H60=H60a AND direction_exec=long`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is RSI=RSI2 (56/73 of losers there)
- **Sharp: n=62  W=6/L=56  WR=9.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when RSI 30-40 weak

### L13.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is RSI=RSI2 (56/73 of losers there)
- **Sharp: n=62  W=6/L=56  WR=9.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L14.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is RSI=RSI2 (56/73 of losers there)
- **Sharp: n=62  W=6/L=56  WR=9.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L15.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=116  W=34/L=82  WR=29.3%
- Sharpen: sharpest is session_bucket=ny_mid (30/82 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L16.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=116  W=34/L=82  WR=29.3%
- Sharpen: sharpest is session_bucket=ny_mid (30/82 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L17.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=112  W=34/L=78  WR=30.4%
- Sharpen: sharpest is session_bucket=ny_mid (30/78 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L18.  `H20=H20e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is T4=T4a (61/67 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is ZS=ZS2 (46/65 of losers there)
- **Sharp: n=63  W=17/L=46  WR=27.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L20.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is ZS=ZS2 (46/65 of losers there)
- **Sharp: n=63  W=17/L=46  WR=27.0%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L21.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=105  W=35/L=70  WR=33.3%
- Sharpen: sharpest is BBP=BBP1 (19/70 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L22.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=105  W=35/L=70  WR=33.3%
- Sharpen: sharpest is BBP=BBP1 (19/70 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L23.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=105  W=35/L=70  WR=33.3%
- Sharpen: sharpest is BBP=BBP1 (19/70 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L24.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is ZS=ZS1 (41/66 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=30/L=69  WR=30.3%
- Sharpen: sharpest is RSI=RSI2 (47/69 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
