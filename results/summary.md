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
- Windows scored: 889; excluded: 0
- Fill rate: 16.5% of scored windows had a fill (0 too small)
- Fills that reached 45c: 68 of 147 = 46.3% (95% range 38.4% to 54.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.55 (balance $7.45 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 68/147 = 46.3%; touch 75/160 = 46.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-10T03:45Z (market 5448193, result up)
Scored: p1 down filled at 78s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5351222948, 5s@0.549999956, 6s@0.55, 8s@0.5966210416, 8s@0.59, 8s@0.59, 8s@0.5525, 12s@0.59999988, 14s@0.54, 15s@0.54, 17s@0.5399999568, 65s@0.57 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 5s@0.46, 5s@0.4635, 6s@0.4599999034, 29s@0.469999906, 36s@0.46, 75s@0.25, 75s@0.25, 77s@0.25, 77s@0.25, 78s@0.22, 78s@0.22 ...

### 2026-10-10T05:30Z (market 5450399, result up)
Scored: p1 down filled at 70s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 4s@0.5, 4s@0.5, 4s@0.5, 4s@0.5, 4s@0.5, 7s@0.584, 22s@0.5899998466, 31s@0.5899999366, 43s@0.5899999725, 57s@0.59, 57s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.51, 61s@0.25, 63s@0.25, 63s@0.25, 63s@0.25, 70s@0.22, 82s@0.22, 84s@0.23, 85s@0.23, 85s@0.23, 87s@0.25, 87s@0.2483870968 ...


_Updated 2026-10-10 09:23Z_
