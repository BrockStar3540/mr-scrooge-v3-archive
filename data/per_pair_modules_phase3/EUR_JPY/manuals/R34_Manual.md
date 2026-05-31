# EUR_JPY — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,261**  (W=1,976 / L=1,285)  -  WR: **60.6%**

## Session distribution

- asia: n=1172  W=705/L=467  WR=60.2%
- london_open: n=477  W=291/L=186  WR=61.0%
- ny_mid: n=447  W=282/L=165  WR=63.1%
- ny_open: n=411  W=243/L=168  WR=59.1%
- london: n=281  W=178/L=103  WR=63.3%
- ny_close: n=216  W=125/L=91  WR=57.9%
- asia_late: n=208  W=125/L=83  WR=60.1%
- off_hours: n=49  W=27/L=22  WR=55.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=ny_mid

### W02.  `T4=T4a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=ny_mid

### W03.  `BBP=BBP2 AND RSI=RSI0 AND direction_exec=short`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: SHORT**  •  lower third; RSI<20 extreme oversold  •  AVOID when session=ny_mid

### W04.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=ny_mid

### W05.  `T1=T1a AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=short`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=ny_mid

### W06.  `T4=T4a AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=short`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; RSI<20 extreme oversold  •  AVOID when session=ny_mid

### W07.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 12/15 losers (80%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W08.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 12/15 losers (80%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W09.  `T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W10.  `T1=T1a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W11.  `T4=T4a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W12.  `RSI=RSI0 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: SHORT**  •  RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W13.  `T1=T1a AND T4=T4a AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W14.  `T1=T1a AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W15.  `T1=T1a AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W16.  `T4=T4a AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W17.  `T4=T4a AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W18.  `BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: SHORT**  •  lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W19.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W20.  `T1=T1c AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W21.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60e drops 12/12 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF60 strongly against

### W22.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60e drops 12/12 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  lower third; session=ny_open  •  AVOID when HTF60 strongly against

### W23.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60e drops 12/12 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF60 strongly against

### W24.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H20=H20a drops 5/11 losers (45%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W25.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H20=H20a drops 5/11 losers (45%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=249  W=99/L=150  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=249  W=99/L=150  WR=39.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral

### L02.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=203  W=75/L=128  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=203  W=75/L=128  WR=36.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral

### L03.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=196  W=73/L=123  WR=37.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=196  W=73/L=123  WR=37.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral

### L04.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=196  W=73/L=123  WR=37.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=196  W=73/L=123  WR=37.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (46/90 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=asia

### L06.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (46/90 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=asia

### L07.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (46/90 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=asia

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (46/90 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=asia

### L09.  `T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (32/69 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when upper third

### L10.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is ZS=ZS2 (14/70 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L11.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is ZS=ZS2 (14/70 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L12.  `H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=106  W=34/L=72  WR=32.1%
- Sharpen: sharpest is BBP=BBP1 (38/72 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L13.  `T1=T1a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (23/64 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L14.  `H20=H20b AND H60=H60a AND T1=T1c`
- Raw: n=99  W=29/L=70  WR=29.3%
- Sharpen: sharpest is ZS=ZS1 (40/70 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H20=H20b AND H60=H60a AND T4=T4c`
- Raw: n=99  W=29/L=70  WR=29.3%
- Sharpen: sharpest is ZS=ZS1 (40/70 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H20=H20b AND H60=H60a AND direction_exec=long`
- Raw: n=99  W=29/L=70  WR=29.3%
- Sharpen: sharpest is ZS=ZS1 (40/70 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20b AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=99  W=29/L=70  WR=29.3%
- Sharpen: sharpest is ZS=ZS1 (40/70 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H20=H20b AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=99  W=29/L=70  WR=29.3%
- Sharpen: sharpest is ZS=ZS1 (40/70 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H20=H20b AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=99  W=29/L=70  WR=29.3%
- Sharpen: sharpest is ZS=ZS1 (40/70 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H60=H60a AND T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is H20=H20b (10/62 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 slightly aligned

### L21.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is H20=H20b (10/62 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 slightly aligned

### L22.  `H60=H60a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is H20=H20b (10/62 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 slightly aligned

### L23.  `H20=H20b AND H60=H60a AND RSI=RSI2`
- Raw: n=87  W=23/L=64  WR=26.4%
- Sharpen: sharpest is BBP=BBP2 (20/64 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when lower third

### L24.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=84  W=28/L=56  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (31/56 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=asia

### L25.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=84  W=28/L=56  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (31/56 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/34) | — |
| H60 | — | H60a(35/42) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
