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
- Windows scored: 37; excluded: 0
- Fill rate: 21.6% of scored windows had a fill (0 too small)
- Fills that reached 45c: 4 of 8 = 50.0% (95% range 21.5% to 78.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-0.95 (balance $19.05 from $20)
- Longest losing streak: 2
- Strict vs touch: strict 4/8 = 50.0%; touch 4/8 = 50.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-01T04:45Z (market 5148040, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 -1.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5399999568, 6s@0.54, 6s@0.5399999568, 8s@0.57, 11s@0.559999972, 11s@0.559999776, 14s@0.5599999839, 18s@0.52, 24s@0.5299999607, 30s@0.5306537063, 36s@0.559999776, 36s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 3s@0.4599997976, 3s@0.5043263256, 3s@0.4835866325, 3s@0.46, 3s@0.4599997976, 3s@0.49, 3s@0.4897551212, 3s@0.4899999984, 3s@0.49, 3s@0.47, 5s@0.466640491 ...

### 2026-10-01T07:30Z (market 5150289, result up)
Scored: p1 down filled at 107s, exit hit 0; p2 none. Profit p1 -1.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999887, 3s@0.54, 3s@0.5494505495, 5s@0.5399998361, 5s@0.5399999568, 5s@0.5099998215, 5s@0.5399999568, 5s@0.53, 5s@0.5299999868, 5s@0.52, 5s@0.5154545455, 5s@0.5299998463 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.48, 5s@0.4855, 5s@0.47, 5s@0.4925, 6s@0.47, 6s@0.47, 6s@0.4699999962, 6s@0.4699999962, 6s@0.47, 6s@0.469999906, 8s@0.4699999691, 8s@0.4899998863 ...

### 2026-10-01T08:30Z (market 5150859, result up)
Scored: p1 up filled at 108s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 50s@0.25, 108s@0.21, 122s@0.16643915, 123s@0.18, 125s@0.17, 128s@0.17, 129s@0.18, 129s@0.17, 137s@0.19, 138s@0.19, 138s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.56, 3s@0.5687741891, 3s@0.504476584, 5s@0.57, 5s@0.5699999998, 5s@0.5699999886, 6s@0.5899998254, 8s@0.6, 11s@0.5799999768, 12s@0.58, 12s@0.58, 14s@0.5899999712 ...

### 2026-10-01T10:00Z (market 5152164, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5685421931, 5s@0.606, 5s@0.5, 6s@0.5599999569, 17s@0.48, 68s@0.25, 68s@0.24, 77s@0.25, 78s@0.25, 78s@0.25, 83s@0.24, 84s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 6s@0.45, 6s@0.45, 6s@0.45, 6s@0.45, 6s@0.45, 8s@0.522, 8s@0.45, 8s@0.45, 11s@0.53, 12s@0.5299999025, 17s@0.52 ...


_Updated 2026-10-01 10:25Z_
