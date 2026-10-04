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
- Windows scored: 365; excluded: 0
- Fill rate: 17.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 30 of 62 = 48.4% (95% range 36.4% to 60.6%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.15 (balance $13.85 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 30/62 = 48.4%; touch 34/67 = 50.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-04T17:45Z (market 5242771, result down)
Scored: p1 down filled at 67s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6063905114, 4s@0.64, 5s@0.66, 5s@0.65, 5s@0.649999805, 5s@0.64, 7s@0.7260217962, 7s@0.71, 8s@0.6299999973, 10s@0.6199998512, 10s@0.62, 11s@0.6199999958 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.45, 2s@0.45, 2s@0.45, 67s@0.229999994, 80s@0.22, 80s@0.2, 104s@0.1848788556, 106s@0.23, 106s@0.21, 107s@0.23, 112s@0.21 ...

### 2026-10-04T19:30Z (market 5247174, result down)
Scored: p1 down filled at 119s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.47, 1s@0.4699999691, 2s@0.4899999654, 2s@0.4899999654, 2s@0.47, 2s@0.4777874485, 2s@0.47, 2s@0.46, 2s@0.469999998, 2s@0.47, 4s@0.49, 4s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.52, 4s@0.5199999792, 4s@0.5199999792, 5s@0.52, 5s@0.5199999792, 5s@0.5199999792, 5s@0.5199999792, 5s@0.52, 7s@0.5199999792, 7s@0.52, 7s@0.52, 7s@0.52 ...

### 2026-10-04T22:00Z (market 5255728, result up)
Scored: p1 down filled at 28s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5899999797, 2s@0.5899999934, 2s@0.59, 4s@0.6199999676, 4s@0.5701282917, 4s@0.6032885906, 5s@0.62, 5s@0.6199999778, 5s@0.62, 7s@0.6599999291, 7s@0.65, 7s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 28s@0.23, 29s@0.22, 31s@0.2, 31s@0.2, 32s@0.21, 32s@0.2, 32s@0.2, 34s@0.2, 34s@0.2299999992, 35s@0.22, 35s@0.2292520305, 38s@0.2 ...


_Updated 2026-10-04 22:23Z_
