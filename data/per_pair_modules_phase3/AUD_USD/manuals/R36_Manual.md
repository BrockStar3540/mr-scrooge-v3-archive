# AUD_USD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,463**  (W=1,552 / L=911)  -  WR: **63.0%**

## Session distribution

- asia: n=1037  W=663/L=374  WR=63.9%
- ny_mid: n=378  W=235/L=143  WR=62.2%
- ny_close: n=312  W=196/L=116  WR=62.8%
- london: n=238  W=145/L=93  WR=60.9%
- london_open: n=228  W=147/L=81  WR=64.5%
- off_hours: n=114  W=68/L=46  WR=59.6%
- asia_late: n=84  W=53/L=31  WR=63.1%
- ny_open: n=72  W=45/L=27  WR=62.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W03.  `RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60e AND T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60e AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W06.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60e AND T4=T4a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W09.  `T4=T4a AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60e AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W11.  `T1=T1a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W12.  `T4=T4a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W13.  `ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W14.  `H60=H60e AND T1=T1a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W15.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W16.  `H60=H60e AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W17.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W18.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W19.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP1 drops 12/13 losers (92%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when just touched lower band

### W20.  `H20=H20a AND H60=H60e AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=ny_close drops 2/11 losers (18%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; just touched lower band; RSI 20-30 oversold  •  AVOID when session=ny_close

### W21.  `H20=H20a AND T1=T1a AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=ny_close drops 2/11 losers (18%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched lower band; RSI 20-30 oversold  •  AVOID when session=ny_close

### W22.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=ny_close drops 2/11 losers (18%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 20-30 oversold  •  AVOID when session=ny_close

### W23.  `H20=H20a AND BBP=BBP1 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=ny_close drops 2/11 losers (18%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched lower band; RSI 20-30 oversold  •  AVOID when session=ny_close

### W24.  `H20=H20d AND H60=H60e AND RSI=RSI1`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude session_bucket=london drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 20-30 oversold  •  AVOID when session=london

### W25.  `H20=H20d AND T1=T1a AND RSI=RSI1`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude session_bucket=london drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L02.  `T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L03.  `T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L04.  `RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L05.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L06.  `H60=H60a AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L07.  `H60=H60a AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L09.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L10.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20b (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L11.  `H60=H60a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is H20=H20a (24/55 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L12.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is H20=H20a (24/55 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L13.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is H20=H20a (24/55 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is H20=H20a (24/55 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L15.  `H60=H60a AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is H20=H20a (24/55 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is H20=H20a (24/55 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L17.  `H60=H60a AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is H20=H20a (18/49 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is H20=H20a (18/49 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L19.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is H20=H20a (18/49 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L20.  `H20=H20b AND H60=H60a AND ZS=ZS2`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L21.  `H20=H20b AND T1=T1c AND ZS=ZS2`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L22.  `H20=H20b AND ZS=ZS2 AND direction_exec=long`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L23.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (21/45 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L24.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (21/45 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L25.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (21/45 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(32/37) |
| H60 | H60e(54/45) | H60a(46/55) |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | T4a(54/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/45) | long(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
