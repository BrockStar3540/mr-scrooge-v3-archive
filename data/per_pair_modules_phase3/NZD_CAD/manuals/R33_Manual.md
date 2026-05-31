# NZD_CAD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,704**  (W=1,114 / L=590)  -  WR: **65.4%**

## Session distribution

- asia: n=505  W=336/L=169  WR=66.5%
- london_open: n=414  W=262/L=152  WR=63.3%
- ny_mid: n=239  W=167/L=72  WR=69.9%
- ny_close: n=160  W=103/L=57  WR=64.4%
- ny_open: n=138  W=93/L=45  WR=67.4%
- london: n=105  W=62/L=43  WR=59.0%
- off_hours: n=103  W=61/L=42  WR=59.2%
- asia_late: n=40  W=30/L=10  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=193  W=166/L=27  WR=86.0%
- Refine: exclude H60=H60a drops 18/27 losers (67%)
- **Final: n=108  W=99/L=9  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W02.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=190  W=162/L=28  WR=85.3%
- Refine: exclude session_bucket=off_hours drops 9/28 losers (32%)
- **Final: n=181  W=162/L=19  WR=89.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=off_hours

### W03.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=190  W=162/L=28  WR=85.3%
- Refine: exclude session_bucket=off_hours drops 9/28 losers (32%)
- **Final: n=181  W=162/L=19  WR=89.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=off_hours

### W04.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=171  W=146/L=25  WR=85.4%
- Refine: exclude RSI=RSI4 drops 16/25 losers (64%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W05.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=171  W=146/L=25  WR=85.4%
- Refine: exclude RSI=RSI4 drops 16/25 losers (64%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=170  W=146/L=24  WR=85.9%
- Refine: exclude session_bucket=off_hours drops 9/24 losers (38%)
- **Final: n=161  W=146/L=15  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W07.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=157  W=136/L=21  WR=86.6%
- Refine: exclude session_bucket=asia drops 10/21 losers (48%)
- **Final: n=128  W=117/L=11  WR=91.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when session=asia

### W08.  `H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=149  W=128/L=21  WR=85.9%
- Refine: exclude direction_exec=short drops 21/21 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when short

### W09.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=147  W=126/L=21  WR=85.7%
- Refine: exclude session_bucket=asia drops 10/21 losers (48%)
- **Final: n=118  W=107/L=11  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=asia

### W10.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude session_bucket=off_hours drops 9/21 losers (43%)
- **Final: n=136  W=124/L=12  WR=91.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=off_hours

### W11.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=140  W=122/L=18  WR=87.1%
- Refine: exclude session_bucket=off_hours drops 9/18 losers (50%)
- **Final: n=131  W=122/L=9  WR=93.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W12.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=134  W=114/L=20  WR=85.1%
- Refine: exclude session_bucket=asia drops 13/20 losers (65%)
- **Final: n=113  W=106/L=7  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=asia

### W13.  `H20=H20a AND H60=H60e AND session_bucket=asia`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude BBP=BBP5 drops 4/11 losers (36%)
- **Final: n=111  W=104/L=7  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=asia  •  AVOID when just touched upper band

### W14.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=122  W=108/L=14  WR=88.5%
- Refine: exclude BBP=BBP3 drops 5/14 losers (36%)
- **Final: n=107  W=98/L=9  WR=91.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  AVOID when middle of band

### W15.  `T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude RSI=RSI5 drops 13/16 losers (81%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W16.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude session_bucket=off_hours drops 5/16 losers (31%)
- **Final: n=105  W=94/L=11  WR=89.5%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W17.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude session_bucket=off_hours drops 5/16 losers (31%)
- **Final: n=103  W=92/L=11  WR=89.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W18.  `T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI5 drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W19.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI5 drops 13/14 losers (93%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W20.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude RSI=RSI4 drops 12/12 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W21.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W22.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W23.  `T1=T1c AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W24.  `H20=H20a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=97  W=88/L=9  WR=90.7%
- Refine: exclude RSI=RSI4 drops 6/9 losers (67%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when RSI 50-60 upper neutral

### W25.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude RSI=RSI4 drops 12/12 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (28/63 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L02.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is direction_exec=short (19/61 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when short

### L03.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is direction_exec=short (19/56 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when short

### L04.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=84  W=28/L=56  WR=33.3%
- Sharpen: sharpest is H60=H60e (48/56 of losers there)
- **Sharp: n=62  W=14/L=48  WR=22.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L05.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (21/52 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L06.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is session_bucket=off_hours (10/54 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=off_hours

### L07.  `H20=H20e AND H60=H60a AND session_bucket=asia`
- Raw: n=81  W=31/L=50  WR=38.3%
- Sharpen: sharpest is T4=T4a (20/50 of losers there)
- **Sharp: n=26  W=6/L=20  WR=23.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L08.  `H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=79  W=12/L=67  WR=15.2%
- Sharpen: sharpest is T1=T1c (37/67 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when 1h trend AGAINST trade

### L09.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=79  W=17/L=62  WR=21.5%
- Sharpen: sharpest is RSI=RSI5 (48/62 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is session_bucket=off_hours (10/47 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=off_hours

### L11.  `T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is session_bucket=off_hours (10/48 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band  •  ONLY when session=off_hours

### L12.  `H20=H20a AND H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is T1=T1c (21/48 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; upper third; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L13.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is session_bucket=off_hours (10/48 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=off_hours

### L14.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (19/45 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L15.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=72  W=24/L=48  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (37/48 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is T1=T1c (20/42 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L17.  `H20=H20a AND H60=H60e AND session_bucket=london_open`
- Raw: n=67  W=15/L=52  WR=22.4%
- Sharpen: sharpest is direction_exec=long (44/52 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  ONLY when long

### L18.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=67  W=15/L=52  WR=22.4%
- Sharpen: sharpest is direction_exec=long (44/52 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when long

### L19.  `H20=H20a AND T4=T4a AND BBP=BBP5`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is session_bucket=off_hours (10/42 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when session=off_hours

### L20.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is session_bucket=off_hours (10/42 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=off_hours

### L21.  `T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=off_hours (10/40 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when session=off_hours

### L22.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=off_hours (10/40 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=off_hours

### L23.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=off_hours (10/40 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when session=off_hours

### L24.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=62  W=14/L=48  WR=22.6%
- Sharpen: sharpest is direction_exec=short (25/48 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when short

### L25.  `T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is T1=T1c (14/40 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(50/43), H60b(8/3) | H60d(3/9), H60e(38/44) |
| T1 | — | — |
| T4 | T4c(54/45) | T4a(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
