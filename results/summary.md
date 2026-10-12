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
- Windows scored: 1101; excluded: 0
- Fill rate: 16.6% of scored windows had a fill (9 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 89/199 = 44.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-12T08:00Z (market 5541324, result down)
Scored: p1 up filled at 64s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5219452189, 64s@0.19, 64s@0.2099999895, 66s@0.1899999962, 69s@0.2099999895, 73s@0.2299999517, 75s@0.23, 76s@0.2, 79s@0.219999978, 82s@0.21, 87s@0.2199999941, 87s@0.219999978 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5999999613, 4s@0.6, 4s@0.5499999656, 4s@0.5499999656, 4s@0.52, 9s@0.5999999991, 9s@0.64, 9s@0.6434396068, 9s@0.64, 10s@0.6218208184, 10s@0.64, 10s@0.63 ...

### 2026-10-12T08:15Z (market 5541935, result down)
Scored: p1 up filled at 45s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 45s@0.24, 45s@0.25, 55s@0.17, 55s@0.1799999856, 57s@0.1799999755, 58s@0.16, 60s@0.16, 61s@0.18, 61s@0.18, 63s@0.19, 66s@0.19, 67s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.6121836852, 4s@0.64, 4s@0.64, 5s@0.64, 10s@0.64, 10s@0.64, 11s@0.6899999546, 11s@0.68, 11s@0.6799999647, 11s@0.68, 11s@0.68, 11s@0.67 ...

### 2026-10-12T10:15Z (market 5546516, result down)
Scored: p1 up filled at 117s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5199999406, 5s@0.46, 81s@0.25, 81s@0.25, 108s@0.25, 117s@0.24, 152s@0.23, 152s@0.23, 158s@0.22, 159s@0.229999994, 159s@0.22, 182s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.49, 2s@0.4907513148, 2s@0.4899999944, 12s@0.5899999288, 12s@0.5899999725, 12s@0.56, 12s@0.557826087, 15s@0.5699999886, 18s@0.6099999955, 18s@0.6, 18s@0.6, 18s@0.6 ...

### 2026-10-12T10:45Z (market 5547474, result down)
Scored: p1 down filled at 105s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.549999945, 2s@0.5499999904, 2s@0.549999945, 8s@0.5299999399, 12s@0.5299999989, 20s@0.5899999458, 20s@0.56, 20s@0.59, 24s@0.5899999725, 26s@0.5899999725, 32s@0.5899999725, 35s@0.5899999918 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4699999944, 3s@0.4739214823, 6s@0.4699999988, 8s@0.48, 105s@0.24, 108s@0.19, 110s@0.2, 116s@0.2, 116s@0.1930406852, 117s@0.2099999895, 120s@0.19, 122s@0.2 ...

### 2026-10-12T12:15Z (market 5554148, result down)
Scored: p1 up filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 5s@0.47, 5s@0.48, 5s@0.4705882353, 89s@0.23, 89s@0.24, 90s@0.23, 93s@0.2399999808, 105s@0.24, 153s@0.23, 186s@0.23, 194s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5039849624, 2s@0.5, 5s@0.549999945, 9s@0.6099999322, 9s@0.6099999962, 21s@0.6099999116, 24s@0.6261538462, 26s@0.6699999863, 26s@0.66, 26s@0.6699999984, 26s@0.64, 26s@0.64 ...


_Updated 2026-10-12 14:33Z_
