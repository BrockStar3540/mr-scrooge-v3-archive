# USD_CHF — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,125**  (W=730 / L=395)  -  WR: **64.9%**

## Session distribution

- ny_open: n=278  W=179/L=99  WR=64.4%
- ny_mid: n=222  W=143/L=79  WR=64.4%
- london_open: n=218  W=143/L=75  WR=65.6%
- asia: n=214  W=150/L=64  WR=70.1%
- london: n=129  W=78/L=51  WR=60.5%
- ny_close: n=55  W=32/L=23  WR=58.2%
- asia_late: n=9  W=5/L=4  WR=55.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=375  W=320/L=55  WR=85.3%
- Refine: exclude H20=H20b drops 17/55 losers (31%)
- **Final: n=327  W=289/L=38  WR=88.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W02.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=375  W=320/L=55  WR=85.3%
- Refine: exclude H20=H20b drops 17/55 losers (31%)
- **Final: n=327  W=289/L=38  WR=88.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W03.  `T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=375  W=320/L=55  WR=85.3%
- Refine: exclude H20=H20b drops 17/55 losers (31%)
- **Final: n=327  W=289/L=38  WR=88.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=375  W=320/L=55  WR=85.3%
- Refine: exclude H20=H20b drops 17/55 losers (31%)
- **Final: n=327  W=289/L=38  WR=88.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W05.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=289  W=250/L=39  WR=86.5%
- Refine: exclude RSI=RSI4 drops 20/39 losers (51%)
- **Final: n=232  W=213/L=19  WR=91.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W06.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=287  W=248/L=39  WR=86.4%
- Refine: exclude RSI=RSI4 drops 20/39 losers (51%)
- **Final: n=232  W=213/L=19  WR=91.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W07.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=270  W=238/L=32  WR=88.1%
- Refine: exclude RSI=RSI4 drops 13/32 losers (41%)
- **Final: n=232  W=213/L=19  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=270  W=238/L=32  WR=88.1%
- Refine: exclude RSI=RSI4 drops 13/32 losers (41%)
- **Final: n=232  W=213/L=19  WR=91.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=204  W=185/L=19  WR=90.7%
- Refine: exclude session_bucket=london drops 10/19 losers (53%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W10.  `H20=H20a AND T4=T4a AND RSI=RSI5`
- Raw: n=204  W=185/L=19  WR=90.7%
- Refine: exclude session_bucket=london drops 10/19 losers (53%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W11.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=204  W=185/L=19  WR=90.7%
- Refine: exclude session_bucket=london drops 10/19 losers (53%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W12.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=204  W=185/L=19  WR=90.7%
- Refine: exclude session_bucket=london drops 10/19 losers (53%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W13.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=204  W=185/L=19  WR=90.7%
- Refine: exclude session_bucket=london drops 10/19 losers (53%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W14.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=204  W=185/L=19  WR=90.7%
- Refine: exclude session_bucket=london drops 10/19 losers (53%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W15.  `T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=174  W=149/L=25  WR=85.6%
- Refine: exclude BBP=BBP6 drops 17/25 losers (68%)
- **Final: n=92  W=84/L=8  WR=91.3%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W16.  `T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=171  W=149/L=22  WR=87.1%
- Refine: exclude BBP=BBP6 drops 17/22 losers (77%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W17.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=171  W=149/L=22  WR=87.1%
- Refine: exclude BBP=BBP6 drops 17/22 losers (77%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W18.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=166  W=147/L=19  WR=88.6%
- Refine: exclude BBP=BBP6 drops 17/19 losers (89%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W19.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=166  W=147/L=19  WR=88.6%
- Refine: exclude BBP=BBP6 drops 17/19 losers (89%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W20.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=166  W=147/L=19  WR=88.6%
- Refine: exclude BBP=BBP6 drops 17/19 losers (89%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W21.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=166  W=147/L=19  WR=88.6%
- Refine: exclude BBP=BBP6 drops 17/19 losers (89%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W22.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=166  W=147/L=19  WR=88.6%
- Refine: exclude BBP=BBP6 drops 17/19 losers (89%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W23.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=166  W=147/L=19  WR=88.6%
- Refine: exclude BBP=BBP6 drops 17/19 losers (89%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W24.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude BBP=BBP3 drops 9/17 losers (53%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia  •  AVOID when middle of band

### W25.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 10/18 losers (56%)
- **Final: n=106  W=98/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=230  W=87/L=143  WR=37.8%
- Sharpen: sharpest is RSI=RSI5 (107/143 of losers there)
- **Sharp: n=154  W=47/L=107  WR=30.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L02.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=228  W=82/L=146  WR=36.0%
- Sharpen: sharpest is RSI=RSI5 (107/146 of losers there)
- **Sharp: n=154  W=47/L=107  WR=30.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L03.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=212  W=75/L=137  WR=35.4%
- Sharpen: sharpest is ZS=ZS5 (45/137 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=212  W=75/L=137  WR=35.4%
- Sharpen: sharpest is ZS=ZS5 (45/137 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=156  W=59/L=97  WR=37.8%
- Sharpen: sharpest is H20=H20e (45/97 of losers there)
- **Sharp: n=59  W=14/L=45  WR=23.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=154  W=47/L=107  WR=30.5%
- Sharpen: sharpest is BBP=BBP5 (20/107 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L07.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=154  W=47/L=107  WR=30.5%
- Sharpen: sharpest is BBP=BBP5 (20/107 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L08.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=154  W=47/L=107  WR=30.5%
- Sharpen: sharpest is BBP=BBP5 (20/107 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when just touched upper band

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=154  W=47/L=107  WR=30.5%
- Sharpen: sharpest is BBP=BBP5 (20/107 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L10.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=154  W=47/L=107  WR=30.5%
- Sharpen: sharpest is BBP=BBP5 (20/107 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L11.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=154  W=47/L=107  WR=30.5%
- Sharpen: sharpest is BBP=BBP5 (20/107 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L12.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L13.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L15.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=140  W=47/L=93  WR=33.6%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L16.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=140  W=47/L=93  WR=33.6%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L17.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=140  W=47/L=93  WR=33.6%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=140  W=47/L=93  WR=33.6%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L19.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=140  W=47/L=93  WR=33.6%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L20.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=140  W=47/L=93  WR=33.6%
- Sharpen: sharpest is H20=H20e (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L21.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (14/60 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L22.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is H60=H60b (12/56 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L23.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is H60=H60b (12/56 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L24.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is H60=H60b (12/56 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L25.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is T1=T1c (53/53 of losers there)
- **Sharp: n=76  W=23/L=53  WR=30.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/33) | H20e(35/50) |
| H60 | H60d(13/3), H60e(38/32) | H60b(4/12), H60a(33/39) |
| T1 | T1a(63/34) | T1c(37/66) |
| T4 | T4a(64/32) | T4c(36/68) |
| BBP | — | BBP6(15/21) |
| RSI | — | — |
| ZS | — | ZS5(28/34) |
| strategy_id | — | — |
| direction_exec | long(63/34) | short(37/66) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
