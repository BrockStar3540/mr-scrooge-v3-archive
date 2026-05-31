# NZD_CAD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,470**  (W=2,212 / L=1,258)  -  WR: **63.7%**

## Session distribution

- asia: n=988  W=635/L=353  WR=64.3%
- ny_mid: n=595  W=376/L=219  WR=63.2%
- london_open: n=589  W=374/L=215  WR=63.5%
- ny_open: n=444  W=282/L=162  WR=63.5%
- ny_close: n=370  W=235/L=135  WR=63.5%
- london: n=211  W=134/L=77  WR=63.5%
- asia_late: n=166  W=109/L=57  WR=65.7%
- off_hours: n=107  W=67/L=40  WR=62.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=142  W=122/L=20  WR=85.9%
- Refine: exclude session_bucket=london_open drops 6/20 losers (30%)
- **Final: n=132  W=118/L=14  WR=89.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W02.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude BBP=BBP0 drops 18/18 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W03.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude H60=H60e drops 13/19 losers (68%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 strongly against

### W04.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=128  W=109/L=19  WR=85.2%
- Refine: exclude T1=T1c drops 12/19 losers (63%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W05.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H60=H60e drops 7/17 losers (41%)
- **Final: n=109  W=99/L=10  WR=90.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W06.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H60=H60e drops 12/14 losers (86%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W07.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W08.  `H20=H20a AND H60=H60b AND T4=T4a`
- Raw: n=109  W=99/L=10  WR=90.8%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20c AND T4=T4a AND RSI=RSI3`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude T1=T1a drops 11/13 losers (85%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W10.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude session_bucket=london_open drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W11.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W12.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=97  W=88/L=9  WR=90.7%
- Refine: exclude H60=H60b drops 6/9 losers (67%)
- **Final: n=91  W=88/L=3  WR=96.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF60 slightly aligned

### W13.  `H20=H20a AND T4=T4a AND BBP=BBP0`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london_open drops 10/13 losers (77%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=london_open

### W14.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude T4=T4c drops 8/14 losers (57%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=92  W=84/L=8  WR=91.3%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=86  W=82/L=4  WR=95.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band  •  AVOID when session=london_open

### W16.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=81  W=72/L=9  WR=88.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP1`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 50-60 upper neutral

### W18.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 50-60 upper neutral

### W19.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude ZS=ZS0 drops 3/12 losers (25%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore <-3 extreme

### W20.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W21.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T1=T1a drops 12/13 losers (92%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 1h trend WITH trade

### W22.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude session_bucket=london_open drops 5/11 losers (45%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W23.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP0 drops 8/12 losers (67%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W24.  `H20=H20a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W25.  `H20=H20a AND T1=T1a AND BBP=BBP0`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=london_open drops 10/12 losers (83%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=202  W=77/L=125  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (52/125 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=168  W=64/L=104  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (39/104 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L03.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: sharpest is H60=H60a (45/93 of losers there)
- **Sharp: n=62  W=17/L=45  WR=27.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L04.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=145  W=56/L=89  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (30/89 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L05.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=138  W=51/L=87  WR=37.0%
- Sharpen: sharpest is H20=H20e (52/87 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L06.  `T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=122  W=47/L=75  WR=38.5%
- Sharpen: sharpest is RSI=RSI3 (68/75 of losers there)
- **Sharp: n=97  W=29/L=68  WR=29.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L07.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=122  W=47/L=75  WR=38.5%
- Sharpen: sharpest is RSI=RSI3 (68/75 of losers there)
- **Sharp: n=97  W=29/L=68  WR=29.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L08.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (24/70 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is ZS=ZS2 (21/73 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is direction_exec=long (49/69 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when long

### L11.  `H20=H20b AND T4=T4c AND direction_exec=long`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (24/70 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  ONLY when session=asia

### L12.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is H20=H20b (11/67 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 slightly aligned

### L13.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=106  W=31/L=75  WR=29.2%
- Sharpen: sharpest is T1=T1c (52/75 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20b AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=105  W=35/L=70  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (24/70 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L15.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is BBP=BBP2 (27/67 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london_open  •  ONLY when lower third

### L16.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=104  W=39/L=65  WR=37.5%
- Sharpen: sharpest is T4=T4c (49/65 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L17.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is direction_exec=short (38/61 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when short

### L18.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=97  W=29/L=68  WR=29.9%
- Sharpen: sharpest is T1=T1c (49/68 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L19.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is H20=H20e (34/58 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 strongly against

### L20.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is H60=H60e (33/67 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L21.  `T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=93  W=35/L=58  WR=37.6%
- Sharpen: sharpest is direction_exec=long (29/58 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=asia  •  ONLY when long

### L22.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is T4=T4c (52/55 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60e AND BBP=BBP3 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (27/54 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: LONG**  •  HTF60 strongly against; middle of band  •  ONLY when session=asia

### L24.  `H60=H60e AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (27/54 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: LONG**  •  HTF60 strongly against; middle of band; zscore -1 to +1 neutral  •  ONLY when session=asia

### L25.  `H20=H20c AND T4=T4c AND RSI=RSI3`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is BBP=BBP0 (16/54 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/31) | H20e(33/41) |
| H60 | H60a(45/39) | H60e(40/46) |
| T1 | T1a(55/47) | T1c(45/52) |
| T4 | T4a(57/42) | T4c(43/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
