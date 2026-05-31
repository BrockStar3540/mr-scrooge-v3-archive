# GBP_NZD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,615**  (W=2,089 / L=1,526)  -  WR: **57.8%**

## Session distribution

- asia: n=958  W=553/L=405  WR=57.7%
- london_open: n=866  W=494/L=372  WR=57.0%
- ny_open: n=535  W=320/L=215  WR=59.8%
- ny_mid: n=413  W=227/L=186  WR=55.0%
- london: n=386  W=235/L=151  WR=60.9%
- ny_close: n=259  W=147/L=112  WR=56.8%
- off_hours: n=100  W=57/L=43  WR=57.0%
- asia_late: n=98  W=56/L=42  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude session_bucket=asia drops 17/17 losers (100%)
- **Final: n=82  W=82/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude ZS=ZS2 drops 15/15 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W03.  `H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=100  W=91/L=9  WR=91.0%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=asia

### W04.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=100  W=91/L=9  WR=91.0%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W05.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude session_bucket=asia drops 13/13 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=asia

### W06.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude session_bucket=asia drops 13/13 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W07.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=asia

### W08.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when session=asia

### W09.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=asia

### W10.  `H20=H20a AND H60=H60e AND ZS=ZS1`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude RSI=RSI4 drops 13/13 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when RSI 50-60 upper neutral

### W11.  `H20=H20a AND H60=H60d AND T4=T4a`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude ZS=ZS6 drops 8/12 losers (67%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when zscore >+3 extreme

### W12.  `H20=H20a AND H60=H60d AND T4=T4a AND RSI=RSI4`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude ZS=ZS6 drops 8/12 losers (67%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W13.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=77/L=10  WR=88.5%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 strongly against

### W14.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  AVOID when 4h trend AGAINST trade

### W15.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=asia

### W16.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude BBP=BBP5 drops 8/8 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W17.  `H60=H60c AND T4=T4a AND session_bucket=london_open`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI3 drops 11/11 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W18.  `H60=H60c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI3 drops 11/11 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 neutral; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W19.  `T1=T1a AND T4=T4c AND BBP=BBP0`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when HTF20 strongly against

### W20.  `H60=H60c AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI3 drops 11/11 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W21.  `H20=H20a AND T1=T1a AND ZS=ZS1`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude T4=T4a drops 7/10 losers (70%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20a AND H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS6 drops 8/8 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when zscore >+3 extreme

### W23.  `T1=T1c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=72  W=72/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open

### W24.  `T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=72  W=72/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open

### W25.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=72  W=72/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=277  W=109/L=168  WR=39.4%
- Sharpen: sharpest is H20=H20a (91/168 of losers there)
- **Sharp: n=127  W=36/L=91  WR=28.3%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=221  W=85/L=136  WR=38.5%
- Sharpen: sharpest is H20=H20a (72/136 of losers there)
- **Sharp: n=99  W=27/L=72  WR=27.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=218  W=82/L=136  WR=37.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=218  W=82/L=136  WR=37.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia

### L04.  `T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=197  W=77/L=120  WR=39.1%
- Sharpen: sharpest is ZS=ZS5 (47/120 of losers there)
- **Sharp: n=54  W=7/L=47  WR=13.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=192  W=73/L=119  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (111/119 of losers there)
- **Sharp: n=160  W=49/L=111  WR=30.6%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=185  W=71/L=114  WR=38.4%
- Sharpen: sharpest is H20=H20b (28/114 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 slightly aligned

### L07.  `T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=184  W=62/L=122  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (47/122 of losers there)
- **Sharp: n=54  W=7/L=47  WR=13.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=180  W=69/L=111  WR=38.3%
- Sharpen: sharpest is H20=H20a (63/111 of losers there)
- **Sharp: n=84  W=21/L=63  WR=25.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=174  W=49/L=125  WR=28.2%
- Sharpen: sharpest is H60=H60b (31/125 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L10.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (47/111 of losers there)
- **Sharp: n=54  W=7/L=47  WR=13.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=160  W=49/L=111  WR=30.6%
- Sharpen: sharpest is H60=H60b (31/111 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L12.  `ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=156  W=62/L=94  WR=39.7%
- Sharpen: sharpest is H60=H60b (27/94 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 slightly aligned

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=154  W=56/L=98  WR=36.4%
- Sharpen: sharpest is H60=H60b (49/98 of losers there)
- **Sharp: n=57  W=8/L=49  WR=14.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L14.  `T4=T4a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=153  W=55/L=98  WR=35.9%
- Sharpen: sharpest is H20=H20e (20/98 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when HTF20 strongly against

### L15.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=152  W=58/L=94  WR=38.2%
- Sharpen: sharpest is H60=H60b (27/94 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 slightly aligned

### L16.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is T4=T4a (24/90 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: sharpest is ZS=ZS5 (23/90 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=137  W=50/L=87  WR=36.5%
- Sharpen: sharpest is H20=H20e (20/87 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when HTF20 strongly against

### L19.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=137  W=50/L=87  WR=36.5%
- Sharpen: sharpest is H20=H20e (20/87 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when HTF20 strongly against

### L20.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is direction_exec=short (72/83 of losers there)
- **Sharp: n=102  W=30/L=72  WR=29.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when short

### L21.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=134  W=45/L=89  WR=33.6%
- Sharpen: sharpest is ZS=ZS5 (39/89 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=127  W=36/L=91  WR=28.3%
- Sharpen: sharpest is session_bucket=london_open (14/91 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L23.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is ZS=ZS5 (39/83 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is H20=H20e (20/78 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when HTF20 strongly against

### L25.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is H20=H20e (20/78 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(42/37) | — |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
