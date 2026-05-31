# AUD_JPY — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,430**  (W=2,678 / L=1,752)  -  WR: **60.5%**

## Session distribution

- asia: n=1390  W=862/L=528  WR=62.0%
- ny_mid: n=1084  W=637/L=447  WR=58.8%
- ny_close: n=605  W=378/L=227  WR=62.5%
- london_open: n=599  W=363/L=236  WR=60.6%
- ny_open: n=251  W=140/L=111  WR=55.8%
- london: n=227  W=127/L=100  WR=55.9%
- asia_late: n=202  W=131/L=71  WR=64.9%
- off_hours: n=72  W=40/L=32  WR=55.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=138  W=118/L=20  WR=85.5%
- Refine: exclude ZS=ZS3 drops 10/20 losers (50%)
- **Final: n=97  W=87/L=10  WR=89.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W02.  `T1=T1a AND RSI=RSI3 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: no further refinement
- **Final: n=129  W=111/L=18  WR=86.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought; session=asia

### W03.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude BBP=BBP1 drops 7/13 losers (54%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when just touched lower band

### W04.  `T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude H60=H60e drops 7/15 losers (47%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W05.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H20=H20a drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W06.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H20=H20a drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H20=H20a drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W08.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude H20=H20a drops 10/12 losers (83%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude H20=H20a drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude H20=H20a drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W12.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W13.  `T1=T1c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W14.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=79  W=74/L=5  WR=93.7%
- Refine: exclude session_bucket=london_open drops 5/5 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W15.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude session_bucket=london_open drops 7/7 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W16.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude session_bucket=london_open drops 7/7 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W17.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude session_bucket=london_open drops 7/7 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W18.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london_open drops 5/5 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W19.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london_open drops 5/5 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W20.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude session_bucket=london_open drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W21.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=london_open drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W22.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=london_open drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W23.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=70  W=65/L=5  WR=92.9%
- Refine: exclude session_bucket=london_open drops 5/5 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W24.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W25.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=65  W=60/L=5  WR=92.3%
- Refine: exclude session_bucket=london_open drops 5/5 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=255  W=94/L=161  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (62/161 of losers there)
- **Sharp: n=81  W=19/L=62  WR=23.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=asia

### L02.  `H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=252  W=94/L=158  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (62/158 of losers there)
- **Sharp: n=81  W=19/L=62  WR=23.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L03.  `T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=252  W=94/L=158  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (62/158 of losers there)
- **Sharp: n=81  W=19/L=62  WR=23.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L04.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=252  W=94/L=158  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (62/158 of losers there)
- **Sharp: n=81  W=19/L=62  WR=23.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI4`
- Raw: n=187  W=72/L=115  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=187  W=72/L=115  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral

### L06.  `H20=H20e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=187  W=72/L=115  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=187  W=72/L=115  WR=38.5%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral

### L07.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=187  W=72/L=115  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=187  W=72/L=115  WR=38.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral

### L08.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=184  W=72/L=112  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=72/L=112  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral

### L09.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=184  W=72/L=112  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=72/L=112  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral

### L10.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=184  W=72/L=112  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=72/L=112  WR=39.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral

### L11.  `H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=139  W=48/L=91  WR=34.5%
- Sharpen: sharpest is session_bucket=asia (55/91 of losers there)
- **Sharp: n=71  W=16/L=55  WR=22.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L12.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=139  W=48/L=91  WR=34.5%
- Sharpen: sharpest is session_bucket=asia (55/91 of losers there)
- **Sharp: n=71  W=16/L=55  WR=22.5%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L13.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=139  W=48/L=91  WR=34.5%
- Sharpen: sharpest is session_bucket=asia (55/91 of losers there)
- **Sharp: n=71  W=16/L=55  WR=22.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L14.  `T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=136  W=48/L=88  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (55/88 of losers there)
- **Sharp: n=71  W=16/L=55  WR=22.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L15.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=136  W=48/L=88  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (55/88 of losers there)
- **Sharp: n=71  W=16/L=55  WR=22.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L16.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=136  W=48/L=88  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (55/88 of losers there)
- **Sharp: n=71  W=16/L=55  WR=22.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L17.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=134  W=52/L=82  WR=38.8%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral

### L18.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=125  W=46/L=79  WR=36.8%
- Sharpen: sharpest is T4=T4a (66/79 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L19.  `H20=H20e AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=125  W=46/L=79  WR=36.8%
- Sharpen: sharpest is T4=T4a (66/79 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=124  W=47/L=77  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L21.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=124  W=47/L=77  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L22.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=119  W=44/L=75  WR=37.0%
- Sharpen: sharpest is H20=H20e (66/75 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF20 strongly against

### L23.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=119  W=44/L=75  WR=37.0%
- Sharpen: sharpest is H20=H20e (66/75 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF20 strongly against

### L24.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=46/L=73  WR=38.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral

### L25.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=46/L=73  WR=38.7%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(53/48) | T4a(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
