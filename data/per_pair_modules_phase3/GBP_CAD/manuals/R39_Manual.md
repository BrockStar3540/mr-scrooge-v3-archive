# GBP_CAD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,023**  (W=2,586 / L=1,437)  -  WR: **64.3%**

## Session distribution

- asia: n=1783  W=1170/L=613  WR=65.6%
- london_open: n=575  W=363/L=212  WR=63.1%
- asia_late: n=477  W=296/L=181  WR=62.1%
- ny_close: n=418  W=270/L=148  WR=64.6%
- london: n=347  W=226/L=121  WR=65.1%
- off_hours: n=182  W=109/L=73  WR=59.9%
- ny_open: n=168  W=103/L=65  WR=61.3%
- ny_mid: n=73  W=49/L=24  WR=67.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND RSI=RSI4`
- Raw: n=274  W=233/L=41  WR=85.0%
- Refine: exclude ZS=ZS2 drops 11/41 losers (27%)
- **Final: n=237  W=207/L=30  WR=87.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W02.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=222  W=190/L=32  WR=85.6%
- Refine: exclude BBP=BBP4 drops 22/32 losers (69%)
- **Final: n=133  W=123/L=10  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when upper third

### W03.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=196  W=167/L=29  WR=85.2%
- Refine: exclude ZS=ZS1 drops 10/29 losers (34%)
- **Final: n=182  W=163/L=19  WR=89.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when zscore -3 to -2 deep oversold

### W04.  `H20=H20b AND H60=H60a AND direction_exec=long`
- Raw: n=192  W=168/L=24  WR=87.5%
- Refine: exclude BBP=BBP4 drops 16/24 losers (67%)
- **Final: n=123  W=115/L=8  WR=93.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when upper third

### W05.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=192  W=168/L=24  WR=87.5%
- Refine: exclude BBP=BBP4 drops 16/24 losers (67%)
- **Final: n=123  W=115/L=8  WR=93.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when upper third

### W06.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=191  W=167/L=24  WR=87.4%
- Refine: exclude ZS=ZS2 drops 9/24 losers (38%)
- **Final: n=172  W=157/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W07.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: exclude T4=T4c drops 17/24 losers (71%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude BBP=BBP4 drops 16/21 losers (76%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W09.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude BBP=BBP4 drops 16/21 losers (76%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W10.  `H20=H20b AND T1=T1a AND ZS=ZS3`
- Raw: n=147  W=126/L=21  WR=85.7%
- Refine: exclude session_bucket=off_hours drops 8/21 losers (38%)
- **Final: n=123  W=110/L=13  WR=89.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W11.  `H20=H20b AND T1=T1a AND T4=T4c`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H60=H60c drops 8/19 losers (42%)
- **Final: n=127  W=116/L=11  WR=91.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 neutral

### W12.  `H20=H20b AND ZS=ZS3 AND direction_exec=long`
- Raw: n=137  W=117/L=20  WR=85.4%
- Refine: exclude H60=H60e drops 7/20 losers (35%)
- **Final: n=114  W=101/L=13  WR=88.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W13.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude BBP=BBP4 drops 12/19 losers (63%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when upper third

### W14.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude BBP=BBP4 drops 12/19 losers (63%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when upper third

### W15.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude BBP=BBP4 drops 12/19 losers (63%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when upper third

### W16.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=132  W=118/L=14  WR=89.4%
- Refine: exclude RSI=RSI5 drops 9/14 losers (64%)
- **Final: n=109  W=104/L=5  WR=95.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W17.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W18.  `H20=H20b AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=off_hours drops 8/18 losers (44%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W19.  `H20=H20b AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=122  W=105/L=17  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 8/17 losers (47%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W20.  `H60=H60a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude T1=T1c drops 18/18 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W21.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude T1=T1c drops 18/18 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W22.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H60=H60e drops 9/18 losers (50%)
- **Final: n=95  W=86/L=9  WR=90.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W23.  `T4=T4a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H60=H60e drops 9/18 losers (50%)
- **Final: n=95  W=86/L=9  WR=90.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W24.  `H20=H20a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF60 strongly against

### W25.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude RSI=RSI5 drops 9/14 losers (64%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 60-70 strong

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20c AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: sharpest is ZS=ZS5 (42/103 of losers there)
- **Sharp: n=52  W=10/L=42  WR=19.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H20=H20d AND H60=H60e AND T4=T4c`
- Raw: n=160  W=61/L=99  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (32/99 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L03.  `H20=H20d AND T4=T4c AND RSI=RSI5`
- Raw: n=157  W=58/L=99  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=58/L=99  WR=36.9%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong

### L04.  `H20=H20d AND H60=H60e AND direction_exec=short`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=141  W=55/L=86  WR=39.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against

### L05.  `H20=H20d AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=141  W=55/L=86  WR=39.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade

### L06.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=130  W=50/L=80  WR=38.5%
- Sharpen: sharpest is BBP=BBP6 (22/80 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia_late  •  ONLY when deep above upper band

### L07.  `H20=H20d AND T1=T1c AND RSI=RSI5`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=47/L=79  WR=37.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong

### L08.  `H20=H20d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=47/L=79  WR=37.3%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 60-70 strong

### L09.  `H20=H20d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=47/L=79  WR=37.3%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong

### L10.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is ZS=ZS5 (24/78 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H20=H20d AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=121  W=45/L=76  WR=37.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=121  W=45/L=76  WR=37.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade

### L12.  `H20=H20d AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=121  W=45/L=76  WR=37.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=121  W=45/L=76  WR=37.2%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade

### L13.  `H20=H20d AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=46/L=73  WR=38.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L14.  `H20=H20d AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=46/L=73  WR=38.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong

### L15.  `H20=H20d AND H60=H60e AND RSI=RSI5`
- Raw: n=118  W=41/L=77  WR=34.7%
- Sharpen: sharpest is ZS=ZS5 (29/77 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60b AND T1=T1a AND BBP=BBP4`
- Raw: n=117  W=45/L=72  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (21/72 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; upper third  •  ONLY when session=london_open

### L17.  `H20=H20d AND T4=T4c AND ZS=ZS3`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=42/L=70  WR=37.5%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore -1 to +1 neutral

### L18.  `H60=H60b AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (21/68 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; upper third  •  ONLY when session=london_open

### L19.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is BBP=BBP6 (22/68 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia_late  •  ONLY when deep above upper band

### L20.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_open (14/64 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  ONLY when session=ny_open

### L21.  `H20=H20d AND ZS=ZS3 AND direction_exec=short`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=39/L=63  WR=38.2%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore -1 to +1 neutral

### L22.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is BBP=BBP6 (22/60 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia_late  •  ONLY when deep above upper band

### L23.  `H60=H60b AND T1=T1a AND ZS=ZS4`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (18/60 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L24.  `H60=H60b AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (18/60 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L25.  `H20=H20e AND direction_exec=long AND session_bucket=asia`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is RSI=RSI4 (47/60 of losers there)
- **Sharp: n=60  W=13/L=47  WR=21.7%**
- **Dir: LONG**  •  HTF20 strongly against; session=asia  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(22/14), H20a(28/22) | H20d(14/21), H20e(21/28) |
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
