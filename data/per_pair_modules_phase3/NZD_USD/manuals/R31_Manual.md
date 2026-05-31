# NZD_USD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,509**  (W=2,274 / L=1,235)  -  WR: **64.8%**

## Session distribution

- asia: n=900  W=588/L=312  WR=65.3%
- ny_mid: n=836  W=535/L=301  WR=64.0%
- london_open: n=543  W=346/L=197  WR=63.7%
- ny_open: n=499  W=333/L=166  WR=66.7%
- ny_close: n=288  W=195/L=93  WR=67.7%
- london: n=226  W=144/L=82  WR=63.7%
- asia_late: n=129  W=87/L=42  WR=67.4%
- off_hours: n=88  W=46/L=42  WR=52.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=153  W=132/L=21  WR=86.3%
- Refine: exclude BBP=BBP2 drops 9/21 losers (43%)
- **Final: n=126  W=114/L=12  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W02.  `H20=H20e AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=129  W=114/L=15  WR=88.4%
- Refine: exclude ZS=ZS4 drops 11/15 losers (73%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W03.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude session_bucket=asia_late drops 5/18 losers (28%)
- **Final: n=120  W=107/L=13  WR=89.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W04.  `ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude BBP=BBP5 drops 14/17 losers (82%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W05.  `T1=T1c AND T4=T4c AND session_bucket=london`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W06.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W07.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude ZS=ZS4 drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W08.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W09.  `H20=H20e AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H60=H60a drops 11/16 losers (69%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; RSI 60-70 strong  •  AVOID when HTF60 aligned WITH trade

### W10.  `H20=H20e AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude direction_exec=short drops 14/15 losers (93%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when short

### W11.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W13.  `T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude H60=H60e drops 8/15 losers (53%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF60 strongly against

### W14.  `T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude H60=H60e drops 8/15 losers (53%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF60 strongly against

### W15.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude H60=H60e drops 8/15 losers (53%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF60 strongly against

### W16.  `H20=H20a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude BBP=BBP5 drops 12/15 losers (80%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W17.  `H60=H60e AND RSI=RSI5 AND session_bucket=london`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london  •  AVOID when HTF20 aligned WITH trade

### W18.  `H20=H20a AND T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude BBP=BBP5 drops 12/15 losers (80%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W19.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude BBP=BBP5 drops 12/15 losers (80%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W20.  `H20=H20a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude BBP=BBP5 drops 12/15 losers (80%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W21.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude session_bucket=london_open drops 10/13 losers (77%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  AVOID when session=london_open

### W22.  `H60=H60e AND T1=T1c AND session_bucket=london`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W23.  `T1=T1c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london  •  AVOID when HTF20 aligned WITH trade

### W24.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is BBP=BBP6 (20/77 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when deep above upper band

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=120  W=45/L=75  WR=37.5%
- Sharpen: sharpest is H20=H20a (17/75 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=111  W=38/L=73  WR=34.2%
- Sharpen: sharpest is BBP=BBP2 (23/73 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when lower third

### L04.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is H60=H60e (34/65 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L05.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is BBP=BBP2 (23/65 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when lower third

### L06.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (25/67 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L07.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (25/67 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L08.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is T1=T1c (17/60 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L09.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (19/57 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; upper third  •  ONLY when session=asia

### L10.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=asia (26/58 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L11.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=79  W=23/L=56  WR=29.1%
- Sharpen: sharpest is T1=T1c (47/56 of losers there)
- **Sharp: n=59  W=12/L=47  WR=20.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L12.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=79  W=25/L=54  WR=31.6%
- Sharpen: sharpest is H20=H20a (35/54 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L13.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=79  W=25/L=54  WR=31.6%
- Sharpen: sharpest is H20=H20a (35/54 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L14.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=79  W=25/L=54  WR=31.6%
- Sharpen: sharpest is H20=H20a (35/54 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L15.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is session_bucket=asia (19/49 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L16.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T4=T4a (31/48 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20e AND H60=H60e AND BBP=BBP6`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (20/49 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  ONLY when session=asia

### L18.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (20/49 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L19.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (20/49 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  ONLY when session=asia

### L20.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (47/52 of losers there)
- **Sharp: n=59  W=12/L=47  WR=20.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is BBP=BBP3 (11/46 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when middle of band

### L22.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (31/46 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L23.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (31/46 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L24.  `BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is H60=H60e (26/47 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: SHORT**  •  deep above upper band; session=asia  •  ONLY when HTF60 strongly against

### L25.  `H20=H20a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is T1=T1a (32/43 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=london  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/40) | H20e(38/46) |
| H60 | H60a(51/44) | H60e(43/51) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
