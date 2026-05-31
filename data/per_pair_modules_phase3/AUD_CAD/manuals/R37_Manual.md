# AUD_CAD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,968**  (W=1,275 / L=693)  -  WR: **64.8%**

## Session distribution

- asia: n=615  W=394/L=221  WR=64.1%
- london_open: n=371  W=227/L=144  WR=61.2%
- ny_open: n=288  W=188/L=100  WR=65.3%
- ny_mid: n=229  W=156/L=73  WR=68.1%
- london: n=229  W=148/L=81  WR=64.6%
- asia_late: n=149  W=102/L=47  WR=68.5%
- ny_close: n=65  W=44/L=21  WR=67.7%
- off_hours: n=22  W=16/L=6  WR=72.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=268  W=229/L=39  WR=85.4%
- Refine: exclude RSI=RSI3 drops 13/39 losers (33%)
- **Final: n=227  W=201/L=26  WR=88.5%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W02.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=193  W=165/L=28  WR=85.5%
- Refine: exclude H60=H60b drops 10/28 losers (36%)
- **Final: n=171  W=153/L=18  WR=89.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 slightly aligned

### W03.  `H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=188  W=160/L=28  WR=85.1%
- Refine: exclude session_bucket=london_open drops 14/28 losers (50%)
- **Final: n=149  W=135/L=14  WR=90.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=186  W=159/L=27  WR=85.5%
- Refine: exclude H20=H20c drops 14/27 losers (52%)
- **Final: n=153  W=140/L=13  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W05.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=181  W=159/L=22  WR=87.8%
- Refine: exclude H20=H20c drops 9/22 losers (41%)
- **Final: n=153  W=140/L=13  WR=91.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=181  W=159/L=22  WR=87.8%
- Refine: exclude H20=H20c drops 9/22 losers (41%)
- **Final: n=153  W=140/L=13  WR=91.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W07.  `H20=H20a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=174  W=150/L=24  WR=86.2%
- Refine: exclude session_bucket=london_open drops 15/24 losers (62%)
- **Final: n=138  W=129/L=9  WR=93.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W08.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=167  W=144/L=23  WR=86.2%
- Refine: exclude session_bucket=london_open drops 14/23 losers (61%)
- **Final: n=132  W=123/L=9  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W09.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=167  W=144/L=23  WR=86.2%
- Refine: exclude session_bucket=london_open drops 14/23 losers (61%)
- **Final: n=132  W=123/L=9  WR=93.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W10.  `T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=164  W=140/L=24  WR=85.4%
- Refine: exclude session_bucket=london_open drops 15/24 losers (62%)
- **Final: n=142  W=133/L=9  WR=93.7%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W11.  `H20=H20a AND H60=H60a AND ZS=ZS4`
- Raw: n=163  W=139/L=24  WR=85.3%
- Refine: exclude RSI=RSI6 drops 5/24 losers (21%)
- **Final: n=155  W=136/L=19  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 70-80 overbought

### W12.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=163  W=139/L=24  WR=85.3%
- Refine: exclude RSI=RSI6 drops 5/24 losers (21%)
- **Final: n=155  W=136/L=19  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 70-80 overbought

### W13.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=163  W=139/L=24  WR=85.3%
- Refine: exclude RSI=RSI6 drops 5/24 losers (21%)
- **Final: n=155  W=136/L=19  WR=87.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 70-80 overbought

### W14.  `H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude session_bucket=london_open drops 14/23 losers (61%)
- **Final: n=116  W=107/L=9  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W15.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude session_bucket=london drops 11/23 losers (48%)
- **Final: n=123  W=111/L=12  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=london

