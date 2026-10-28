# BTC 15-min strategy tracker: FAIL

Data source: INTL_PROXY. INTL_PROXY means trades from the international exchange, used because the US gateway publishes no public trade history.
Real money needs PASS in both the backtest and the live paper run, with the live hit rate within 8 points of the backtest.

## Backtest

- Verdict: **FAIL**
- Windows scored: 700; excluded: 0
- Fill rate: 16.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 52 of 118 = 44.1% (95% range 35.4% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.35 (balance $7.65 from $20)
- Longest losing streak: 9
- Strict vs touch: strict 52/118 = 44.1%; touch 67/136 = 49.3%. The verdict uses strict.

## Live paper run

- Verdict: **FAIL**
- Windows scored: 2613; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.2% of scored windows had a fill (327 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 259/557 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-28T03:00Z (market 6288170, result down)
Scored: p1 up filled at 32s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.25, 32s@0.2399999808, 33s@0.2399999997, 41s@0.2399999981, 45s@0.2199999962, 54s@0.2275027144, 57s@0.2299999989, 66s@0.229999994, 80s@0.24, 80s@0.246875, 195s@0.2299999517, 195s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5674778669, 2s@0.61, 3s@0.58, 3s@0.5799999809, 3s@0.57, 3s@0.5699999961, 3s@0.5699999923, 3s@0.5699999923, 5s@0.6199999587, 5s@0.6199999587, 5s@0.61, 5s@0.5999999607 ...

### 2026-10-28T04:30Z (market 6289703, result up)
Scored: p1 down filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4899998383, 4s@0.4899998383, 7s@0.4899999183, 8s@0.4899998383, 32s@0.5099998215, 43s@0.5, 70s@0.51, 71s@0.6099999836, 71s@0.56, 71s@0.5387755014, 71s@0.5399999848, 73s@0.6099999913 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.519999985, 4s@0.5199999792, 10s@0.5, 35s@0.5, 37s@0.5, 38s@0.5099999442, 43s@0.51, 89s@0.24, 104s@0.23, 106s@0.23, 106s@0.23, 106s@0.23 ...

### 2026-10-28T05:00Z (market 6290630, result down)
Scored: p1 up filled at 119s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.4799999616, 20s@0.5, 112s@0.25, 115s@0.25, 119s@0.2399999808, 122s@0.24, 124s@0.24, 124s@0.25, 194s@0.25, 215s@0.23, 226s@0.21, 226s@0.2199999995 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.51, 11s@0.51, 11s@0.5099999776, 20s@0.509999914, 25s@0.51, 25s@0.51, 26s@0.5799999658, 26s@0.53, 32s@0.58, 41s@0.5699999886, 43s@0.5999997692, 44s@0.6067573069 ...

### 2026-10-28T07:45Z (market 6293974, result up)
Scored: p1 down filled at 25s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.72, 1s@0.7, 2s@0.5799999988, 2s@0.5899998466, 2s@0.61, 2s@0.72, 4s@0.6923214286, 4s@0.7099999966, 4s@0.71, 4s@0.7099999946, 4s@0.7099999896, 4s@0.6625396825 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 13s@0.25, 16s@0.25, 19s@0.25, 22s@0.25, 25s@0.2, 34s@0.18, 35s@0.18, 40s@0.1699999983, 41s@0.1699999983, 44s@0.1699999983, 46s@0.1703419753, 46s@0.1699999983 ...

### 2026-10-28T08:00Z (market 6294300, result up)
Scored: p1 down filled at 61s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.52, 7s@0.6, 7s@0.5699999886, 7s@0.51, 7s@0.55, 7s@0.53, 7s@0.6, 7s@0.59999994, 7s@0.5416666667, 7s@0.6, 7s@0.5832393135, 7s@0.5199999843 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.509999956, 7s@0.5326270937, 7s@0.49, 7s@0.49, 7s@0.4799999941, 7s@0.51, 7s@0.5, 7s@0.49, 7s@0.4914705882, 59s@0.25, 61s@0.2399999952, 62s@0.2399999808 ...


_Updated 2026-10-28 09:33Z_
