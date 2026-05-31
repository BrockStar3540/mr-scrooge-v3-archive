# CAD_JPY — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,909**  (W=1,776 / L=1,133)  -  WR: **61.1%**

## Session distribution

- ny_mid: n=1366  W=824/L=542  WR=60.3%
- asia: n=595  W=373/L=222  WR=62.7%
- london_open: n=403  W=236/L=167  WR=58.6%
- ny_close: n=252  W=158/L=94  WR=62.7%
- ny_open: n=190  W=123/L=67  WR=64.7%
- london: n=59  W=39/L=20  WR=66.1%
- off_hours: n=24  W=12/L=12  WR=50.0%
- asia_late: n=20  W=11/L=9  WR=55.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=180  W=162/L=18  WR=90.0%
- Refine: exclude T4=T4c drops 15/18 losers (83%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W02.  `H60=H60a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=180  W=162/L=18  WR=90.0%
- Refine: exclude T4=T4c drops 15/18 losers (83%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W03.  `T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=180  W=162/L=18  WR=90.0%
- Refine: exclude T4=T4c drops 15/18 losers (83%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=180  W=162/L=18  WR=90.0%
- Refine: exclude T4=T4c drops 15/18 losers (83%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20a AND H60=H60a AND RSI=RSI6`
- Raw: n=137  W=130/L=7  WR=94.9%
- Refine: exclude T4=T4c drops 4/7 losers (57%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND T1=T1a AND RSI=RSI6`
- Raw: n=137  W=130/L=7  WR=94.9%
- Refine: exclude T4=T4c drops 4/7 losers (57%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W07.  `H20=H20a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=137  W=130/L=7  WR=94.9%
- Refine: exclude T4=T4c drops 4/7 losers (57%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=137  W=130/L=7  WR=94.9%
- Refine: exclude T4=T4c drops 4/7 losers (57%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=137  W=130/L=7  WR=94.9%
- Refine: exclude T4=T4c drops 4/7 losers (57%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=137  W=130/L=7  WR=94.9%
- Refine: exclude T4=T4c drops 4/7 losers (57%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude session_bucket=ny_mid drops 15/17 losers (88%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W12.  `H20=H20d AND H60=H60e AND T4=T4c`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=london_open

### W13.  `H20=H20d AND H60=H60e AND direction_exec=short`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against  •  AVOID when session=london_open

### W14.  `H20=H20d AND T4=T4c AND direction_exec=short`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade  •  AVOID when session=london_open

### W15.  `H20=H20d AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=london_open

### W16.  `H60=H60a AND T4=T4a AND RSI=RSI6`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W17.  `T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W18.  `T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W19.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI6`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W20.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W21.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W22.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W25.  `H20=H20e AND H60=H60a AND ZS=ZS5`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 11/13 losers (85%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=233  W=91/L=142  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=233  W=91/L=142  WR=39.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=137  W=26/L=111  WR=19.0%
- Sharpen: sharpest is H20=H20e (84/111 of losers there)
- **Sharp: n=88  W=4/L=84  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=137  W=26/L=111  WR=19.0%
- Sharpen: sharpest is H20=H20e (84/111 of losers there)
- **Sharp: n=88  W=4/L=84  WR=4.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L04.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=137  W=26/L=111  WR=19.0%
- Sharpen: sharpest is H20=H20e (84/111 of losers there)
- **Sharp: n=88  W=4/L=84  WR=4.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=137  W=26/L=111  WR=19.0%
- Sharpen: sharpest is H20=H20e (84/111 of losers there)
- **Sharp: n=88  W=4/L=84  WR=4.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L06.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP4 (25/77 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L07.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP4 (25/77 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L08.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP4 (25/77 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L09.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP4 (25/77 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L10.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP4 (25/77 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L11.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=117  W=45/L=72  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (15/72 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L12.  `H20=H20e AND T4=T4c AND RSI=RSI6`
- Raw: n=115  W=36/L=79  WR=31.3%
- Sharpen: sharpest is H60=H60e (68/79 of losers there)
- **Sharp: n=72  W=4/L=68  WR=5.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L13.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (54/67 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 70-80 overbought

### L14.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (54/67 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  ONLY when RSI 70-80 overbought

### L15.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (54/67 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 70-80 overbought

### L16.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=107  W=42/L=65  WR=39.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid

### L17.  `T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=107  W=42/L=65  WR=39.3%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_mid

### L18.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=107  W=42/L=65  WR=39.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid

### L19.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=107  W=42/L=65  WR=39.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid

### L20.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=107  W=42/L=65  WR=39.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid

### L21.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is RSI=RSI6 (54/67 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L22.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is RSI=RSI6 (54/67 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L23.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is RSI=RSI6 (54/67 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L24.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=98  W=34/L=64  WR=34.7%
- Sharpen: sharpest is session_bucket=asia (19/64 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=asia

### L25.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=98  W=34/L=64  WR=34.7%
- Sharpen: sharpest is session_bucket=asia (19/64 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(58/43) | T1c(42/57) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
