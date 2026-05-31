# EUR_CAD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,123**  (W=1,352 / L=771)  -  WR: **63.7%**

## Session distribution

- asia: n=856  W=569/L=287  WR=66.5%
- ny_close: n=290  W=179/L=111  WR=61.7%
- london_open: n=269  W=160/L=109  WR=59.5%
- asia_late: n=210  W=139/L=71  WR=66.2%
- london: n=207  W=133/L=74  WR=64.3%
- ny_open: n=165  W=97/L=68  WR=58.8%
- off_hours: n=72  W=44/L=28  WR=61.1%
- ny_mid: n=54  W=31/L=23  WR=57.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4a AND RSI=RSI5`
- Raw: n=159  W=137/L=22  WR=86.2%
- Refine: exclude ZS=ZS5 drops 14/22 losers (64%)
- **Final: n=130  W=122/L=8  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W02.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=159  W=137/L=22  WR=86.2%
- Refine: exclude ZS=ZS5 drops 14/22 losers (64%)
- **Final: n=130  W=122/L=8  WR=93.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W03.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=153  W=132/L=21  WR=86.3%
- Refine: exclude ZS=ZS5 drops 14/21 losers (67%)
- **Final: n=124  W=117/L=7  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W04.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude ZS=ZS5 drops 14/20 losers (70%)
- **Final: n=117  W=111/L=6  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W05.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=134  W=119/L=15  WR=88.8%
- Refine: exclude H60=H60a drops 13/15 losers (87%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  upper third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W06.  `T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=134  W=117/L=17  WR=87.3%
- Refine: exclude H60=H60a drops 13/17 losers (76%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W07.  `H20=H20e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude T1=T1a drops 14/14 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W08.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=127  W=113/L=14  WR=89.0%
- Refine: exclude H60=H60a drops 13/14 losers (93%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W09.  `H60=H60d AND T4=T4a AND RSI=RSI5`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude ZS=ZS4 drops 10/16 losers (62%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W10.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude H60=H60a drops 13/14 losers (93%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W11.  `H20=H20b AND H60=H60a AND T1=T1c`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude session_bucket=london_open drops 7/11 losers (64%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london_open

### W12.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W13.  `ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20a drops 10/13 losers (77%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W14.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20a drops 10/13 losers (77%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H60=H60e drops 5/14 losers (36%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  AVOID when HTF60 strongly against

### W16.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude T1=T1a drops 14/14 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W17.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude H20=H20a drops 10/13 losers (77%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude session_bucket=london_open drops 5/15 losers (33%)
- **Final: n=92  W=82/L=10  WR=89.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W19.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude session_bucket=london drops 9/14 losers (64%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london

### W20.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4c drops 12/14 losers (86%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W21.  `H60=H60d AND T1=T1a AND RSI=RSI5`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W22.  `H60=H60d AND RSI=RSI5 AND direction_exec=long`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=asia

### W23.  `H60=H60d AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W24.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=97  W=94/L=3  WR=96.9%
- Refine: exclude H20=H20a drops 3/3 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60d AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude session_bucket=asia drops 7/11 losers (64%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (30/63 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L02.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is H60=H60c (13/62 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 neutral

### L03.  `H20=H20a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is T1=T1a (36/60 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  ONLY when 1h trend WITH trade

### L04.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=91  W=30/L=61  WR=33.0%
- Sharpen: sharpest is H60=H60e (45/61 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L05.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is H60=H60e (37/58 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L06.  `H20=H20d AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=32/L=58  WR=35.6%
- Sharpen: sharpest is T4=T4c (58/58 of losers there)
- **Sharp: n=74  W=16/L=58  WR=21.6%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20d AND T1=T1a AND direction_exec=long`
- Raw: n=87  W=26/L=61  WR=29.9%
- Sharpen: sharpest is H60=H60e (45/61 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade  •  ONLY when HTF60 strongly against

### L08.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=26/L=61  WR=29.9%
- Sharpen: sharpest is H60=H60e (45/61 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L09.  `H20=H20d AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=26/L=61  WR=29.9%
- Sharpen: sharpest is H60=H60e (45/61 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L10.  `T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H60=H60e (33/52 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when HTF60 strongly against

### L11.  `H20=H20d AND T1=T1c AND ZS=ZS5`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is T4=T4c (50/50 of losers there)
- **Sharp: n=66  W=16/L=50  WR=24.2%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20d AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is T4=T4c (50/50 of losers there)
- **Sharp: n=66  W=16/L=50  WR=24.2%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20a AND H60=H60b AND RSI=RSI4`
- Raw: n=81  W=27/L=54  WR=33.3%
- Sharpen: sharpest is T4=T4c (29/54 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (36/47 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=75  W=13/L=62  WR=17.3%
- Sharpen: sharpest is direction_exec=short (25/62 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when short

### L16.  `H20=H20d AND T4=T4c AND ZS=ZS5`
- Raw: n=74  W=16/L=58  WR=21.6%
- Sharpen: sharpest is RSI=RSI5 (35/58 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L17.  `H20=H20d AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=74  W=16/L=58  WR=21.6%
- Sharpen: sharpest is RSI=RSI5 (35/58 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L18.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is ZS=ZS5 (17/52 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H20=H20a AND H60=H60b AND T4=T4a`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (21/46 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20a AND H60=H60b AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (21/46 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 slightly aligned  •  ONLY when RSI 60-70 strong

### L21.  `H20=H20a AND H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (21/46 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L22.  `H60=H60b AND T4=T4c AND RSI=RSI5`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is ZS=ZS5 (22/47 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is RSI=RSI5 (36/46 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  ONLY when RSI 60-70 strong

### L24.  `T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is H60=H60e (29/46 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L25.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is RSI=RSI5 (36/46 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(24/14), H20e(31/25) | H20d(14/22), H20a(24/29) |
| H60 | H60a(36/24), H60d(20/11) | H60e(28/37), H60b(11/20) |
| T1 | T1c(55/43) | T1a(45/57) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/46) | long(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
