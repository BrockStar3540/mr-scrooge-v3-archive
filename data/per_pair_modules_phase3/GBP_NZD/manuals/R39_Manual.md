# GBP_NZD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **9,230**  (W=5,070 / L=4,160)  -  WR: **54.9%**

## Session distribution

- ny_mid: n=2317  W=1236/L=1081  WR=53.3%
- asia: n=1941  W=1066/L=875  WR=54.9%
- ny_close: n=1490  W=830/L=660  WR=55.7%
- ny_open: n=1246  W=705/L=541  WR=56.6%
- london_open: n=875  W=495/L=380  WR=56.6%
- london: n=727  W=410/L=317  WR=56.4%
- off_hours: n=610  W=314/L=296  WR=51.5%
- asia_late: n=24  W=14/L=10  WR=58.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=asia drops 15/17 losers (88%)
- **Final: n=98  W=96/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=asia

### W02.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=95  W=87/L=8  WR=91.6%
- Refine: exclude session_bucket=ny_mid drops 5/8 losers (62%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude H60=H60d drops 6/9 losers (67%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when HTF60 mildly against

### W04.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP5`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude session_bucket=ny_mid drops 5/8 losers (62%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  AVOID when session=ny_mid

### W05.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude H60=H60d drops 6/9 losers (67%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when HTF60 mildly against

### W06.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND session_bucket=london`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london  •  AVOID when HTF60 aligned WITH trade

### W07.  `H20=H20e AND ZS=ZS5 AND direction_exec=short AND session_bucket=london`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought; session=london  •  AVOID when HTF60 aligned WITH trade

### W08.  `T1=T1c AND ZS=ZS5 AND session_bucket=off_hours`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20b drops 7/9 losers (78%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=off_hours  •  AVOID when HTF20 slightly aligned

### W09.  `ZS=ZS5 AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20b drops 7/9 losers (78%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=off_hours  •  AVOID when HTF20 slightly aligned

### W10.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20b drops 7/9 losers (78%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=off_hours  •  AVOID when HTF20 slightly aligned

### W11.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W12.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when just touched upper band

### W13.  `T4=T4c AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when just touched upper band

### W14.  `H20=H20a AND T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H60=H60d drops 6/6 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF60 mildly against

### W15.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W16.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  deep above upper band; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W17.  `H20=H20b AND H60=H60e AND session_bucket=london_open`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; session=london_open  •  AVOID when upper third

### W18.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W19.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W20.  `T1=T1c AND RSI=RSI6 AND ZS=ZS5 AND session_bucket=london`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought; session=london  •  AVOID when HTF60 aligned WITH trade

### W21.  `T4=T4c AND RSI=RSI6 AND ZS=ZS5 AND session_bucket=london`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought; session=london  •  AVOID when HTF60 aligned WITH trade

### W22.  `RSI=RSI6 AND ZS=ZS5 AND direction_exec=short AND session_bucket=london`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +2 to +3 deep overbought; session=london  •  AVOID when HTF60 aligned WITH trade

### W23.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP5`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude RSI=RSI6 drops 3/3 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when RSI 70-80 overbought

### W24.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS3 drops 7/8 losers (88%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60b AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude BBP=BBP5 drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=586  W=234/L=352  WR=39.9%
- Sharpen: sharpest is H20=H20e (86/352 of losers there)
- **Sharp: n=108  W=22/L=86  WR=20.4%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND BBP=BBP5 AND direction_exec=long`
- Raw: n=358  W=140/L=218  WR=39.1%
- Sharpen: sharpest is H20=H20e (56/218 of losers there)
- **Sharp: n=69  W=13/L=56  WR=18.8%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=358  W=140/L=218  WR=39.1%
- Sharpen: sharpest is H20=H20e (56/218 of losers there)
- **Sharp: n=69  W=13/L=56  WR=18.8%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L04.  `H60=H60e AND T1=T1a AND BBP=BBP5`
- Raw: n=352  W=140/L=212  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=352  W=140/L=212  WR=39.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band

### L05.  `H60=H60e AND T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=352  W=140/L=212  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=352  W=140/L=212  WR=39.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought

### L06.  `H60=H60e AND T1=T1a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=352  W=140/L=212  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=352  W=140/L=212  WR=39.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band

### L07.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=318  W=124/L=194  WR=39.0%
- Sharpen: sharpest is T4=T4a (55/194 of losers there)
- **Sharp: n=61  W=6/L=55  WR=9.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend WITH trade

### L08.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=318  W=124/L=194  WR=39.0%
- Sharpen: sharpest is T4=T4a (55/194 of losers there)
- **Sharp: n=61  W=6/L=55  WR=9.8%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open  •  ONLY when 4h trend WITH trade

### L09.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=318  W=124/L=194  WR=39.0%
- Sharpen: sharpest is T4=T4a (55/194 of losers there)
- **Sharp: n=61  W=6/L=55  WR=9.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60e AND T4=T4a AND BBP=BBP5`
- Raw: n=312  W=121/L=191  WR=38.8%
- Sharpen: sharpest is H20=H20e (40/191 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; just touched upper band  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=312  W=121/L=191  WR=38.8%
- Sharpen: sharpest is H20=H20e (40/191 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=306  W=121/L=185  WR=39.5%
- Sharpen: sharpest is H20=H20e (40/185 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; just touched upper band  •  ONLY when HTF20 strongly against

### L13.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=297  W=116/L=181  WR=39.1%
- Sharpen: sharpest is H20=H20e (47/181 of losers there)
- **Sharp: n=54  W=7/L=47  WR=13.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L14.  `T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is H20=H20a (111/160 of losers there)
- **Sharp: n=152  W=41/L=111  WR=27.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=off_hours  •  ONLY when HTF20 aligned WITH trade

### L15.  `H20=H20c AND T4=T4c AND RSI=RSI5`
- Raw: n=249  W=86/L=163  WR=34.5%
- Sharpen: sharpest is session_bucket=ny_mid (56/163 of losers there)
- **Sharp: n=61  W=5/L=56  WR=8.2%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L16.  `H20=H20c AND T1=T1c AND RSI=RSI5`
- Raw: n=248  W=74/L=174  WR=29.8%
- Sharpen: sharpest is session_bucket=ny_mid (56/174 of losers there)
- **Sharp: n=61  W=5/L=56  WR=8.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L17.  `H20=H20c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=248  W=74/L=174  WR=29.8%
- Sharpen: sharpest is session_bucket=ny_mid (56/174 of losers there)
- **Sharp: n=61  W=5/L=56  WR=8.2%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 60-70 strong  •  ONLY when session=ny_mid

### L18.  `H20=H20c AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=248  W=74/L=174  WR=29.8%
- Sharpen: sharpest is session_bucket=ny_mid (56/174 of losers there)
- **Sharp: n=61  W=5/L=56  WR=8.2%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L19.  `H20=H20c AND H60=H60a AND T4=T4c`
- Raw: n=236  W=90/L=146  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_mid (79/146 of losers there)
- **Sharp: n=91  W=12/L=79  WR=13.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L20.  `H20=H20c AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=236  W=90/L=146  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_mid (79/146 of losers there)
- **Sharp: n=91  W=12/L=79  WR=13.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L21.  `H20=H20c AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=236  W=90/L=146  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_mid (79/146 of losers there)
- **Sharp: n=91  W=12/L=79  WR=13.2%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L22.  `H20=H20c AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=225  W=68/L=157  WR=30.2%
- Sharpen: sharpest is ZS=ZS5 (68/157 of losers there)
- **Sharp: n=76  W=8/L=68  WR=10.5%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=225  W=68/L=157  WR=30.2%
- Sharpen: sharpest is ZS=ZS5 (68/157 of losers there)
- **Sharp: n=76  W=8/L=68  WR=10.5%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20a AND T1=T1a AND BBP=BBP5`
- Raw: n=215  W=84/L=131  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (35/131 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band  •  ONLY when session=ny_mid

### L25.  `H20=H20a AND T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=215  W=84/L=131  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (35/131 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
