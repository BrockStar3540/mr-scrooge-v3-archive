# AUD_USD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,003**  (W=1,932 / L=1,071)  -  WR: **64.3%**

## Session distribution

- asia: n=1222  W=762/L=460  WR=62.4%
- ny_close: n=511  W=342/L=169  WR=66.9%
- ny_open: n=318  W=210/L=108  WR=66.0%
- london_open: n=216  W=137/L=79  WR=63.4%
- london: n=216  W=140/L=76  WR=64.8%
- off_hours: n=188  W=131/L=57  WR=69.7%
- asia_late: n=178  W=114/L=64  WR=64.0%
- ny_mid: n=154  W=96/L=58  WR=62.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP5 drops 10/15 losers (67%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when just touched upper band

### W02.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP5 drops 10/15 losers (67%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when just touched upper band

### W03.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=114  W=100/L=14  WR=87.7%
- Refine: exclude BBP=BBP5 drops 10/14 losers (71%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W04.  `T4=T4a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude RSI=RSI5 drops 13/13 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W05.  `T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude RSI=RSI5 drops 13/15 losers (87%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  1h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W06.  `T1=T1a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude RSI=RSI5 drops 13/13 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W07.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude RSI=RSI5 drops 13/13 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W08.  `H60=H60a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W09.  `H60=H60a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W10.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W11.  `H60=H60a AND T1=T1a AND session_bucket=off_hours`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W12.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W13.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W14.  `H20=H20a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W15.  `H20=H20a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W17.  `H20=H20a AND T1=T1a AND session_bucket=off_hours`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W18.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W19.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=off_hours  •  AVOID when RSI 60-70 strong

### W20.  `H20=H20c AND T1=T1c AND RSI=RSI5`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20c AND T4=T4c AND RSI=RSI5`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20c AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20c AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is BBP=BBP6 (28/51 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L02.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is BBP=BBP6 (28/51 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L03.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is T1=T1a (13/48 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L04.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is T1=T1a (13/48 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L05.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=72  W=24/L=48  WR=33.3%
- Sharpen: sharpest is BBP=BBP6 (28/48 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L06.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is H60=H60c (16/45 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 neutral

### L07.  `H20=H20c AND T1=T1a AND direction_exec=long`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is H60=H60c (16/45 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade  •  ONLY when HTF60 neutral

### L08.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is H60=H60c (16/45 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 neutral

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is ZS=ZS6 (7/41 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore >+3 extreme

### L10.  `H60=H60e AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is H20=H20e (26/37 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=off_hours  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (18/36 of losers there)
- **Sharp: n=25  W=7/L=18  WR=28.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L12.  `H60=H60e AND T1=T1c AND session_bucket=off_hours`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is H20=H20e (24/35 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=off_hours  •  ONLY when HTF20 strongly against

### L13.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is H20=H20e (24/35 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=off_hours  •  ONLY when HTF20 strongly against

### L14.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is T1=T1c (14/35 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=asia  •  ONLY when 1h trend AGAINST trade

### L15.  `BBP=BBP6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is ZS=ZS6 (7/34 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  deep above upper band; session=ny_open  •  ONLY when zscore >+3 extreme

### L16.  `H20=H20c AND T1=T1a AND RSI=RSI5`
- Raw: n=53  W=15/L=38  WR=28.3%
- Sharpen: sharpest is H60=H60c (16/38 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 neutral

### L17.  `H20=H20c AND T4=T4a AND RSI=RSI5`
- Raw: n=53  W=15/L=38  WR=28.3%
- Sharpen: sharpest is H60=H60c (16/38 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 neutral

### L18.  `H20=H20c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=53  W=15/L=38  WR=28.3%
- Sharpen: sharpest is H60=H60c (16/38 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 neutral; RSI 60-70 strong  •  ONLY when HTF60 neutral

### L19.  `H20=H20c AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=53  W=15/L=38  WR=28.3%
- Sharpen: sharpest is H60=H60c (16/38 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 neutral

### L20.  `H20=H20c AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=53  W=15/L=38  WR=28.3%
- Sharpen: sharpest is H60=H60c (16/38 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 neutral

### L21.  `H20=H20c AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=53  W=15/L=38  WR=28.3%
- Sharpen: sharpest is H60=H60c (16/38 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 neutral

### L22.  `H20=H20e AND BBP=BBP6 AND session_bucket=ny_open`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is ZS=ZS6 (7/35 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; session=ny_open  •  ONLY when zscore >+3 extreme

### L23.  `T4=T4c AND BBP=BBP6 AND session_bucket=ny_open`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is H60=H60e (28/35 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; session=ny_open  •  ONLY when HTF60 strongly against

### L24.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is BBP=BBP6 (18/32 of losers there)
- **Sharp: n=25  W=7/L=18  WR=28.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L25.  `H20=H20e AND BBP=BBP6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is T4=T4c (34/34 of losers there)
- **Sharp: n=48  W=14/L=34  WR=29.2%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; session=ny_open  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/35) | H20e(37/45) |
| H60 | H60a(46/36) | H60e(37/47) |
| T1 | T1a(54/45) | T1c(46/54) |
| T4 | T4a(54/44) | T4c(46/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/43) | short(45/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
