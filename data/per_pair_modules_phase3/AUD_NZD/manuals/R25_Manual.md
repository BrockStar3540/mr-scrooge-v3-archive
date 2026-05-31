# AUD_NZD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,126**  (W=1,973 / L=1,153)  -  WR: **63.1%**

## Session distribution

- asia: n=1029  W=664/L=365  WR=64.5%
- london_open: n=491  W=311/L=180  WR=63.3%
- ny_open: n=371  W=240/L=131  WR=64.7%
- london: n=295  W=181/L=114  WR=61.4%
- ny_close: n=289  W=171/L=118  WR=59.2%
- ny_mid: n=249  W=160/L=89  WR=64.3%
- off_hours: n=213  W=125/L=88  WR=58.7%
- asia_late: n=189  W=121/L=68  WR=64.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W02.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W03.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W04.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W05.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W06.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W07.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=87  W=80/L=7  WR=92.0%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W08.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=87  W=80/L=7  WR=92.0%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W09.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=87  W=80/L=7  WR=92.0%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W10.  `T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude RSI=RSI4 drops 5/10 losers (50%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W11.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude session_bucket=asia_late drops 5/7 losers (71%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W12.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude session_bucket=asia_late drops 5/7 losers (71%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W13.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude session_bucket=asia_late drops 5/7 losers (71%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W14.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude session_bucket=asia_late drops 5/7 losers (71%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W15.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=66  W=64/L=2  WR=97.0%
- Refine: exclude session_bucket=off_hours drops 2/2 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=off_hours

### W16.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when just touched upper band

### W17.  `H20=H20d AND H60=H60e AND ZS=ZS5`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W18.  `H20=H20d AND ZS=ZS5 AND direction_exec=short`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W19.  `H20=H20d AND H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W20.  `H20=H20d AND T4=T4c AND ZS=ZS5`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W21.  `H20=H20d AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W22.  `H20=H20d AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W23.  `H20=H20e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude BBP=BBP4 drops 8/9 losers (89%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when upper third

### W24.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude BBP=BBP4 drops 8/9 losers (89%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when upper third

### W25.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude BBP=BBP4 drops 8/9 losers (89%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=144  W=49/L=95  WR=34.0%
- Sharpen: sharpest is RSI=RSI4 (21/95 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L02.  `H20=H20a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=144  W=49/L=95  WR=34.0%
- Sharpen: sharpest is RSI=RSI4 (21/95 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L03.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=144  W=49/L=95  WR=34.0%
- Sharpen: sharpest is RSI=RSI4 (21/95 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L04.  `H20=H20a AND T1=T1a AND BBP=BBP6`
- Raw: n=141  W=49/L=92  WR=34.8%
- Sharpen: sharpest is RSI=RSI4 (18/92 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=141  W=49/L=92  WR=34.8%
- Sharpen: sharpest is RSI=RSI4 (18/92 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L06.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=141  W=49/L=92  WR=34.8%
- Sharpen: sharpest is RSI=RSI4 (18/92 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L07.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is RSI=RSI4 (21/91 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L08.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is RSI=RSI4 (21/91 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L09.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is RSI=RSI4 (21/91 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L10.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=131  W=43/L=88  WR=32.8%
- Sharpen: sharpest is RSI=RSI4 (18/88 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=105  W=33/L=72  WR=31.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=33/L=72  WR=31.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 60-70 strong

### L12.  `H20=H20a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=104  W=34/L=70  WR=32.7%
- Sharpen: sharpest is RSI=RSI4 (21/70 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is RSI=RSI4 (21/65 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L14.  `H20=H20a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is RSI=RSI4 (21/65 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is RSI=RSI4 (18/62 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=31/L=62  WR=33.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band; RSI 60-70 strong

### L17.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=31/L=62  WR=33.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band; RSI 60-70 strong

### L18.  `H20=H20a AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=31/L=62  WR=33.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band; RSI 60-70 strong

### L19.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=89  W=28/L=61  WR=31.5%
- Sharpen: sharpest is RSI=RSI4 (21/61 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L20.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=83  W=25/L=58  WR=30.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=83  W=25/L=58  WR=30.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 60-70 strong

### L21.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is ZS=ZS5 (18/45 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is ZS=ZS5 (18/45 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is ZS=ZS5 (18/45 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is ZS=ZS5 (18/45 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20b AND T1=T1c AND session_bucket=asia`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is ZS=ZS3 (11/37 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when zscore -1 to +1 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
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
