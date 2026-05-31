# EUR_CHF — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **785**  (W=514 / L=271)  -  WR: **65.5%**

## Session distribution

- asia: n=163  W=113/L=50  WR=69.3%
- london_open: n=151  W=91/L=60  WR=60.3%
- london: n=141  W=94/L=47  WR=66.7%
- ny_open: n=94  W=61/L=33  WR=64.9%
- ny_close: n=92  W=59/L=33  WR=64.1%
- off_hours: n=58  W=38/L=20  WR=65.5%
- ny_mid: n=47  W=34/L=13  WR=72.3%
- asia_late: n=39  W=24/L=15  WR=61.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade  •  AVOID when HTF20 strongly against

### W02.  `H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF20 strongly against

### W03.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF20 strongly against

### W04.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude H60=H60c drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF60 neutral

### W05.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude H60=H60c drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when HTF60 neutral

### W06.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude H60=H60c drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF60 neutral

### W07.  `H20=H20c AND T1=T1a AND direction_exec=long`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when session=ny_close

### W08.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W09.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W10.  `H20=H20d AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W11.  `H20=H20c AND H60=H60b AND T1=T1a`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF20 neutral; HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_close

### W12.  `H20=H20c AND H60=H60b AND direction_exec=long`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 slightly aligned  •  AVOID when session=ny_close

### W13.  `H20=H20c AND H60=H60b AND T1=T1a AND direction_exec=long`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_close

### W14.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W15.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when session=ny_close

### W16.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W17.  `H20=H20c AND H60=H60b AND T4=T4a`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_close

### W18.  `H20=H20c AND H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W19.  `H20=H20c AND H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_close

### W20.  `T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H60=H60d drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band  •  AVOID when HTF60 mildly against

### W21.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H60=H60d drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W22.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=69  W=65/L=4  WR=94.2%
- Refine: exclude session_bucket=london_open drops 4/4 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W23.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=69  W=65/L=4  WR=94.2%
- Refine: exclude session_bucket=london_open drops 4/4 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W24.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 4/9 losers (44%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W25.  `T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H60=H60d drops 4/10 losers (40%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when HTF60 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is H60=H60a (27/47 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L02.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is H60=H60a (27/47 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L03.  `H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is BBP=BBP5 (27/49 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when just touched upper band

### L04.  `T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is H60=H60a (26/46 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L05.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is H60=H60a (26/46 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L06.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is H60=H60a (26/46 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L07.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=71  W=25/L=46  WR=35.2%
- Sharpen: sharpest is BBP=BBP5 (26/46 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when just touched upper band

### L08.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=71  W=25/L=46  WR=35.2%
- Sharpen: sharpest is BBP=BBP5 (26/46 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when just touched upper band

### L09.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is T4=T4c (23/41 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is T4=T4c (23/41 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=61  W=14/L=47  WR=23.0%
- Sharpen: sharpest is session_bucket=ny_open (12/47 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L12.  `H20=H20c AND H60=H60d AND T1=T1c`
- Raw: n=59  W=14/L=45  WR=23.7%
- Sharpen: sharpest is session_bucket=ny_open (12/45 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L13.  `H20=H20c AND H60=H60d AND direction_exec=short`
- Raw: n=59  W=14/L=45  WR=23.7%
- Sharpen: sharpest is session_bucket=ny_open (12/45 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 mildly against  •  ONLY when session=ny_open

### L14.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=59  W=14/L=45  WR=23.7%
- Sharpen: sharpest is RSI=RSI4 (11/45 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=59  W=14/L=45  WR=23.7%
- Sharpen: sharpest is RSI=RSI4 (11/45 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20c AND H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=59  W=14/L=45  WR=23.7%
- Sharpen: sharpest is session_bucket=ny_open (12/45 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L17.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=59  W=14/L=45  WR=23.7%
- Sharpen: sharpest is RSI=RSI4 (11/45 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20c AND H60=H60d AND T4=T4c`
- Raw: n=57  W=14/L=43  WR=24.6%
- Sharpen: sharpest is RSI=RSI4 (11/43 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L19.  `H20=H20c AND H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=57  W=14/L=43  WR=24.6%
- Sharpen: sharpest is RSI=RSI4 (11/43 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L20.  `H20=H20c AND H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=57  W=14/L=43  WR=24.6%
- Sharpen: sharpest is RSI=RSI4 (11/43 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L21.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is T4=T4c (24/35 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: sharpest is BBP=BBP5 (21/37 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L23.  `T4=T4c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is H20=H20b (12/31 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 slightly aligned

### L24.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=49  W=12/L=37  WR=24.5%
- Sharpen: sharpest is BBP=BBP5 (21/37 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L25.  `T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is H60=H60d (12/31 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(16/8), H20e(33/25) | H20b(10/18), H20a(24/29) |
| H60 | H60b(25/10) | H60d(10/24) |
| T1 | T1a(50/44) | T1c(50/56) |
| T4 | T4a(62/36) | T4c(38/63) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | ZS5(32/38) |
| strategy_id | — | — |
| direction_exec | long(51/43) | short(49/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
