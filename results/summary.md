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
- Windows scored: 2450; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (294 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 241/521 = 46.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-26T10:00Z (market 6183229, result down)
Scored: p1 up filled at 108s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 17s@0.4599997976, 102s@0.25, 104s@0.25, 108s@0.24, 108s@0.25, 110s@0.24, 114s@0.2199999993, 114s@0.21, 122s@0.2199999979, 126s@0.2299999993, 128s@0.2299999517, 149s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.5299999505, 3s@0.53, 6s@0.55, 9s@0.559999776, 9s@0.5599999642, 12s@0.54999989, 17s@0.549999986, 21s@0.549999945, 35s@0.64, 35s@0.64, 35s@0.6041904325 ...

### 2026-10-26T10:30Z (market 6184073, result up)
Scored: p1 down filled at 105s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.5, 5s@0.5, 8s@0.5, 9s@0.5, 9s@0.5, 11s@0.5099999516, 14s@0.51, 33s@0.51, 35s@0.59, 35s@0.5899999656, 35s@0.5899999656 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4813572271, 12s@0.5, 104s@0.25, 104s@0.25, 105s@0.19, 105s@0.25, 107s@0.22, 107s@0.2, 111s@0.25, 116s@0.24, 206s@0.2399999808, 218s@0.25 ...

### 2026-10-26T11:30Z (market 6186116, result up)
Scored: p1 up filled at 83s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.47, 14s@0.4599999986, 20s@0.469999906, 20s@0.46, 20s@0.4639724224, 20s@0.4599999842, 20s@0.4599999924, 83s@0.23, 83s@0.22, 83s@0.22, 99s@0.229999994, 102s@0.2299999517 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.549999956, 18s@0.54, 21s@0.55, 21s@0.5777593025, 23s@0.62, 23s@0.6099999588, 26s@0.62, 32s@0.63, 32s@0.6676706226, 32s@0.659999968, 39s@0.68, 41s@0.68 ...

### 2026-10-26T13:00Z (market 6192268, result down)
Scored: p1 up filled at 90s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998383, 3s@0.49, 8s@0.5, 8s@0.4899998383, 11s@0.48, 12s@0.47, 14s@0.45, 17s@0.4599999472, 18s@0.4932328454, 21s@0.479999993, 87s@0.25, 89s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.48, 0s@0.48, 0s@0.48, 2s@0.48, 3s@0.5, 3s@0.49, 23s@0.6099999848, 23s@0.5799999768, 23s@0.6, 26s@0.61, 29s@0.64, 30s@0.63 ...


_Updated 2026-10-26 16:06Z_
