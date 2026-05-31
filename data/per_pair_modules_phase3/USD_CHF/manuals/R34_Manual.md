# USD_CHF — R34 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,749**  (W=1,116 / L=633)  -  WR: **63.8%**

## Session distribution

- london_open: n=408  W=267/L=141  WR=65.4%
- ny_open: n=335  W=216/L=119  WR=64.5%
- london: n=321  W=198/L=123  WR=61.7%
- ny_mid: n=291  W=191/L=100  WR=65.6%
- asia: n=209  W=132/L=77  WR=63.2%
- ny_close: n=104  W=66/L=38  WR=63.5%
- asia_late: n=43  W=22/L=21  WR=51.2%
- off_hours: n=38  W=24/L=14  WR=63.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=202  W=172/L=30  WR=85.1%
- Refine: exclude H20=H20c drops 18/30 losers (60%)
- **Final: n=133  W=121/L=12  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF20 neutral

### W02.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=188  W=160/L=28  WR=85.1%
- Refine: exclude H20=H20c drops 18/28 losers (64%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF20 neutral

### W03.  `H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=148  W=129/L=19  WR=87.2%
- Refine: exclude session_bucket=off_hours drops 6/19 losers (32%)
- **Final: n=142  W=129/L=13  WR=90.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=140  W=122/L=18  WR=87.1%
- Refine: exclude session_bucket=off_hours drops 6/18 losers (33%)
- **Final: n=134  W=122/L=12  WR=91.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W05.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20c drops 10/10 losers (100%)
- **Final: n=104  W=104/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W06.  `H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20c drops 10/10 losers (100%)
- **Final: n=104  W=104/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W07.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20c drops 10/10 losers (100%)
- **Final: n=104  W=104/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W08.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude H20=H20c drops 10/10 losers (100%)
- **Final: n=94  W=94/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W09.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude T1=T1c drops 12/14 losers (86%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when 1h trend AGAINST trade

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T1=T1c drops 12/15 losers (80%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W11.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20c drops 10/13 losers (77%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 neutral

### W12.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20c drops 10/13 losers (77%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 neutral

### W13.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude H20=H20a drops 14/14 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude H20=H20c drops 10/10 losers (100%)
- **Final: n=84  W=84/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W15.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude BBP=BBP6 drops 5/11 losers (45%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when deep above upper band

### W16.  `H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude BBP=BBP6 drops 5/9 losers (56%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when deep above upper band

### W17.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude BBP=BBP6 drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W18.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude BBP=BBP6 drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W19.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=ny_open drops 5/12 losers (42%)
- **Final: n=66  W=59/L=7  WR=89.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W20.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=ny_open drops 5/12 losers (42%)
- **Final: n=66  W=59/L=7  WR=89.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W21.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=82  W=76/L=6  WR=92.7%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 neutral

### W22.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=82  W=76/L=6  WR=92.7%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 neutral

### W23.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H60=H60b drops 7/10 losers (70%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W24.  `H60=H60a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI4 drops 10/11 losers (91%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W25.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=137  W=51/L=86  WR=37.2%
- Sharpen: sharpest is H20=H20e (24/86 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is direction_exec=short (74/83 of losers there)
- **Sharp: n=109  W=35/L=74  WR=32.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when short

### L03.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is H20=H20e (38/78 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L04.  `H60=H60e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=129  W=47/L=82  WR=36.4%
- Sharpen: sharpest is H20=H20e (18/82 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (25/79 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_mid

### L06.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=127  W=47/L=80  WR=37.0%
- Sharpen: sharpest is H20=H20e (18/80 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L07.  `H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is H20=H20e (20/75 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L08.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is H20=H20e (20/75 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L09.  `H20=H20e AND H60=H60e AND BBP=BBP4`
- Raw: n=121  W=45/L=76  WR=37.2%
- Sharpen: sharpest is T1=T1c (24/76 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third  •  ONLY when 1h trend AGAINST trade

### L10.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is H20=H20e (35/72 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L11.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is H20=H20e (35/72 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is H20=H20b (17/71 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when HTF20 slightly aligned

### L13.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is H20=H20b (17/71 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 slightly aligned

### L14.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (28/69 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L15.  `H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=114  W=35/L=79  WR=30.7%
- Sharpen: sharpest is ZS=ZS5 (22/79 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=109  W=35/L=74  WR=32.1%
- Sharpen: sharpest is ZS=ZS5 (22/74 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H20=H20e AND H60=H60e AND ZS=ZS4`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is T1=T1c (20/66 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L18.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is T1=T1c (20/66 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is BBP=BBP5 (20/68 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when just touched upper band

### L20.  `H20=H20e AND T1=T1c AND BBP=BBP4`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is H60=H60e (24/60 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when HTF60 strongly against

### L21.  `H20=H20e AND T1=T1c AND ZS=ZS4`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60e (20/54 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L22.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60e (20/54 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L23.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is H20=H20e (21/56 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L24.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=80  W=24/L=56  WR=30.0%
- Sharpen: sharpest is ZS=ZS5 (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=80  W=24/L=56  WR=30.0%
- Sharpen: sharpest is ZS=ZS5 (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(10/1) | H20b(2/8) |
| H60 | H60a(47/27), H60d(12/6) | H60e(24/43) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/45) | short(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
