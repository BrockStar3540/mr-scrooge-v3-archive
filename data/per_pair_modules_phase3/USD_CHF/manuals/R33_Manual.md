# USD_CHF — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,020**  (W=1,272 / L=748)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=605  W=367/L=238  WR=60.7%
- ny_close: n=373  W=241/L=132  WR=64.6%
- asia: n=355  W=221/L=134  WR=62.3%
- london_open: n=272  W=177/L=95  WR=65.1%
- ny_open: n=177  W=107/L=70  WR=60.5%
- london: n=159  W=112/L=47  WR=70.4%
- off_hours: n=67  W=37/L=30  WR=55.2%
- asia_late: n=12  W=10/L=2  WR=83.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=142  W=122/L=20  WR=85.9%
- Refine: exclude RSI=RSI2 drops 12/20 losers (60%)
- **Final: n=114  W=106/L=8  WR=93.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  AVOID when RSI 30-40 weak

### W02.  `H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=120  W=107/L=13  WR=89.2%
- Refine: exclude ZS=ZS1 drops 6/13 losers (46%)
- **Final: n=114  W=107/L=7  WR=93.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W03.  `T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude H60=H60c drops 10/16 losers (62%)
- **Final: n=105  W=99/L=6  WR=94.3%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_close  •  AVOID when HTF60 neutral

### W04.  `T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=118  W=106/L=12  WR=89.8%
- Refine: exclude RSI=RSI3 drops 8/12 losers (67%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60c AND T4=T4c AND RSI=RSI4`
- Raw: n=106  W=95/L=11  WR=89.6%
- Refine: exclude session_bucket=ny_mid drops 11/11 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W06.  `T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude RSI=RSI3 drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W07.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude RSI=RSI3 drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W08.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude ZS=ZS1 drops 6/13 losers (46%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `T1=T1a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude RSI=RSI2 drops 12/13 losers (92%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_close  •  AVOID when RSI 30-40 weak

### W10.  `H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=89  W=83/L=6  WR=93.3%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W11.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=89  W=83/L=6  WR=93.3%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W12.  `H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS2 drops 8/12 losers (67%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london  •  AVOID when zscore -2 to -1 oversold

### W13.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude direction_exec=long drops 10/12 losers (83%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when long

### W14.  `H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude session_bucket=ny_mid drops 5/7 losers (71%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W15.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude session_bucket=ny_mid drops 5/7 losers (71%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W16.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when 1h trend WITH trade

### W17.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude ZS=ZS1 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W18.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude ZS=ZS1 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `T1=T1a AND T4=T4c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W20.  `H20=H20e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third  •  AVOID when session=asia

### W21.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude BBP=BBP1 drops 5/7 losers (71%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when just touched lower band

### W22.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude BBP=BBP1 drops 5/7 losers (71%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_close  •  AVOID when just touched lower band

### W23.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude BBP=BBP2 drops 5/10 losers (50%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when lower third

### W24.  `H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=170  W=65/L=105  WR=38.2%
- Sharpen: sharpest is BBP=BBP4 (32/105 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when upper third

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is T4=T4a (40/76 of losers there)
- **Sharp: n=56  W=16/L=40  WR=28.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=109  W=32/L=77  WR=29.4%
- Sharpen: sharpest is H60=H60c (35/77 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 neutral

### L04.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is T1=T1a (31/64 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  ONLY when 1h trend WITH trade

### L05.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_close (31/67 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=ny_close

### L06.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=36/L=63  WR=36.4%
- Sharpen: sharpest is BBP=BBP4 (18/63 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when upper third

### L07.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H20=H20d (26/58 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 mildly against

### L08.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=92  W=27/L=65  WR=29.3%
- Sharpen: sharpest is ZS=ZS4 (20/65 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L09.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=92  W=30/L=62  WR=32.6%
- Sharpen: sharpest is BBP=BBP4 (17/62 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when upper third

### L10.  `H20=H20a AND H60=H60c AND T4=T4a`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (35/54 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L11.  `H60=H60c AND T4=T4a AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (35/54 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20a AND H60=H60c AND T4=T4a AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (35/54 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L13.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is H20=H20a (27/56 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L14.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is BBP=BBP4 (20/56 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when upper third

### L15.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is BBP=BBP4 (17/59 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  ONLY when upper third

### L16.  `H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=86  W=26/L=60  WR=30.2%
- Sharpen: sharpest is BBP=BBP4 (18/60 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_close  •  ONLY when upper third

### L17.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is ZS=ZS4 (20/59 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L18.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=29/L=54  WR=34.9%
- Sharpen: sharpest is T4=T4a (25/54 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when 4h trend WITH trade

### L19.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=81  W=27/L=54  WR=33.3%
- Sharpen: sharpest is BBP=BBP4 (16/54 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when upper third

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=81  W=32/L=49  WR=39.5%
- Sharpen: sharpest is BBP=BBP4 (22/49 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L21.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is T4=T4a (22/51 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L22.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is direction_exec=long (50/50 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_close  •  ONLY when long

### L23.  `T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=77  W=20/L=57  WR=26.0%
- Sharpen: sharpest is RSI=RSI4 (36/57 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L24.  `T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (26/47 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L25.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (26/47 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(45/39) | H20a(38/45) |
| H60 | H60a(39/34) | — |
| T1 | — | — |
| T4 | T4c(53/47) | T4a(47/53) |
| BBP | — | — |
| RSI | — | RSI4(58/63) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/46) | long(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
