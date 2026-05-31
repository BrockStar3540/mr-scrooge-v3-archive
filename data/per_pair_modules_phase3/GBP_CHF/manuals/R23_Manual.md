# GBP_CHF — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,942**  (W=1,221 / L=721)  -  WR: **62.9%**

## Session distribution

- london_open: n=436  W=278/L=158  WR=63.8%
- ny_mid: n=405  W=251/L=154  WR=62.0%
- ny_open: n=310  W=206/L=104  WR=66.5%
- london: n=286  W=179/L=107  WR=62.6%
- asia: n=188  W=119/L=69  WR=63.3%
- ny_close: n=159  W=94/L=65  WR=59.1%
- off_hours: n=90  W=53/L=37  WR=58.9%
- asia_late: n=68  W=41/L=27  WR=60.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude H20=H20e drops 10/14 losers (71%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W02.  `H20=H20a AND H60=H60d AND T4=T4a`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 7/12 losers (58%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when session=ny_mid

### W04.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W05.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=87  W=77/L=10  WR=88.5%
- Refine: exclude RSI=RSI3 drops 9/10 losers (90%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W06.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W07.  `T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when session=london_open

### W08.  `T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when session=london_open

### W09.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W10.  `T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when session=london_open

### W11.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W12.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when session=london_open

### W13.  `H20=H20a AND H60=H60d AND direction_exec=short`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when session=ny_mid

### W14.  `H60=H60e AND T4=T4a AND session_bucket=london`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude H20=H20b drops 11/11 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london  •  AVOID when HTF20 slightly aligned

### W15.  `H20=H20a AND H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W16.  `H20=H20a AND H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when session=ny_mid

### W17.  `H20=H20a AND H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W18.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W19.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20a AND H60=H60d AND T1=T1a AND RSI=RSI2`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W21.  `H20=H20a AND H60=H60d AND T4=T4a AND RSI=RSI2`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W22.  `H20=H20a AND H60=H60d AND RSI=RSI2 AND direction_exec=short`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 30-40 weak  •  AVOID when session=ny_mid

### W23.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=74  W=72/L=2  WR=97.3%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when 1h trend WITH trade

### W24.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude H60=H60b drops 3/7 losers (43%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W25.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude H60=H60b drops 3/7 losers (43%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is H20=H20e (34/72 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20e (35/64 of losers there)
- **Sharp: n=35  W=0/L=35  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L03.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is T4=T4c (53/61 of losers there)
- **Sharp: n=62  W=9/L=53  WR=14.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is T4=T4c (50/58 of losers there)
- **Sharp: n=59  W=9/L=50  WR=15.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L05.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=93  W=32/L=61  WR=34.4%
- Sharpen: sharpest is H20=H20e (33/61 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L06.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=87  W=25/L=62  WR=28.7%
- Sharpen: sharpest is RSI=RSI2 (42/62 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L07.  `H20=H20e AND H60=H60e AND BBP=BBP2`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is T4=T4c (45/52 of losers there)
- **Sharp: n=61  W=16/L=45  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is T1=T1c (50/50 of losers there)
- **Sharp: n=59  W=9/L=50  WR=15.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L09.  `H60=H60e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is H20=H20b (18/45 of losers there)
- **Sharp: n=23  W=5/L=18  WR=21.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L10.  `H20=H20e AND H60=H60e AND ZS=ZS2`
- Raw: n=72  W=24/L=48  WR=33.3%
- Sharpen: sharpest is T4=T4c (43/48 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=72  W=24/L=48  WR=33.3%
- Sharpen: sharpest is T4=T4c (43/48 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L12.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is H60=H60e (15/42 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  ONLY when HTF60 strongly against

### L13.  `H20=H20a AND T1=T1a AND ZS=ZS1`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H60=H60c (22/40 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 neutral

### L14.  `H20=H20b AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is session_bucket=london (20/40 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; zscore -2 to -1 oversold  •  ONLY when session=london

### L15.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=62  W=9/L=53  WR=14.5%
- Sharpen: sharpest is BBP=BBP2 (37/53 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L16.  `H20=H20e AND H60=H60b AND T4=T4c`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is session_bucket=asia_late (9/39 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L17.  `T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (15/39 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 20-30 oversold

### L18.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (15/39 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when RSI 20-30 oversold

### L19.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (15/39 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 20-30 oversold

### L20.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=61  W=16/L=45  WR=26.2%
- Sharpen: sharpest is RSI=RSI2 (35/45 of losers there)
- **Sharp: n=35  W=0/L=35  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L21.  `T1=T1a AND T4=T4c AND RSI=RSI2`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is ZS=ZS2 (24/37 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L22.  `H20=H20a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is H60=H60c (23/39 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 neutral

### L23.  `H20=H20a AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=59  W=21/L=38  WR=35.6%
- Sharpen: sharpest is H60=H60c (22/38 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 neutral

### L24.  `H60=H60e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=58  W=18/L=40  WR=31.0%
- Sharpen: sharpest is BBP=BBP2 (25/40 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=london_open  •  ONLY when lower third

### L25.  `H20=H20e AND H60=H60e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is T4=T4c (35/35 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/31) | H20e(29/36) |
| H60 | H60d(14/8) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
