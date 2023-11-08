def look_and_say(L):
    for item in L:
        print(item, end="")
    print()
    L1 = encode(L)
    look_and_say(L1)

def encode(In):
    R1 = packList(In)
    return R1

def packList(L):
    if len(L) == 0:
        return []
    if len(L) == 1:
        return [[1, L[0]]]
    
    X = L[0]
    XRun, Packed = run(X, L[1:])
    return [XRun] + Packed

def run(Var, L):
    if len(L) == 0:
        return [1, Var], []

    if L[0] == Var:
        N1, RRest = run(Var, L[1:])
        return [N1, Var], RRest
    else:
        return [1, Var], L

# Example usage
look_and_say(['a', 'a', 'a', 'b', 'c', 'c', 'c', 'd', 'd', 'e'])