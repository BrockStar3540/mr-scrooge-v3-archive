# AUD_NZD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,159**  (W=723 / L=436)  -  WR: **62.4%**

## Session distribution

- asia: n=718  W=448/L=270  WR=62.4%
- ny_mid: n=183  W=109/L=74  WR=59.6%
- ny_open: n=126  W=82/L=44  WR=65.1%
- london_open: n=52  W=34/L=18  WR=65.4%
- london: n=43  W=27/L=16  WR=62.8%
- off_hours: n=28  W=18/L=10  WR=64.3%
- asia_late: n=8  W=5/L=3  WR=62.5%
- ny_close: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20b drops 6/13 losers (46%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W02.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20b drops 6/13 losers (46%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W03.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20b drops 6/13 losers (46%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W04.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20b drops 6/13 losers (46%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20b drops 6/13 losers (46%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W06.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20b drops 6/13 losers (46%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W07.  `H60=H60e AND T1=T1a AND ZS=ZS3`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI4 drops 4/13 losers (31%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 50-60 upper neutral

### W08.  `T1=T1a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI4 drops 4/13 losers (31%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 50-60 upper neutral

### W09.  `H60=H60e AND T1=T1a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI4 drops 4/13 losers (31%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 50-60 upper neutral

### W10.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W11.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W12.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W13.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W14.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W15.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W16.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W17.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W18.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W19.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W21.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W22.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W24.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W25.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (29/64 of losers there)
- **Sharp: n=41  W=12/L=29  WR=29.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L02.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_open (13/63 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when session=ny_open

### L03.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_open (13/63 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when session=ny_open

### L04.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (28/55 of losers there)
- **Sharp: n=39  W=11/L=28  WR=28.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L05.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (28/55 of losers there)
- **Sharp: n=39  W=11/L=28  WR=28.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L06.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  ONLY when session=ny_open

### L07.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=ny_open

### L08.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak  •  ONLY when session=ny_open

### L09.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=ny_open

### L10.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  ONLY when session=ny_open

### L11.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=ny_open

### L12.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=79  W=31/L=48  WR=39.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=asia

### L13.  `T4=T4a AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=79  W=31/L=48  WR=39.2%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; session=asia

### L14.  `H60=H60a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is RSI=RSI3 (25/48 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L15.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (13/47 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when session=ny_open

### L16.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L17.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L18.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L19.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L20.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L21.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L22.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L23.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L24.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=74  W=22/L=52  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (9/52 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L25.  `T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is RSI=RSI3 (17/41 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(36/25) | H20a(24/33) |
| H60 | H60e(56/47) | H60a(44/53) |
| T1 | T1a(56/42) | T1c(44/58) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/47) | long(44/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
