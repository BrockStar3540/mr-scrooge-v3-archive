# AUD_JPY — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,804**  (W=2,326 / L=1,478)  -  WR: **61.1%**

## Session distribution

- asia: n=1014  W=613/L=401  WR=60.5%
- ny_mid: n=922  W=552/L=370  WR=59.9%
- london_open: n=815  W=500/L=315  WR=61.3%
- ny_close: n=490  W=311/L=179  WR=63.5%
- ny_open: n=333  W=205/L=128  WR=61.6%
- asia_late: n=138  W=89/L=49  WR=64.5%
- london: n=92  W=56/L=36  WR=60.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude T1=T1c drops 5/14 losers (36%)
- **Final: n=84  W=75/L=9  WR=89.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude T1=T1c drops 5/14 losers (36%)
- **Final: n=84  W=75/L=9  WR=89.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W03.  `H20=H20a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude T1=T1c drops 5/14 losers (36%)
- **Final: n=84  W=75/L=9  WR=89.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W04.  `H20=H20a AND T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude RSI=RSI5 drops 9/9 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 60-70 strong

### W05.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude RSI=RSI5 drops 9/9 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 60-70 strong

### W06.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude ZS=ZS4 drops 9/9 losers (100%)
- **Final: n=11  W=11/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W07.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20a drops 5/9 losers (56%)
- **Final: n=41  W=37/L=4  WR=90.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W08.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude BBP=BBP5 drops 7/9 losers (78%)
- **Final: n=29  W=27/L=2  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W10.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=ny_open  •  AVOID when RSI 60-70 strong

### W11.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when RSI 60-70 strong

### W12.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; session=ny_open  •  AVOID when RSI 60-70 strong

### W13.  `T1=T1c AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when RSI 60-70 strong

### W14.  `T4=T4a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; session=ny_open  •  AVOID when RSI 60-70 strong

### W15.  `T4=T4a AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when RSI 60-70 strong

### W16.  `T1=T1c AND T4=T4a AND session_bucket=asia_late`
- Raw: n=66  W=62/L=4  WR=93.9%
- Refine: exclude BBP=BBP2 drops 4/4 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia_late  •  AVOID when lower third

### W17.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W18.  `H60=H60e AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W19.  `T1=T1c AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W20.  `BBP=BBP6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W21.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W22.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W23.  `H60=H60e AND BBP=BBP6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W24.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W25.  `T1=T1c AND BBP=BBP6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=57  W=54/L=3  WR=94.7%
- Refine: exclude RSI=RSI4 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; session=ny_close  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia

### L02.  `H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia

### L03.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L04.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=asia

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L07.  `H20=H20e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia

### L08.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L09.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia

### L10.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=36/L=66  WR=35.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L11.  `T1=T1c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20e (46/64 of losers there)
- **Sharp: n=62  W=16/L=46  WR=25.8%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L12.  `T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20e (46/64 of losers there)
- **Sharp: n=62  W=16/L=46  WR=25.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L13.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H20=H20e (46/64 of losers there)
- **Sharp: n=62  W=16/L=46  WR=25.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L14.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=34/L=57  WR=37.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=34/L=57  WR=37.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L16.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=34/L=57  WR=37.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L17.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=34/L=57  WR=37.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L18.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is H20=H20e (46/59 of losers there)
- **Sharp: n=62  W=16/L=46  WR=25.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L19.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is H20=H20e (46/59 of losers there)
- **Sharp: n=62  W=16/L=46  WR=25.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L20.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is H20=H20e (46/59 of losers there)
- **Sharp: n=62  W=16/L=46  WR=25.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L21.  `T4=T4c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is H20=H20e (46/59 of losers there)
- **Sharp: n=62  W=16/L=46  WR=25.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L22.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H20=H20a (33/52 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is H20=H20e (38/51 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L24.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is H20=H20e (38/51 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L25.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is H20=H20e (38/51 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/45) | H20e(44/50) |
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
