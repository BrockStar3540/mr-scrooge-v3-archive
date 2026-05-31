# NZD_CAD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,177**  (W=2,045 / L=1,132)  -  WR: **64.4%**

## Session distribution

- asia: n=864  W=553/L=311  WR=64.0%
- ny_mid: n=807  W=518/L=289  WR=64.2%
- london_open: n=399  W=269/L=130  WR=67.4%
- ny_open: n=398  W=252/L=146  WR=63.3%
- ny_close: n=311  W=197/L=114  WR=63.3%
- london: n=201  W=122/L=79  WR=60.7%
- asia_late: n=128  W=91/L=37  WR=71.1%
- off_hours: n=69  W=43/L=26  WR=62.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=154  W=131/L=23  WR=85.1%
- Refine: exclude T4=T4a drops 23/23 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend WITH trade

### W02.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=154  W=131/L=23  WR=85.1%
- Refine: exclude T4=T4a drops 23/23 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when 4h trend WITH trade

### W03.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 10/20 losers (50%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 10/20 losers (50%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W05.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=138  W=127/L=11  WR=92.0%
- Refine: exclude H60=H60e drops 9/11 losers (82%)
- **Final: n=86  W=84/L=2  WR=97.7%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W06.  `H60=H60e AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude H20=H20c drops 16/18 losers (89%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when HTF20 neutral

### W07.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude H60=H60e drops 10/16 losers (62%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when HTF60 strongly against

### W08.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude H60=H60e drops 10/16 losers (62%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W09.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude H60=H60e drops 10/16 losers (62%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when HTF60 strongly against

### W10.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude session_bucket=ny_mid drops 8/11 losers (73%)
- **Final: n=86  W=83/L=3  WR=96.5%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W11.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude session_bucket=london drops 3/9 losers (33%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W12.  `H20=H20a AND H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W13.  `H20=H20a AND H60=H60e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W14.  `T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude H20=H20c drops 4/10 losers (40%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; session=asia  •  AVOID when HTF20 neutral

### W15.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 1h trend WITH trade

### W16.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude RSI=RSI6 drops 6/8 losers (75%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 70-80 overbought

### W17.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude RSI=RSI6 drops 6/8 losers (75%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when RSI 70-80 overbought

### W18.  `H60=H60a AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude RSI=RSI6 drops 6/8 losers (75%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when RSI 70-80 overbought

### W19.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude RSI=RSI5 drops 12/12 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W20.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude RSI=RSI5 drops 12/12 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W21.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude RSI=RSI5 drops 12/12 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W22.  `H20=H20a AND H60=H60e AND session_bucket=asia`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude RSI=RSI5 drops 10/10 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=asia  •  AVOID when RSI 60-70 strong

### W23.  `H60=H60d AND T1=T1c AND session_bucket=london_open`
- Raw: n=80  W=77/L=3  WR=96.2%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W24.  `H60=H60d AND T4=T4c AND session_bucket=london_open`
- Raw: n=80  W=77/L=3  WR=96.2%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W25.  `H60=H60d AND direction_exec=short AND session_bucket=london_open`
- Raw: n=80  W=77/L=3  WR=96.2%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 mildly against; session=london_open  •  AVOID when middle of band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is RSI=RSI6 (20/81 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  ONLY when RSI 70-80 overbought

### L02.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=123  W=46/L=77  WR=37.4%
- Sharpen: sharpest is H20=H20e (33/77 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L03.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=120  W=42/L=78  WR=35.0%
- Sharpen: sharpest is BBP=BBP6 (18/78 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L04.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=120  W=42/L=78  WR=35.0%
- Sharpen: sharpest is BBP=BBP6 (18/78 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid  •  ONLY when deep above upper band

### L05.  `H60=H60a AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is H20=H20e (28/64 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H60=H60a (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L07.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H60=H60a (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L08.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H60=H60a (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L09.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H60=H60a (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L10.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H60=H60a (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L11.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H60=H60a (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L12.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: sharpest is T4=T4a (27/62 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: sharpest is T4=T4a (27/62 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: sharpest is T4=T4a (27/62 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L15.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=92  W=26/L=66  WR=28.3%
- Sharpen: sharpest is ZS=ZS6 (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when zscore >+3 extreme

### L16.  `H20=H20e AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is T4=T4a (22/55 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is T4=T4a (22/55 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third  •  ONLY when 4h trend WITH trade

### L18.  `H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is BBP=BBP6 (10/54 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when deep above upper band

### L19.  `H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is BBP=BBP6 (10/54 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_close  •  ONLY when deep above upper band

### L20.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is BBP=BBP6 (10/54 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when deep above upper band

### L21.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (18/51 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L22.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (18/51 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L23.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is RSI=RSI6 (20/53 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 70-80 overbought

### L24.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is RSI=RSI6 (20/53 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  ONLY when RSI 70-80 overbought

### L25.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is RSI=RSI6 (20/53 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/38) | H20e(39/47) |
| H60 | — | — |
| T1 | T1c(55/48) | T1a(45/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/48) | long(45/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
