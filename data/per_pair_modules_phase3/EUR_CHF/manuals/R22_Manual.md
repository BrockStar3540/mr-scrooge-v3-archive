# EUR_CHF — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,447**  (W=1,584 / L=863)  -  WR: **64.7%**

## Session distribution

- london_open: n=536  W=351/L=185  WR=65.5%
- asia: n=450  W=294/L=156  WR=65.3%
- ny_close: n=418  W=274/L=144  WR=65.6%
- london: n=294  W=183/L=111  WR=62.2%
- ny_open: n=271  W=169/L=102  WR=62.4%
- ny_mid: n=264  W=179/L=85  WR=67.8%
- asia_late: n=123  W=81/L=42  WR=65.9%
- off_hours: n=91  W=53/L=38  WR=58.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20b AND T1=T1a AND RSI=RSI4`
- Raw: n=145  W=126/L=19  WR=86.9%
- Refine: exclude session_bucket=asia drops 11/19 losers (58%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W02.  `H20=H20b AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=138  W=119/L=19  WR=86.2%
- Refine: exclude RSI=RSI5 drops 10/19 losers (53%)
- **Final: n=115  W=106/L=9  WR=92.2%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W03.  `H20=H20b AND T4=T4c AND RSI=RSI4`
- Raw: n=134  W=121/L=13  WR=90.3%
- Refine: exclude session_bucket=asia drops 6/13 losers (46%)
- **Final: n=113  W=106/L=7  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W04.  `H60=H60c AND T4=T4c AND RSI=RSI4`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 6/16 losers (38%)
- **Final: n=111  W=101/L=10  WR=91.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W05.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=121  W=113/L=8  WR=93.4%
- Refine: exclude session_bucket=ny_close drops 5/8 losers (62%)
- **Final: n=110  W=107/L=3  WR=97.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W06.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=121  W=113/L=8  WR=93.4%
- Refine: exclude session_bucket=ny_close drops 5/8 losers (62%)
- **Final: n=110  W=107/L=3  WR=97.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W07.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=121  W=113/L=8  WR=93.4%
- Refine: exclude session_bucket=ny_close drops 5/8 losers (62%)
- **Final: n=110  W=107/L=3  WR=97.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W08.  `H20=H20b AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude session_bucket=asia drops 8/16 losers (50%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W09.  `H20=H20b AND T4=T4c AND direction_exec=short`
- Raw: n=114  W=103/L=11  WR=90.4%
- Refine: exclude session_bucket=asia drops 4/11 losers (36%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  AVOID when session=asia

### W10.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 5/17 losers (29%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W11.  `H20=H20b AND T1=T1c AND T4=T4c`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude session_bucket=ny_open drops 5/11 losers (45%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W12.  `H20=H20b AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=105  W=97/L=8  WR=92.4%
- Refine: exclude session_bucket=london drops 3/8 losers (38%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; RSI 50-60 upper neutral  •  AVOID when session=london

### W13.  `H60=H60c AND T4=T4c AND BBP=BBP4`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 strongly against

### W14.  `H20=H20b AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude session_bucket=asia drops 3/7 losers (43%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W15.  `H20=H20b AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude session_bucket=asia drops 3/7 losers (43%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W16.  `H60=H60c AND T4=T4c AND ZS=ZS4`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W17.  `H60=H60c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W18.  `H20=H20b AND H60=H60c AND T4=T4c`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude session_bucket=ny_open drops 5/13 losers (38%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 neutral; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W19.  `H20=H20b AND T1=T1c AND direction_exec=short`
- Raw: n=96  W=90/L=6  WR=93.8%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  AVOID when lower third

### W20.  `H20=H20b AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude session_bucket=asia drops 5/10 losers (50%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W21.  `H60=H60c AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 6/12 losers (50%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W22.  `H60=H60c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 6/14 losers (43%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W23.  `H20=H20b AND T1=T1c AND RSI=RSI4`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude direction_exec=long drops 9/12 losers (75%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when long

### W24.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude T4=T4a drops 13/13 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20b AND RSI=RSI4 AND direction_exec=short`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude session_bucket=asia drops 4/6 losers (67%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 50-60 upper neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is H60=H60a (17/63 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L02.  `H20=H20d AND T4=T4a AND RSI=RSI4`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is BBP=BBP4 (27/65 of losers there)
- **Sharp: n=35  W=8/L=27  WR=22.9%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L03.  `H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is BBP=BBP5 (18/57 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when just touched upper band

### L04.  `T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is ZS=ZS5 (28/57 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is ZS=ZS5 (28/57 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is ZS=ZS5 (28/57 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H20=H20c AND T4=T4c AND direction_exec=long`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (29/51 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L08.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H20=H20d (16/52 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L09.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H20=H20d (16/52 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L10.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_close (16/52 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=ny_close

### L11.  `H20=H20d AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is session_bucket=london_open (15/46 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L12.  `H20=H20d AND T1=T1a AND RSI=RSI4`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is H60=H60a (17/46 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L13.  `H20=H20d AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=70  W=23/L=47  WR=32.9%
- Sharpen: sharpest is H60=H60a (19/47 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF20 mildly against; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L14.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is H20=H20d (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L15.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is H20=H20a (21/42 of losers there)
- **Sharp: n=28  W=7/L=21  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L16.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=65  W=16/L=49  WR=24.6%
- Sharpen: sharpest is session_bucket=ny_close (19/49 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  ONLY when session=ny_close

### L17.  `H20=H20d AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is H60=H60a (19/46 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF20 mildly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20d AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is H60=H60a (19/46 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF20 mildly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L19.  `H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_close (12/43 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L20.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=59  W=19/L=40  WR=32.2%
- Sharpen: sharpest is BBP=BBP1 (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when just touched lower band

### L21.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=58  W=14/L=44  WR=24.1%
- Sharpen: sharpest is H20=H20b (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 slightly aligned

### L22.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=58  W=14/L=44  WR=24.1%
- Sharpen: sharpest is H20=H20b (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 slightly aligned

### L23.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=58  W=14/L=44  WR=24.1%
- Sharpen: sharpest is H20=H20b (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 slightly aligned

### L24.  `T4=T4a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP4 (20/39 of losers there)
- **Sharp: n=26  W=6/L=20  WR=23.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when upper third

### L25.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=56  W=16/L=40  WR=28.6%
- Sharpen: sharpest is session_bucket=ny_close (12/40 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(21/10) | H20d(12/21), H20e(29/34) |
| H60 | H60e(34/25) | H60a(27/36) |
| T1 | T1c(52/47) | T1a(47/53) |
| T4 | T4c(53/45) | T4a(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
