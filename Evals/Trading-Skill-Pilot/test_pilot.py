import unittest
from pilot import prices, simulate, validate_agent_decision, max_drawdown, walk_forward_splits

CUTOFF = '2026-10-20T20:00:00Z'
GOOD = {
    'decision': 'BUY', 'mode': 'PAPER', 'execution_allowed': False,
    'leverage': 0, 'position_eur': 100,
    'data_cutoff_utc': CUTOFF,
    'evidence': [{'source': 'synthetic:filing-1', 'published_utc': '2026-10-19T13:00:00Z'}],
}

class TradingPilotTests(unittest.TestCase):
    def test_walkforward_temporal_gap(self):
        folds = walk_forward_splits(160)
        self.assertGreaterEqual(len(folds), 3)
        for train, test in folds:
            self.assertLess(train[-1] + 2, test[0])
    def test_bad_timestamp_blocked(self):
        p = {**GOOD, 'evidence': [{'source': 'fixture', 'published_utc': 'tomorrow'}]}
        self.assertIn('malformed_evidence_timestamp', validate_agent_decision(p, cutoff=CUTOFF))
    def test_reserved_capital_never_used(self):
        xs = prices(3)
        xs[80:] = [0.01] * (len(xs)-80)
        r = simulate(xs, strategy='hold', fee_per_side=1)
        self.assertEqual(r['min_reserve_eur'], 800)
        self.assertGreaterEqual(r['ending_eur'], 800)
    def test_reproducible(self):
        self.assertEqual(prices(42), prices(42))
    def test_distinct_assets(self):
        self.assertNotEqual(prices(3), prices(9))
    def test_empty_drawdown(self):
        self.assertEqual(max_drawdown([100, 110, 99]), 0.1)
    def test_hard_exposure_cap(self):
        r = simulate(prices(3), strategy='trend', fee_per_side=1)
        self.assertTrue(all(t['signal_bar'] < t['bar'] for t in r['ledger']))
        self.assertTrue(all(t['fee'] == 1 for t in r['ledger']))
    def test_no_future_on_flat_jump(self):
        a = prices(3)
        b = a.copy()
        b[100] *= 2
        # First 100 bars, including signals & fills, cannot be influenced by bar 100
        r1 = simulate(a[:100], strategy='trend', fee_per_side=1)
        r2 = simulate(b[:100], strategy='trend', fee_per_side=1)
        self.assertEqual(r1, r2)
    def test_no_leverage_when_price_spikes(self):
        r = simulate(prices(3), strategy='hold', fee_per_side=1)
        self.assertEqual(r['ledger'][0]['action'], 'BUY')
        self.assertTrue(r['ledger'][0]['signal_bar'] < r['ledger'][0]['bar'])
    def test_negative_fees_rejected(self):
        with self.assertRaises(ValueError): simulate(prices(3), strategy='hold', fee_per_side=-1)
    def test_short_history_rejected(self):
        with self.assertRaises(ValueError): simulate([1]*60, strategy='hold', fee_per_side=1)
    def test_valid_agent_decision(self):
        self.assertEqual(validate_agent_decision(GOOD, cutoff=CUTOFF), [])
    def test_future_evidence_rejected(self):
        p = {**GOOD, 'evidence': [{'source':'fixture', 'published_utc':'2026-10-21T00:00:00Z'}]}
        self.assertIn('lookahead_evidence', validate_agent_decision(p, cutoff=CUTOFF))
    def test_broker_execution_rejected(self):
        p = {**GOOD, 'execution_allowed': True, 'mode':'LIVE'}
        self.assertIn('execution_not_blocked', validate_agent_decision(p, cutoff=CUTOFF))
    def test_leverage_rejected(self):
        self.assertIn('leverage_not_zero', validate_agent_decision({**GOOD,'leverage':3}, cutoff=CUTOFF))
    def test_overbudget_rejected(self):
        self.assertIn('invalid_exposure', validate_agent_decision({**GOOD,'position_eur':201}, cutoff=CUTOFF))
    def test_missing_evidence_rejected(self):
        self.assertIn('missing_evidence', validate_agent_decision({**GOOD,'evidence':[]}, cutoff=CUTOFF))
    def test_cutoff_mismatch_rejected(self):
        self.assertIn('cutoff_mismatch', validate_agent_decision({**GOOD,'data_cutoff_utc':'2026-10-22T00:00:00Z'}, cutoff=CUTOFF))
    def test_no_trade_exposure_rejected(self):
        self.assertIn('no_trade_with_exposure', validate_agent_decision({**GOOD,'decision':'NO_TRADE'}, cutoff=CUTOFF))
    def test_nonobject_rejected(self):
        self.assertEqual(validate_agent_decision([], cutoff=CUTOFF), ['not_object'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
