# AUD_CAD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,320**  (W=850 / L=470)  -  WR: **64.4%**

## Session distribution

- ny_mid: n=574  W=367/L=207  WR=63.9%
- asia: n=243  W=156/L=87  WR=64.2%
- ny_close: n=162  W=110/L=52  WR=67.9%
- ny_open: n=109  W=64/L=45  WR=58.7%
- london: n=99  W=72/L=27  WR=72.7%
- london_open: n=87  W=54/L=33  WR=62.1%
- asia_late: n=30  W=16/L=14  WR=53.3%
- off_hours: n=16  W=11/L=5  WR=68.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude BBP=BBP0 drops 5/18 losers (28%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when deep below lower band

### W02.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude BBP=BBP0 drops 5/18 losers (28%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_mid  •  AVOID when deep below lower band

### W03.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude BBP=BBP0 drops 5/18 losers (28%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when deep below lower band

### W04.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=119  W=106/L=13  WR=89.1%
- Refine: exclude H20=H20e drops 12/13 losers (92%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 strongly against

### W05.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=119  W=106/L=13  WR=89.1%
- Refine: exclude H20=H20e drops 12/13 losers (92%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 strongly against

### W06.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude BBP=BBP0 drops 5/14 losers (36%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when deep below lower band

### W07.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude BBP=BBP0 drops 5/14 losers (36%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when deep below lower band

### W08.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 strongly against

### W09.  `T4=T4a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia_late drops 5/8 losers (62%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W10.  `H20=H20d AND H60=H60e AND RSI=RSI4`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W11.  `H20=H20d AND T1=T1c AND RSI=RSI4`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W12.  `H20=H20d AND RSI=RSI4 AND direction_exec=short`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W13.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T1=T1c drops 7/8 losers (88%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W14.  `H20=H20d AND H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W15.  `H20=H20d AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W16.  `H20=H20d AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W17.  `H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W18.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W19.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W20.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W21.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W22.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W23.  `H60=H60a AND T1=T1a AND session_bucket=london`
- Raw: n=59  W=56/L=3  WR=94.9%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when HTF20 mildly against

### W24.  `H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=59  W=56/L=3  WR=94.9%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london  •  AVOID when HTF20 mildly against

### W25.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=59  W=56/L=3  WR=94.9%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (17/47 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L02.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is H20=H20b (8/42 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L03.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is H20=H20b (8/42 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L04.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is H20=H20b (8/42 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L05.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_open (12/31 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when session=ny_open

### L06.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_open (12/31 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when session=ny_open

### L07.  `T4=T4c AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: sharpest is session_bucket=ny_open (10/31 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when session=ny_open

### L08.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is ZS=ZS3 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L09.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is ZS=ZS3 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L10.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is ZS=ZS3 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L11.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is ZS=ZS3 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L12.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is ZS=ZS3 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L13.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is ZS=ZS3 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L14.  `H60=H60e AND T1=T1c AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when upper third

### L15.  `H60=H60e AND RSI=RSI5 AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london  •  ONLY when upper third

### L16.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  ONLY when upper third

### L17.  `T1=T1c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london  •  ONLY when upper third

### L18.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  ONLY when upper third

### L19.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london  •  ONLY when upper third

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london  •  ONLY when upper third

### L21.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when upper third

### L22.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=london  •  ONLY when upper third

### L23.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (8/24 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london  •  ONLY when upper third

### L24.  `H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=39  W=13/L=26  WR=33.3%
- Sharpen: sharpest is H20=H20e (14/26 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 strongly against

### L25.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=39  W=13/L=26  WR=33.3%
- Sharpen: sharpest is H20=H20e (14/26 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(51/46) | H60a(48/53) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/46) | long(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
