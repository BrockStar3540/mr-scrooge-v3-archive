# EUR_NZD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,277**  (W=3,754 / L=2,523)  -  WR: **59.8%**

## Session distribution

- asia: n=2282  W=1400/L=882  WR=61.3%
- london_open: n=1286  W=769/L=517  WR=59.8%
- ny_open: n=659  W=353/L=306  WR=53.6%
- london: n=570  W=347/L=223  WR=60.9%
- ny_close: n=557  W=325/L=232  WR=58.3%
- ny_mid: n=458  W=295/L=163  WR=64.4%
- asia_late: n=356  W=206/L=150  WR=57.9%
- off_hours: n=109  W=59/L=50  WR=54.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 15/22 losers (68%)
- **Final: n=124  W=117/L=7  WR=94.4%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W02.  `H20=H20d AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 15/22 losers (68%)
- **Final: n=124  W=117/L=7  WR=94.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W03.  `H20=H20d AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 15/22 losers (68%)
- **Final: n=124  W=117/L=7  WR=94.4%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude H20=H20e drops 13/14 losers (93%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W05.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude H20=H20e drops 13/14 losers (93%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=118  W=108/L=10  WR=91.5%
- Refine: exclude T4=T4c drops 8/10 losers (80%)
- **Final: n=86  W=84/L=2  WR=97.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W07.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=118  W=108/L=10  WR=91.5%
- Refine: exclude T4=T4c drops 8/10 losers (80%)
- **Final: n=86  W=84/L=2  WR=97.7%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W08.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=114  W=101/L=13  WR=88.6%
- Refine: exclude H20=H20b drops 11/13 losers (85%)
- **Final: n=100  W=98/L=2  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W09.  `T1=T1a AND T4=T4a AND RSI=RSI7`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=asia_late drops 10/17 losers (59%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=asia_late

### W10.  `T1=T1a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=asia_late drops 10/17 losers (59%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=asia_late

### W11.  `T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=asia_late drops 10/17 losers (59%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=asia_late

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=asia_late drops 10/17 losers (59%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=asia_late

### W13.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=109  W=99/L=10  WR=90.8%
- Refine: exclude T4=T4c drops 8/10 losers (80%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W14.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=109  W=99/L=10  WR=90.8%
- Refine: exclude T4=T4c drops 8/10 losers (80%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20a AND H60=H60e AND T4=T4a AND BBP=BBP5`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 4/13 losers (31%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; just touched upper band  •  AVOID when strategy=delta_tag_and_go_v2

### W16.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude H20=H20b drops 11/13 losers (85%)
- **Final: n=91  W=89/L=2  WR=97.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W17.  `H20=H20a AND H60=H60e AND BBP=BBP5 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 4/13 losers (31%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; just touched upper band  •  AVOID when strategy=delta_tag_and_go_v2

### W18.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/13 losers (23%)
- **Final: n=86  W=76/L=10  WR=88.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band; session=asia  •  AVOID when strategy=delta_tag_and_go_v2

### W19.  `H20=H20a AND H60=H60e AND T1=T1a AND BBP=BBP5`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 4/12 losers (33%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; just touched upper band  •  AVOID when strategy=delta_tag_and_go_v2

### W20.  `H60=H60b AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude T1=T1a drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF60 slightly aligned; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W21.  `H20=H20e AND H60=H60b AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude T1=T1a drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W23.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W24.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=83  W=79/L=4  WR=95.2%
- Refine: exclude BBP=BBP3 drops 4/4 losers (100%)
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when middle of band

### W25.  `H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=83  W=79/L=4  WR=95.2%
- Refine: exclude BBP=BBP3 drops 4/4 losers (100%)
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_mid  •  AVOID when middle of band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=264  W=103/L=161  WR=39.0%
- Sharpen: sharpest is H20=H20b (81/161 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 slightly aligned

### L02.  `H20=H20e AND T4=T4c AND BBP=BBP5`
- Raw: n=197  W=77/L=120  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=197  W=77/L=120  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band

### L03.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=197  W=77/L=120  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=197  W=77/L=120  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought

### L04.  `H20=H20b AND H60=H60e AND T4=T4a`
- Raw: n=152  W=42/L=110  WR=27.6%
- Sharpen: sharpest is RSI=RSI5 (81/110 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20b AND T4=T4a AND ZS=ZS4`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is RSI=RSI5 (60/87 of losers there)
- **Sharp: n=84  W=24/L=60  WR=28.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20b AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is RSI=RSI5 (60/87 of losers there)
- **Sharp: n=84  W=24/L=60  WR=28.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H60=H60e (29/86 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band  •  ONLY when HTF60 strongly against

### L08.  `H20=H20e AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H60=H60e (29/86 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when HTF60 strongly against

### L09.  `H20=H20b AND T4=T4a AND RSI=RSI5`
- Raw: n=141  W=35/L=106  WR=24.8%
- Sharpen: sharpest is H60=H60e (81/106 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L10.  `H20=H20b AND T1=T1c AND T4=T4a`
- Raw: n=137  W=40/L=97  WR=29.2%
- Sharpen: sharpest is RSI=RSI5 (81/97 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20b AND T4=T4a AND direction_exec=short`
- Raw: n=137  W=40/L=97  WR=29.2%
- Sharpen: sharpest is RSI=RSI5 (81/97 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20b AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=137  W=40/L=97  WR=29.2%
- Sharpen: sharpest is RSI=RSI5 (81/97 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20b AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=137  W=40/L=97  WR=29.2%
- Sharpen: sharpest is RSI=RSI5 (81/97 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20b AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=137  W=40/L=97  WR=29.2%
- Sharpen: sharpest is RSI=RSI5 (81/97 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L15.  `T1=T1c AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is H20=H20e (20/81 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L16.  `BBP=BBP5 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is H20=H20e (20/81 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  just touched upper band; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L17.  `T1=T1c AND BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is H20=H20e (20/81 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND BBP=BBP5 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is H20=H20e (20/81 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L19.  `BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is H20=H20e (20/81 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L20.  `T1=T1a AND RSI=RSI5 AND session_bucket=asia_late`
- Raw: n=127  W=42/L=85  WR=33.1%
- Sharpen: sharpest is BBP=BBP4 (40/85 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=asia_late  •  ONLY when upper third

### L21.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is H20=H20e (42/75 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong; session=asia  •  ONLY when HTF20 strongly against

### L22.  `H20=H20b AND H60=H60e AND RSI=RSI5`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is T4=T4a (81/85 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20b AND T1=T1c AND RSI=RSI5`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is T4=T4a (81/85 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L24.  `H20=H20b AND RSI=RSI5 AND direction_exec=short`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is T4=T4a (81/85 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20b AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is T4=T4a (81/85 of losers there)
- **Sharp: n=98  W=17/L=81  WR=17.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
