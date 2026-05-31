# NZD_CAD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,558**  (W=1,015 / L=543)  -  WR: **65.1%**

## Session distribution

- ny_mid: n=335  W=217/L=118  WR=64.8%
- asia: n=275  W=176/L=99  WR=64.0%
- london_open: n=246  W=161/L=85  WR=65.4%
- ny_open: n=229  W=159/L=70  WR=69.4%
- ny_close: n=204  W=129/L=75  WR=63.2%
- london: n=165  W=105/L=60  WR=63.6%
- asia_late: n=72  W=49/L=23  WR=68.1%
- off_hours: n=32  W=19/L=13  WR=59.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=203  W=175/L=28  WR=86.2%
- Refine: exclude BBP=BBP4 drops 11/28 losers (39%)
- **Final: n=172  W=155/L=17  WR=90.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W02.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=183  W=162/L=21  WR=88.5%
- Refine: exclude session_bucket=london drops 9/21 losers (43%)
- **Final: n=163  W=151/L=12  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=london

### W03.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=178  W=155/L=23  WR=87.1%
- Refine: exclude BBP=BBP2 drops 16/23 losers (70%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  AVOID when lower third

### W04.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=168  W=150/L=18  WR=89.3%
- Refine: exclude session_bucket=london drops 6/18 losers (33%)
- **Final: n=151  W=139/L=12  WR=92.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=london

### W05.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=138  W=123/L=15  WR=89.1%
- Refine: exclude session_bucket=london drops 9/15 losers (60%)
- **Final: n=122  W=116/L=6  WR=95.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W06.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=135  W=125/L=10  WR=92.6%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W07.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=135  W=119/L=16  WR=88.1%
- Refine: exclude session_bucket=asia drops 6/16 losers (38%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W08.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude session_bucket=london drops 6/17 losers (35%)
- **Final: n=120  W=109/L=11  WR=90.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W09.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude RSI=RSI3 drops 18/18 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W10.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude session_bucket=asia drops 6/16 losers (38%)
- **Final: n=114  W=104/L=10  WR=91.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W11.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude BBP=BBP4 drops 5/11 losers (45%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when upper third

### W12.  `T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude RSI=RSI3 drops 16/16 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W13.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=asia drops 6/16 losers (38%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W14.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W15.  `T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20c drops 8/14 losers (57%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 neutral

### W16.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20c drops 8/14 losers (57%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 neutral

### W17.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude session_bucket=ny_open drops 7/9 losers (78%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W18.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=london_open drops 11/13 losers (85%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W19.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when upper third

### W20.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/12 losers (33%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W21.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude direction_exec=long drops 11/12 losers (92%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when long

### W22.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W23.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W24.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=asia  •  AVOID when HTF20 strongly against

### W25.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=132  W=51/L=81  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (37/81 of losers there)
- **Sharp: n=51  W=14/L=37  WR=27.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H20=H20e AND H60=H60a AND T4=T4a`
- Raw: n=98  W=30/L=68  WR=30.6%
- Sharpen: sharpest is T1=T1c (28/68 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when 1h trend AGAINST trade

### L03.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (15/55 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L04.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_open (15/50 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L05.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=81  W=32/L=49  WR=39.5%
- Sharpen: sharpest is session_bucket=ny_open (15/49 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is direction_exec=short (29/45 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when short

### L07.  `H20=H20c AND T4=T4c AND direction_exec=long`
- Raw: n=74  W=24/L=50  WR=32.4%
- Sharpen: sharpest is RSI=RSI1 (15/50 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L08.  `H20=H20c AND T1=T1c AND direction_exec=long`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (31/45 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=asia

### L09.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=71  W=22/L=49  WR=31.0%
- Sharpen: sharpest is H60=H60a (24/49 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is ZS=ZS1 (13/44 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is BBP=BBP1 (37/46 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L12.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is H20=H20e (13/45 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L13.  `T1=T1a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is direction_exec=short (37/46 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when short

### L14.  `T1=T1a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is direction_exec=short (37/46 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when short

### L15.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: sharpest is H20=H20c (31/43 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 neutral

### L16.  `T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: sharpest is T1=T1a (16/43 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=asia  •  ONLY when 1h trend WITH trade

### L17.  `T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is T1=T1a (16/42 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when 1h trend WITH trade

### L18.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is T1=T1a (16/42 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when 1h trend WITH trade

### L19.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is session_bucket=asia (31/43 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L20.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is session_bucket=asia (31/43 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L21.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (9/42 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L22.  `H60=H60e AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L23.  `H60=H60e AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L24.  `H60=H60e AND T1=T1a AND BBP=BBP1`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (11/40 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band  •  ONLY when session=ny_open

### L25.  `H60=H60e AND T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (11/40 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(16/10) | — |
| H60 | H60a(48/40) | H60e(42/48) |
| T1 | — | — |
| T4 | T4c(53/45) | T4a(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
