# GBP_CAD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,298**  (W=2,604 / L=1,694)  -  WR: **60.6%**

## Session distribution

- london_open: n=993  W=607/L=386  WR=61.1%
- ny_close: n=955  W=582/L=373  WR=60.9%
- ny_open: n=730  W=406/L=324  WR=55.6%
- ny_mid: n=630  W=395/L=235  WR=62.7%
- london: n=469  W=297/L=172  WR=63.3%
- asia: n=351  W=212/L=139  WR=60.4%
- off_hours: n=137  W=83/L=54  WR=60.6%
- asia_late: n=33  W=22/L=11  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=291  W=257/L=34  WR=88.3%
- Refine: exclude H20=H20a drops 21/34 losers (62%)
- **Final: n=182  W=169/L=13  WR=92.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=235  W=201/L=34  WR=85.5%
- Refine: exclude ZS=ZS3 drops 13/34 losers (38%)
- **Final: n=197  W=176/L=21  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W03.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=178  W=153/L=25  WR=86.0%
- Refine: exclude H60=H60a drops 19/25 losers (76%)
- **Final: n=122  W=116/L=6  WR=95.1%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  AVOID when HTF60 aligned WITH trade

### W04.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: exclude session_bucket=london_open drops 12/24 losers (50%)
- **Final: n=128  W=116/L=12  WR=90.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when session=london_open

### W05.  `H20=H20a AND H60=H60d AND direction_exec=short`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: exclude session_bucket=london_open drops 12/24 losers (50%)
- **Final: n=128  W=116/L=12  WR=90.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when session=london_open

### W06.  `H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: exclude session_bucket=london_open drops 12/24 losers (50%)
- **Final: n=128  W=116/L=12  WR=90.6%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade  •  AVOID when session=london_open

### W07.  `H20=H20a AND H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: exclude session_bucket=london_open drops 12/24 losers (50%)
- **Final: n=128  W=116/L=12  WR=90.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when session=london_open

### W08.  `T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude H60=H60e drops 12/18 losers (67%)
- **Final: n=112  W=106/L=6  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when HTF60 strongly against

