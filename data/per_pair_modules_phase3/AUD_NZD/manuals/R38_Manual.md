# AUD_NZD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,565**  (W=1,006 / L=559)  -  WR: **64.3%**

## Session distribution

- asia: n=572  W=370/L=202  WR=64.7%
- ny_open: n=214  W=147/L=67  WR=68.7%
- london_open: n=180  W=118/L=62  WR=65.6%
- london: n=172  W=112/L=60  WR=65.1%
- ny_mid: n=159  W=104/L=55  WR=65.4%
- off_hours: n=148  W=79/L=69  WR=53.4%
- ny_close: n=61  W=41/L=20  WR=67.2%
- asia_late: n=59  W=35/L=24  WR=59.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=asia drops 7/14 losers (50%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=asia

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 4/12 losers (33%)
- **Final: n=84  W=76/L=8  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W03.  `H60=H60a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band  •  AVOID when session=asia

### W04.  `H60=H60a AND T1=T1c AND BBP=BBP0`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W05.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W06.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W07.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W08.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W09.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 7/10 losers (70%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W10.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude ZS=ZS0 drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when zscore <-3 extreme

### W11.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude ZS=ZS0 drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 30-40 weak  •  AVOID when zscore <-3 extreme

### W12.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude ZS=ZS0 drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when zscore <-3 extreme

### W13.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W14.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude RSI=RSI1 drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 20-30 oversold

### W15.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude RSI=RSI1 drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 20-30 oversold

### W16.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude RSI=RSI1 drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 20-30 oversold

### W17.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude H20=H20c drops 7/7 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 neutral

### W18.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude ZS=ZS0 drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when zscore <-3 extreme

### W19.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude ZS=ZS0 drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when zscore <-3 extreme

### W20.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude RSI=RSI1 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 20-30 oversold

### W21.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude RSI=RSI1 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 20-30 oversold

### W22.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude BBP=BBP3 drops 8/8 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when middle of band

### W23.  `T1=T1c AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude BBP=BBP3 drops 8/8 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when middle of band

### W24.  `H20=H20c AND T4=T4a AND RSI=RSI3`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W25.  `T4=T4c AND RSI=RSI2 AND session_bucket=london`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H20=H20e drops 4/6 losers (67%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is BBP=BBP0 (35/64 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L02.  `H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is BBP=BBP0 (33/62 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L03.  `T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is BBP=BBP0 (33/62 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L04.  `H60=H60e AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is BBP=BBP0 (33/62 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L05.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP0 (26/53 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L06.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP0 (26/53 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L07.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP0 (26/53 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L08.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H20=H20d (20/51 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L09.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H20=H20d (20/51 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L10.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is RSI=RSI2 (40/49 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L11.  `H20=H20d AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is RSI=RSI2 (40/49 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20d AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is RSI=RSI2 (40/49 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L13.  `H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20d (20/42 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L14.  `T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20d (20/42 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L15.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20d (20/42 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L16.  `H60=H60e AND T1=T1a AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L17.  `H60=H60e AND T4=T4a AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L18.  `H60=H60e AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  HTF60 strongly against; session=off_hours  •  ONLY when HTF20 mildly against

### L19.  `T1=T1a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L20.  `T1=T1a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  1h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L21.  `T4=T4a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  4h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L22.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L23.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L24.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

### L25.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is H20=H20d (32/45 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/31) | H20d(6/11), H20e(33/38) |
| H60 | H60a(57/42) | H60e(43/58) |
| T1 | T1c(56/44) | T1a(44/56) |
| T4 | T4c(52/45) | T4a(48/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/42) | short(43/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
