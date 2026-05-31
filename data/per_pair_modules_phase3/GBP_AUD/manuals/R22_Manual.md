# GBP_AUD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,926**  (W=2,424 / L=1,502)  -  WR: **61.7%**

## Session distribution

- asia: n=1132  W=722/L=410  WR=63.8%
- london_open: n=825  W=508/L=317  WR=61.6%
- ny_mid: n=574  W=354/L=220  WR=61.7%
- ny_open: n=560  W=334/L=226  WR=59.6%
- london: n=307  W=187/L=120  WR=60.9%
- ny_close: n=258  W=166/L=92  WR=64.3%
- asia_late: n=160  W=89/L=71  WR=55.6%
- off_hours: n=110  W=64/L=46  WR=58.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=206  W=179/L=27  WR=86.9%
- Refine: exclude H20=H20a drops 7/27 losers (26%)
- **Final: n=190  W=170/L=20  WR=89.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=206  W=179/L=27  WR=86.9%
- Refine: exclude H20=H20a drops 7/27 losers (26%)
- **Final: n=190  W=170/L=20  WR=89.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=178  W=152/L=26  WR=85.4%
- Refine: exclude H20=H20a drops 7/26 losers (27%)
- **Final: n=162  W=143/L=19  WR=88.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=178  W=152/L=26  WR=85.4%
- Refine: exclude H20=H20a drops 7/26 losers (27%)
- **Final: n=162  W=143/L=19  WR=88.3%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=178  W=152/L=26  WR=85.4%
- Refine: exclude H20=H20a drops 7/26 losers (27%)
- **Final: n=162  W=143/L=19  WR=88.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=160  W=140/L=20  WR=87.5%
- Refine: exclude H20=H20a drops 7/20 losers (35%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W07.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=160  W=140/L=20  WR=87.5%
- Refine: exclude H20=H20a drops 7/20 losers (35%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W08.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=154  W=136/L=18  WR=88.3%
- Refine: exclude H20=H20a drops 7/18 losers (39%)
- **Final: n=138  W=127/L=11  WR=92.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=154  W=136/L=18  WR=88.3%
- Refine: exclude H20=H20a drops 7/18 losers (39%)
- **Final: n=138  W=127/L=11  WR=92.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude H20=H20b drops 17/20 losers (85%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 slightly aligned

### W11.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude H20=H20b drops 17/20 losers (85%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude H20=H20b drops 17/20 losers (85%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 slightly aligned

### W13.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=138  W=125/L=13  WR=90.6%
- Refine: exclude ZS=ZS1 drops 12/13 losers (92%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=138  W=125/L=13  WR=90.6%
- Refine: exclude ZS=ZS1 drops 12/13 losers (92%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -3 to -2 deep oversold

### W15.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=135  W=121/L=14  WR=89.6%
- Refine: exclude ZS=ZS2 drops 5/14 losers (36%)
- **Final: n=129  W=120/L=9  WR=93.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -2 to -1 oversold

### W16.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=131  W=117/L=14  WR=89.3%
- Refine: exclude session_bucket=london_open drops 9/14 losers (64%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W17.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP5 drops 4/15 losers (27%)
- **Final: n=109  W=98/L=11  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when just touched upper band

### W18.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP5 drops 4/15 losers (27%)
- **Final: n=109  W=98/L=11  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when just touched upper band

### W19.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP5 drops 4/15 losers (27%)
- **Final: n=109  W=98/L=11  WR=89.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when just touched upper band

### W20.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=106  W=95/L=11  WR=89.6%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W21.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=106  W=95/L=11  WR=89.6%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W22.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T1=T1c drops 10/13 losers (77%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W23.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T1=T1c drops 10/13 losers (77%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W24.  `T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 strongly against

### W25.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=320  W=128/L=192  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (40/192 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=320  W=128/L=192  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (40/192 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L03.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=207  W=82/L=125  WR=39.6%
- Sharpen: sharpest is ZS=ZS2 (55/125 of losers there)
- **Sharp: n=75  W=20/L=55  WR=26.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L04.  `H20=H20a AND T1=T1c AND BBP=BBP2`
- Raw: n=162  W=64/L=98  WR=39.5%
- Sharpen: sharpest is ZS=ZS2 (86/98 of losers there)
- **Sharp: n=132  W=46/L=86  WR=34.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L05.  `H60=H60e AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=161  W=53/L=108  WR=32.9%
- Sharpen: sharpest is T1=T1c (73/108 of losers there)
- **Sharp: n=95  W=22/L=73  WR=23.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L06.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=161  W=53/L=108  WR=32.9%
- Sharpen: sharpest is T1=T1c (73/108 of losers there)
- **Sharp: n=95  W=22/L=73  WR=23.2%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L07.  `H60=H60e AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=161  W=53/L=108  WR=32.9%
- Sharpen: sharpest is T1=T1c (73/108 of losers there)
- **Sharp: n=95  W=22/L=73  WR=23.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L08.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=160  W=62/L=98  WR=38.8%
- Sharpen: sharpest is ZS=ZS2 (86/98 of losers there)
- **Sharp: n=130  W=44/L=86  WR=33.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L09.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=160  W=62/L=98  WR=38.8%
- Sharpen: sharpest is ZS=ZS2 (86/98 of losers there)
- **Sharp: n=130  W=44/L=86  WR=33.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L10.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is H20=H20e (74/90 of losers there)
- **Sharp: n=101  W=27/L=74  WR=26.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L11.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is H20=H20e (74/90 of losers there)
- **Sharp: n=101  W=27/L=74  WR=26.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND T1=T1c AND BBP=BBP2`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI3 (78/88 of losers there)
- **Sharp: n=110  W=32/L=78  WR=29.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L13.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: sharpest is ZS=ZS3 (21/86 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L14.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: sharpest is ZS=ZS3 (21/86 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L15.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: sharpest is ZS=ZS3 (21/86 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is H20=H20e (71/86 of losers there)
- **Sharp: n=93  W=22/L=71  WR=23.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L17.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is H20=H20e (71/86 of losers there)
- **Sharp: n=93  W=22/L=71  WR=23.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L18.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is RSI=RSI3 (74/84 of losers there)
- **Sharp: n=101  W=27/L=74  WR=26.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is RSI=RSI3 (74/84 of losers there)
- **Sharp: n=101  W=27/L=74  WR=26.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L20.  `H20=H20a AND T1=T1c AND ZS=ZS2`
- Raw: n=132  W=46/L=86  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=132  W=46/L=86  WR=34.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold

### L21.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=132  W=46/L=86  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=132  W=46/L=86  WR=34.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L22.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS2`
- Raw: n=130  W=44/L=86  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=44/L=86  WR=33.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold

### L23.  `H20=H20a AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=130  W=44/L=86  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=44/L=86  WR=33.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold

### L24.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is H60=H60e (66/77 of losers there)
- **Sharp: n=95  W=29/L=66  WR=30.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L25.  `H20=H20e AND T1=T1c AND ZS=ZS2`
- Raw: n=124  W=42/L=82  WR=33.9%
- Sharpen: sharpest is RSI=RSI3 (75/82 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
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
