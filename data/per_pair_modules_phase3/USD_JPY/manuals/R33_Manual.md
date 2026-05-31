# USD_JPY — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,058**  (W=1,767 / L=1,291)  -  WR: **57.8%**

## Session distribution

- asia: n=896  W=541/L=355  WR=60.4%
- ny_mid: n=566  W=319/L=247  WR=56.4%
- ny_close: n=481  W=295/L=186  WR=61.3%
- ny_open: n=387  W=215/L=172  WR=55.6%
- london_open: n=364  W=204/L=160  WR=56.0%
- london: n=174  W=103/L=71  WR=59.2%
- asia_late: n=138  W=59/L=79  WR=42.8%
- off_hours: n=52  W=31/L=21  WR=59.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude RSI=RSI3 drops 4/6 losers (67%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W02.  `H60=H60a AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 6/10 losers (60%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W03.  `H60=H60a AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 6/10 losers (60%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W04.  `H60=H60a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 6/10 losers (60%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W05.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=71  W=71/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 30-40 weak

### W06.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude direction_exec=short drops 6/6 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when short

### W07.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=66  W=61/L=5  WR=92.4%
- Refine: exclude direction_exec=short drops 5/5 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when short

### W08.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=65  W=65/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak

### W09.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude RSI=RSI3 drops 4/6 losers (67%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W10.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude RSI=RSI3 drops 4/6 losers (67%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W11.  `H20=H20a AND T4=T4c AND ZS=ZS4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W12.  `H20=H20a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W13.  `H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W14.  `H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W15.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W16.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W17.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W18.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W19.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W20.  `H20=H20a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W21.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W22.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W23.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W24.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W25.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is H60=H60e (60/70 of losers there)
- **Sharp: n=79  W=19/L=60  WR=24.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_mid  •  ONLY when HTF60 strongly against

### L02.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (50/69 of losers there)
- **Sharp: n=74  W=24/L=50  WR=32.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L03.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=95  W=20/L=75  WR=21.1%
- Sharpen: sharpest is RSI=RSI2 (40/75 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L04.  `H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: sharpest is RSI=RSI3 (25/67 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L05.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: sharpest is RSI=RSI3 (25/67 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L06.  `H60=H60c AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is H20=H20a (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L07.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=87  W=20/L=67  WR=23.0%
- Sharpen: sharpest is RSI=RSI2 (39/67 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L08.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is H60=H60c (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF60 neutral

### L09.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is H60=H60c (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF60 neutral

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is session_bucket=ny_mid (11/56 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L11.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is H60=H60c (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF60 neutral

### L12.  `T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=84  W=27/L=57  WR=32.1%
- Sharpen: sharpest is H60=H60c (29/57 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L13.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=84  W=27/L=57  WR=32.1%
- Sharpen: sharpest is H60=H60c (29/57 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=83  W=29/L=54  WR=34.9%
- Sharpen: sharpest is session_bucket=ny_mid (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L15.  `T1=T1c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L16.  `T4=T4c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L17.  `ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L19.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L20.  `T1=T1c AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L21.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L22.  `T4=T4c AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L23.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF20 strongly against

### L24.  `T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=82  W=20/L=62  WR=24.4%
- Sharpen: sharpest is RSI=RSI2 (34/62 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L25.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=82  W=20/L=62  WR=24.4%
- Sharpen: sharpest is RSI=RSI2 (34/62 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(34/27) | H60c(35/41) |
| T1 | — | — |
| T4 | T4c(55/48) | T4a(45/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/48) | short(45/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
