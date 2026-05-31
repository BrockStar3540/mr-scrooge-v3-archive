# EUR_JPY — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,239**  (W=1,985 / L=1,254)  -  WR: **61.3%**

## Session distribution

- asia: n=1171  W=715/L=456  WR=61.1%
- london_open: n=583  W=361/L=222  WR=61.9%
- ny_mid: n=422  W=249/L=173  WR=59.0%
- ny_close: n=393  W=245/L=148  WR=62.3%
- ny_open: n=347  W=214/L=133  WR=61.7%
- london: n=178  W=109/L=69  WR=61.2%
- asia_late: n=100  W=59/L=41  WR=59.0%
- off_hours: n=45  W=33/L=12  WR=73.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=170  W=152/L=18  WR=89.4%
- Refine: exclude H60=H60a drops 18/18 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W02.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=166  W=144/L=22  WR=86.7%
- Refine: exclude T1=T1c drops 21/22 losers (95%)
- **Final: n=93  W=92/L=1  WR=98.9%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W03.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=166  W=144/L=22  WR=86.7%
- Refine: exclude T1=T1c drops 21/22 losers (95%)
- **Final: n=93  W=92/L=1  WR=98.9%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W04.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=146  W=128/L=18  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 12/18 losers (67%)
- **Final: n=121  W=115/L=6  WR=95.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W05.  `T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=138  W=118/L=20  WR=85.5%
- Refine: exclude direction_exec=long drops 12/20 losers (60%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when long

### W06.  `H20=H20a AND H60=H60e AND RSI=RSI3`
- Raw: n=136  W=121/L=15  WR=89.0%
- Refine: exclude BBP=BBP1 drops 7/15 losers (47%)
- **Final: n=129  W=121/L=8  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W07.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=136  W=121/L=15  WR=89.0%
- Refine: exclude BBP=BBP1 drops 7/15 losers (47%)
- **Final: n=129  W=121/L=8  WR=93.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W08.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=136  W=121/L=15  WR=89.0%
- Refine: exclude BBP=BBP1 drops 7/15 losers (47%)
- **Final: n=129  W=121/L=8  WR=93.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W09.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude T1=T1c drops 14/14 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W10.  `T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=131  W=120/L=11  WR=91.6%
- Refine: exclude RSI=RSI4 drops 8/11 losers (73%)
- **Final: n=96  W=93/L=3  WR=96.9%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third  •  AVOID when RSI 50-60 upper neutral

