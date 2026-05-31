# NZD_CAD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,282**  (W=1,469 / L=813)  -  WR: **64.4%**

## Session distribution

- asia: n=914  W=595/L=319  WR=65.1%
- ny_close: n=531  W=325/L=206  WR=61.2%
- london: n=219  W=144/L=75  WR=65.8%
- ny_open: n=182  W=118/L=64  WR=64.8%
- asia_late: n=168  W=108/L=60  WR=64.3%
- off_hours: n=127  W=85/L=42  WR=66.9%
- london_open: n=95  W=65/L=30  WR=68.4%
- ny_mid: n=46  W=29/L=17  WR=63.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20b AND H60=H60e AND T4=T4c`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude RSI=RSI4 drops 13/17 losers (76%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W02.  `H20=H20b AND T4=T4c AND direction_exec=short`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude T1=T1c drops 9/14 losers (64%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  AVOID when 1h trend AGAINST trade

### W03.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude ZS=ZS3 drops 6/14 losers (43%)
- **Final: n=84  W=76/L=8  WR=90.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W04.  `H20=H20b AND T1=T1a AND T4=T4c`
- Raw: n=97  W=87/L=10  WR=89.7%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W05.  `H20=H20b AND T4=T4c AND RSI=RSI3`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude BBP=BBP0 drops 4/8 losers (50%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W06.  `T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude ZS=ZS1 drops 5/7 losers (71%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W08.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude ZS=ZS1 drops 5/5 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when HTF20 strongly against

### W10.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=asia drops 9/10 losers (90%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when session=asia

### W11.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W12.  `H60=H60a AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W13.  `H20=H20b AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=70  W=65/L=5  WR=92.9%
- Refine: exclude session_bucket=ny_close drops 4/5 losers (80%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W14.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W15.  `BBP=BBP1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20a drops 4/10 losers (40%)
- **Final: n=50  W=44/L=6  WR=88.0%**
- **Dir: SHORT**  •  just touched lower band; session=asia  •  AVOID when HTF20 aligned WITH trade

### W16.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20a drops 4/10 losers (40%)
- **Final: n=50  W=44/L=6  WR=88.0%**
- **Dir: SHORT**  •  just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W17.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20b AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude T4=T4a drops 6/8 losers (75%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20b AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude T4=T4a drops 6/8 losers (75%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W20.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude H20=H20e drops 5/8 losers (62%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when HTF20 strongly against

### W21.  `H20=H20b AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude T4=T4a drops 6/8 losers (75%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20b AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude session_bucket=ny_open drops 3/4 losers (75%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W23.  `H20=H20b AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude BBP=BBP0 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W24.  `H20=H20b AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude T1=T1c drops 7/8 losers (88%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when 1h trend AGAINST trade

### W25.  `H20=H20b AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude direction_exec=long drops 5/6 losers (83%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when long

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is H20=H20d (21/69 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 mildly against

### L02.  `H20=H20e AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI2 (20/67 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 30-40 weak

### L03.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=36/L=63  WR=36.4%
- Sharpen: sharpest is H60=H60c (16/63 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L04.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is BBP=BBP4 (23/55 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when upper third

### L05.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=31/L=56  WR=35.6%
- Sharpen: sharpest is RSI=RSI3 (35/56 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L06.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=86  W=29/L=57  WR=33.7%
- Sharpen: sharpest is T4=T4a (24/57 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend WITH trade

### L07.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is H20=H20a (22/46 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is H20=H20d (15/52 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 mildly against

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is H60=H60c (13/44 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L10.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is BBP=BBP4 (22/44 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when upper third

### L11.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=70  W=27/L=43  WR=38.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; upper third

### L12.  `H20=H20d AND T4=T4a AND RSI=RSI3`
- Raw: n=69  W=22/L=47  WR=31.9%
- Sharpen: sharpest is H60=H60e (15/47 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L13.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=65  W=23/L=42  WR=35.4%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought

### L14.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is T1=T1c (19/40 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is ZS=ZS5 (10/39 of losers there)
- **Sharp: n=12  W=2/L=10  WR=16.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=57  W=15/L=42  WR=26.3%
- Sharpen: sharpest is H20=H20d (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  ONLY when HTF20 mildly against

### L17.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: sharpest is RSI=RSI2 (10/37 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is H60=H60a (18/36 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L19.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is T4=T4a (23/34 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20e AND H60=H60a AND direction_exec=long`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is T1=T1c (22/33 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when 1h trend AGAINST trade

### L21.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H60=H60a (13/32 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  ONLY when HTF60 aligned WITH trade

### L22.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=52  W=15/L=37  WR=28.8%
- Sharpen: sharpest is H60=H60e (23/37 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london  •  ONLY when HTF60 strongly against

### L23.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: sharpest is session_bucket=ny_close (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L24.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=51  W=17/L=34  WR=33.3%
- Sharpen: sharpest is T1=T1c (20/34 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L25.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=50  W=12/L=38  WR=24.0%
- Sharpen: sharpest is H60=H60a (23/38 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/33), H20b(16/10) | H20e(29/38) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(56/45) | T4a(44/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/44) | long(46/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
