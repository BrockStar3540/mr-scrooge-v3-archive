# NZD_JPY — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,690**  (W=1,103 / L=587)  -  WR: **65.3%**

## Session distribution

- asia: n=466  W=296/L=170  WR=63.5%
- ny_close: n=262  W=171/L=91  WR=65.3%
- ny_mid: n=240  W=151/L=89  WR=62.9%
- ny_open: n=218  W=139/L=79  WR=63.8%
- london_open: n=207  W=150/L=57  WR=72.5%
- london: n=142  W=95/L=47  WR=66.9%
- asia_late: n=96  W=63/L=33  WR=65.6%
- off_hours: n=59  W=38/L=21  WR=64.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude session_bucket=asia drops 9/17 losers (53%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=asia

### W02.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude session_bucket=asia drops 9/17 losers (53%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W03.  `T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20a drops 7/14 losers (50%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `H20=H20e AND H60=H60e AND BBP=BBP6`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia_late drops 5/14 losers (36%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when session=asia_late

### W05.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia_late drops 5/14 losers (36%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=asia_late

### W06.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia_late drops 5/14 losers (36%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when session=asia_late

### W07.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude T4=T4a drops 7/14 losers (50%)
- **Final: n=94  W=87/L=7  WR=92.6%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  AVOID when 4h trend WITH trade

### W08.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=91/L=11  WR=89.2%
- Refine: exclude H20=H20a drops 4/11 losers (36%)
- **Final: n=94  W=87/L=7  WR=92.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 7/14 losers (50%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when 4h trend WITH trade

### W10.  `H60=H60e AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20d drops 6/14 losers (43%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W11.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20d drops 6/14 losers (43%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W12.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 7/14 losers (50%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when 4h trend WITH trade

### W13.  `H60=H60e AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20d drops 6/14 losers (43%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W14.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude H20=H20a drops 4/11 losers (36%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W15.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude H20=H20a drops 4/11 losers (36%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W16.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude H60=H60b drops 6/12 losers (50%)
- **Final: n=91  W=85/L=6  WR=93.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W17.  `T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude H60=H60b drops 6/12 losers (50%)
- **Final: n=91  W=85/L=6  WR=93.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W18.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude H60=H60b drops 6/12 losers (50%)
- **Final: n=91  W=85/L=6  WR=93.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W19.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=94  W=87/L=7  WR=92.6%
- Refine: exclude BBP=BBP3 drops 3/7 losers (43%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W20.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=94  W=87/L=7  WR=92.6%
- Refine: exclude BBP=BBP3 drops 3/7 losers (43%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W21.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H20=H20a drops 4/11 losers (36%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W22.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H20=H20a drops 4/11 losers (36%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W23.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4a drops 7/13 losers (54%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when 4h trend WITH trade

### W24.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4a drops 7/13 losers (54%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4a drops 7/13 losers (54%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is T4=T4a (29/44 of losers there)
- **Sharp: n=41  W=12/L=29  WR=29.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is T4=T4a (29/44 of losers there)
- **Sharp: n=41  W=12/L=29  WR=29.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L03.  `T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (12/44 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when session=london_open

### L04.  `T4=T4a AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (12/44 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L05.  `H20=H20a AND T1=T1a AND BBP=BBP6`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is ZS=ZS6 (14/39 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L06.  `H20=H20a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is ZS=ZS6 (14/39 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L07.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is ZS=ZS6 (14/39 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L08.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=61  W=16/L=45  WR=26.2%
- Sharpen: sharpest is H20=H20e (13/45 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L09.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=61  W=16/L=45  WR=26.2%
- Sharpen: sharpest is H20=H20e (13/45 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L10.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=61  W=16/L=45  WR=26.2%
- Sharpen: sharpest is H20=H20e (13/45 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L11.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is ZS=ZS6 (14/39 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L12.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is ZS=ZS6 (14/39 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L13.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is ZS=ZS6 (14/39 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L14.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is direction_exec=long (32/37 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when long

### L15.  `H20=H20e AND T1=T1a AND direction_exec=long`
- Raw: n=54  W=17/L=37  WR=31.5%
- Sharpen: sharpest is H60=H60e (13/37 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when HTF60 strongly against

### L16.  `T4=T4a AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=51  W=17/L=34  WR=33.3%
- Sharpen: sharpest is session_bucket=london (10/34 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when session=london

### L17.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is ZS=ZS4 (13/32 of losers there)
- **Sharp: n=17  W=4/L=13  WR=23.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L18.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is ZS=ZS4 (13/32 of losers there)
- **Sharp: n=17  W=4/L=13  WR=23.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L19.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is ZS=ZS4 (13/32 of losers there)
- **Sharp: n=17  W=4/L=13  WR=23.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L20.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is ZS=ZS4 (13/32 of losers there)
- **Sharp: n=17  W=4/L=13  WR=23.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L21.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is session_bucket=london (10/30 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when session=london

### L22.  `H20=H20a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is strategy_id=alpha_pullback_v2 (5/31 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when strategy=alpha_pullback_v2

### L23.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is strategy_id=alpha_pullback_v2 (5/31 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when strategy=alpha_pullback_v2

### L24.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is strategy_id=alpha_pullback_v2 (5/31 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when strategy=alpha_pullback_v2

### L25.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=44  W=10/L=34  WR=22.7%
- Sharpen: sharpest is H20=H20e (13/34 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(53/47) | T1a(47/53) |
| T4 | T4c(55/45) | T4a(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/46) | long(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
