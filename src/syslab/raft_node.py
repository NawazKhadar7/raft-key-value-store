from .storage import StateStorage
class Node:
    def __init__(self,identity,storage=None):
        self.id=identity;self.storage=storage or StateStorage();self.term=0;self.voted_for=None;self.log=[{'term':0,'command':None}];self.commit=0;self.applied=0;self.kv={};self.role='follower';self.alive=True
        saved=self.storage.load()
        if saved:self.term=saved['term'];self.voted_for=saved['voted_for'];self.log=saved['log']
    def persist(self):self.storage.save({'term':self.term,'voted_for':self.voted_for,'log':self.log})
    def observe_term(self,term):
        if term>self.term:self.term=term;self.voted_for=None;self.role='follower';self.persist()
    def request_vote(self,term,candidate,last_index,last_term):
        if not self.alive:return False
        self.observe_term(term)
        fresh=(last_term,last_index)>=(self.log[-1]['term'],len(self.log)-1)
        if term==self.term and fresh and self.voted_for in (None,candidate):
            self.voted_for=candidate;self.persist();return True
        return False
    def append_entries(self,term,leader,previous,previous_term,entries,commit):
        if not self.alive:return False
        self.observe_term(term)
        if term<self.term:return False
        self.role='follower'
        if previous>=len(self.log) or self.log[previous]['term']!=previous_term:return False
        for offset,entry in enumerate(entries,start=previous+1):
            if offset<len(self.log) and self.log[offset]['term']!=entry['term']:
                if offset<=self.commit:raise AssertionError('cannot overwrite committed entry')
                self.log=self.log[:offset]
            if offset==len(self.log):self.log.append(dict(entry))
        self.persist();self.commit=max(self.commit,min(commit,len(self.log)-1));self.apply();return True
    def apply(self):
        while self.applied<self.commit:
            self.applied+=1;command=self.log[self.applied]['command']
            if command:self.kv[command['key']]=command['value']
