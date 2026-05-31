# AUD_USD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,817**  (W=1,840 / L=977)  -  WR: **65.3%**

## Session distribution

- asia: n=915  W=593/L=322  WR=64.8%
- ny_close: n=676  W=451/L=225  WR=66.7%
- ny_open: n=435  W=282/L=153  WR=64.8%
- ny_mid: n=309  W=202/L=107  WR=65.4%
- london: n=202  W=132/L=70  WR=65.3%
- london_open: n=152  W=96/L=56  WR=63.2%
- off_hours: n=68  W=45/L=23  WR=66.2%
- asia_late: n=60  W=39/L=21  WR=65.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude H20=H20a drops 22/25 losers (88%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude BBP=BBP2 drops 16/20 losers (80%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W03.  `RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude BBP=BBP2 drops 16/20 losers (80%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W04.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude BBP=BBP2 drops 16/20 losers (80%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W05.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude BBP=BBP5 drops 17/17 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W06.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude H60=H60a drops 7/11 losers (64%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W07.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W08.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W09.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W10.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude H20=H20e drops 14/15 losers (93%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W11.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude H20=H20e drops 14/15 losers (93%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W12.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude T4=T4a drops 4/8 losers (50%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

### W13.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude T4=T4a drops 4/8 losers (50%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

### W14.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude T4=T4a drops 4/8 losers (50%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

### W15.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 6/15 losers (40%)
- **Final: n=95  W=86/L=9  WR=90.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W16.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W17.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W18.  `T4=T4c AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude H20=H20a drops 8/13 losers (62%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -1 to +1 neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60a AND T1=T1a AND session_bucket=london`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI3 drops 14/14 losers (100%)
- **Final: n=78  W=78/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W20.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI3 drops 14/14 losers (100%)
- **Final: n=78  W=78/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W21.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI3 drops 14/14 losers (100%)
- **Final: n=78  W=78/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W22.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=91  W=87/L=4  WR=95.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/4 losers (50%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W23.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=91  W=87/L=4  WR=95.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/4 losers (50%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W24.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H20=H20e drops 13/13 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=ny_close  •  AVOID when HTF20 strongly against

### W25.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H20=H20e drops 13/13 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=ny_close  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: sharpest is RSI=RSI4 (45/90 of losers there)
- **Sharp: n=56  W=11/L=45  WR=19.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L02.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: sharpest is RSI=RSI4 (45/90 of losers there)
- **Sharp: n=56  W=11/L=45  WR=19.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L03.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: sharpest is RSI=RSI4 (45/90 of losers there)
- **Sharp: n=56  W=11/L=45  WR=19.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L04.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=132  W=49/L=83  WR=37.1%
- Sharpen: sharpest is H20=H20a (42/83 of losers there)
- **Sharp: n=52  W=10/L=42  WR=19.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L05.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=107  W=39/L=68  WR=36.4%
- Sharpen: sharpest is ZS=ZS1 (38/68 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=39/L=68  WR=36.4%
- Sharpen: sharpest is ZS=ZS1 (38/68 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=39/L=68  WR=36.4%
- Sharpen: sharpest is ZS=ZS1 (38/68 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is T1=T1c (62/65 of losers there)
- **Sharp: n=89  W=27/L=62  WR=30.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L09.  `H20=H20a AND H60=H60a AND RSI=RSI3`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is session_bucket=asia (27/64 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L10.  `H20=H20a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is session_bucket=asia (27/64 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L11.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is session_bucket=asia (27/64 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L12.  `T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=97  W=36/L=61  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (25/61 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L13.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is ZS=ZS1 (36/58 of losers there)
- **Sharp: n=50  W=14/L=36  WR=28.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is ZS=ZS1 (36/58 of losers there)
- **Sharp: n=50  W=14/L=36  WR=28.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=90  W=27/L=63  WR=30.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=90  W=27/L=63  WR=30.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open

### L16.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=89  W=27/L=62  WR=30.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=89  W=27/L=62  WR=30.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open

### L17.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is H20=H20a (26/54 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L18.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is ZS=ZS1 (28/55 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is ZS=ZS1 (28/55 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is T1=T1c (49/52 of losers there)
- **Sharp: n=72  W=23/L=49  WR=31.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L21.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is T1=T1c (49/52 of losers there)
- **Sharp: n=72  W=23/L=49  WR=31.9%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is T1=T1c (49/52 of losers there)
- **Sharp: n=72  W=23/L=49  WR=31.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is T1=T1c (48/51 of losers there)
- **Sharp: n=71  W=23/L=48  WR=32.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is T1=T1c (48/51 of losers there)
- **Sharp: n=71  W=23/L=48  WR=32.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L25.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is T1=T1c (28/50 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(52/46) | H60a(48/54) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | T4c(52/46) | T4a(48/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/46) | long(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
