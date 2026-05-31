# EUR_CAD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,052**  (W=1,948 / L=1,104)  -  WR: **63.8%**

## Session distribution

- asia: n=811  W=519/L=292  WR=64.0%
- london_open: n=633  W=401/L=232  WR=63.3%
- london: n=491  W=306/L=185  WR=62.3%
- ny_open: n=345  W=220/L=125  WR=63.8%
- ny_close: n=290  W=191/L=99  WR=65.9%
- asia_late: n=274  W=181/L=93  WR=66.1%
- ny_mid: n=142  W=90/L=52  WR=63.4%
- off_hours: n=66  W=40/L=26  WR=60.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND H60=H60a AND T4=T4a`
- Raw: n=194  W=166/L=28  WR=85.6%
- Refine: exclude session_bucket=london drops 10/28 losers (36%)
- **Final: n=176  W=158/L=18  WR=89.8%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=london

### W02.  `H20=H20d AND H60=H60a AND direction_exec=short`
- Raw: n=194  W=166/L=28  WR=85.6%
- Refine: exclude session_bucket=london drops 10/28 losers (36%)
- **Final: n=176  W=158/L=18  WR=89.8%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade  •  AVOID when session=london

### W03.  `H20=H20d AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=194  W=166/L=28  WR=85.6%
- Refine: exclude session_bucket=london drops 10/28 losers (36%)
- **Final: n=176  W=158/L=18  WR=89.8%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=london

### W04.  `H20=H20d AND H60=H60a AND T1=T1a`
- Raw: n=187  W=162/L=25  WR=86.6%
- Refine: exclude session_bucket=london drops 10/25 losers (40%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london

### W05.  `H20=H20d AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=187  W=162/L=25  WR=86.6%
- Refine: exclude session_bucket=london drops 10/25 losers (40%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=london

### W06.  `H20=H20d AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=187  W=162/L=25  WR=86.6%
- Refine: exclude session_bucket=london drops 10/25 losers (40%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london

### W07.  `T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=london drops 13/21 losers (62%)
- **Final: n=111  W=103/L=8  WR=92.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W08.  `T1=T1a AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=105  W=91/L=14  WR=86.7%
- Refine: exclude BBP=BBP4 drops 3/14 losers (21%)
- **Final: n=100  W=89/L=11  WR=89.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W09.  `RSI=RSI2 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=105  W=91/L=14  WR=86.7%
- Refine: exclude BBP=BBP4 drops 3/14 losers (21%)
- **Final: n=100  W=89/L=11  WR=89.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W10.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=105  W=91/L=14  WR=86.7%
- Refine: exclude BBP=BBP4 drops 3/14 losers (21%)
- **Final: n=100  W=89/L=11  WR=89.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W11.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude BBP=BBP6 drops 4/9 losers (44%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when deep above upper band

### W12.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude BBP=BBP6 drops 4/9 losers (44%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=london_open  •  AVOID when deep above upper band

### W13.  `H60=H60a AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude BBP=BBP4 drops 3/11 losers (27%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W14.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude BBP=BBP4 drops 3/11 losers (27%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W15.  `H60=H60a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude BBP=BBP4 drops 3/11 losers (27%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W16.  `T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude T1=T1a drops 7/10 losers (70%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W17.  `H20=H20d AND H60=H60a AND BBP=BBP2`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1c drops 3/11 losers (27%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; lower third  •  AVOID when 1h trend AGAINST trade

### W18.  `H20=H20d AND H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1c drops 3/11 losers (27%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20d AND H60=H60a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1c drops 3/11 losers (27%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; lower third  •  AVOID when 1h trend AGAINST trade

### W20.  `T1=T1a AND BBP=BBP2 AND session_bucket=london`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/12 losers (25%)
- **Final: n=81  W=72/L=9  WR=88.9%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=london  •  AVOID when strategy=RG1_range_bound_scalp_long

### W21.  `H20=H20d AND H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/8 losers (38%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when strategy=RG1_range_bound_scalp_long

### W22.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W23.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude BBP=BBP4 drops 3/11 losers (27%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W24.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude BBP=BBP4 drops 3/11 losers (27%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

### W25.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude BBP=BBP4 drops 3/11 losers (27%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20b AND H60=H60e AND T4=T4c`
- Raw: n=148  W=47/L=101  WR=31.8%
- Sharpen: sharpest is T1=T1c (99/101 of losers there)
- **Sharp: n=136  W=37/L=99  WR=27.2%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L02.  `H20=H20b AND H60=H60e AND direction_exec=long`
- Raw: n=148  W=47/L=101  WR=31.8%
- Sharpen: sharpest is T1=T1c (99/101 of losers there)
- **Sharp: n=136  W=37/L=99  WR=27.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against  •  ONLY when 1h trend AGAINST trade

### L03.  `H20=H20b AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=148  W=47/L=101  WR=31.8%
- Sharpen: sharpest is T1=T1c (99/101 of losers there)
- **Sharp: n=136  W=37/L=99  WR=27.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20b AND H60=H60e AND T1=T1c`
- Raw: n=136  W=37/L=99  WR=27.2%
- Sharpen: sharpest is RSI=RSI3 (21/99 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L05.  `H20=H20b AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=136  W=37/L=99  WR=27.2%
- Sharpen: sharpest is RSI=RSI3 (21/99 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L06.  `H20=H20b AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=136  W=37/L=99  WR=27.2%
- Sharpen: sharpest is RSI=RSI3 (21/99 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L07.  `H20=H20b AND T4=T4c AND RSI=RSI2`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H60=H60e (74/80 of losers there)
- **Sharp: n=105  W=31/L=74  WR=29.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L08.  `H20=H20b AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H60=H60e (74/80 of losers there)
- **Sharp: n=105  W=31/L=74  WR=29.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L09.  `H20=H20b AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H60=H60e (74/80 of losers there)
- **Sharp: n=105  W=31/L=74  WR=29.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L10.  `H20=H20b AND H60=H60e AND RSI=RSI2`
- Raw: n=105  W=31/L=74  WR=29.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=31/L=74  WR=29.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 30-40 weak

### L11.  `H20=H20b AND H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=105  W=31/L=74  WR=29.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=31/L=74  WR=29.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak

### L12.  `H20=H20b AND H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=105  W=31/L=74  WR=29.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=31/L=74  WR=29.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak

### L13.  `H20=H20b AND H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=105  W=31/L=74  WR=29.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=31/L=74  WR=29.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 30-40 weak

### L14.  `H20=H20a AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is session_bucket=london (7/42 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when session=london

### L15.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is ZS=ZS1 (33/45 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia_late  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is ZS=ZS1 (33/45 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia_late  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is ZS=ZS1 (33/45 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia_late  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is H20=H20e (28/45 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L19.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is T1=T1a (42/42 of losers there)
- **Sharp: n=57  W=15/L=42  WR=26.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when 1h trend WITH trade

### L20.  `H20=H20b AND H60=H60e AND BBP=BBP2`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is T1=T1c (41/41 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; lower third  •  ONLY when 1h trend AGAINST trade

### L21.  `H20=H20b AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is T1=T1c (41/41 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20b AND H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is T1=T1c (41/41 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; lower third  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20a AND T1=T1a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is T4=T4c (6/40 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20b AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is H60=H60e (34/36 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 strongly against

### L25.  `H20=H20b AND H60=H60e AND ZS=ZS2`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is T1=T1c (36/36 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(47/41) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
