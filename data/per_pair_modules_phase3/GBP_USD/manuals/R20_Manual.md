# GBP_USD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,139**  (W=1,916 / L=1,223)  -  WR: **61.0%**

## Session distribution

- ny_mid: n=1089  W=662/L=427  WR=60.8%
- london_open: n=694  W=435/L=259  WR=62.7%
- ny_open: n=497  W=302/L=195  WR=60.8%
- ny_close: n=458  W=274/L=184  WR=59.8%
- london: n=229  W=141/L=88  WR=61.6%
- asia: n=136  W=79/L=57  WR=58.1%
- off_hours: n=24  W=15/L=9  WR=62.5%
- asia_late: n=12  W=8/L=4  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W02.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W03.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude session_bucket=london drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W04.  `H60=H60e AND T4=T4a AND BBP=BBP0`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude RSI=RSI2 drops 10/12 losers (83%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W05.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude ZS=ZS4 drops 9/12 losers (75%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched lower band

### W07.  `T4=T4a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=ny_open drops 10/12 losers (83%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band  •  AVOID when session=ny_open

### W08.  `T1=T1c AND T4=T4a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=ny_open drops 10/12 losers (83%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=ny_open

### W09.  `H60=H60e AND T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=72  W=70/L=2  WR=97.2%
- Refine: exclude session_bucket=ny_mid drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W10.  `T1=T1c AND T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude BBP=BBP5 drops 6/7 losers (86%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W12.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude session_bucket=london drops 7/8 losers (88%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=london

### W13.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude session_bucket=london drops 7/8 losers (88%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W14.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude session_bucket=ny_open drops 2/4 losers (50%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W15.  `T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude H20=H20d drops 6/7 losers (86%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band  •  AVOID when HTF20 mildly against

### W16.  `T1=T1c AND T4=T4a AND ZS=ZS0`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore <-3 extreme  •  AVOID when session=ny_open

### W17.  `T4=T4a AND ZS=ZS0 AND direction_exec=long`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore <-3 extreme  •  AVOID when session=ny_open

### W18.  `T1=T1c AND T4=T4a AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_open

### W19.  `T1=T1c AND T4=T4a AND ZS=ZS0 AND direction_exec=long`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore <-3 extreme  •  AVOID when session=ny_open

### W20.  `T4=T4a AND BBP=BBP0 AND ZS=ZS0 AND direction_exec=long`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_open

### W21.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=63  W=62/L=1  WR=98.4%
- Refine: no further refinement
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought

### W22.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude ZS=ZS1 drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W23.  `H20=H20a AND H60=H60d AND RSI=RSI4`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=london drops 5/9 losers (56%)
- **Final: n=42  W=38/L=4  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 50-60 upper neutral  •  AVOID when session=london

### W24.  `H20=H20a AND T4=T4a AND BBP=BBP0`
- Raw: n=62  W=57/L=5  WR=91.9%
- Refine: exclude ZS=ZS1 drops 5/5 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W25.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude RSI=RSI3 drops 4/7 losers (57%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=96  W=31/L=65  WR=32.3%
- Sharpen: sharpest is H60=H60e (29/65 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L02.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is T4=T4c (34/57 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L03.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H60=H60a (39/58 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L04.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=92  W=33/L=59  WR=35.9%
- Sharpen: sharpest is H60=H60a (43/59 of losers there)
- **Sharp: n=47  W=4/L=43  WR=8.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L05.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=85  W=27/L=58  WR=31.8%
- Sharpen: sharpest is H60=H60e (41/58 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L06.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=84  W=23/L=61  WR=27.4%
- Sharpen: sharpest is T4=T4c (43/61 of losers there)
- **Sharp: n=47  W=4/L=43  WR=8.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L07.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=84  W=27/L=57  WR=32.1%
- Sharpen: sharpest is direction_exec=long (39/57 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when long

### L08.  `H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=83  W=26/L=57  WR=31.3%
- Sharpen: sharpest is RSI=RSI3 (39/57 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L09.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is T4=T4c (34/53 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L10.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4c (41/51 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=82  W=26/L=56  WR=31.7%
- Sharpen: sharpest is RSI=RSI3 (38/56 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L12.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is T1=T1c (41/52 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI4`
- Raw: n=79  W=26/L=53  WR=32.9%
- Sharpen: sharpest is session_bucket=london (18/53 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=london

### L14.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (34/52 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L15.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=77  W=23/L=54  WR=29.9%
- Sharpen: sharpest is RSI=RSI4 (39/54 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is session_bucket=ny_mid (25/49 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  HTF20 strongly against; deep below lower band  •  ONLY when session=ny_mid

### L17.  `T4=T4a AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is direction_exec=short (25/45 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_close  •  ONLY when short

### L18.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is direction_exec=short (25/45 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_close  •  ONLY when short

### L19.  `H20=H20e AND T4=T4a AND BBP=BBP3 AND direction_exec=short`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=74  W=25/L=49  WR=33.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; middle of band

### L20.  `T1=T1c AND T4=T4c AND session_bucket=london`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H20=H20e (27/47 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  ONLY when HTF20 strongly against

### L21.  `T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is H60=H60e (44/50 of losers there)
- **Sharp: n=55  W=11/L=44  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L22.  `H20=H20e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=70  W=23/L=47  WR=32.9%
- Sharpen: sharpest is session_bucket=ny_mid (33/47 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  HTF20 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L23.  `H20=H20a AND T1=T1c AND ZS=ZS5`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is H60=H60e (31/44 of losers there)
- **Sharp: n=44  W=13/L=31  WR=29.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L24.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (20/44 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L25.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=69  W=16/L=53  WR=23.2%
- Sharpen: sharpest is RSI=RSI4 (12/53 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/39) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
