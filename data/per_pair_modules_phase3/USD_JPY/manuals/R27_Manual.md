# USD_JPY — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,899**  (W=1,064 / L=835)  -  WR: **56.0%**

## Session distribution

- asia: n=551  W=310/L=241  WR=56.3%
- ny_mid: n=493  W=261/L=232  WR=52.9%
- london_open: n=370  W=211/L=159  WR=57.0%
- ny_close: n=235  W=149/L=86  WR=63.4%
- london: n=117  W=60/L=57  WR=51.3%
- ny_open: n=98  W=55/L=43  WR=56.1%
- asia_late: n=30  W=16/L=14  WR=53.3%
- off_hours: n=5  W=2/L=3  WR=40.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude T4=T4c drops 9/14 losers (64%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W02.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T4=T4c drops 8/13 losers (62%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W03.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude session_bucket=asia drops 3/10 losers (30%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W04.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude session_bucket=asia drops 3/10 losers (30%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W05.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude H20=H20d drops 6/13 losers (46%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W06.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude H20=H20d drops 6/13 losers (46%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W07.  `H20=H20a AND H60=H60a AND BBP=BBP4`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude RSI=RSI5 drops 9/14 losers (64%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  AVOID when RSI 60-70 strong

### W08.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude RSI=RSI5 drops 9/14 losers (64%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when RSI 60-70 strong

### W09.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude T4=T4c drops 8/11 losers (73%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W10.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude T4=T4c drops 8/11 losers (73%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude T4=T4c drops 8/11 losers (73%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W12.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude session_bucket=asia drops 3/9 losers (33%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W13.  `H20=H20a AND H60=H60e AND ZS=ZS4`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI5 drops 3/12 losers (25%)
- **Final: n=79  W=70/L=9  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W14.  `H20=H20a AND H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI5 drops 3/12 losers (25%)
- **Final: n=79  W=70/L=9  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W15.  `H20=H20a AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI5 drops 3/12 losers (25%)
- **Final: n=79  W=70/L=9  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20a AND H60=H60e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI5 drops 3/12 losers (25%)
- **Final: n=79  W=70/L=9  WR=88.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W17.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=asia drops 3/7 losers (43%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W18.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=asia drops 3/7 losers (43%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W19.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=asia drops 3/7 losers (43%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=asia drops 3/7 losers (43%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W21.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20d drops 7/10 losers (70%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W22.  `H60=H60b AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF60 slightly aligned; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W23.  `H20=H20a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/7 losers (29%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when strategy=delta_tag_and_go_v2

### W24.  `T1=T1a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude H60=H60b drops 4/5 losers (80%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W25.  `RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude H60=H60b drops 4/5 losers (80%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: LONG**  •  RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=301  W=117/L=184  WR=38.9%
- Sharpen: sharpest is RSI=RSI4 (57/184 of losers there)
- **Sharp: n=65  W=8/L=57  WR=12.3%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L02.  `H20=H20e AND T1=T1a AND ZS=ZS4`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (57/152 of losers there)
- **Sharp: n=65  W=8/L=57  WR=12.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L03.  `H20=H20e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (57/152 of losers there)
- **Sharp: n=65  W=8/L=57  WR=12.3%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L04.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (57/152 of losers there)
- **Sharp: n=65  W=8/L=57  WR=12.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (57/152 of losers there)
- **Sharp: n=65  W=8/L=57  WR=12.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L06.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (57/152 of losers there)
- **Sharp: n=65  W=8/L=57  WR=12.3%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L07.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=153  W=52/L=101  WR=34.0%
- Sharpen: sharpest is ZS=ZS5 (39/101 of losers there)
- **Sharp: n=40  W=1/L=39  WR=2.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=153  W=54/L=99  WR=35.3%
- Sharpen: sharpest is RSI=RSI6 (39/99 of losers there)
- **Sharp: n=40  W=1/L=39  WR=2.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L09.  `H60=H60d AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=152  W=59/L=93  WR=38.8%
- Sharpen: sharpest is T1=T1a (25/93 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF60 mildly against; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20e AND H60=H60e AND T1=T1a`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade

### L11.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=137  W=54/L=83  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (28/83 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when session=ny_close

### L12.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=137  W=54/L=83  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (28/83 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L13.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=137  W=54/L=83  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (28/83 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L14.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is BBP=BBP6 (33/79 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L15.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is BBP=BBP6 (33/79 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when deep above upper band

### L16.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is BBP=BBP6 (33/79 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L17.  `H20=H20a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=116  W=42/L=74  WR=36.2%
- Sharpen: sharpest is RSI=RSI6 (32/74 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is ZS=ZS5 (24/70 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is ZS=ZS5 (24/70 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is ZS=ZS5 (24/70 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=114  W=39/L=75  WR=34.2%
- Sharpen: sharpest is RSI=RSI6 (19/75 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when RSI 70-80 overbought

### L22.  `H20=H20a AND T1=T1c AND RSI=RSI6`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is ZS=ZS5 (32/68 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is ZS=ZS5 (32/68 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20a AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is ZS=ZS5 (32/68 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is H60=H60d (15/66 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=asia  •  ONLY when HTF60 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60b(25/14) | H60d(13/23) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | ZS3(25/20) | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
