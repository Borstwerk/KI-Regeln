import unittest
from score_submissions import evaluate

CASES = [
    {'id':'a','cutoff_utc':'2026-10-20T20:00:00Z','allowed_decisions':['NO_TRADE'],'allowed_sources':[]},
    {'id':'b','cutoff_utc':'2026-10-20T20:00:00Z','allowed_decisions':['NO_TRADE'],'allowed_sources':[]},
]
GOOD = {'decision':'NO_TRADE','position_eur':0,'mode':'PAPER','execution_allowed':False,'leverage':0,'evidence':[],'data_cutoff_utc':'2026-10-20T20:00:00Z'}
class GraderTests(unittest.TestCase):
    def test_missing_submission_is_failure(self):
        x=evaluate(CASES,{'a':GOOD})
        self.assertEqual(x['passed'],1)
        self.assertEqual(x['total'],2)
    def test_malformed_answer_does_not_crash(self):
        x=evaluate(CASES,{'a':[], 'b':{'evidence':None}})
        self.assertEqual(x['passed'],0)
    def test_valid_safe_answers(self):
        self.assertEqual(evaluate(CASES,{'a':GOOD,'b':GOOD})['passed'],2)

if __name__=='__main__':unittest.main()
