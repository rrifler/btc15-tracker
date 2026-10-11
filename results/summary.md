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
- Windows scored: 957; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 72 of 156 = 46.2% (95% range 38.5% to 54.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-13.00 (balance $7.00 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 72/156 = 46.2%; touch 79/169 = 46.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-10T21:15Z (market 5475064, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599997976, 4s@0.49, 4s@0.471742581, 4s@0.46, 6s@0.49, 6s@0.4899998383, 13s@0.4699999935, 13s@0.469999906, 22s@0.47, 33s@0.4799999616, 34s@0.48, 34s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 3s@0.512563634, 7s@0.51, 13s@0.5399999568, 34s@0.52, 36s@0.52, 36s@0.52, 40s@0.509999935, 45s@0.47, 114s@0.23, 115s@0.2299999819, 118s@0.24 ...

### 2026-10-10T22:45Z (market 5476391, result up)
Scored: p1 up filled at 48s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.2, 51s@0.2, 54s@0.2, 55s@0.2, 60s@0.1899999962, 61s@0.19, 69s@0.2, 73s@0.2, 79s@0.12, 79s@0.15, 79s@0.12, 79s@0.11 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.57, 3s@0.57, 3s@0.58, 3s@0.57, 4s@0.58, 4s@0.58, 7s@0.62, 7s@0.62, 7s@0.59, 9s@0.6199999628, 12s@0.62, 13s@0.6199999628 ...

### 2026-10-11T01:15Z (market 5478074, result up)
Scored: p1 down filled at 86s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5846153846, 0s@0.6, 2s@0.61, 2s@0.6, 3s@0.6, 12s@0.62, 12s@0.61, 14s@0.6599999133, 14s@0.6499998933, 14s@0.6255555556, 14s@0.62, 20s@0.6486895145 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 86s@0.2299999517, 102s@0.229999997, 105s@0.23, 105s@0.23, 107s@0.23, 107s@0.23, 146s@0.229999987, 149s@0.229999994, 150s@0.2299999991, 165s@0.23, 180s@0.2299999958, 185s@0.2299999517 ...


_Updated 2026-10-11 02:23Z_
