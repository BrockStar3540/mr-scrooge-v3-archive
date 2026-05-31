# NZD_JPY — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,457**  (W=2,245 / L=1,212)  -  WR: **64.9%**

## Session distribution

- asia: n=1249  W=810/L=439  WR=64.9%
- ny_close: n=493  W=311/L=182  WR=63.1%
- london: n=357  W=244/L=113  WR=68.3%
- london_open: n=347  W=221/L=126  WR=63.7%
- ny_open: n=309  W=205/L=104  WR=66.3%
- ny_mid: n=301  W=186/L=115  WR=61.8%
- asia_late: n=202  W=137/L=65  WR=67.8%
- off_hours: n=199  W=131/L=68  WR=65.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=91/L=11  WR=89.2%
- Refine: exclude RSI=RSI3 drops 11/11 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W02.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia_late  •  AVOID when just touched upper band

### W03.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when zscore +1 to +2 overbought

### W04.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H20=H20b drops 8/13 losers (62%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

### W05.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H20=H20b drops 8/13 losers (62%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

### W06.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H20=H20b drops 8/13 losers (62%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

### W07.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: SHORT**  •  upper third; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W08.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 6/11 losers (55%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral  •  AVOID when strategy=TF2_pullback_EMA20_long

### W09.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=london_open drops 4/12 losers (33%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W10.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20b drops 8/12 losers (67%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

### W11.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20b drops 8/12 losers (67%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP2 drops 7/12 losers (58%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when lower third

### W13.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP2 drops 7/12 losers (58%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  AVOID when lower third

### W14.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP2 drops 7/12 losers (58%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when lower third

### W15.  `H20=H20a AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude BBP=BBP6 drops 4/9 losers (44%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=off_hours  •  AVOID when deep above upper band

### W16.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude T4=T4c drops 9/11 losers (82%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W17.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude T4=T4c drops 9/11 losers (82%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W18.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W19.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W20.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 4/8 losers (50%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when strategy=TF2_pullback_EMA20_long

### W21.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 4/8 losers (50%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when strategy=TF2_pullback_EMA20_long

### W22.  `H20=H20a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude BBP=BBP6 drops 4/8 losers (50%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when deep above upper band

### W23.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude T4=T4c drops 8/8 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W24.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP4 drops 7/8 losers (88%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when upper third

### W25.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude T4=T4c drops 8/8 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=london (18/81 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=london

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is session_bucket=london (25/57 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L03.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is T1=T1c (40/55 of losers there)
- **Sharp: n=57  W=17/L=40  WR=29.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_close (16/53 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_close

### L05.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is T1=T1c (32/51 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L06.  `T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=82  W=24/L=58  WR=29.3%
- Sharpen: sharpest is H20=H20e (20/58 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_close (15/47 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L08.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is T4=T4c (14/47 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L09.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is T4=T4c (14/47 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (26/42 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T1=T1c (14/41 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L12.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4c (14/41 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is H20=H20e (16/44 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L14.  `H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is T1=T1c (14/40 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is T1=T1c (14/40 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L16.  `H20=H20e AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (14/39 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L17.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_close (13/40 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L18.  `T1=T1a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is H60=H60e (18/39 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; session=asia  •  ONLY when HTF60 strongly against

### L19.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is H20=H20e (27/39 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF20 strongly against

### L20.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is H60=H60e (18/39 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF60 strongly against

### L21.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is H20=H20e (27/39 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF20 strongly against

### L22.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (26/36 of losers there)
- **Sharp: n=37  W=11/L=26  WR=29.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L23.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (26/36 of losers there)
- **Sharp: n=37  W=11/L=26  WR=29.7%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L24.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (26/36 of losers there)
- **Sharp: n=37  W=11/L=26  WR=29.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L25.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is BBP=BBP4 (10/40 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/34) | H20e(33/39) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/48) | T4c(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
