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
- Windows scored: 2045; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.7% of scored windows had a fill (209 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 194/422 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-22T04:45Z (market 6003504, result up)
Scored: p1 down filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5135802165, 5s@0.55, 5s@0.53, 5s@0.52, 6s@0.5599999955, 6s@0.5599999955, 6s@0.5699999914, 6s@0.5488372093, 6s@0.55, 6s@0.5599999955, 6s@0.5599999955, 6s@0.5599999955 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998383, 3s@0.5, 63s@0.2299999864, 63s@0.23, 72s@0.2, 81s@0.14, 89s@0.13, 93s@0.15, 95s@0.16, 102s@0.1499999993, 102s@0.14, 110s@0.1499999925 ...

### 2026-10-22T05:30Z (market 6004194, result down)
Scored: p1 up filled at 40s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 38s@0.25, 40s@0.22, 44s@0.2199999974, 46s@0.2099999895, 55s@0.25, 56s@0.25, 62s@0.2299999996, 65s@0.22, 88s@0.2, 94s@0.1699999994, 98s@0.1299999959, 98s@0.1299999968 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.61, 4s@0.6, 4s@0.6, 7s@0.6299998362, 8s@0.6309961538, 11s@0.649999805, 22s@0.7, 26s@0.71, 29s@0.72, 37s@0.71, 38s@0.78, 38s@0.78 ...

### 2026-10-22T10:00Z (market 6007437, result up)
Scored: p1 down filled at 95s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.58042301, 2s@0.5899999841, 5s@0.48, 5s@0.48, 5s@0.4799998464, 5s@0.5528961148, 8s@0.48, 8s@0.4799999846, 8s@0.48, 8s@0.48, 9s@0.4799999216, 9s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.464, 3s@0.45, 3s@0.45, 6s@0.5299999587, 6s@0.5299999702, 9s@0.53, 12s@0.49, 14s@0.49, 20s@0.48, 26s@0.52, 36s@0.49, 42s@0.4899999824 ...


_Updated 2026-10-22 10:37Z_
