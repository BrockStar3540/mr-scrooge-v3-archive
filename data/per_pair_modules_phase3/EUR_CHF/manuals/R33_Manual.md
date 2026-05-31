# EUR_CHF — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **691**  (W=427 / L=264)  -  WR: **61.8%**

## Session distribution

- ny_mid: n=310  W=188/L=122  WR=60.6%
- ny_open: n=224  W=145/L=79  WR=64.7%
- london_open: n=78  W=48/L=30  WR=61.5%
- london: n=40  W=25/L=15  WR=62.5%
- ny_close: n=39  W=21/L=18  WR=53.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W02.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 13/14 losers (93%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W03.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 13/14 losers (93%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W04.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 13/14 losers (93%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W05.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 13/14 losers (93%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W06.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 13/14 losers (93%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W07.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 13/14 losers (93%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W08.  `H20=H20a AND H60=H60e AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_open

### W09.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open

### W10.  `H20=H20a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_open

### W11.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open

### W12.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_open

### W13.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_open

### W14.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_open

### W15.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_open

### W16.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=ny_open

### W17.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=ny_open

### W18.  `H20=H20a AND H60=H60e AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought; session=ny_open

### W19.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_open

### W20.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open

### W21.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_open

### W22.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open

### W23.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_open

### W24.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open

### W25.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=73/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND BBP=BBP4`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is H60=H60a (38/62 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when HTF60 aligned WITH trade

### L02.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L03.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L04.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when session=ny_open

### L05.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L06.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L07.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L08.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L09.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L10.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L11.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (40/58 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L12.  `H20=H20e AND T4=T4c AND ZS=ZS4`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is session_bucket=ny_open (35/58 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L13.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is session_bucket=ny_open (35/58 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L14.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is session_bucket=ny_open (35/58 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L15.  `H20=H20e AND H60=H60a AND RSI=RSI6`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI6`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L17.  `H20=H20e AND T4=T4c AND RSI=RSI6`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L18.  `H20=H20e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought  •  ONLY when session=ny_open

### L19.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L20.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L21.  `H20=H20e AND H60=H60a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L22.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L23.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L24.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (40/52 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L25.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20e (40/44 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(36/20) | H20e(14/34) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(60/43) | T4c(40/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | ZS5(17/23) |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
