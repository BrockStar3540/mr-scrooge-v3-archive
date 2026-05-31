# USD_CAD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,739**  (W=1,098 / L=641)  -  WR: **63.1%**

## Session distribution

- asia: n=629  W=405/L=224  WR=64.4%
- ny_close: n=563  W=346/L=217  WR=61.5%
- london: n=138  W=86/L=52  WR=62.3%
- london_open: n=127  W=80/L=47  WR=63.0%
- ny_mid: n=102  W=63/L=39  WR=61.8%
- ny_open: n=87  W=60/L=27  WR=69.0%
- off_hours: n=62  W=37/L=25  WR=59.7%
- asia_late: n=31  W=21/L=10  WR=67.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=90/L=11  WR=89.1%
- Refine: exclude H20=H20c drops 10/11 losers (91%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 neutral

### W02.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched upper band

### W03.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude BBP=BBP5 drops 8/10 losers (80%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched upper band

### W04.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_close

### W05.  `T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude BBP=BBP1 drops 7/11 losers (64%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W06.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W07.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W08.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W09.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4a drops 9/12 losers (75%)
- **Final: n=37  W=34/L=3  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W10.  `H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude H60=H60a drops 8/12 losers (67%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W12.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude H60=H60a drops 8/12 losers (67%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W13.  `T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T4=T4a drops 7/10 losers (70%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; upper third  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20d AND T4=T4a AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W15.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H60=H60b drops 3/9 losers (33%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W16.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H60=H60b drops 3/9 losers (33%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W17.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W18.  `H60=H60e AND T1=T1a AND ZS=ZS4`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude T4=T4a drops 4/5 losers (80%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W19.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude T4=T4a drops 4/5 losers (80%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W20.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude BBP=BBP6 drops 3/10 losers (30%)
- **Final: n=68  W=61/L=7  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  AVOID when deep above upper band

### W21.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude BBP=BBP6 drops 3/10 losers (30%)
- **Final: n=68  W=61/L=7  WR=89.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  AVOID when deep above upper band

### W22.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude ZS=ZS3 drops 3/6 losers (50%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W23.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=london

### W24.  `T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude H60=H60b drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W25.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is direction_exec=short (15/46 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=asia  •  ONLY when short

### L02.  `H20=H20a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is RSI=RSI2 (19/45 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is ZS=ZS4 (24/44 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

### L04.  `H20=H20c AND T4=T4c AND RSI=RSI2`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (23/43 of losers there)
- **Sharp: n=33  W=10/L=23  WR=30.3%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L05.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is T1=T1a (19/42 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L06.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is H20=H20e (16/43 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L07.  `T4=T4c AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is BBP=BBP1 (23/38 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_close  •  ONLY when just touched lower band

### L08.  `H20=H20d AND T1=T1c AND direction_exec=short`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is BBP=BBP5 (14/39 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade  •  ONLY when just touched upper band

### L09.  `H20=H20a AND H60=H60a AND session_bucket=ny_close`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is RSI=RSI2 (12/37 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L10.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is RSI=RSI2 (12/37 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L11.  `H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=58  W=16/L=42  WR=27.6%
- Sharpen: sharpest is T4=T4a (25/42 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when 4h trend WITH trade

### L12.  `T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=58  W=18/L=40  WR=31.0%
- Sharpen: sharpest is T1=T1a (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when 1h trend WITH trade

### L13.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (26/36 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L14.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=56  W=17/L=39  WR=30.4%
- Sharpen: sharpest is direction_exec=short (16/39 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when short

### L15.  `T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is direction_exec=short (11/37 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when short

### L16.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is direction_exec=short (11/37 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when short

### L17.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=55  W=18/L=37  WR=32.7%
- Sharpen: sharpest is BBP=BBP3 (9/37 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when middle of band

### L18.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=18/L=37  WR=32.7%
- Sharpen: sharpest is BBP=BBP3 (9/37 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when middle of band

### L19.  `H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=18/L=37  WR=32.7%
- Sharpen: sharpest is BBP=BBP3 (9/37 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london_open  •  ONLY when middle of band

### L20.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=18/L=37  WR=32.7%
- Sharpen: sharpest is BBP=BBP3 (9/37 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when middle of band

### L21.  `H20=H20a AND T4=T4a AND BBP=BBP4`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (17/33 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  ONLY when session=asia

### L22.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (16/32 of losers there)
- **Sharp: n=22  W=6/L=16  WR=27.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; session=asia  •  ONLY when RSI 30-40 weak

### L23.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=52  W=14/L=38  WR=26.9%
- Sharpen: sharpest is T4=T4a (25/38 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when 4h trend WITH trade

### L24.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is ZS=ZS4 (18/32 of losers there)
- **Sharp: n=25  W=7/L=18  WR=28.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore +1 to +2 overbought

### L25.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is ZS=ZS4 (18/32 of losers there)
- **Sharp: n=25  W=7/L=18  WR=28.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(17/10) | — |
| H60 | H60e(45/34) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/43) | short(43/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
