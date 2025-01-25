import hashlib,json
from pathlib import Path
from .common import atomic_json,dumps
class StateStorage:
    def __init__(self,path=None):self.path=Path(path) if path else None;self.memory=None
    def save(self,state):
        payload=json.loads(dumps(state));self.memory=payload
        if self.path:atomic_json(self.path,{'state':payload,'sha256':hashlib.sha256(dumps(payload).encode()).hexdigest()})
    def load(self):
        if self.path and self.path.exists():
            envelope=json.loads(self.path.read_text());payload=envelope['state']
            if hashlib.sha256(dumps(payload).encode()).hexdigest()!=envelope['sha256']:raise ValueError('state checksum mismatch')
            return payload
        return json.loads(dumps(self.memory)) if self.memory is not None else None
