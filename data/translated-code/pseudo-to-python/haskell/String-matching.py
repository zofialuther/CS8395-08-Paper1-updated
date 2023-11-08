def isPrefixOf(a, b):
    if b.startswith(a):
        return True
    else:
        return False

def isSuffixOf(a, b):
    if b.endswith(a):
        return True
    else:
        return False

def isInfixOf(a, b):
    if a in b:
        return True
    else:
        return False

def infixes(a, b):
    indices = [i for i in range(len(b)) if isPrefixOf(a, b[i:])]
    return indices