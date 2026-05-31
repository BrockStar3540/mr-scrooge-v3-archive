# AUD_CHF — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,076**  (W=1,356 / L=720)  -  WR: **65.3%**

## Session distribution

- asia: n=832  W=546/L=286  WR=65.6%
- ny_close: n=348  W=225/L=123  WR=64.7%
- london: n=196  W=124/L=72  WR=63.3%
- london_open: n=186  W=125/L=61  WR=67.2%
- ny_open: n=180  W=120/L=60  WR=66.7%
- asia_late: n=112  W=74/L=38  WR=66.1%
- ny_mid: n=111  W=76/L=35  WR=68.5%
- off_hours: n=111  W=66/L=45  WR=59.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=164  W=140/L=24  WR=85.4%
- Refine: exclude ZS=ZS5 drops 16/24 losers (67%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=125  W=113/L=12  WR=90.4%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W03.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=125  W=113/L=12  WR=90.4%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W04.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude direction_exec=short drops 10/16 losers (62%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when short

### W05.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=113  W=103/L=10  WR=91.2%
- Refine: exclude T1=T1a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W06.  `T1=T1a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude T4=T4a drops 13/13 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W07.  `H20=H20a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude T1=T1c drops 10/14 losers (71%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when 1h trend AGAINST trade

### W08.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude RSI=RSI3 drops 7/9 losers (78%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude RSI=RSI3 drops 7/9 losers (78%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W10.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude direction_exec=short drops 9/13 losers (69%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when short

### W11.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude RSI=RSI3 drops 7/9 losers (78%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W12.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude BBP=BBP5 drops 8/12 losers (67%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched upper band

### W13.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude T4=T4c drops 6/10 losers (60%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=asia  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude ZS=ZS1 drops 9/10 losers (90%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  AVOID when zscore -3 to -2 deep oversold

### W15.  `H20=H20a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude T1=T1c drops 9/13 losers (69%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude T1=T1c drops 9/13 losers (69%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend AGAINST trade

### W17.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 mildly against

### W18.  `H20=H20a AND T4=T4c AND ZS=ZS5`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude T1=T1a drops 8/10 losers (80%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W19.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude T1=T1c drops 10/10 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20a AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude T1=T1a drops 8/10 losers (80%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W21.  `T1=T1a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 6/12 losers (50%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W22.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 mildly against

### W23.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when 4h trend AGAINST trade

### W24.  `H20=H20b AND T4=T4a AND session_bucket=asia`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W25.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude T1=T1a drops 8/10 losers (80%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=131  W=45/L=86  WR=34.4%
- Sharpen: sharpest is T4=T4a (21/86 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=119  W=40/L=79  WR=33.6%
- Sharpen: sharpest is T4=T4a (21/79 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=118  W=40/L=78  WR=33.9%
- Sharpen: sharpest is BBP=BBP4 (25/78 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L04.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=118  W=44/L=74  WR=37.3%
- Sharpen: sharpest is ZS=ZS3 (21/74 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS3 (20/67 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L06.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is T4=T4a (21/69 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L07.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (22/68 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L08.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=108  W=43/L=65  WR=39.8%
- Sharpen: sharpest is BBP=BBP4 (25/65 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=96  W=32/L=64  WR=33.3%
- Sharpen: sharpest is ZS=ZS3 (17/64 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L10.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=74  W=11/L=63  WR=14.9%
- Sharpen: sharpest is T1=T1a (27/63 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L11.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=74  W=11/L=63  WR=14.9%
- Sharpen: sharpest is T1=T1a (27/63 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L12.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is T4=T4a (22/47 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20e AND T1=T1c AND ZS=ZS5`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is session_bucket=london_open (10/46 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L14.  `H20=H20e AND H60=H60e AND BBP=BBP5`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is T4=T4a (22/45 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is T4=T4a (22/45 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is T4=T4a (22/45 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is T4=T4a (22/45 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is T4=T4a (22/45 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L19.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is T1=T1c (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L20.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (10/44 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L21.  `H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=69  W=22/L=47  WR=31.9%
- Sharpen: sharpest is session_bucket=asia (22/47 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L22.  `H60=H60d AND RSI=RSI4 AND direction_exec=short`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (22/44 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 50-60 upper neutral  •  ONLY when session=asia

### L23.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=london_open (10/42 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L24.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is H20=H20a (17/42 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L25.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=68  W=9/L=59  WR=13.2%
- Sharpen: sharpest is T1=T1a (23/59 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(41/30) | H20e(28/41) |
| H60 | — | — |
| T1 | T1a(59/47) | T1c(41/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
