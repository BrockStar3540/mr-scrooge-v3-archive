# EUR_GBP — R39 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **437**  (W=282 / L=155)  -  WR: **64.5%**

## Session distribution

- ny_open: n=92  W=58/L=34  WR=63.0%
- asia: n=91  W=64/L=27  WR=70.3%
- ny_mid: n=81  W=48/L=33  WR=59.3%
- london: n=65  W=47/L=18  WR=72.3%
- london_open: n=45  W=26/L=19  WR=57.8%
- asia_late: n=37  W=25/L=12  WR=67.6%
- ny_close: n=26  W=14/L=12  WR=53.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W02.  `RSI=RSI6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W03.  `T1=T1c AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W04.  `H20=H20a AND T1=T1c AND direction_exec=short`
- Raw: n=41  W=41/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade

### W05.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=36  W=36/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade

### W06.  `H20=H20a AND H60=H60a AND direction_exec=short`
- Raw: n=36  W=36/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade

### W07.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=36  W=36/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade

### W08.  `H60=H60b AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=35  W=31/L=4  WR=88.6%
- Refine: exclude H20=H20b drops 4/4 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; upper third; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI6`
- Raw: n=32  W=32/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought

### W10.  `H20=H20a AND T1=T1c AND RSI=RSI6`
- Raw: n=32  W=32/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought

### W11.  `H20=H20a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=32  W=32/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 70-80 overbought

### W12.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=32  W=32/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought

### W13.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=32  W=32/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought

### W14.  `H20=H20a AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=32  W=32/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought

### W15.  `H20=H20d AND T1=T1a AND session_bucket=asia`
- Raw: n=32  W=30/L=2  WR=93.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; session=asia  •  AVOID when upper third

### W16.  `H20=H20d AND T4=T4a AND session_bucket=asia`
- Raw: n=32  W=30/L=2  WR=93.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W17.  `H20=H20d AND direction_exec=long AND session_bucket=asia`
- Raw: n=32  W=30/L=2  WR=93.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; session=asia  •  AVOID when upper third

### W18.  `H20=H20d AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=32  W=30/L=2  WR=93.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W19.  `H20=H20d AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=32  W=30/L=2  WR=93.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; session=asia  •  AVOID when upper third

### W20.  `H20=H20d AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=32  W=30/L=2  WR=93.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=31  W=28/L=3  WR=90.3%
- Refine: exclude H20=H20d drops 2/3 losers (67%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 mildly against

### W22.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=31  W=28/L=3  WR=90.3%
- Refine: exclude H20=H20d drops 2/3 losers (67%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 mildly against

### W23.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=31  W=28/L=3  WR=90.3%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF20 mildly against

### W24.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=31  W=28/L=3  WR=90.3%
- Refine: exclude H20=H20d drops 2/3 losers (67%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 mildly against

### W25.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=31  W=28/L=3  WR=90.3%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is H20=H20a (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is H20=H20a (8/23 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is H20=H20a (8/23 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L04.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is H20=H20a (8/23 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L05.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is H20=H20d (14/20 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF20 mildly against

### L06.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is H20=H20d (14/20 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when HTF20 mildly against

### L07.  `T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is H20=H20d (14/20 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band  •  ONLY when HTF20 mildly against

### L08.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is H20=H20d (14/20 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF20 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(21/12), H20b(36/30) | H20d(30/41) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(57/51) | long(43/49) |
| session_bucket | asia(23/17), london(17/12) | — |

*Read: `bucket(winner%/loser%)`.*
