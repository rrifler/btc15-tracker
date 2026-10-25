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
- Windows scored: 2341; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (272 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 225/494 = 45.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-25T07:00Z (market 6111796, result up)
Scored: p1 down filled at 60s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.54, 5s@0.5699999556, 6s@0.6, 8s@0.59, 9s@0.5899998399, 9s@0.5899999145, 12s@0.58, 12s@0.59, 14s@0.58, 14s@0.5799999189, 17s@0.58, 18s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 60s@0.2399999808, 78s@0.24, 81s@0.24, 83s@0.24, 95s@0.24, 96s@0.24, 96s@0.24, 102s@0.25, 129s@0.25, 234s@0.1872972973, 236s@0.1899999824, 243s@0.1499999993 ...

### 2026-10-25T08:00Z (market 6112986, result down)
Scored: p1 up filled at 111s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.646699335, 5s@0.699999999, 5s@0.699999987, 5s@0.7099999533, 5s@0.7199999424, 5s@0.6405353467, 5s@0.7199999891, 5s@0.7102702549, 5s@0.6299999392, 5s@0.63, 6s@0.7, 6s@0.7 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.45, 38s@0.48, 39s@0.48, 39s@0.5058644043, 42s@0.5199999792, 42s@0.5199999792, 47s@0.51, 65s@0.56, 65s@0.5599999686, 65s@0.5299999587, 66s@0.5699999916, 84s@0.63 ...

### 2026-10-25T08:30Z (market 6113096, result up)
Scored: p1 down filled at 119s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 3s@0.4944140311, 3s@0.4993314018, 3s@0.46, 3s@0.4599999034, 3s@0.49, 6s@0.469999906, 6s@0.4599999739, 8s@0.47, 8s@0.4699999796, 8s@0.4699999962, 8s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.47, 3s@0.55, 3s@0.51, 3s@0.4893617021, 3s@0.46506, 5s@0.58, 5s@0.57, 5s@0.61, 5s@0.61, 9s@0.529999991, 14s@0.4799999846, 14s@0.48 ...

### 2026-10-25T09:00Z (market 6113654, result down)
Scored: p1 down filled at 50s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5599999851, 11s@0.5799999768, 11s@0.5599999642, 12s@0.62, 12s@0.58, 12s@0.6156995573, 12s@0.61, 24s@0.62, 27s@0.69, 30s@0.71, 30s@0.7199999424, 32s@0.7199999835 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 50s@0.22, 50s@0.22, 53s@0.22, 77s@0.46, 84s@0.45, 89s@0.4599999669, 92s@0.469999906, 95s@0.57, 95s@0.57, 95s@0.47, 96s@0.5699999942, 96s@0.57 ...

### 2026-10-25T10:45Z (market 6115568, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.549999981, 2s@0.55, 2s@0.5499998234, 2s@0.5499998503, 2s@0.54, 2s@0.55, 2s@0.55, 3s@0.5335604755, 3s@0.5299999251, 3s@0.5299999196, 3s@0.5399999942, 3s@0.5299998463 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.4667857143, 9s@0.48, 24s@0.469999906, 24s@0.469999971, 32s@0.48, 32s@0.49, 33s@0.5, 33s@0.5338214834, 35s@0.54, 36s@0.64, 36s@0.6 ...


_Updated 2026-10-25 12:39Z_
