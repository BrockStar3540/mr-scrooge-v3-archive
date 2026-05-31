# CHF_JPY — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **8,856**  (W=5,365 / L=3,491)  -  WR: **60.6%**

## Session distribution

- asia: n=2417  W=1479/L=938  WR=61.2%
- london_open: n=1480  W=897/L=583  WR=60.6%
- ny_mid: n=1355  W=840/L=515  WR=62.0%
- ny_open: n=1327  W=787/L=540  WR=59.3%
- ny_close: n=985  W=583/L=402  WR=59.2%
- london: n=713  W=438/L=275  WR=61.4%
- asia_late: n=386  W=236/L=150  WR=61.1%
- off_hours: n=193  W=105/L=88  WR=54.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=178  W=154/L=24  WR=86.5%
- Refine: no further refinement
- **Final: n=178  W=154/L=24  WR=86.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 70-80 overbought; session=asia

### W02.  `H20=H20a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=171  W=147/L=24  WR=86.0%
- Refine: no further refinement
- **Final: n=171  W=147/L=24  WR=86.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### W03.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude session_bucket=asia drops 7/23 losers (30%)
- **Final: n=148  W=132/L=16  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=asia

### W04.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude ZS=ZS3 drops 7/17 losers (41%)
- **Final: n=113  W=103/L=10  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude H60=H60a drops 6/12 losers (50%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W06.  `T4=T4c AND BBP=BBP5 AND session_bucket=ny_mid`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude RSI=RSI6 drops 16/16 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W07.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude RSI=RSI6 drops 16/16 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W08.  `H20=H20a AND T1=T1a AND ZS=ZS3 AND strategy_id=alpha_extended_fade_v2`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: no further refinement
- **Final: n=103  W=88/L=15  WR=85.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral; strategy=alpha_extended_fade_v2

### W09.  `H20=H20a AND ZS=ZS3 AND strategy_id=alpha_extended_fade_v2 AND direction_exec=long`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: no further refinement
- **Final: n=103  W=88/L=15  WR=85.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral; strategy=alpha_extended_fade_v2

### W10.  `H20=H20a AND H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude ZS=ZS3 drops 7/11 losers (64%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude ZS=ZS3 drops 7/11 losers (64%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude ZS=ZS3 drops 7/11 losers (64%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20a AND T4=T4c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=98  W=89/L=9  WR=90.8%
- Refine: exclude H60=H60a drops 6/9 losers (67%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W14.  `T4=T4a AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 5/14 losers (36%)
- **Final: n=81  W=72/L=9  WR=88.9%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; session=ny_close  •  AVOID when HTF20 strongly against

### W15.  `T4=T4a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 5/14 losers (36%)
- **Final: n=81  W=72/L=9  WR=88.9%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; zscore -1 to +1 neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W16.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude ZS=ZS3 drops 6/11 losers (55%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20a AND H60=H60e AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude ZS=ZS3 drops 6/11 losers (55%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; upper third; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20a AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude ZS=ZS3 drops 6/11 losers (55%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W19.  `H20=H20a AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude RSI=RSI5 drops 11/12 losers (92%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; session=ny_close  •  AVOID when RSI 60-70 strong

### W20.  `H20=H20a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude RSI=RSI5 drops 11/12 losers (92%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; zscore -1 to +1 neutral; session=ny_close  •  AVOID when RSI 60-70 strong

### W21.  `H60=H60a AND RSI=RSI6 AND session_bucket=asia_late`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia_late  •  AVOID when HTF20 mildly against

### W22.  `T1=T1a AND RSI=RSI6 AND session_bucket=asia_late`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=asia_late  •  AVOID when HTF20 mildly against

### W23.  `T4=T4a AND RSI=RSI6 AND session_bucket=asia_late`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=asia_late  •  AVOID when HTF20 mildly against

### W24.  `RSI=RSI6 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=asia_late  •  AVOID when HTF20 mildly against

### W25.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=asia_late`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=asia_late  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=280  W=96/L=184  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=280  W=96/L=184  WR=34.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia

### L02.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=280  W=96/L=184  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=280  W=96/L=184  WR=34.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=asia

### L03.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=280  W=96/L=184  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=280  W=96/L=184  WR=34.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L04.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=280  W=96/L=184  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=280  W=96/L=184  WR=34.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L05.  `H20=H20e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=280  W=96/L=184  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=280  W=96/L=184  WR=34.3%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia

### L06.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=213  W=84/L=129  WR=39.4%
- Sharpen: sharpest is session_bucket=asia_late (33/129 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when session=asia_late

### L07.  `H20=H20e AND BBP=BBP6 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=213  W=84/L=129  WR=39.4%
- Sharpen: sharpest is session_bucket=asia_late (33/129 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; RSI 70-80 overbought  •  ONLY when session=asia_late

### L08.  `T4=T4c AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=207  W=82/L=125  WR=39.6%
- Sharpen: sharpest is session_bucket=asia_late (33/125 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when session=asia_late

### L09.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=189  W=70/L=119  WR=37.0%
- Sharpen: sharpest is session_bucket=asia_late (33/119 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when session=asia_late

### L10.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=189  W=70/L=119  WR=37.0%
- Sharpen: sharpest is session_bucket=asia_late (33/119 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when session=asia_late

### L11.  `T4=T4c AND BBP=BBP6 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=189  W=70/L=119  WR=37.0%
- Sharpen: sharpest is session_bucket=asia_late (33/119 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when session=asia_late

### L12.  `H20=H20b AND H60=H60e AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  ONLY when just touched upper band

### L13.  `H20=H20b AND T1=T1c AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L14.  `H20=H20b AND direction_exec=short AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; session=asia  •  ONLY when just touched upper band

### L15.  `H20=H20b AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L16.  `H20=H20b AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L17.  `H20=H20b AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  ONLY when just touched upper band

### L18.  `H20=H20b AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L19.  `H20=H20b AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L20.  `H20=H20b AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is BBP=BBP5 (26/112 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L21.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=178  W=64/L=114  WR=36.0%
- Sharpen: sharpest is session_bucket=asia_late (33/114 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when session=asia_late

### L22.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND ZS=ZS3`
- Raw: n=168  W=66/L=102  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_close (32/102 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L23.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND ZS=ZS3`
- Raw: n=168  W=66/L=102  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_close (32/102 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L24.  `H20=H20e AND RSI=RSI6 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=168  W=66/L=102  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_close (32/102 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L25.  `H20=H20e AND T1=T1c AND session_bucket=asia_late`
- Raw: n=153  W=56/L=97  WR=36.6%
- Sharpen: sharpest is RSI=RSI6 (48/97 of losers there)
- **Sharp: n=50  W=2/L=48  WR=4.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia_late  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/33) | H20e(33/44) |
| H60 | H60a(52/44) | H60e(45/53) |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/45) | short(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
