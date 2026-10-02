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
- Windows scored: 93; excluded: 0
- Fill rate: 22.6% of scored windows had a fill (0 too small)
- Fills that reached 45c: 11 of 21 = 52.4% (95% range 32.4% to 71.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-1.25 (balance $18.75 from $20)
- Longest losing streak: 2
- Strict vs touch: strict 11/21 = 52.4%; touch 12/22 = 54.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-01T19:30Z (market 5162124, result up)
Scored: p1 down filled at 119s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099998215, 3s@0.5, 5s@0.5099998215, 5s@0.5099998215, 5s@0.51, 5s@0.51, 6s@0.5099998215, 6s@0.5099998215, 6s@0.5099999604, 8s@0.5199999792, 12s@0.4899998383, 14s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.5, 11s@0.5, 11s@0.5, 12s@0.5, 12s@0.5, 12s@0.5, 12s@0.5, 12s@0.5, 12s@0.5, 15s@0.54, 15s@0.52 ...

### 2026-10-01T20:00Z (market 5162477, result up)
Scored: p1 down filled at 119s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.49, 0s@0.48063125, 0s@0.4725, 0s@0.46, 2s@0.51, 5s@0.5199999792, 6s@0.51, 14s@0.5699999214, 14s@0.550999989, 14s@0.53, 15s@0.5699999886, 17s@0.5699998586 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.48, 11s@0.4755, 14s@0.48, 14s@0.48, 14s@0.48, 119s@0.21, 138s@0.1799999986, 140s@0.17, 146s@0.1799999856, 147s@0.17, 150s@0.19, 152s@0.19 ...

### 2026-10-01T21:15Z (market 5164709, result down)
Scored: p1 up filled at 95s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 93s@0.25, 93s@0.25, 93s@0.25, 95s@0.2299999782, 99s@0.23, 99s@0.2299999992, 101s@0.2299999517, 101s@0.22, 101s@0.23, 101s@0.2299999992, 101s@0.22, 105s@0.2299999975 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.6047530289, 6s@0.6299999764, 11s@0.61, 14s@0.6199998512, 15s@0.6099999488, 18s@0.6099998206, 20s@0.6, 20s@0.6099999968, 23s@0.6099998597, 32s@0.6999999905, 32s@0.71, 32s@0.7 ...

### 2026-10-01T22:00Z (market 5165047, result up)
Scored: p1 down filled at 68s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 6s@0.45, 6s@0.45, 9s@0.46, 11s@0.48, 12s@0.47, 17s@0.5275117272, 18s@0.55, 18s@0.5599998098, 18s@0.55, 18s@0.54, 18s@0.5399999151 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5049800368, 3s@0.5599999961, 5s@0.5599998682, 8s@0.53, 9s@0.5299999868, 9s@0.549999945, 11s@0.5299999868, 11s@0.5399999568, 14s@0.5499999828, 18s@0.4599999828, 68s@0.21, 68s@0.2099999995 ...

### 2026-10-01T23:00Z (market 5166144, result down)
Scored: p1 up filled at 68s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 68s@0.2490384615, 89s@0.25, 107s@0.24, 111s@0.25, 119s@0.25, 120s@0.25, 219s@0.4599999387, 219s@0.45, 231s@0.4599999387, 231s@0.4599999387, 237s@0.45, 248s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 5s@0.5441666667, 6s@0.6410612977, 6s@0.6335979513, 8s@0.64, 9s@0.68, 9s@0.6999999054, 9s@0.6999999754, 9s@0.67, 9s@0.6699999823, 9s@0.6799999547, 9s@0.67 ...


_Updated 2026-10-02 00:31Z_
