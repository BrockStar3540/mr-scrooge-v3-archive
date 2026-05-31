# AUD_NZD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,176**  (W=727 / L=449)  -  WR: **61.8%**

## Session distribution

- asia: n=587  W=357/L=230  WR=60.8%
- london_open: n=140  W=90/L=50  WR=64.3%
- ny_open: n=102  W=68/L=34  WR=66.7%
- ny_close: n=89  W=48/L=41  WR=53.9%
- off_hours: n=81  W=49/L=32  WR=60.5%
- ny_mid: n=71  W=46/L=25  WR=64.8%
- asia_late: n=59  W=39/L=20  WR=66.1%
- london: n=47  W=30/L=17  WR=63.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W02.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W03.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W04.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W05.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W06.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W07.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W08.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W09.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W10.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS3 drops 8/9 losers (89%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H60=H60a drops 7/9 losers (78%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 aligned WITH trade

### W12.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS3 drops 8/9 losers (89%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS3 drops 8/9 losers (89%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W14.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H60=H60a drops 7/9 losers (78%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 aligned WITH trade

### W15.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude ZS=ZS3 drops 8/10 losers (80%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude ZS=ZS3 drops 8/10 losers (80%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude ZS=ZS3 drops 8/9 losers (89%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W18.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude ZS=ZS3 drops 8/10 losers (80%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W19.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude ZS=ZS3 drops 8/8 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W20.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI4 drops 9/9 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W21.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude H60=H60a drops 5/5 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 aligned WITH trade

### W22.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=57  W=56/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### W23.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=57  W=56/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### W24.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=57  W=56/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### W25.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=57  W=56/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20b AND T4=T4a AND RSI=RSI5`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is BBP=BBP6 (12/53 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L02.  `H20=H20b AND H60=H60a AND RSI=RSI5`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (12/48 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L03.  `H20=H20b AND RSI=RSI5 AND direction_exec=long`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (12/48 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong  •  ONLY when deep above upper band

### L04.  `H20=H20b AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (12/48 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L05.  `H20=H20b AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (12/48 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L06.  `H20=H20b AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (12/48 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L07.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when deep above upper band

### L08.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L09.  `H20=H20b AND T1=T1a AND direction_exec=long`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade  •  ONLY when deep above upper band

### L10.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L11.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when deep above upper band

### L12.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L13.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=68  W=27/L=41  WR=39.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=asia

### L14.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is session_bucket=off_hours (23/42 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when session=off_hours

### L15.  `H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is session_bucket=off_hours (23/42 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep above upper band  •  ONLY when session=off_hours

### L16.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is session_bucket=off_hours (23/42 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when session=off_hours

### L17.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is session_bucket=off_hours (23/42 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when session=off_hours

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=59  W=19/L=40  WR=32.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=19/L=40  WR=32.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia

### L19.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is H20=H20a (36/39 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L20.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is H20=H20a (37/40 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L21.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is H20=H20a (37/40 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L22.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is H20=H20a (37/40 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=off_hours (23/36 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when session=off_hours

### L24.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=off_hours (23/36 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when session=off_hours

### L25.  `T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=off_hours (23/36 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band  •  ONLY when session=off_hours

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(17/6) | H20b(7/17) |
| H60 | H60e(55/46) | H60a(45/54) |
| T1 | T1c(55/47) | T1a(45/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/46) | long(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
