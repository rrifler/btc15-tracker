"""Live trading loop for the 25c -> 45c strategy. Hard limits live here, not in config you can forget."""
import csv
import json
import math
import os
import time

from . import pm_us
from .pm_us import BUY, DOWN, SELL, UP

LOG_COLS = ["ts_utc", "window_start", "mode", "event", "side", "price", "qty", "order_id", "detail"]
WINDOW_S = 900


class Halt(Exception):
    """Trading stopped on purpose. The job fails so GitHub emails the owner."""


class Trader:
    def __init__(self, client, cfg, state_path="results/state.json", log_path="results/live_trades.csv",
                 now=time.time, sleep=time.sleep, settle=pm_us.settlement, skew=pm_us.clock_skew_seconds):
        self.client, self.cfg = client, cfg
        self.state_path, self.log_path = state_path, log_path
        self.now, self.sleep, self.settle, self.skew = now, sleep, settle, skew
        self.state = self._load_state()

    # ---- state and log -------------------------------------------------------------------
    def _load_state(self):
        if os.path.exists(self.state_path):
            with open(self.state_path) as f:
                return json.load(f)
        return {"halted": False, "consecutive_losses": 0, "reason": ""}

    def _save_state(self):
        os.makedirs(os.path.dirname(self.state_path) or ".", exist_ok=True)
        with open(self.state_path, "w") as f:
            json.dump(self.state, f, indent=2)

    def log(self, ws, event, side="", price="", qty="", order_id="", detail=""):
        new = not os.path.exists(self.log_path)
        os.makedirs(os.path.dirname(self.log_path) or ".", exist_ok=True)
        with open(self.log_path, "a", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            if new:
                w.writerow(LOG_COLS)
            w.writerow([time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(self.now())), ws, self.client.mode,
                        event, side, price, qty, order_id, detail])

    def halt(self, reason, ws=""):
        try:
            self.client.cancel_all()
        finally:
            self.state.update(halted=True, reason=reason)
            self._save_state()
            self.log(ws, "halt", detail=reason)
        raise Halt(reason)

    # ---- startup -------------------------------------------------------------------------
    def startup(self):
        if self.state.get("halted"):
            raise Halt(f"previous run halted: {self.state.get('reason')}. Set halted to false to resume.")
        skew = self.skew()
        if abs(skew) > 1.0:
            self.halt(f"clock off by {skew:.1f}s")
        self.client.cancel_all()
        self.log("", "startup", detail=f"mode={self.client.mode} skew={skew:.2f}s")

    # ---- one window ----------------------------------------------------------------------
    def run_window(self, ws):
        cfg = self.cfg
        slug = pm_us.window_slug(ws)
        try:
            self._run_window(ws, slug, cfg)
        except Halt:
            raise
        except Exception as e:  # any unexpected API error stops trading
            self.halt(f"unexpected error: {type(e).__name__}: {e}", ws)

    def _run_window(self, ws, slug, cfg):
        balance = self.client.balance()
        if balance <= cfg["floor_balance"]:
            self.halt(f"balance ${balance:.2f} at or below floor ${cfg['floor_balance']}", ws)
        if self.state["consecutive_losses"] >= cfg["max_consecutive_losses"]:
            self.halt(f"{self.state['consecutive_losses']} losses in a row", ws)
        entry, exit_p = cfg["entry_price"], cfg["exit_price"]
        qty = math.floor(balance * cfg["stake_pct"] / entry)
        if qty < cfg["min_shares"]:
            self.log(ws, "skip", detail=f"too_small balance={balance:.2f}")
            return
        buys = {}
        for side in (UP, DOWN):
            oid = self.client.place(slug, side, BUY, entry, qty)
            buys[side] = oid
            self.log(ws, "buy_placed", side, entry, qty, oid)
        # watch the buys until +entry_window_s
        filled = {}
        deadline = ws + cfg["entry_window_s"]
        while self.now() < deadline and not filled:
            for side, oid in buys.items():
                n, _ = self.client.filled_qty(oid)
                if n > 0:
                    filled[side] = n
            if not filled:
                self.sleep(1)
        for side, oid in buys.items():
            if side not in filled:
                n, _ = self.client.filled_qty(oid)       # last look before cancelling
                if n > 0:
                    filled[side] = n
                    self.log(ws, "fill", side, entry, n, oid, "late fill before cancel")
                else:
                    self.client.cancel(slug, oid)
                    self.log(ws, "buy_cancelled", side, entry, qty, oid)
            else:
                self.log(ws, "fill", side, entry, filled[side], oid)
        if not filled:
            self.log(ws, "no_fill")
            return
        sells = {}
        for side, n in filled.items():
            oid = self.client.place(slug, side, SELL, exit_p, n)
            sells[side] = oid
            self.log(ws, "sell_placed", side, exit_p, n, oid)
        # wait for exit fills until window end
        end = ws + WINDOW_S
        exited = {}
        while self.now() < end and len(exited) < len(sells):
            for side, oid in sells.items():
                if side in exited:
                    continue
                n, _ = self.client.filled_qty(oid)
                if n >= filled[side]:
                    exited[side] = n
                    self.log(ws, "exit_fill", side, exit_p, n, oid)
            if len(exited) < len(sells):
                self.sleep(1)
        for side, oid in sells.items():
            if side not in exited:
                self.client.cancel(slug, oid)
                self.log(ws, "sell_cancelled", side, exit_p, filled[side], oid)
        self._settle(ws, slug, filled, exited)

    def _settle(self, ws, slug, filled, exited):
        entry, exit_p = self.cfg["entry_price"], self.cfg["exit_price"]
        pnl = 0.0
        for side, n in filled.items():
            if side in exited:
                pnl += n * (exit_p - entry)
        open_sides = [s for s in filled if s not in exited]
        if open_sides:
            value = None
            for _ in range(20):                       # settlement lands within about a minute
                value = self.settle(slug)
                if value is not None:
                    break
                self.sleep(15)
            if value is None:
                self.halt("settlement not available after 5 minutes", ws)
            for side in open_sides:
                won = (value == 1.0) == (side == UP)
                pnl += filled[side] * ((1.0 if won else 0.0) - entry)
                self.log(ws, "settled", side, 1.0 if won else 0.0, filled[side], detail=f"settlement={value}")
        self.state["consecutive_losses"] = self.state["consecutive_losses"] + 1 if pnl < 0 else 0
        self._save_state()
        self.log(ws, "window_pnl", detail=f"{pnl:.4f} losses_in_row={self.state['consecutive_losses']}")

    # ---- loop ----------------------------------------------------------------------------
    def run(self, until):
        """Trade each window until `until` (epoch seconds), then cancel everything."""
        self.startup()
        try:
            ws = (int(self.now()) // WINDOW_S + 1) * WINDOW_S
            while ws + WINDOW_S + 300 <= until:
                while self.now() < ws:
                    self.sleep(min(1.0, max(0.05, ws - self.now())))
                if self.now() - ws > 2:
                    self.log(ws, "late_start", detail=f"{self.now() - ws:.1f}s late, window skipped")
                else:
                    self.run_window(ws)
                ws += WINDOW_S
                while self.now() >= ws:
                    ws += WINDOW_S
        finally:
            self.client.cancel_all()
            self.log("", "shutdown", detail="cancelled all open orders")
