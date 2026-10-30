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
- Windows scored: 2758; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.2% of scored windows had a fill (356 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 272/589 = 46.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-29T19:30Z (market 6361210, result up)
Scored: p1 down filled at 82s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.56, 18s@0.6, 21s@0.66, 27s@0.62, 27s@0.62, 33s@0.7, 33s@0.69, 51s@0.7, 51s@0.7, 51s@0.7, 63s@0.71, 67s@0.72 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999415, 82s@0.22, 112s@0.45, 144s@0.25, 174s@0.15, 175s@0.15, 186s@0.14, 187s@0.161546921, 189s@0.17, 192s@0.22, 192s@0.22, 208s@0.25 ...

### 2026-10-29T20:00Z (market 6362029, result down)
Scored: p1 up filled at 70s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.52, 3s@0.5113888889, 70s@0.24, 70s@0.2399999631, 73s@0.21, 73s@0.2199999802, 75s@0.24375, 79s@0.1899999665, 82s@0.21, 82s@0.2086666667, 84s@0.2, 85s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.57, 18s@0.6, 22s@0.6099999756, 27s@0.62, 27s@0.62, 27s@0.6199999904, 27s@0.61, 36s@0.5799999893, 60s@0.5, 63s@0.739999978, 63s@0.7299999816, 63s@0.71 ...

### 2026-10-29T23:00Z (market 6369855, result down)
Scored: p1 up filled at 115s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 22s@0.45, 24s@0.45, 24s@0.4599999935, 24s@0.45, 24s@0.45, 25s@0.47, 25s@0.469999998, 25s@0.4599999935, 25s@0.4699999948, 25s@0.46, 25s@0.46, 33s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 3s@0.5189624724, 6s@0.56, 10s@0.5899999705, 12s@0.5947918641, 12s@0.599999985, 13s@0.6, 13s@0.6, 28s@0.55, 30s@0.549999956, 34s@0.51, 42s@0.52 ...

### 2026-10-29T23:45Z (market 6370726, result down)
Scored: p1 up filled at 45s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5338510051, 4s@0.5499999904, 7s@0.5, 7s@0.5, 7s@0.5, 7s@0.5, 7s@0.5, 9s@0.48, 9s@0.5, 9s@0.5, 45s@0.2385159006, 45s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.49, 7s@0.51, 7s@0.51, 9s@0.5299999607, 9s@0.56, 9s@0.5458976248, 9s@0.53, 9s@0.515, 9s@0.5099999215, 9s@0.51, 9s@0.5099999977, 10s@0.58 ...


_Updated 2026-10-30 00:54Z_
