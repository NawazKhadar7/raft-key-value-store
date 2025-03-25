import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.raft_node import Node
from syslab.storage import StateStorage
class PersistenceTests(unittest.TestCase):
    def test_restart_vote(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'state';n=Node(0,StateStorage(path));n.request_vote(3,2,0,0);other=Node(0,StateStorage(path));self.assertEqual(other.term,3);self.assertEqual(other.voted_for,2)
    def test_corruption(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'state';s=StateStorage(path);s.save({'term':1});v=json.loads(path.read_text());v['state']['term']=8;path.write_text(json.dumps(v))
            with self.assertRaises(ValueError):s.load()
