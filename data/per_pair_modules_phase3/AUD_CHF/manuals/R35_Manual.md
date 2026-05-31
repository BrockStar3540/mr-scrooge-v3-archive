# AUD_CHF — R35 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,449**  (W=931 / L=518)  -  WR: **64.3%**

## Session distribution

- asia: n=486  W=315/L=171  WR=64.8%
- london_open: n=259  W=165/L=94  WR=63.7%
- ny_close: n=170  W=119/L=51  WR=70.0%
- london: n=151  W=95/L=56  WR=62.9%
- asia_late: n=130  W=76/L=54  WR=58.5%
- ny_open: n=116  W=73/L=43  WR=62.9%
- ny_mid: n=89  W=56/L=33  WR=62.9%
- off_hours: n=48  W=32/L=16  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=223  W=191/L=32  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 7/32 losers (22%)
- **Final: n=212  W=187/L=25  WR=88.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W02.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=189  W=165/L=24  WR=87.3%
- Refine: exclude session_bucket=ny_close drops 7/24 losers (29%)
- **Final: n=178  W=161/L=17  WR=90.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W03.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=189  W=165/L=24  WR=87.3%
- Refine: exclude session_bucket=ny_close drops 7/24 losers (29%)
- **Final: n=178  W=161/L=17  WR=90.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W04.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude H60=H60d drops 4/18 losers (22%)
- **Final: n=147  W=133/L=14  WR=90.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF60 mildly against

### W05.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude session_bucket=ny_close drops 5/15 losers (33%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W06.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=115  W=103/L=12  WR=89.6%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 3/12 losers (25%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when strategy=TF2_pullback_EMA20_long

### W07.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=114  W=103/L=11  WR=90.4%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  AVOID when HTF20 aligned WITH trade

### W08.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude H60=H60b drops 6/14 losers (43%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W09.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude H60=H60b drops 6/14 losers (43%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W10.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude H60=H60b drops 5/15 losers (33%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF60 slightly aligned

### W11.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=london_open drops 6/15 losers (40%)
- **Final: n=80  W=71/L=9  WR=88.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W12.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=london_open drops 6/15 losers (40%)
- **Final: n=80  W=71/L=9  WR=88.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W13.  `T1=T1a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H60=H60b drops 5/13 losers (38%)
- **Final: n=81  W=73/L=8  WR=90.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W14.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=off_hours drops 5/13 losers (38%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=off_hours

### W15.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=off_hours drops 5/13 losers (38%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=off_hours

### W16.  `BBP=BBP6 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude session_bucket=ny_mid drops 3/8 losers (38%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: LONG**  •  deep above upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W17.  `H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude RSI=RSI4 drops 10/12 losers (83%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 50-60 upper neutral

### W18.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude RSI=RSI4 drops 10/12 losers (83%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 50-60 upper neutral

### W19.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=91  W=85/L=6  WR=93.4%
- Refine: exclude session_bucket=london drops 2/6 losers (33%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=london

### W22.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 50-60 upper neutral

### W23.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W24.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=182  W=71/L=111  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (31/111 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when deep above upper band

### L02.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=174  W=63/L=111  WR=36.2%
- Sharpen: sharpest is BBP=BBP6 (31/111 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L03.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=174  W=63/L=111  WR=36.2%
- Sharpen: sharpest is BBP=BBP6 (31/111 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L04.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_open

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=ny_open

### L06.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_open

### L07.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=115  W=45/L=70  WR=39.1%
- Sharpen: sharpest is BBP=BBP6 (26/70 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when deep above upper band

### L08.  `H20=H20d AND T1=T1c AND direction_exec=short`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (22/64 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade  •  ONLY when deep above upper band

### L09.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is T4=T4a (35/67 of losers there)
- **Sharp: n=41  W=6/L=35  WR=14.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L10.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H60=H60e (45/57 of losers there)
- **Sharp: n=62  W=17/L=45  WR=27.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L11.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H60=H60e (45/57 of losers there)
- **Sharp: n=62  W=17/L=45  WR=27.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L12.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI4 (32/61 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is session_bucket=asia_late (16/52 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L14.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is session_bucket=asia_late (16/52 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L15.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is session_bucket=asia_late (16/52 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L16.  `H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is T4=T4a (31/53 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is T4=T4a (31/53 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L18.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is BBP=BBP6 (32/49 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L19.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is BBP=BBP6 (32/49 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L20.  `H20=H20d AND T1=T1c AND RSI=RSI5`
- Raw: n=74  W=23/L=51  WR=31.1%
- Sharpen: sharpest is H60=H60e (35/51 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L21.  `H20=H20d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=74  W=23/L=51  WR=31.1%
- Sharpen: sharpest is H60=H60e (35/51 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L22.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=71  W=20/L=51  WR=28.2%
- Sharpen: sharpest is T4=T4a (32/51 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20d AND H60=H60e AND T1=T1c`
- Raw: n=71  W=23/L=48  WR=32.4%
- Sharpen: sharpest is BBP=BBP6 (20/48 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep above upper band

### L24.  `H20=H20d AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=71  W=23/L=48  WR=32.4%
- Sharpen: sharpest is BBP=BBP6 (20/48 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep above upper band

### L25.  `T1=T1c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is ZS=ZS6 (16/45 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when zscore >+3 extreme

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/28) | H20e(32/44) |
| H60 | H60a(46/32) | H60e(38/51), H60d(5/10) |
| T1 | T1a(61/35) | T1c(39/65) |
| T4 | T4c(53/45) | T4a(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/38) | short(43/62) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