### W16.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude session_bucket=london_open drops 14/23 losers (61%)
- **Final: n=116  W=107/L=9  WR=92.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W17.  `H20=H20a AND T1=T1a AND ZS=ZS5`
- Raw: n=145  W=126/L=19  WR=86.9%
- Refine: exclude session_bucket=london_open drops 15/19 losers (79%)
- **Final: n=109  W=105/L=4  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W18.  `H20=H20a AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=145  W=126/L=19  WR=86.9%
- Refine: exclude session_bucket=london_open drops 15/19 losers (79%)
- **Final: n=109  W=105/L=4  WR=96.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W19.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude session_bucket=london_open drops 14/18 losers (78%)
- **Final: n=103  W=99/L=4  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W20.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude session_bucket=london_open drops 14/19 losers (74%)
- **Final: n=116  W=111/L=5  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W21.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude session_bucket=london_open drops 14/19 losers (74%)
- **Final: n=116  W=111/L=5  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W22.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude session_bucket=london_open drops 14/19 losers (74%)
- **Final: n=116  W=111/L=5  WR=95.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W23.  `H20=H20c AND T4=T4a AND session_bucket=asia`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude RSI=RSI5 drops 10/15 losers (67%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W24.  `H20=H20a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude RSI=RSI3 drops 7/15 losers (47%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W25.  `H20=H20a AND T4=T4a AND ZS=ZS4`
- Raw: n=130  W=112/L=18  WR=86.2%
- Refine: exclude T1=T1a drops 15/18 losers (83%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=196  W=70/L=126  WR=35.7%
- Sharpen: sharpest is H20=H20c (32/126 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 neutral

### L02.  `T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=190  W=66/L=124  WR=34.7%
- Sharpen: sharpest is BBP=BBP4 (51/124 of losers there)
- **Sharp: n=66  W=15/L=51  WR=22.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L03.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=190  W=74/L=116  WR=38.9%
- Sharpen: sharpest is H20=H20e (60/116 of losers there)
- **Sharp: n=72  W=12/L=60  WR=16.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L04.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=170  W=68/L=102  WR=40.0%
- Sharpen: sharpest is H20=H20e (79/102 of losers there)
- **Sharp: n=112  W=33/L=79  WR=29.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=169  W=61/L=108  WR=36.1%
- Sharpen: sharpest is RSI=RSI5 (44/108 of losers there)
- **Sharp: n=46  W=2/L=44  WR=4.3%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=141  W=47/L=94  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (34/94 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L07.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is RSI=RSI5 (44/92 of losers there)
- **Sharp: n=46  W=2/L=44  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is RSI=RSI5 (44/92 of losers there)
- **Sharp: n=46  W=2/L=44  WR=4.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L09.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=137  W=46/L=91  WR=33.6%
- Sharpen: sharpest is H20=H20e (60/91 of losers there)
- **Sharp: n=66  W=6/L=60  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L10.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=137  W=54/L=83  WR=39.4%
- Sharpen: sharpest is H60=H60c (20/83 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  ONLY when HTF60 neutral

### L11.  `H20=H20e AND H60=H60e AND ZS=ZS5`
- Raw: n=136  W=45/L=91  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (34/91 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20e AND H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=136  W=45/L=91  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (34/91 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L13.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=131  W=40/L=91  WR=30.5%
- Sharpen: sharpest is H20=H20e (60/91 of losers there)
- **Sharp: n=66  W=6/L=60  WR=9.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=131  W=40/L=91  WR=30.5%
- Sharpen: sharpest is H20=H20e (60/91 of losers there)
- **Sharp: n=66  W=6/L=60  WR=9.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L15.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is H60=H60c (20/83 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 neutral

### L16.  `H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is H20=H20e (71/81 of losers there)
- **Sharp: n=94  W=23/L=71  WR=24.5%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band  •  ONLY when HTF20 strongly against

### L17.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=116  W=42/L=74  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (29/74 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L18.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=116  W=42/L=74  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (29/74 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L19.  `H20=H20e AND T1=T1c AND ZS=ZS5`
- Raw: n=112  W=33/L=79  WR=29.5%
- Sharpen: sharpest is RSI=RSI5 (34/79 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=112  W=33/L=79  WR=29.5%
- Sharpen: sharpest is RSI=RSI5 (34/79 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=112  W=43/L=69  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (29/69 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=43/L=69  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (29/69 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (33/66 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london_open

### L24.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=108  W=36/L=72  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (28/72 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L25.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=108  W=36/L=72  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (28/72 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(42/23) | H20e(23/41) |
| H60 | H60a(50/31) | H60e(31/48) |
| T1 | T1a(57/43) | T1c(43/57) |
| T4 | T4a(55/43) | T4c(45/57) |
| BBP | — | — |
| RSI | RSI3(33/26) | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(62/40) | short(38/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
