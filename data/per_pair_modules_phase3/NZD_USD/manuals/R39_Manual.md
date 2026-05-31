# NZD_USD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,530**  (W=985 / L=545)  -  WR: **64.4%**

## Session distribution

- asia: n=359  W=237/L=122  WR=66.0%
- london_open: n=309  W=204/L=105  WR=66.0%
- ny_mid: n=270  W=176/L=94  WR=65.2%
- ny_open: n=225  W=149/L=76  WR=66.2%
- london: n=171  W=106/L=65  WR=62.0%
- ny_close: n=126  W=63/L=63  WR=50.0%
- off_hours: n=45  W=33/L=12  WR=73.3%
- asia_late: n=25  W=17/L=8  WR=68.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=167  W=149/L=18  WR=89.2%
- Refine: exclude H60=H60a drops 6/18 losers (33%)
- **Final: n=161  W=149/L=12  WR=92.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W02.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=160  W=141/L=19  WR=88.1%
- Refine: exclude ZS=ZS3 drops 10/19 losers (53%)
- **Final: n=130  W=121/L=9  WR=93.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=113  W=102/L=11  WR=90.3%
- Refine: exclude H60=H60a drops 5/11 losers (45%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W04.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H60=H60a drops 11/15 losers (73%)
- **Final: n=100  W=96/L=4  WR=96.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 aligned WITH trade

### W05.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=100  W=93/L=7  WR=93.0%
- Refine: exclude session_bucket=asia drops 4/7 losers (57%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when session=asia

### W06.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  AVOID when HTF20 strongly against

### W07.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude H20=H20e drops 7/10 losers (70%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 strongly against

### W08.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T1=T1a drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W09.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T1=T1a drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W10.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude RSI=RSI3 drops 8/12 losers (67%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W11.  `T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H20=H20e drops 7/11 losers (64%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W12.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H20=H20e drops 7/11 losers (64%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W13.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H20=H20e drops 11/13 losers (85%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W14.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude RSI=RSI4 drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W15.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W16.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude H20=H20e drops 7/12 losers (58%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF20 strongly against

### W17.  `H20=H20a AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=78  W=72/L=6  WR=92.3%
- Refine: exclude session_bucket=london_open drops 3/6 losers (50%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=london_open

### W18.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude T1=T1a drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude direction_exec=long drops 7/11 losers (64%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when long

### W20.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude RSI=RSI4 drops 6/9 losers (67%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  AVOID when RSI 50-60 upper neutral

### W21.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude direction_exec=long drops 8/10 losers (80%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when long

### W22.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude T1=T1a drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=69  W=66/L=3  WR=95.7%
- Refine: exclude session_bucket=london_open drops 3/3 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W24.  `H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 strongly against

### W25.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is T4=T4a (36/88 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L02.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is H20=H20e (40/57 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L03.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (36/53 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is T4=T4a (39/50 of losers there)
- **Sharp: n=53  W=14/L=39  WR=26.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is T4=T4a (40/52 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=81  W=24/L=57  WR=29.6%
- Sharpen: sharpest is T4=T4a (36/57 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L07.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=80  W=25/L=55  WR=31.2%
- Sharpen: sharpest is BBP=BBP4 (16/55 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L08.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=76  W=25/L=51  WR=32.9%
- Sharpen: sharpest is BBP=BBP4 (16/51 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L09.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=london_open (26/50 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L10.  `T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=72  W=27/L=45  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (30/45 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: LONG**  •  1h trend WITH trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L11.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (23/46 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L12.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is RSI=RSI4 (23/44 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L13.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is RSI=RSI4 (23/42 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L14.  `T1=T1a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is RSI=RSI3 (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L15.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is RSI=RSI3 (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L16.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is T1=T1a (28/41 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  ONLY when 1h trend WITH trade

### L17.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is T1=T1a (30/37 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L18.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is session_bucket=london (17/41 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=london

### L19.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is H20=H20a (23/37 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (12/36 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when upper third

### L21.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI3 (36/41 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L22.  `H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is H20=H20e (29/39 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when HTF20 strongly against

### L23.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is BBP=BBP4 (14/36 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when upper third

### L24.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is H20=H20e (24/39 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L25.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is RSI=RSI3 (30/39 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/39) | H20e(40/47) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(57/43) | T4a(43/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/45) | long(46/55) |
| session_bucket | — | ny_close(6/12) |

*Read: `bucket(winner%/loser%)`.*
