import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest  # noqa: E402

from src import report, runner  # noqa: E402
from src.sim import apply_stake, classify  # noqa: E402
from src.stats import combined_verdict, verdict, wilson  # noqa: E402

CFG = runner.load_config(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.yaml"))
WS = 1_800_000_000 - 1_800_000_000 % 900


def tr(offset, price):
    return {"timestamp": WS + offset, "price": price, "size": 10, "side": "BUY"}


def test_no_fill():
    out = classify(WS, [tr(5, 0.30), tr(60, 0.26)], [tr(5, 0.70)], CFG)
    assert out.status == "no_fill" and apply_stake(out, "up", 20.0, CFG) == 20.0


def test_fill_hits_45():
    out = classify(WS, [tr(10, 0.24), tr(100, 0.50)], [tr(10, 0.76)], CFG)
    assert [p.side for p in out.positions] == ["up"] and out.positions[0].exit_hit
    bal = apply_stake(out, "down", 20.0, CFG)  # exit hit, so the final result does not matter
    assert out.positions[0].shares == 4                      # floor(20*0.05/0.25)
    assert bal == pytest.approx(20 + 4 * 0.20)               # +80% of the $1 stake


def test_fill_misses_and_settles_zero():
    out = classify(WS, [tr(10, 0.20), tr(200, 0.40)], [tr(10, 0.80)], CFG)
    assert not out.positions[0].exit_hit
    bal = apply_stake(out, "down", 20.0, CFG)
    assert bal == pytest.approx(20 - 4 * 0.25)


def test_fill_misses_and_settles_one():
    out = classify(WS, [tr(10, 0.20)], [], CFG)
    assert apply_stake(out, "up", 20.0, CFG) == pytest.approx(20 + 4 * 0.75)


def test_both_sides_fill_within_10s():
    out = classify(WS, [tr(30, 0.20)], [tr(35, 0.22), tr(300, 0.60)], CFG)
    assert sorted(p.side for p in out.positions) == ["down", "up"]
    by = {p.side: p for p in out.positions}
    assert not by["up"].exit_hit and by["down"].exit_hit
    bal = apply_stake(out, "down", 20.0, CFG)
    assert bal == pytest.approx(20 + 4 * 0.20 + 4 * -0.25)   # down hit exit, up settles $0


def test_second_side_after_10s_is_cancelled():
    out = classify(WS, [tr(30, 0.20)], [tr(50, 0.22)], CFG)
    assert [p.side for p in out.positions] == ["up"]


def test_entry_after_120s_ignored():
    assert classify(WS, [tr(120, 0.10)], [tr(121, 0.10)], CFG).status == "no_fill"


def test_strict_vs_touch():
    up = [tr(10, 0.25), tr(50, 0.45)]
    assert classify(WS, up, [], CFG, strict=True).status == "no_fill"
    out = classify(WS, up, [], CFG, strict=False)
    assert out.positions[0].exit_hit


def test_exit_needs_later_trade():
    out = classify(WS, [tr(10, 0.20), tr(10, 0.50)], [], CFG)   # same-second trade does not count
    assert not out.positions[0].exit_hit


def test_exit_after_window_end_ignored():
    out = classify(WS, [tr(10, 0.20), tr(900, 0.60)], [], CFG)
    assert not out.positions[0].exit_hit


def test_too_small_stake():
    out = classify(WS, [tr(10, 0.20)], [], CFG)
    assert apply_stake(out, "up", 4.0, CFG) == 4.0           # floor(4*0.05/0.25) = 0 shares
    assert out.status == "too_small"


def test_excluded_window_row():
    row = report.make_row(WS, {"market_id": "1", "result": None}, "INTL_PROXY", 3, "result_missing", None, None)
    rows = report.rebuild({WS: row}, CFG)
    assert rows[WS]["balance_after"] == "" and rows[WS]["status"] == "excluded"
    assert report.metrics(rows, CFG)["scored"] == 0


def test_wilson_and_verdict_rules():
    low, high = wilson(31, 50)                     # 62% on 50 fills
    assert low < 0.556 < high
    assert verdict(50, 31, 5.0, CFG) == "NOT ENOUGH DATA"
    assert verdict(100, 80, 5.0, CFG) == "PASS"
    assert verdict(100, 80, -1.0, CFG) == "FAIL"   # profit must be positive too
    assert verdict(100, 60, 5.0, CFG) == "FAIL"    # low end of range below 55.6%
    assert combined_verdict("PASS", "PASS", 0.80, 0.70, CFG) == "FAIL"   # 10 point gap
    assert combined_verdict("PASS", "PASS", 0.80, 0.75, CFG) == "PASS"
    assert combined_verdict("PASS", "NOT ENOUGH DATA", 0.8, 0.8, CFG) == "NOT ENOUGH DATA"
    assert combined_verdict("FAIL", "NOT ENOUGH DATA", 0.4, 0.0, CFG) == "FAIL"   # a failed backtest ends it


def test_rebuild_is_idempotent_and_balance_compounds():
    rows = {}
    for i, win in enumerate([WS, WS + 900]):
        out = classify(win, [{"timestamp": win + 10, "price": 0.2, "size": 1, "side": "BUY"},
                             {"timestamp": win + 50, "price": 0.5, "size": 1, "side": "BUY"}], [], CFG)
        rows[win] = report.make_row(win, {"market_id": str(i), "result": "up"}, "INTL_PROXY", 2, "", out, out)
    first = {k: dict(v) for k, v in report.rebuild(rows, CFG).items()}
    second = report.rebuild({k: dict(v) for k, v in first.items()}, CFG)
    assert first == second
    assert float(second[WS + 900]["balance_after"]) > float(second[WS]["balance_after"]) > 20
