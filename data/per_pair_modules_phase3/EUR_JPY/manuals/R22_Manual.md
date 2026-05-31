# EUR_JPY — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,361**  (W=1,953 / L=1,408)  -  WR: **58.1%**

## Session distribution

- london_open: n=1240  W=700/L=540  WR=56.5%
- asia: n=859  W=500/L=359  WR=58.2%
- ny_mid: n=748  W=433/L=315  WR=57.9%
- ny_open: n=138  W=85/L=53  WR=61.6%
- ny_close: n=127  W=80/L=47  WR=63.0%
- asia_late: n=122  W=75/L=47  WR=61.5%
- london: n=117  W=75/L=42  WR=64.1%
- off_hours: n=10  W=5/L=5  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude H20=H20e drops 10/15 losers (67%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 strongly against

### W02.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=95  W=87/L=8  WR=91.6%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=london_open

### W03.  `H20=H20b AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF20 slightly aligned; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W04.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=london_open drops 4/13 losers (31%)
- **Final: n=81  W=72/L=9  WR=88.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W05.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H60=H60a drops 5/12 losers (42%)
- **Final: n=68  W=61/L=7  WR=89.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=london_open

### W12.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=london_open

### W13.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20a drops 4/6 losers (67%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20a drops 4/6 losers (67%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T1=T1a AND session_bucket=london`
- Raw: n=68  W=66/L=2  WR=97.1%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=68  W=66/L=2  WR=97.1%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W17.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=68  W=66/L=2  WR=97.1%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=68  W=66/L=2  WR=97.1%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W19.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H60=H60a drops 5/9 losers (56%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W20.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid

### W21.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid

### W22.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid

### W23.  `BBP=BBP5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude H60=H60b drops 7/7 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  just touched upper band; session=asia  •  AVOID when HTF60 slightly aligned

### W24.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude H60=H60b drops 7/7 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 slightly aligned

### W25.  `H20=H20b AND H60=H60e AND BBP=BBP5`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; just touched upper band  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=194  W=74/L=120  WR=38.1%
- Sharpen: sharpest is BBP=BBP6 (36/120 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L02.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=194  W=74/L=120  WR=38.1%
- Sharpen: sharpest is BBP=BBP6 (36/120 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L03.  `T1=T1c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=184  W=61/L=123  WR=33.2%
- Sharpen: sharpest is BBP=BBP6 (52/123 of losers there)
- **Sharp: n=61  W=9/L=52  WR=14.8%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when deep above upper band

### L04.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=171  W=67/L=104  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (32/104 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L05.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=170  W=58/L=112  WR=34.1%
- Sharpen: sharpest is BBP=BBP6 (44/112 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when deep above upper band

### L06.  `H60=H60e AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=161  W=58/L=103  WR=36.0%
- Sharpen: sharpest is BBP=BBP6 (44/103 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when deep above upper band

### L07.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=161  W=58/L=103  WR=36.0%
- Sharpen: sharpest is BBP=BBP6 (44/103 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when deep above upper band

### L08.  `H60=H60e AND ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=161  W=58/L=103  WR=36.0%
- Sharpen: sharpest is BBP=BBP6 (44/103 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when deep above upper band

### L09.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=150  W=56/L=94  WR=37.3%
- Sharpen: sharpest is BBP=BBP6 (31/94 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when deep above upper band

### L10.  `H60=H60e AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L11.  `T1=T1c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L12.  `T4=T4c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L13.  `RSI=RSI6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L16.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L17.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L18.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L19.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/92 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

### L20.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=141  W=52/L=89  WR=36.9%
- Sharpen: sharpest is BBP=BBP3 (41/89 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when middle of band

### L21.  `T4=T4c AND ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is H20=H20d (17/83 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when HTF20 mildly against

### L22.  `H20=H20d AND H60=H60e AND RSI=RSI6`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 70-80 overbought

### L23.  `H20=H20d AND T1=T1c AND RSI=RSI6`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 70-80 overbought

### L24.  `H20=H20d AND T4=T4c AND RSI=RSI6`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 70-80 overbought

### L25.  `H20=H20d AND RSI=RSI6 AND direction_exec=short`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(20/15) | H20d(14/20) |
| H60 | — | — |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
