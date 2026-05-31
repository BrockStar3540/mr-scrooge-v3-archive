# NZD_CAD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,286**  (W=809 / L=477)  -  WR: **62.9%**

## Session distribution

- asia: n=383  W=243/L=140  WR=63.4%
- ny_mid: n=321  W=200/L=121  WR=62.3%
- london_open: n=209  W=134/L=75  WR=64.1%
- ny_close: n=149  W=92/L=57  WR=61.7%
- ny_open: n=126  W=79/L=47  WR=62.7%
- london: n=45  W=30/L=15  WR=66.7%
- off_hours: n=40  W=24/L=16  WR=60.0%
- asia_late: n=13  W=7/L=6  WR=53.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=201  W=174/L=27  WR=86.6%
- Refine: exclude session_bucket=ny_close drops 13/27 losers (48%)
- **Final: n=171  W=157/L=14  WR=91.8%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W02.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=182  W=158/L=24  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 9/24 losers (38%)
- **Final: n=164  W=149/L=15  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_close

### W03.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude H20=H20b drops 10/15 losers (67%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W04.  `H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude H20=H20b drops 10/15 losers (67%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude H20=H20b drops 10/15 losers (67%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W06.  `H60=H60a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H20=H20b drops 10/15 losers (67%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W07.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude H20=H20e drops 8/16 losers (50%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when HTF20 strongly against

### W08.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 11/12 losers (92%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 11/12 losers (92%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 11/12 losers (92%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W11.  `H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude H20=H20b drops 10/15 losers (67%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude H20=H20b drops 10/15 losers (67%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W13.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude H20=H20b drops 10/15 losers (67%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W14.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=111  W=104/L=7  WR=93.7%
- Refine: exclude RSI=RSI1 drops 4/7 losers (57%)
- **Final: n=93  W=90/L=3  WR=96.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 20-30 oversold

### W15.  `H60=H60a AND T1=T1a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude H20=H20b drops 10/13 losers (77%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W16.  `H60=H60a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude H20=H20b drops 10/13 losers (77%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W17.  `H60=H60a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude H20=H20b drops 10/13 losers (77%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W18.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 10/15 losers (67%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W19.  `H60=H60a AND T1=T1a AND ZS=ZS1`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=ny_close drops 10/15 losers (67%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W20.  `H60=H60a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=ny_close drops 10/15 losers (67%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W21.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=ny_close drops 10/15 losers (67%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W22.  `T1=T1a AND T4=T4c AND RSI=RSI2`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=91  W=90/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when middle of band

### W23.  `T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=91  W=90/L=1  WR=98.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when middle of band

### W24.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=91  W=90/L=1  WR=98.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when middle of band

### W25.  `H20=H20a AND T1=T1a AND BBP=BBP2`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H60=H60d drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when HTF60 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=159  W=47/L=112  WR=29.6%
- Sharpen: sharpest is session_bucket=london_open (27/112 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when session=london_open

### L02.  `T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=156  W=56/L=100  WR=35.9%
- Sharpen: sharpest is RSI=RSI2 (50/100 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L03.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (34/81 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L04.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (34/81 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L05.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (34/81 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L06.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=116  W=42/L=74  WR=36.2%
- Sharpen: sharpest is T1=T1c (40/74 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak  •  ONLY when 1h trend AGAINST trade

### L07.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is T1=T1c (38/69 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L08.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is T1=T1c (38/69 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L09.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is RSI=RSI2 (40/66 of losers there)
- **Sharp: n=46  W=6/L=40  WR=13.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L10.  `T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is RSI=RSI2 (40/66 of losers there)
- **Sharp: n=46  W=6/L=40  WR=13.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band  •  ONLY when RSI 30-40 weak

### L11.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is RSI=RSI2 (40/66 of losers there)
- **Sharp: n=46  W=6/L=40  WR=13.0%**
- **Dir: LONG**  •  just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L12.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is RSI=RSI2 (40/66 of losers there)
- **Sharp: n=46  W=6/L=40  WR=13.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L13.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H20=H20a (31/64 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H20=H20a (31/64 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L15.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H20=H20a (31/64 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=102  W=28/L=74  WR=27.5%
- Sharpen: sharpest is H60=H60b (25/74 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 slightly aligned

### L17.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=102  W=28/L=74  WR=27.5%
- Sharpen: sharpest is H60=H60b (25/74 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when HTF60 slightly aligned

### L18.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=102  W=28/L=74  WR=27.5%
- Sharpen: sharpest is H60=H60b (25/74 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 slightly aligned

### L19.  `H60=H60e AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is H20=H20a (25/63 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L20.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=101  W=29/L=72  WR=28.7%
- Sharpen: sharpest is RSI=RSI1 (27/72 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L21.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=101  W=29/L=72  WR=28.7%
- Sharpen: sharpest is RSI=RSI1 (27/72 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L22.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=101  W=29/L=72  WR=28.7%
- Sharpen: sharpest is RSI=RSI1 (27/72 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L23.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=33/L=59  WR=35.9%
- Sharpen: sharpest is H20=H20e (27/59 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L24.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=91  W=22/L=69  WR=24.2%
- Sharpen: sharpest is session_bucket=london_open (23/69 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london_open

### L25.  `H20=H20e AND T1=T1c AND BBP=BBP2`
- Raw: n=85  W=25/L=60  WR=29.4%
- Sharpen: sharpest is H60=H60a (31/60 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(16/7), H20a(33/24) | H20e(24/36), H20d(9/16) |
| H60 | H60a(46/39) | H60e(38/44) |
| T1 | T1a(62/32) | T1c(38/68) |
| T4 | T4a(52/45) | T4c(48/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(62/32) | long(38/68) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
