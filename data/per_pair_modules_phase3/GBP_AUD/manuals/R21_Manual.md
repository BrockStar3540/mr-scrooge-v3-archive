# GBP_AUD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **8,448**  (W=5,122 / L=3,326)  -  WR: **60.6%**

## Session distribution

- asia: n=2476  W=1521/L=955  WR=61.4%
- london_open: n=1408  W=850/L=558  WR=60.4%
- ny_close: n=1239  W=778/L=461  WR=62.8%
- ny_mid: n=1198  W=694/L=504  WR=57.9%
- london: n=626  W=389/L=237  WR=62.1%
- ny_open: n=586  W=351/L=235  WR=59.9%
- asia_late: n=574  W=357/L=217  WR=62.2%
- off_hours: n=341  W=182/L=159  WR=53.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20b AND T4=T4a AND BBP=BBP4`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude H60=H60e drops 5/15 losers (33%)
- **Final: n=107  W=97/L=10  WR=90.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third  •  AVOID when HTF60 strongly against

### W02.  `H60=H60a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W03.  `T1=T1a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W04.  `T4=T4a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W05.  `ZS=ZS1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W06.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W07.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W08.  `H60=H60a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W09.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W10.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W11.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W12.  `H20=H20b AND H60=H60a AND BBP=BBP4`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W13.  `H20=H20b AND T1=T1a AND BBP=BBP4`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W14.  `H20=H20b AND BBP=BBP4 AND direction_exec=short`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; upper third  •  AVOID when RSI 30-40 weak

### W15.  `H20=H20b AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W16.  `H20=H20b AND H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W17.  `H20=H20b AND H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20b AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W19.  `H20=H20b AND T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W20.  `H20=H20b AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20d AND T4=T4a AND RSI=RSI1`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude session_bucket=ny_mid drops 9/9 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W22.  `H20=H20d AND H60=H60a AND T4=T4a AND RSI=RSI1`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude session_bucket=ny_mid drops 9/9 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W23.  `H20=H20d AND T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude session_bucket=ny_mid drops 9/9 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W24.  `H20=H20d AND T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude session_bucket=ny_mid drops 9/9 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W25.  `H20=H20b AND T4=T4a AND ZS=ZS4`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H60=H60e drops 5/14 losers (36%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=147  W=53/L=94  WR=36.1%
- Sharpen: sharpest is H60=H60a (40/94 of losers there)
- **Sharp: n=44  W=4/L=40  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L02.  `H20=H20e AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=48/L=94  WR=33.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=asia_late

### L03.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=48/L=94  WR=33.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=asia_late

### L04.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=48/L=94  WR=33.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia_late

### L05.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=48/L=94  WR=33.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia_late

### L06.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=48/L=94  WR=33.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=asia_late

### L07.  `H60=H60a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=55/L=85  WR=39.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=london_open

### L08.  `T1=T1a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=55/L=85  WR=39.3%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open

### L09.  `ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=55/L=85  WR=39.3%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=london_open

### L10.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=55/L=85  WR=39.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open

### L11.  `H60=H60a AND ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=55/L=85  WR=39.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=london_open

### L12.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=55/L=85  WR=39.3%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open

### L13.  `H20=H20e AND H60=H60a AND BBP=BBP2`
- Raw: n=139  W=50/L=89  WR=36.0%
- Sharpen: sharpest is session_bucket=ny_close (42/89 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  ONLY when session=ny_close

### L14.  `H20=H20e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=139  W=50/L=89  WR=36.0%
- Sharpen: sharpest is session_bucket=ny_close (42/89 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third  •  ONLY when session=ny_close

### L15.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=139  W=50/L=89  WR=36.0%
- Sharpen: sharpest is session_bucket=ny_close (42/89 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  ONLY when session=ny_close

### L16.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=139  W=52/L=87  WR=37.4%
- Sharpen: sharpest is session_bucket=ny_close (42/87 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=ny_close

### L17.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is H20=H20a (43/85 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 aligned WITH trade

### L18.  `H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is H20=H20a (43/85 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 aligned WITH trade

### L19.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is H20=H20a (43/85 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 aligned WITH trade

### L20.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is H20=H20a (43/85 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20e AND H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=137  W=50/L=87  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_close (42/87 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  ONLY when session=ny_close

### L22.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=137  W=50/L=87  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_close (42/87 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=ny_close

### L23.  `H20=H20e AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=132  W=43/L=89  WR=32.6%
- Sharpen: sharpest is H60=H60a (39/89 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L24.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=128  W=49/L=79  WR=38.3%
- Sharpen: sharpest is H20=H20b (28/79 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L25.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (40/77 of losers there)
- **Sharp: n=44  W=4/L=40  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; RSI 30-40 weak  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
