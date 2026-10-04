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
- Windows scored: 349; excluded: 0
- Fill rate: 17.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 29 of 60 = 48.3% (95% range 36.2% to 60.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.05 (balance $13.95 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 29/60 = 48.3%; touch 32/64 = 50.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-04T12:00Z (market 5230692, result down)
Scored: p1 down filled at 106s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.5099999516, 8s@0.55, 10s@0.56, 10s@0.56, 14s@0.55, 17s@0.56, 20s@0.559999776, 38s@0.5299999653, 46s@0.5338764352, 47s@0.54, 67s@0.54, 82s@0.5501522722 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 10s@0.45, 11s@0.45999999, 13s@0.46, 16s@0.45, 28s@0.45, 34s@0.46, 34s@0.46, 35s@0.46, 56s@0.47, 56s@0.47, 68s@0.4699999999, 104s@0.25 ...

### 2026-10-04T12:15Z (market 5231263, result up)
Scored: p1 up filled at 110s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 97s@0.25, 110s@0.23, 116s@0.2, 118s@0.2, 121s@0.1748603786, 121s@0.1899999998, 122s@0.1899999896, 122s@0.19, 122s@0.18, 122s@0.1899999962, 122s@0.17, 122s@0.169999999 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.58, 1s@0.58, 2s@0.6203076746, 5s@0.63, 5s@0.6299998362, 8s@0.64, 8s@0.64, 23s@0.6499998839, 25s@0.649999974, 29s@0.649999805, 37s@0.65, 40s@0.649999805 ...

### 2026-10-04T12:45Z (market 5231654, result down)
Scored: p1 up filled at 91s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 4s@0.4958333333, 4s@0.5099999949, 4s@0.5, 5s@0.5099999516, 5s@0.51, 5s@0.5099998215, 5s@0.5, 5s@0.51, 7s@0.5099999776, 8s@0.5099999812, 8s@0.5099999215 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.58, 1s@0.58, 2s@0.5999999827, 7s@0.5, 13s@0.5, 13s@0.5, 14s@0.46, 16s@0.46, 19s@0.46, 25s@0.47, 26s@0.4673483775, 26s@0.5299999325 ...

### 2026-10-04T13:30Z (market 5233488, result up)
Scored: p1 down filled at 82s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5099998215, 14s@0.5199999792, 23s@0.5099999906, 28s@0.5099999516, 28s@0.5099999935, 35s@0.5099998215, 38s@0.51, 41s@0.5099999516, 52s@0.54, 52s@0.52, 53s@0.5799999987, 53s@0.5699999983 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.51, 7s@0.4899999584, 7s@0.49, 16s@0.49, 22s@0.5, 37s@0.5, 50s@0.469999954, 52s@0.4629098016, 52s@0.47, 53s@0.47, 82s@0.2399999808, 83s@0.2399999868 ...

### 2026-10-04T17:45Z (market 5242771, result down)
Scored: p1 down filled at 67s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6063905114, 4s@0.64, 5s@0.66, 5s@0.65, 5s@0.649999805, 5s@0.64, 7s@0.7260217962, 7s@0.71, 8s@0.6299999973, 10s@0.6199998512, 10s@0.62, 11s@0.6199999958 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.45, 2s@0.45, 2s@0.45, 67s@0.229999994, 80s@0.22, 80s@0.2, 104s@0.1848788556, 106s@0.23, 106s@0.21, 107s@0.23, 112s@0.21 ...


_Updated 2026-10-04 18:21Z_
