# NZD_CHF — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **431**  (W=278 / L=153)  -  WR: **64.5%**

## Session distribution

- london_open: n=131  W=81/L=50  WR=61.8%
- asia: n=89  W=56/L=33  WR=62.9%
- ny_open: n=61  W=43/L=18  WR=70.5%
- london: n=54  W=34/L=20  WR=63.0%
- off_hours: n=38  W=23/L=15  WR=60.5%
- ny_mid: n=32  W=24/L=8  WR=75.0%
- ny_close: n=26  W=17/L=9  WR=65.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W02.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W03.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H20=H20d drops 5/6 losers (83%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W04.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H20=H20d drops 5/6 losers (83%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W05.  `H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=69  W=66/L=3  WR=95.7%
- Refine: exclude session_bucket=ny_close drops 2/3 losers (67%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_close

### W06.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude session_bucket=asia drops 6/7 losers (86%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W07.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=62  W=60/L=2  WR=96.8%
- Refine: no further refinement
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong

### W08.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=62  W=60/L=2  WR=96.8%
- Refine: no further refinement
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong

### W09.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=62  W=60/L=2  WR=96.8%
- Refine: no further refinement
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong

### W10.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=59  W=58/L=1  WR=98.3%
- Refine: no further refinement
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade

### W11.  `H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=59  W=58/L=1  WR=98.3%
- Refine: no further refinement
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade

### W12.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=59  W=58/L=1  WR=98.3%
- Refine: no further refinement
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade

### W13.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude session_bucket=asia drops 6/7 losers (86%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W14.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=53  W=52/L=1  WR=98.1%
- Refine: no further refinement
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### W15.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=53  W=52/L=1  WR=98.1%
- Refine: no further refinement
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong

### W16.  `H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude session_bucket=london_open drops 4/5 losers (80%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=london_open

### W17.  `H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=52  W=48/L=4  WR=92.3%
- Refine: exclude session_bucket=london_open drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W18.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=52  W=48/L=4  WR=92.3%
- Refine: exclude session_bucket=london_open drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W19.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W20.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W21.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude session_bucket=london_open drops 4/5 losers (80%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W22.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=50  W=46/L=4  WR=92.0%
- Refine: exclude session_bucket=london_open drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W23.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W24.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W25.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (11/31 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L02.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is T1=T1a (16/27 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L03.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is T1=T1a (16/27 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L04.  `H20=H20e AND H60=H60e AND BBP=BBP4`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is ZS=ZS4 (23/23 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third  •  ONLY when zscore +1 to +2 overbought

### L05.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=37  W=11/L=26  WR=29.7%
- Sharpen: sharpest is H60=H60e (14/26 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is T1=T1a (13/22 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend WITH trade

### L07.  `H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=35  W=7/L=28  WR=20.0%
- Sharpen: sharpest is T4=T4c (25/28 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade  •  ONLY when 4h trend AGAINST trade

### L08.  `H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=35  W=12/L=23  WR=34.3%
- Sharpen: sharpest is T1=T1a (14/23 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L09.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=35  W=12/L=23  WR=34.3%
- Sharpen: sharpest is T1=T1a (14/23 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=34  W=9/L=25  WR=26.5%
- Sharpen: sharpest is T1=T1a (15/25 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L11.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=34  W=11/L=23  WR=32.4%
- Sharpen: sharpest is H60=H60e (11/23 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L12.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=34  W=11/L=23  WR=32.4%
- Sharpen: sharpest is H60=H60e (11/23 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L13.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=34  W=11/L=23  WR=32.4%
- Sharpen: sharpest is H60=H60e (11/23 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L14.  `H20=H20e AND H60=H60e AND ZS=ZS4`
- Raw: n=32  W=9/L=23  WR=28.1%
- Sharpen: sharpest is RSI=RSI5 (17/23 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=32  W=9/L=23  WR=28.1%
- Sharpen: sharpest is RSI=RSI5 (17/23 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L16.  `T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is H60=H60e (14/20 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  ONLY when HTF60 strongly against

### L17.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is H60=H60e (14/20 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  ONLY when HTF60 strongly against

### L18.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is H60=H60e (14/20 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/29) | H20b(12/20), H20e(30/35) |
| H60 | H60a(41/22) | H60e(17/36) |
| T1 | T1c(65/37) | T1a(35/63) |
| T4 | T4a(59/48) | T4c(41/52) |
| BBP | BBP4(58/52) | BBP5(14/20) |
| RSI | — | — |
| ZS | — | ZS5(23/31) |
| strategy_id | — | — |
| direction_exec | short(65/37) | long(35/63) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
