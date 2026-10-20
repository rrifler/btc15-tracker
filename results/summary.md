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
- Windows scored: 1893; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (181 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 176/392 = 44.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-20T15:00Z (market 5927247, result down)
Scored: p1 up filled at 101s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 6s@0.45, 101s@0.23, 101s@0.2299999985, 102s@0.229999994, 108s@0.2199999931, 110s@0.2199999959, 110s@0.2199999959, 110s@0.2199999841, 113s@0.23, 113s@0.23, 119s@0.219999978 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699998454, 3s@0.5799999768, 9s@0.5599999642, 9s@0.5699999886, 9s@0.56, 11s@0.56, 14s@0.6, 14s@0.58, 15s@0.59999988, 18s@0.61, 18s@0.6, 18s@0.6 ...

### 2026-10-20T15:15Z (market 5928237, result up)
Scored: p1 down filled at 95s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.62, 8s@0.57, 8s@0.57, 14s@0.5299999325, 14s@0.5299998463, 15s@0.53, 15s@0.53, 15s@0.53, 17s@0.5099999334, 17s@0.51, 17s@0.5099999672, 17s@0.5099999334 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.45, 9s@0.47, 9s@0.45, 9s@0.45, 11s@0.469999998, 11s@0.47, 11s@0.4699999962, 11s@0.4699999944, 11s@0.4675996159, 12s@0.47, 14s@0.48, 14s@0.48 ...

### 2026-10-20T15:45Z (market 5928627, result up)
Scored: p1 up filled at 38s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 36s@0.25, 36s@0.25, 36s@0.25, 38s@0.24, 38s@0.24, 45s@0.2399999808, 47s@0.25, 47s@0.25, 47s@0.24, 126s@0.25, 137s@0.24, 243s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6099998373, 3s@0.6099997255, 5s@0.6099998597, 6s@0.61, 9s@0.6, 9s@0.61, 11s@0.61, 12s@0.65, 14s@0.65, 14s@0.65, 18s@0.6799999921, 18s@0.68 ...

### 2026-10-20T16:30Z (market 5930645, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.53, 3s@0.51, 3s@0.51, 8s@0.54, 18s@0.6, 20s@0.6, 30s@0.62, 33s@0.6299999181, 51s@0.6499999309, 51s@0.65, 51s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.469999906, 5s@0.47, 6s@0.469999906, 114s@0.219999978, 129s@0.1699999918, 131s@0.15, 134s@0.13, 135s@0.1299999999, 135s@0.13, 137s@0.12, 137s@0.12, 137s@0.12 ...

### 2026-10-20T17:00Z (market 5931608, result down)
Scored: p1 up filled at 116s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 21s@0.46, 21s@0.45455, 116s@0.24, 119s@0.24, 119s@0.24, 119s@0.24, 125s@0.25, 125s@0.25, 282s@0.4699999773, 288s@0.47, 311s@0.469999906, 321s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.559999776, 3s@0.5499999783, 5s@0.56, 9s@0.5899999145, 11s@0.5899999712, 12s@0.5899999712, 15s@0.5899999841, 17s@0.589999941, 27s@0.5699999886, 33s@0.5599999805, 65s@0.61, 65s@0.5999999754 ...


_Updated 2026-10-20 20:37Z_
