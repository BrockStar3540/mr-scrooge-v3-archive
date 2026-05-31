# NZD_USD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,211**  (W=746 / L=465)  -  WR: **61.6%**

## Session distribution

- asia: n=497  W=295/L=202  WR=59.4%
- ny_mid: n=178  W=121/L=57  WR=68.0%
- ny_open: n=172  W=103/L=69  WR=59.9%
- ny_close: n=161  W=98/L=63  WR=60.9%
- london: n=110  W=72/L=38  WR=65.5%
- london_open: n=50  W=28/L=22  WR=56.0%
- asia_late: n=25  W=18/L=7  WR=72.0%
- off_hours: n=18  W=11/L=7  WR=61.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND session_bucket=london`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude RSI=RSI7 drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london  •  AVOID when RSI>80 extreme overbought

### W02.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=55  W=54/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close

### W03.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_open

### W04.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_open

### W05.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_open

### W06.  `H20=H20e AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 70-80 overbought  •  AVOID when session=ny_open

### W07.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude H60=H60a drops 5/6 losers (83%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W08.  `H20=H20e AND H60=H60a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=45  W=40/L=5  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W09.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=43  W=38/L=5  WR=88.4%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W10.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=42  W=41/L=1  WR=97.6%
- Refine: no further refinement
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_close

### W11.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=42  W=41/L=1  WR=97.6%
- Refine: no further refinement
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_close

### W12.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=42  W=41/L=1  WR=97.6%
- Refine: no further refinement
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  upper third; session=ny_close

### W13.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=42  W=41/L=1  WR=97.6%
- Refine: no further refinement
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=ny_close

### W14.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=42  W=41/L=1  WR=97.6%
- Refine: no further refinement
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_close

### W15.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=42  W=41/L=1  WR=97.6%
- Refine: no further refinement
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=ny_close

### W16.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=24  W=23/L=1  WR=95.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when just touched upper band

### W17.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=24  W=23/L=1  WR=95.8%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  AVOID when just touched upper band

### W18.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=24  W=23/L=1  WR=95.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when just touched upper band

### W19.  `H20=H20e AND T1=T1a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=39  W=34/L=5  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=31  W=29/L=2  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W20.  `H20=H20e AND T4=T4a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=39  W=34/L=5  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=31  W=29/L=2  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W21.  `H20=H20e AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=39  W=34/L=5  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=31  W=29/L=2  WR=93.5%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W22.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=38  W=37/L=1  WR=97.4%
- Refine: no further refinement
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_close

### W23.  `T4=T4a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=38  W=37/L=1  WR=97.4%
- Refine: no further refinement
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_close

### W24.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=38  W=37/L=1  WR=97.4%
- Refine: no further refinement
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_close

### W25.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=38  W=37/L=1  WR=97.4%
- Refine: no further refinement
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is session_bucket=asia (48/61 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L02.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is session_bucket=asia (48/61 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L03.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is session_bucket=asia (48/61 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L04.  `T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H60=H60e (48/58 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 strongly against

### L05.  `H60=H60e AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP5 (44/48 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when just touched upper band

### L06.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP5 (44/48 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when just touched upper band

### L07.  `H60=H60e AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP5 (44/48 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when just touched upper band

### L08.  `T4=T4c AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=70  W=20/L=50  WR=28.6%
- Sharpen: sharpest is H60=H60e (44/50 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; session=asia  •  ONLY when HTF60 strongly against

### L09.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=70  W=20/L=50  WR=28.6%
- Sharpen: sharpest is H60=H60e (44/50 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 strongly against

### L10.  `T1=T1c AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is H60=H60e (44/47 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; session=asia  •  ONLY when HTF60 strongly against

### L11.  `BBP=BBP5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is H60=H60e (44/47 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  just touched upper band; session=asia  •  ONLY when HTF60 strongly against

### L12.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is H60=H60e (44/47 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 strongly against

### L13.  `T1=T1c AND BBP=BBP5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is H60=H60e (44/47 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; session=asia  •  ONLY when HTF60 strongly against

### L14.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is H60=H60e (44/47 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 strongly against

### L15.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=66  W=19/L=47  WR=28.8%
- Sharpen: sharpest is H60=H60e (44/47 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band; session=asia  •  ONLY when HTF60 strongly against

### L16.  `T4=T4c AND BBP=BBP5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=66  W=19/L=47  WR=28.8%
- Sharpen: sharpest is H60=H60e (44/47 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band; session=asia  •  ONLY when HTF60 strongly against

### L17.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=65  W=17/L=48  WR=26.2%
- Sharpen: sharpest is BBP=BBP5 (44/48 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when just touched upper band

### L18.  `H60=H60e AND T1=T1c AND BBP=BBP5`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L19.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L20.  `H60=H60e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band  •  ONLY when session=asia

### L21.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L22.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L23.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L24.  `H60=H60e AND T4=T4c AND BBP=BBP5`
- Raw: n=63  W=17/L=46  WR=27.0%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L25.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=63  W=17/L=46  WR=27.0%
- Sharpen: sharpest is session_bucket=asia (44/46 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(52/43) | H20a(45/54) |
| H60 | H60a(43/30) | H60e(33/44) |
| T1 | T1a(51/44) | T1c(49/56) |
| T4 | T4a(53/44) | T4c(47/56) |
| BBP | — | — |
| RSI | — | RSI7(20/25) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(51/44) | short(49/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
