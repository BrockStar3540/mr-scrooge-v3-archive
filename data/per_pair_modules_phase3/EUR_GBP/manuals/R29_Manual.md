# EUR_GBP — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **801**  (W=530 / L=271)  -  WR: **66.2%**

## Session distribution

- london_open: n=163  W=112/L=51  WR=68.7%
- ny_close: n=150  W=97/L=53  WR=64.7%
- london: n=139  W=96/L=43  WR=69.1%
- ny_mid: n=129  W=84/L=45  WR=65.1%
- asia: n=94  W=58/L=36  WR=61.7%
- ny_open: n=86  W=60/L=26  WR=69.8%
- off_hours: n=31  W=17/L=14  WR=54.8%
- asia_late: n=9  W=6/L=3  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND T1=T1c AND T4=T4a`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W02.  `H20=H20c AND T1=T1c AND direction_exec=long`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade  •  AVOID when session=london_open

### W03.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when session=london_open

### W04.  `H20=H20c AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W05.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H20=H20b drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london_open  •  AVOID when HTF20 slightly aligned

### W06.  `T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude H20=H20b drops 9/10 losers (90%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 slightly aligned

### W07.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude H20=H20b drops 9/10 losers (90%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 slightly aligned

### W08.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude T1=T1c drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W09.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W10.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W11.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=59/L=2  WR=96.7%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when 1h trend WITH trade

### W13.  `H20=H20d AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: exclude session_bucket=london_open drops 4/4 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W14.  `H60=H60b AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude H20=H20b drops 2/5 losers (40%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W15.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude T1=T1c drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20a AND H60=H60b AND T4=T4c`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude session_bucket=london_open drops 4/6 losers (67%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when session=london_open

### W17.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=london_open

### W18.  `H20=H20c AND H60=H60e AND T4=T4a`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=london_open

### W19.  `H20=H20c AND H60=H60e AND direction_exec=long`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against  •  AVOID when session=london_open

### W20.  `T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude ZS=ZS4 drops 3/6 losers (50%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W21.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W22.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=london_open

### W23.  `H20=H20c AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=london_open

### W24.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

### W25.  `BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is T4=T4a (30/47 of losers there)
- **Sharp: n=32  W=2/L=30  WR=6.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is T4=T4a (30/47 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is T4=T4a (30/47 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20c AND T1=T1a AND T4=T4c`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_close (16/38 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L05.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_close (16/38 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  ONLY when session=ny_close

### L06.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_close (16/38 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L07.  `H20=H20c AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_close (16/38 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L08.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is RSI=RSI3 (10/31 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20b AND T4=T4a AND direction_exec=short`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is RSI=RSI3 (10/31 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L10.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is RSI=RSI3 (10/31 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L11.  `H20=H20e AND H60=H60d AND T4=T4a`
- Raw: n=46  W=16/L=30  WR=34.8%
- Sharpen: sharpest is direction_exec=long (21/30 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade  •  ONLY when long

### L12.  `RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is H20=H20e (13/28 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L13.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is H20=H20e (13/28 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L14.  `H60=H60d AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is session_bucket=ny_mid (14/27 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L15.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is T4=T4a (20/28 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when 4h trend WITH trade

### L16.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is T4=T4a (20/28 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_mid  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is T4=T4a (20/28 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20e AND H60=H60d AND RSI=RSI2`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is T1=T1c (18/27 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 30-40 weak  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20c AND T1=T1a AND RSI=RSI3`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (9/25 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L20.  `H20=H20c AND T4=T4c AND RSI=RSI3`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (9/25 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L21.  `H20=H20c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (9/25 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L22.  `H20=H20c AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (9/25 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L23.  `H20=H20c AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (9/25 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L24.  `H20=H20c AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (9/25 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L25.  `H20=H20e AND H60=H60d AND T4=T4a AND RSI=RSI2`
- Raw: n=40  W=14/L=26  WR=35.0%
- Sharpen: sharpest is T1=T1c (17/26 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(26/12), H20a(22/14) | H20b(18/30), H20e(16/25) |
| H60 | H60b(29/14), H60e(25/13) | H60d(14/31), H60a(19/26) |
| T1 | — | — |
| T4 | T4c(55/46) | T4a(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | ZS1(35/28) | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
