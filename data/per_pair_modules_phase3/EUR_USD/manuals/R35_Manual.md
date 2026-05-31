# EUR_USD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,956**  (W=1,226 / L=730)  -  WR: **62.7%**

## Session distribution

- asia: n=538  W=346/L=192  WR=64.3%
- ny_mid: n=347  W=213/L=134  WR=61.4%
- ny_close: n=308  W=200/L=108  WR=64.9%
- london_open: n=305  W=185/L=120  WR=60.7%
- ny_open: n=244  W=148/L=96  WR=60.7%
- london: n=99  W=58/L=41  WR=58.6%
- asia_late: n=87  W=58/L=29  WR=66.7%
- off_hours: n=28  W=18/L=10  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude ZS=ZS2 drops 19/19 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W02.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude ZS=ZS2 drops 19/19 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W03.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude ZS=ZS2 drops 19/19 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W04.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude ZS=ZS2 drops 19/19 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W05.  `T1=T1a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H60=H60d drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 mildly against

### W06.  `T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H60=H60d drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 mildly against

### W07.  `RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H60=H60d drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 mildly against

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H60=H60d drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 mildly against

### W09.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H60=H60d drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 mildly against

### W10.  `T4=T4a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H60=H60d drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 mildly against

### W11.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude BBP=BBP4 drops 8/11 losers (73%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when upper third

### W12.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude BBP=BBP4 drops 8/11 losers (73%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when upper third

### W13.  `H20=H20a AND H60=H60b AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; session=london_open  •  AVOID when just touched lower band

### W14.  `H60=H60b AND T1=T1a AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W15.  `H60=H60b AND T4=T4a AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W16.  `H60=H60b AND direction_exec=short AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; session=london_open  •  AVOID when just touched lower band

### W17.  `H20=H20a AND H60=H60b AND T1=T1a AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W18.  `H20=H20a AND H60=H60b AND T4=T4a AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W19.  `H20=H20a AND H60=H60b AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; RSI 20-30 oversold; session=london_open  •  AVOID when just touched lower band

### W20.  `H20=H20a AND H60=H60b AND direction_exec=short AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; session=london_open  •  AVOID when just touched lower band

### W21.  `H60=H60b AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W22.  `H60=H60b AND T1=T1a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when just touched lower band

### W23.  `H60=H60b AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W24.  `H60=H60b AND T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when just touched lower band

### W25.  `H60=H60b AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60d AND T1=T1c`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=london_open

### L02.  `H20=H20e AND H60=H60d AND T4=T4c`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=london_open

### L03.  `H20=H20e AND H60=H60d AND direction_exec=long`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against  •  ONLY when session=london_open

### L04.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L05.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=london_open

### L06.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=london_open

### L07.  `H20=H20e AND H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L08.  `H20=H20e AND H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=london_open

### L09.  `H20=H20e AND H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=london_open

### L10.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (52/160 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L11.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L12.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L13.  `RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L14.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L15.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L16.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L17.  `H20=H20e AND H60=H60d AND RSI=RSI1`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 20-30 oversold  •  ONLY when session=london_open

### L18.  `H60=H60d AND T1=T1c AND RSI=RSI1`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L19.  `H60=H60d AND T4=T4c AND RSI=RSI1`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L20.  `H60=H60d AND RSI=RSI1 AND direction_exec=long`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 20-30 oversold  •  ONLY when session=london_open

### L21.  `H20=H20e AND H60=H60d AND T1=T1c AND RSI=RSI1`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L22.  `H20=H20e AND H60=H60d AND T4=T4c AND RSI=RSI1`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L23.  `H20=H20e AND H60=H60d AND RSI=RSI1 AND direction_exec=long`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; RSI 20-30 oversold  •  ONLY when session=london_open

### L24.  `H60=H60d AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L25.  `H60=H60d AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=london_open (52/92 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(57/43) | H20e(43/57) |
| H60 | H60e(24/18) | H60d(23/30) |
| T1 | T1a(55/44) | T1c(45/56) |
| T4 | T4a(56/44) | T4c(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/44) | long(45/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
