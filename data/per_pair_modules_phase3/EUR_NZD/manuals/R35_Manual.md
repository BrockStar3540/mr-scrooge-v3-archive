# EUR_NZD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,991**  (W=3,027 / L=1,964)  -  WR: **60.6%**

## Session distribution

- asia: n=1432  W=898/L=534  WR=62.7%
- london_open: n=903  W=544/L=359  WR=60.2%
- london: n=762  W=464/L=298  WR=60.9%
- ny_open: n=634  W=374/L=260  WR=59.0%
- ny_mid: n=452  W=268/L=184  WR=59.3%
- asia_late: n=378  W=235/L=143  WR=62.2%
- ny_close: n=255  W=146/L=109  WR=57.3%
- off_hours: n=175  W=98/L=77  WR=56.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND T1=T1c AND RSI=RSI4`
- Raw: n=174  W=148/L=26  WR=85.1%
- Refine: exclude ZS=ZS3 drops 15/26 losers (58%)
- **Final: n=113  W=102/L=11  WR=90.3%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W02.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=171  W=149/L=22  WR=87.1%
- Refine: exclude session_bucket=ny_open drops 10/22 losers (45%)
- **Final: n=160  W=148/L=12  WR=92.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W03.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=166  W=149/L=17  WR=89.8%
- Refine: exclude session_bucket=ny_open drops 10/17 losers (59%)
- **Final: n=155  W=148/L=7  WR=95.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W04.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=147  W=129/L=18  WR=87.8%
- Refine: exclude T4=T4a drops 14/18 losers (78%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  AVOID when 4h trend WITH trade

### W05.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=138  W=121/L=17  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 10/17 losers (59%)
- **Final: n=127  W=120/L=7  WR=94.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W06.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=127  W=110/L=17  WR=86.6%
- Refine: exclude H20=H20d drops 9/17 losers (53%)
- **Final: n=106  W=98/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 mildly against

### W07.  `H20=H20c AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude ZS=ZS3 drops 11/18 losers (61%)
- **Final: n=78  W=71/L=7  WR=91.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W08.  `T4=T4c AND ZS=ZS5 AND session_bucket=london`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude RSI=RSI4 drops 16/16 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=112  W=99/L=13  WR=88.4%
- Refine: exclude session_bucket=ny_open drops 5/13 losers (38%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_open

### W10.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=109  W=100/L=9  WR=91.7%
- Refine: exclude T1=T1c drops 6/9 losers (67%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W11.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude session_bucket=ny_open drops 5/9 losers (56%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W12.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude session_bucket=ny_open drops 5/9 losers (56%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W13.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=106  W=94/L=12  WR=88.7%
- Refine: exclude BBP=BBP5 drops 12/12 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W14.  `T4=T4a AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=101  W=90/L=11  WR=89.1%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W15.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 6/12 losers (50%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=asia  •  AVOID when HTF20 strongly against

### W16.  `H20=H20c AND T1=T1c AND session_bucket=asia`
- Raw: n=96  W=92/L=4  WR=95.8%
- Refine: exclude BBP=BBP2 drops 4/4 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W17.  `H20=H20c AND direction_exec=short AND session_bucket=asia`
- Raw: n=96  W=92/L=4  WR=95.8%
- Refine: exclude BBP=BBP2 drops 4/4 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; session=asia  •  AVOID when lower third

### W18.  `H20=H20c AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=96  W=92/L=4  WR=95.8%
- Refine: exclude BBP=BBP2 drops 4/4 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W19.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=94  W=88/L=6  WR=93.6%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W20.  `H20=H20c AND H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4a drops 4/13 losers (31%)
- **Final: n=88  W=79/L=9  WR=89.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude T4=T4a drops 4/10 losers (40%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20a AND T4=T4c AND session_bucket=asia_late`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude H60=H60e drops 9/11 losers (82%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when HTF60 strongly against

### W23.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude H60=H60e drops 9/11 losers (82%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia_late  •  AVOID when HTF60 strongly against

### W24.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude H60=H60e drops 9/11 losers (82%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when HTF60 strongly against

### W25.  `H20=H20c AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude session_bucket=ny_open drops 5/9 losers (56%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=312  W=113/L=199  WR=36.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=312  W=113/L=199  WR=36.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral

### L02.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=263  W=86/L=177  WR=32.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=263  W=86/L=177  WR=32.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L03.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=235  W=85/L=150  WR=36.2%
- Sharpen: sharpest is ZS=ZS4 (63/150 of losers there)
- **Sharp: n=78  W=15/L=63  WR=19.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L04.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=217  W=86/L=131  WR=39.6%
- Sharpen: sharpest is H60=H60a (63/131 of losers there)
- **Sharp: n=81  W=18/L=63  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L05.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=190  W=76/L=114  WR=40.0%
- Sharpen: sharpest is H20=H20e (33/114 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=180  W=55/L=125  WR=30.6%
- Sharpen: sharpest is BBP=BBP6 (39/125 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L07.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is T1=T1a (46/105 of losers there)
- **Sharp: n=53  W=7/L=46  WR=13.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L08.  `H60=H60a AND T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=157  W=62/L=95  WR=39.5%
- Sharpen: sharpest is H20=H20e (60/95 of losers there)
- **Sharp: n=78  W=18/L=60  WR=23.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L09.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=150  W=53/L=97  WR=35.3%
- Sharpen: sharpest is T1=T1a (40/97 of losers there)
- **Sharp: n=52  W=12/L=40  WR=23.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20e AND H60=H60a AND session_bucket=ny_open`
- Raw: n=150  W=57/L=93  WR=38.0%
- Sharpen: sharpest is T1=T1a (53/93 of losers there)
- **Sharp: n=74  W=21/L=53  WR=28.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L11.  `H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=146  W=55/L=91  WR=37.7%
- Sharpen: sharpest is direction_exec=short (56/91 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  ONLY when short

### L12.  `H20=H20e AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=146  W=58/L=88  WR=39.7%
- Sharpen: sharpest is ZS=ZS4 (85/88 of losers there)
- **Sharp: n=119  W=34/L=85  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L13.  `H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is ZS=ZS5 (33/86 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=138  W=31/L=107  WR=22.5%
- Sharpen: sharpest is BBP=BBP6 (33/107 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L15.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=138  W=55/L=83  WR=39.9%
- Sharpen: sharpest is T4=T4c (37/83 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20c AND T1=T1a AND RSI=RSI4`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is ZS=ZS4 (38/83 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L17.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=128  W=44/L=84  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=44/L=84  WR=34.4%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral

### L18.  `H20=H20e AND H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: sharpest is T4=T4c (63/77 of losers there)
- **Sharp: n=78  W=15/L=63  WR=19.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=127  W=46/L=81  WR=36.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L20.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is direction_exec=short (46/78 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  ONLY when short

### L21.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=126  W=40/L=86  WR=31.7%
- Sharpen: sharpest is T4=T4a (45/86 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L22.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is ZS=ZS5 (14/79 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=124  W=48/L=76  WR=38.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=london_open

### L24.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is T1=T1a (21/78 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is T1=T1a (36/76 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(41/35) | H20e(33/41) |
| H60 | — | — |
| T1 | T1c(52/46) | T1a(47/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
