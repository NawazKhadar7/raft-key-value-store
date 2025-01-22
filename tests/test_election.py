import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.cluster import Cluster
from syslab.raft_node import Node
class ElectionTests(unittest.TestCase):
    def test_single_vote_per_term(self):
        n=Node(0);self.assertTrue(n.request_vote(1,1,0,0));self.assertFalse(n.request_vote(1,2,0,0))
    def test_stale_candidate(self):
        c=Cluster();c.elect(0);c.put('x',1);c.nodes[2].log=c.nodes[2].log[:1]
        self.assertFalse(c.elect(2))
