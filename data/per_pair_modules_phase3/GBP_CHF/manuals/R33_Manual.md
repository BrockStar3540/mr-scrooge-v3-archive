# GBP_CHF — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,389**  (W=1,526 / L=863)  -  WR: **63.9%**

## Session distribution

- ny_mid: n=712  W=484/L=228  WR=68.0%
- london_open: n=551  W=348/L=203  WR=63.2%
- ny_open: n=441  W=289/L=152  WR=65.5%
- london: n=361  W=218/L=143  WR=60.4%
- asia: n=219  W=119/L=100  WR=54.3%
- asia_late: n=50  W=38/L=12  WR=76.0%
- ny_close: n=42  W=22/L=20  WR=52.4%
- off_hours: n=13  W=8/L=5  WR=61.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=162  W=142/L=20  WR=87.7%
- Refine: exclude H60=H60a drops 11/20 losers (55%)
- **Final: n=119  W=110/L=9  WR=92.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W02.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=159  W=141/L=18  WR=88.7%
- Refine: exclude H20=H20e drops 6/18 losers (33%)
- **Final: n=143  W=131/L=12  WR=91.6%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W03.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=154  W=133/L=21  WR=86.4%
- Refine: exclude H20=H20e drops 7/21 losers (33%)
- **Final: n=141  W=127/L=14  WR=90.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W04.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=150  W=135/L=15  WR=90.0%
- Refine: exclude H60=H60e drops 15/15 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W05.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=139  W=125/L=14  WR=89.9%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W06.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude H60=H60a drops 10/18 losers (56%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W07.  `H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=136  W=117/L=19  WR=86.0%
- Refine: exclude H20=H20e drops 6/19 losers (32%)
- **Final: n=120  W=107/L=13  WR=89.2%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W08.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=128  W=109/L=19  WR=85.2%
- Refine: exclude RSI=RSI3 drops 9/19 losers (47%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W09.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude H20=H20e drops 6/18 losers (33%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W10.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude H20=H20e drops 6/18 losers (33%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W11.  `H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=121  W=109/L=12  WR=90.1%
- Refine: exclude direction_exec=short drops 11/12 losers (92%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when short

### W12.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=121  W=107/L=14  WR=88.4%
- Refine: exclude session_bucket=london_open drops 7/14 losers (50%)
- **Final: n=104  W=97/L=7  WR=93.3%**
- **Dir: LONG**  •  just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W13.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude session_bucket=london_open drops 8/15 losers (53%)
- **Final: n=104  W=97/L=7  WR=93.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W14.  `T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=115  W=103/L=12  WR=89.6%
- Refine: exclude H20=H20e drops 6/12 losers (50%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W15.  `T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=113  W=107/L=6  WR=94.7%
- Refine: exclude H60=H60a drops 5/6 losers (83%)
- **Final: n=104  W=103/L=1  WR=99.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W16.  `H20=H20b AND H60=H60e AND T4=T4a`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude BBP=BBP3 drops 5/8 losers (62%)
- **Final: n=97  W=94/L=3  WR=96.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  AVOID when middle of band

### W17.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude H60=H60a drops 9/16 losers (56%)
- **Final: n=94  W=87/L=7  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W18.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude H20=H20e drops 6/12 losers (50%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W19.  `H20=H20a AND H60=H60d AND RSI=RSI4`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude session_bucket=london_open drops 12/16 losers (75%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W20.  `H20=H20b AND H60=H60e AND direction_exec=long`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude ZS=ZS3 drops 9/11 losers (82%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against  •  AVOID when zscore -1 to +1 neutral

### W21.  `H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude H20=H20c drops 7/15 losers (47%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 neutral

### W22.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude H20=H20c drops 7/15 losers (47%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 neutral

### W23.  `H20=H20b AND H60=H60e AND RSI=RSI4`
- Raw: n=106  W=99/L=7  WR=93.4%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=87  W=85/L=2  WR=97.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W24.  `T4=T4a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=92  W=89/L=3  WR=96.7%**
- **Dir: LONG**  •  4h trend WITH trade; just touched lower band  •  AVOID when session=london_open

### W25.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=92  W=89/L=3  WR=96.7%**
- **Dir: LONG**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=153  W=61/L=92  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (20/92 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=asia

### L02.  `H20=H20e AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (29/91 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=london_open

### L03.  `T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: sharpest is T4=T4c (38/81 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 4h trend AGAINST trade

### L04.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is RSI=RSI4 (40/67 of losers there)
- **Sharp: n=54  W=14/L=40  WR=25.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L05.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is BBP=BBP0 (29/67 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L06.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=108  W=43/L=65  WR=39.8%
- Sharpen: sharpest is H60=H60a (48/65 of losers there)
- **Sharp: n=67  W=19/L=48  WR=28.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london  •  ONLY when HTF60 aligned WITH trade

### L07.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=101  W=36/L=65  WR=35.6%
- Sharpen: sharpest is H60=H60a (31/65 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L08.  `H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is H20=H20d (19/65 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london  •  ONLY when HTF20 mildly against

### L09.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=33/L=64  WR=34.0%
- Sharpen: sharpest is H20=H20e (21/64 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L10.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=93  W=33/L=60  WR=35.5%
- Sharpen: sharpest is BBP=BBP0 (24/60 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L11.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is RSI=RSI4 (39/59 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L12.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is H20=H20d (19/57 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  ONLY when HTF20 mildly against

### L13.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is H60=H60a (37/55 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L14.  `H60=H60a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is BBP=BBP0 (25/54 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L15.  `H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is direction_exec=short (48/59 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when short

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4c (51/51 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T1=T1c (51/51 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L18.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is H20=H20e (29/54 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when HTF20 strongly against

### L19.  `H20=H20e AND H60=H60b AND direction_exec=short`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (41/50 of losers there)
- **Sharp: n=43  W=2/L=41  WR=4.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned  •  ONLY when RSI 50-60 upper neutral

### L20.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=81  W=21/L=60  WR=25.9%
- Sharpen: sharpest is H60=H60a (48/60 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L21.  `H20=H20e AND H60=H60b AND RSI=RSI4`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is direction_exec=short (41/51 of losers there)
- **Sharp: n=43  W=2/L=41  WR=4.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; RSI 50-60 upper neutral  •  ONLY when short

### L22.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is H60=H60a (27/48 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L23.  `H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=77  W=24/L=53  WR=31.2%
- Sharpen: sharpest is T4=T4c (48/53 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L24.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is RSI=RSI4 (38/50 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L25.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is T1=T1c (39/47 of losers there)
- **Sharp: n=53  W=14/L=39  WR=26.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(36/26) | H20e(25/37) |
| H60 | H60e(46/31) | H60a(29/45) |
| T1 | — | — |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/44) | short(43/56) |
| session_bucket | ny_mid(32/26) | — |

*Read: `bucket(winner%/loser%)`.*
