# AUD_NZD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,108**  (W=688 / L=420)  -  WR: **62.1%**

## Session distribution

- asia: n=447  W=269/L=178  WR=60.2%
- ny_mid: n=203  W=134/L=69  WR=66.0%
- london_open: n=163  W=103/L=60  WR=63.2%
- off_hours: n=88  W=48/L=40  WR=54.5%
- ny_open: n=79  W=54/L=25  WR=68.4%
- london: n=64  W=44/L=20  WR=68.8%
- ny_close: n=39  W=21/L=18  WR=53.8%
- asia_late: n=25  W=15/L=10  WR=60.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude session_bucket=london_open drops 6/14 losers (43%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third  •  AVOID when session=london_open

### W02.  `H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W03.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: LONG**  •  4h trend WITH trade; lower third  •  AVOID when session=london_open

### W04.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W05.  `H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=86  W=78/L=8  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=london_open

### W06.  `T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=86  W=78/L=8  WR=90.7%**
- **Dir: LONG**  •  1h trend WITH trade; lower third  •  AVOID when session=london_open

### W07.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=86  W=78/L=8  WR=90.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=london_open

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W09.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W10.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W11.  `H20=H20a AND H60=H60a AND BBP=BBP2`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  AVOID when session=london_open

### W12.  `H20=H20a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third  •  AVOID when session=london_open

### W13.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  AVOID when session=london_open

### W14.  `H20=H20a AND T4=T4a AND BBP=BBP2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W15.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W16.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W17.  `H20=H20a AND T1=T1a AND BBP=BBP2`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/11 losers (45%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=london_open

### W18.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/11 losers (45%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=london_open

### W19.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/11 losers (45%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=london_open

### W20.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude RSI=RSI5 drops 8/10 losers (80%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral; session=asia  •  AVOID when RSI 60-70 strong

### W21.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W22.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W23.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W24.  `H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W25.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is BBP=BBP2 (20/93 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when lower third

### L02.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is BBP=BBP2 (20/93 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when lower third

### L03.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is BBP=BBP2 (20/93 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when lower third

### L04.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=145  W=55/L=90  WR=37.9%
- Sharpen: sharpest is BBP=BBP2 (19/90 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when lower third

### L05.  `T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=89  W=27/L=62  WR=30.3%
- Sharpen: sharpest is session_bucket=london_open (14/62 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L06.  `H60=H60e AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI4 (23/58 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L07.  `H60=H60e AND BBP=BBP3 AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI4 (23/58 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: SHORT**  •  HTF60 strongly against; middle of band  •  ONLY when RSI 50-60 upper neutral

### L08.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI4 (23/58 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: SHORT**  •  middle of band; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L09.  `H60=H60e AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI4 (23/58 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: SHORT**  •  HTF60 strongly against; middle of band; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L10.  `H60=H60e AND T4=T4c AND BBP=BBP3`
- Raw: n=81  W=24/L=57  WR=29.6%
- Sharpen: sharpest is session_bucket=london_open (14/57 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L11.  `T4=T4c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=81  W=24/L=57  WR=29.6%
- Sharpen: sharpest is session_bucket=london_open (14/57 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L12.  `H60=H60e AND T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=81  W=24/L=57  WR=29.6%
- Sharpen: sharpest is session_bucket=london_open (14/57 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L13.  `H60=H60e AND T4=T4c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=81  W=24/L=57  WR=29.6%
- Sharpen: sharpest is session_bucket=london_open (14/57 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L14.  `T4=T4c AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=81  W=24/L=57  WR=29.6%
- Sharpen: sharpest is session_bucket=london_open (14/57 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L15.  `H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=81  W=26/L=55  WR=32.1%
- Sharpen: sharpest is T4=T4a (55/55 of losers there)
- **Sharp: n=69  W=14/L=55  WR=20.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L16.  `H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is T4=T4a (52/52 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is T4=T4a (52/52 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L18.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is T4=T4a (52/52 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L19.  `T1=T1c AND T4=T4c AND BBP=BBP3`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is session_bucket=london_open (14/49 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L20.  `T1=T1c AND T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is session_bucket=london_open (14/49 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L21.  `H60=H60e AND T1=T1c AND BBP=BBP3`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L22.  `H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (21/47 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third  •  ONLY when session=asia

### L23.  `T1=T1c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L24.  `H60=H60e AND T1=T1c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; middle of band  •  ONLY when session=london_open

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
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
