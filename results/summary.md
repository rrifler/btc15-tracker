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
- Windows scored: 465; excluded: 0
- Fill rate: 17.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 35 of 79 = 44.3% (95% range 33.9% to 55.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-10.15 (balance $9.85 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 35/79 = 44.3%; touch 40/86 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-05T17:15Z (market 5291212, result up)
Scored: p1 down filled at 112s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 2s@0.575, 4s@0.549999945, 4s@0.56, 5s@0.549999945, 5s@0.55, 11s@0.5499999966, 17s@0.58, 19s@0.62, 19s@0.63, 19s@0.62, 19s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4599997976, 4s@0.4599999034, 4s@0.469999998, 14s@0.459999988, 79s@0.25, 112s@0.24, 113s@0.25, 115s@0.25, 115s@0.25, 128s@0.22, 143s@0.21, 143s@0.2099999983 ...

### 2026-10-05T21:00Z (market 5304855, result down)
Scored: p1 up filled at 86s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 86s@0.24, 94s@0.24, 95s@0.24, 100s@0.2399999808, 104s@0.23, 104s@0.23, 104s@0.23, 104s@0.23, 106s@0.2399999845, 106s@0.2399999808, 106s@0.23, 106s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.59, 4s@0.57, 5s@0.599999952, 7s@0.5899999145, 7s@0.5899997404, 8s@0.5955791335, 10s@0.6299999758, 10s@0.61, 10s@0.61, 20s@0.6299998362, 20s@0.629999995, 29s@0.64 ...


_Updated 2026-10-05 23:21Z_
