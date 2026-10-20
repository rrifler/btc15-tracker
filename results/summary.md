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
- Windows scored: 1813; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.4% of scored windows had a fill (160 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 166/370 = 44.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-19T18:30Z (market 5900104, result up)
Scored: p1 down filled at 87s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6, 0s@0.6, 3s@0.629999995, 3s@0.6299999685, 5s@0.64, 5s@0.629999995, 6s@0.6299999084, 8s@0.63, 8s@0.63, 8s@0.63, 8s@0.6299998362, 11s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 69s@0.25, 75s@0.25, 87s@0.21, 89s@0.2223076923, 93s@0.23, 95s@0.23, 96s@0.25, 96s@0.25, 96s@0.25, 96s@0.25, 96s@0.25, 96s@0.25 ...

### 2026-10-19T18:45Z (market 5900313, result up)
Scored: p1 down filled at 54s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.57, 6s@0.6, 6s@0.57, 6s@0.57, 9s@0.5999999032, 12s@0.61, 21s@0.64, 23s@0.65, 23s@0.649999974, 27s@0.6899999546, 33s@0.6799996464, 33s@0.6799999238 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 54s@0.23, 54s@0.24, 54s@0.23, 56s@0.24, 59s@0.25, 227s@0.24, 227s@0.25, 227s@0.25, 231s@0.25, 237s@0.2299999993, 249s@0.229999987, 258s@0.2299999782 ...

### 2026-10-19T19:00Z (market 5902374, result down)
Scored: p1 up filled at 80s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4799998464, 6s@0.47, 6s@0.48, 6s@0.4772820379, 6s@0.47, 8s@0.4599999681, 80s@0.24, 80s@0.24, 83s@0.23, 92s@0.23, 95s@0.24, 95s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 3s@0.5399999568, 6s@0.53, 9s@0.58, 17s@0.6, 20s@0.59999988, 21s@0.5999999976, 24s@0.5999999976, 26s@0.6, 26s@0.6, 27s@0.5999999976, 29s@0.6099999986 ...

### 2026-10-19T19:45Z (market 5904226, result down)
Scored: p1 up filled at 74s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.48, 6s@0.5, 74s@0.2, 75s@0.2, 77s@0.2, 78s@0.2, 81s@0.2, 87s@0.18, 90s@0.18, 93s@0.18, 93s@0.1799999856, 99s@0.1518047367 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299998463, 9s@0.5, 14s@0.59, 14s@0.56, 14s@0.52, 14s@0.52, 17s@0.5899999546, 20s@0.6, 21s@0.599999976, 24s@0.61, 24s@0.6, 24s@0.599999976 ...

### 2026-10-19T21:15Z (market 5907414, result down)
Scored: p1 down filled at 12s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.58, 3s@0.68, 3s@0.644172, 3s@0.65, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.64, 4s@0.73, 4s@0.72, 4s@0.73, 4s@0.72 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.2225, 12s@0.21, 12s@0.22, 12s@0.2299999993, 12s@0.22, 12s@0.23, 12s@0.2299999988, 13s@0.24, 13s@0.23, 13s@0.25, 13s@0.25, 13s@0.24 ...


_Updated 2026-10-20 00:47Z_
