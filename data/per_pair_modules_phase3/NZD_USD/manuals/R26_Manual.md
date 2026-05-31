# NZD_USD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,460**  (W=938 / L=522)  -  WR: **64.2%**

## Session distribution

- asia: n=587  W=383/L=204  WR=65.2%
- ny_close: n=387  W=244/L=143  WR=63.0%
- ny_open: n=102  W=64/L=38  WR=62.7%
- ny_mid: n=94  W=62/L=32  WR=66.0%
- london_open: n=90  W=56/L=34  WR=62.2%
- london: n=81  W=52/L=29  WR=64.2%
- off_hours: n=70  W=44/L=26  WR=62.9%
- asia_late: n=49  W=33/L=16  WR=67.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND ZS=ZS1`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude T1=T1a drops 4/10 losers (40%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W02.  `H20=H20e AND H60=H60a AND T4=T4a`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude T1=T1a drops 6/10 losers (60%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when 1h trend WITH trade

### W03.  `H20=H20e AND T4=T4a AND RSI=RSI3`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H60=H60e drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 strongly against

### W04.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H20=H20a drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H20=H20a drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H20=H20a drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W07.  `H20=H20e AND H60=H60a AND T1=T1c AND ZS=ZS1`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W08.  `H20=H20e AND H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W09.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H20=H20a drops 6/10 losers (60%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W10.  `H20=H20e AND T1=T1a AND T4=T4c`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W11.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude session_bucket=ny_close drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W12.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude session_bucket=ny_close drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W13.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude session_bucket=ny_close drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W14.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude session_bucket=ny_close drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W15.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude session_bucket=ny_close drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W16.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude session_bucket=ny_mid drops 4/4 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W17.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude session_bucket=ny_mid drops 4/4 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W18.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude session_bucket=ny_mid drops 4/4 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W19.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude session_bucket=ny_mid drops 4/4 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W20.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude session_bucket=ny_mid drops 4/4 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W21.  `H60=H60a AND T1=T1c AND BBP=BBP1`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band  •  AVOID when HTF20 aligned WITH trade

### W24.  `H60=H60a AND T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND session_bucket=ny_close`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=44/L=67  WR=39.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_close

### L02.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=38/L=62  WR=38.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=ny_close

### L03.  `H20=H20a AND H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=38/L=62  WR=38.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_close

### L04.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=56  W=17/L=39  WR=30.4%
- Sharpen: sharpest is BBP=BBP4 (17/39 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when upper third

### L05.  `H20=H20a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is ZS=ZS0 (12/32 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L06.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is session_bucket=asia (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L07.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is session_bucket=asia (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L08.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is session_bucket=asia (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L09.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is session_bucket=asia (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L10.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is session_bucket=asia (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L11.  `H20=H20e AND H60=H60b AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; session=asia  •  ONLY when RSI 30-40 weak

### L12.  `H60=H60b AND T1=T1c AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 30-40 weak

### L13.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is H20=H20a (22/28 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60b AND T4=T4c AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 30-40 weak

### L15.  `H60=H60b AND direction_exec=long AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: LONG**  •  HTF60 slightly aligned; session=asia  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20e AND H60=H60b AND T1=T1c AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 30-40 weak

### L17.  `H20=H20e AND H60=H60b AND T4=T4c AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20e AND H60=H60b AND direction_exec=long AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; session=asia  •  ONLY when RSI 30-40 weak

### L19.  `H60=H60b AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 30-40 weak

### L20.  `H60=H60b AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 30-40 weak

### L21.  `H60=H60b AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 30-40 weak

### L22.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is H20=H20a (11/27 of losers there)
- **Sharp: n=14  W=3/L=11  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L23.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is H20=H20a (11/27 of losers there)
- **Sharp: n=14  W=3/L=11  WR=21.4%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L24.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=42  W=10/L=32  WR=23.8%
- Sharpen: sharpest is H60=H60a (32/32 of losers there)
- **Sharp: n=34  W=2/L=32  WR=5.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L25.  `H60=H60e AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=40  W=13/L=27  WR=32.5%
- Sharpen: sharpest is session_bucket=london_open (8/27 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 30-40 weak  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(54/44) | H20a(46/56) |
| H60 | H60a(45/36) | H60e(38/45) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
