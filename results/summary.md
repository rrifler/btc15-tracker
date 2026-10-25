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
- Windows scored: 2352; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.0% of scored windows had a fill (274 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 226/496 = 45.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-25T09:00Z (market 6113654, result down)
Scored: p1 down filled at 50s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5599999851, 11s@0.5799999768, 11s@0.5599999642, 12s@0.62, 12s@0.58, 12s@0.6156995573, 12s@0.61, 24s@0.62, 27s@0.69, 30s@0.71, 30s@0.7199999424, 32s@0.7199999835 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 50s@0.22, 50s@0.22, 53s@0.22, 77s@0.46, 84s@0.45, 89s@0.4599999669, 92s@0.469999906, 95s@0.57, 95s@0.57, 95s@0.47, 96s@0.5699999942, 96s@0.57 ...

### 2026-10-25T10:45Z (market 6115568, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.549999981, 2s@0.55, 2s@0.5499998234, 2s@0.5499998503, 2s@0.54, 2s@0.55, 2s@0.55, 3s@0.5335604755, 3s@0.5299999251, 3s@0.5299999196, 3s@0.5399999942, 3s@0.5299998463 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.4667857143, 9s@0.48, 24s@0.469999906, 24s@0.469999971, 32s@0.48, 32s@0.49, 33s@0.5, 33s@0.5338214834, 35s@0.54, 36s@0.64, 36s@0.6 ...

### 2026-10-25T11:00Z (market 6116735, result up)
Scored: p1 down filled at 17s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6799998912, 6s@0.7, 11s@0.7299999939, 11s@0.73, 12s@0.75, 12s@0.75, 15s@0.7599999763, 15s@0.76, 15s@0.76, 15s@0.76, 15s@0.76, 15s@0.75 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 17s@0.23, 26s@0.14, 33s@0.11, 33s@0.12, 35s@0.1281132075, 35s@0.12, 36s@0.11, 38s@0.1099999991, 39s@0.07, 39s@0.1, 41s@0.08, 44s@0.08 ...

### 2026-10-25T11:15Z (market 6117425, result up)
Scored: p1 down filled at 59s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.63, 5s@0.6299999306, 5s@0.63, 5s@0.6299999275, 5s@0.5899999657, 6s@0.64, 17s@0.66, 18s@0.68, 18s@0.68, 18s@0.66, 20s@0.7, 24s@0.7 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.47, 59s@0.2099999952, 66s@0.21, 66s@0.2, 69s@0.25, 75s@0.23, 75s@0.23, 75s@0.23, 150s@0.25, 194s@0.1047618998, 194s@0.1, 194s@0.1 ...

### 2026-10-25T11:45Z (market 6118122, result up)
Scored: p1 down filled at 65s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6712096323, 0s@0.66, 0s@0.66, 5s@0.65, 14s@0.61, 15s@0.62, 15s@0.6117839193, 15s@0.62, 15s@0.62, 15s@0.62, 23s@0.6229400074, 26s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 65s@0.24, 66s@0.2199999914, 66s@0.24, 68s@0.23, 68s@0.23, 144s@0.22, 149s@0.21, 149s@0.21, 149s@0.21, 152s@0.24, 159s@0.2399999808, 209s@0.219999978 ...


_Updated 2026-10-25 15:33Z_
