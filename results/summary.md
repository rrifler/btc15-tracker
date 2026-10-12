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
- Windows scored: 1121; excluded: 0
- Fill rate: 16.7% of scored windows had a fill (13 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 92/204 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-12T14:45Z (market 5562096, result down)
Scored: p1 up filled at 104s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.48, 6s@0.5, 6s@0.4867249351, 9s@0.5, 9s@0.5, 11s@0.48, 11s@0.49, 14s@0.48, 21s@0.4599999387, 96s@0.25, 99s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4899999799, 2s@0.5, 3s@0.53, 3s@0.53, 6s@0.51, 12s@0.53, 17s@0.5299998463, 21s@0.5899999725, 21s@0.5609957239, 21s@0.5499999693, 21s@0.54, 23s@0.59 ...

### 2026-10-12T16:00Z (market 5566142, result up)
Scored: p1 down filled at 77s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.5, 5s@0.51, 6s@0.5, 6s@0.5, 6s@0.5326228827, 14s@0.58, 14s@0.5799999768, 17s@0.6, 17s@0.5999999925, 17s@0.5999999925, 20s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999886, 6s@0.45, 77s@0.2, 77s@0.2, 78s@0.1899999962, 84s@0.19, 86s@0.189999999, 87s@0.19, 92s@0.1899999962, 92s@0.1761290323, 92s@0.1541375, 96s@0.17 ...

### 2026-10-12T18:15Z (market 5574618, result down)
Scored: p1 up filled at 104s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.47, 3s@0.47, 104s@0.225, 107s@0.21, 113s@0.2199999974, 119s@0.219999978, 120s@0.22, 122s@0.2199999974, 128s@0.2, 131s@0.2099999958, 131s@0.2099999983, 131s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.54, 3s@0.54, 5s@0.6199999651, 5s@0.6199999449, 6s@0.609999986, 12s@0.609999986, 18s@0.64, 18s@0.6259027778, 18s@0.63, 18s@0.62, 18s@0.63, 18s@0.64 ...

### 2026-10-12T19:00Z (market 5578878, result down)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.56, 5s@0.6, 5s@0.5973333333, 5s@0.6499999594, 6s@0.652520346, 6s@0.64, 6s@0.5599999851, 8s@0.6699998822, 9s@0.6699999971, 11s@0.7299998102, 11s@0.72, 11s@0.6999999754 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.25, 32s@0.25, 72s@0.21, 78s@0.21, 86s@0.2099999969, 89s@0.21, 108s@0.2, 110s@0.17, 114s@0.14, 114s@0.15, 114s@0.16, 114s@0.16 ...


_Updated 2026-10-12 19:25Z_
