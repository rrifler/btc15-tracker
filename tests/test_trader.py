import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest  # noqa: E402

from src import pm_us, runner  # noqa: E402
from src.trader import Halt, Trader  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = runner.load_config(os.path.join(ROOT, "config.yaml"))
WS = 1_800_000_000 - 1_800_000_000 % 900


class Clock:
    def __init__(self, t):
        self.t = t

    def now(self):
        return self.t

    def sleep(self, s):
        self.t += s


class FakeClient:
    """Mock exchange. fills maps (side, action) -> seconds after window start when it fills."""
    mode = "live"

    def __init__(self, clock, balance=20.0, fills=None, fail_on=None):
        self.clock, self._balance, self.fills = clock, balance, fills or {}
        self.fail_on = fail_on
        self.orders, self.cancelled, self.cancel_all_calls = {}, [], 0
        self.n = 0

    def balance(self):
        return self._balance

    def place(self, slug, side, action, price, qty):
        if self.fail_on == "place":
            raise RuntimeError("boom")
        self.n += 1
        oid = f"o{self.n}"
        self.orders[oid] = dict(slug=slug, side=side, action=action, price=price, qty=qty, t=self.clock.t)
        return oid

    def filled_qty(self, oid):
        o = self.orders[oid]
        at = self.fills.get((o["side"], o["action"]))
        if oid in self.cancelled or at is None or self.clock.t < WS + at:
            return 0, "ORDER_STATE_NEW"
        return o["qty"], "ORDER_STATE_FILLED"

    def cancel(self, slug, oid):
        self.cancelled.append(oid)

    def cancel_all(self):
        self.cancel_all_calls += 1


def make(tmp_path, client_kw=None, settle=1.0, skew=0.0):
    clock = Clock(WS - 1)
    client = FakeClient(clock, **(client_kw or {}))
    tr = Trader(client, CFG, state_path=str(tmp_path / "state.json"), log_path=str(tmp_path / "log.csv"),
                now=clock.now, sleep=clock.sleep, settle=lambda slug: settle, skew=lambda: skew)
    return clock, client, tr


def events(tmp_path):
    with open(tmp_path / "log.csv") as f:
        return [r["event"] for r in csv.DictReader(f)]


def test_orders_placed_on_time_and_cancelled_at_120s(tmp_path):
    clock, client, tr = make(tmp_path)
    clock.t = WS
    placed_at = []
    orig = client.place
    client.place = lambda *a, **k: (placed_at.append(clock.t), orig(*a, **k))[1]
    tr.run_window(WS)
    assert all(t - WS <= 2 for t in placed_at[:2])
    assert len(client.cancelled) == 2                       # both unfilled buys cancelled
    assert clock.t >= WS + CFG["entry_window_s"]
    assert clock.t < WS + CFG["entry_window_s"] + 3
    assert events(tmp_path)[-1] == "no_fill"
    buys = [o for o in client.orders.values()]
    assert {(o["side"], o["price"], o["qty"]) for o in buys} == {("up", 0.25, 4), ("down", 0.25, 4)}


def test_fill_cancels_other_side_and_places_sell(tmp_path):
    clock, client, tr = make(tmp_path, dict(fills={("up", "buy"): 30, ("up", "sell"): 200}))
    clock.t = WS
    tr.run_window(WS)
    sells = [o for o in client.orders.values() if o["action"] == "sell"]
    assert len(sells) == 1 and sells[0]["side"] == "up" and sells[0]["price"] == 0.45
    assert "o2" in client.cancelled                          # the Down buy
    assert "exit_fill" in events(tmp_path)
    assert tr.state["consecutive_losses"] == 0


def test_down_prices_sent_on_yes_side():
    assert pm_us.yes_price("down", 0.25) == 0.75 and pm_us.yes_price("up", 0.25) == 0.25
    assert pm_us.to_intent("down", "buy") == "ORDER_INTENT_BUY_SHORT"
    assert pm_us.window_slug(1790769600) == "cpc-btc-updown-15m-2026-09-30-1200z"


def test_unsold_loss_counts_and_five_losses_halt(tmp_path):
    clock, client, tr = make(tmp_path, dict(fills={("up", "buy"): 30}), settle=0.0)   # Up fills, Down wins
    for i in range(5):
        clock.t = WS + i * 900
        tr.run_window(WS + i * 900)
    assert tr.state["consecutive_losses"] == 5
    clock.t = WS + 5 * 900
    with pytest.raises(Halt):
        tr.run_window(WS + 5 * 900)
    assert tr.state["halted"] and client.cancel_all_calls >= 1


def test_balance_floor_halts(tmp_path):
    clock, client, tr = make(tmp_path, dict(balance=12.0))
    clock.t = WS
    with pytest.raises(Halt):
        tr.run_window(WS)
    assert tr.state["halted"] and not client.orders


def test_unexpected_error_halts_and_cancels(tmp_path):
    clock, client, tr = make(tmp_path, dict(fail_on="place"))
    clock.t = WS
    with pytest.raises(Halt):
        tr.run_window(WS)
    assert tr.state["halted"] and client.cancel_all_calls == 1


def test_startup_refuses_when_halted_or_clock_off(tmp_path):
    _, _, tr = make(tmp_path)
    tr.state["halted"] = True
    with pytest.raises(Halt):
        tr.startup()
    _, client, tr2 = make(tmp_path / "b", skew=1.5) if (tmp_path / "b").mkdir() is None else (None, None, None)
    with pytest.raises(Halt):
        tr2.startup()


def test_startup_cancels_leftover_orders(tmp_path):
    _, client, tr = make(tmp_path)
    tr.startup()
    assert client.cancel_all_calls == 1


def test_too_small_stake_skips(tmp_path):
    clock, client, tr = make(tmp_path, dict(balance=12.5))     # floor(12.5*0.05/0.25) = 2 -> ok
    clock.t = WS
    tr.run_window(WS)
    assert client.orders
    clock2, client2, tr2 = make(tmp_path / "c") if (tmp_path / "c").mkdir() is None else None
    client2._balance = 4.0
    tr2.cfg = dict(CFG, floor_balance=0)
    clock2.t = WS
    tr2.run_window(WS)
    assert not client2.orders and "skip" in events(tmp_path / "c")


def test_dry_run_sends_nothing():
    c = pm_us.DryRunClient(20)
    oid = c.place("slug", "up", "buy", 0.25, 4)
    assert c.filled_qty(oid)[0] == 0 and c.mode == "dry"
