# EUR_USD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,363**  (W=1,497 / L=866)  -  WR: **63.4%**

## Session distribution

- ny_close: n=812  W=511/L=301  WR=62.9%
- asia: n=763  W=475/L=288  WR=62.3%
- ny_mid: n=255  W=163/L=92  WR=63.9%
- ny_open: n=155  W=96/L=59  WR=61.9%
- asia_late: n=136  W=90/L=46  WR=66.2%
- london_open: n=117  W=76/L=41  WR=65.0%
- off_hours: n=68  W=46/L=22  WR=67.6%
- london: n=57  W=40/L=17  WR=70.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W02.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W03.  `T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=90  W=85/L=5  WR=94.4%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore -1 to +1 neutral

### W04.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when RSI 50-60 upper neutral

### W05.  `T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W06.  `T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W07.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when just touched upper band

### W08.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude BBP=BBP5 drops 5/5 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W09.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude BBP=BBP5 drops 5/5 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W10.  `H20=H20c AND T1=T1a AND session_bucket=ny_close`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W12.  `H20=H20c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W13.  `H20=H20c AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20c AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20c AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W16.  `H20=H20e AND H60=H60a AND session_bucket=asia`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W17.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude T1=T1a drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W18.  `T1=T1c AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 50-60 upper neutral

### W19.  `T4=T4a AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude BBP=BBP6 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when deep above upper band

### W20.  `H20=H20e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude T1=T1a drops 9/10 losers (90%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W21.  `H60=H60e AND RSI=RSI5 AND session_bucket=asia_late`
- Raw: n=65  W=64/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=asia_late

### W22.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20e AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W24.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W25.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is H20=H20a (33/80 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L02.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/78 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=ny_open

### L03.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/78 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=ny_open

### L04.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_close (36/58 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L05.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_close (36/58 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L06.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_close (36/58 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L07.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_close (36/58 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L08.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is ZS=ZS4 (27/55 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L09.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is ZS=ZS4 (27/55 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L10.  `H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is T4=T4a (43/50 of losers there)
- **Sharp: n=61  W=18/L=43  WR=29.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L11.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=71  W=8/L=63  WR=11.3%
- Sharpen: sharpest is T4=T4c (55/63 of losers there)
- **Sharp: n=55  W=0/L=55  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=71  W=21/L=50  WR=29.6%
- Sharpen: sharpest is T1=T1a (37/50 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=asia  •  ONLY when 1h trend WITH trade

### L13.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (35/42 of losers there)
- **Sharp: n=50  W=15/L=35  WR=30.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L14.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (35/42 of losers there)
- **Sharp: n=50  W=15/L=35  WR=30.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is RSI=RSI4 (30/45 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_open (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_open

### L17.  `H60=H60e AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is T1=T1a (34/45 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L18.  `H20=H20a AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (15/39 of losers there)
- **Sharp: n=20  W=5/L=15  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 60-70 strong  •  ONLY when session=asia

### L19.  `H20=H20a AND BBP=BBP3 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (15/39 of losers there)
- **Sharp: n=20  W=5/L=15  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when session=asia

### L20.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=61  W=17/L=44  WR=27.9%
- Sharpen: sharpest is direction_exec=short (27/44 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when short

### L21.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=61  W=18/L=43  WR=29.5%
- Sharpen: sharpest is ZS=ZS4 (25/43 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=61  W=18/L=43  WR=29.5%
- Sharpen: sharpest is ZS=ZS4 (25/43 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is T1=T1a (38/40 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=asia  •  ONLY when 1h trend WITH trade

### L24.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (14/36 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when upper third

### L25.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (14/36 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(46/41) | H20a(40/47) |
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
