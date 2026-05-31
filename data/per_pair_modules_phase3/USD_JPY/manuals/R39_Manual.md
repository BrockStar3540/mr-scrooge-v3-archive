# USD_JPY — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,180**  (W=2,543 / L=1,637)  -  WR: **60.8%**

## Session distribution

- asia: n=1467  W=882/L=585  WR=60.1%
- london_open: n=681  W=423/L=258  WR=62.1%
- ny_mid: n=628  W=364/L=264  WR=58.0%
- ny_close: n=552  W=348/L=204  WR=63.0%
- ny_open: n=321  W=191/L=130  WR=59.5%
- asia_late: n=307  W=190/L=117  WR=61.9%
- london: n=132  W=87/L=45  WR=65.9%
- off_hours: n=92  W=58/L=34  WR=63.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 4/15 losers (27%)
- **Final: n=93  W=82/L=11  WR=88.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_open

### W02.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 4/15 losers (27%)
- **Final: n=93  W=82/L=11  WR=88.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_open

### W03.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_open drops 4/13 losers (31%)
- **Final: n=89  W=80/L=9  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W04.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude BBP=BBP4 drops 12/14 losers (86%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when upper third

### W05.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude BBP=BBP4 drops 12/14 losers (86%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when upper third

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude BBP=BBP4 drops 12/14 losers (86%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when upper third

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude session_bucket=ny_open drops 4/13 losers (31%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W08.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=89  W=85/L=4  WR=95.5%
- Refine: exclude BBP=BBP5 drops 2/4 losers (50%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W09.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude BBP=BBP0 drops 7/11 losers (64%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W10.  `BBP=BBP1 AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude H60=H60c drops 6/11 losers (55%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 neutral

### W11.  `H20=H20e AND H60=H60a AND ZS=ZS1`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=asia drops 11/12 losers (92%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W12.  `H20=H20e AND H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=asia drops 11/12 losers (92%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W13.  `H20=H20e AND H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W14.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60e drops 3/7 losers (43%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W15.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude ZS=ZS3 drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude ZS=ZS3 drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W17.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude T4=T4a drops 5/10 losers (50%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=ny_close  •  AVOID when 4h trend WITH trade

### W18.  `T1=T1a AND ZS=ZS3 AND session_bucket=asia_late`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=asia_late  •  AVOID when HTF60 strongly against

### W19.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3 AND session_bucket=asia_late`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=asia_late  •  AVOID when HTF60 strongly against

### W20.  `T4=T4c AND RSI=RSI3 AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude H60=H60e drops 4/9 losers (44%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W21.  `H60=H60a AND BBP=BBP1 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude strategy_id=BR2_vcb_short drops 2/4 losers (50%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=BR2_vcb_short

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude ZS=ZS3 drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60b AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude BBP=BBP5 drops 4/9 losers (44%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: LONG**  •  HTF60 slightly aligned; session=asia  •  AVOID when just touched upper band

### W24.  `H60=H60b AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude BBP=BBP5 drops 4/9 losers (44%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade; session=asia  •  AVOID when just touched upper band

### W25.  `H60=H60b AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude BBP=BBP5 drops 4/9 losers (44%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=170  W=62/L=108  WR=36.5%
- Sharpen: sharpest is BBP=BBP0 (62/108 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L02.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=160  W=55/L=105  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=55/L=105  WR=34.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=157  W=54/L=103  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=54/L=103  WR=34.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak

### L04.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=157  W=54/L=103  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=54/L=103  WR=34.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=157  W=54/L=103  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=54/L=103  WR=34.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak

### L06.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=157  W=55/L=102  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=55/L=102  WR=35.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak

### L07.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=157  W=55/L=102  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=55/L=102  WR=35.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak

### L08.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=157  W=55/L=102  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=55/L=102  WR=35.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak

### L09.  `H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=154  W=54/L=100  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=154  W=54/L=100  WR=35.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak

### L10.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=154  W=54/L=100  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=154  W=54/L=100  WR=35.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak

### L11.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=154  W=54/L=100  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=154  W=54/L=100  WR=35.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak

### L12.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=146  W=52/L=94  WR=35.6%
- Sharpen: sharpest is session_bucket=ny_mid (24/94 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L13.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=130  W=44/L=86  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (24/86 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L14.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=126  W=41/L=85  WR=32.5%
- Sharpen: sharpest is session_bucket=ny_mid (24/85 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L15.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=119  W=41/L=78  WR=34.5%
- Sharpen: sharpest is session_bucket=ny_mid (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L16.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is H60=H60e (62/74 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L17.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is session_bucket=ny_mid (24/74 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L18.  `H60=H60e AND T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=103  W=33/L=70  WR=32.0%
- Sharpen: sharpest is ZS=ZS1 (62/70 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=95  W=35/L=60  WR=36.8%
- Sharpen: sharpest is H20=H20e (43/60 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L20.  `H60=H60d AND RSI=RSI3 AND direction_exec=short`
- Raw: n=92  W=29/L=63  WR=31.5%
- Sharpen: sharpest is session_bucket=asia (34/63 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 40-50 lower neutral  •  ONLY when session=asia

### L21.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=90  W=25/L=65  WR=27.8%
- Sharpen: sharpest is session_bucket=ny_mid (24/65 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L22.  `H20=H20e AND H60=H60e AND BBP=BBP0`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is RSI=RSI3 (43/58 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L23.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP0`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is RSI=RSI3 (43/58 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L24.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (21/53 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L25.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=21/L=66  WR=24.1%
- Sharpen: sharpest is H60=H60e (46/66 of losers there)
- **Sharp: n=53  W=7/L=46  WR=13.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