### W09.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=160  W=142/L=18  WR=88.8%
- Refine: exclude ZS=ZS3 drops 7/18 losers (39%)
- **Final: n=142  W=131/L=11  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W10.  `H60=H60d AND T1=T1a AND T4=T4c`
- Raw: n=153  W=135/L=18  WR=88.2%
- Refine: exclude BBP=BBP4 drops 8/18 losers (44%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when upper third

### W11.  `H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=153  W=135/L=18  WR=88.2%
- Refine: exclude BBP=BBP4 drops 8/18 losers (44%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when upper third

### W12.  `H20=H20a AND H60=H60d AND T1=T1a AND T4=T4c`
- Raw: n=153  W=135/L=18  WR=88.2%
- Refine: exclude BBP=BBP4 drops 8/18 losers (44%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when upper third

### W13.  `H20=H20a AND H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=153  W=135/L=18  WR=88.2%
- Refine: exclude BBP=BBP4 drops 8/18 losers (44%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when upper third

### W14.  `H60=H60d AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=153  W=135/L=18  WR=88.2%
- Refine: exclude BBP=BBP4 drops 8/18 losers (44%)
- **Final: n=128  W=118/L=10  WR=92.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when upper third

### W15.  `H20=H20a AND direction_exec=short AND session_bucket=london`
- Raw: n=150  W=134/L=16  WR=89.3%
- Refine: exclude H60=H60a drops 10/16 losers (62%)
- **Final: n=98  W=92/L=6  WR=93.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london  •  AVOID when HTF60 aligned WITH trade

### W16.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=150  W=128/L=22  WR=85.3%
- Refine: exclude RSI=RSI3 drops 11/22 losers (50%)
- **Final: n=125  W=114/L=11  WR=91.2%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W17.  `T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=149  W=130/L=19  WR=87.2%
- Refine: exclude H60=H60a drops 13/19 losers (68%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when HTF60 aligned WITH trade

### W18.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=149  W=128/L=21  WR=85.9%
- Refine: exclude H60=H60a drops 13/21 losers (62%)
- **Final: n=116  W=108/L=8  WR=93.1%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london  •  AVOID when HTF60 aligned WITH trade

### W19.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude H60=H60a drops 13/19 losers (68%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when HTF60 aligned WITH trade

### W20.  `H20=H20a AND H60=H60d AND T4=T4c AND RSI=RSI2`
- Raw: n=141  W=120/L=21  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 11/21 losers (52%)
- **Final: n=126  W=116/L=10  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=ny_open

### W21.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude T1=T1c drops 20/21 losers (95%)
- **Final: n=99  W=98/L=1  WR=99.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when 1h trend AGAINST trade

### W22.  `H60=H60d AND T1=T1a AND RSI=RSI2`
- Raw: n=139  W=122/L=17  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 4/17 losers (24%)
- **Final: n=135  W=122/L=13  WR=90.4%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_open

### W23.  `H60=H60d AND RSI=RSI2 AND direction_exec=short`
- Raw: n=139  W=122/L=17  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 4/17 losers (24%)
- **Final: n=135  W=122/L=13  WR=90.4%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 30-40 weak  •  AVOID when session=ny_open

### W24.  `H20=H20a AND H60=H60d AND T1=T1a AND RSI=RSI2`
- Raw: n=139  W=122/L=17  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 4/17 losers (24%)
- **Final: n=135  W=122/L=13  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_open

### W25.  `H20=H20a AND H60=H60d AND RSI=RSI2 AND direction_exec=short`
- Raw: n=139  W=122/L=17  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 4/17 losers (24%)
- **Final: n=135  W=122/L=13  WR=90.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 30-40 weak  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=394  W=156/L=238  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=394  W=156/L=238  WR=39.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=320  W=115/L=205  WR=35.9%
- Sharpen: sharpest is T4=T4c (146/205 of losers there)
- **Sharp: n=188  W=42/L=146  WR=22.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L03.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=294  W=114/L=180  WR=38.8%
- Sharpen: sharpest is T1=T1c (146/180 of losers there)
- **Sharp: n=188  W=42/L=146  WR=22.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  ONLY when 1h trend AGAINST trade

### L04.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=212  W=66/L=146  WR=31.1%
- Sharpen: sharpest is direction_exec=long (146/146 of losers there)
- **Sharp: n=188  W=42/L=146  WR=22.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when long

### L05.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=194  W=70/L=124  WR=36.1%
- Sharpen: sharpest is session_bucket=london_open (46/124 of losers there)
- **Sharp: n=54  W=8/L=46  WR=14.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L06.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=188  W=42/L=146  WR=22.3%
- Sharpen: sharpest is RSI=RSI2 (56/146 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L07.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=187  W=68/L=119  WR=36.4%
- Sharpen: sharpest is session_bucket=london_open (50/119 of losers there)
- **Sharp: n=58  W=8/L=50  WR=13.8%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L08.  `H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=178  W=48/L=130  WR=27.0%
- Sharpen: sharpest is RSI=RSI1 (38/130 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: LONG**  •  HTF60 strongly against; session=london_open  •  ONLY when RSI 20-30 oversold

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=164  W=64/L=100  WR=39.0%
- Sharpen: sharpest is session_bucket=london_open (22/100 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L10.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=163  W=60/L=103  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (36/103 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L11.  `ZS=ZS1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=161  W=55/L=106  WR=34.2%
- Sharpen: sharpest is H20=H20e (50/106 of losers there)
- **Sharp: n=58  W=8/L=50  WR=13.8%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is T4=T4a (57/102 of losers there)
- **Sharp: n=73  W=16/L=57  WR=21.9%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20b AND T1=T1c AND RSI=RSI2`
- Raw: n=159  W=56/L=103  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=56/L=103  WR=35.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak

### L14.  `H20=H20b AND RSI=RSI2 AND direction_exec=long`
- Raw: n=159  W=56/L=103  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=56/L=103  WR=35.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 30-40 weak

### L15.  `H20=H20b AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=159  W=56/L=103  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=56/L=103  WR=35.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak

### L16.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=158  W=42/L=116  WR=26.6%
- Sharpen: sharpest is T4=T4c (82/116 of losers there)
- **Sharp: n=101  W=19/L=82  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L17.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=157  W=51/L=106  WR=32.5%
- Sharpen: sharpest is T1=T1c (82/106 of losers there)
- **Sharp: n=101  W=19/L=82  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when 1h trend AGAINST trade

### L18.  `T1=T1c AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=157  W=60/L=97  WR=38.2%
- Sharpen: sharpest is H20=H20e (36/97 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF20 strongly against

### L19.  `H20=H20e AND H60=H60b AND T4=T4a`
- Raw: n=155  W=59/L=96  WR=38.1%
- Sharpen: sharpest is BBP=BBP1 (34/96 of losers there)
- **Sharp: n=35  W=1/L=34  WR=2.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when just touched lower band

### L20.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=155  W=60/L=95  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (28/95 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L21.  `T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=153  W=55/L=98  WR=35.9%
- Sharpen: sharpest is T4=T4a (63/98 of losers there)
- **Sharp: n=80  W=17/L=63  WR=21.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london  •  ONLY when 4h trend WITH trade

### L22.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=150  W=53/L=97  WR=35.3%
- Sharpen: sharpest is T4=T4c (56/97 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20e AND H60=H60b AND RSI=RSI2`
- Raw: n=144  W=54/L=90  WR=37.5%
- Sharpen: sharpest is session_bucket=london (51/90 of losers there)
- **Sharp: n=66  W=15/L=51  WR=22.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; RSI 30-40 weak  •  ONLY when session=london

### L24.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is T4=T4a (37/91 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L25.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is T4=T4a (37/91 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(33/21) | H20e(21/35) |
| H60 | H60a(40/32) | H60e(31/39) |
| T1 | T1a(58/41) | T1c(42/59) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/44) | long(44/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
