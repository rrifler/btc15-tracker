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
- Windows scored: 693; excluded: 0
- Fill rate: 16.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 47 of 111 = 42.3% (95% range 33.6% to 51.6%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-13.00 (balance $7.00 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 47/111 = 42.3%; touch 53/121 = 43.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-08T02:15Z (market 5395211, result up)
Scored: p1 down filled at 82s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.6, 5s@0.5799999936, 5s@0.5799999768, 5s@0.5799999768, 7s@0.599999988, 10s@0.5899999866, 11s@0.5899999894, 13s@0.55, 16s@0.549999945, 19s@0.549999945, 20s@0.5199999792, 35s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.450728, 19s@0.46, 23s@0.469999906, 28s@0.4599999034, 82s@0.2299999517, 82s@0.2299999693, 101s@0.22, 103s@0.2399999852, 106s@0.25, 112s@0.2399999808, 113s@0.25, 133s@0.4599999829 ...

### 2026-10-08T07:00Z (market 5399661, result up)
Scored: p1 up filled at 25s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 25s@0.24, 26s@0.25, 29s@0.25, 29s@0.25, 85s@0.223773241, 86s@0.22, 95s@0.23, 98s@0.2399999808, 101s@0.23, 104s@0.2299999595, 116s@0.21, 122s@0.15 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.6005710337, 7s@0.6, 8s@0.61, 10s@0.6199999943, 10s@0.6199999907, 13s@0.62, 14s@0.58, 17s@0.5899999145, 17s@0.5999999607, 17s@0.6, 17s@0.59999988, 17s@0.59 ...


_Updated 2026-10-08 08:28Z_
