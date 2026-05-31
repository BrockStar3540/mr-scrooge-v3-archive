# EUR_JPY — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **5,040**  (W=3,069 / L=1,971)  -  WR: **60.9%**

## Session distribution

- ny_mid: n=1325  W=801/L=524  WR=60.5%
- london_open: n=1123  W=701/L=422  WR=62.4%
- asia: n=1112  W=659/L=453  WR=59.3%
- ny_open: n=457  W=262/L=195  WR=57.3%
- london: n=442  W=293/L=149  WR=66.3%
- ny_close: n=299  W=191/L=108  WR=63.9%
- asia_late: n=229  W=132/L=97  WR=57.6%
- off_hours: n=53  W=30/L=23  WR=56.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude BBP=BBP6 drops 7/16 losers (44%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W02.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude RSI=RSI4 drops 7/11 losers (64%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W03.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W04.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W05.  `T1=T1a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W06.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude RSI=RSI5 drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W07.  `H20=H20a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W09.  `T4=T4a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W10.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W11.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W12.  `H60=H60a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W13.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W14.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W15.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W16.  `H20=H20e AND H60=H60a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: no further refinement
- **Final: n=91  W=78/L=13  WR=85.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia

### W17.  `H20=H20e AND T1=T1a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: no further refinement
- **Final: n=91  W=78/L=13  WR=85.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 70-80 overbought; session=asia

### W18.  `H20=H20e AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: no further refinement
- **Final: n=91  W=78/L=13  WR=85.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 70-80 overbought; session=asia

### W19.  `H20=H20e AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: no further refinement
- **Final: n=91  W=78/L=13  WR=85.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia

### W20.  `H60=H60a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; session=asia  •  AVOID when RSI 60-70 strong

### W21.  `T1=T1a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; session=asia  •  AVOID when RSI 60-70 strong

### W22.  `T4=T4a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; session=asia  •  AVOID when RSI 60-70 strong

### W23.  `BBP=BBP5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  just touched upper band; session=asia  •  AVOID when RSI 60-70 strong

### W24.  `H60=H60a AND T1=T1a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; just touched upper band; session=asia  •  AVOID when RSI 60-70 strong

### W25.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band; session=asia  •  AVOID when RSI 60-70 strong

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia

### L02.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L03.  `T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L04.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L07.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L09.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L10.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=200  W=77/L=123  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=200  W=77/L=123  WR=38.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L11.  `H20=H20e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=167  W=64/L=103  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (37/103 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third  •  ONLY when session=ny_mid

### L12.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=165  W=64/L=101  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (35/101 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L13.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=165  W=64/L=101  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (35/101 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L14.  `H20=H20e AND T1=T1c AND BBP=BBP2`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_mid (37/99 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L15.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_mid (37/99 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L16.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (35/97 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L17.  `H20=H20e AND H60=H60e AND BBP=BBP2`
- Raw: n=152  W=58/L=94  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_mid (35/94 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when session=ny_mid

### L18.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=152  W=58/L=94  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_mid (35/94 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when session=ny_mid

### L19.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=150  W=58/L=92  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_mid (33/92 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L20.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=149  W=58/L=91  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_mid (31/91 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L21.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (35/90 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L22.  `H20=H20e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_mid (31/87 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L23.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_mid (31/87 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L24.  `H20=H20e AND T4=T4c AND ZS=ZS2`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (30/86 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L25.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (30/86 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/40) | — |
| H60 | H60a(47/41) | H60e(42/48) |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/45) | short(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
