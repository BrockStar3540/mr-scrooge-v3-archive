# EUR_JPY — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **5,018**  (W=3,114 / L=1,904)  -  WR: **62.1%**

## Session distribution

- asia: n=1759  W=1078/L=681  WR=61.3%
- ny_close: n=1214  W=774/L=440  WR=63.8%
- ny_open: n=531  W=330/L=201  WR=62.1%
- london_open: n=396  W=244/L=152  WR=61.6%
- london: n=370  W=234/L=136  WR=63.2%
- off_hours: n=288  W=182/L=106  WR=63.2%
- ny_mid: n=244  W=146/L=98  WR=59.8%
- asia_late: n=216  W=126/L=90  WR=58.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  AVOID when deep above upper band

### W02.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W03.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W04.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when deep above upper band

### W05.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W06.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  AVOID when deep above upper band

### W08.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W09.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W10.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude BBP=BBP6 drops 6/21 losers (29%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W11.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20b drops 12/19 losers (63%)
- **Final: n=107  W=100/L=7  WR=93.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20b drops 12/19 losers (63%)
- **Final: n=107  W=100/L=7  WR=93.5%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade  •  AVOID when HTF20 slightly aligned

### W13.  `H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20b drops 12/19 losers (63%)
- **Final: n=107  W=100/L=7  WR=93.5%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when HTF20 slightly aligned

### W14.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20b drops 12/19 losers (63%)
- **Final: n=107  W=100/L=7  WR=93.5%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF20 slightly aligned

### W15.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W16.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W17.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W18.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W19.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W20.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W21.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W22.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W23.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W24.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W25.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=209  W=80/L=129  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=209  W=80/L=129  WR=38.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### L02.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=172  W=65/L=107  WR=37.8%
- Sharpen: sharpest is RSI=RSI6 (45/107 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L03.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=172  W=65/L=107  WR=37.8%
- Sharpen: sharpest is RSI=RSI6 (45/107 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L04.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=172  W=65/L=107  WR=37.8%
- Sharpen: sharpest is RSI=RSI6 (45/107 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L05.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=172  W=65/L=107  WR=37.8%
- Sharpen: sharpest is RSI=RSI6 (45/107 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L06.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (40/102 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L07.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (40/102 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L08.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (40/102 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  ONLY when RSI 70-80 overbought

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (40/102 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L10.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (40/102 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L11.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (40/102 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L12.  `H20=H20e AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=140  W=48/L=92  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=48/L=92  WR=34.3%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 70-80 overbought

### L13.  `H20=H20e AND BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=140  W=48/L=92  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=48/L=92  WR=34.3%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### L14.  `H20=H20e AND T1=T1c AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=132  W=48/L=84  WR=36.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band; RSI 70-80 overbought

### L15.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=132  W=48/L=84  WR=36.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; RSI 70-80 overbought

### L16.  `H20=H20e AND BBP=BBP5 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=132  W=48/L=84  WR=36.4%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; RSI 70-80 overbought

### L17.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=117  W=43/L=74  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=117  W=43/L=74  WR=36.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band; RSI 70-80 overbought

### L18.  `T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is H20=H20e (20/70 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=off_hours  •  ONLY when HTF20 strongly against

### L19.  `T1=T1a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=112  W=43/L=69  WR=38.4%
- Sharpen: sharpest is H20=H20e (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 strongly against

### L20.  `T4=T4a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=112  W=43/L=69  WR=38.4%
- Sharpen: sharpest is H20=H20e (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=off_hours  •  ONLY when HTF20 strongly against

### L21.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=112  W=43/L=69  WR=38.4%
- Sharpen: sharpest is H20=H20e (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 strongly against

### L22.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=107  W=33/L=74  WR=30.8%
- Sharpen: sharpest is ZS=ZS4 (48/74 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L23.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=107  W=33/L=74  WR=30.8%
- Sharpen: sharpest is ZS=ZS4 (48/74 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L24.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=107  W=33/L=74  WR=30.8%
- Sharpen: sharpest is ZS=ZS4 (48/74 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L25.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=107  W=33/L=74  WR=30.8%
- Sharpen: sharpest is ZS=ZS4 (48/74 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(48/37) | H20e(37/47) |
| H60 | H60a(50/42) | H60e(41/51) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
