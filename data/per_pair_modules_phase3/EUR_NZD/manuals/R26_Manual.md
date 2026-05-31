# EUR_NZD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,949**  (W=2,694 / L=2,255)  -  WR: **54.4%**

## Session distribution

- ny_mid: n=1596  W=835/L=761  WR=52.3%
- asia: n=1514  W=837/L=677  WR=55.3%
- ny_open: n=541  W=305/L=236  WR=56.4%
- ny_close: n=518  W=288/L=230  WR=55.6%
- london: n=356  W=203/L=153  WR=57.0%
- off_hours: n=205  W=110/L=95  WR=53.7%
- london_open: n=155  W=85/L=70  WR=54.8%
- asia_late: n=64  W=31/L=33  WR=48.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=135  W=121/L=14  WR=89.6%
- Refine: exclude direction_exec=long drops 14/14 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when long

### W02.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude direction_exec=long drops 14/14 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when long

### W03.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude direction_exec=long drops 14/14 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when long

### W04.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude H20=H20b drops 2/2 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W05.  `T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude H20=H20c drops 7/7 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 neutral

### W06.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_mid drops 7/10 losers (70%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W07.  `T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=72  W=72/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band

### W08.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=72  W=72/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band

### W09.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=72  W=72/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band

### W10.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude H20=H20c drops 7/7 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W11.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; deep above upper band

### W12.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; deep above upper band

### W13.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band

### W14.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=66  W=66/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought

### W15.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=65  W=60/L=5  WR=92.3%
- Refine: exclude T1=T1c drops 4/5 losers (80%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W16.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=61  W=59/L=2  WR=96.7%
- Refine: no further refinement
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_open

### W17.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=61  W=59/L=2  WR=96.7%
- Refine: no further refinement
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=ny_open

### W18.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=61  W=59/L=2  WR=96.7%
- Refine: no further refinement
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_open

### W19.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude BBP=BBP0 drops 5/5 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when deep below lower band

### W20.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude T1=T1c drops 4/6 losers (67%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W21.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=59  W=54/L=5  WR=91.5%
- Refine: exclude BBP=BBP3 drops 5/5 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when middle of band

### W22.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=59  W=54/L=5  WR=91.5%
- Refine: exclude BBP=BBP3 drops 5/5 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when middle of band

### W23.  `H20=H20c AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=ny_mid  •  AVOID when 1h trend WITH trade

### W24.  `H20=H20c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; session=ny_mid  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=346  W=106/L=240  WR=30.6%
- Sharpen: sharpest is H60=H60e (162/240 of losers there)
- **Sharp: n=194  W=32/L=162  WR=16.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L02.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=320  W=122/L=198  WR=38.1%
- Sharpen: sharpest is H60=H60e (94/198 of losers there)
- **Sharp: n=115  W=21/L=94  WR=18.3%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L03.  `H20=H20e AND H60=H60e AND ZS=ZS5`
- Raw: n=307  W=115/L=192  WR=37.5%
- Sharpen: sharpest is T4=T4c (162/192 of losers there)
- **Sharp: n=194  W=32/L=162  WR=16.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=276  W=98/L=178  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=276  W=98/L=178  WR=35.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought

### L05.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=276  W=98/L=178  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=276  W=98/L=178  WR=35.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought

### L06.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=276  W=98/L=178  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=276  W=98/L=178  WR=35.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought

### L07.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=276  W=98/L=178  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=276  W=98/L=178  WR=35.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought

### L08.  `H20=H20e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=268  W=105/L=163  WR=39.2%
- Sharpen: sharpest is T4=T4c (113/163 of losers there)
- **Sharp: n=125  W=12/L=113  WR=9.6%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=263  W=105/L=158  WR=39.9%
- Sharpen: sharpest is T4=T4c (108/158 of losers there)
- **Sharp: n=120  W=12/L=108  WR=10.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L10.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=245  W=95/L=150  WR=38.8%
- Sharpen: sharpest is H60=H60e (78/150 of losers there)
- **Sharp: n=92  W=14/L=78  WR=15.2%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L11.  `H20=H20e AND H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=238  W=95/L=143  WR=39.9%
- Sharpen: sharpest is T4=T4c (113/143 of losers there)
- **Sharp: n=125  W=12/L=113  WR=9.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=237  W=87/L=150  WR=36.7%
- Sharpen: sharpest is T4=T4c (78/150 of losers there)
- **Sharp: n=92  W=14/L=78  WR=15.2%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=231  W=78/L=153  WR=33.8%
- Sharpen: sharpest is T1=T1a (71/153 of losers there)
- **Sharp: n=83  W=12/L=71  WR=14.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L14.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=219  W=86/L=133  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=86/L=133  WR=39.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia

### L15.  `H60=H60e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=215  W=82/L=133  WR=38.1%
- Sharpen: sharpest is T4=T4c (46/133 of losers there)
- **Sharp: n=46  W=0/L=46  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; deep above upper band  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20e AND T1=T1c AND ZS=ZS5`
- Raw: n=210  W=79/L=131  WR=37.6%
- Sharpen: sharpest is RSI=RSI6 (34/131 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L17.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=210  W=79/L=131  WR=37.6%
- Sharpen: sharpest is RSI=RSI6 (34/131 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L18.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=207  W=35/L=172  WR=16.9%
- Sharpen: sharpest is direction_exec=long (113/172 of losers there)
- **Sharp: n=125  W=12/L=113  WR=9.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when long

### L19.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=205  W=79/L=126  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (34/126 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L20.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=204  W=77/L=127  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_open (28/127 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when session=ny_open

### L21.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=204  W=77/L=127  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_open (28/127 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 60-70 strong  •  ONLY when session=ny_open

### L22.  `H20=H20e AND T4=T4c AND BBP=BBP5`
- Raw: n=203  W=70/L=133  WR=34.5%
- Sharpen: sharpest is H60=H60e (94/133 of losers there)
- **Sharp: n=112  W=18/L=94  WR=16.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=203  W=70/L=133  WR=34.5%
- Sharpen: sharpest is H60=H60e (94/133 of losers there)
- **Sharp: n=112  W=18/L=94  WR=16.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L24.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=201  W=77/L=124  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=201  W=77/L=124  WR=38.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 60-70 strong

### L25.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=201  W=77/L=124  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=201  W=77/L=124  WR=38.3%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 60-70 strong

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
| direction_exec | long(52/47) | short(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
