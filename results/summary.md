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
- Windows scored: 989; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 74 of 161 = 46.0% (95% range 38.4% to 53.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-13.35 (balance $6.65 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 74/161 = 46.0%; touch 82/175 = 46.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-11T04:30Z (market 5480330, result up)
Scored: p1 down filled at 101s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5, 12s@0.5099999542, 17s@0.5099999776, 20s@0.51, 20s@0.5099999761, 23s@0.51, 32s@0.5099998215, 32s@0.5099998215, 35s@0.51, 35s@0.51, 39s@0.5099999949, 39s@0.5099998215 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 6s@0.5, 6s@0.5, 20s@0.5, 26s@0.5, 27s@0.5, 39s@0.5, 42s@0.5175, 50s@0.53, 50s@0.53, 54s@0.52, 60s@0.5 ...

### 2026-10-11T06:45Z (market 5482405, result up)
Scored: p1 down filled at 95s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 3s@0.5, 3s@0.4799999687, 3s@0.4799999962, 3s@0.48, 3s@0.48, 3s@0.4607318501, 3s@0.457436, 3s@0.4599999968, 3s@0.45, 3s@0.45, 6s@0.5199999843 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.4899998383, 3s@0.5299998463, 3s@0.5299998463, 5s@0.49, 5s@0.49, 5s@0.49, 6s@0.4899999824, 6s@0.49, 6s@0.49, 6s@0.489999992, 6s@0.49 ...

### 2026-10-11T08:00Z (market 5483626, result up)
Scored: p1 down filled at 57s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.57, 4s@0.578, 4s@0.57, 4s@0.57, 13s@0.6, 13s@0.6, 15s@0.64, 15s@0.64, 15s@0.64, 15s@0.64, 15s@0.64, 16s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.23, 57s@0.23, 57s@0.23, 58s@0.2299999914, 61s@0.225, 63s@0.219999978, 66s@0.2299999914, 66s@0.22, 87s@0.235, 174s@0.25, 180s@0.25, 447s@0.22 ...

### 2026-10-11T08:30Z (market 5483714, result up)
Scored: p1 down filled at 33s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.59, 3s@0.59, 4s@0.5899999813, 6s@0.65, 7s@0.65, 24s@0.66, 25s@0.705, 25s@0.67, 27s@0.72, 27s@0.7199998953, 27s@0.7199999611, 27s@0.7199999934 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 33s@0.2299999819, 34s@0.45, 34s@0.45, 34s@0.45, 52s@0.45, 54s@0.45, 54s@0.4545454545, 54s@0.5099999215, 54s@0.51, 54s@0.4925, 55s@0.51, 55s@0.5099998215 ...


_Updated 2026-10-11 10:23Z_
