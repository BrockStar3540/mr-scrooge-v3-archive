# AUD_CHF — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,217**  (W=784 / L=433)  -  WR: **64.4%**

## Session distribution

- london_open: n=523  W=343/L=180  WR=65.6%
- ny_mid: n=237  W=158/L=79  WR=66.7%
- ny_open: n=193  W=134/L=59  WR=69.4%
- london: n=177  W=101/L=76  WR=57.1%
- asia: n=47  W=24/L=23  WR=51.1%
- ny_close: n=23  W=16/L=7  WR=69.6%
- asia_late: n=10  W=4/L=6  WR=40.0%
- off_hours: n=7  W=4/L=3  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=288  W=256/L=32  WR=88.9%
- Refine: exclude ZS=ZS5 drops 21/32 losers (66%)
- **Final: n=149  W=138/L=11  WR=92.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W02.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=282  W=253/L=29  WR=89.7%
- Refine: exclude RSI=RSI5 drops 19/29 losers (66%)
- **Final: n=142  W=132/L=10  WR=93.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  AVOID when RSI 60-70 strong

### W03.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=281  W=253/L=28  WR=90.0%
- Refine: exclude RSI=RSI5 drops 19/28 losers (68%)
- **Final: n=141  W=132/L=9  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 60-70 strong

### W04.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=281  W=253/L=28  WR=90.0%
- Refine: exclude RSI=RSI5 drops 19/28 losers (68%)
- **Final: n=141  W=132/L=9  WR=93.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 60-70 strong

### W05.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=245  W=215/L=30  WR=87.8%
- Refine: exclude BBP=BBP6 drops 10/30 losers (33%)
- **Final: n=207  W=187/L=20  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when deep above upper band

### W06.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=244  W=215/L=29  WR=88.1%
- Refine: exclude BBP=BBP6 drops 10/29 losers (34%)
- **Final: n=206  W=187/L=19  WR=90.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  AVOID when deep above upper band

### W07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=244  W=215/L=29  WR=88.1%
- Refine: exclude BBP=BBP6 drops 10/29 losers (34%)
- **Final: n=206  W=187/L=19  WR=90.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  AVOID when deep above upper band

### W08.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=241  W=215/L=26  WR=89.2%
- Refine: exclude BBP=BBP6 drops 10/26 losers (38%)
- **Final: n=203  W=187/L=16  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W09.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=241  W=215/L=26  WR=89.2%
- Refine: exclude BBP=BBP6 drops 10/26 losers (38%)
- **Final: n=203  W=187/L=16  WR=92.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W10.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=240  W=215/L=25  WR=89.6%
- Refine: exclude RSI=RSI5 drops 19/25 losers (76%)
- **Final: n=118  W=112/L=6  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 60-70 strong

### W11.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/24 losers (42%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W12.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/24 losers (42%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W13.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/24 losers (42%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W14.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/24 losers (42%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W15.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/24 losers (42%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W16.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/24 losers (42%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W17.  `H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=164  W=141/L=23  WR=86.0%
- Refine: exclude ZS=ZS5 drops 17/23 losers (74%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W18.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=164  W=141/L=23  WR=86.0%
- Refine: exclude ZS=ZS5 drops 17/23 losers (74%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W19.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=164  W=141/L=23  WR=86.0%
- Refine: exclude ZS=ZS5 drops 17/23 losers (74%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W20.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=161  W=141/L=20  WR=87.6%
- Refine: exclude RSI=RSI5 drops 13/20 losers (65%)
- **Final: n=97  W=90/L=7  WR=92.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 60-70 strong

### W21.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=160  W=141/L=19  WR=88.1%
- Refine: exclude RSI=RSI5 drops 13/19 losers (68%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 60-70 strong

### W22.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=160  W=141/L=19  WR=88.1%
- Refine: exclude RSI=RSI5 drops 13/19 losers (68%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 60-70 strong

### W23.  `T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=151  W=140/L=11  WR=92.7%
- Refine: exclude BBP=BBP5 drops 6/11 losers (55%)
- **Final: n=114  W=109/L=5  WR=95.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when just touched upper band

### W24.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=149  W=135/L=14  WR=90.6%
- Refine: exclude BBP=BBP5 drops 10/14 losers (71%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london_open  •  AVOID when just touched upper band

### W25.  `H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=148  W=135/L=13  WR=91.2%
- Refine: exclude BBP=BBP5 drops 10/13 losers (77%)
- **Final: n=109  W=106/L=3  WR=97.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=257  W=102/L=155  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=257  W=102/L=155  WR=39.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L02.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=257  W=102/L=155  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=257  W=102/L=155  WR=39.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong

### L03.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=257  W=102/L=155  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=257  W=102/L=155  WR=39.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=257  W=102/L=155  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=257  W=102/L=155  WR=39.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L05.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=232  W=85/L=147  WR=36.6%
- Sharpen: sharpest is RSI=RSI4 (83/147 of losers there)
- **Sharp: n=114  W=31/L=83  WR=27.2%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L06.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=225  W=79/L=146  WR=35.1%
- Sharpen: sharpest is RSI=RSI4 (82/146 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L07.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=223  W=77/L=146  WR=34.5%
- Sharpen: sharpest is RSI=RSI4 (82/146 of losers there)
- **Sharp: n=105  W=23/L=82  WR=21.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L08.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=223  W=77/L=146  WR=34.5%
- Sharpen: sharpest is RSI=RSI4 (82/146 of losers there)
- **Sharp: n=105  W=23/L=82  WR=21.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L09.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=205  W=82/L=123  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (69/123 of losers there)
- **Sharp: n=97  W=28/L=69  WR=28.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L10.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=205  W=82/L=123  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (69/123 of losers there)
- **Sharp: n=97  W=28/L=69  WR=28.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=199  W=76/L=123  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (69/123 of losers there)
- **Sharp: n=91  W=22/L=69  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=199  W=76/L=123  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (69/123 of losers there)
- **Sharp: n=91  W=22/L=69  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=197  W=74/L=123  WR=37.6%
- Sharpen: sharpest is RSI=RSI4 (69/123 of losers there)
- **Sharp: n=89  W=20/L=69  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L14.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is RSI=RSI4 (58/88 of losers there)
- **Sharp: n=78  W=20/L=58  WR=25.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L15.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is RSI=RSI4 (58/88 of losers there)
- **Sharp: n=78  W=20/L=58  WR=25.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L16.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is H20=H20d (20/80 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L17.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is H20=H20d (20/80 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L18.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is H20=H20d (20/80 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L19.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is H20=H20d (20/80 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L20.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is H20=H20d (20/80 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L21.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is H20=H20d (20/80 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L22.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=116  W=33/L=83  WR=28.4%
- Sharpen: sharpest is T1=T1c (82/83 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

### L23.  `T1=T1c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=115  W=39/L=76  WR=33.9%
- Sharpen: sharpest is BBP=BBP5 (47/76 of losers there)
- **Sharp: n=56  W=9/L=47  WR=16.1%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when just touched upper band

### L24.  `T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=114  W=28/L=86  WR=24.6%
- Sharpen: sharpest is ZS=ZS5 (44/86 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=114  W=31/L=83  WR=27.2%
- Sharpen: sharpest is T1=T1c (82/83 of losers there)
- **Sharp: n=105  W=23/L=82  WR=21.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(56/25) | H20e(30/56), H20d(0/8) |
| H60 | H60a(65/31) | H60e(34/68) |
| T1 | T1a(67/31) | T1c(33/69) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(65/32) | short(35/68) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
