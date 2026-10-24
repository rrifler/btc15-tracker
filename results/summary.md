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
- Windows scored: 2264; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.0% of scored windows had a fill (257 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 220/477 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-24T13:30Z (market 6081697, result down)
Scored: p1 up filled at 50s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4854056325, 2s@0.4982608696, 47s@0.25, 48s@0.25, 50s@0.18, 50s@0.2, 50s@0.18, 50s@0.18, 50s@0.18, 50s@0.1799999986, 50s@0.18, 50s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5200500522, 8s@0.5190989211, 8s@0.5299999868, 8s@0.53, 9s@0.5099999776, 9s@0.5199999792, 12s@0.5099999474, 12s@0.5099999431, 17s@0.5099999551, 23s@0.5599999628, 23s@0.55, 23s@0.53 ...

### 2026-10-24T13:45Z (market 6082062, result down)
Scored: p1 up filled at 54s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.4799998464, 8s@0.48, 11s@0.4799999846, 12s@0.5, 18s@0.4899999183, 21s@0.469999906, 33s@0.459999977, 36s@0.47, 54s@0.2488202478, 54s@0.2299999978, 54s@0.229999987, 54s@0.1899999989 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.459999988, 6s@0.4818188766, 12s@0.5099999949, 14s@0.5099998215, 18s@0.5199999956, 48s@0.5199999972, 48s@0.5850952941, 48s@0.5454228186, 50s@0.72, 50s@0.6588006108, 50s@0.6180162368, 50s@0.689999984 ...

### 2026-10-24T14:15Z (market 6082682, result down)
Scored: p1 up filled at 30s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.25, 12s@0.25, 12s@0.25, 30s@0.25, 30s@0.23, 32s@0.236692607, 32s@0.2479553705, 33s@0.2114206105, 33s@0.2128092416, 33s@0.2099999957, 33s@0.2, 33s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.65, 0s@0.65, 0s@0.6599999974, 0s@0.6599997888, 3s@0.6799999975, 3s@0.6699999994, 5s@0.67, 6s@0.69, 6s@0.67, 6s@0.67, 8s@0.7099999533, 8s@0.68 ...

### 2026-10-24T14:30Z (market 6082721, result down)
Scored: p1 down filled at 71s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.58, 3s@0.56, 3s@0.5599999496, 3s@0.5599999527, 5s@0.5584878788, 5s@0.55, 5s@0.5499998396, 5s@0.55, 5s@0.549999945, 6s@0.5499998949, 6s@0.5874299924, 6s@0.5499999904 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 3s@0.45, 5s@0.4599997976, 5s@0.4599999687, 5s@0.4543333333, 5s@0.45, 6s@0.4599999641, 6s@0.4599999687, 24s@0.4599999687, 26s@0.45, 26s@0.46, 71s@0.23 ...

### 2026-10-24T15:15Z (market 6083670, result down)
Scored: p1 up filled at 83s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.58, 3s@0.54, 3s@0.54, 3s@0.5399999568, 3s@0.5299999399, 3s@0.52, 3s@0.51, 3s@0.52, 3s@0.51, 3s@0.5078791667, 5s@0.5199999792, 5s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 3s@0.5, 3s@0.4579061668, 3s@0.5, 3s@0.45, 3s@0.4845013333, 3s@0.5, 3s@0.45, 3s@0.49, 3s@0.45, 3s@0.47, 5s@0.4758102214 ...


_Updated 2026-10-24 17:32Z_
