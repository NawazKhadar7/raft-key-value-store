from .raft_node import Node
from .membership import majority
class Cluster:
    def __init__(self,count=3):
        if count<3 or count%2==0:raise ValueError('odd cluster >=3 required')
        self.nodes={i:Node(i) for i in range(count)};self.blocked=set();self.leader=None;self.next_index={};self.match_index={}
    def reachable(self,a,b):return self.nodes[a].alive and self.nodes[b].alive and tuple(sorted((a,b))) not in self.blocked
    def partition(self,left,right):
        for a in left:
            for b in right:self.blocked.add(tuple(sorted((a,b))))
    def heal(self):self.blocked.clear()
    def elect(self,candidate):
        node=self.nodes[candidate]
        if not node.alive:return False
        node.term+=1;node.role='candidate';node.voted_for=candidate;node.persist();votes={candidate}
        for identity,peer in self.nodes.items():
            if identity!=candidate and self.reachable(candidate,identity):
                if peer.request_vote(node.term,candidate,len(node.log)-1,node.log[-1]['term']):votes.add(identity)
                if peer.term>node.term:node.observe_term(peer.term);return False
        if majority(votes,self.nodes):
            self.leader=candidate;node.role='leader';self.next_index={i:len(node.log) for i in self.nodes};self.match_index={i:0 for i in self.nodes};self.match_index[candidate]=len(node.log)-1;return True
        node.role='follower';return False
    def replicate(self):
        if self.leader is None:return False
        leader=self.nodes[self.leader]
        if not leader.alive or leader.role!='leader':return False
        self.match_index[leader.id]=len(leader.log)-1
        for identity,peer in self.nodes.items():
            if identity==leader.id or not self.reachable(leader.id,identity):continue
            if peer.term>leader.term:leader.observe_term(peer.term);self.leader=None;return False
            next_index=min(self.next_index.get(identity,len(leader.log)),len(leader.log))
            while next_index>=1:
                previous=next_index-1
                if peer.append_entries(leader.term,leader.id,previous,leader.log[previous]['term'],leader.log[next_index:],leader.commit):
                    self.match_index[identity]=len(leader.log)-1;self.next_index[identity]=len(leader.log);break
                next_index-=1
        for index in range(len(leader.log)-1,leader.commit,-1):
            acks={i for i,matched in self.match_index.items() if matched>=index}
            if leader.log[index]['term']==leader.term and majority(acks,self.nodes):leader.commit=index;break
        leader.apply()
        for identity,peer in self.nodes.items():
            if identity!=leader.id and self.reachable(leader.id,identity):
                next_index=self.next_index.get(identity,1);prev=next_index-1
                peer.append_entries(leader.term,leader.id,prev,leader.log[prev]['term'],leader.log[next_index:],leader.commit)
        return True
    def put(self,key,value):
        if self.leader is None:return False
        leader=self.nodes[self.leader]
        if not leader.alive or leader.role!='leader':return False
        leader.log.append({'term':leader.term,'command':{'key':key,'value':value}});leader.persist();index=len(leader.log)-1;self.replicate()
        return leader.commit>=index
    def safety(self):
        for a in self.nodes.values():
            for b in self.nodes.values():
                upto=min(a.commit,b.commit)
                if a.log[:upto+1]!=b.log[:upto+1]:return False
        return True
