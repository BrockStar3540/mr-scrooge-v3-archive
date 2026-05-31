# EUR_GBP — R26 Manual

## Regime centroid (locked factors)

- **BB = BB0**  (very narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **935**  (W=616 / L=319)  -  WR: **65.9%**

## Session distribution

- asia: n=481  W=315/L=166  WR=65.5%
- ny_close: n=139  W=93/L=46  WR=66.9%
- asia_late: n=99  W=69/L=30  WR=69.7%
- off_hours: n=77  W=51/L=26  WR=66.2%
- london_open: n=69  W=44/L=25  WR=63.8%
- london: n=29  W=17/L=12  WR=58.6%
- ny_open: n=22  W=16/L=6  WR=72.7%
- ny_mid: n=19  W=11/L=8  WR=57.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=152  W=131/L=21  WR=86.2%
- Refine: exclude H60=H60e drops 10/21 losers (48%)
- **Final: n=131  W=120/L=11  WR=91.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 strongly against

### W02.  `H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude BBP=BBP4 drops 5/16 losers (31%)
- **Final: n=98  W=87/L=11  WR=88.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when upper third

### W03.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude session_bucket=london drops 5/10 losers (50%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=london

### W04.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=91  W=85/L=6  WR=93.4%
- Refine: exclude H60=H60b drops 2/6 losers (33%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W05.  `H20=H20b AND T1=T1a AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude H60=H60e drops 5/12 losers (42%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade  •  AVOID when HTF60 strongly against

### W06.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T4=T4c drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when 4h trend AGAINST trade

### W07.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude ZS=ZS1 drops 7/10 losers (70%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W08.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude ZS=ZS1 drops 4/7 losers (57%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude direction_exec=short drops 11/12 losers (92%)
- **Final: n=21  W=20/L=1  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when short

### W10.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T1=T1c drops 8/9 losers (89%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W11.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T1=T1c drops 8/9 losers (89%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H20=H20e drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W13.  `H20=H20b AND T4=T4a AND direction_exec=short`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H60=H60e drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade  •  AVOID when HTF60 strongly against

### W14.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude H60=H60b drops 5/8 losers (62%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 slightly aligned

### W15.  `H20=H20a AND T1=T1a AND RSI=RSI4`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS1 drops 3/8 losers (38%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -3 to -2 deep oversold

### W16.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W17.  `H20=H20a AND T4=T4c AND BBP=BBP4`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI5 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 60-70 strong

### W18.  `H20=H20a AND T1=T1a AND RSI=RSI3`
- Raw: n=67  W=62/L=5  WR=92.5%
- Refine: exclude T4=T4c drops 3/5 losers (60%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude T4=T4c drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when 4h trend AGAINST trade

### W20.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude T4=T4c drops 8/10 losers (80%)
- **Final: n=31  W=29/L=2  WR=93.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20a AND H60=H60a AND direction_exec=short`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 7/9 losers (78%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  AVOID when session=ny_close

### W22.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude ZS=ZS1 drops 3/5 losers (60%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W23.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H60=H60a drops 3/9 losers (33%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W24.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude H60=H60e drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 strongly against

### W25.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude H60=H60b drops 5/8 losers (62%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H20=H20d (26/66 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L02.  `H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H20=H20d (28/43 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L03.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=64  W=20/L=44  WR=31.2%
- Sharpen: sharpest is BBP=BBP4 (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when upper third

### L04.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is T1=T1c (22/37 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is T1=T1c (21/37 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20d AND T1=T1c AND direction_exec=long`
- Raw: n=54  W=19/L=35  WR=35.2%
- Sharpen: sharpest is H60=H60e (28/35 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L07.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=52  W=12/L=40  WR=23.1%
- Sharpen: sharpest is RSI=RSI3 (27/40 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L08.  `H20=H20d AND H60=H60e AND direction_exec=long`
- Raw: n=52  W=16/L=36  WR=30.8%
- Sharpen: sharpest is BBP=BBP6 (15/36 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against  •  ONLY when deep above upper band

### L09.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is T1=T1c (20/32 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L10.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is T1=T1c (20/32 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L11.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is H20=H20e (20/31 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=49  W=17/L=32  WR=34.7%
- Sharpen: sharpest is ZS=ZS4 (18/32 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L13.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60e (20/30 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

### L14.  `H20=H20d AND T4=T4c AND direction_exec=long`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is BBP=BBP6 (16/31 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade  •  ONLY when deep above upper band

### L15.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is H20=H20d (21/31 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI3`
- Raw: n=44  W=12/L=32  WR=27.3%
- Sharpen: sharpest is direction_exec=long (27/32 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when long

### L17.  `H20=H20d AND H60=H60e AND T1=T1c`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is BBP=BBP6 (15/28 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep above upper band

### L18.  `H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is H20=H20d (15/27 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 mildly against

### L19.  `H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is BBP=BBP2 (10/27 of losers there)
- **Sharp: n=12  W=2/L=10  WR=16.7%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when lower third

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI4`
- Raw: n=41  W=8/L=33  WR=19.5%
- Sharpen: sharpest is ZS=ZS4 (20/33 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L21.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (20/26 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L22.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is H20=H20d (13/25 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 mildly against

### L23.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=40  W=14/L=26  WR=35.0%
- Sharpen: sharpest is RSI=RSI4 (15/26 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L24.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (20/25 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=39  W=10/L=29  WR=25.6%
- Sharpen: sharpest is RSI=RSI3 (20/29 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(42/19) | H20e(22/41), H20d(13/22) |
| H60 | — | H60e(17/29) |
| T1 | T1a(62/40) | T1c(38/60) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(58/43) | long(42/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
