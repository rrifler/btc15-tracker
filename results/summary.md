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
- Windows scored: 1117; excluded: 0
- Fill rate: 16.6% of scored windows had a fill (11 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 90/202 = 44.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-12T12:15Z (market 5554148, result down)
Scored: p1 up filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 5s@0.47, 5s@0.48, 5s@0.4705882353, 89s@0.23, 89s@0.24, 90s@0.23, 93s@0.2399999808, 105s@0.24, 153s@0.23, 186s@0.23, 194s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5039849624, 2s@0.5, 5s@0.549999945, 9s@0.6099999322, 9s@0.6099999962, 21s@0.6099999116, 24s@0.6261538462, 26s@0.6699999863, 26s@0.66, 26s@0.6699999984, 26s@0.64, 26s@0.64 ...

### 2026-10-12T12:45Z (market 5557504, result down)
Scored: p1 down filled at 75s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.59, 3s@0.59, 3s@0.5899999145, 3s@0.5899999458, 3s@0.5699999873, 3s@0.5899999954, 3s@0.5838058098, 5s@0.59, 5s@0.59, 6s@0.59, 6s@0.5899999841, 6s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 75s@0.25, 75s@0.24, 77s@0.25, 132s@0.23, 137s@0.2099999983, 147s@0.2099999895, 147s@0.21, 149s@0.2099999983, 149s@0.2099999895, 162s@0.19, 203s@0.16, 204s@0.16 ...

### 2026-10-12T14:45Z (market 5562096, result down)
Scored: p1 up filled at 104s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.48, 6s@0.5, 6s@0.4867249351, 9s@0.5, 9s@0.5, 11s@0.48, 11s@0.49, 14s@0.48, 21s@0.4599999387, 96s@0.25, 99s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4899999799, 2s@0.5, 3s@0.53, 3s@0.53, 6s@0.51, 12s@0.53, 17s@0.5299998463, 21s@0.5899999725, 21s@0.5609957239, 21s@0.5499999693, 21s@0.54, 23s@0.59 ...

### 2026-10-12T16:00Z (market 5566142, result up)
Scored: p1 down filled at 77s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.5, 5s@0.51, 6s@0.5, 6s@0.5, 6s@0.5326228827, 14s@0.58, 14s@0.5799999768, 17s@0.6, 17s@0.5999999925, 17s@0.5999999925, 20s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999886, 6s@0.45, 77s@0.2, 77s@0.2, 78s@0.1899999962, 84s@0.19, 86s@0.189999999, 87s@0.19, 92s@0.1899999962, 92s@0.1761290323, 92s@0.1541375, 96s@0.17 ...


_Updated 2026-10-12 18:29Z_
