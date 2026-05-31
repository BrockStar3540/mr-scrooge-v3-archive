# EUR_CHF — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,397**  (W=925 / L=472)  -  WR: **66.2%**

## Session distribution

- ny_mid: n=527  W=368/L=159  WR=69.8%
- ny_open: n=230  W=143/L=87  WR=62.2%
- london: n=215  W=130/L=85  WR=60.5%
- london_open: n=213  W=141/L=72  WR=66.2%
- ny_close: n=120  W=82/L=38  WR=68.3%
- asia: n=54  W=37/L=17  WR=68.5%
- off_hours: n=29  W=20/L=9  WR=69.0%
- asia_late: n=9  W=4/L=5  WR=44.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude H20=H20b drops 15/18 losers (83%)
- **Final: n=117  W=114/L=3  WR=97.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W02.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude H20=H20b drops 15/18 losers (83%)
- **Final: n=117  W=114/L=3  WR=97.4%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W03.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude H20=H20b drops 15/18 losers (83%)
- **Final: n=117  W=114/L=3  WR=97.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W04.  `H60=H60a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude H20=H20b drops 15/16 losers (94%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60a AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude H20=H20b drops 15/16 losers (94%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W06.  `H60=H60a AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude H20=H20b drops 15/16 losers (94%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W07.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W08.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W09.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W10.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W11.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W12.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W13.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=101  W=95/L=6  WR=94.1%
- Refine: exclude H20=H20e drops 5/6 losers (83%)
- **Final: n=85  W=84/L=1  WR=98.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF20 strongly against

### W14.  `H20=H20e AND T4=T4a AND BBP=BBP4`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude session_bucket=ny_mid drops 7/10 losers (70%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W15.  `H20=H20e AND T4=T4a AND ZS=ZS4`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/10 losers (70%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W16.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/10 losers (70%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W17.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H20=H20b drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when HTF20 slightly aligned

### W18.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20b drops 4/11 losers (36%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W19.  `T4=T4c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20b drops 4/11 losers (36%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W20.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W21.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W22.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W23.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude H20=H20b drops 4/9 losers (44%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W24.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=68/L=2  WR=97.1%
- Refine: exclude BBP=BBP3 drops 2/2 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  AVOID when middle of band

### W25.  `H20=H20e AND T4=T4a AND RSI=RSI6`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=london_open

### L02.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=london_open

### L03.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=london_open

### L04.  `H20=H20a AND RSI=RSI6 AND session_bucket=london`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is H60=H60a (17/39 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=london  •  ONLY when HTF60 aligned WITH trade

### L05.  `H20=H20d AND T4=T4c AND RSI=RSI5`
- Raw: n=58  W=20/L=38  WR=34.5%
- Sharpen: sharpest is H60=H60a (26/38 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L06.  `H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is RSI=RSI5 (28/44 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L07.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is RSI=RSI5 (28/44 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is RSI=RSI5 (28/44 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L09.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is RSI=RSI5 (28/44 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L10.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is RSI=RSI5 (28/44 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L11.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is RSI=RSI5 (28/44 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (13/36 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L13.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (13/36 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L14.  `H20=H20a AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (13/36 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L15.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=22/L=35  WR=38.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid

### L16.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=22/L=35  WR=38.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=ny_mid

### L17.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=22/L=35  WR=38.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=ny_mid

### L18.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=22/L=35  WR=38.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid

### L19.  `H20=H20a AND T4=T4c AND RSI=RSI6`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is session_bucket=london_open (14/36 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L20.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is session_bucket=london_open (14/36 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L21.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is session_bucket=london_open (14/36 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L22.  `H20=H20a AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is session_bucket=london_open (14/36 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L23.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (16/33 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND T1=T1a AND T4=T4c`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (16/33 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L25.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (16/33 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(32/23) | H20a(28/35) |
| H60 | — | H60a(34/40) |
| T1 | T1c(53/43) | T1a(47/57) |
| T4 | T4a(53/48) | T4c(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/43) | long(47/57) |
| session_bucket | ny_mid(40/34) | — |

*Read: `bucket(winner%/loser%)`.*
