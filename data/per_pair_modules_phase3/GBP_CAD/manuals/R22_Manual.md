# GBP_CAD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,144**  (W=1,790 / L=1,354)  -  WR: **56.9%**

## Session distribution

- ny_mid: n=1412  W=815/L=597  WR=57.7%
- ny_open: n=646  W=387/L=259  WR=59.9%
- london: n=323  W=160/L=163  WR=49.5%
- asia: n=274  W=156/L=118  WR=56.9%
- london_open: n=250  W=146/L=104  WR=58.4%
- ny_close: n=239  W=126/L=113  WR=52.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND H60=H60e AND T1=T1a`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude RSI=RSI4 drops 17/18 losers (94%)
- **Final: n=88  W=87/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W02.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude H20=H20a drops 10/20 losers (50%)
- **Final: n=114  W=104/L=10  WR=91.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `T4=T4a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude H20=H20a drops 9/18 losers (50%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude H20=H20a drops 9/18 losers (50%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude H20=H20a drops 10/17 losers (59%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W06.  `H20=H20c AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=116  W=106/L=10  WR=91.4%
- Refine: exclude session_bucket=london_open drops 9/10 losers (90%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=london_open

### W07.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W08.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude BBP=BBP3 drops 7/13 losers (54%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when middle of band

### W09.  `T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=100  W=94/L=6  WR=94.0%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=80  W=78/L=2  WR=97.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W10.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude H60=H60e drops 8/14 losers (57%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF60 strongly against

### W11.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude H20=H20a drops 7/13 losers (54%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W12.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=93  W=86/L=7  WR=92.5%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W13.  `BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=93  W=86/L=7  WR=92.5%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W14.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W15.  `H20=H20a AND H60=H60c AND T1=T1a`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude direction_exec=long drops 9/11 losers (82%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when long

### W16.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude H20=H20a drops 10/13 losers (77%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when middle of band

### W18.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W19.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H60=H60c drops 7/13 losers (54%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 neutral

### W20.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W21.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W22.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W23.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude H20=H20a drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W24.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude BBP=BBP3 drops 7/10 losers (70%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when middle of band

### W25.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude direction_exec=short drops 5/11 losers (45%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when short

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=213  W=85/L=128  WR=39.9%
- Sharpen: sharpest is T1=T1c (99/128 of losers there)
- **Sharp: n=150  W=51/L=99  WR=34.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L02.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=196  W=70/L=126  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=196  W=70/L=126  WR=35.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid

### L03.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=192  W=75/L=117  WR=39.1%
- Sharpen: sharpest is H20=H20d (44/117 of losers there)
- **Sharp: n=48  W=4/L=44  WR=8.3%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 mildly against

### L04.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=178  W=70/L=108  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_mid (51/108 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L05.  `T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=174  W=67/L=107  WR=38.5%
- Sharpen: sharpest is H20=H20c (37/107 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 neutral

### L06.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=173  W=59/L=114  WR=34.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=173  W=59/L=114  WR=34.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid

### L07.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=157  W=44/L=113  WR=28.0%
- Sharpen: sharpest is H20=H20c (40/113 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L08.  `H20=H20d AND T4=T4a AND RSI=RSI4`
- Raw: n=157  W=59/L=98  WR=37.6%
- Sharpen: sharpest is ZS=ZS3 (32/98 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L09.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is T4=T4c (51/94 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L10.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=152  W=53/L=99  WR=34.9%
- Sharpen: sharpest is H20=H20a (33/99 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L11.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: sharpest is direction_exec=long (46/95 of losers there)
- **Sharp: n=55  W=9/L=46  WR=16.4%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when long

### L12.  `H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=149  W=52/L=97  WR=34.9%
- Sharpen: sharpest is H20=H20d (52/97 of losers there)
- **Sharp: n=70  W=18/L=52  WR=25.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L13.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=148  W=52/L=96  WR=35.1%
- Sharpen: sharpest is H20=H20d (52/96 of losers there)
- **Sharp: n=70  W=18/L=52  WR=25.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L14.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=145  W=56/L=89  WR=38.6%
- Sharpen: sharpest is direction_exec=long (46/89 of losers there)
- **Sharp: n=55  W=9/L=46  WR=16.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when long

### L15.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=144  W=41/L=103  WR=28.5%
- Sharpen: sharpest is BBP=BBP4 (54/103 of losers there)
- **Sharp: n=59  W=5/L=54  WR=8.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when upper third

### L16.  `T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=144  W=57/L=87  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (27/87 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third  •  ONLY when RSI 60-70 strong

### L17.  `H60=H60a AND T1=T1a AND ZS=ZS2`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is T4=T4a (52/86 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L18.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is T4=T4a (52/86 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L19.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=142  W=52/L=90  WR=36.6%
- Sharpen: sharpest is H20=H20c (34/90 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 neutral

### L20.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=141  W=56/L=85  WR=39.7%
- Sharpen: sharpest is ZS=ZS1 (36/85 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H60=H60a AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is T4=T4a (52/86 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L22.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=137  W=48/L=89  WR=35.0%
- Sharpen: sharpest is direction_exec=long (49/89 of losers there)
- **Sharp: n=68  W=19/L=49  WR=27.9%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when long

### L23.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is H20=H20d (59/85 of losers there)
- **Sharp: n=83  W=24/L=59  WR=28.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when HTF20 mildly against

### L24.  `H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (27/83 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

### L25.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (27/83 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(6/11) |
| H60 | — | — |
| T1 | T1a(56/44) | T1c(44/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
