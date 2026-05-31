# USD_CAD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,755**  (W=1,805 / L=950)  -  WR: **65.5%**

## Session distribution

- asia: n=1617  W=1066/L=551  WR=65.9%
- asia_late: n=314  W=192/L=122  WR=61.1%
- london: n=231  W=155/L=76  WR=67.1%
- london_open: n=220  W=145/L=75  WR=65.9%
- ny_close: n=187  W=123/L=64  WR=65.8%
- off_hours: n=137  W=89/L=48  WR=65.0%
- ny_open: n=49  W=35/L=14  WR=71.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude T4=T4a drops 11/18 losers (61%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W02.  `H60=H60b AND T4=T4a AND session_bucket=asia`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude direction_exec=long drops 12/12 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; session=asia  •  AVOID when long

### W03.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H60=H60d drops 6/13 losers (46%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 mildly against

### W04.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=97  W=88/L=9  WR=90.7%
- Refine: exclude session_bucket=off_hours drops 3/9 losers (33%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W05.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude direction_exec=short drops 9/14 losers (64%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when short

### W06.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 3/10 losers (30%)
- **Final: n=83  W=76/L=7  WR=91.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; upper third  •  AVOID when strategy=echo_box_fade_v2

### W07.  `H20=H20e AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 3/8 losers (38%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when strategy=echo_box_fade_v2

### W08.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude BBP=BBP0 drops 3/5 losers (60%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W09.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI3 drops 4/12 losers (33%)
- **Final: n=78  W=70/L=8  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W10.  `H60=H60b AND T1=T1a AND session_bucket=asia`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60b AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H20=H20b drops 8/11 losers (73%)
- **Final: n=40  W=37/L=3  WR=92.5%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W12.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS4`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude RSI=RSI3 drops 4/11 losers (36%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W13.  `H60=H60b AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H20=H20b drops 8/11 losers (73%)
- **Final: n=38  W=35/L=3  WR=92.1%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W14.  `H20=H20b AND T4=T4a AND session_bucket=asia`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude ZS=ZS4 drops 7/12 losers (58%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W15.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude H20=H20d drops 4/8 losers (50%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 mildly against

### W16.  `H60=H60b AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20b drops 8/11 losers (73%)
- **Final: n=37  W=34/L=3  WR=91.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W17.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=78  W=72/L=6  WR=92.3%
- Refine: exclude BBP=BBP0 drops 3/6 losers (50%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W18.  `H60=H60b AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W19.  `BBP=BBP0 AND direction_exec=long AND session_bucket=asia`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H60=H60d drops 5/11 losers (45%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  deep below lower band; session=asia  •  AVOID when HTF60 mildly against

### W20.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude direction_exec=short drops 5/9 losers (56%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when short

### W21.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude BBP=BBP0 drops 8/10 losers (80%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when deep below lower band

### W22.  `H60=H60b AND T4=T4a AND BBP=BBP4`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude H20=H20a drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; upper third  •  AVOID when HTF20 aligned WITH trade

### W23.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude H60=H60d drops 4/7 losers (57%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 mildly against

### W24.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude H60=H60d drops 5/8 losers (62%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 mildly against

### W25.  `H60=H60b AND BBP=BBP4 AND direction_exec=long`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=47  W=43/L=4  WR=91.5%**
- **Dir: LONG**  •  HTF60 slightly aligned; upper third  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=174  W=66/L=108  WR=37.9%
- Sharpen: sharpest is H20=H20a (60/108 of losers there)
- **Sharp: n=84  W=24/L=60  WR=28.6%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L02.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=159  W=60/L=99  WR=37.7%
- Sharpen: sharpest is H20=H20a (58/99 of losers there)
- **Sharp: n=80  W=22/L=58  WR=27.5%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 aligned WITH trade

### L03.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is session_bucket=asia_late (18/63 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L04.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is T4=T4a (17/61 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L05.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is H20=H20a (34/56 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L06.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is BBP=BBP4 (34/59 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L07.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is H20=H20a (34/54 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is session_bucket=asia_late (16/48 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L09.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is session_bucket=asia (26/42 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=asia

### L10.  `T1=T1a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is H60=H60a (34/41 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia_late  •  ONLY when HTF60 aligned WITH trade

### L11.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (23/36 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=asia

### L12.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=58  W=20/L=38  WR=34.5%
- Sharpen: sharpest is RSI=RSI4 (34/38 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is T4=T4a (10/35 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L14.  `H20=H20a AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=56  W=18/L=38  WR=32.1%
- Sharpen: sharpest is session_bucket=asia (24/38 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L15.  `H20=H20a AND T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is RSI=RSI4 (34/36 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=asia (21/34 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L17.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (19/34 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when RSI 50-60 upper neutral

### L18.  `T1=T1c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is direction_exec=long (31/34 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when long

### L19.  `H60=H60a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H20=H20e (13/33 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band  •  ONLY when HTF20 strongly against

### L20.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=53  W=16/L=37  WR=30.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral

### L21.  `H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is direction_exec=short (34/36 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  ONLY when short

### L22.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is session_bucket=asia_late (13/32 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L23.  `H20=H20a AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is RSI=RSI4 (18/32 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

### L24.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=51  W=15/L=36  WR=29.4%
- Sharpen: sharpest is T1=T1c (31/36 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

### L25.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (31/31 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(39/32), H60b(11/5) | H60a(35/41), H60d(7/13) |
| T1 | — | — |
| T4 | T4a(54/44) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/44) | short(45/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
