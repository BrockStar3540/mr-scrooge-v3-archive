# NZD_JPY — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **4,824**  (W=3,019 / L=1,805)  -  WR: **62.6%**

## Session distribution

- asia: n=1886  W=1211/L=675  WR=64.2%
- ny_close: n=808  W=482/L=326  WR=59.7%
- london_open: n=571  W=370/L=201  WR=64.8%
- ny_open: n=478  W=304/L=174  WR=63.6%
- london: n=424  W=261/L=163  WR=61.6%
- ny_mid: n=279  W=169/L=110  WR=60.6%
- off_hours: n=202  W=116/L=86  WR=57.4%
- asia_late: n=176  W=106/L=70  WR=60.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=244  W=215/L=29  WR=88.1%
- Refine: exclude BBP=BBP6 drops 6/29 losers (21%)
- **Final: n=234  W=211/L=23  WR=90.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep above upper band

### W02.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=241  W=206/L=35  WR=85.5%
- Refine: exclude H60=H60d drops 9/35 losers (26%)
- **Final: n=224  W=198/L=26  WR=88.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF60 mildly against

### W03.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=241  W=206/L=35  WR=85.5%
- Refine: exclude H60=H60d drops 9/35 losers (26%)
- **Final: n=224  W=198/L=26  WR=88.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF60 mildly against

### W04.  `H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=218  W=195/L=23  WR=89.4%
- Refine: exclude H20=H20e drops 10/23 losers (43%)
- **Final: n=180  W=167/L=13  WR=92.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W05.  `T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=206  W=179/L=27  WR=86.9%
- Refine: exclude H60=H60e drops 11/27 losers (41%)
- **Final: n=186  W=170/L=16  WR=91.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W06.  `H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude H20=H20e drops 22/28 losers (79%)
- **Final: n=148  W=142/L=6  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W07.  `T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=198  W=171/L=27  WR=86.4%
- Refine: exclude H60=H60e drops 12/27 losers (44%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W08.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=186  W=170/L=16  WR=91.4%
- Refine: exclude H20=H20e drops 10/16 losers (62%)
- **Final: n=148  W=142/L=6  WR=95.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W09.  `H20=H20a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=184  W=165/L=19  WR=89.7%
- Refine: exclude H60=H60e drops 12/19 losers (63%)
- **Final: n=151  W=144/L=7  WR=95.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W10.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude BBP=BBP1 drops 9/23 losers (39%)
- **Final: n=159  W=145/L=14  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  AVOID when just touched lower band

### W11.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude BBP=BBP1 drops 9/23 losers (39%)
- **Final: n=159  W=145/L=14  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when just touched lower band

### W12.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude BBP=BBP1 drops 9/23 losers (39%)
- **Final: n=159  W=145/L=14  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when just touched lower band

### W13.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude BBP=BBP1 drops 9/23 losers (39%)
- **Final: n=159  W=145/L=14  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when just touched lower band

### W14.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude BBP=BBP1 drops 9/23 losers (39%)
- **Final: n=159  W=145/L=14  WR=91.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  AVOID when just touched lower band

### W15.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude BBP=BBP1 drops 9/23 losers (39%)
- **Final: n=159  W=145/L=14  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when just touched lower band

### W16.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude BBP=BBP1 drops 9/23 losers (39%)
- **Final: n=159  W=145/L=14  WR=91.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when just touched lower band

