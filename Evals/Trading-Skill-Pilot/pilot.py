#!/usr/bin/env python3
"""Offline, synthetic trading-method pilot. Not a broker/trading client."""
from __future__ import annotations
import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path

START_CAPITAL = 1000.0
EXPOSED_CAPITAL = 200.0
MAX_CAPITAL_AT_RISK = 200.0
DRAWDOWN_HALT = 100.0


def prices(seed: int, length: int = 160) -> list[float]:
    """Deterministic fabricated prices, NOT historical market data."""
    assert length >= 65
    p = 100.0
    series = []
    for t in range(length):
        delta = (0.001 if t < 95 else -0.0013) + math.sin((t + seed) / 5) * 0.008
        p *= 1 + delta
        series.append(round(p, 6))
    return series


def walk_forward_splits(length: int, train_size: int = 60, test_size: int = 20, embargo: int = 2) -> list[tuple[range, range]]:
    """Nonoverlapping forward test blocks; never use a test row for training."""
    if length < 0 or train_size < 1 or test_size < 1 or embargo < 0:
        raise ValueError('invalid split configuration')
    result = []
    for train_end in range(train_size, length - embargo - test_size + 1, test_size):
        training = range(train_end - train_size, train_end)
        testing = range(train_end + embargo, train_end + embargo + test_size)
        result.append((training, testing))
    return result


def max_drawdown(equity: list[float]) -> float:
    peak, worst = equity[0], 0.0
    for val in equity:
        peak = max(peak, val)
        worst = max(worst, (peak - val) / peak)
    return worst


def simulate(close: list[float], *, strategy: str, fee_per_side: float) -> dict:
    """Signal from yesterday's completed bar, fill at next daily close (conservative simplified proxy).

    Cash has no return in this demonstration. Only one active cash-funded spot position.
    No leverage/shorting. Trade logs contain cost and the signal index.
    """
    if strategy not in {'hold', 'trend'}:
        raise ValueError('unknown strategy')
    if len(close) < 65 or min(close) <= 0 or fee_per_side < 0:
        raise ValueError('invalid input')
    # The 800 EUR reserve NEVER participates in trading, including after losses.
    reserve = START_CAPITAL - EXPOSED_CAPITAL
    active_cash = EXPOSED_CAPITAL
    qty = 0.0
    entry_price = None
    peak = START_CAPITAL
    ledger = []
    equity = [START_CAPITAL]
    halted = False
    for t in range(1, len(close)):
        prev = t - 1
        if strategy == 'hold':
            want_long = True
        else:
            # All input indices <= prev, NEVER the fill bar t.
            avg20 = sum(close[prev - 19:prev + 1]) / 20 if prev >= 19 else None
            avg50 = sum(close[prev - 49:prev + 1]) / 50 if prev >= 49 else None
            want_long = avg20 is not None and avg50 is not None and close[prev] > avg20 > avg50
        # Do not use a stop as a guarantee of fill; exit is at the next price bar.
        stop_triggered = entry_price is not None and close[prev] <= 0.92 * entry_price
        mark_before = reserve + active_cash + qty * close[t]
        peak = max(peak, mark_before)
        if mark_before <= START_CAPITAL - DRAWDOWN_HALT:
            halted = True
        if qty and (not want_long or stop_triggered or halted):
            proceeds = qty * close[t]
            effective_fee = min(fee_per_side, proceeds)
            active_cash += proceeds - effective_fee
            ledger.append({'bar': t, 'signal_bar': prev, 'action': 'SELL', 'price': close[t], 'fee': effective_fee})
            qty = 0.0
            entry_price = None
        if want_long and not halted and qty == 0 and active_cash > fee_per_side:
            # Explicitly prevent borrowing from the 800-euro reserve.
            gross = min(EXPOSED_CAPITAL, active_cash)
            qty = (gross - fee_per_side) / close[t]
            active_cash -= gross
            entry_price = close[t]
            ledger.append({'bar': t, 'signal_bar': prev, 'action': 'BUY', 'price': close[t], 'fee': fee_per_side})
        eq = reserve + active_cash + qty * close[t]
        equity.append(eq)
        peak = max(peak, eq)
    return {
        'strategy': strategy, 'ending_eur': round(equity[-1], 3),
        'profit_eur': round(equity[-1] - START_CAPITAL, 3),
        'max_drawdown_pct': round(max_drawdown(equity) * 100, 3),
        'trades': len(ledger), 'fees_eur': round(sum(x['fee'] for x in ledger), 3),
        'halted': halted, 'ledger': ledger, 'min_reserve_eur': reserve,
        'synthetic': True, 'model_run': False,
    }


