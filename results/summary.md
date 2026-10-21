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
- Windows scored: 1909; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (185 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 180/396 = 45.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-20T21:15Z (market 5940366, result up)
Scored: p1 down filled at 45s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5799999768, 3s@0.5799999768, 6s@0.59, 6s@0.59, 6s@0.59, 6s@0.58, 8s@0.59, 8s@0.585746, 8s@0.59, 9s@0.5599999851, 11s@0.559999776, 17s@0.54 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.45, 9s@0.45, 11s@0.45, 14s@0.4679166667, 15s@0.47, 20s@0.4599999034, 20s@0.46, 26s@0.46, 32s@0.46, 45s@0.2, 45s@0.2, 47s@0.19 ...

### 2026-10-20T23:00Z (market 5950902, result down)
Scored: p1 up filled at 86s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999387, 3s@0.469999906, 5s@0.459999996, 86s@0.24, 87s@0.25, 90s@0.25, 162s@0.25, 162s@0.25, 162s@0.25, 162s@0.25, 165s@0.2299999993, 168s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5355371759, 5s@0.5499998396, 5s@0.5499999018, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55, 8s@0.55, 8s@0.55, 8s@0.55, 8s@0.55 ...

### 2026-10-20T23:45Z (market 5951389, result up)
Scored: p1 down filled at 42s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 5s@0.5299999282, 5s@0.52, 5s@0.5284147083, 8s@0.5479166667, 9s@0.57, 11s@0.64, 11s@0.6499999409, 11s@0.64, 11s@0.64, 11s@0.64, 11s@0.5999999758 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4622562801, 5s@0.4899999984, 6s@0.47, 30s@0.25, 42s@0.2399999808, 47s@0.24, 54s@0.24, 56s@0.24, 66s@0.21, 66s@0.2199999945, 68s@0.23, 68s@0.23 ...

### 2026-10-21T00:00Z (market 5951482, result up)
Scored: p1 up filled at 18s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.469999906, 18s@0.23, 18s@0.2299999945, 20s@0.23, 20s@0.23, 20s@0.229999994, 20s@0.229999994, 21s@0.22, 21s@0.2299999517, 21s@0.229999994, 23s@0.2299999517, 24s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.539999986, 3s@0.55, 6s@0.6199999868, 6s@0.62, 8s@0.6415401023, 8s@0.64, 8s@0.6222413793, 11s@0.64, 15s@0.6699999882, 15s@0.64, 15s@0.63, 15s@0.62 ...


_Updated 2026-10-21 00:45Z_
