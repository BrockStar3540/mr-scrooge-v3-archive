# EUR_AUD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,528**  (W=3,256 / L=2,272)  -  WR: **58.9%**

## Session distribution

- asia: n=1872  W=1140/L=732  WR=60.9%
- ny_mid: n=878  W=509/L=369  WR=58.0%
- london_open: n=732  W=443/L=289  WR=60.5%
- ny_close: n=720  W=411/L=309  WR=57.1%
- ny_open: n=466  W=253/L=213  WR=54.3%
- london: n=414  W=259/L=155  WR=62.6%
- off_hours: n=242  W=127/L=115  WR=52.5%
- asia_late: n=204  W=114/L=90  WR=55.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP1 drops 5/12 losers (42%)
- **Final: n=77  W=70/L=7  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when just touched lower band

### W02.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP1 drops 5/12 losers (42%)
- **Final: n=77  W=70/L=7  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when just touched lower band

### W03.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP1 drops 5/12 losers (42%)
- **Final: n=77  W=70/L=7  WR=90.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when just touched lower band

### W04.  `T1=T1c AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W05.  `T4=T4c AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W06.  `BBP=BBP6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1c AND BBP=BBP6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W09.  `T4=T4c AND BBP=BBP6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W10.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W11.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20d drops 8/9 losers (89%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF20 mildly against

### W12.  `T4=T4a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20d drops 8/9 losers (89%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF20 mildly against

### W13.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20d drops 8/9 losers (89%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: LONG**  •  upper third; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF20 mildly against

### W14.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude BBP=BBP6 drops 7/8 losers (88%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_open  •  AVOID when deep above upper band

### W16.  `H20=H20e AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI>80 extreme overbought; session=asia

### W17.  `H60=H60e AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI>80 extreme overbought; session=asia

### W18.  `T1=T1a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI>80 extreme overbought; session=asia

### W19.  `T4=T4a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI>80 extreme overbought; session=asia

### W20.  `RSI=RSI7 AND direction_exec=long AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI>80 extreme overbought; session=asia

### W21.  `H20=H20e AND H60=H60e AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI>80 extreme overbought; session=asia

### W22.  `H20=H20e AND T1=T1a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI>80 extreme overbought; session=asia

### W23.  `H20=H20e AND T4=T4a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI>80 extreme overbought; session=asia

### W24.  `H20=H20e AND RSI=RSI7 AND direction_exec=long AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI>80 extreme overbought; session=asia

### W25.  `H60=H60e AND T1=T1a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI>80 extreme overbought; session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=302  W=118/L=184  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=302  W=118/L=184  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; RSI 60-70 strong

### L02.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=271  W=100/L=171  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=271  W=100/L=171  WR=36.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought

### L03.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=211  W=83/L=128  WR=39.3%
- Sharpen: sharpest is H20=H20e (62/128 of losers there)
- **Sharp: n=81  W=19/L=62  WR=23.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when HTF20 strongly against

### L04.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=181  W=70/L=111  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=181  W=70/L=111  WR=38.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong; session=asia

### L05.  `H20=H20e AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=169  W=64/L=105  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=169  W=64/L=105  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought; session=asia

### L06.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=166  W=64/L=102  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (61/102 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band; RSI 60-70 strong  •  ONLY when session=asia

### L07.  `H20=H20e AND T1=T1a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=166  W=64/L=102  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (61/102 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when session=asia

### L08.  `H20=H20e AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=166  W=64/L=102  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (61/102 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when session=asia

### L09.  `H20=H20e AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=166  W=64/L=102  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (61/102 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band; RSI 60-70 strong  •  ONLY when session=asia

### L10.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=151  W=52/L=99  WR=34.4%
- Sharpen: sharpest is BBP=BBP4 (38/99 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L11.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=139  W=52/L=87  WR=37.4%
- Sharpen: sharpest is BBP=BBP4 (28/87 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L12.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=139  W=52/L=87  WR=37.4%
- Sharpen: sharpest is BBP=BBP4 (28/87 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L13.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=139  W=52/L=87  WR=37.4%
- Sharpen: sharpest is BBP=BBP4 (28/87 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L14.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (38/71 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=asia

### L15.  `H20=H20b AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP5 (16/72 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=ny_mid  •  ONLY when just touched upper band

### L16.  `H20=H20b AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP5 (16/72 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=ny_mid  •  ONLY when just touched upper band

### L17.  `H20=H20b AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP5 (16/72 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; session=ny_mid  •  ONLY when just touched upper band

### L18.  `H20=H20b AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP5 (16/72 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when just touched upper band

### L19.  `H20=H20b AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP5 (16/72 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=ny_mid  •  ONLY when just touched upper band

### L20.  `H20=H20b AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP5 (16/72 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=ny_mid  •  ONLY when just touched upper band

### L21.  `H60=H60e AND BBP=BBP6 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is H20=H20e (61/64 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 60-70 strong; session=asia  •  ONLY when HTF20 strongly against

### L22.  `T1=T1a AND BBP=BBP6 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is H20=H20e (61/64 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 60-70 strong; session=asia  •  ONLY when HTF20 strongly against

### L23.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is H20=H20e (61/64 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong; session=asia  •  ONLY when HTF20 strongly against

### L24.  `BBP=BBP6 AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is H20=H20e (61/64 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: LONG**  •  deep above upper band; RSI 60-70 strong; session=asia  •  ONLY when HTF20 strongly against

### L25.  `H20=H20e AND BBP=BBP6 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=98  W=31/L=67  WR=31.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=98  W=31/L=67  WR=31.6%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 60-70 strong; session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(54/49) | T4a(46/51) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
