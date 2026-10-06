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
- Windows scored: 545; excluded: 0
- Fill rate: 17.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 40 of 93 = 43.0% (95% range 33.4% to 53.2%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.65 (balance $8.35 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 40/93 = 43.0%; touch 45/103 = 43.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-06T15:30Z (market 5329787, result down)
Scored: p1 up filled at 102s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.4799999855, 9s@0.48, 12s@0.5, 15s@0.4699999796, 17s@0.4699999998, 21s@0.47, 23s@0.469999906, 27s@0.48, 29s@0.49, 38s@0.469999998, 45s@0.4992878507, 47s@0.509999966 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 5s@0.5219874149, 6s@0.53, 6s@0.5299999025, 14s@0.49, 15s@0.5299999991, 27s@0.5199999792, 27s@0.5199999757, 33s@0.52, 51s@0.51, 69s@0.53375, 71s@0.5499999763 ...

### 2026-10-06T17:30Z (market 5332388, result down)
Scored: p1 up filled at 81s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.47, 5s@0.469999906, 5s@0.47, 5s@0.4799999616, 6s@0.4599997976, 20s@0.45, 54s@0.25, 56s@0.25, 57s@0.25, 81s@0.24, 81s@0.24, 86s@0.2475247525 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.52, 5s@0.539999997, 5s@0.53, 6s@0.55, 11s@0.53, 20s@0.55, 20s@0.5479166667, 20s@0.53, 21s@0.64, 21s@0.61, 24s@0.65, 24s@0.649999805 ...

### 2026-10-06T18:00Z (market 5335464, result up)
Scored: p1 down filled at 95s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.57, 5s@0.609284, 5s@0.595, 6s@0.6599999448, 6s@0.66, 6s@0.65, 6s@0.66, 6s@0.66, 6s@0.64, 6s@0.65, 6s@0.64, 8s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 95s@0.229999994, 96s@0.229999994, 102s@0.2299999517, 123s@0.25, 126s@0.21, 126s@0.21, 128s@0.24, 128s@0.24, 128s@0.25, 128s@0.22, 128s@0.22, 128s@0.21 ...


_Updated 2026-10-06 19:23Z_
