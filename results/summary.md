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
- Windows scored: 121; excluded: 0
- Fill rate: 21.5% of scored windows had a fill (0 too small)
- Fills that reached 45c: 11 of 26 = 42.3% (95% range 25.5% to 61.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-5.00 (balance $15.00 from $20)
- Longest losing streak: 5
- Strict vs touch: strict 11/26 = 42.3%; touch 14/29 = 48.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-02T03:00Z (market 5169021, result up)
Scored: p1 down filled at 83s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.47, 5s@0.469999906, 5s@0.47, 9s@0.47, 9s@0.4787174298, 11s@0.48, 12s@0.4799999616, 14s@0.48, 14s@0.4799999616, 14s@0.48, 15s@0.5199999567, 15s@0.5215857141 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 3s@0.559999776, 3s@0.5475776501, 3s@0.529999998, 5s@0.5399999568, 5s@0.5399999648, 5s@0.5399999568, 5s@0.559999776, 5s@0.559999776, 6s@0.54, 6s@0.5399999568, 6s@0.5399999568 ...

### 2026-10-02T03:30Z (market 5169113, result up)
Scored: p1 down filled at 68s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 3s@0.51, 5s@0.5348814938, 6s@0.54, 8s@0.5199999792, 11s@0.5199999792, 12s@0.5299998463, 12s@0.5299999868, 14s@0.5299999868, 15s@0.53, 18s@0.5299999868, 20s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.485, 2s@0.469525, 2s@0.46, 2s@0.46, 3s@0.48, 3s@0.4905, 5s@0.4763721704, 5s@0.47, 5s@0.469999906, 6s@0.469999906, 11s@0.4899999183, 11s@0.49 ...

### 2026-10-02T04:15Z (market 5169621, result up)
Scored: p1 down filled at 68s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.47, 5s@0.49, 8s@0.5199999792, 8s@0.5199999843, 8s@0.48, 8s@0.53, 9s@0.5099999916, 11s@0.5299999868, 14s@0.5299999868, 18s@0.5417916667, 18s@0.5299999868 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999251, 6s@0.52, 8s@0.5299998463, 14s@0.48, 68s@0.24, 75s@0.23, 75s@0.23, 77s@0.23, 81s@0.23, 89s@0.24, 89s@0.23, 89s@0.23 ...

### 2026-10-02T06:15Z (market 5171299, result up)
Scored: p1 down filled at 74s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 2s@0.48, 3s@0.45, 5s@0.469999969, 5s@0.4699999727, 5s@0.469999906, 5s@0.469999906, 5s@0.469999906, 5s@0.47, 5s@0.47, 6s@0.4699999944, 6s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.54, 5s@0.5399999568, 6s@0.5399999568, 6s@0.54, 8s@0.5199999792, 15s@0.5199999803, 15s@0.5199999692, 17s@0.5399999821, 17s@0.5399999887, 17s@0.5382754602, 17s@0.5199999889, 17s@0.5199999768 ...


_Updated 2026-10-02 07:26Z_
