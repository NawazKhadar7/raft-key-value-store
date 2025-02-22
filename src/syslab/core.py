from .common import validate_case
from .cluster import Cluster
from .membership import joint_quorum
FAMILIES=('steady','follower-crash','leader-crash','partition','no-quorum','membership')
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown Raft family')
    c=Cluster();assert c.elect(0);family=case['family'];n=case['size'];acknowledged=0;checks=[]
    if family=='follower-crash':c.nodes[2].alive=False
    if family=='partition':c.partition([0,1],[2])
    if family=='no-quorum':c.partition([0],[1,2])
    for i in range(n):
        if family=='leader-crash' and i==n//2:
            c.nodes[0].alive=False;assert c.elect(1)
        ok=c.put(f'k{i}',i);acknowledged+=ok;checks.append(c.safety())
    if family not in ('no-quorum','leader-crash'):
        c.nodes[2].alive=True;c.heal();c.replicate()
    leader=c.nodes[c.leader] if c.leader is not None else c.nodes[0]
    joint=joint_quorum({0,1,2},{0,1,2},{1,2,3}) and not joint_quorum({0,1},{0,1,2},{1,2,3})
    return {'metrics':{'attempted':n,'acknowledged':acknowledged,'rejected':n-acknowledged,'committed_keys':len(leader.kv),'committed_prefix_safe':all(checks),'joint_quorum_rule':joint,'leader_term':leader.term},'output':{'leader':c.leader,'nodes':[{'id':node.id,'term':node.term,'commit':node.commit,'alive':node.alive,'keys':len(node.kv)} for node in c.nodes.values()]}}
