# GBP_AUD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **4,366**  (W=2,648 / L=1,718)  -  WR: **60.7%**

## Session distribution

- asia: n=1441  W=875/L=566  WR=60.7%
- london_open: n=810  W=516/L=294  WR=63.7%
- ny_open: n=617  W=362/L=255  WR=58.7%
- ny_mid: n=538  W=321/L=217  WR=59.7%
- london: n=404  W=241/L=163  WR=59.7%
- ny_close: n=380  W=228/L=152  WR=60.0%
- off_hours: n=120  W=73/L=47  WR=60.8%
- asia_late: n=56  W=32/L=24  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 10/18 losers (56%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W02.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=london`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude BBP=BBP4 drops 13/17 losers (76%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=london  •  AVOID when upper third

### W03.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude BBP=BBP4 drops 13/17 losers (76%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london  •  AVOID when upper third

### W04.  `H20=H20a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=114  W=101/L=13  WR=88.6%
- Refine: exclude T4=T4c drops 12/13 losers (92%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; session=asia  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20e AND T1=T1a AND session_bucket=london`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude ZS=ZS4 drops 11/15 losers (73%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude ZS=ZS4 drops 11/15 losers (73%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W07.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude ZS=ZS4 drops 11/15 losers (73%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude ZS=ZS4 drops 11/15 losers (73%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W09.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude BBP=BBP4 drops 11/15 losers (73%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  AVOID when upper third

### W10.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude ZS=ZS4 drops 9/13 losers (69%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W11.  `T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=87  W=85/L=2  WR=97.7%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; session=asia  •  AVOID when HTF20 strongly against

### W12.  `H20=H20a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude T4=T4c drops 12/13 losers (92%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W13.  `H20=H20c AND T4=T4a AND ZS=ZS3`
- Raw: n=92  W=86/L=6  WR=93.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when 1h trend AGAINST trade

### W14.  `H20=H20c AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=92  W=86/L=6  WR=93.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=86  W=85/L=1  WR=98.8%
- Refine: no further refinement
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; session=asia

### W16.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 strongly against

### W17.  `H60=H60a AND T1=T1c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when 4h trend AGAINST trade

### W18.  `T1=T1c AND BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20c AND H60=H60e AND ZS=ZS3`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  HTF20 neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20c AND H60=H60e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20c AND H60=H60e AND ZS=ZS3 AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W23.  `H20=H20c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  HTF20 neutral; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W24.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude H20=H20e drops 6/8 losers (75%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_open  •  AVOID when HTF20 strongly against

### W25.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude H20=H20e drops 6/8 losers (75%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=ny_open  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=166  W=60/L=106  WR=36.1%
- Sharpen: sharpest is session_bucket=asia (39/106 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=asia

### L02.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=161  W=63/L=98  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (50/98 of losers there)
- **Sharp: n=68  W=18/L=50  WR=26.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L03.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP5`
- Raw: n=156  W=60/L=96  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (49/96 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; just touched upper band  •  ONLY when session=asia

### L04.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP5`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (44/93 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L05.  `H20=H20a AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (44/93 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L06.  `H60=H60e AND T1=T1a AND BBP=BBP6`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (31/92 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L07.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (31/92 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60e AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (31/92 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L09.  `H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=151  W=58/L=93  WR=38.4%
- Sharpen: sharpest is session_bucket=london (20/93 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when session=london

### L10.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=142  W=45/L=97  WR=31.7%
- Sharpen: sharpest is session_bucket=asia (45/97 of losers there)
- **Sharp: n=47  W=2/L=45  WR=4.3%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when session=asia

### L11.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=136  W=43/L=93  WR=31.6%
- Sharpen: sharpest is session_bucket=asia (50/93 of losers there)
- **Sharp: n=52  W=2/L=50  WR=3.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L12.  `T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=136  W=43/L=93  WR=31.6%
- Sharpen: sharpest is session_bucket=asia (50/93 of losers there)
- **Sharp: n=52  W=2/L=50  WR=3.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L13.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=136  W=43/L=93  WR=31.6%
- Sharpen: sharpest is session_bucket=asia (50/93 of losers there)
- **Sharp: n=52  W=2/L=50  WR=3.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L14.  `H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is session_bucket=london (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L15.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is session_bucket=london (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L16.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is session_bucket=london (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L17.  `T1=T1a AND T4=T4c AND BBP=BBP6`
- Raw: n=126  W=41/L=85  WR=32.5%
- Sharpen: sharpest is session_bucket=asia (49/85 of losers there)
- **Sharp: n=51  W=2/L=49  WR=3.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L18.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=121  W=41/L=80  WR=33.9%
- Sharpen: sharpest is session_bucket=asia (35/80 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L19.  `H60=H60e AND T1=T1a AND T4=T4c AND BBP=BBP6`
- Raw: n=116  W=37/L=79  WR=31.9%
- Sharpen: sharpest is session_bucket=asia (43/79 of losers there)
- **Sharp: n=45  W=2/L=43  WR=4.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L20.  `T1=T1a AND T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=116  W=37/L=79  WR=31.9%
- Sharpen: sharpest is session_bucket=asia (43/79 of losers there)
- **Sharp: n=45  W=2/L=43  WR=4.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L21.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is T1=T1c (70/70 of losers there)
- **Sharp: n=85  W=15/L=70  WR=17.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20a AND direction_exec=short AND session_bucket=london`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is T1=T1c (70/70 of losers there)
- **Sharp: n=85  W=15/L=70  WR=17.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is T1=T1c (70/70 of losers there)
- **Sharp: n=85  W=15/L=70  WR=17.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when 1h trend AGAINST trade

### L24.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (35/71 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L25.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (35/71 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
