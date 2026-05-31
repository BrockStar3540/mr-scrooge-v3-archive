# AUD_CAD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,322**  (W=2,152 / L=1,170)  -  WR: **64.8%**

## Session distribution

- asia: n=869  W=564/L=305  WR=64.9%
- london_open: n=632  W=421/L=211  WR=66.6%
- ny_mid: n=543  W=361/L=182  WR=66.5%
- ny_open: n=528  W=333/L=195  WR=63.1%
- ny_close: n=262  W=167/L=95  WR=63.7%
- london: n=249  W=151/L=98  WR=60.6%
- asia_late: n=149  W=97/L=52  WR=65.1%
- off_hours: n=90  W=58/L=32  WR=64.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W02.  `H20=H20b AND H60=H60b AND T4=T4a`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude BBP=BBP4 drops 9/9 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when upper third

### W03.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude BBP=BBP4 drops 9/9 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when upper third

### W04.  `H20=H20b AND H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude BBP=BBP4 drops 9/9 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when upper third

### W05.  `H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W06.  `H20=H20b AND H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W07.  `H60=H60b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W08.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=78  W=73/L=5  WR=93.6%
- Refine: exclude direction_exec=long drops 5/5 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when long

### W09.  `T1=T1a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W10.  `BBP=BBP2 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: LONG**  •  lower third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W11.  `T1=T1a AND BBP=BBP2 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W12.  `T4=T4a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W13.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W14.  `T4=T4a AND BBP=BBP2 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/6 losers (33%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 60-70 strong  •  AVOID when strategy=delta_tag_and_go_v2

### W16.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/6 losers (33%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when strategy=delta_tag_and_go_v2

### W17.  `H60=H60a AND BBP=BBP2 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/6 losers (33%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 60-70 strong  •  AVOID when strategy=delta_tag_and_go_v2

### W18.  `H20=H20c AND H60=H60a AND session_bucket=asia`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude ZS=ZS6 drops 5/10 losers (50%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore >+3 extreme

### W19.  `H20=H20c AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude ZS=ZS6 drops 5/10 losers (50%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore >+3 extreme

### W20.  `H20=H20c AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude ZS=ZS6 drops 5/10 losers (50%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore >+3 extreme

### W21.  `H20=H20c AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude ZS=ZS6 drops 5/10 losers (50%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore >+3 extreme

### W22.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/6 losers (33%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when strategy=delta_tag_and_go_v2

### W23.  `H20=H20c AND H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS6 drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore >+3 extreme

### W24.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=59  W=53/L=6  WR=89.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 mildly against

### W25.  `BBP=BBP3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude H60=H60a drops 9/9 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: LONG**  •  middle of band; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is BBP=BBP4 (20/40 of losers there)
- **Sharp: n=29  W=9/L=20  WR=31.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london  •  ONLY when upper third

### L02.  `H20=H20d AND H60=H60d AND T4=T4c`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L03.  `H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L04.  `H20=H20d AND H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L05.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L06.  `H20=H20d AND H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L07.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L08.  `H20=H20c AND T1=T1c AND session_bucket=asia`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=20/L=39  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia

### L09.  `H20=H20c AND T4=T4c AND session_bucket=asia`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=20/L=39  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; session=asia

### L10.  `H20=H20c AND direction_exec=short AND session_bucket=asia`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=20/L=39  WR=33.9%**
- **Dir: SHORT**  •  HTF20 neutral; session=asia

### L11.  `H20=H20c AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=20/L=39  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L12.  `H20=H20c AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=20/L=39  WR=33.9%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia

### L13.  `H20=H20c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=20/L=39  WR=33.9%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade; session=asia

### L14.  `H20=H20e AND RSI=RSI4 AND session_bucket=london`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=58  W=22/L=36  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london

### L15.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=london`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=58  W=22/L=36  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=london

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=58  W=22/L=36  WR=37.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london

### L17.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=58  W=22/L=36  WR=37.9%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london

### L18.  `H20=H20c AND H60=H60e AND session_bucket=asia`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=asia

### L19.  `H20=H20c AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; session=asia

### L20.  `H20=H20c AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade; session=asia

### L21.  `H20=H20c AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; session=asia

### L22.  `H20=H20c AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 60-70 strong; session=asia

### L23.  `H20=H20c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 60-70 strong; session=asia

### L24.  `H20=H20c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 60-70 strong; session=asia

### L25.  `H20=H20c AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=55  W=20/L=35  WR=36.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 60-70 strong; session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/45) | T4c(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
