# EUR_GBP — R34 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **586**  (W=372 / L=214)  -  WR: **63.5%**

## Session distribution

- ny_mid: n=213  W=138/L=75  WR=64.8%
- ny_open: n=116  W=69/L=47  WR=59.5%
- london_open: n=112  W=72/L=40  WR=64.3%
- ny_close: n=61  W=40/L=21  WR=65.6%
- asia: n=46  W=25/L=21  WR=54.3%
- london: n=38  W=28/L=10  WR=73.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 11/16 losers (69%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W02.  `T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 11/16 losers (69%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W03.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 11/16 losers (69%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude BBP=BBP0 drops 9/10 losers (90%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W05.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude BBP=BBP0 drops 9/10 losers (90%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W06.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude BBP=BBP0 drops 9/10 losers (90%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W07.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude ZS=ZS0 drops 4/8 losers (50%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when zscore <-3 extreme

### W08.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when 1h trend AGAINST trade

### W09.  `H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20d drops 7/9 losers (78%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W10.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_mid

### W11.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak  •  AVOID when session=ny_mid

### W12.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_mid

### W13.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W14.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W15.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W16.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W17.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W18.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W19.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W20.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W21.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20a AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W23.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=53  W=49/L=4  WR=92.5%
- Refine: exclude H20=H20d drops 3/4 losers (75%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W24.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=52  W=47/L=5  WR=90.4%
- Refine: exclude ZS=ZS0 drops 4/5 losers (80%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore <-3 extreme

### W25.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=52  W=47/L=5  WR=90.4%
- Refine: exclude ZS=ZS0 drops 4/5 losers (80%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore <-3 extreme

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=162  W=58/L=104  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_open (33/104 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_open (32/74 of losers there)
- **Sharp: n=34  W=2/L=32  WR=5.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L03.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_open (32/74 of losers there)
- **Sharp: n=34  W=2/L=32  WR=5.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when session=ny_open

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_open (32/74 of losers there)
- **Sharp: n=34  W=2/L=32  WR=5.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=110  W=33/L=77  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_open (25/77 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L06.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=110  W=33/L=77  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_open (25/77 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L07.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=110  W=33/L=77  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_open (25/77 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is H20=H20e (25/55 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=84  W=29/L=55  WR=34.5%
- Sharpen: sharpest is H20=H20e (25/55 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=84  W=29/L=55  WR=34.5%
- Sharpen: sharpest is H20=H20e (25/55 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L11.  `H20=H20d AND T1=T1c AND direction_exec=long`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_open (10/52 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L12.  `H20=H20d AND H60=H60e AND direction_exec=long`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against  •  ONLY when session=ny_open

### L13.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is T4=T4c (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is T4=T4c (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is T4=T4c (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L16.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=61  W=15/L=46  WR=24.6%
- Sharpen: sharpest is session_bucket=london_open (12/46 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=london_open

### L17.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=61  W=15/L=46  WR=24.6%
- Sharpen: sharpest is session_bucket=london_open (12/46 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak  •  ONLY when session=london_open

### L18.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=61  W=15/L=46  WR=24.6%
- Sharpen: sharpest is session_bucket=london_open (12/46 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=london_open

### L19.  `H20=H20d AND T1=T1c AND RSI=RSI2`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_open (10/39 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L20.  `H20=H20d AND RSI=RSI2 AND direction_exec=long`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_open (10/39 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 30-40 weak  •  ONLY when session=ny_open

### L21.  `H20=H20d AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_open (10/39 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L22.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=60  W=15/L=45  WR=25.0%
- Sharpen: sharpest is session_bucket=london_open (12/45 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L23.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=60  W=15/L=45  WR=25.0%
- Sharpen: sharpest is session_bucket=london_open (12/45 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L24.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=60  W=15/L=45  WR=25.0%
- Sharpen: sharpest is session_bucket=london_open (12/45 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L25.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=60  W=15/L=45  WR=25.0%
- Sharpen: sharpest is session_bucket=london_open (12/45 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(30/12) | H20d(12/34) |
| H60 | H60b(15/8) | — |
| T1 | T1a(58/35) | T1c(42/65) |
| T4 | T4a(57/44) | T4c(43/56) |
| BBP | — | BBP2(34/40) |
| RSI | — | RSI2(56/61) |
| ZS | — | ZS2(33/39) |
| strategy_id | — | — |
| direction_exec | short(59/33) | long(41/67) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
