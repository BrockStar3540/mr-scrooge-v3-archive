# EUR_CAD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,151**  (W=2,666 / L=1,485)  -  WR: **64.2%**

## Session distribution

- asia: n=1006  W=655/L=351  WR=65.1%
- london_open: n=937  W=600/L=337  WR=64.0%
- london: n=547  W=355/L=192  WR=64.9%
- ny_open: n=483  W=300/L=183  WR=62.1%
- asia_late: n=429  W=275/L=154  WR=64.1%
- ny_close: n=342  W=216/L=126  WR=63.2%
- ny_mid: n=265  W=171/L=94  WR=64.5%
- off_hours: n=142  W=94/L=48  WR=66.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=230  W=196/L=34  WR=85.2%
- Refine: exclude T4=T4a drops 30/34 losers (88%)
- **Final: n=86  W=82/L=4  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

### W02.  `H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=181  W=161/L=20  WR=89.0%
- Refine: exclude H20=H20e drops 4/20 losers (20%)
- **Final: n=177  W=161/L=16  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W03.  `H20=H20b AND RSI=RSI4 AND direction_exec=long`
- Raw: n=166  W=144/L=22  WR=86.7%
- Refine: exclude T1=T1a drops 21/22 losers (95%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W04.  `H20=H20b AND T4=T4a AND RSI=RSI4`
- Raw: n=164  W=141/L=23  WR=86.0%
- Refine: exclude direction_exec=short drops 18/23 losers (78%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when short

### W05.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=162  W=139/L=23  WR=85.8%
- Refine: exclude H60=H60a drops 20/23 losers (87%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=161  W=137/L=24  WR=85.1%
- Refine: exclude H60=H60b drops 14/24 losers (58%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 slightly aligned

### W07.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=157  W=137/L=20  WR=87.3%
- Refine: exclude H20=H20e drops 4/20 losers (20%)
- **Final: n=153  W=137/L=16  WR=89.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W08.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=157  W=134/L=23  WR=85.4%
- Refine: exclude H60=H60b drops 10/23 losers (43%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W09.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=157  W=134/L=23  WR=85.4%
- Refine: exclude H60=H60b drops 10/23 losers (43%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=150  W=133/L=17  WR=88.7%
- Refine: exclude H20=H20e drops 4/17 losers (24%)
- **Final: n=146  W=133/L=13  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W11.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=150  W=128/L=22  WR=85.3%
- Refine: exclude H60=H60b drops 14/22 losers (64%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 slightly aligned

### W12.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=144  W=126/L=18  WR=87.5%
- Refine: exclude H20=H20c drops 6/18 losers (33%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W13.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=141  W=120/L=21  WR=85.1%
- Refine: exclude H20=H20a drops 18/21 losers (86%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=134  W=121/L=13  WR=90.3%
- Refine: exclude H20=H20a drops 9/13 losers (69%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `H20=H20b AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=128  W=109/L=19  WR=85.2%
- Refine: exclude session_bucket=london drops 10/19 losers (53%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london

### W16.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude T1=T1c drops 14/15 losers (93%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W17.  `H20=H20a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 6/14 losers (43%)
- **Final: n=102  W=94/L=8  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W18.  `H60=H60a AND T1=T1c AND session_bucket=asia_late`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude H20=H20a drops 15/16 losers (94%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

### W19.  `H20=H20a AND T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 10/16 losers (62%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude session_bucket=london_open drops 8/16 losers (50%)
- **Final: n=86  W=78/L=8  WR=90.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W21.  `H20=H20c AND T1=T1c AND session_bucket=asia`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude RSI=RSI3 drops 10/14 losers (71%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20b AND H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude session_bucket=london drops 10/14 losers (71%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W23.  `H20=H20b AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude session_bucket=london drops 10/14 losers (71%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W24.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=106  W=97/L=9  WR=91.5%
- Refine: exclude H60=H60d drops 8/9 losers (89%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 mildly against

### W25.  `H60=H60d AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude session_bucket=asia drops 7/14 losers (50%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=186  W=66/L=120  WR=35.5%
- Sharpen: sharpest is T4=T4a (52/120 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=184  W=66/L=118  WR=35.9%
- Sharpen: sharpest is T4=T4a (52/118 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is T4=T4a (32/85 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is T4=T4a (32/85 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L05.  `BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=131  W=52/L=79  WR=39.7%
- Sharpen: sharpest is T4=T4a (32/79 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: LONG**  •  upper third; session=asia  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=129  W=38/L=91  WR=29.5%
- Sharpen: sharpest is RSI=RSI3 (53/91 of losers there)
- **Sharp: n=66  W=13/L=53  WR=19.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L07.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is H60=H60e (56/72 of losers there)
- **Sharp: n=85  W=29/L=56  WR=34.1%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia  •  ONLY when HTF60 strongly against

### L08.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is H60=H60e (56/72 of losers there)
- **Sharp: n=85  W=29/L=56  WR=34.1%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF60 strongly against

### L09.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=118  W=34/L=84  WR=28.8%
- Sharpen: sharpest is direction_exec=short (30/84 of losers there)
- **Sharp: n=32  W=2/L=30  WR=6.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when short

### L10.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is T4=T4a (28/68 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L11.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=110  W=34/L=76  WR=30.9%
- Sharpen: sharpest is H60=H60e (52/76 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L12.  `H20=H20e AND H60=H60e AND ZS=ZS5`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is T1=T1c (22/63 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is T4=T4a (26/63 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L14.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is session_bucket=asia_late (23/65 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia_late

### L15.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is H20=H20e (39/58 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia_late  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is T1=T1a (38/62 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when 1h trend WITH trade

### L17.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=93  W=32/L=61  WR=34.4%
- Sharpen: sharpest is direction_exec=short (23/61 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when short

### L18.  `H60=H60a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is T4=T4c (29/56 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60a AND ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is T4=T4c (29/56 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60e AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=31/L=60  WR=34.1%
- Sharpen: sharpest is T1=T1a (38/60 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when 1h trend WITH trade

### L21.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is BBP=BBP4 (28/56 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L22.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=89  W=29/L=60  WR=32.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=89  W=29/L=60  WR=32.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral

### L23.  `H60=H60e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=87  W=29/L=58  WR=33.3%
- Sharpen: sharpest is T1=T1a (36/58 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L24.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=87  W=29/L=58  WR=33.3%
- Sharpen: sharpest is T1=T1a (36/58 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is T1=T1c (16/54 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(26/19) | H20e(19/28) |
| H60 | H60a(41/33) | H60e(33/41) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/48) | long(47/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
