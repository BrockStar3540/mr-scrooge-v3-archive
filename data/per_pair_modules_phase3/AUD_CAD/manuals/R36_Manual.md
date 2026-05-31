# AUD_CAD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,106**  (W=1,353 / L=753)  -  WR: **64.2%**

## Session distribution

- ny_open: n=424  W=273/L=151  WR=64.4%
- ny_mid: n=419  W=280/L=139  WR=66.8%
- london_open: n=384  W=247/L=137  WR=64.3%
- asia: n=365  W=228/L=137  WR=62.5%
- london: n=230  W=145/L=85  WR=63.0%
- ny_close: n=171  W=115/L=56  WR=67.3%
- asia_late: n=75  W=46/L=29  WR=61.3%
- off_hours: n=38  W=19/L=19  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=london_open drops 8/17 losers (47%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W02.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude H20=H20b drops 2/8 losers (25%)
- **Final: n=111  W=105/L=6  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  AVOID when HTF20 slightly aligned

### W03.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=110  W=105/L=5  WR=95.5%
- Refine: exclude BBP=BBP5 drops 2/5 losers (40%)
- **Final: n=102  W=99/L=3  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W04.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=110  W=105/L=5  WR=95.5%
- Refine: exclude BBP=BBP5 drops 2/5 losers (40%)
- **Final: n=102  W=99/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W05.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude BBP=BBP5 drops 2/5 losers (40%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W06.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude BBP=BBP5 drops 2/5 losers (40%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W07.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude BBP=BBP5 drops 2/5 losers (40%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W08.  `H20=H20a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T1=T1c drops 12/15 losers (80%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W09.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T1=T1c drops 12/15 losers (80%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W10.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H60=H60a drops 9/14 losers (64%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W11.  `H20=H20a AND T1=T1c AND BBP=BBP2`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  AVOID when 4h trend WITH trade

### W12.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 7/13 losers (54%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W13.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 7/11 losers (64%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W15.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20a AND T1=T1c AND ZS=ZS2`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20a AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS2`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W20.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI5 drops 7/11 losers (64%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W21.  `H20=H20a AND T4=T4c AND BBP=BBP2`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=london_open drops 9/10 losers (90%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when session=london_open

### W22.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: LONG**  •  upper third; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=london_open drops 9/10 losers (90%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when session=london_open

### W24.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS3 drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS3 drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_open  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_open (29/59 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when session=ny_open

### L02.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is T1=T1c (35/50 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L03.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is T1=T1c (35/50 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is T1=T1c (35/50 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (28/49 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L06.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is H20=H20e (30/48 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF20 strongly against

### L07.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=75  W=30/L=45  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral

### L08.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=74  W=13/L=61  WR=17.6%
- Sharpen: sharpest is H20=H20e (61/61 of losers there)
- **Sharp: n=64  W=3/L=61  WR=4.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L09.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=72  W=28/L=44  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third

### L10.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is T1=T1a (27/42 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L11.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=68  W=26/L=42  WR=38.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L12.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is RSI=RSI4 (27/41 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L13.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is RSI=RSI5 (10/42 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20e AND T1=T1a AND ZS=ZS2`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=66  W=25/L=41  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold

### L15.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=66  W=25/L=41  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold

### L16.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is RSI=RSI5 (10/41 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L17.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is RSI=RSI5 (10/41 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=64  W=3/L=61  WR=4.7%
- Sharpen: sharpest is RSI=RSI5 (24/61 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=64  W=3/L=61  WR=4.7%
- Sharpen: sharpest is RSI=RSI5 (24/61 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=64  W=24/L=40  WR=37.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; lower third

### L21.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=63  W=3/L=60  WR=4.8%
- Sharpen: sharpest is RSI=RSI5 (24/60 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=63  W=3/L=60  WR=4.8%
- Sharpen: sharpest is RSI=RSI5 (24/60 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L23.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=63  W=3/L=60  WR=4.8%
- Sharpen: sharpest is RSI=RSI5 (24/60 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=63  W=24/L=39  WR=38.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; lower third

### L25.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is RSI=RSI3 (12/39 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/28) | H20e(27/41) |
| H60 | H60a(48/37) | H60e(35/47) |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/46) | short(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
