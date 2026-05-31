# USD_JPY — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,655**  (W=2,282 / L=1,373)  -  WR: **62.4%**

## Session distribution

- asia: n=1385  W=865/L=520  WR=62.5%
- ny_close: n=960  W=614/L=346  WR=64.0%
- ny_open: n=341  W=213/L=128  WR=62.5%
- london: n=287  W=183/L=104  WR=63.8%
- off_hours: n=267  W=154/L=113  WR=57.7%
- london_open: n=149  W=84/L=65  WR=56.4%
- asia_late: n=142  W=89/L=53  WR=62.7%
- ny_mid: n=124  W=80/L=44  WR=64.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude session_bucket=ny_open drops 5/13 losers (38%)
- **Final: n=139  W=131/L=8  WR=94.2%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  AVOID when session=ny_open

### W02.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=137  W=119/L=18  WR=86.9%
- Refine: exclude H20=H20e drops 8/18 losers (44%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W03.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=125  W=112/L=13  WR=89.6%
- Refine: exclude session_bucket=ny_open drops 5/13 losers (38%)
- **Final: n=120  W=112/L=8  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W04.  `H20=H20d AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=125  W=112/L=13  WR=89.6%
- Refine: exclude session_bucket=ny_open drops 5/13 losers (38%)
- **Final: n=120  W=112/L=8  WR=93.3%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W05.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20e drops 5/17 losers (29%)
- **Final: n=111  W=99/L=12  WR=89.2%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W06.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude H20=H20e drops 7/16 losers (44%)
- **Final: n=105  W=96/L=9  WR=91.4%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W07.  `H20=H20d AND H60=H60a AND T4=T4a`
- Raw: n=118  W=106/L=12  WR=89.8%
- Refine: exclude RSI=RSI4 drops 10/12 losers (83%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20d AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=118  W=106/L=12  WR=89.8%
- Refine: exclude RSI=RSI4 drops 10/12 losers (83%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20c AND T1=T1a AND BBP=BBP4`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 7/15 losers (47%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; upper third  •  AVOID when session=ny_close

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude H20=H20e drops 6/15 losers (40%)
- **Final: n=95  W=86/L=9  WR=90.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W11.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 4/13 losers (31%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=echo_box_fade_v2

### W12.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude H20=H20e drops 6/15 losers (40%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W13.  `H20=H20d AND RSI=RSI4 AND direction_exec=long`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 5/12 losers (42%)
- **Final: n=102  W=95/L=7  WR=93.1%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W14.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude BBP=BBP5 drops 13/13 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W15.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude BBP=BBP5 drops 13/14 losers (93%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W16.  `H20=H20c AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 6/14 losers (43%)
- **Final: n=78  W=70/L=8  WR=89.7%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=ny_close

### W17.  `H20=H20c AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 6/14 losers (43%)
- **Final: n=78  W=70/L=8  WR=89.7%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; upper third  •  AVOID when session=ny_close

### W18.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=100  W=91/L=9  WR=91.0%
- Refine: exclude session_bucket=off_hours drops 3/9 losers (33%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W19.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude strategy_id=BR3_inside_bar_long drops 3/11 losers (27%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when strategy=BR3_inside_bar_long

### W20.  `H20=H20d AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude BBP=BBP4 drops 7/12 losers (58%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W21.  `H20=H20c AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/14 losers (43%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_close

### W22.  `H20=H20c AND T1=T1a AND ZS=ZS4`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 6/14 losers (43%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W23.  `H20=H20c AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 6/14 losers (43%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W24.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude session_bucket=asia_late drops 3/3 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W25.  `BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude session_bucket=asia_late drops 3/3 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=223  W=80/L=143  WR=35.9%
- Sharpen: sharpest is T4=T4c (121/143 of losers there)
- **Sharp: n=167  W=46/L=121  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=204  W=61/L=143  WR=29.9%
- Sharpen: sharpest is RSI=RSI4 (50/143 of losers there)
- **Sharp: n=57  W=7/L=50  WR=12.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L03.  `H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=200  W=61/L=139  WR=30.5%
- Sharpen: sharpest is RSI=RSI4 (46/139 of losers there)
- **Sharp: n=53  W=7/L=46  WR=13.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L04.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=200  W=61/L=139  WR=30.5%
- Sharpen: sharpest is RSI=RSI4 (46/139 of losers there)
- **Sharp: n=53  W=7/L=46  WR=13.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=191  W=62/L=129  WR=32.5%
- Sharpen: sharpest is RSI=RSI5 (59/129 of losers there)
- **Sharp: n=74  W=15/L=59  WR=20.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=191  W=62/L=129  WR=32.5%
- Sharpen: sharpest is RSI=RSI5 (59/129 of losers there)
- **Sharp: n=74  W=15/L=59  WR=20.3%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=191  W=62/L=129  WR=32.5%
- Sharpen: sharpest is RSI=RSI5 (59/129 of losers there)
- **Sharp: n=74  W=15/L=59  WR=20.3%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=182  W=56/L=126  WR=30.8%
- Sharpen: sharpest is RSI=RSI5 (56/126 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L09.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=182  W=56/L=126  WR=30.8%
- Sharpen: sharpest is RSI=RSI5 (56/126 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=182  W=56/L=126  WR=30.8%
- Sharpen: sharpest is RSI=RSI5 (56/126 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L11.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=181  W=67/L=114  WR=37.0%
- Sharpen: sharpest is RSI=RSI4 (50/114 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L12.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=181  W=67/L=114  WR=37.0%
- Sharpen: sharpest is RSI=RSI4 (53/114 of losers there)
- **Sharp: n=60  W=7/L=53  WR=11.7%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L13.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=177  W=67/L=110  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (49/110 of losers there)
- **Sharp: n=56  W=7/L=49  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L14.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=177  W=67/L=110  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (49/110 of losers there)
- **Sharp: n=56  W=7/L=49  WR=12.5%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L15.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=171  W=46/L=125  WR=26.9%
- Sharpen: sharpest is H20=H20b (26/125 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when HTF20 slightly aligned

### L16.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=170  W=43/L=127  WR=25.3%
- Sharpen: sharpest is ZS=ZS6 (36/127 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L17.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=169  W=59/L=110  WR=34.9%
- Sharpen: sharpest is RSI=RSI4 (50/110 of losers there)
- **Sharp: n=57  W=7/L=50  WR=12.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L18.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=167  W=46/L=121  WR=27.5%
- Sharpen: sharpest is H20=H20b (26/121 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when HTF20 slightly aligned

### L19.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=167  W=46/L=121  WR=27.5%
- Sharpen: sharpest is H20=H20b (26/121 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when HTF20 slightly aligned

### L20.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=165  W=59/L=106  WR=35.8%
- Sharpen: sharpest is RSI=RSI4 (46/106 of losers there)
- **Sharp: n=53  W=7/L=46  WR=13.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L21.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=159  W=41/L=118  WR=25.8%
- Sharpen: sharpest is ZS=ZS6 (31/118 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=159  W=41/L=118  WR=25.8%
- Sharpen: sharpest is ZS=ZS6 (31/118 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=132  W=41/L=91  WR=31.1%
- Sharpen: sharpest is RSI=RSI4 (30/91 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20b AND T1=T1c AND direction_exec=short`
- Raw: n=132  W=52/L=80  WR=39.4%
- Sharpen: sharpest is session_bucket=off_hours (25/80 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  ONLY when session=off_hours

### L25.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=129  W=39/L=90  WR=30.2%
- Sharpen: sharpest is RSI=RSI4 (33/90 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/31) | H20e(28/37) |
| H60 | H60a(54/43) | H60e(41/50) |
| T1 | T1a(59/45) | T1c(41/55) |
| T4 | T4a(57/46) | T4c(43/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/45) | short(42/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
