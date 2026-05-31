# GBP_NZD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,716**  (W=3,487 / L=2,229)  -  WR: **61.0%**

## Session distribution

- asia: n=2049  W=1258/L=791  WR=61.4%
- london_open: n=1196  W=726/L=470  WR=60.7%
- london: n=825  W=516/L=309  WR=62.5%
- asia_late: n=605  W=358/L=247  WR=59.2%
- ny_open: n=564  W=328/L=236  WR=58.2%
- ny_close: n=215  W=139/L=76  WR=64.7%
- ny_mid: n=213  W=135/L=78  WR=63.4%
- off_hours: n=49  W=27/L=22  WR=55.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=279  W=239/L=40  WR=85.7%
- Refine: exclude BBP=BBP4 drops 28/40 losers (70%)
- **Final: n=132  W=120/L=12  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when upper third

### W02.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=279  W=239/L=40  WR=85.7%
- Refine: exclude BBP=BBP4 drops 28/40 losers (70%)
- **Final: n=132  W=120/L=12  WR=90.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when upper third

### W03.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=256  W=220/L=36  WR=85.9%
- Refine: exclude H20=H20a drops 22/36 losers (61%)
- **Final: n=187  W=173/L=14  WR=92.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=207  W=180/L=27  WR=87.0%
- Refine: exclude session_bucket=london drops 13/27 losers (48%)
- **Final: n=192  W=178/L=14  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W05.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=london drops 4/18 losers (22%)
- **Final: n=122  W=108/L=14  WR=88.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=london

### W06.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 strongly against

### W07.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude direction_exec=short drops 9/17 losers (53%)
- **Final: n=116  W=108/L=8  WR=93.1%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when short

### W08.  `H20=H20b AND T1=T1a AND session_bucket=london_open`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H60=H60e drops 5/17 losers (29%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W09.  `H60=H60a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=121  W=114/L=7  WR=94.2%
- Refine: exclude H20=H20c drops 7/7 losers (100%)
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W10.  `H20=H20b AND H60=H60a AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20b AND direction_exec=long AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; session=london_open  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20b AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20b AND H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20b AND H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W15.  `H20=H20b AND T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20b AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20b AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20a AND H60=H60e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude RSI=RSI7 drops 5/13 losers (38%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; deep above upper band  •  AVOID when RSI>80 extreme overbought

### W19.  `H60=H60e AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude RSI=RSI7 drops 5/13 losers (38%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; deep above upper band  •  AVOID when RSI>80 extreme overbought

### W20.  `H60=H60d AND T4=T4c AND RSI=RSI5`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude BBP=BBP6 drops 10/11 losers (91%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W21.  `H60=H60d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude BBP=BBP6 drops 10/11 losers (91%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 60-70 strong  •  AVOID when deep above upper band

### W22.  `H60=H60d AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude BBP=BBP6 drops 10/11 losers (91%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W23.  `H60=H60d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude BBP=BBP6 drops 10/11 losers (91%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W24.  `H60=H60d AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude BBP=BBP6 drops 10/11 losers (91%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W25.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia_late`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude H60=H60b drops 5/9 losers (56%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia_late  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=360  W=143/L=217  WR=39.7%
- Sharpen: sharpest is H60=H60e (161/217 of losers there)
- **Sharp: n=213  W=52/L=161  WR=24.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF60 strongly against

### L02.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=360  W=143/L=217  WR=39.7%
- Sharpen: sharpest is H60=H60e (161/217 of losers there)
- **Sharp: n=213  W=52/L=161  WR=24.4%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open  •  ONLY when HTF60 strongly against

### L03.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=360  W=143/L=217  WR=39.7%
- Sharpen: sharpest is H60=H60e (161/217 of losers there)
- **Sharp: n=213  W=52/L=161  WR=24.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF60 strongly against

### L04.  `H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=328  W=122/L=206  WR=37.2%
- Sharpen: sharpest is T1=T1c (161/206 of losers there)
- **Sharp: n=213  W=52/L=161  WR=24.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when 1h trend AGAINST trade

### L05.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=250  W=83/L=167  WR=33.2%
- Sharpen: sharpest is session_bucket=asia (82/167 of losers there)
- **Sharp: n=89  W=7/L=82  WR=7.9%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L06.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=241  W=83/L=158  WR=34.4%
- Sharpen: sharpest is session_bucket=asia (73/158 of losers there)
- **Sharp: n=80  W=7/L=73  WR=8.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L07.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=241  W=91/L=150  WR=37.8%
- Sharpen: sharpest is H60=H60c (53/150 of losers there)
- **Sharp: n=68  W=15/L=53  WR=22.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 neutral

### L08.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=241  W=91/L=150  WR=37.8%
- Sharpen: sharpest is H60=H60c (53/150 of losers there)
- **Sharp: n=68  W=15/L=53  WR=22.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 neutral

### L09.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=241  W=91/L=150  WR=37.8%
- Sharpen: sharpest is H60=H60c (53/150 of losers there)
- **Sharp: n=68  W=15/L=53  WR=22.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 neutral

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=241  W=91/L=150  WR=37.8%
- Sharpen: sharpest is H60=H60c (53/150 of losers there)
- **Sharp: n=68  W=15/L=53  WR=22.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 neutral

### L11.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=224  W=86/L=138  WR=38.4%
- Sharpen: sharpest is session_bucket=asia (51/138 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L12.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=216  W=70/L=146  WR=32.4%
- Sharpen: sharpest is session_bucket=asia (67/146 of losers there)
- **Sharp: n=74  W=7/L=67  WR=9.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L13.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=213  W=52/L=161  WR=24.4%
- Sharpen: sharpest is H20=H20b (28/161 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 slightly aligned

### L14.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=213  W=52/L=161  WR=24.4%
- Sharpen: sharpest is H20=H20b (28/161 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 slightly aligned

### L15.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=202  W=80/L=122  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (58/122 of losers there)
- **Sharp: n=72  W=14/L=58  WR=19.4%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong  •  ONLY when session=london_open

### L16.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=202  W=80/L=122  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (58/122 of losers there)
- **Sharp: n=72  W=14/L=58  WR=19.4%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L17.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=194  W=77/L=117  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (93/117 of losers there)
- **Sharp: n=124  W=31/L=93  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=london_open  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20a AND BBP=BBP4 AND session_bucket=london`
- Raw: n=185  W=69/L=116  WR=37.3%
- Sharpen: sharpest is H60=H60e (64/116 of losers there)
- **Sharp: n=88  W=24/L=64  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london  •  ONLY when HTF60 strongly against

### L19.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=185  W=70/L=115  WR=37.8%
- Sharpen: sharpest is RSI=RSI5 (93/115 of losers there)
- **Sharp: n=124  W=31/L=93  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=london_open  •  ONLY when RSI 60-70 strong

### L20.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=181  W=54/L=127  WR=29.8%
- Sharpen: sharpest is H20=H20b (28/127 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 slightly aligned

### L21.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=176  W=60/L=116  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (51/116 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L22.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=176  W=60/L=116  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (51/116 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L23.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=167  W=54/L=113  WR=32.3%
- Sharpen: sharpest is session_bucket=asia (45/113 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L24.  `H60=H60e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=166  W=59/L=107  WR=35.5%
- Sharpen: sharpest is session_bucket=asia (48/107 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band  •  ONLY when session=asia

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=166  W=59/L=107  WR=35.5%
- Sharpen: sharpest is session_bucket=asia (48/107 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/45) | T1c(48/55) |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/45) | short(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
