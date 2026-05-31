# AUD_JPY — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,159**  (W=2,495 / L=1,664)  -  WR: **60.0%**

## Session distribution

- asia: n=1366  W=826/L=540  WR=60.5%
- ny_mid: n=734  W=436/L=298  WR=59.4%
- london_open: n=595  W=371/L=224  WR=62.4%
- ny_open: n=559  W=317/L=242  WR=56.7%
- london: n=385  W=241/L=144  WR=62.6%
- asia_late: n=240  W=140/L=100  WR=58.3%
- ny_close: n=232  W=133/L=99  WR=57.3%
- off_hours: n=48  W=31/L=17  WR=64.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=146  W=125/L=21  WR=85.6%
- Refine: exclude H20=H20d drops 9/21 losers (43%)
- **Final: n=137  W=125/L=12  WR=91.2%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; session=asia  •  AVOID when HTF20 mildly against

### W02.  `T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=144  W=123/L=21  WR=85.4%
- Refine: exclude H60=H60e drops 10/21 losers (48%)
- **Final: n=116  W=105/L=11  WR=90.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when HTF60 strongly against

### W03.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_open drops 10/17 losers (59%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when session=ny_open

### W04.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_open drops 10/17 losers (59%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak  •  AVOID when session=ny_open

### W05.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_open drops 10/17 losers (59%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when session=ny_open

### W06.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H60=H60a drops 9/14 losers (64%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W07.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=116  W=105/L=11  WR=90.5%
- Refine: exclude BBP=BBP4 drops 9/11 losers (82%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when upper third

### W08.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=116  W=105/L=11  WR=90.5%
- Refine: exclude BBP=BBP4 drops 9/11 losers (82%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when upper third

### W09.  `H60=H60e AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude BBP=BBP1 drops 12/17 losers (71%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W10.  `T4=T4c AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude BBP=BBP1 drops 12/17 losers (71%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W11.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude BBP=BBP4 drops 9/13 losers (69%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  AVOID when upper third

### W12.  `T1=T1a AND T4=T4c AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude H20=H20d drops 9/14 losers (64%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band; session=asia  •  AVOID when HTF20 mildly against

### W13.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude BBP=BBP1 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W14.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude BBP=BBP1 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W15.  `T4=T4c AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude BBP=BBP1 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W16.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude BBP=BBP4 drops 9/11 losers (82%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when upper third

### W17.  `H20=H20e AND T4=T4c AND session_bucket=london`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude BBP=BBP1 drops 7/12 losers (58%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W18.  `H20=H20e AND T4=T4c AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep below lower band; session=asia  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; session=asia  •  AVOID when RSI 40-50 lower neutral

### W20.  `T4=T4c AND BBP=BBP0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep below lower band; session=asia  •  AVOID when RSI 40-50 lower neutral

### W21.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude ZS=ZS2 drops 7/11 losers (64%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W22.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude ZS=ZS2 drops 7/11 losers (64%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W23.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when 4h trend WITH trade

### W24.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when 4h trend WITH trade

### W25.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude H60=H60a drops 9/9 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND BBP=BBP0`
- Raw: n=278  W=111/L=167  WR=39.9%
- Sharpen: sharpest is RSI=RSI2 (62/167 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L02.  `H20=H20a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=278  W=111/L=167  WR=39.9%
- Sharpen: sharpest is RSI=RSI2 (62/167 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L03.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=278  W=111/L=167  WR=39.9%
- Sharpen: sharpest is RSI=RSI2 (62/167 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L04.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=271  W=99/L=172  WR=36.5%
- Sharpen: sharpest is BBP=BBP0 (71/172 of losers there)
- **Sharp: n=88  W=17/L=71  WR=19.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L05.  `H20=H20a AND H60=H60a AND RSI=RSI2`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `H20=H20a AND T1=T1c AND RSI=RSI2`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=262  W=99/L=163  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (101/163 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=240  W=95/L=145  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (57/145 of losers there)
- **Sharp: n=74  W=17/L=57  WR=23.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L15.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=240  W=95/L=145  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (57/145 of losers there)
- **Sharp: n=74  W=17/L=57  WR=23.0%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L16.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=240  W=95/L=145  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (57/145 of losers there)
- **Sharp: n=74  W=17/L=57  WR=23.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L17.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=226  W=83/L=143  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (55/143 of losers there)
- **Sharp: n=72  W=17/L=55  WR=23.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=226  W=83/L=143  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (55/143 of losers there)
- **Sharp: n=72  W=17/L=55  WR=23.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L19.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=226  W=83/L=143  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (55/143 of losers there)
- **Sharp: n=72  W=17/L=55  WR=23.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=194  W=62/L=132  WR=32.0%
- Sharpen: sharpest is T4=T4c (67/132 of losers there)
- **Sharp: n=83  W=16/L=67  WR=19.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=194  W=62/L=132  WR=32.0%
- Sharpen: sharpest is T4=T4c (67/132 of losers there)
- **Sharp: n=83  W=16/L=67  WR=19.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=194  W=62/L=132  WR=32.0%
- Sharpen: sharpest is T4=T4c (67/132 of losers there)
- **Sharp: n=83  W=16/L=67  WR=19.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20a AND T1=T1c AND BBP=BBP0`
- Raw: n=182  W=71/L=111  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (62/111 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L24.  `H60=H60a AND T1=T1c AND BBP=BBP0`
- Raw: n=182  W=71/L=111  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (62/111 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L25.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=182  W=71/L=111  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (62/111 of losers there)
- **Sharp: n=79  W=17/L=62  WR=21.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
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
