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
- Windows scored: 949; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 72 of 155 = 46.5% (95% range 38.8% to 54.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.75 (balance $7.25 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 72/155 = 46.5%; touch 79/168 = 47.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-10T18:30Z (market 5470792, result up)
Scored: p1 down filled at 70s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999914, 4s@0.5699999886, 13s@0.5499999995, 22s@0.55, 25s@0.5499999841, 31s@0.5549195162, 36s@0.57, 37s@0.5903225426, 37s@0.59, 37s@0.5899999458, 37s@0.6, 37s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.46, 15s@0.46, 25s@0.4599997976, 25s@0.46, 70s@0.2099999895, 72s@0.21, 72s@0.2099999895, 72s@0.21, 72s@0.21, 73s@0.21, 73s@0.21, 73s@0.21 ...

### 2026-10-10T19:30Z (market 5473305, result up)
Scored: p1 down filled at 117s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5, 18s@0.49, 18s@0.5, 22s@0.5, 22s@0.5, 27s@0.5, 27s@0.5, 45s@0.53, 54s@0.5299999006, 54s@0.5299999787, 58s@0.5299999587, 67s@0.568538963 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.48, 7s@0.48, 12s@0.49, 12s@0.49, 12s@0.48, 13s@0.5, 13s@0.5, 13s@0.5, 15s@0.51, 16s@0.51, 16s@0.5099999749, 16s@0.51 ...

### 2026-10-10T21:15Z (market 5475064, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599997976, 4s@0.49, 4s@0.471742581, 4s@0.46, 6s@0.49, 6s@0.4899998383, 13s@0.4699999935, 13s@0.469999906, 22s@0.47, 33s@0.4799999616, 34s@0.48, 34s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 3s@0.512563634, 7s@0.51, 13s@0.5399999568, 34s@0.52, 36s@0.52, 36s@0.52, 40s@0.509999935, 45s@0.47, 114s@0.23, 115s@0.2299999819, 118s@0.24 ...

### 2026-10-10T22:45Z (market 5476391, result up)
Scored: p1 up filled at 48s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.2, 51s@0.2, 54s@0.2, 55s@0.2, 60s@0.1899999962, 61s@0.19, 69s@0.2, 73s@0.2, 79s@0.12, 79s@0.15, 79s@0.12, 79s@0.11 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.57, 3s@0.57, 3s@0.58, 3s@0.57, 4s@0.58, 4s@0.58, 7s@0.62, 7s@0.62, 7s@0.59, 9s@0.6199999628, 12s@0.62, 13s@0.6199999628 ...


_Updated 2026-10-11 00:34Z_
