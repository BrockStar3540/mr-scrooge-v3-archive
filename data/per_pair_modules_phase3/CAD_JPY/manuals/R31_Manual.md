# CAD_JPY — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,652**  (W=1,665 / L=987)  -  WR: **62.8%**

## Session distribution

- asia: n=1027  W=660/L=367  WR=64.3%
- ny_close: n=504  W=302/L=202  WR=59.9%
- ny_open: n=281  W=178/L=103  WR=63.3%
- london: n=226  W=140/L=86  WR=61.9%
- london_open: n=198  W=124/L=74  WR=62.6%
- ny_mid: n=192  W=121/L=71  WR=63.0%
- off_hours: n=137  W=83/L=54  WR=60.6%
- asia_late: n=87  W=57/L=30  WR=65.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=283  W=242/L=41  WR=85.5%
- Refine: exclude ZS=ZS4 drops 11/41 losers (27%)
- **Final: n=250  W=220/L=30  WR=88.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W02.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=242  W=207/L=35  WR=85.5%
- Refine: exclude RSI=RSI4 drops 10/35 losers (29%)
- **Final: n=210  W=185/L=25  WR=88.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W03.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=235  W=200/L=35  WR=85.1%
- Refine: exclude RSI=RSI4 drops 10/35 losers (29%)
- **Final: n=203  W=178/L=25  WR=87.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W04.  `H20=H20e AND H60=H60a AND session_bucket=asia`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude RSI=RSI3 drops 22/23 losers (96%)
- **Final: n=106  W=105/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W05.  `H20=H20e AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude RSI=RSI3 drops 22/23 losers (96%)
- **Final: n=106  W=105/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W06.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude H20=H20b drops 5/21 losers (24%)
- **Final: n=135  W=119/L=16  WR=88.1%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W07.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=136  W=122/L=14  WR=89.7%
- Refine: exclude session_bucket=ny_mid drops 8/14 losers (57%)
- **Final: n=119  W=113/L=6  WR=95.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W08.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=126  W=113/L=13  WR=89.7%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=122  W=113/L=9  WR=92.6%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W09.  `T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude T4=T4a drops 10/18 losers (56%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=114  W=103/L=11  WR=90.4%
- Refine: exclude RSI=RSI3 drops 10/11 losers (91%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W11.  `H60=H60e AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude H20=H20a drops 7/16 losers (44%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W12.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI3 drops 10/11 losers (91%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W13.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude RSI=RSI3 drops 13/13 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; session=asia  •  AVOID when RSI 40-50 lower neutral

### W14.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=106  W=97/L=9  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W15.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude T1=T1a drops 13/15 losers (87%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W16.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude T1=T1c drops 10/15 losers (67%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when 1h trend AGAINST trade

### W17.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude H20=H20a drops 10/15 losers (67%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W18.  `T1=T1a AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI3 drops 11/11 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W19.  `H20=H20e AND T1=T1a AND BBP=BBP0`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude session_bucket=ny_mid drops 4/12 losers (33%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W20.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude T1=T1a drops 13/15 losers (87%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W21.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=charlie_pullback_continuation_v2

### W23.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude T4=T4a drops 8/14 losers (57%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W24.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude T1=T1c drops 5/12 losers (42%)
- **Final: n=78  W=71/L=7  WR=91.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  AVOID when 1h trend AGAINST trade

### W25.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude T4=T4b drops 2/9 losers (22%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; session=asia  •  AVOID when 4h trend flat

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=212  W=78/L=134  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=212  W=78/L=134  WR=36.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia

### L02.  `H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=187  W=72/L=115  WR=38.5%
- Sharpen: sharpest is T4=T4c (95/115 of losers there)
- **Sharp: n=141  W=46/L=95  WR=32.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when 4h trend AGAINST trade

### L03.  `T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=187  W=72/L=115  WR=38.5%
- Sharpen: sharpest is T4=T4c (95/115 of losers there)
- **Sharp: n=141  W=46/L=95  WR=32.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=187  W=72/L=115  WR=38.5%
- Sharpen: sharpest is T4=T4c (95/115 of losers there)
- **Sharp: n=141  W=46/L=95  WR=32.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when 4h trend AGAINST trade

### L05.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=183  W=67/L=116  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=183  W=67/L=116  WR=36.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia

### L06.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: sharpest is T4=T4c (90/108 of losers there)
- **Sharp: n=135  W=45/L=90  WR=33.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L07.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: sharpest is T4=T4c (90/108 of losers there)
- **Sharp: n=135  W=45/L=90  WR=33.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L08.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=175  W=67/L=108  WR=38.3%
- Sharpen: sharpest is BBP=BBP0 (24/108 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when deep below lower band

### L09.  `H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is T4=T4c (88/106 of losers there)
- **Sharp: n=127  W=39/L=88  WR=30.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L10.  `T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is T4=T4c (88/106 of losers there)
- **Sharp: n=127  W=39/L=88  WR=30.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is T4=T4c (88/106 of losers there)
- **Sharp: n=127  W=39/L=88  WR=30.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is T4=T4c (88/106 of losers there)
- **Sharp: n=127  W=39/L=88  WR=30.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is T4=T4c (88/106 of losers there)
- **Sharp: n=127  W=39/L=88  WR=30.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L14.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=167  W=66/L=101  WR=39.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia

### L15.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=165  W=63/L=102  WR=38.2%
- Sharpen: sharpest is H60=H60e (88/102 of losers there)
- **Sharp: n=127  W=39/L=88  WR=30.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L16.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=165  W=63/L=102  WR=38.2%
- Sharpen: sharpest is H60=H60e (88/102 of losers there)
- **Sharp: n=127  W=39/L=88  WR=30.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=164  W=63/L=101  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=63/L=101  WR=38.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold

### L18.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=156  W=57/L=99  WR=36.5%
- Sharpen: sharpest is T4=T4c (83/99 of losers there)
- **Sharp: n=121  W=38/L=83  WR=31.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L19.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=156  W=57/L=99  WR=36.5%
- Sharpen: sharpest is T4=T4c (83/99 of losers there)
- **Sharp: n=121  W=38/L=83  WR=31.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=151  W=55/L=96  WR=36.4%
- Sharpen: sharpest is T4=T4a (40/96 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L21.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=151  W=55/L=96  WR=36.4%
- Sharpen: sharpest is T4=T4a (40/96 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L22.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=151  W=55/L=96  WR=36.4%
- Sharpen: sharpest is T4=T4a (40/96 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L23.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=146  W=55/L=91  WR=37.7%
- Sharpen: sharpest is H60=H60e (83/91 of losers there)
- **Sharp: n=121  W=38/L=83  WR=31.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L24.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=144  W=55/L=89  WR=38.2%
- Sharpen: sharpest is ZS=ZS1 (37/89 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=141  W=46/L=95  WR=32.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=141  W=46/L=95  WR=32.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(46/38) | H20a(38/45) |
| H60 | H60a(52/45) | H60e(45/51) |
| T1 | T1a(59/40) | T1c(41/60) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/47) | short(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
