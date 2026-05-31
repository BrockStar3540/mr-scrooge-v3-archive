# GBP_NZD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,090**  (W=2,990 / L=2,100)  -  WR: **58.7%**

## Session distribution

- asia: n=2001  W=1177/L=824  WR=58.8%
- ny_close: n=1383  W=823/L=560  WR=59.5%
- ny_open: n=567  W=329/L=238  WR=58.0%
- london: n=421  W=265/L=156  WR=62.9%
- off_hours: n=326  W=167/L=159  WR=51.2%
- asia_late: n=194  W=113/L=81  WR=58.2%
- london_open: n=139  W=83/L=56  WR=59.7%
- ny_mid: n=59  W=33/L=26  WR=55.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=208  W=178/L=30  WR=85.6%
- Refine: exclude ZS=ZS4 drops 20/30 losers (67%)
- **Final: n=113  W=103/L=10  WR=91.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W02.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=201  W=178/L=23  WR=88.6%
- Refine: exclude ZS=ZS4 drops 20/23 losers (87%)
- **Final: n=106  W=103/L=3  WR=97.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W03.  `H20=H20a AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=136  W=119/L=17  WR=87.5%
- Refine: exclude H60=H60e drops 17/17 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W04.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude session_bucket=asia drops 16/17 losers (94%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W05.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude H60=H60e drops 17/17 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W06.  `T1=T1a AND BBP=BBP3 AND session_bucket=asia`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude RSI=RSI4 drops 15/17 losers (88%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W07.  `T1=T1a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude RSI=RSI4 drops 15/17 losers (88%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; zscore -1 to +1 neutral; session=asia  •  AVOID when RSI 50-60 upper neutral

### W08.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W13.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=114  W=100/L=14  WR=87.7%
- Refine: exclude H60=H60a drops 13/14 losers (93%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W14.  `T1=T1a AND BBP=BBP3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude RSI=RSI4 drops 15/17 losers (88%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: LONG**  •  1h trend WITH trade; middle of band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W15.  `T1=T1a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H20=H20c drops 10/16 losers (62%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W16.  `T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H20=H20c drops 10/16 losers (62%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W17.  `RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H20=H20c drops 10/16 losers (62%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: LONG**  •  RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W18.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H20=H20c drops 10/16 losers (62%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W19.  `T1=T1a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H20=H20c drops 10/16 losers (62%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W20.  `T4=T4a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H20=H20c drops 10/16 losers (62%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W21.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude session_bucket=asia drops 6/7 losers (86%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W22.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=101  W=93/L=8  WR=92.1%
- Refine: exclude BBP=BBP6 drops 7/8 losers (88%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when deep above upper band

### W23.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=101  W=93/L=8  WR=92.1%
- Refine: exclude BBP=BBP6 drops 7/8 losers (88%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when deep above upper band

### W24.  `H20=H20e AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=101  W=93/L=8  WR=92.1%
- Refine: exclude BBP=BBP6 drops 7/8 losers (88%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when deep above upper band

### W25.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=100  W=93/L=7  WR=93.0%
- Refine: exclude session_bucket=asia drops 6/7 losers (86%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=257  W=85/L=172  WR=33.1%
- Sharpen: sharpest is H60=H60e (88/172 of losers there)
- **Sharp: n=109  W=21/L=88  WR=19.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=252  W=83/L=169  WR=32.9%
- Sharpen: sharpest is H60=H60e (88/169 of losers there)
- **Sharp: n=109  W=21/L=88  WR=19.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L03.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=252  W=83/L=169  WR=32.9%
- Sharpen: sharpest is H60=H60e (88/169 of losers there)
- **Sharp: n=109  W=21/L=88  WR=19.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=252  W=83/L=169  WR=32.9%
- Sharpen: sharpest is H60=H60e (88/169 of losers there)
- **Sharp: n=109  W=21/L=88  WR=19.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L05.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=252  W=97/L=155  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (60/155 of losers there)
- **Sharp: n=65  W=5/L=60  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=229  W=87/L=142  WR=38.0%
- Sharpen: sharpest is RSI=RSI6 (60/142 of losers there)
- **Sharp: n=65  W=5/L=60  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L07.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=229  W=87/L=142  WR=38.0%
- Sharpen: sharpest is RSI=RSI6 (60/142 of losers there)
- **Sharp: n=65  W=5/L=60  WR=7.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L08.  `T1=T1c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=225  W=86/L=139  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=86/L=139  WR=38.2%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 60-70 strong

### L09.  `T1=T1c AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=225  W=86/L=139  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=86/L=139  WR=38.2%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought

### L10.  `BBP=BBP5 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=224  W=84/L=140  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=224  W=84/L=140  WR=37.5%**
- **Dir: SHORT**  •  just touched upper band; RSI 60-70 strong

### L11.  `BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=224  W=84/L=140  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=224  W=84/L=140  WR=37.5%**
- **Dir: SHORT**  •  just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought

### L12.  `T1=T1c AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=223  W=84/L=139  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=223  W=84/L=139  WR=37.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 60-70 strong

### L13.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=220  W=86/L=134  WR=39.1%
- Sharpen: sharpest is direction_exec=short (126/134 of losers there)
- **Sharp: n=191  W=65/L=126  WR=34.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  ONLY when short

### L14.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=220  W=86/L=134  WR=39.1%
- Sharpen: sharpest is direction_exec=short (126/134 of losers there)
- **Sharp: n=191  W=65/L=126  WR=34.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when short

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=204  W=78/L=126  WR=38.2%
- Sharpen: sharpest is H20=H20d (50/126 of losers there)
- **Sharp: n=59  W=9/L=50  WR=15.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 mildly against

### L16.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=204  W=78/L=126  WR=38.2%
- Sharpen: sharpest is H20=H20d (50/126 of losers there)
- **Sharp: n=59  W=9/L=50  WR=15.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when HTF20 mildly against

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI6`
- Raw: n=197  W=57/L=140  WR=28.9%
- Sharpen: sharpest is H60=H60e (68/140 of losers there)
- **Sharp: n=75  W=7/L=68  WR=9.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L18.  `H20=H20e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=197  W=57/L=140  WR=28.9%
- Sharpen: sharpest is H60=H60e (68/140 of losers there)
- **Sharp: n=75  W=7/L=68  WR=9.3%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=197  W=57/L=140  WR=28.9%
- Sharpen: sharpest is H60=H60e (68/140 of losers there)
- **Sharp: n=75  W=7/L=68  WR=9.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L20.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=196  W=78/L=118  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (49/118 of losers there)
- **Sharp: n=56  W=7/L=49  WR=12.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L21.  `H20=H20d AND T1=T1c AND T4=T4c`
- Raw: n=193  W=64/L=129  WR=33.2%
- Sharpen: sharpest is RSI=RSI5 (102/129 of losers there)
- **Sharp: n=139  W=37/L=102  WR=26.6%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20d AND T4=T4c AND direction_exec=short`
- Raw: n=193  W=64/L=129  WR=33.2%
- Sharpen: sharpest is RSI=RSI5 (102/129 of losers there)
- **Sharp: n=139  W=37/L=102  WR=26.6%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L23.  `H20=H20d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=193  W=64/L=129  WR=33.2%
- Sharpen: sharpest is RSI=RSI5 (102/129 of losers there)
- **Sharp: n=139  W=37/L=102  WR=26.6%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND T4=T4c AND RSI=RSI6`
- Raw: n=192  W=55/L=137  WR=28.6%
- Sharpen: sharpest is H60=H60e (68/137 of losers there)
- **Sharp: n=75  W=7/L=68  WR=9.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=192  W=55/L=137  WR=28.6%
- Sharpen: sharpest is H60=H60e (68/137 of losers there)
- **Sharp: n=75  W=7/L=68  WR=9.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(56/43) | T1c(44/57) |
| T4 | T4a(55/43) | T4c(45/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/43) | short(44/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
