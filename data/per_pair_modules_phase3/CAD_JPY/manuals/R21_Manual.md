# CAD_JPY — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,886**  (W=2,513 / L=1,373)  -  WR: **64.7%**

## Session distribution

- asia: n=1013  W=656/L=357  WR=64.8%
- ny_mid: n=926  W=592/L=334  WR=63.9%
- london_open: n=602  W=379/L=223  WR=63.0%
- ny_close: n=542  W=367/L=175  WR=67.7%
- ny_open: n=448  W=289/L=159  WR=64.5%
- london: n=225  W=145/L=80  WR=64.4%
- asia_late: n=111  W=75/L=36  WR=67.6%
- off_hours: n=19  W=10/L=9  WR=52.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude T1=T1a drops 22/23 losers (96%)
- **Final: n=81  W=80/L=1  WR=98.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend WITH trade

### W02.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=143  W=126/L=17  WR=88.1%
- Refine: exclude BBP=BBP5 drops 11/17 losers (65%)
- **Final: n=103  W=97/L=6  WR=94.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W03.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=143  W=126/L=17  WR=88.1%
- Refine: exclude BBP=BBP5 drops 11/17 losers (65%)
- **Final: n=103  W=97/L=6  WR=94.2%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W04.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=143  W=126/L=17  WR=88.1%
- Refine: exclude BBP=BBP5 drops 11/17 losers (65%)
- **Final: n=103  W=97/L=6  WR=94.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W05.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude BBP=BBP5 drops 11/17 losers (65%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude BBP=BBP5 drops 11/17 losers (65%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W07.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude BBP=BBP5 drops 11/17 losers (65%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W08.  `H60=H60a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band  •  AVOID when HTF20 aligned WITH trade

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude ZS=ZS5 drops 10/10 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude ZS=ZS5 drops 10/10 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W11.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude ZS=ZS5 drops 10/10 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W12.  `H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude ZS=ZS0 drops 5/8 losers (62%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when zscore <-3 extreme

### W13.  `T1=T1a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude ZS=ZS0 drops 5/8 losers (62%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: LONG**  •  1h trend WITH trade; deep below lower band  •  AVOID when zscore <-3 extreme

### W14.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude ZS=ZS0 drops 5/8 losers (62%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when zscore <-3 extreme

### W15.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude T1=T1c drops 7/10 losers (70%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W16.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude T1=T1c drops 7/10 losers (70%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W17.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude T1=T1c drops 7/10 losers (70%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W18.  `T4=T4c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T1=T1c drops 8/12 losers (67%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when 1h trend AGAINST trade

### W19.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=88  W=86/L=2  WR=97.7%
- Refine: exclude H20=H20e drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W20.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1c drops 7/11 losers (64%)
- **Final: n=50  W=46/L=4  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W21.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude H60=H60e drops 8/11 losers (73%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W22.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=81  W=80/L=1  WR=98.8%
- Refine: no further refinement
- **Final: n=81  W=80/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close

### W23.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 11/11 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W24.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 11/11 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W25.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 11/11 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP0 (45/77 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L02.  `H20=H20a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is RSI=RSI4 (41/68 of losers there)
- **Sharp: n=50  W=9/L=41  WR=18.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L03.  `H20=H20a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (40/67 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L04.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (40/67 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L05.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=101  W=38/L=63  WR=37.6%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_mid

### L06.  `T1=T1c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=99  W=32/L=67  WR=32.3%
- Sharpen: sharpest is RSI=RSI4 (50/67 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L07.  `H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=97  W=32/L=65  WR=33.0%
- Sharpen: sharpest is RSI=RSI4 (50/65 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L08.  `H60=H60e AND T1=T1c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=32/L=65  WR=33.0%
- Sharpen: sharpest is RSI=RSI4 (50/65 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L09.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is BBP=BBP4 (33/56 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when upper third

### L10.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is BBP=BBP4 (33/56 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_open  •  ONLY when upper third

### L11.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is BBP=BBP4 (33/56 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when upper third

### L12.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=90  W=32/L=58  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (47/58 of losers there)
- **Sharp: n=66  W=19/L=47  WR=28.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L13.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=90  W=32/L=58  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (47/58 of losers there)
- **Sharp: n=66  W=19/L=47  WR=28.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L14.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is RSI=RSI4 (47/56 of losers there)
- **Sharp: n=66  W=19/L=47  WR=28.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L15.  `T4=T4c AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is T1=T1c (47/53 of losers there)
- **Sharp: n=66  W=19/L=47  WR=28.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L16.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (34/53 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L17.  `H20=H20a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (34/53 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is T4=T4c (29/56 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is RSI=RSI4 (33/52 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L20.  `H20=H20a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is RSI=RSI4 (33/52 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L21.  `H60=H60e AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=83  W=27/L=56  WR=32.5%
- Sharpen: sharpest is T1=T1c (50/56 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L22.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=83  W=27/L=56  WR=32.5%
- Sharpen: sharpest is T1=T1c (50/56 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L23.  `H60=H60e AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=83  W=27/L=56  WR=32.5%
- Sharpen: sharpest is T1=T1c (50/56 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is BBP=BBP0 (27/50 of losers there)
- **Sharp: n=35  W=8/L=27  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L25.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is BBP=BBP0 (24/53 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
