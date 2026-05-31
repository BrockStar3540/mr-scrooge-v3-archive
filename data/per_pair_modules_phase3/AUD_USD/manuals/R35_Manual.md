# AUD_USD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,886**  (W=1,220 / L=666)  -  WR: **64.7%**

## Session distribution

- ny_mid: n=596  W=372/L=224  WR=62.4%
- asia: n=360  W=244/L=116  WR=67.8%
- ny_open: n=332  W=220/L=112  WR=66.3%
- london: n=294  W=184/L=110  WR=62.6%
- london_open: n=170  W=112/L=58  WR=65.9%
- ny_close: n=92  W=63/L=29  WR=68.5%
- off_hours: n=30  W=19/L=11  WR=63.3%
- asia_late: n=12  W=6/L=6  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=185  W=160/L=25  WR=86.5%
- Refine: exclude BBP=BBP2 drops 11/25 losers (44%)
- **Final: n=141  W=127/L=14  WR=90.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when lower third

### W02.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude ZS=ZS4 drops 14/17 losers (82%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W03.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude ZS=ZS4 drops 14/17 losers (82%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W04.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude ZS=ZS4 drops 14/17 losers (82%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W05.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W06.  `H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W07.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W08.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W09.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W10.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W11.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude session_bucket=london_open drops 6/18 losers (33%)
- **Final: n=117  W=105/L=12  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W12.  `H20=H20a AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude session_bucket=london_open drops 7/16 losers (44%)
- **Final: n=112  W=103/L=9  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W13.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude session_bucket=london_open drops 6/18 losers (33%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W14.  `H20=H20a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude session_bucket=london_open drops 6/18 losers (33%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W15.  `H20=H20a AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude session_bucket=london_open drops 6/14 losers (43%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W16.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude T4=T4a drops 10/16 losers (62%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude T4=T4a drops 10/16 losers (62%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude T4=T4a drops 10/16 losers (62%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W19.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude session_bucket=london_open drops 3/13 losers (23%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london_open

### W20.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude RSI=RSI4 drops 9/15 losers (60%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W21.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude H60=H60a drops 11/11 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W22.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude BBP=BBP1 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W23.  `H20=H20a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude ZS=ZS5 drops 3/6 losers (50%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W24.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude ZS=ZS5 drops 3/6 losers (50%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W25.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude ZS=ZS5 drops 3/6 losers (50%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: sharpest is T4=T4a (42/97 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: sharpest is T4=T4a (42/97 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: sharpest is T4=T4a (42/97 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L04.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=124  W=32/L=92  WR=25.8%
- Sharpen: sharpest is H60=H60d (24/92 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF60 mildly against

### L05.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is session_bucket=london (25/53 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L06.  `H60=H60e AND T1=T1c AND session_bucket=london`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is RSI=RSI5 (25/50 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when RSI 60-70 strong

### L07.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is RSI=RSI5 (25/50 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is T1=T1c (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L09.  `H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is T1=T1c (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L10.  `T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is T1=T1c (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L11.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is T1=T1c (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L12.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is T1=T1c (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L13.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is T1=T1c (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (20/50 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L15.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/47 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  ONLY when session=ny_mid

### L16.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=71  W=21/L=50  WR=29.6%
- Sharpen: sharpest is H60=H60d (24/50 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF60 mildly against

### L17.  `T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=71  W=25/L=46  WR=35.2%
- Sharpen: sharpest is session_bucket=ny_mid (19/46 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L18.  `H20=H20c AND T1=T1c AND T4=T4a`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/45 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=ny_mid

### L19.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/45 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L20.  `H20=H20c AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/45 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=ny_mid

### L21.  `H20=H20a AND T4=T4a AND RSI=RSI2`
- Raw: n=69  W=19/L=50  WR=27.5%
- Sharpen: sharpest is session_bucket=asia (19/50 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when session=asia

### L22.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=69  W=26/L=43  WR=37.7%
- Sharpen: sharpest is T1=T1c (24/43 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is BBP=BBP0 (8/42 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when deep below lower band

### L24.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is BBP=BBP0 (8/42 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when deep below lower band

### L25.  `T4=T4a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is T1=T1c (23/42 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(41/36) | — |
| H60 | — | — |
| T1 | T1a(57/41) | T1c(43/59) |
| T4 | T4c(59/40) | T4a(41/60) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
