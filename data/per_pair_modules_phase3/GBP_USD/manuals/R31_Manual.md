# GBP_USD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,080**  (W=1,930 / L=1,150)  -  WR: **62.7%**

## Session distribution

- asia: n=1167  W=739/L=428  WR=63.3%
- london_open: n=676  W=422/L=254  WR=62.4%
- ny_open: n=384  W=231/L=153  WR=60.2%
- london: n=318  W=206/L=112  WR=64.8%
- asia_late: n=318  W=189/L=129  WR=59.4%
- ny_mid: n=89  W=57/L=32  WR=64.0%
- off_hours: n=84  W=55/L=29  WR=65.5%
- ny_close: n=44  W=31/L=13  WR=70.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=231  W=199/L=32  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 15/32 losers (47%)
- **Final: n=202  W=185/L=17  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=188  W=169/L=19  WR=89.9%
- Refine: exclude H60=H60a drops 12/19 losers (63%)
- **Final: n=135  W=128/L=7  WR=94.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W03.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=155  W=135/L=20  WR=87.1%
- Refine: exclude H20=H20e drops 12/20 losers (60%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W04.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude RSI=RSI3 drops 14/18 losers (78%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W05.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=126  W=115/L=11  WR=91.3%
- Refine: exclude session_bucket=ny_open drops 7/11 losers (64%)
- **Final: n=117  W=113/L=4  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W06.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude H20=H20e drops 15/17 losers (88%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W07.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude RSI=RSI3 drops 8/16 losers (50%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W08.  `H20=H20e AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=121  W=108/L=13  WR=89.3%
- Refine: exclude RSI=RSI4 drops 9/13 losers (69%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W09.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude BBP=BBP4 drops 9/15 losers (60%)
- **Final: n=98  W=92/L=6  WR=93.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when upper third

### W10.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude H60=H60a drops 10/12 losers (83%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W11.  `H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude T4=T4a drops 12/15 losers (80%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=109  W=101/L=8  WR=92.7%
- Refine: exclude direction_exec=short drops 4/8 losers (50%)
- **Final: n=105  W=101/L=4  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when short

### W13.  `T1=T1a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 strongly against

### W14.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude H20=H20d drops 5/14 losers (36%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=asia  •  AVOID when HTF20 mildly against

### W15.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP2 drops 9/15 losers (60%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W16.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude BBP=BBP2 drops 7/15 losers (47%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when lower third

### W17.  `T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude RSI=RSI3 drops 7/15 losers (47%)
- **Final: n=81  W=73/L=8  WR=90.1%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W18.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude direction_exec=short drops 10/15 losers (67%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when short

### W19.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=96  W=86/L=10  WR=89.6%
- Refine: exclude RSI=RSI3 drops 4/10 losers (40%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W20.  `H60=H60e AND T1=T1a AND ZS=ZS4`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=off_hours drops 4/13 losers (31%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W21.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=off_hours drops 4/13 losers (31%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W22.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude BBP=BBP4 drops 8/14 losers (57%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when upper third

### W23.  `H60=H60b AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude T4=T4a drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W24.  `H20=H20a AND H60=H60e AND T4=T4c AND RSI=RSI4`
- Raw: n=90  W=86/L=4  WR=95.6%
- Refine: no further refinement
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral

### W25.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=86  W=79/L=7  WR=91.9%
- Refine: exclude ZS=ZS5 drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore +2 to +3 deep overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=186  W=67/L=119  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (58/119 of losers there)
- **Sharp: n=76  W=18/L=58  WR=23.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L02.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=154  W=60/L=94  WR=39.0%
- Sharpen: sharpest is T4=T4a (52/94 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: sharpest is H20=H20e (62/91 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L04.  `T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is direction_exec=short (60/87 of losers there)
- **Sharp: n=78  W=18/L=60  WR=23.1%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=asia  •  ONLY when short

### L05.  `T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=144  W=51/L=93  WR=35.4%
- Sharpen: sharpest is H20=H20e (38/93 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L06.  `H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=143  W=48/L=95  WR=33.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=143  W=48/L=95  WR=33.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third

### L07.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is BBP=BBP4 (50/95 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L08.  `T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is BBP=BBP4 (37/83 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when upper third

### L09.  `H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is RSI=RSI5 (17/80 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L10.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is RSI=RSI5 (17/80 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L11.  `T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=122  W=46/L=76  WR=37.7%
- Sharpen: sharpest is H20=H20e (28/76 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=122  W=46/L=76  WR=37.7%
- Sharpen: sharpest is H20=H20e (28/76 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L13.  `T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is direction_exec=short (50/74 of losers there)
- **Sharp: n=66  W=16/L=50  WR=24.2%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when short

### L14.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is direction_exec=short (50/74 of losers there)
- **Sharp: n=66  W=16/L=50  WR=24.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when short

### L15.  `H60=H60d AND RSI=RSI4 AND direction_exec=short`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=44/L=67  WR=39.6%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 50-60 upper neutral

### L16.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=107  W=35/L=72  WR=32.7%
- Sharpen: sharpest is H20=H20e (50/72 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L17.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is RSI=RSI4 (44/68 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L18.  `H60=H60d AND T1=T1c AND RSI=RSI4`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20e (53/65 of losers there)
- **Sharp: n=78  W=25/L=53  WR=32.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L19.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is T1=T1c (42/64 of losers there)
- **Sharp: n=52  W=10/L=42  WR=19.2%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L20.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is H20=H20e (16/63 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF20 strongly against

### L21.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (23/62 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H20=H20e AND T4=T4a AND BBP=BBP4`
- Raw: n=102  W=30/L=72  WR=29.4%
- Sharpen: sharpest is direction_exec=short (62/72 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third  •  ONLY when short

### L23.  `H20=H20e AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is T1=T1c (53/66 of losers there)
- **Sharp: n=64  W=11/L=53  WR=17.2%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (42/60 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L25.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is H20=H20e (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/41) | H20e(41/47) |
| H60 | H60e(38/28) | H60a(30/42) |
| T1 | T1a(57/47) | T1c(43/52) |
| T4 | T4c(54/45) | T4a(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
