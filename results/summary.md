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
- Windows scored: 933; excluded: 0
- Fill rate: 16.4% of scored windows had a fill (0 too small)
- Fills that reached 45c: 71 of 153 = 46.4% (95% range 38.7% to 54.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.70 (balance $7.30 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 71/153 = 46.4%; touch 78/166 = 47.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-10T14:30Z (market 5458054, result up)
Scored: p1 down filled at 6s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.629999937, 0s@0.62, 0s@0.61, 0s@0.6, 0s@0.5941747457, 0s@0.58, 0s@0.5799999673, 0s@0.57, 1s@0.63, 1s@0.6099999322, 3s@0.70246, 3s@0.649585992 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.25, 6s@0.219999978, 6s@0.2299999998, 6s@0.2299999961, 7s@0.22, 7s@0.2199999983, 19s@0.49, 19s@0.45, 19s@0.4535205184, 22s@0.469999998, 24s@0.47, 30s@0.5073003874 ...

### 2026-10-10T15:30Z (market 5458838, result up)
Scored: p1 down filled at 103s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999776, 4s@0.48, 12s@0.5, 16s@0.5199999844, 18s@0.5314646753, 21s@0.55, 28s@0.54, 28s@0.56, 30s@0.6425, 30s@0.62, 34s@0.65, 34s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 3s@0.5, 3s@0.5, 27s@0.4599999034, 28s@0.47, 103s@0.1699999983, 105s@0.17, 108s@0.1635848983, 108s@0.16, 109s@0.16, 114s@0.17, 117s@0.1699999986 ...

### 2026-10-10T18:30Z (market 5470792, result up)
Scored: p1 down filled at 70s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999914, 4s@0.5699999886, 13s@0.5499999995, 22s@0.55, 25s@0.5499999841, 31s@0.5549195162, 36s@0.57, 37s@0.5903225426, 37s@0.59, 37s@0.5899999458, 37s@0.6, 37s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.46, 15s@0.46, 25s@0.4599997976, 25s@0.46, 70s@0.2099999895, 72s@0.21, 72s@0.2099999895, 72s@0.21, 72s@0.21, 73s@0.21, 73s@0.21, 73s@0.21 ...

### 2026-10-10T19:30Z (market 5473305, result up)
Scored: p1 down filled at 117s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5, 18s@0.49, 18s@0.5, 22s@0.5, 22s@0.5, 27s@0.5, 27s@0.5, 45s@0.53, 54s@0.5299999006, 54s@0.5299999787, 58s@0.5299999587, 67s@0.568538963 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.48, 7s@0.48, 12s@0.49, 12s@0.49, 12s@0.48, 13s@0.5, 13s@0.5, 13s@0.5, 15s@0.51, 16s@0.51, 16s@0.5099999749, 16s@0.51 ...


_Updated 2026-10-10 20:22Z_
