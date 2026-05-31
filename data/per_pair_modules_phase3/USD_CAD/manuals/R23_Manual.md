# USD_CAD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,034**  (W=1,941 / L=1,093)  -  WR: **64.0%**

## Session distribution

- asia: n=1198  W=783/L=415  WR=65.4%
- ny_close: n=519  W=325/L=194  WR=62.6%
- ny_open: n=419  W=253/L=166  WR=60.4%
- london_open: n=354  W=227/L=127  WR=64.1%
- london: n=274  W=185/L=89  WR=67.5%
- ny_mid: n=121  W=83/L=38  WR=68.6%
- asia_late: n=85  W=50/L=35  WR=58.8%
- off_hours: n=64  W=35/L=29  WR=54.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=176  W=150/L=26  WR=85.2%
- Refine: exclude H60=H60b drops 8/26 losers (31%)
- **Final: n=168  W=150/L=18  WR=89.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 slightly aligned

### W02.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude BBP=BBP4 drops 14/23 losers (61%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when upper third

### W03.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude BBP=BBP4 drops 14/23 losers (61%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W04.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude BBP=BBP4 drops 14/23 losers (61%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when upper third

### W05.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude BBP=BBP4 drops 14/23 losers (61%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W06.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=157  W=136/L=21  WR=86.6%
- Refine: exclude RSI=RSI4 drops 12/21 losers (57%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W07.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=157  W=136/L=21  WR=86.6%
- Refine: exclude RSI=RSI4 drops 12/21 losers (57%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=157  W=136/L=21  WR=86.6%
- Refine: exclude RSI=RSI4 drops 12/21 losers (57%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when RSI 50-60 upper neutral

### W09.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude ZS=ZS4 drops 14/18 losers (78%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W10.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude ZS=ZS2 drops 4/16 losers (25%)
- **Final: n=108  W=96/L=12  WR=88.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W11.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude ZS=ZS2 drops 4/16 losers (25%)
- **Final: n=108  W=96/L=12  WR=88.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W12.  `T4=T4a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude RSI=RSI4 drops 8/11 losers (73%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W13.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude RSI=RSI4 drops 8/11 losers (73%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 50-60 upper neutral

### W14.  `T4=T4a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60b drops 7/10 losers (70%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 slightly aligned

### W15.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60b drops 7/10 losers (70%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 slightly aligned

### W16.  `T4=T4a AND BBP=BBP5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude RSI=RSI4 drops 6/9 losers (67%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W17.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude ZS=ZS5 drops 7/9 losers (78%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W18.  `H20=H20a AND H60=H60d AND T1=T1c AND session_bucket=asia`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude ZS=ZS3 drops 3/6 losers (50%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W19.  `H20=H20e AND H60=H60d AND RSI=RSI5`
- Raw: n=60  W=53/L=7  WR=88.3%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=london_open

### W20.  `H20=H20e AND H60=H60d AND T1=T1c AND RSI=RSI5`
- Raw: n=60  W=53/L=7  WR=88.3%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london_open

### W21.  `H20=H20e AND H60=H60d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=60  W=53/L=7  WR=88.3%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=london_open

### W22.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20e drops 4/9 losers (44%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; session=asia  •  AVOID when HTF20 strongly against

### W23.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude H60=H60b drops 4/7 losers (57%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W24.  `H20=H20e AND H60=H60d AND T4=T4c AND RSI=RSI5`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london_open

### W25.  `H60=H60d AND T1=T1c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude H20=H20a drops 3/6 losers (50%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is H20=H20a (48/79 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is H20=H20a (48/79 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=118  W=46/L=72  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (48/72 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 60-70 strong

### L04.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=118  W=46/L=72  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (48/72 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=118  W=46/L=72  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (48/72 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  ONLY when RSI 60-70 strong

### L06.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=102  W=37/L=65  WR=36.3%
- Sharpen: sharpest is H20=H20a (48/65 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L07.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is H60=H60a (33/50 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60a (33/49 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L09.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60a (33/49 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20b AND H60=H60e AND T4=T4a`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T1=T1c (10/45 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  ONLY when 1h trend AGAINST trade

### L11.  `H20=H20b AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T1=T1c (10/45 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  ONLY when 1h trend AGAINST trade

### L12.  `H20=H20a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L13.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L14.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L15.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is ZS=ZS4 (25/44 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L16.  `T4=T4c AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=70  W=21/L=49  WR=30.0%
- Sharpen: sharpest is H60=H60a (33/49 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L17.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=70  W=21/L=49  WR=30.0%
- Sharpen: sharpest is H60=H60a (33/49 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L18.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=69  W=21/L=48  WR=30.4%
- Sharpen: sharpest is H60=H60a (33/48 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L19.  `T4=T4c AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=69  W=21/L=48  WR=30.4%
- Sharpen: sharpest is H60=H60a (33/48 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L20.  `T4=T4c AND RSI=RSI5 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H60=H60e (8/41 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral; session=asia  •  ONLY when HTF60 strongly against

### L21.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is BBP=BBP4 (21/39 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L22.  `H60=H60c AND T1=T1c AND direction_exec=short`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is H20=H20d (9/36 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L23.  `H20=H20a AND H60=H60b AND T1=T1a`
- Raw: n=58  W=18/L=40  WR=31.0%
- Sharpen: sharpest is BBP=BBP6 (14/40 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade  •  ONLY when deep above upper band

### L24.  `H20=H20a AND H60=H60b AND direction_exec=long`
- Raw: n=58  W=18/L=40  WR=31.0%
- Sharpen: sharpest is BBP=BBP6 (14/40 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 slightly aligned  •  ONLY when deep above upper band

### L25.  `H20=H20a AND H60=H60b AND T1=T1a AND direction_exec=long`
- Raw: n=58  W=18/L=40  WR=31.0%
- Sharpen: sharpest is BBP=BBP6 (14/40 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60b(9/14) |
| T1 | T1a(55/45) | T1c(45/55) |
| T4 | T4a(54/44) | T4c(46/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/45) | short(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
