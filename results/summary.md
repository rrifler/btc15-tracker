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
- Windows scored: 1085; excluded: 0
- Fill rate: 16.5% of scored windows had a fill (5 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 86/195 = 44.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-12T04:30Z (market 5535830, result up)
Scored: p1 down filled at 92s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.52, 8s@0.5, 17s@0.6, 17s@0.6, 17s@0.5216666667, 17s@0.57, 17s@0.53, 18s@0.5999999607, 18s@0.6, 21s@0.5899999145, 24s@0.59, 24s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.4980258256, 6s@0.5, 92s@0.2, 95s@0.21, 176s@0.23, 230s@0.21, 230s@0.2099999895, 231s@0.21, 233s@0.21, 242s@0.2199999941, 245s@0.21 ...

### 2026-10-12T05:30Z (market 5538218, result down)
Scored: p1 up filled at 32s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 32s@0.2, 35s@0.16, 35s@0.179, 39s@0.1699999983, 39s@0.1699999983, 45s@0.2, 47s@0.21, 47s@0.2099999895, 47s@0.21, 48s@0.24, 48s@0.24, 48s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.64, 5s@0.64, 5s@0.5599999851, 6s@0.64, 6s@0.64, 6s@0.64, 8s@0.64, 8s@0.64, 8s@0.64, 9s@0.6899999561, 9s@0.69, 9s@0.6899999801 ...

### 2026-10-12T06:15Z (market 5539628, result down)
Scored: p1 up filled at 80s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 80s@0.23, 84s@0.23, 84s@0.2299999517, 92s@0.2, 92s@0.2, 92s@0.2, 104s@0.2, 105s@0.2099999995, 120s@0.18, 134s@0.1499999925, 138s@0.15, 143s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6099999322, 5s@0.64, 5s@0.63, 8s@0.63, 9s@0.67, 9s@0.64, 11s@0.67, 11s@0.6799998617, 14s@0.6699999611, 18s@0.65, 18s@0.64, 20s@0.64 ...

### 2026-10-12T06:30Z (market 5539670, result up)
Scored: p1 down filled at 32s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 8s@0.557676, 9s@0.61, 9s@0.5899999958, 9s@0.57, 12s@0.649999997, 12s@0.6442307692, 14s@0.64, 15s@0.64, 21s@0.6999999606, 21s@0.6999999606, 21s@0.6699999823 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 30s@0.25, 32s@0.2299999693, 36s@0.23, 36s@0.23, 39s@0.24, 41s@0.2399999808, 47s@0.24, 47s@0.24, 47s@0.24, 50s@0.25, 53s@0.25, 74s@0.2099999895 ...

### 2026-10-12T07:15Z (market 5540465, result down)
Scored: p1 up filled at 55s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4599999912, 4s@0.4799999687, 4s@0.49, 4s@0.4857288045, 4s@0.479999998, 4s@0.479999998, 4s@0.479999998, 5s@0.48, 7s@0.45, 49s@0.25, 49s@0.25, 49s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.549999945, 4s@0.5499999679, 4s@0.549999945, 5s@0.5599999955, 5s@0.5599999558, 5s@0.54999999, 5s@0.55, 5s@0.5499999787, 5s@0.5342622951, 5s@0.5176190476, 7s@0.6199999258, 7s@0.5797015827 ...


_Updated 2026-10-12 10:28Z_
