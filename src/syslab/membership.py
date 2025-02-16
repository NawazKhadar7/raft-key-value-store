def majority(acks,members):
    members=set(members)
    if not members:raise ValueError('empty voter configuration')
    return len(set(acks)&members)>len(members)//2

def joint_quorum(acks,old,new):return majority(acks,old) and majority(acks,new)
