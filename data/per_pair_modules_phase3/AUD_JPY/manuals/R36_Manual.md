# AUD_JPY — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,110**  (W=1,840 / L=1,270)  -  WR: **59.2%**

## Session distribution

- asia: n=863  W=502/L=361  WR=58.2%
- ny_mid: n=649  W=368/L=281  WR=56.7%
- london_open: n=629  W=391/L=238  WR=62.2%
- ny_close: n=346  W=209/L=137  WR=60.4%
- ny_open: n=299  W=172/L=127  WR=57.5%
- london: n=194  W=119/L=75  WR=61.3%
- asia_late: n=84  W=51/L=33  WR=60.7%
- off_hours: n=46  W=28/L=18  WR=60.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=184  W=158/L=26  WR=85.9%
- Refine: exclude BBP=BBP6 drops 8/26 losers (31%)
- **Final: n=172  W=154/L=18  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when deep above upper band

### W02.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=184  W=158/L=26  WR=85.9%
- Refine: exclude BBP=BBP6 drops 8/26 losers (31%)
- **Final: n=172  W=154/L=18  WR=89.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when deep above upper band

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude BBP=BBP6 drops 8/17 losers (47%)
- **Final: n=107  W=98/L=9  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when deep above upper band

### W04.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W05.  `H60=H60e AND BBP=BBP1 AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched lower band  •  AVOID when session=asia

### W06.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W07.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W08.  `H20=H20e AND H60=H60e AND BBP=BBP1`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  AVOID when session=asia

### W09.  `H20=H20e AND BBP=BBP1 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched lower band  •  AVOID when session=asia

### W10.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W11.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  AVOID when session=asia

### W12.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W13.  `T1=T1c AND T4=T4a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20e drops 8/12 losers (67%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W14.  `H60=H60e AND T4=T4c AND BBP=BBP1`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W15.  `T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W16.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W17.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W18.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W19.  `H20=H20e AND T4=T4c AND BBP=BBP1`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W20.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP1`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W21.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W22.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W23.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude T1=T1a drops 10/10 losers (100%)
- **Final: n=19  W=19/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W24.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 strongly against

### W25.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude T1=T1a drops 10/10 losers (100%)
- **Final: n=19  W=19/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=162  W=56/L=106  WR=34.6%
- Sharpen: sharpest is ZS=ZS3 (33/106 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L02.  `H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=159  W=54/L=105  WR=34.0%
- Sharpen: sharpest is ZS=ZS3 (33/105 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L03.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=159  W=54/L=105  WR=34.0%
- Sharpen: sharpest is ZS=ZS3 (33/105 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L04.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=159  W=54/L=105  WR=34.0%
- Sharpen: sharpest is ZS=ZS3 (33/105 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L05.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=156  W=62/L=94  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (33/94 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=156  W=62/L=94  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (33/94 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L07.  `T4=T4c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=156  W=62/L=94  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (33/94 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L08.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=146  W=47/L=99  WR=32.2%
- Sharpen: sharpest is ZS=ZS3 (33/99 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L09.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=146  W=47/L=99  WR=32.2%
- Sharpen: sharpest is ZS=ZS3 (33/99 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is ZS=ZS3 (33/92 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L11.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is ZS=ZS3 (33/92 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L12.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is ZS=ZS3 (33/86 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L13.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=51/L=77  WR=39.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; upper third

### L14.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=51/L=77  WR=39.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; upper third

### L15.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=51/L=77  WR=39.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third

### L16.  `H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=119  W=44/L=75  WR=37.0%
- Sharpen: sharpest is BBP=BBP1 (56/75 of losers there)
- **Sharp: n=77  W=21/L=56  WR=27.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L17.  `H20=H20a AND H60=H60a AND ZS=ZS1`
- Raw: n=116  W=43/L=73  WR=37.1%
- Sharpen: sharpest is BBP=BBP1 (54/73 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L18.  `H20=H20a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=116  W=43/L=73  WR=37.1%
- Sharpen: sharpest is BBP=BBP1 (54/73 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L19.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=116  W=43/L=73  WR=37.1%
- Sharpen: sharpest is BBP=BBP1 (54/73 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L20.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=111  W=42/L=69  WR=37.8%
- Sharpen: sharpest is BBP=BBP1 (50/69 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L21.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=111  W=42/L=69  WR=37.8%
- Sharpen: sharpest is BBP=BBP1 (50/69 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L22.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=111  W=42/L=69  WR=37.8%
- Sharpen: sharpest is BBP=BBP1 (50/69 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L23.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is BBP=BBP1 (48/67 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L24.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is BBP=BBP1 (48/67 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L25.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is BBP=BBP1 (48/67 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
