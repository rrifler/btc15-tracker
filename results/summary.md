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
- Windows scored: 657; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 45 of 107 = 42.1% (95% range 33.1% to 51.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.90 (balance $7.10 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 45/107 = 42.1%; touch 51/117 = 43.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-07T22:00Z (market 5392657, result up)
Scored: p1 down filled at 90s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 4s@0.5299998463, 4s@0.53, 4s@0.5299999868, 6s@0.5299999868, 6s@0.529999959, 6s@0.5299999763, 6s@0.5299999399, 7s@0.53, 7s@0.5299999868, 9s@0.53, 9s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799998464, 3s@0.47, 3s@0.4602011385, 3s@0.4599999992, 3s@0.46, 3s@0.4596489217, 3s@0.45, 4s@0.4799998551, 4s@0.4799998464, 4s@0.4799998464, 4s@0.4799998551, 4s@0.4799998551 ...

### 2026-10-07T22:45Z (market 5393003, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 53s@0.25, 68s@0.24, 70s@0.2462503645, 116s@0.25, 118s@0.23, 121s@0.2, 143s@0.2026903115, 160s@0.2, 161s@0.2, 164s@0.2128653905, 169s@0.23, 172s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5731225251, 5s@0.6, 5s@0.5899999145, 5s@0.5899997404, 10s@0.6, 10s@0.6, 11s@0.6, 14s@0.6099999892, 26s@0.61, 31s@0.65, 31s@0.61, 31s@0.649999997 ...


_Updated 2026-10-07 23:21Z_
