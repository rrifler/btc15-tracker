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
- Windows scored: 2208; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (247 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 214/466 = 45.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-23T22:00Z (market 6066753, result down)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.57, 3s@0.5799999768, 5s@0.6899999966, 5s@0.69, 5s@0.6799999562, 5s@0.68, 5s@0.6799999299, 5s@0.6799999212, 5s@0.6848838279, 5s@0.6799998776, 5s@0.6799999892, 5s@0.6799999856 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 20s@0.25, 20s@0.25, 20s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25 ...

### 2026-10-23T22:15Z (market 6067265, result up)
Scored: p1 down filled at 107s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.530899451, 6s@0.5399999568, 6s@0.54, 8s@0.5899999705, 18s@0.57, 21s@0.5799999768, 33s@0.5899999705, 35s@0.5899999705, 42s@0.6499999495, 45s@0.6, 47s@0.5799999768, 65s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.48, 12s@0.47, 14s@0.47, 105s@0.25, 107s@0.24, 152s@0.25, 153s@0.25, 209s@0.2359982883, 215s@0.25, 216s@0.25, 231s@0.24, 257s@0.24 ...

### 2026-10-23T22:30Z (market 6067895, result down)
Scored: p1 up filled at 42s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 42s@0.24, 42s@0.2399999808, 42s@0.24, 44s@0.23, 44s@0.23, 44s@0.24, 44s@0.23, 44s@0.24, 45s@0.21, 45s@0.21, 45s@0.2099999779, 45s@0.2099999895 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5824248662, 6s@0.59999988, 6s@0.59, 8s@0.6, 8s@0.59999994, 9s@0.599999976, 9s@0.599999988, 12s@0.6499999923, 12s@0.65, 12s@0.6499999789, 12s@0.65, 12s@0.6499999665 ...

### 2026-10-23T23:30Z (market 6070257, result down)
Scored: p1 up filled at 84s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 84s@0.22, 84s@0.22, 93s@0.2188675918, 93s@0.22, 93s@0.2199999955, 93s@0.2099999962, 101s@0.21, 102s@0.2299999517, 102s@0.22, 104s@0.2299999996, 107s@0.24, 107s@0.2399999852 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.59999988, 6s@0.6012998894, 8s@0.62, 8s@0.6, 9s@0.6199998946, 23s@0.6699999988, 26s@0.6699999196, 38s@0.67, 63s@0.7299999083, 65s@0.72, 65s@0.7199999844, 78s@0.75 ...

### 2026-10-23T23:45Z (market 6070427, result up)
Scored: p1 down filled at 35s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.52, 2s@0.63, 3s@0.64, 3s@0.64, 3s@0.63, 5s@0.5799999768, 6s@0.58, 9s@0.5799999768, 14s@0.579999944, 14s@0.5799999448, 14s@0.58, 17s@0.5799999768 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 35s@0.23, 44s@0.23, 44s@0.23, 44s@0.23, 45s@0.24, 45s@0.23, 47s@0.25, 48s@0.22, 50s@0.229999994, 66s@0.19, 66s@0.2, 72s@0.21 ...


_Updated 2026-10-24 03:34Z_
