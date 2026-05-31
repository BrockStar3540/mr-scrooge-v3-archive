# GBP_CAD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,879**  (W=1,846 / L=1,033)  -  WR: **64.1%**

## Session distribution

- asia: n=1123  W=745/L=378  WR=66.3%
- ny_close: n=555  W=346/L=209  WR=62.3%
- london_open: n=522  W=327/L=195  WR=62.6%
- asia_late: n=265  W=162/L=103  WR=61.1%
- off_hours: n=155  W=103/L=52  WR=66.5%
- ny_mid: n=101  W=66/L=35  WR=65.3%
- london: n=88  W=53/L=35  WR=60.2%
- ny_open: n=70  W=44/L=26  WR=62.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=220  W=194/L=26  WR=88.2%
- Refine: exclude BBP=BBP4 drops 11/26 losers (42%)
- **Final: n=191  W=176/L=15  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W02.  `H20=H20a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=219  W=196/L=23  WR=89.5%
- Refine: exclude T1=T1a drops 17/23 losers (74%)
- **Final: n=118  W=112/L=6  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend WITH trade

### W03.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=216  W=187/L=29  WR=86.6%
- Refine: exclude H60=H60c drops 15/29 losers (52%)
- **Final: n=175  W=161/L=14  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 neutral

### W04.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=179  W=160/L=19  WR=89.4%
- Refine: exclude T1=T1a drops 13/19 losers (68%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend WITH trade

### W05.  `H20=H20a AND T1=T1a AND ZS=ZS2`
- Raw: n=175  W=152/L=23  WR=86.9%
- Refine: exclude session_bucket=asia drops 16/23 losers (70%)
- **Final: n=121  W=114/L=7  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W06.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=175  W=152/L=23  WR=86.9%
- Refine: exclude session_bucket=asia drops 16/23 losers (70%)
- **Final: n=121  W=114/L=7  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=asia

### W07.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=166  W=143/L=23  WR=86.1%
- Refine: exclude H60=H60c drops 15/23 losers (65%)
- **Final: n=125  W=117/L=8  WR=93.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 neutral

### W08.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=155  W=141/L=14  WR=91.0%
- Refine: exclude BBP=BBP2 drops 9/14 losers (64%)
- **Final: n=106  W=101/L=5  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when lower third

### W09.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=155  W=141/L=14  WR=91.0%
- Refine: exclude BBP=BBP2 drops 9/14 losers (64%)
- **Final: n=106  W=101/L=5  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W10.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=146  W=132/L=14  WR=90.4%
- Refine: exclude session_bucket=london_open drops 10/14 losers (71%)
- **Final: n=134  W=130/L=4  WR=97.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W11.  `H20=H20c AND H60=H60e AND RSI=RSI3`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude session_bucket=london_open drops 10/18 losers (56%)
- **Final: n=131  W=123/L=8  WR=93.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W12.  `H20=H20c AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude session_bucket=london_open drops 10/18 losers (56%)
- **Final: n=131  W=123/L=8  WR=93.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W13.  `H20=H20c AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude session_bucket=london_open drops 10/18 losers (56%)
- **Final: n=131  W=123/L=8  WR=93.9%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W14.  `H20=H20a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=141  W=121/L=20  WR=85.8%
- Refine: exclude session_bucket=london_open drops 15/20 losers (75%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W15.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=140  W=123/L=17  WR=87.9%
- Refine: exclude session_bucket=asia drops 12/17 losers (71%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=asia

### W16.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude session_bucket=london_open drops 10/14 losers (71%)
- **Final: n=122  W=118/L=4  WR=96.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W17.  `H60=H60b AND T1=T1a AND session_bucket=asia`
- Raw: n=132  W=117/L=15  WR=88.6%
- Refine: exclude T4=T4a drops 12/15 losers (80%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20a AND H60=H60a AND ZS=ZS2`
- Raw: n=131  W=114/L=17  WR=87.0%
- Refine: exclude RSI=RSI3 drops 17/17 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W19.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=131  W=114/L=17  WR=87.0%
- Refine: exclude RSI=RSI3 drops 17/17 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude H60=H60a drops 10/14 losers (71%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W21.  `H60=H60b AND direction_exec=short AND session_bucket=asia`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude T4=T4a drops 12/15 losers (80%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; session=asia  •  AVOID when 4h trend WITH trade

### W22.  `H60=H60b AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude T4=T4a drops 12/15 losers (80%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when 4h trend WITH trade

### W23.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=129  W=116/L=13  WR=89.9%
- Refine: exclude session_bucket=asia drops 10/13 losers (77%)
- **Final: n=91  W=88/L=3  WR=96.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W24.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=129  W=116/L=13  WR=89.9%
- Refine: exclude T1=T1a drops 13/13 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude BBP=BBP2 drops 9/14 losers (64%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=169  W=60/L=109  WR=35.5%
- Sharpen: sharpest is BBP=BBP1 (31/109 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when just touched lower band

### L02.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (45/102 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `H20=H20e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=144  W=42/L=102  WR=29.2%
- Sharpen: sharpest is ZS=ZS1 (34/102 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20e AND T1=T1c AND ZS=ZS2`
- Raw: n=141  W=54/L=87  WR=38.3%
- Sharpen: sharpest is H60=H60e (62/87 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L05.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=141  W=54/L=87  WR=38.3%
- Sharpen: sharpest is H60=H60e (62/87 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=131  W=49/L=82  WR=37.4%
- Sharpen: sharpest is ZS=ZS1 (42/82 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=125  W=36/L=89  WR=28.8%
- Sharpen: sharpest is ZS=ZS1 (34/89 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20e AND H60=H60e AND ZS=ZS2`
- Raw: n=120  W=41/L=79  WR=34.2%
- Sharpen: sharpest is T1=T1c (62/79 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L09.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=120  W=41/L=79  WR=34.2%
- Sharpen: sharpest is T1=T1c (62/79 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (27/72 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=113  W=36/L=77  WR=31.9%
- Sharpen: sharpest is ZS=ZS1 (37/77 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is T1=T1c (59/68 of losers there)
- **Sharp: n=78  W=19/L=59  WR=24.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20b AND H60=H60d AND T1=T1c`
- Raw: n=112  W=38/L=74  WR=33.9%
- Sharpen: sharpest is RSI=RSI2 (24/74 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L14.  `H20=H20b AND H60=H60d AND direction_exec=long`
- Raw: n=112  W=38/L=74  WR=33.9%
- Sharpen: sharpest is RSI=RSI2 (24/74 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 mildly against  •  ONLY when RSI 30-40 weak

### L15.  `H20=H20b AND H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=112  W=38/L=74  WR=33.9%
- Sharpen: sharpest is RSI=RSI2 (24/74 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=111  W=34/L=77  WR=30.6%
- Sharpen: sharpest is ZS=ZS1 (37/77 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is T4=T4c (69/69 of losers there)
- **Sharp: n=85  W=16/L=69  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=106  W=40/L=66  WR=37.7%
- Sharpen: sharpest is H60=H60e (47/66 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=104  W=34/L=70  WR=32.7%
- Sharpen: sharpest is H60=H60e (45/70 of losers there)
- **Sharp: n=61  W=16/L=45  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L20.  `H20=H20e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (34/63 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L21.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is T1=T1c (47/64 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=98  W=32/L=66  WR=32.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=98  W=32/L=66  WR=32.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L23.  `H20=H20c AND H60=H60a AND RSI=RSI3`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is ZS=ZS1 (32/65 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H20=H20c AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is ZS=ZS1 (32/65 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H20=H20c AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is ZS=ZS1 (32/65 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(34/21) | H20e(21/32), H20b(13/19) |
| H60 | — | H60d(7/12) |
| T1 | T1a(54/44) | T1c(46/56) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/46) | long(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
