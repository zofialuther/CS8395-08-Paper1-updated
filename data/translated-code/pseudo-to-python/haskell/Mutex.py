def takeMVar(mVar):
    return mVar.value

def putMVar(mVar, value):
    mVar.value = value

def tryTakeMVar(mVar):
    if mVar.value is not None:
        return Just(mVar.value)
    else:
        return Nothing

def tryPutMVar(mVar, value):
    if mVar.value is None:
        mVar.value = value
        return True
    else:
        return False