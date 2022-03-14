import nuke

def tuplesToAnimationKeys(tupleList):
    return map(lambda (x,y): nuke.AnimationKey(x,y),tupleList)