# GBP_NZD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **7,760**  (W=4,451 / L=3,309)  -  WR: **57.4%**

## Session distribution

- asia: n=2572  W=1506/L=1066  WR=58.6%
- ny_close: n=1494  W=899/L=595  WR=60.2%
- ny_mid: n=1404  W=753/L=651  WR=53.6%
- london_open: n=671  W=391/L=280  WR=58.3%
- london: n=629  W=354/L=275  WR=56.3%
- ny_open: n=575  W=322/L=253  WR=56.0%
- off_hours: n=282  W=146/L=136  WR=51.8%
- asia_late: n=133  W=80/L=53  WR=60.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=112  W=99/L=13  WR=88.4%
- Refine: exclude session_bucket=asia drops 10/13 losers (77%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W02.  `H20=H20a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W03.  `H20=H20d AND T1=T1c AND ZS=ZS1`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W04.  `H20=H20d AND ZS=ZS1 AND direction_exec=long`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W05.  `H20=H20d AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W06.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when HTF60 strongly against

### W07.  `H20=H20a AND T1=T1c AND ZS=ZS1`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W08.  `H20=H20a AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W09.  `T4=T4a AND ZS=ZS2 AND direction_exec=short AND session_bucket=london`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude H20=H20d drops 2/13 losers (15%)
- **Final: n=90  W=79/L=11  WR=87.8%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=london  •  AVOID when HTF20 mildly against

### W10.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=ny_close

### W11.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W12.  `H20=H20e AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W13.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H60=H60c drops 6/10 losers (60%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak; session=asia  •  AVOID when HTF60 neutral

### W14.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: no further refinement
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W15.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: no further refinement
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W16.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: no further refinement
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W17.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 2/7 losers (29%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close  •  AVOID when strategy=alpha_pullback_v2

### W18.  `H20=H20a AND H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude T1=T1a drops 3/8 losers (38%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=73  W=67/L=6  WR=91.8%
- Refine: no further refinement
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W20.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=72  W=67/L=5  WR=93.1%
- Refine: exclude BBP=BBP1 drops 5/5 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W21.  `H20=H20a AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=71  W=66/L=5  WR=93.0%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W22.  `H20=H20a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T1=T1a drops 3/8 losers (38%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched lower band  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T1=T1a drops 3/8 losers (38%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W24.  `BBP=BBP3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: LONG**  •  middle of band; session=london_open  •  AVOID when HTF20 mildly against

### W25.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: LONG**  •  middle of band; zscore -1 to +1 neutral; session=london_open  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=475  W=185/L=290  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=475  W=185/L=290  WR=38.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 30-40 weak

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=429  W=159/L=270  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=429  W=159/L=270  WR=37.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold

### L03.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=320  W=126/L=194  WR=39.4%
- Sharpen: sharpest is ZS=ZS2 (154/194 of losers there)
- **Sharp: n=230  W=76/L=154  WR=33.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L04.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=316  W=123/L=193  WR=38.9%
- Sharpen: sharpest is ZS=ZS2 (150/193 of losers there)
- **Sharp: n=224  W=74/L=150  WR=33.0%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L05.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=305  W=122/L=183  WR=40.0%
- Sharpen: sharpest is ZS=ZS2 (144/183 of losers there)
- **Sharp: n=220  W=76/L=144  WR=34.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L06.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=298  W=115/L=183  WR=38.6%
- Sharpen: sharpest is ZS=ZS2 (144/183 of losers there)
- **Sharp: n=214  W=70/L=144  WR=32.7%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L07.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=291  W=115/L=176  WR=39.5%
- Sharpen: sharpest is ZS=ZS2 (134/176 of losers there)
- **Sharp: n=204  W=70/L=134  WR=34.3%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L08.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=237  W=88/L=149  WR=37.1%
- Sharpen: sharpest is H20=H20a (40/149 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=230  W=76/L=154  WR=33.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=230  W=76/L=154  WR=33.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L10.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=230  W=76/L=154  WR=33.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=230  W=76/L=154  WR=33.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L11.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=228  W=84/L=144  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=228  W=84/L=144  WR=36.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L12.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=228  W=84/L=144  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=228  W=84/L=144  WR=36.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L13.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=224  W=74/L=150  WR=33.0%
- Sharpen: sharpest is H20=H20d (27/150 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 mildly against

### L14.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=224  W=74/L=150  WR=33.0%
- Sharpen: sharpest is H20=H20d (27/150 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 mildly against

### L15.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=220  W=76/L=144  WR=34.5%
- Sharpen: sharpest is H20=H20d (26/144 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 mildly against

### L16.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=214  W=70/L=144  WR=32.7%
- Sharpen: sharpest is H20=H20d (27/144 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 mildly against

### L17.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=204  W=70/L=134  WR=34.3%
- Sharpen: sharpest is H20=H20d (26/134 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 mildly against

### L18.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=202  W=75/L=127  WR=37.1%
- Sharpen: sharpest is session_bucket=asia (45/127 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak  •  ONLY when session=asia

### L19.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=199  W=75/L=124  WR=37.7%
- Sharpen: sharpest is T4=T4c (26/124 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=185  W=74/L=111  WR=40.0%
- Sharpen: sharpest is T4=T4c (85/111 of losers there)
- **Sharp: n=113  W=28/L=85  WR=24.8%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=182  W=70/L=112  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_close (44/112 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L22.  `H20=H20a AND T4=T4c AND ZS=ZS2`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is T1=T1a (53/117 of losers there)
- **Sharp: n=62  W=9/L=53  WR=14.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L23.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is T1=T1a (53/117 of losers there)
- **Sharp: n=62  W=9/L=53  WR=14.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L24.  `BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=173  W=59/L=114  WR=34.1%
- Sharpen: sharpest is T4=T4c (26/114 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L25.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=172  W=66/L=106  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (44/106 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(39/44) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
