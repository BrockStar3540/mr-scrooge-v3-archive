# CHF_JPY — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,714**  (W=1,651 / L=1,063)  -  WR: **60.8%**

## Session distribution

- asia: n=1048  W=636/L=412  WR=60.7%
- london_open: n=392  W=244/L=148  WR=62.2%
- ny_mid: n=292  W=182/L=110  WR=62.3%
- london: n=262  W=163/L=99  WR=62.2%
- ny_close: n=246  W=152/L=94  WR=61.8%
- ny_open: n=200  W=120/L=80  WR=60.0%
- asia_late: n=155  W=90/L=65  WR=58.1%
- off_hours: n=119  W=64/L=55  WR=53.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=135  W=121/L=14  WR=89.6%
- Refine: exclude ZS=ZS2 drops 9/14 losers (64%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W02.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=124  W=111/L=13  WR=89.5%
- Refine: exclude ZS=ZS2 drops 9/13 losers (69%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W03.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=124  W=111/L=13  WR=89.5%
- Refine: exclude ZS=ZS2 drops 9/13 losers (69%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W04.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude ZS=ZS2 drops 9/14 losers (64%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W05.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude H20=H20c drops 3/11 losers (27%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W06.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude BBP=BBP2 drops 7/11 losers (64%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when lower third

### W07.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W08.  `T1=T1a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude ZS=ZS2 drops 8/11 losers (73%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -2 to -1 oversold

### W10.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude BBP=BBP3 drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when middle of band

### W11.  `H20=H20b AND H60=H60a AND direction_exec=long`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude BBP=BBP3 drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when middle of band

### W12.  `H20=H20b AND T4=T4a AND direction_exec=long`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude BBP=BBP3 drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade  •  AVOID when middle of band

### W13.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude BBP=BBP3 drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when middle of band

### W14.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T1=T1a drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W15.  `H20=H20b AND T1=T1a AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_open drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_open

### W16.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W17.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W18.  `H60=H60e AND T1=T1c AND BBP=BBP0`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W19.  `T1=T1c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W20.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W21.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W22.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W23.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W24.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W25.  `H20=H20e AND T1=T1c AND BBP=BBP0`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=ny_open drops 6/10 losers (60%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=235  W=86/L=149  WR=36.6%
- Sharpen: sharpest is BBP=BBP4 (29/149 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L02.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=235  W=86/L=149  WR=36.6%
- Sharpen: sharpest is BBP=BBP4 (29/149 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L03.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=235  W=86/L=149  WR=36.6%
- Sharpen: sharpest is BBP=BBP4 (29/149 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L04.  `H20=H20a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=178  W=71/L=107  WR=39.9%
- Sharpen: sharpest is T4=T4c (59/107 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L05.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is BBP=BBP4 (22/102 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is BBP=BBP4 (22/102 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L07.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=145  W=55/L=90  WR=37.9%
- Sharpen: sharpest is H20=H20a (59/90 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L08.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=145  W=55/L=90  WR=37.9%
- Sharpen: sharpest is H20=H20a (59/90 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is session_bucket=london_open (19/86 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L10.  `H20=H20a AND T4=T4c AND RSI=RSI3`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (59/82 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L11.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is T4=T4c (34/74 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L12.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is T4=T4c (34/74 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: sharpest is H60=H60a (41/70 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 aligned WITH trade

### L14.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=110  W=25/L=85  WR=22.7%
- Sharpen: sharpest is T1=T1a (14/85 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend WITH trade

### L15.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (50/64 of losers there)
- **Sharp: n=64  W=14/L=50  WR=21.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L16.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=104  W=24/L=80  WR=23.1%
- Sharpen: sharpest is RSI=RSI3 (59/80 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L17.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=24/L=80  WR=23.1%
- Sharpen: sharpest is RSI=RSI3 (59/80 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L18.  `H20=H20c AND T1=T1a AND session_bucket=asia`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is BBP=BBP2 (20/64 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=asia  •  ONLY when lower third

### L19.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H60=H60a (40/64 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 aligned WITH trade

### L20.  `H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (41/60 of losers there)
- **Sharp: n=55  W=14/L=41  WR=25.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=asia

### L21.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (41/60 of losers there)
- **Sharp: n=55  W=14/L=41  WR=25.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=asia

### L22.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=96  W=25/L=71  WR=26.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=96  W=25/L=71  WR=26.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L23.  `T1=T1c AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=96  W=36/L=60  WR=37.5%
- Sharpen: sharpest is session_bucket=london_open (15/60 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L24.  `T1=T1c AND BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=96  W=36/L=60  WR=37.5%
- Sharpen: sharpest is session_bucket=london_open (15/60 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L25.  `H20=H20c AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is BBP=BBP2 (20/57 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(12/6) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
