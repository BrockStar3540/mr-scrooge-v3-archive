# AUD_CAD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,921**  (W=1,872 / L=1,049)  -  WR: **64.1%**

## Session distribution

- asia: n=869  W=555/L=314  WR=63.9%
- ny_mid: n=571  W=362/L=209  WR=63.4%
- ny_close: n=367  W=243/L=124  WR=66.2%
- ny_open: n=326  W=207/L=119  WR=63.5%
- london_open: n=273  W=174/L=99  WR=63.7%
- asia_late: n=247  W=161/L=86  WR=65.2%
- london: n=232  W=151/L=81  WR=65.1%
- off_hours: n=36  W=19/L=17  WR=52.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND H60=H60e AND T1=T1a`
- Raw: n=210  W=179/L=31  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 9/31 losers (29%)
- **Final: n=193  W=171/L=22  WR=88.6%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=ny_mid

### W02.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=210  W=179/L=31  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 9/31 losers (29%)
- **Final: n=193  W=171/L=22  WR=88.6%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  AVOID when session=ny_mid

### W03.  `H20=H20c AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=210  W=179/L=31  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 9/31 losers (29%)
- **Final: n=193  W=171/L=22  WR=88.6%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=ny_mid

### W04.  `H20=H20c AND H60=H60e AND T4=T4a`
- Raw: n=204  W=179/L=25  WR=87.7%
- Refine: exclude BBP=BBP1 drops 8/25 losers (32%)
- **Final: n=176  W=159/L=17  WR=90.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  AVOID when just touched lower band

### W05.  `H20=H20c AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=204  W=179/L=25  WR=87.7%
- Refine: exclude BBP=BBP1 drops 8/25 losers (32%)
- **Final: n=176  W=159/L=17  WR=90.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when just touched lower band

### W06.  `H20=H20c AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=204  W=179/L=25  WR=87.7%
- Refine: exclude BBP=BBP1 drops 8/25 losers (32%)
- **Final: n=176  W=159/L=17  WR=90.3%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  AVOID when just touched lower band

### W07.  `H60=H60e AND T1=T1a AND RSI=RSI1`
- Raw: n=196  W=178/L=18  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 9/18 losers (50%)
- **Final: n=186  W=177/L=9  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W08.  `H60=H60e AND RSI=RSI1 AND direction_exec=short`
- Raw: n=196  W=178/L=18  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 9/18 losers (50%)
- **Final: n=186  W=177/L=9  WR=95.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 20-30 oversold  •  AVOID when session=ny_close

### W09.  `H60=H60e AND T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=196  W=178/L=18  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 9/18 losers (50%)
- **Final: n=186  W=177/L=9  WR=95.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W10.  `H20=H20c AND H60=H60e AND RSI=RSI2`
- Raw: n=154  W=133/L=21  WR=86.4%
- Refine: exclude BBP=BBP1 drops 7/21 losers (33%)
- **Final: n=129  W=115/L=14  WR=89.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 30-40 weak  •  AVOID when just touched lower band

### W11.  `H20=H20c AND H60=H60e AND T1=T1a AND RSI=RSI2`
- Raw: n=154  W=133/L=21  WR=86.4%
- Refine: exclude BBP=BBP1 drops 7/21 losers (33%)
- **Final: n=129  W=115/L=14  WR=89.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when just touched lower band

### W12.  `H20=H20c AND H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=154  W=133/L=21  WR=86.4%
- Refine: exclude BBP=BBP1 drops 7/21 losers (33%)
- **Final: n=129  W=115/L=14  WR=89.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when just touched lower band

### W13.  `H20=H20c AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=154  W=133/L=21  WR=86.4%
- Refine: exclude BBP=BBP1 drops 7/21 losers (33%)
- **Final: n=129  W=115/L=14  WR=89.1%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; RSI 30-40 weak  •  AVOID when just touched lower band

### W14.  `T1=T1a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude H20=H20d drops 16/20 losers (80%)
- **Final: n=132  W=128/L=4  WR=97.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W15.  `RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude H20=H20d drops 16/20 losers (80%)
- **Final: n=132  W=128/L=4  WR=97.0%**
- **Dir: SHORT**  •  RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W16.  `T1=T1a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude H20=H20d drops 16/20 losers (80%)
- **Final: n=132  W=128/L=4  WR=97.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W17.  `H20=H20e AND T1=T1a AND RSI=RSI1`
- Raw: n=147  W=132/L=15  WR=89.8%
- Refine: exclude session_bucket=ny_close drops 9/15 losers (60%)
- **Final: n=117  W=111/L=6  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W18.  `H20=H20e AND RSI=RSI1 AND direction_exec=short`
- Raw: n=147  W=132/L=15  WR=89.8%
- Refine: exclude session_bucket=ny_close drops 9/15 losers (60%)
- **Final: n=117  W=111/L=6  WR=94.9%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 20-30 oversold  •  AVOID when session=ny_close

