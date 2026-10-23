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
- Windows scored: 2133; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.0% of scored windows had a fill (232 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 204/448 = 45.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-23T02:30Z (market 6034202, result up)
Scored: p1 down filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.48, 6s@0.5099999516, 6s@0.51, 6s@0.5199999843, 6s@0.5199999792, 6s@0.52, 14s@0.52, 14s@0.5199999406, 14s@0.5199999406, 14s@0.51, 14s@0.5099999215 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299998463, 3s@0.5175, 5s@0.4899998383, 6s@0.49, 8s@0.5, 8s@0.49, 8s@0.4922994652, 9s@0.5099998215, 14s@0.49, 15s@0.4899999929, 15s@0.46, 87s@0.25 ...

### 2026-10-23T03:15Z (market 6034535, result down)
Scored: p1 up filled at 92s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4599997976, 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.47, 3s@0.47, 5s@0.4899998383, 5s@0.48, 6s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999732, 5s@0.52, 6s@0.52, 8s@0.5, 8s@0.5, 9s@0.5099999137, 9s@0.5, 12s@0.55, 15s@0.55, 15s@0.55, 17s@0.55, 17s@0.5499999214 ...

### 2026-10-23T03:30Z (market 6034582, result up)
Scored: p1 down filled at 66s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.469999998, 3s@0.47, 5s@0.469999906, 6s@0.56, 6s@0.51, 6s@0.55, 20s@0.55, 26s@0.6099999543, 26s@0.6099998597, 38s@0.65, 42s@0.6499999044, 42s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999622, 8s@0.4599999034, 66s@0.24, 69s@0.25, 69s@0.25, 69s@0.24, 249s@0.25, 249s@0.25, 252s@0.25, 279s@0.2199999937, 285s@0.23, 309s@0.25 ...

### 2026-10-23T03:45Z (market 6034685, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.64, 6s@0.64, 8s@0.64, 9s@0.69, 12s@0.6899999808, 14s@0.69, 26s@0.58, 27s@0.62, 27s@0.635, 27s@0.61, 29s@0.62, 29s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 114s@0.2099999934, 117s@0.22, 117s@0.23, 119s@0.2199999955, 123s@0.2099999895, 134s@0.23, 143s@0.2, 156s@0.2, 158s@0.21, 173s@0.2, 179s@0.1899999941, 191s@0.1699999983 ...

### 2026-10-23T05:00Z (market 6036271, result up)
Scored: p1 down filled at 86s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5680232738, 3s@0.554455439, 9s@0.59, 9s@0.589999844, 20s@0.64, 20s@0.64, 20s@0.64, 56s@0.72, 57s@0.74, 63s@0.75, 63s@0.73, 63s@0.73 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 86s@0.2399999808, 93s@0.22, 102s@0.2, 104s@0.2, 122s@0.23, 123s@0.25, 131s@0.2099999895, 132s@0.22, 134s@0.2270652174, 152s@0.2399999923, 153s@0.2399999959, 156s@0.239999998 ...


_Updated 2026-10-23 08:39Z_
