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
- Windows scored: 533; excluded: 0
- Fill rate: 17.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 39 of 91 = 42.9% (95% range 33.2% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.60 (balance $8.40 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 39/91 = 42.9%; touch 44/100 = 44.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-06T11:15Z (market 5320544, result up)
Scored: p1 down filled at 45s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 37s@0.48, 37s@0.48, 37s@0.48, 43s@0.5025, 45s@0.75, 45s@0.751616341, 45s@0.75, 45s@0.75, 45s@0.75, 45s@0.75, 45s@0.7399999703, 45s@0.739999997 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.57, 0s@0.5781531532, 3s@0.56, 4s@0.5699999886, 4s@0.5799999768, 4s@0.57, 4s@0.58, 4s@0.58, 6s@0.5699999886, 6s@0.5699999886, 7s@0.57, 7s@0.57 ...

### 2026-10-06T15:30Z (market 5329787, result down)
Scored: p1 up filled at 102s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.4799999855, 9s@0.48, 12s@0.5, 15s@0.4699999796, 17s@0.4699999998, 21s@0.47, 23s@0.469999906, 27s@0.48, 29s@0.49, 38s@0.469999998, 45s@0.4992878507, 47s@0.509999966 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 5s@0.5219874149, 6s@0.53, 6s@0.5299999025, 14s@0.49, 15s@0.5299999991, 27s@0.5199999792, 27s@0.5199999757, 33s@0.52, 51s@0.51, 69s@0.53375, 71s@0.5499999763 ...


_Updated 2026-10-06 16:27Z_
