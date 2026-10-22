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
- Windows scored: 2029; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (208 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 194/421 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-22T01:00Z (market 6000609, result up)
Scored: p1 up filled at 66s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 66s@0.23, 68s@0.21, 68s@0.2048780488, 68s@0.2, 68s@0.24, 69s@0.2, 69s@0.21, 72s@0.24, 72s@0.21, 72s@0.2325465607, 74s@0.25, 77s@0.2199999974 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.612, 6s@0.6703571429, 6s@0.68, 6s@0.6799998204, 6s@0.64, 6s@0.62, 6s@0.6199999907, 6s@0.64, 6s@0.64, 6s@0.62, 6s@0.62, 9s@0.63 ...

### 2026-10-22T01:30Z (market 6000697, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.54, 2s@0.549999945, 3s@0.5599999328, 3s@0.559999776, 15s@0.5199999792, 18s@0.4799999846, 24s@0.46, 68s@0.21, 69s@0.19, 71s@0.1899999986, 72s@0.18, 77s@0.1499999993 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.469999906, 8s@0.47, 9s@0.4699999888, 15s@0.4899999183, 17s@0.51, 17s@0.49, 18s@0.52, 21s@0.5299998463, 23s@0.54, 27s@0.6280769231, 27s@0.64, 27s@0.555 ...

### 2026-10-22T02:30Z (market 6001638, result up)
Scored: p1 down filled at 102s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6199998512, 3s@0.6199998946, 5s@0.6199999907, 6s@0.6199999945, 6s@0.6199999907, 6s@0.6199998512, 6s@0.6199998512, 8s@0.63, 8s@0.629999995, 8s@0.6299999181, 8s@0.629999995, 8s@0.6254653756 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 98s@0.25, 99s@0.25, 102s@0.22, 105s@0.22, 131s@0.45, 131s@0.45, 131s@0.45, 242s@0.45, 242s@0.45, 242s@0.45, 258s@0.45, 260s@0.46 ...

### 2026-10-22T03:00Z (market 6001992, result down)
Scored: p1 down filled at 81s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.52, 3s@0.5099998215, 3s@0.5099999516, 5s@0.47, 5s@0.4963531378, 6s@0.47, 8s@0.48, 8s@0.48, 15s@0.47, 20s@0.4799999616, 20s@0.48, 23s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.5316666667, 9s@0.5899999544, 9s@0.55, 9s@0.5472080232, 11s@0.5899999819, 15s@0.53, 17s@0.5099999788, 18s@0.51, 18s@0.51, 23s@0.5099999949, 81s@0.23, 83s@0.25 ...

### 2026-10-22T04:45Z (market 6003504, result up)
Scored: p1 down filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5135802165, 5s@0.55, 5s@0.53, 5s@0.52, 6s@0.5599999955, 6s@0.5599999955, 6s@0.5699999914, 6s@0.5488372093, 6s@0.55, 6s@0.5599999955, 6s@0.5599999955, 6s@0.5599999955 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998383, 3s@0.5, 63s@0.2299999864, 63s@0.23, 72s@0.2, 81s@0.14, 89s@0.13, 93s@0.15, 95s@0.16, 102s@0.1499999993, 102s@0.14, 110s@0.1499999925 ...


_Updated 2026-10-22 06:44Z_
