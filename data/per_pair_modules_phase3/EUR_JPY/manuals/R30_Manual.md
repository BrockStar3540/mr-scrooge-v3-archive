# EUR_JPY — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,736**  (W=1,613 / L=1,123)  -  WR: **59.0%**

## Session distribution

- ny_mid: n=1247  W=748/L=499  WR=60.0%
- asia: n=748  W=431/L=317  WR=57.6%
- london_open: n=380  W=238/L=142  WR=62.6%
- ny_open: n=156  W=86/L=70  WR=55.1%
- london: n=68  W=38/L=30  WR=55.9%
- ny_close: n=51  W=32/L=19  WR=62.7%
- off_hours: n=50  W=27/L=23  WR=54.0%
- asia_late: n=36  W=13/L=23  WR=36.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude T1=T1c drops 17/17 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H60=H60b drops 9/14 losers (64%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF60 slightly aligned

### W03.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude H60=H60b drops 9/12 losers (75%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W04.  `H20=H20d AND H60=H60e AND RSI=RSI4`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when upper third

### W05.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude BBP=BBP2 drops 4/9 losers (44%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when lower third

### W06.  `H20=H20d AND H60=H60e AND T4=T4c AND RSI=RSI4`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP4 drops 10/11 losers (91%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W07.  `H20=H20e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude T4=T4a drops 10/11 losers (91%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W08.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude T4=T4a drops 6/7 losers (86%)
- **Final: n=62  W=61/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 4h trend WITH trade

### W09.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude H20=H20d drops 4/8 losers (50%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W10.  `H20=H20e AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=london_open  •  AVOID when HTF60 strongly against

### W11.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20b drops 4/10 losers (40%)
- **Final: n=55  W=49/L=6  WR=89.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 slightly aligned

### W12.  `H20=H20e AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W13.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W14.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W15.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W16.  `H20=H20e AND H60=H60b AND T1=T1a`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=ny_close drops 8/8 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_close

### W17.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 6/9 losers (67%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_open

### W18.  `H20=H20d AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude BBP=BBP4 drops 5/7 losers (71%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF20 mildly against; RSI 50-60 upper neutral; session=asia  •  AVOID when upper third

### W19.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=58  W=53/L=5  WR=91.4%
- Refine: exclude BBP=BBP3 drops 4/5 losers (80%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when middle of band

### W20.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=58  W=53/L=5  WR=91.4%
- Refine: exclude BBP=BBP3 drops 4/5 losers (80%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when middle of band

### W21.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude BBP=BBP5 drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W23.  `H20=H20d AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude BBP=BBP4 drops 5/6 losers (83%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when upper third

### W24.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude RSI=RSI2 drops 6/7 losers (86%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; session=london_open  •  AVOID when RSI 30-40 weak

### W25.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude H20=H20b drops 4/7 losers (57%)
- **Final: n=36  W=33/L=3  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=199  W=74/L=125  WR=37.2%
- Sharpen: sharpest is H60=H60e (110/125 of losers there)
- **Sharp: n=162  W=52/L=110  WR=32.1%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

### L02.  `T1=T1c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=172  W=65/L=107  WR=37.8%
- Sharpen: sharpest is H60=H60e (107/107 of losers there)
- **Sharp: n=159  W=52/L=107  WR=32.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

### L03.  `H20=H20a AND T4=T4a AND BBP=BBP4`
- Raw: n=165  W=66/L=99  WR=40.0%
- Sharpen: sharpest is T1=T1a (55/99 of losers there)
- **Sharp: n=72  W=17/L=55  WR=23.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  ONLY when 1h trend WITH trade

### L04.  `H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is H20=H20b (34/99 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L05.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is H20=H20b (34/99 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L06.  `H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=162  W=52/L=110  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=162  W=52/L=110  WR=32.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia

### L07.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=162  W=52/L=110  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=162  W=52/L=110  WR=32.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia

### L08.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=159  W=52/L=107  WR=32.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=52/L=107  WR=32.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia

### L09.  `T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=157  W=56/L=101  WR=35.7%
- Sharpen: sharpest is T1=T1a (49/101 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: LONG**  •  4h trend WITH trade; upper third  •  ONLY when 1h trend WITH trade

### L10.  `T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=153  W=56/L=97  WR=36.6%
- Sharpen: sharpest is ZS=ZS2 (77/97 of losers there)
- **Sharp: n=108  W=31/L=77  WR=28.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L11.  `H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=150  W=56/L=94  WR=37.3%
- Sharpen: sharpest is T1=T1a (46/94 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  ONLY when 1h trend WITH trade

### L12.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=150  W=56/L=94  WR=37.3%
- Sharpen: sharpest is T1=T1a (46/94 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  ONLY when 1h trend WITH trade

### L13.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is BBP=BBP4 (38/91 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L14.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is ZS=ZS2 (34/85 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -2 to -1 oversold

### L15.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=137  W=47/L=90  WR=34.3%
- Sharpen: sharpest is T4=T4a (66/90 of losers there)
- **Sharp: n=91  W=25/L=66  WR=27.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L16.  `H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is ZS=ZS2 (67/87 of losers there)
- **Sharp: n=92  W=25/L=67  WR=27.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L17.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is ZS=ZS2 (67/87 of losers there)
- **Sharp: n=92  W=25/L=67  WR=27.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L18.  `T1=T1a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=133  W=46/L=87  WR=34.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral

### L19.  `T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=131  W=46/L=85  WR=35.1%
- Sharpen: sharpest is T1=T1a (39/85 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L20.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=131  W=46/L=85  WR=35.1%
- Sharpen: sharpest is T1=T1a (39/85 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L21.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=130  W=44/L=86  WR=33.8%
- Sharpen: sharpest is BBP=BBP4 (38/86 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L22.  `H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is T1=T1a (39/81 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L23.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is T1=T1a (39/81 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L24.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is T1=T1a (39/81 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=126  W=50/L=76  WR=39.7%
- Sharpen: sharpest is T1=T1a (50/76 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60a(36/41) |
| T1 | — | — |
| T4 | T4c(54/48) | T4a(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
