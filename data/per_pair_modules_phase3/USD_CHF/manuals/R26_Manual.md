# USD_CHF — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,926**  (W=1,229 / L=697)  -  WR: **63.8%**

## Session distribution

- asia: n=1021  W=665/L=356  WR=65.1%
- ny_close: n=405  W=253/L=152  WR=62.5%
- asia_late: n=141  W=83/L=58  WR=58.9%
- ny_open: n=140  W=87/L=53  WR=62.1%
- off_hours: n=107  W=72/L=35  WR=67.3%
- london_open: n=70  W=46/L=24  WR=65.7%
- london: n=33  W=17/L=16  WR=51.5%
- ny_mid: n=9  W=6/L=3  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 10/12 losers (83%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_close

### W02.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=79  W=77/L=2  WR=97.5%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W03.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H20=H20e drops 9/9 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W04.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude RSI=RSI3 drops 4/10 losers (40%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when RSI 40-50 lower neutral

### W05.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H60=H60d drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 mildly against

### W06.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=69  W=67/L=2  WR=97.1%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W07.  `H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W08.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia

### W09.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude T4=T4c drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

### W10.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=65  W=63/L=2  WR=96.9%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W11.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=65  W=63/L=2  WR=96.9%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W12.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W13.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W14.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W15.  `H20=H20a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 3/8 losers (38%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=alpha_pullback_v2

### W16.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 3/8 losers (38%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=alpha_pullback_v2

### W17.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W18.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude T1=T1c drops 3/5 losers (60%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=24  W=23/L=1  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=asia

### W20.  `H20=H20b AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude BBP=BBP5 drops 2/9 losers (22%)
- **Final: n=59  W=52/L=7  WR=88.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched upper band

### W21.  `H20=H20d AND H60=H60e AND T1=T1a`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20d AND H60=H60e AND direction_exec=short`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against  •  AVOID when RSI 40-50 lower neutral

### W23.  `H20=H20d AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W25.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude H60=H60c drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is T4=T4c (9/42 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L02.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is T4=T4c (36/39 of losers there)
- **Sharp: n=53  W=17/L=36  WR=32.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L03.  `H20=H20a AND T1=T1a AND BBP=BBP0`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is T4=T4c (7/39 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20a AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is T4=T4c (7/39 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is T4=T4c (31/34 of losers there)
- **Sharp: n=45  W=14/L=31  WR=31.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L06.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=54  W=6/L=48  WR=11.1%
- Sharpen: sharpest is H60=H60b (27/48 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 slightly aligned

### L07.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is T4=T4c (20/38 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when 4h trend AGAINST trade

### L08.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is T1=T1a (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when 1h trend WITH trade

### L09.  `H20=H20e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=52  W=17/L=35  WR=32.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia

### L10.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=52  W=17/L=35  WR=32.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=asia

### L11.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=51  W=6/L=45  WR=11.8%
- Sharpen: sharpest is H60=H60b (27/45 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 slightly aligned

### L12.  `H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=50  W=4/L=46  WR=8.0%
- Sharpen: sharpest is BBP=BBP0 (10/46 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L13.  `H20=H20d AND H60=H60c AND T1=T1a`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 1h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L14.  `H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is H20=H20e (28/31 of losers there)
- **Sharp: n=41  W=13/L=28  WR=31.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L15.  `H20=H20d AND H60=H60c AND T1=T1a AND T4=T4a`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L16.  `H20=H20d AND H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 neutral; 1h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L17.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is H20=H20e (28/31 of losers there)
- **Sharp: n=41  W=13/L=28  WR=31.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=48  W=6/L=42  WR=12.5%
- Sharpen: sharpest is H60=H60b (27/42 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 slightly aligned

### L19.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=48  W=6/L=42  WR=12.5%
- Sharpen: sharpest is H60=H60b (27/42 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 slightly aligned

### L20.  `H60=H60e AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is session_bucket=asia_late (7/30 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia_late

### L21.  `H20=H20e AND H60=H60e AND ZS=ZS4`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is T4=T4c (28/29 of losers there)
- **Sharp: n=41  W=13/L=28  WR=31.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is T4=T4c (28/29 of losers there)
- **Sharp: n=41  W=13/L=28  WR=31.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is session_bucket=asia_late (7/29 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia_late

### L24.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is T4=T4c (27/28 of losers there)
- **Sharp: n=40  W=13/L=27  WR=32.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L25.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is T4=T4c (5/28 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/31) | H20e(33/42) |
| H60 | — | — |
| T1 | T1a(50/45) | T1c(50/55) |
| T4 | T4a(52/45) | T4c(48/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
