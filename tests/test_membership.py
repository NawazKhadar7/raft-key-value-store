import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.membership import joint_quorum,majority
class MembershipTests(unittest.TestCase):
    def test_both_majorities_required(self):
        self.assertFalse(joint_quorum({0,1},{0,1,2},{1,2,3}));self.assertTrue(joint_quorum({1,2},{0,1,2},{1,2,3}))
    def test_empty_configuration(self):
        with self.assertRaises(ValueError):majority([],[])
