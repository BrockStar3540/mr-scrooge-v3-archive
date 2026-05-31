# GBP_JPY — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,796**  (W=2,210 / L=1,586)  -  WR: **58.2%**

## Session distribution

- asia: n=1579  W=914/L=665  WR=57.9%
- ny_close: n=1147  W=682/L=465  WR=59.5%
- ny_mid: n=335  W=197/L=138  WR=58.8%
- off_hours: n=266  W=143/L=123  WR=53.8%
- ny_open: n=211  W=128/L=83  WR=60.7%
- london: n=177  W=98/L=79  WR=55.4%
- london_open: n=64  W=40/L=24  WR=62.5%
- asia_late: n=17  W=8/L=9  WR=47.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude RSI=RSI2 drops 8/24 losers (33%)
- **Final: n=155  W=139/L=16  WR=89.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 30-40 weak

### W02.  `T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude RSI=RSI2 drops 8/15 losers (53%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; session=asia  •  AVOID when RSI 30-40 weak

### W03.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude RSI=RSI2 drops 8/15 losers (53%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 30-40 weak

### W04.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=97  W=93/L=4  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `T4=T4a AND BBP=BBP1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude RSI=RSI2 drops 8/12 losers (67%)
- **Final: n=93  W=89/L=4  WR=95.7%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched lower band; session=asia  •  AVOID when RSI 30-40 weak

### W06.  `H60=H60e AND T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude RSI=RSI2 drops 8/12 losers (67%)
- **Final: n=93  W=89/L=4  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; just touched lower band; session=asia  •  AVOID when RSI 30-40 weak

### W07.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=102  W=92/L=10  WR=90.2%
- Refine: exclude RSI=RSI2 drops 6/10 losers (60%)
- **Final: n=93  W=89/L=4  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; session=asia  •  AVOID when RSI 30-40 weak

### W08.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude RSI=RSI2 drops 8/12 losers (67%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; session=asia  •  AVOID when RSI 30-40 weak

### W09.  `H60=H60b AND T4=T4a AND session_bucket=ny_close`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude T1=T1a drops 12/13 losers (92%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W10.  `H20=H20e AND H60=H60b AND session_bucket=ny_close`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; session=ny_close  •  AVOID when 1h trend WITH trade

### W11.  `H60=H60b AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; session=ny_close  •  AVOID when 1h trend WITH trade

### W12.  `H20=H20e AND H60=H60b AND T4=T4a AND session_bucket=ny_close`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend WITH trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W13.  `H20=H20e AND H60=H60b AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned; session=ny_close  •  AVOID when 1h trend WITH trade

### W14.  `H60=H60b AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W15.  `H20=H20a AND H60=H60c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W16.  `H60=H60c AND T1=T1c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W17.  `H60=H60c AND T4=T4c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W18.  `H60=H60c AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  HTF60 neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W19.  `H20=H20a AND H60=H60c AND T1=T1c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W20.  `H20=H20a AND H60=H60c AND T4=T4c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W21.  `H20=H20a AND H60=H60c AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W22.  `H60=H60c AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W23.  `H60=H60c AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W24.  `H60=H60c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W25.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude H60=H60e drops 9/10 losers (90%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=335  W=126/L=209  WR=37.6%
- Sharpen: sharpest is T4=T4c (167/209 of losers there)
- **Sharp: n=244  W=77/L=167  WR=31.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L02.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=323  W=121/L=202  WR=37.5%
- Sharpen: sharpest is T4=T4c (167/202 of losers there)
- **Sharp: n=244  W=77/L=167  WR=31.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L03.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=323  W=121/L=202  WR=37.5%
- Sharpen: sharpest is T4=T4c (167/202 of losers there)
- **Sharp: n=244  W=77/L=167  WR=31.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=320  W=115/L=205  WR=35.9%
- Sharpen: sharpest is RSI=RSI3 (54/205 of losers there)
- **Sharp: n=63  W=9/L=54  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L05.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=295  W=110/L=185  WR=37.3%
- Sharpen: sharpest is T1=T1c (167/185 of losers there)
- **Sharp: n=244  W=77/L=167  WR=31.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=295  W=110/L=185  WR=37.3%
- Sharpen: sharpest is T1=T1c (167/185 of losers there)
- **Sharp: n=244  W=77/L=167  WR=31.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L07.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=244  W=77/L=167  WR=31.6%
- Sharpen: sharpest is BBP=BBP1 (53/167 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when just touched lower band

### L08.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=219  W=83/L=136  WR=37.9%
- Sharpen: sharpest is BBP=BBP1 (86/136 of losers there)
- **Sharp: n=123  W=37/L=86  WR=30.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L09.  `ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=205  W=80/L=125  WR=39.0%
- Sharpen: sharpest is H60=H60a (117/125 of losers there)
- **Sharp: n=175  W=58/L=117  WR=33.1%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=204  W=78/L=126  WR=38.2%
- Sharpen: sharpest is H60=H60c (21/126 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 30-40 weak  •  ONLY when HTF60 neutral

### L11.  `T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=201  W=74/L=127  WR=36.8%
- Sharpen: sharpest is BBP=BBP1 (68/127 of losers there)
- **Sharp: n=88  W=20/L=68  WR=22.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L12.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=201  W=77/L=124  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (86/124 of losers there)
- **Sharp: n=118  W=32/L=86  WR=27.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L13.  `T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=199  W=63/L=136  WR=31.7%
- Sharpen: sharpest is BBP=BBP1 (76/136 of losers there)
- **Sharp: n=93  W=17/L=76  WR=18.3%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L14.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=199  W=74/L=125  WR=37.2%
- Sharpen: sharpest is BBP=BBP1 (66/125 of losers there)
- **Sharp: n=86  W=20/L=66  WR=23.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L15.  `H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=190  W=67/L=123  WR=35.3%
- Sharpen: sharpest is T4=T4c (108/123 of losers there)
- **Sharp: n=146  W=38/L=108  WR=26.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L16.  `T4=T4c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=176  W=60/L=116  WR=34.1%
- Sharpen: sharpest is BBP=BBP1 (63/116 of losers there)
- **Sharp: n=77  W=14/L=63  WR=18.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L17.  `H60=H60a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=175  W=58/L=117  WR=33.1%
- Sharpen: sharpest is RSI=RSI3 (34/117 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L18.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=170  W=54/L=116  WR=31.8%
- Sharpen: sharpest is BBP=BBP1 (63/116 of losers there)
- **Sharp: n=71  W=8/L=63  WR=11.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L19.  `H60=H60a AND T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=169  W=52/L=117  WR=30.8%
- Sharpen: sharpest is T4=T4c (108/117 of losers there)
- **Sharp: n=140  W=32/L=108  WR=22.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20a AND T4=T4c AND ZS=ZS1`
- Raw: n=166  W=56/L=110  WR=33.7%
- Sharpen: sharpest is T1=T1a (39/110 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=164  W=56/L=108  WR=34.1%
- Sharpen: sharpest is H60=H60c (20/108 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF60 neutral

### L22.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=164  W=56/L=108  WR=34.1%
- Sharpen: sharpest is H60=H60c (20/108 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF60 neutral

### L23.  `H20=H20e AND H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=153  W=58/L=95  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (25/95 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L24.  `H20=H20e AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=153  W=58/L=95  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (25/95 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L25.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=147  W=52/L=95  WR=35.4%
- Sharpen: sharpest is T4=T4c (86/95 of losers there)
- **Sharp: n=118  W=32/L=86  WR=27.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(48/38) | H20e(38/48) |
| H60 | H60b(13/7) | — |
| T1 | — | — |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/46) | long(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
