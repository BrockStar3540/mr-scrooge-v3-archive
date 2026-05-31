# NZD_USD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **985**  (W=620 / L=365)  -  WR: **62.9%**

## Session distribution

- asia: n=194  W=131/L=63  WR=67.5%
- ny_mid: n=186  W=114/L=72  WR=61.3%
- london_open: n=177  W=112/L=65  WR=63.3%
- ny_close: n=174  W=112/L=62  WR=64.4%
- london: n=132  W=81/L=51  WR=61.4%
- off_hours: n=56  W=33/L=23  WR=58.9%
- ny_open: n=48  W=27/L=21  WR=56.2%
- asia_late: n=18  W=10/L=8  WR=55.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W02.  `T1=T1a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W03.  `T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W04.  `RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W05.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W06.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W07.  `H20=H20a AND RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W09.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W10.  `T4=T4a AND RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 neutral

### W11.  `H20=H20a AND H60=H60e AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W12.  `H20=H20a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold; session=asia

### W13.  `T1=T1a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI<20 extreme oversold; session=asia

### W14.  `T4=T4a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI<20 extreme oversold; session=asia

### W15.  `RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI<20 extreme oversold; session=asia

### W16.  `H20=H20a AND T1=T1a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold; session=asia

### W17.  `H20=H20a AND T4=T4a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold; session=asia

### W18.  `H20=H20a AND RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold; session=asia

### W19.  `T1=T1a AND T4=T4a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI<20 extreme oversold; session=asia

### W20.  `T1=T1a AND RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI<20 extreme oversold; session=asia

### W21.  `T4=T4a AND RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI<20 extreme oversold; session=asia

### W22.  `H60=H60a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude RSI=RSI1 drops 4/5 losers (80%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=asia  •  AVOID when RSI 20-30 oversold

### W23.  `H20=H20a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H60=H60e drops 4/6 losers (67%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=asia  •  AVOID when HTF60 strongly against

### W24.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_open

### W25.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (21/88 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L02.  `H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (21/88 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L03.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (21/88 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L04.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (21/88 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L05.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (21/88 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L06.  `H60=H60a AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (21/88 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london_open

### L07.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is H60=H60a (38/69 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L08.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is H60=H60a (38/69 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L09.  `H20=H20e AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is H60=H60a (38/69 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND H60=H60a AND RSI=RSI1`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is ZS=ZS2 (38/63 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when zscore -2 to -1 oversold

### L11.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is ZS=ZS2 (38/63 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -2 to -1 oversold

### L12.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is ZS=ZS2 (38/63 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -2 to -1 oversold

### L13.  `H20=H20e AND H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is ZS=ZS2 (38/63 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when zscore -2 to -1 oversold

### L14.  `H60=H60a AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H20=H20e (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L15.  `H60=H60a AND BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H20=H20e (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L16.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (18/55 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L17.  `T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (18/55 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L18.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (18/55 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L19.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (18/55 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L20.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (18/53 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=asia

### L21.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (18/53 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L22.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (18/53 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when session=asia

### L23.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (18/53 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L24.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (18/53 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=asia

### L25.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (18/53 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(58/41) | H20e(41/58) |
| H60 | — | — |
| T1 | T1a(61/40) | T1c(39/60) |
| T4 | T4a(61/40) | T4c(39/60) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(61/40) | long(39/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
