# CHF_JPY — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,586**  (W=2,248 / L=1,338)  -  WR: **62.7%**

## Session distribution

- asia: n=1589  W=1021/L=568  WR=64.3%
- ny_close: n=652  W=377/L=275  WR=57.8%
- london_open: n=328  W=207/L=121  WR=63.1%
- london: n=308  W=212/L=96  WR=68.8%
- ny_open: n=282  W=181/L=101  WR=64.2%
- asia_late: n=269  W=158/L=111  WR=58.7%
- off_hours: n=105  W=66/L=39  WR=62.9%
- ny_mid: n=53  W=26/L=27  WR=49.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude H20=H20c drops 13/17 losers (76%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 neutral

### W02.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP3`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude RSI=RSI4 drops 10/18 losers (56%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; middle of band  •  AVOID when RSI 50-60 upper neutral

### W03.  `BBP=BBP3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=113  W=102/L=11  WR=90.3%
- Refine: exclude RSI=RSI4 drops 8/11 losers (73%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  middle of band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W04.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=113  W=102/L=11  WR=90.3%
- Refine: exclude RSI=RSI4 drops 8/11 losers (73%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  middle of band; zscore -1 to +1 neutral; session=asia  •  AVOID when RSI 50-60 upper neutral

### W05.  `H60=H60a AND T4=T4c AND BBP=BBP3`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude RSI=RSI4 drops 9/15 losers (60%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; middle of band  •  AVOID when RSI 50-60 upper neutral

### W06.  `H60=H60a AND T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude RSI=RSI4 drops 9/15 losers (60%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  AVOID when RSI 50-60 upper neutral

### W07.  `H60=H60a AND T4=T4c AND BBP=BBP3 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude RSI=RSI4 drops 9/15 losers (60%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; middle of band  •  AVOID when RSI 50-60 upper neutral

### W08.  `T1=T1a AND BBP=BBP3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude RSI=RSI4 drops 8/11 losers (73%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: LONG**  •  1h trend WITH trade; middle of band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W09.  `H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=97  W=90/L=7  WR=92.8%
- Refine: exclude H20=H20a drops 6/7 losers (86%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=97  W=90/L=7  WR=92.8%
- Refine: exclude H20=H20a drops 6/7 losers (86%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

### W11.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=96  W=94/L=2  WR=97.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W12.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=96  W=94/L=2  WR=97.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: LONG**  •  upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W13.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=96  W=94/L=2  WR=97.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W14.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=94  W=92/L=2  WR=97.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W15.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=94  W=92/L=2  WR=97.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W16.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=94  W=92/L=2  WR=97.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W17.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=90  W=88/L=2  WR=97.8%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W18.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=88/L=2  WR=97.8%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W19.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=90  W=88/L=2  WR=97.8%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W20.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=88/L=2  WR=97.8%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W21.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=88/L=2  WR=97.8%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W22.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 7/11 losers (64%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band; RSI 60-70 strong  •  AVOID when session=ny_close

### W23.  `T4=T4c AND BBP=BBP3 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 7/11 losers (64%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; middle of band; RSI 60-70 strong  •  AVOID when session=ny_close

### W24.  `H60=H60a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20d AND T1=T1c AND direction_exec=short`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=173  W=64/L=109  WR=37.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade

### L02.  `H20=H20d AND T1=T1c AND session_bucket=asia`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is T4=T4a (27/92 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20d AND direction_exec=short AND session_bucket=asia`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is T4=T4a (27/92 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  HTF20 mildly against; session=asia  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20d AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is T4=T4a (27/92 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20d AND T1=T1c AND BBP=BBP4`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (14/81 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L06.  `H20=H20d AND BBP=BBP4 AND direction_exec=short`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (14/81 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 mildly against; upper third  •  ONLY when RSI 50-60 upper neutral

### L07.  `H20=H20d AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (14/81 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L08.  `H20=H20d AND T1=T1c AND ZS=ZS4`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (14/78 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L09.  `H20=H20d AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (14/78 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 mildly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L10.  `H20=H20d AND ZS=ZS4 AND direction_exec=short`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (14/78 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20d AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (14/78 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20d AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (14/78 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20d AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (14/78 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 mildly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L14.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: sharpest is BBP=BBP4 (50/77 of losers there)
- **Sharp: n=57  W=7/L=50  WR=12.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L15.  `H20=H20d AND T1=T1c AND T4=T4c`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=124  W=48/L=76  WR=38.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade

### L16.  `H20=H20d AND T4=T4c AND direction_exec=short`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=124  W=48/L=76  WR=38.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade

### L17.  `H20=H20d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=124  W=48/L=76  WR=38.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade

### L18.  `H20=H20d AND H60=H60e AND T1=T1c`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=47/L=76  WR=38.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade

### L19.  `H20=H20d AND H60=H60e AND direction_exec=short`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=47/L=76  WR=38.2%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against

### L20.  `H20=H20d AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=47/L=76  WR=38.2%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade

### L21.  `H20=H20d AND H60=H60e AND session_bucket=asia`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=47/L=71  WR=39.8%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; session=asia

### L22.  `H20=H20d AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=47/L=71  WR=39.8%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia

### L23.  `H20=H20d AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=47/L=71  WR=39.8%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; session=asia

### L24.  `H20=H20d AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=110  W=39/L=71  WR=35.5%
- Sharpen: sharpest is T4=T4a (26/71 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF20 mildly against; RSI 60-70 strong; session=asia  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20d AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=110  W=39/L=71  WR=35.5%
- Sharpen: sharpest is T4=T4a (26/71 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(3/8) |
| H60 | H60a(47/40) | H60e(41/49) |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | T4a(54/48) | T4c(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/45) | short(45/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
