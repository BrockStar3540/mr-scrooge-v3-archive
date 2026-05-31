# USD_CAD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,948**  (W=1,270 / L=678)  -  WR: **65.2%**

## Session distribution

- asia: n=549  W=365/L=184  WR=66.5%
- ny_close: n=497  W=318/L=179  WR=64.0%
- ny_mid: n=250  W=165/L=85  WR=66.0%
- london_open: n=218  W=139/L=79  WR=63.8%
- london: n=181  W=129/L=52  WR=71.3%
- asia_late: n=128  W=81/L=47  WR=63.3%
- ny_open: n=70  W=37/L=33  WR=52.9%
- off_hours: n=55  W=36/L=19  WR=65.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20e drops 7/16 losers (44%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W02.  `H60=H60e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20e drops 7/16 losers (44%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W03.  `H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20e drops 7/16 losers (44%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_close  •  AVOID when HTF20 strongly against

### W04.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20e drops 7/16 losers (44%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W05.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20e drops 7/16 losers (44%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W06.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20e drops 7/16 losers (44%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W07.  `H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude session_bucket=asia_late drops 8/17 losers (47%)
- **Final: n=108  W=99/L=9  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W08.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude session_bucket=asia_late drops 8/17 losers (47%)
- **Final: n=108  W=99/L=9  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W09.  `H60=H60e AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude session_bucket=asia_late drops 8/17 losers (47%)
- **Final: n=108  W=99/L=9  WR=91.7%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W10.  `H20=H20c AND H60=H60e AND T1=T1a`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=asia

### W11.  `H20=H20c AND H60=H60e AND T4=T4a`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=asia

### W12.  `H20=H20c AND H60=H60e AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against  •  AVOID when session=asia

### W13.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W14.  `H20=H20c AND T1=T1a AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when session=asia

### W15.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when session=asia

### W16.  `H20=H20c AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W17.  `H20=H20c AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=asia

### W18.  `H20=H20c AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=asia

### W19.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W20.  `H20=H20b AND H60=H60e AND RSI=RSI6`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when session=london_open

### W21.  `H60=H60e AND T1=T1a AND BBP=BBP5`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band  •  AVOID when session=asia_late

### W22.  `H60=H60e AND T4=T4a AND BBP=BBP5`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; just touched upper band  •  AVOID when session=asia_late

### W23.  `H60=H60e AND BBP=BBP5 AND direction_exec=long`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band  •  AVOID when session=asia_late

### W24.  `H20=H20b AND H60=H60e AND T1=T1a AND RSI=RSI6`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=london_open

### W25.  `H20=H20b AND H60=H60e AND T4=T4a AND RSI=RSI6`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20c AND H60=H60a AND T1=T1c`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L02.  `H20=H20c AND H60=H60a AND T4=T4c`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L03.  `H20=H20c AND H60=H60a AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade  •  ONLY when session=ny_close

### L04.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L05.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L06.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L07.  `H20=H20c AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L08.  `H20=H20c AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L09.  `H20=H20c AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L10.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (36/50 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L11.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is H20=H20c (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L12.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is H20=H20c (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L13.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is H20=H20c (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  upper third; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L14.  `H60=H60e AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is T1=T1a (18/35 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=london_open  •  ONLY when 1h trend WITH trade

### L15.  `H60=H60e AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is T1=T1a (18/35 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend WITH trade

### L16.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is T1=T1a (18/35 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend WITH trade

### L17.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H20=H20c (18/35 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when HTF20 neutral

### L18.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H20=H20c (18/35 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; session=ny_close  •  ONLY when HTF20 neutral

### L19.  `H60=H60a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H20=H20c (18/35 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; session=ny_close  •  ONLY when HTF20 neutral

### L20.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is H20=H20c (11/38 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L21.  `T4=T4c AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is H20=H20c (11/38 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L22.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is H20=H20c (11/38 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L23.  `H20=H20d AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=51  W=16/L=35  WR=31.4%
- Sharpen: sharpest is session_bucket=asia (12/35 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; upper third; RSI 70-80 overbought  •  ONLY when session=asia

### L24.  `H20=H20d AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=51  W=16/L=35  WR=31.4%
- Sharpen: sharpest is session_bucket=asia (12/35 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=asia

### L25.  `H20=H20d AND T1=T1c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=51  W=16/L=35  WR=31.4%
- Sharpen: sharpest is session_bucket=asia (12/35 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/34) | H20e(31/39) |
| H60 | — | — |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(53/45) | T4c(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | ZS5(34/28) | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