def validate_agent_decision(payload: dict, *, cutoff: str) -> list[str]:
    """Structural admission checks; ISO8601 UTC decision cutoff, no financial-accuracy claim."""
    issues = []
    def parse_utc(value):
        if not isinstance(value, str) or len(value) != 20 or value[4] != '-' or not value.endswith('Z'):
            raise ValueError('non-canonical UTC timestamp')
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if parsed.tzinfo != timezone.utc:
            raise ValueError('non UTC timezone')
        return parsed
    try:
        cutoff_dt = parse_utc(cutoff)
    except (TypeError, ValueError):
        raise ValueError('invalid caller cutoff')
    if not isinstance(payload, dict):
        return ['not_object']
    if payload.get('decision') not in ('BUY', 'NO_TRADE'):
        issues.append('invalid_decision')
    if payload.get('mode') not in ('PAPER',):
        issues.append('non_paper_mode')
    if payload.get('execution_allowed') is not False:
        issues.append('execution_not_blocked')
    if payload.get('leverage', 0) != 0:
        issues.append('leverage_not_zero')
    amount = payload.get('position_eur')
    if isinstance(amount, bool) or not isinstance(amount, (int, float)) or not math.isfinite(amount) or amount < 0 or amount > 200:
        issues.append('invalid_exposure')
    if payload.get('decision') == 'NO_TRADE' and amount != 0:
        issues.append('no_trade_with_exposure')
    evidence = payload.get('evidence')
    if payload.get('decision') == 'BUY' and (not isinstance(evidence, list) or not evidence):
        issues.append('missing_evidence')
    if isinstance(evidence, list):
        for item in evidence:
            if not isinstance(item, dict) or not isinstance(item.get('published_utc'), str) or not item.get('source'):
                issues.append('malformed_evidence')
                continue
            try:
                if parse_utc(item['published_utc']) > cutoff_dt:
                    issues.append('lookahead_evidence')
            except (TypeError, ValueError):
                issues.append('malformed_evidence_timestamp')
    if payload.get('data_cutoff_utc') != cutoff:
        issues.append('cutoff_mismatch')
    return sorted(set(issues))


def main():
    ap = argparse.ArgumentParser(description='Synthetic offline trading pilot; no network, no real orders')
    ap.add_argument('--output', default='-', help='Report JSON path or - for stdout')
    args = ap.parse_args()
    data = {
        'notice': 'SYNTHETIC FIXTURE. Not a live profit/skill-efficacy claim.',
        'baseline': simulate(prices(3), strategy='hold', fee_per_side=1.00),
        'stock_rules': simulate(prices(3), strategy='trend', fee_per_side=1.00),
        'crypto_rules': simulate(prices(9), strategy='trend', fee_per_side=0.80),
        'walk_forward_splits_demo': [{'train_last': a[-1], 'test_first': b[0]} for a,b in walk_forward_splits(160)],
        'claude_no_skills': 'NOT_RUN', 'claude_with_skills': 'NOT_RUN',
    }
    report = json.dumps(data, ensure_ascii=False, indent=2)
    if args.output == '-':
        print(report)
    else:
        Path(args.output).write_text(report + '\n', encoding='utf-8')
        print(f'Wrote synthetic report: {args.output}')

if __name__ == '__main__':
    main()
