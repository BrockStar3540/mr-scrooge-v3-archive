# NZD_USD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,697**  (W=1,769 / L=928)  -  WR: **65.6%**

## Session distribution

- asia: n=1044  W=700/L=344  WR=67.0%
- ny_close: n=492  W=313/L=179  WR=63.6%
- off_hours: n=287  W=178/L=109  WR=62.0%
- ny_open: n=257  W=166/L=91  WR=64.6%
- london: n=254  W=167/L=87  WR=65.7%
- asia_late: n=202  W=132/L=70  WR=65.3%
- ny_mid: n=82  W=57/L=25  WR=69.5%
- london_open: n=79  W=56/L=23  WR=70.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=179  W=163/L=16  WR=91.1%
- Refine: exclude session_bucket=ny_close drops 7/16 losers (44%)
- **Final: n=164  W=155/L=9  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W02.  `H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=165  W=141/L=24  WR=85.5%
- Refine: exclude T1=T1a drops 19/24 losers (79%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when 1h trend WITH trade

### W03.  `H60=H60a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=152  W=130/L=22  WR=85.5%
- Refine: no further refinement
- **Final: n=152  W=130/L=22  WR=85.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia

### W04.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=152  W=130/L=22  WR=85.5%
- Refine: no further refinement
- **Final: n=152  W=130/L=22  WR=85.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=asia

### W05.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=146  W=140/L=6  WR=95.9%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  AVOID when HTF60 strongly against

### W06.  `H20=H20e AND H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=133  W=114/L=19  WR=85.7%
- Refine: exclude T1=T1a drops 16/19 losers (84%)
- **Final: n=101  W=98/L=3  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W07.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=118  W=109/L=9  WR=92.4%
- Refine: exclude T4=T4c drops 4/9 losers (44%)
- **Final: n=114  W=109/L=5  WR=95.6%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when 4h trend AGAINST trade

### W08.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude T1=T1a drops 9/15 losers (60%)
- **Final: n=98  W=92/L=6  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W09.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=116  W=103/L=13  WR=88.8%
- Refine: exclude T4=T4c drops 12/13 losers (92%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W10.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=114  W=109/L=5  WR=95.6%
- Refine: exclude H60=H60e drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF60 strongly against

### W11.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=114  W=109/L=5  WR=95.6%
- Refine: exclude H60=H60e drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF60 strongly against

### W12.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=108  W=102/L=6  WR=94.4%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when middle of band

### W13.  `H20=H20a AND T4=T4a AND session_bucket=london`
- Raw: n=107  W=101/L=6  WR=94.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF60 strongly against

### W14.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=107  W=101/L=6  WR=94.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  AVOID when HTF60 strongly against

### W15.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=107  W=101/L=6  WR=94.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF60 strongly against

### W16.  `H20=H20a AND T4=T4a AND direction_exec=short`
- Raw: n=107  W=98/L=9  WR=91.6%
- Refine: exclude BBP=BBP2 drops 4/9 losers (44%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when lower third

### W17.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=107  W=98/L=9  WR=91.6%
- Refine: exclude BBP=BBP2 drops 4/9 losers (44%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when lower third

### W18.  `T4=T4a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=106  W=105/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=106  W=105/L=1  WR=99.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london

### W19.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude RSI=RSI5 drops 12/14 losers (86%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W20.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=105  W=96/L=9  WR=91.4%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W21.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=104  W=98/L=6  WR=94.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when middle of band

### W22.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude RSI=RSI5 drops 10/12 losers (83%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W23.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude direction_exec=short drops 12/14 losers (86%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when short

### W24.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=98  W=93/L=5  WR=94.9%
- Refine: exclude T4=T4c drops 4/5 losers (80%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london  •  AVOID when 4h trend AGAINST trade

### W25.  `H20=H20a AND RSI=RSI5 AND session_bucket=asia_late`
- Raw: n=96  W=94/L=2  WR=97.9%
- Refine: exclude H60=H60e drops 2/2 losers (100%)
- **Final: n=86  W=86/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia_late  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND T4=T4c`
- Raw: n=146  W=51/L=95  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (40/95 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L02.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP4`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is session_bucket=london (21/86 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when session=london

### L03.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is session_bucket=london (20/77 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=london

### L04.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is session_bucket=london (20/75 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when session=london

### L05.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is T4=T4c (40/58 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L06.  `T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=92  W=15/L=77  WR=16.3%
- Sharpen: sharpest is ZS=ZS4 (34/77 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london  •  ONLY when zscore +1 to +2 overbought

### L07.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is session_bucket=asia (26/57 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L08.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is session_bucket=asia (26/57 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L09.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=87  W=23/L=64  WR=26.4%
- Sharpen: sharpest is T4=T4c (64/64 of losers there)
- **Sharp: n=75  W=11/L=64  WR=14.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  ONLY when 4h trend AGAINST trade

### L10.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=86  W=34/L=52  WR=39.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=asia

### L11.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=79  W=30/L=49  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (19/49 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L12.  `T1=T1c AND T4=T4c AND session_bucket=london`
- Raw: n=75  W=11/L=64  WR=14.7%
- Sharpen: sharpest is ZS=ZS4 (28/64 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  ONLY when zscore +1 to +2 overbought

### L13.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=75  W=11/L=64  WR=14.7%
- Sharpen: sharpest is ZS=ZS4 (28/64 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  ONLY when zscore +1 to +2 overbought

### L14.  `H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=71  W=25/L=46  WR=35.2%
- Sharpen: sharpest is session_bucket=asia (16/46 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L15.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=70  W=23/L=47  WR=32.9%
- Sharpen: sharpest is T4=T4c (47/47 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (16/42 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L17.  `H60=H60e AND T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is H20=H20e (25/38 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L18.  `T4=T4c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=62  W=11/L=51  WR=17.7%
- Sharpen: sharpest is ZS=ZS4 (22/51 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london  •  ONLY when zscore +1 to +2 overbought

### L19.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=62  W=19/L=43  WR=30.6%
- Sharpen: sharpest is T4=T4c (43/43 of losers there)
- **Sharp: n=50  W=7/L=43  WR=14.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20e AND T1=T1a AND BBP=BBP4`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is ZS=ZS4 (34/38 of losers there)
- **Sharp: n=50  W=16/L=34  WR=32.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L21.  `H20=H20e AND T1=T1a AND direction_exec=short`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is H60=H60e (34/38 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when HTF60 strongly against

### L22.  `H20=H20e AND T4=T4c AND session_bucket=london`
- Raw: n=60  W=8/L=52  WR=13.3%
- Sharpen: sharpest is H60=H60e (29/52 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND direction_exec=short AND session_bucket=london`
- Raw: n=60  W=8/L=52  WR=13.3%
- Sharpen: sharpest is H60=H60e (29/52 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london  •  ONLY when HTF60 strongly against

### L24.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=60  W=8/L=52  WR=13.3%
- Sharpen: sharpest is H60=H60e (29/52 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  ONLY when HTF60 strongly against

### L25.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=60  W=12/L=48  WR=20.0%
- Sharpen: sharpest is BBP=BBP6 (20/48 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/32) | H20e(35/47) |
| H60 | H60a(53/37) | H60e(37/53) |
| T1 | — | — |
| T4 | T4a(54/44) | T4c(46/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
