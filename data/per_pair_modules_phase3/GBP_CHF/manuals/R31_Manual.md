# GBP_CHF — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,363**  (W=826 / L=537)  -  WR: **60.6%**

## Session distribution

- ny_close: n=412  W=251/L=161  WR=60.9%
- asia: n=345  W=207/L=138  WR=60.0%
- ny_mid: n=287  W=179/L=108  WR=62.4%
- off_hours: n=140  W=73/L=67  WR=52.1%
- ny_open: n=109  W=72/L=37  WR=66.1%
- london: n=63  W=38/L=25  WR=60.3%
- london_open: n=7  W=6/L=1  WR=85.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=140  W=121/L=19  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 8/19 losers (42%)
- **Final: n=111  W=100/L=11  WR=90.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W02.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W03.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W04.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI2 drops 5/11 losers (45%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W05.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI2 drops 5/11 losers (45%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W06.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI2 drops 5/11 losers (45%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W07.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W08.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_open drops 6/10 losers (60%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W09.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W10.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude H20=H20c drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W11.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude BBP=BBP6 drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when deep above upper band

### W12.  `H20=H20a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude T1=T1a drops 5/8 losers (62%)
- **Final: n=40  W=37/L=3  WR=92.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third  •  AVOID when 1h trend WITH trade

### W13.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP1`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude RSI=RSI2 drops 5/8 losers (62%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 30-40 weak

### W14.  `H60=H60a AND T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude RSI=RSI2 drops 5/8 losers (62%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 30-40 weak

### W15.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude RSI=RSI2 drops 5/8 losers (62%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 30-40 weak

### W16.  `H20=H20c AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude direction_exec=long drops 7/7 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when long

### W17.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude session_bucket=ny_close drops 5/7 losers (71%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=ny_close

### W18.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude session_bucket=ny_close drops 5/8 losers (62%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W19.  `T1=T1a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20c drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched upper band  •  AVOID when HTF20 neutral

### W20.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20c drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W21.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: SHORT**  •  upper third; session=asia  •  AVOID when HTF20 aligned WITH trade

### W22.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=asia

### W23.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W24.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude direction_exec=long drops 4/7 losers (57%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when long

### W25.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=180  W=71/L=109  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (38/109 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when session=asia

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI3`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is T4=T4c (89/92 of losers there)
- **Sharp: n=125  W=36/L=89  WR=28.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L03.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=151  W=54/L=97  WR=35.8%
- Sharpen: sharpest is T1=T1c (85/97 of losers there)
- **Sharp: n=113  W=28/L=85  WR=24.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=151  W=60/L=91  WR=39.7%
- Sharpen: sharpest is ZS=ZS1 (41/91 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=151  W=60/L=91  WR=39.7%
- Sharpen: sharpest is ZS=ZS1 (41/91 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=142  W=47/L=95  WR=33.1%
- Sharpen: sharpest is ZS=ZS1 (41/95 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (41/81 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=129  W=44/L=85  WR=34.1%
- Sharpen: sharpest is T4=T4c (85/85 of losers there)
- **Sharp: n=113  W=28/L=85  WR=24.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=129  W=48/L=81  WR=37.2%
- Sharpen: sharpest is RSI=RSI3 (72/81 of losers there)
- **Sharp: n=95  W=23/L=72  WR=24.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L10.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=125  W=36/L=89  WR=28.8%
- Sharpen: sharpest is ZS=ZS1 (45/89 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=113  W=36/L=77  WR=31.9%
- Sharpen: sharpest is ZS=ZS1 (41/77 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=107  W=39/L=68  WR=36.4%
- Sharpen: sharpest is T4=T4c (68/68 of losers there)
- **Sharp: n=91  W=23/L=68  WR=25.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is H20=H20e (38/66 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=101  W=34/L=67  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (19/67 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=99  W=27/L=72  WR=27.3%
- Sharpen: sharpest is ZS=ZS1 (41/72 of losers there)
- **Sharp: n=43  W=2/L=41  WR=4.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is T4=T4c (41/64 of losers there)
- **Sharp: n=51  W=10/L=41  WR=19.6%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is BBP=BBP2 (25/62 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when lower third

### L18.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is RSI=RSI4 (29/59 of losers there)
- **Sharp: n=42  W=13/L=29  WR=31.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L19.  `H20=H20a AND T1=T1c AND RSI=RSI4`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is ZS=ZS5 (14/60 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is H20=H20e (50/56 of losers there)
- **Sharp: n=64  W=14/L=50  WR=21.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=84  W=30/L=54  WR=35.7%
- Sharpen: sharpest is T4=T4c (41/54 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=81  W=21/L=60  WR=25.9%
- Sharpen: sharpest is H60=H60e (41/60 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L23.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is session_bucket=london (9/51 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london

### L24.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is H20=H20e (49/49 of losers there)
- **Sharp: n=58  W=9/L=49  WR=15.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L25.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is ZS=ZS2 (21/48 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when zscore -2 to -1 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/39) | — |
| H60 | — | — |
| T1 | T1a(60/46) | T1c(40/54) |
| T4 | — | — |
| BBP | BBP2(30/24) | BBP0(9/15) |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/47) | long(45/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