### W17.  `H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=165  W=150/L=15  WR=90.9%
- Refine: exclude H20=H20e drops 10/15 losers (67%)
- **Final: n=127  W=122/L=5  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W18.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=165  W=150/L=15  WR=90.9%
- Refine: exclude H20=H20e drops 10/15 losers (67%)
- **Final: n=127  W=122/L=5  WR=96.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W19.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=160  W=143/L=17  WR=89.4%
- Refine: exclude H60=H60e drops 12/17 losers (71%)
- **Final: n=127  W=122/L=5  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W20.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=160  W=143/L=17  WR=89.4%
- Refine: exclude H60=H60e drops 12/17 losers (71%)
- **Final: n=127  W=122/L=5  WR=96.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W21.  `T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=159  W=138/L=21  WR=86.8%
- Refine: exclude H60=H60e drops 11/21 losers (52%)
- **Final: n=135  W=125/L=10  WR=92.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W22.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H60=H60e drops 11/21 losers (52%)
- **Final: n=135  W=125/L=10  WR=92.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W23.  `H20=H20a AND H60=H60a AND RSI=RSI4`
- Raw: n=151  W=144/L=7  WR=95.4%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=119  W=119/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W24.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=151  W=144/L=7  WR=95.4%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=119  W=119/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20e AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=150  W=135/L=15  WR=90.0%
- Refine: exclude T1=T1b drops 7/15 losers (47%)
- **Final: n=141  W=133/L=8  WR=94.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend flat

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close

### L02.  `H20=H20a AND H60=H60a AND session_bucket=ny_close`
- Raw: n=186  W=71/L=115  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=186  W=71/L=115  WR=38.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close

### L03.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=186  W=71/L=115  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=186  W=71/L=115  WR=38.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close

### L04.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=182  W=66/L=116  WR=36.3%
- Sharpen: sharpest is session_bucket=asia (53/116 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L05.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (56/109 of losers there)
- **Sharp: n=67  W=11/L=56  WR=16.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L06.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (56/109 of losers there)
- **Sharp: n=67  W=11/L=56  WR=16.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L07.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=170  W=57/L=113  WR=33.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=170  W=57/L=113  WR=33.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close

### L08.  `H20=H20a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=158  W=61/L=97  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=158  W=61/L=97  WR=38.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close

### L09.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=158  W=61/L=97  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=158  W=61/L=97  WR=38.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close

### L10.  `H20=H20a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=151  W=57/L=94  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=57/L=94  WR=37.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close

### L11.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=151  W=57/L=94  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=57/L=94  WR=37.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close

### L12.  `T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=146  W=43/L=103  WR=29.5%
- Sharpen: sharpest is H20=H20e (91/103 of losers there)
- **Sharp: n=114  W=23/L=91  WR=20.2%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L13.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=146  W=58/L=88  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=58/L=88  WR=39.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close

### L14.  `H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=145  W=31/L=114  WR=21.4%
- Sharpen: sharpest is session_bucket=asia (55/114 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=asia

### L15.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=144  W=39/L=105  WR=27.1%
- Sharpen: sharpest is T4=T4c (32/105 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=144  W=55/L=89  WR=38.2%
- Sharpen: sharpest is ZS=ZS1 (35/89 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=143  W=54/L=89  WR=37.8%
- Sharpen: sharpest is T1=T1a (53/89 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend WITH trade

### L18.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=137  W=51/L=86  WR=37.2%
- Sharpen: sharpest is ZS=ZS1 (39/86 of losers there)
- **Sharp: n=53  W=14/L=39  WR=26.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=133  W=36/L=97  WR=27.1%
- Sharpen: sharpest is H20=H20e (64/97 of losers there)
- **Sharp: n=68  W=4/L=64  WR=5.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L20.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=133  W=45/L=88  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=133  W=45/L=88  WR=33.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close

### L21.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=133  W=45/L=88  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=133  W=45/L=88  WR=33.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close

### L22.  `H20=H20e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=130  W=27/L=103  WR=20.8%
- Sharpen: sharpest is H60=H60e (82/103 of losers there)
- **Sharp: n=93  W=11/L=82  WR=11.8%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L23.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=129  W=44/L=85  WR=34.1%
- Sharpen: sharpest is ZS=ZS1 (38/85 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=123  W=40/L=83  WR=32.5%
- Sharpen: sharpest is RSI=RSI4 (39/83 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=123  W=40/L=83  WR=32.5%
- Sharpen: sharpest is RSI=RSI4 (39/83 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(53/45) | H60e(45/53) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
