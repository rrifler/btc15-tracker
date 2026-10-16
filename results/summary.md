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
- Windows scored: 1497; excluded: 0
- Fill rate: 17.6% of scored windows had a fill (90 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 132/293 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-16T12:15Z (market 5728312, result up)
Scored: p1 up filled at 25s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 25s@0.24, 25s@0.23, 25s@0.22, 136s@0.45, 141s@0.48, 142s@0.48, 145s@0.48, 145s@0.4899998332, 148s@0.4899999183, 150s@0.4899998383, 154s@0.48, 154s@0.4899999412 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5989310409, 4s@0.64, 4s@0.64, 10s@0.629999968, 10s@0.629999958, 10s@0.6199999221, 15s@0.7099999691, 15s@0.709999968, 15s@0.7004795507, 15s@0.71, 15s@0.676558653, 15s@0.64 ...

### 2026-10-16T12:45Z (market 5729269, result down)
Scored: p1 up filled at 106s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.53, 4s@0.53, 4s@0.53, 4s@0.53, 9s@0.4989120887, 9s@0.4899999584, 12s@0.4799999846, 13s@0.4799998464, 106s@0.21, 108s@0.205, 109s@0.2251789165, 109s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.469999906, 4s@0.4799999818, 4s@0.47, 4s@0.4699999839, 9s@0.5299999417, 9s@0.53, 10s@0.53, 10s@0.53, 13s@0.53, 15s@0.5399999963, 15s@0.54, 15s@0.54 ...

### 2026-10-16T13:30Z (market 5731150, result down)
Scored: p1 up filled at 96s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.57, 3s@0.59, 3s@0.59, 3s@0.5899999802, 3s@0.5899999813, 4s@0.6499999594, 4s@0.64, 4s@0.6299998277, 4s@0.62, 4s@0.65, 4s@0.6299999539, 4s@0.649999984 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.45, 18s@0.4799999846, 18s@0.48, 19s@0.52, 19s@0.4826943112, 19s@0.5, 19s@0.5, 19s@0.48, 19s@0.48, 19s@0.48, 19s@0.48, 22s@0.51 ...


_Updated 2026-10-16 17:33Z_