### W19.  `H20=H20e AND T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=147  W=132/L=15  WR=89.8%
- Refine: exclude session_bucket=ny_close drops 9/15 losers (60%)
- **Final: n=117  W=111/L=6  WR=94.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W20.  `H60=H60c AND T4=T4c AND session_bucket=asia`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude BBP=BBP2 drops 8/17 losers (47%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W21.  `H20=H20c AND H60=H60e AND session_bucket=asia`
- Raw: n=126  W=113/L=13  WR=89.7%
- Refine: exclude RSI=RSI2 drops 12/13 losers (92%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=asia  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20c AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=126  W=113/L=13  WR=89.7%
- Refine: exclude RSI=RSI2 drops 12/13 losers (92%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20c AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=126  W=113/L=13  WR=89.7%
- Refine: exclude RSI=RSI2 drops 12/13 losers (92%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W24.  `H20=H20c AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=126  W=113/L=13  WR=89.7%
- Refine: exclude RSI=RSI2 drops 12/13 losers (92%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; session=asia  •  AVOID when RSI 30-40 weak

### W25.  `H60=H60e AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=124  W=122/L=2  WR=98.4%
- Refine: exclude BBP=BBP1 drops 2/2 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20c AND H60=H60a AND T1=T1c`
- Raw: n=154  W=59/L=95  WR=38.3%
- Sharpen: sharpest is T4=T4c (95/95 of losers there)
- **Sharp: n=144  W=49/L=95  WR=34.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L02.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=154  W=59/L=95  WR=38.3%
- Sharpen: sharpest is T4=T4c (95/95 of losers there)
- **Sharp: n=144  W=49/L=95  WR=34.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  ONLY when 4h trend AGAINST trade

### L03.  `H20=H20c AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=154  W=59/L=95  WR=38.3%
- Sharpen: sharpest is T4=T4c (95/95 of losers there)
- **Sharp: n=144  W=49/L=95  WR=34.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=151  W=43/L=108  WR=28.5%
- Sharpen: sharpest is BBP=BBP0 (39/108 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L05.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=151  W=43/L=108  WR=28.5%
- Sharpen: sharpest is BBP=BBP0 (39/108 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L06.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=151  W=43/L=108  WR=28.5%
- Sharpen: sharpest is BBP=BBP0 (39/108 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L07.  `H20=H20c AND H60=H60a AND T4=T4c`
- Raw: n=144  W=49/L=95  WR=34.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=144  W=49/L=95  WR=34.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade

### L08.  `H20=H20c AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=144  W=49/L=95  WR=34.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=144  W=49/L=95  WR=34.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade

### L09.  `H20=H20c AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=144  W=49/L=95  WR=34.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=144  W=49/L=95  WR=34.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade

### L10.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is T4=T4c (42/77 of losers there)
- **Sharp: n=61  W=19/L=42  WR=31.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20a AND T1=T1c AND RSI=RSI1`
- Raw: n=120  W=41/L=79  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (21/79 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L12.  `H20=H20a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=120  W=41/L=79  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (21/79 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L13.  `H20=H20a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=120  W=41/L=79  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (21/79 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L14.  `H20=H20c AND H60=H60a AND RSI=RSI2`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=40/L=68  WR=37.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 30-40 weak

### L15.  `H20=H20c AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=40/L=68  WR=37.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak

### L16.  `H20=H20c AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=40/L=68  WR=37.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak

### L17.  `H20=H20c AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=40/L=68  WR=37.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 30-40 weak

### L18.  `H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=99  W=26/L=73  WR=26.3%
- Sharpen: sharpest is session_bucket=ny_open (21/73 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L19.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=99  W=26/L=73  WR=26.3%
- Sharpen: sharpest is session_bucket=ny_open (21/73 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L20.  `H60=H60a AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=99  W=26/L=73  WR=26.3%
- Sharpen: sharpest is session_bucket=ny_open (21/73 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L21.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T4=T4c (25/60 of losers there)
- **Sharp: n=33  W=8/L=25  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T4=T4c (25/60 of losers there)
- **Sharp: n=33  W=8/L=25  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T4=T4c (25/60 of losers there)
- **Sharp: n=33  W=8/L=25  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20a AND H60=H60a AND RSI=RSI1`
- Raw: n=92  W=34/L=58  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_open (21/58 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L25.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=92  W=34/L=58  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_open (21/58 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(33/26) | H20e(25/33) |
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
