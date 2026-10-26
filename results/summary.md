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
- Windows scored: 2404; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (286 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 234/509 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-25T23:30Z (market 6163903, result up)
Scored: p1 up filled at 48s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 5s@0.4699999961, 5s@0.4699999754, 5s@0.4699999904, 5s@0.5299998463, 5s@0.53, 6s@0.469999991, 6s@0.4699999949, 6s@0.47, 8s@0.45, 8s@0.4599999929, 12s@0.4639774514 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 5s@0.479999998, 5s@0.48, 5s@0.48, 5s@0.47999994, 5s@0.4799999779, 5s@0.48, 8s@0.55, 8s@0.54, 9s@0.57, 9s@0.5699999886, 9s@0.56 ...

### 2026-10-25T23:45Z (market 6165080, result up)
Scored: p1 up filled at 99s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999707, 3s@0.4599999669, 5s@0.4599999923, 5s@0.4599999923, 5s@0.4599999828, 86s@0.25, 99s@0.24, 143s@0.2299999726, 143s@0.22, 143s@0.22, 146s@0.21, 150s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.55, 5s@0.55, 5s@0.549999945, 6s@0.6, 6s@0.6, 8s@0.599999994, 11s@0.59999988, 12s@0.6199997024, 12s@0.61, 12s@0.59, 14s@0.62, 15s@0.6299998362 ...

### 2026-10-26T03:00Z (market 6170231, result up)
Scored: p1 down filled at 98s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.559999776, 3s@0.5399999568, 6s@0.51, 6s@0.48, 9s@0.5399999568, 9s@0.54, 9s@0.54, 11s@0.575, 12s@0.5799999768, 14s@0.57, 17s@0.5799999768, 29s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 3s@0.47, 3s@0.47, 5s@0.6299999573, 5s@0.6299999573, 5s@0.6299999573, 5s@0.53, 5s@0.51, 5s@0.5257960633, 5s@0.53, 5s@0.52, 5s@0.49 ...

### 2026-10-26T04:15Z (market 6173122, result down)
Scored: p1 down filled at 48s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799999346, 5s@0.49, 6s@0.51, 6s@0.51, 9s@0.5199999843, 12s@0.5299998463, 18s@0.53, 20s@0.55, 20s@0.55, 30s@0.54, 32s@0.56, 32s@0.5399999948 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5099999687, 6s@0.4899999561, 6s@0.51, 8s@0.5, 9s@0.4899999824, 9s@0.49, 11s@0.4899999984, 11s@0.4899999584, 12s@0.48, 12s@0.5, 23s@0.469999906, 48s@0.2399999923 ...


_Updated 2026-10-26 04:38Z_
