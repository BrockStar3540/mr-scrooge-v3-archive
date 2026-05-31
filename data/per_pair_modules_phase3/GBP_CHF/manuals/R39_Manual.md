# GBP_CHF — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,687**  (W=1,091 / L=596)  -  WR: **64.7%**

## Session distribution

- london_open: n=362  W=230/L=132  WR=63.5%
- ny_mid: n=269  W=180/L=89  WR=66.9%
- ny_close: n=268  W=177/L=91  WR=66.0%
- ny_open: n=237  W=150/L=87  WR=63.3%
- london: n=235  W=149/L=86  WR=63.4%
- asia: n=172  W=115/L=57  WR=66.9%
- off_hours: n=94  W=55/L=39  WR=58.5%
- asia_late: n=50  W=35/L=15  WR=70.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=267  W=229/L=38  WR=85.8%
- Refine: exclude BBP=BBP5 drops 30/38 losers (79%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W02.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=267  W=229/L=38  WR=85.8%
- Refine: exclude BBP=BBP5 drops 30/38 losers (79%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W03.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=267  W=229/L=38  WR=85.8%
- Refine: exclude BBP=BBP5 drops 30/38 losers (79%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W04.  `H20=H20e AND T1=T1c AND ZS=ZS5`
- Raw: n=188  W=165/L=23  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 9/23 losers (39%)
- **Final: n=168  W=154/L=14  WR=91.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W05.  `H20=H20e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=188  W=165/L=23  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 9/23 losers (39%)
- **Final: n=168  W=154/L=14  WR=91.7%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W06.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=188  W=165/L=23  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 9/23 losers (39%)
- **Final: n=168  W=154/L=14  WR=91.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W07.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=182  W=157/L=25  WR=86.3%
- Refine: exclude session_bucket=ny_open drops 9/25 losers (36%)
- **Final: n=162  W=146/L=16  WR=90.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W08.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=180  W=157/L=23  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 9/23 losers (39%)
- **Final: n=160  W=146/L=14  WR=91.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W09.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=180  W=157/L=23  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 9/23 losers (39%)
- **Final: n=160  W=146/L=14  WR=91.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W10.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=142  W=129/L=13  WR=90.8%
- Refine: exclude H20=H20d drops 5/13 losers (38%)
- **Final: n=137  W=129/L=8  WR=94.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 mildly against

### W11.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=129  W=121/L=8  WR=93.8%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=london_open

### W12.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=129  W=121/L=8  WR=93.8%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  AVOID when session=london_open

### W13.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=129  W=121/L=8  WR=93.8%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=london_open

### W14.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude H20=H20d drops 5/13 losers (38%)
- **Final: n=123  W=115/L=8  WR=93.5%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W15.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude H20=H20d drops 5/13 losers (38%)
- **Final: n=123  W=115/L=8  WR=93.5%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W16.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude H20=H20d drops 5/13 losers (38%)
- **Final: n=123  W=115/L=8  WR=93.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W17.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=122  W=113/L=9  WR=92.6%
- Refine: exclude session_bucket=london_open drops 7/9 losers (78%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W18.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W19.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W20.  `H20=H20a AND T1=T1c AND direction_exec=short`
- Raw: n=112  W=101/L=11  WR=90.2%
- Refine: exclude session_bucket=london drops 8/11 losers (73%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london

### W21.  `H20=H20e AND T1=T1c AND BBP=BBP6`
- Raw: n=105  W=97/L=8  WR=92.4%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=london_open

### W22.  `H20=H20e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=105  W=97/L=8  WR=92.4%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band  •  AVOID when session=london_open

### W23.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=105  W=97/L=8  WR=92.4%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=london_open

### W24.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude session_bucket=london drops 8/10 losers (80%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=london

### W25.  `T1=T1c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude H60=H60a drops 7/10 losers (70%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=144  W=51/L=93  WR=35.4%
- Sharpen: sharpest is ZS=ZS5 (39/93 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=136  W=47/L=89  WR=34.6%
- Sharpen: sharpest is ZS=ZS5 (37/89 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=136  W=47/L=89  WR=34.6%
- Sharpen: sharpest is ZS=ZS5 (37/89 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=136  W=47/L=89  WR=34.6%
- Sharpen: sharpest is ZS=ZS5 (37/89 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=130  W=51/L=79  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (41/79 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L06.  `H20=H20a AND T1=T1a AND ZS=ZS5`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is BBP=BBP6 (42/80 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L07.  `H20=H20a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is BBP=BBP6 (42/80 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L08.  `H20=H20a AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is BBP=BBP6 (42/80 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L09.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=128  W=49/L=79  WR=38.3%
- Sharpen: sharpest is BBP=BBP6 (41/79 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L10.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=128  W=49/L=79  WR=38.3%
- Sharpen: sharpest is BBP=BBP6 (41/79 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L11.  `T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is H20=H20d (19/60 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L12.  `T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is H20=H20d (19/60 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L13.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is H20=H20d (19/60 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L14.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is H20=H20d (19/60 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L15.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is H20=H20d (19/60 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L16.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is H20=H20d (19/60 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L17.  `H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is BBP=BBP6 (19/62 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when deep above upper band

### L18.  `H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is BBP=BBP6 (19/62 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: LONG**  •  HTF60 strongly against; session=london_open  •  ONLY when deep above upper band

### L19.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is BBP=BBP6 (19/62 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when deep above upper band

### L20.  `H20=H20e AND T1=T1a AND direction_exec=long`
- Raw: n=90  W=25/L=65  WR=27.8%
- Sharpen: sharpest is session_bucket=asia (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when session=asia

### L21.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=85  W=27/L=58  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (19/58 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when deep above upper band

### L22.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=85  W=27/L=58  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (19/58 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when deep above upper band

### L23.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=85  W=27/L=58  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (19/58 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when deep above upper band

### L24.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=82  W=21/L=61  WR=25.6%
- Sharpen: sharpest is RSI=RSI4 (31/61 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=80  W=21/L=59  WR=26.2%
- Sharpen: sharpest is session_bucket=asia (16/59 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(12/6), H20e(37/32) | H20a(30/37) |
| H60 | H60a(44/31), H60b(13/7) | H60e(32/47), H60d(6/11) |
| T1 | T1c(59/38) | T1a(40/62) |
| T4 | T4c(61/38) | T4a(39/62) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(63/36) | long(37/64) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
