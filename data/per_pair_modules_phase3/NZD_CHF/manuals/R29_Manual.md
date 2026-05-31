# NZD_CHF — R29 Manual

## Regime centroid (locked factors)

- **BB = BB0**  (very narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **555**  (W=366 / L=189)  -  WR: **65.9%**

## Session distribution

- asia: n=179  W=120/L=59  WR=67.0%
- ny_close: n=120  W=83/L=37  WR=69.2%
- london_open: n=63  W=42/L=21  WR=66.7%
- london: n=57  W=38/L=19  WR=66.7%
- asia_late: n=46  W=28/L=18  WR=60.9%
- ny_open: n=35  W=24/L=11  WR=68.6%
- off_hours: n=31  W=19/L=12  WR=61.3%
- ny_mid: n=24  W=12/L=12  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude RSI=RSI3 drops 11/13 losers (85%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W02.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude BBP=BBP5 drops 3/10 losers (30%)
- **Final: n=66  W=59/L=7  WR=89.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when just touched upper band

### W03.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude BBP=BBP4 drops 4/9 losers (44%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W04.  `H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=58  W=53/L=5  WR=91.4%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third  •  AVOID when HTF20 strongly against

### W05.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude T4=T4a drops 5/5 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=54  W=50/L=4  WR=92.6%
- Refine: exclude T4=T4a drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W07.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=54  W=50/L=4  WR=92.6%
- Refine: exclude T4=T4a drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude strategy_id=BR2_vcb_short drops 4/6 losers (67%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when strategy=BR2_vcb_short

### W09.  `T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude H60=H60d drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third  •  AVOID when HTF60 mildly against

### W10.  `T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=45  W=41/L=4  WR=91.1%
- Refine: exclude session_bucket=asia drops 2/4 losers (50%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 4/6 losers (67%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W12.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 4/6 losers (67%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W13.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=42  W=38/L=4  WR=90.5%
- Refine: exclude H60=H60e drops 3/4 losers (75%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W14.  `T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude H60=H60d drops 5/6 losers (83%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF60 mildly against

### W15.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude BBP=BBP2 drops 3/6 losers (50%)
- **Final: n=34  W=31/L=3  WR=91.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when lower third

### W16.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude H60=H60d drops 5/6 losers (83%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF60 mildly against

### W17.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; session=asia  •  AVOID when HTF20 strongly against

### W18.  `ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W19.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W20.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=40  W=35/L=5  WR=87.5%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W21.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=39  W=37/L=2  WR=94.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=39  W=36/L=3  WR=92.3%
- Refine: exclude H60=H60a drops 3/3 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W23.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=38  W=35/L=3  WR=92.1%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 2/3 losers (67%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when strategy=TF2_pullback_EMA20_long

### W24.  `H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=38  W=34/L=4  WR=89.5%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W25.  `H60=H60a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=38  W=34/L=4  WR=89.5%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is ZS=ZS1 (15/44 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is ZS=ZS1 (10/45 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is ZS=ZS1 (15/41 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (13/40 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=48  W=15/L=33  WR=31.2%
- Sharpen: sharpest is ZS=ZS1 (11/33 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is ZS=ZS1 (10/30 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is T4=T4a (14/26 of losers there)
- **Sharp: n=20  W=6/L=14  WR=30.0%**
- **Dir: LONG**  •  HTF60 strongly against; upper third  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_open (6/27 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L09.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_open (6/27 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L10.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS1 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS1 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is T4=T4a (11/24 of losers there)
- **Sharp: n=14  W=3/L=11  WR=21.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=36  W=10/L=26  WR=27.8%
- Sharpen: sharpest is BBP=BBP5 (6/26 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when just touched upper band

### L14.  `H20=H20a AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=36  W=10/L=26  WR=27.8%
- Sharpen: sharpest is BBP=BBP5 (6/26 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when just touched upper band

### L15.  `H60=H60e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is T4=T4a (10/22 of losers there)
- **Sharp: n=13  W=3/L=10  WR=23.1%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L16.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is T4=T4a (10/22 of losers there)
- **Sharp: n=13  W=3/L=10  WR=23.1%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L17.  `T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=33  W=13/L=20  WR=39.4%
- Sharpen: sharpest is H60=H60b (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia  •  ONLY when HTF60 slightly aligned

### L18.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=30  W=8/L=22  WR=26.7%
- Sharpen: sharpest is direction_exec=long (19/22 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when long

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(49/29) | H60e(28/49) |
| T1 | T1a(62/42) | T1c(38/58) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(63/40) | long(37/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
