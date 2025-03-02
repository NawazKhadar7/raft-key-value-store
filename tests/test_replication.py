import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.cluster import Cluster
class ReplicationTests(unittest.TestCase):
    def test_uncommitted_conflict_repaired(self):
        c=Cluster();c.elect(0);c.partition([0],[1,2]);self.assertFalse(c.put('bad',1));self.assertTrue(c.elect(1));self.assertTrue(c.put('good',2));c.heal();c.replicate()
        self.assertNotIn('bad',c.nodes[0].kv);self.assertEqual(c.nodes[0].kv['good'],2);self.assertTrue(c.safety())
    def test_no_quorum_no_apply(self):
        c=Cluster();c.elect(0);c.partition([0],[1,2]);self.assertFalse(c.put('x',2));self.assertEqual(c.nodes[0].kv,{})