### W11.  `T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=127  W=110/L=17  WR=86.6%
- Refine: exclude RSI=RSI4 drops 12/17 losers (71%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W12.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=127  W=110/L=17  WR=86.6%
- Refine: exclude RSI=RSI4 drops 12/17 losers (71%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T1=T1c drops 18/19 losers (95%)
- **Final: n=62  W=61/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W14.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T1=T1c drops 18/19 losers (95%)
- **Final: n=62  W=61/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W15.  `T1=T1a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude direction_exec=long drops 17/18 losers (94%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=london_open  •  AVOID when long

### W16.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude T1=T1c drops 17/18 losers (94%)
- **Final: n=62  W=61/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W17.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude ZS=ZS1 drops 13/16 losers (81%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W18.  `T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=121  W=113/L=8  WR=93.4%
- Refine: exclude RSI=RSI4 drops 7/8 losers (88%)
- **Final: n=93  W=92/L=1  WR=98.9%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W19.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=121  W=113/L=8  WR=93.4%
- Refine: exclude RSI=RSI4 drops 7/8 losers (88%)
- **Final: n=93  W=92/L=1  WR=98.9%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W20.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude session_bucket=ny_open drops 12/14 losers (86%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W21.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude ZS=ZS1 drops 12/17 losers (71%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W22.  `T1=T1c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude ZS=ZS1 drops 12/17 losers (71%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W23.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude direction_exec=long drops 15/15 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=london_open  •  AVOID when long

### W24.  `T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=110  W=101/L=9  WR=91.8%
- Refine: exclude BBP=BBP4 drops 3/9 losers (33%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when upper third

### W25.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude session_bucket=ny_open drops 8/10 losers (80%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=334  W=114/L=220  WR=34.1%
- Sharpen: sharpest is T1=T1c (118/220 of losers there)
- **Sharp: n=148  W=30/L=118  WR=20.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L02.  `T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=294  W=114/L=180  WR=38.8%
- Sharpen: sharpest is T4=T4a (118/180 of losers there)
- **Sharp: n=148  W=30/L=118  WR=20.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=257  W=82/L=175  WR=31.9%
- Sharpen: sharpest is session_bucket=asia (57/175 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L04.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=257  W=82/L=175  WR=31.9%
- Sharpen: sharpest is session_bucket=asia (57/175 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L05.  `T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=242  W=88/L=154  WR=36.4%
- Sharpen: sharpest is direction_exec=long (118/154 of losers there)
- **Sharp: n=148  W=30/L=118  WR=20.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when long

### L06.  `RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=182  W=52/L=130  WR=28.6%
- Sharpen: sharpest is T4=T4a (73/130 of losers there)
- **Sharp: n=83  W=10/L=73  WR=12.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=180  W=72/L=108  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (44/108 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L08.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=180  W=72/L=108  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (44/108 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L09.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=177  W=62/L=115  WR=35.0%
- Sharpen: sharpest is T1=T1c (79/115 of losers there)
- **Sharp: n=99  W=20/L=79  WR=20.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L10.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=174  W=63/L=111  WR=36.2%
- Sharpen: sharpest is H60=H60d (21/111 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 mildly against

### L11.  `T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: sharpest is direction_exec=long (52/93 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when long

### L12.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=148  W=30/L=118  WR=20.3%
- Sharpen: sharpest is H20=H20b (48/118 of losers there)
- **Sharp: n=49  W=1/L=48  WR=2.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L13.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=146  W=48/L=98  WR=32.9%
- Sharpen: sharpest is RSI=RSI3 (48/98 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L14.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=146  W=49/L=97  WR=33.6%
- Sharpen: sharpest is T1=T1c (61/97 of losers there)
- **Sharp: n=74  W=13/L=61  WR=17.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=144  W=45/L=99  WR=31.2%
- Sharpen: sharpest is T4=T4a (57/99 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L16.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=144  W=45/L=99  WR=31.2%
- Sharpen: sharpest is T4=T4a (57/99 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=144  W=48/L=96  WR=33.3%
- Sharpen: sharpest is H20=H20b (41/96 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

### L18.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=140  W=53/L=87  WR=37.9%
- Sharpen: sharpest is session_bucket=asia (45/87 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L19.  `T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (79/85 of losers there)
- **Sharp: n=99  W=20/L=79  WR=20.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L20.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=136  W=50/L=86  WR=36.8%
- Sharpen: sharpest is T1=T1c (70/86 of losers there)
- **Sharp: n=93  W=23/L=70  WR=24.7%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L21.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=131  W=52/L=79  WR=39.7%
- Sharpen: sharpest is T1=T1c (43/79 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L22.  `T1=T1c AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=127  W=36/L=91  WR=28.3%
- Sharpen: sharpest is H20=H20b (41/91 of losers there)
- **Sharp: n=42  W=1/L=41  WR=2.4%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L23.  `T1=T1c AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=127  W=36/L=91  WR=28.3%
- Sharpen: sharpest is H20=H20b (41/91 of losers there)
- **Sharp: n=42  W=1/L=41  WR=2.4%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

### L24.  `T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=121  W=38/L=83  WR=31.4%
- Sharpen: sharpest is T1=T1c (68/83 of losers there)
- **Sharp: n=81  W=13/L=68  WR=16.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L25.  `T4=T4a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=121  W=38/L=83  WR=31.4%
- Sharpen: sharpest is T1=T1c (68/83 of losers there)
- **Sharp: n=81  W=13/L=68  WR=16.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(56/46) | T4a(44/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/48) | long(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
