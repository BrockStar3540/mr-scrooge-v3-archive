# EUR_GBP — R21 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **763**  (W=486 / L=277)  -  WR: **63.7%**

## Session distribution

- ny_mid: n=284  W=174/L=110  WR=61.3%
- london: n=173  W=112/L=61  WR=64.7%
- ny_open: n=112  W=80/L=32  WR=71.4%
- london_open: n=106  W=68/L=38  WR=64.2%
- ny_close: n=43  W=28/L=15  WR=65.1%
- asia: n=39  W=22/L=17  WR=56.4%
- off_hours: n=6  W=2/L=4  WR=33.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 5/15 losers (33%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W02.  `T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude RSI=RSI4 drops 10/14 losers (71%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W03.  `H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP6 drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W04.  `H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP6 drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong  •  AVOID when deep above upper band

### W05.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP6 drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W06.  `H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W07.  `H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=off_hours drops 4/9 losers (44%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  HTF60 strongly against; upper third  •  AVOID when session=off_hours

### W08.  `H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when session=london_open

### W09.  `H60=H60e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=off_hours drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W10.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 8/8 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W11.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=off_hours drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W12.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude session_bucket=london_open drops 2/3 losers (67%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W13.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude session_bucket=london_open drops 2/3 losers (67%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W14.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude session_bucket=london_open drops 2/3 losers (67%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W15.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude BBP=BBP5 drops 6/7 losers (86%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W16.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude BBP=BBP5 drops 6/7 losers (86%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when just touched upper band

### W17.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude BBP=BBP5 drops 6/7 losers (86%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W18.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude H60=H60a drops 9/9 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude RSI=RSI4 drops 6/9 losers (67%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W20.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude RSI=RSI4 drops 5/5 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W21.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=59  W=54/L=5  WR=91.5%
- Refine: exclude session_bucket=london_open drops 4/5 losers (80%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when session=london_open

### W22.  `H60=H60e AND T1=T1a AND ZS=ZS4`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 4/6 losers (67%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W23.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 4/6 losers (67%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W24.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude BBP=BBP5 drops 4/4 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W25.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude BBP=BBP5 drops 4/4 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is session_bucket=london (27/61 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=london

### L02.  `T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=81  W=24/L=57  WR=29.6%
- Sharpen: sharpest is session_bucket=london (21/57 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london

### L03.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is T4=T4c (26/44 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L04.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: sharpest is RSI=RSI5 (22/43 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is session_bucket=london (16/38 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=london

### L06.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=london (21/39 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london

### L07.  `H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is session_bucket=london (15/35 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third  •  ONLY when session=london

### L08.  `H60=H60a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=london (14/33 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when session=london

### L09.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is H60=H60b (10/33 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 slightly aligned

### L10.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=london (14/33 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=london

### L11.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is RSI=RSI5 (25/31 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L12.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is T1=T1c (25/31 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L13.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is T4=T4c (14/30 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L14.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is T4=T4c (14/30 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is T4=T4c (14/30 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is RSI=RSI5 (25/31 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L17.  `H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=48  W=14/L=34  WR=29.2%
- Sharpen: sharpest is session_bucket=london (13/34 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when session=london

### L18.  `H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP6 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L19.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is T4=T4c (25/31 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is T4=T4c (25/31 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is T4=T4c (25/31 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H20=H20b (8/28 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L23.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: sharpest is session_bucket=london (21/31 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london

### L24.  `H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=43  W=13/L=30  WR=30.2%
- Sharpen: sharpest is session_bucket=london (12/30 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=london

### L25.  `H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=43  W=13/L=30  WR=30.2%
- Sharpen: sharpest is T4=T4c (24/30 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(12/19) |
| H60 | H60e(39/25), H60c(16/10) | H60a(25/42), H60b(8/13) |
| T1 | T1a(60/43) | T1c(40/57) |
| T4 | T4a(58/37) | T4c(42/63) |
| BBP | — | — |
| RSI | — | RSI3(24/29) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/46) | short(44/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
