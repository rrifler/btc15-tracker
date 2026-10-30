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
- Windows scored: 2782; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.2% of scored windows had a fill (360 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 274/595 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-30T01:30Z (market 6374904, result up)
Scored: p1 up filled at 58s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 58s@0.209999998, 60s@0.24, 60s@0.24, 60s@0.2130526275, 60s@0.2099999885, 60s@0.2199999983, 60s@0.2199999987, 60s@0.2145273546, 60s@0.2199999885, 78s@0.19, 78s@0.2099999895 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.51, 0s@0.51, 1s@0.55, 3s@0.55, 3s@0.5499999586, 3s@0.5499999763, 3s@0.5499999763, 3s@0.55, 3s@0.6, 4s@0.57, 4s@0.5699999991, 4s@0.5699999991 ...

### 2026-10-30T01:45Z (market 6375574, result down)
Scored: p1 up filled at 91s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.46, 6s@0.46, 7s@0.46, 18s@0.4699999962, 19s@0.47, 91s@0.2399999981, 91s@0.2399999852, 97s@0.24, 97s@0.2399999992, 99s@0.2435144789, 124s@0.24, 124s@0.2399999808 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 7s@0.549999945, 9s@0.55, 10s@0.57, 10s@0.5699999214, 13s@0.5799999768, 18s@0.52, 19s@0.559999776, 19s@0.56, 25s@0.59, 27s@0.6099999971, 30s@0.61 ...

### 2026-10-30T04:00Z (market 6377865, result down)
Scored: p1 up filled at 66s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.4799999846, 4s@0.4847916667, 61s@0.25, 66s@0.24, 66s@0.2399999726, 66s@0.24, 66s@0.2399999981, 79s@0.2199999984, 81s@0.2199999984, 82s@0.22, 82s@0.22, 84s@0.219999978 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5799999768, 4s@0.55, 4s@0.5299999868, 7s@0.5799999768, 9s@0.6, 9s@0.59, 9s@0.59, 9s@0.58, 9s@0.58, 9s@0.58, 9s@0.58, 10s@0.6199999864 ...

### 2026-10-30T06:30Z (market 6380706, result down)
Scored: p1 down filled at 16s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 7s@0.5499999904, 7s@0.55, 7s@0.5399999773, 7s@0.5399999833, 9s@0.5599999693, 9s@0.56, 9s@0.56, 9s@0.56, 10s@0.57, 12s@0.61, 12s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4599999387, 4s@0.4599997976, 4s@0.46, 6s@0.46, 6s@0.4599999986, 7s@0.4599997976, 7s@0.4599997976, 7s@0.4599999986, 7s@0.4599999986, 7s@0.4699999944, 7s@0.4599999986, 7s@0.4599999986 ...


_Updated 2026-10-30 07:03Z_
