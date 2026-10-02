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

- Verdict: **NOT ENOUGH DATA**
- Windows scored: 105; excluded: 0
- Fill rate: 21.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 11 of 23 = 47.8% (95% range 29.2% to 67.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-2.75 (balance $17.25 from $20)
- Longest losing streak: 2
- Strict vs touch: strict 11/23 = 47.8%; touch 14/26 = 53.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-01T21:15Z (market 5164709, result down)
Scored: p1 up filled at 95s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 93s@0.25, 93s@0.25, 93s@0.25, 95s@0.2299999782, 99s@0.23, 99s@0.2299999992, 101s@0.2299999517, 101s@0.22, 101s@0.23, 101s@0.2299999992, 101s@0.22, 105s@0.2299999975 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.6047530289, 6s@0.6299999764, 11s@0.61, 14s@0.6199998512, 15s@0.6099999488, 18s@0.6099998206, 20s@0.6, 20s@0.6099999968, 23s@0.6099998597, 32s@0.6999999905, 32s@0.71, 32s@0.7 ...

### 2026-10-01T22:00Z (market 5165047, result up)
Scored: p1 down filled at 68s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 6s@0.45, 6s@0.45, 9s@0.46, 11s@0.48, 12s@0.47, 17s@0.5275117272, 18s@0.55, 18s@0.5599998098, 18s@0.55, 18s@0.54, 18s@0.5399999151 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5049800368, 3s@0.5599999961, 5s@0.5599998682, 8s@0.53, 9s@0.5299999868, 9s@0.549999945, 11s@0.5299999868, 11s@0.5399999568, 14s@0.5499999828, 18s@0.4599999828, 68s@0.21, 68s@0.2099999995 ...

### 2026-10-01T23:00Z (market 5166144, result down)
Scored: p1 up filled at 68s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 68s@0.2490384615, 89s@0.25, 107s@0.24, 111s@0.25, 119s@0.25, 120s@0.25, 219s@0.4599999387, 219s@0.45, 231s@0.4599999387, 231s@0.4599999387, 237s@0.45, 248s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 5s@0.5441666667, 6s@0.6410612977, 6s@0.6335979513, 8s@0.64, 9s@0.68, 9s@0.6999999054, 9s@0.6999999754, 9s@0.67, 9s@0.6699999823, 9s@0.6799999547, 9s@0.67 ...

### 2026-10-02T00:00Z (market 5166950, result up)
Scored: p1 up filled at 51s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 51s@0.22, 53s@0.22, 53s@0.22, 54s@0.2299999517, 65s@0.2467105263, 65s@0.23, 72s@0.2, 75s@0.2099999958, 75s@0.21, 77s@0.2, 77s@0.25, 80s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6, 5s@0.62, 5s@0.63, 5s@0.6, 5s@0.59999988, 6s@0.64, 6s@0.64, 8s@0.64, 8s@0.64, 9s@0.66, 9s@0.65, 11s@0.6799999946 ...

### 2026-10-02T00:45Z (market 5167489, result down)
Scored: p1 up filled at 50s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4579780731, 50s@0.229999994, 63s@0.1899999986, 68s@0.17, 68s@0.19, 75s@0.17, 77s@0.17, 77s@0.17, 77s@0.17, 77s@0.17, 77s@0.17, 77s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 2s@0.56, 3s@0.59, 3s@0.5750427291, 5s@0.628, 5s@0.6, 8s@0.64, 8s@0.65, 9s@0.646822477, 9s@0.64, 24s@0.65, 27s@0.7199999726 ...


_Updated 2026-10-02 03:24Z_
