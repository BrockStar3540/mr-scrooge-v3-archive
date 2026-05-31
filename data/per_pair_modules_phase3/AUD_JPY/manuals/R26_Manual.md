# AUD_JPY — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,218**  (W=2,003 / L=1,215)  -  WR: **62.2%**

## Session distribution

- asia: n=1181  W=738/L=443  WR=62.5%
- ny_open: n=545  W=356/L=189  WR=65.3%
- london: n=362  W=219/L=143  WR=60.5%
- ny_mid: n=323  W=184/L=139  WR=57.0%
- london_open: n=307  W=184/L=123  WR=59.9%
- ny_close: n=277  W=182/L=95  WR=65.7%
- asia_late: n=147  W=88/L=59  WR=59.9%
- off_hours: n=76  W=52/L=24  WR=68.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/18 losers (56%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W02.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/18 losers (56%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W03.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/18 losers (56%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W04.  `T4=T4a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude RSI=RSI3 drops 10/18 losers (56%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; session=asia  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60e AND T4=T4a AND RSI=RSI1`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W06.  `T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W07.  `T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W08.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W09.  `H60=H60e AND T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W10.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W11.  `H20=H20b AND H60=H60e AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  AVOID when zscore -2 to -1 oversold

### W12.  `H20=H20b AND T1=T1a AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W13.  `H20=H20b AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; session=asia  •  AVOID when zscore -2 to -1 oversold

### W14.  `H20=H20b AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W15.  `H20=H20b AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  AVOID when zscore -2 to -1 oversold

### W16.  `H20=H20b AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W17.  `H20=H20e AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude RSI=RSI3 drops 3/8 losers (38%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W18.  `H60=H60e AND ZS=ZS1 AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

### W19.  `T1=T1a AND ZS=ZS1 AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

### W20.  `ZS=ZS1 AND direction_exec=short AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

### W21.  `H60=H60e AND T1=T1a AND ZS=ZS1 AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

### W22.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

### W23.  `H60=H60e AND ZS=ZS1 AND direction_exec=short AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

### W24.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

### W25.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=london`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold

### L02.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold

### L03.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold

### L04.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold

### L05.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold

### L06.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold

### L07.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=223  W=84/L=139  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (32/139 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L08.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=223  W=84/L=139  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (32/139 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L09.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=223  W=84/L=139  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (32/139 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L10.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=223  W=84/L=139  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (32/139 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L11.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=223  W=84/L=139  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (32/139 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L12.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=223  W=84/L=139  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (32/139 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L13.  `H60=H60a AND T4=T4c AND BBP=BBP0`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (75/114 of losers there)
- **Sharp: n=103  W=28/L=75  WR=27.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L14.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (75/114 of losers there)
- **Sharp: n=103  W=28/L=75  WR=27.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L15.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (75/114 of losers there)
- **Sharp: n=103  W=28/L=75  WR=27.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L16.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (75/114 of losers there)
- **Sharp: n=103  W=28/L=75  WR=27.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L17.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (75/114 of losers there)
- **Sharp: n=103  W=28/L=75  WR=27.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L18.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (75/114 of losers there)
- **Sharp: n=103  W=28/L=75  WR=27.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L19.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=152  W=58/L=94  WR=38.2%
- Sharpen: sharpest is T4=T4c (54/94 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L20.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=152  W=58/L=94  WR=38.2%
- Sharpen: sharpest is T4=T4c (54/94 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L21.  `BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=152  W=58/L=94  WR=38.2%
- Sharpen: sharpest is T4=T4c (54/94 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: LONG**  •  deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is T4=T4c (44/90 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is T4=T4c (44/90 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is T4=T4c (44/90 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L25.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=145  W=52/L=93  WR=35.9%
- Sharpen: sharpest is H20=H20e (39/93 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(55/43) | H60a(45/57) |
| T1 | T1a(56/42) | T1c(44/58) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/43) | long(45/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
