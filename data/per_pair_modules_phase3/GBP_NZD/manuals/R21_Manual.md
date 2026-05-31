# GBP_NZD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,948**  (W=4,102 / L=2,846)  -  WR: **59.0%**

## Session distribution

- asia: n=2136  W=1287/L=849  WR=60.3%
- london_open: n=1328  W=759/L=569  WR=57.2%
- ny_mid: n=868  W=510/L=358  WR=58.8%
- ny_open: n=771  W=437/L=334  WR=56.7%
- london: n=532  W=313/L=219  WR=58.8%
- ny_close: n=510  W=329/L=181  WR=64.5%
- asia_late: n=438  W=265/L=173  WR=60.5%
- off_hours: n=365  W=202/L=163  WR=55.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI1`
- Raw: n=147  W=127/L=20  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 9/20 losers (45%)
- **Final: n=128  W=117/L=11  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_open

### W02.  `H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=133  W=122/L=11  WR=91.7%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=113  W=107/L=6  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W03.  `H20=H20b AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude ZS=ZS3 drops 15/18 losers (83%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W04.  `H20=H20b AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude ZS=ZS3 drops 15/18 losers (83%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=119  W=110/L=9  WR=92.4%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W06.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=119  W=110/L=9  WR=92.4%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W07.  `H60=H60e AND T1=T1a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP2 drops 13/15 losers (87%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when lower third

### W08.  `H60=H60e AND T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP2 drops 13/15 losers (87%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when lower third

### W09.  `H60=H60e AND RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP2 drops 13/15 losers (87%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 20-30 oversold; session=london_open  •  AVOID when lower third

### W10.  `H20=H20b AND H60=H60a AND ZS=ZS2`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude session_bucket=london_open drops 12/16 losers (75%)
- **Final: n=86  W=82/L=4  WR=95.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W11.  `H20=H20b AND H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude session_bucket=london_open drops 12/16 losers (75%)
- **Final: n=86  W=82/L=4  WR=95.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W12.  `H20=H20b AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude ZS=ZS3 drops 11/14 losers (79%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20b AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude ZS=ZS3 drops 11/14 losers (79%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude ZS=ZS3 drops 7/13 losers (54%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W15.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude ZS=ZS3 drops 7/13 losers (54%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude ZS=ZS3 drops 7/13 losers (54%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20b AND H60=H60a AND T1=T1c AND ZS=ZS2`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W18.  `H20=H20b AND H60=H60a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W19.  `T1=T1c AND RSI=RSI2 AND ZS=ZS3 AND session_bucket=ny_open`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude H20=H20e drops 8/12 losers (67%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral; session=ny_open  •  AVOID when HTF20 strongly against

### W20.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude H20=H20e drops 8/12 losers (67%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -1 to +1 neutral; session=ny_open  •  AVOID when HTF20 strongly against

### W21.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W23.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=london_open drops 4/6 losers (67%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W24.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=london_open drops 4/6 losers (67%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W25.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=london_open drops 4/6 losers (67%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND RSI=RSI1`
- Raw: n=419  W=145/L=274  WR=34.6%
- Sharpen: sharpest is H60=H60a (119/274 of losers there)
- **Sharp: n=156  W=37/L=119  WR=23.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF60 aligned WITH trade

### L02.  `H20=H20e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=419  W=145/L=274  WR=34.6%
- Sharpen: sharpest is H60=H60a (119/274 of losers there)
- **Sharp: n=156  W=37/L=119  WR=23.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold  •  ONLY when HTF60 aligned WITH trade

### L03.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=419  W=145/L=274  WR=34.6%
- Sharpen: sharpest is H60=H60a (119/274 of losers there)
- **Sharp: n=156  W=37/L=119  WR=23.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF60 aligned WITH trade

### L04.  `H20=H20e AND T4=T4c AND RSI=RSI1`
- Raw: n=384  W=132/L=252  WR=34.4%
- Sharpen: sharpest is H60=H60a (97/252 of losers there)
- **Sharp: n=121  W=24/L=97  WR=19.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF60 aligned WITH trade

### L05.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=384  W=132/L=252  WR=34.4%
- Sharpen: sharpest is H60=H60a (97/252 of losers there)
- **Sharp: n=121  W=24/L=97  WR=19.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF60 aligned WITH trade

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=384  W=132/L=252  WR=34.4%
- Sharpen: sharpest is H60=H60a (97/252 of losers there)
- **Sharp: n=121  W=24/L=97  WR=19.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF60 aligned WITH trade

### L07.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=262  W=95/L=167  WR=36.3%
- Sharpen: sharpest is ZS=ZS2 (46/167 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L08.  `H20=H20e AND H60=H60e AND ZS=ZS1`
- Raw: n=262  W=98/L=164  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=262  W=98/L=164  WR=37.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold

### L09.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=255  W=96/L=159  WR=37.6%
- Sharpen: sharpest is H20=H20e (119/159 of losers there)
- **Sharp: n=156  W=37/L=119  WR=23.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L10.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=255  W=96/L=159  WR=37.6%
- Sharpen: sharpest is H20=H20e (119/159 of losers there)
- **Sharp: n=156  W=37/L=119  WR=23.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L11.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=255  W=96/L=159  WR=37.6%
- Sharpen: sharpest is H20=H20e (119/159 of losers there)
- **Sharp: n=156  W=37/L=119  WR=23.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=244  W=95/L=149  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=244  W=95/L=149  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold

### L13.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=244  W=95/L=149  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=244  W=95/L=149  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold

### L14.  `H20=H20e AND H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=244  W=95/L=149  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=244  W=95/L=149  WR=38.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold

### L15.  `H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=224  W=88/L=136  WR=39.3%
- Sharpen: sharpest is session_bucket=asia_late (46/136 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia_late

### L16.  `H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=224  W=88/L=136  WR=39.3%
- Sharpen: sharpest is session_bucket=asia_late (46/136 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold  •  ONLY when session=asia_late

### L17.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=224  W=88/L=136  WR=39.3%
- Sharpen: sharpest is session_bucket=asia_late (46/136 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia_late

### L18.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=224  W=88/L=136  WR=39.3%
- Sharpen: sharpest is session_bucket=asia_late (46/136 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia_late

### L19.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=224  W=88/L=136  WR=39.3%
- Sharpen: sharpest is session_bucket=asia_late (46/136 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia_late

### L20.  `H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=222  W=87/L=135  WR=39.2%
- Sharpen: sharpest is RSI=RSI1 (62/135 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 20-30 oversold

### L21.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=222  W=88/L=134  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=222  W=88/L=134  WR=39.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia

### L22.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=222  W=88/L=134  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=222  W=88/L=134  WR=39.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia

### L23.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=222  W=88/L=134  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=222  W=88/L=134  WR=39.6%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia

### L24.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=222  W=88/L=134  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=222  W=88/L=134  WR=39.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia

### L25.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=222  W=88/L=134  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=222  W=88/L=134  WR=39.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(32/38) |
| H60 | — | H60e(34/40) |
| T1 | — | — |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
