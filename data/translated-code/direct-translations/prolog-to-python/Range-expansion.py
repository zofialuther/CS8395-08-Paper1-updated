def range_expand():
    L = '-6,-3--1,3-5,7-11,14,15,17-20'
    print(L)
    LA = list(L)
    R = extract_Range(LA)
    LR = list(map(study_Range, R))
    LX = pack_Range(LR)
    print(LX)

def extract_Range(X):
    if not X:
        return []
    else:
        Range, X1 = get_Range(X, [], [])
        return [Range] + extract_Range(X1)

def get_Range(X, EC, Range):
    if not X:
        return Range, [], []
    elif X[0] == ',':
        return Range, [], X[1:]
    else:
        new_EC = EC + [X[0]]
        return get_Range(X[1:], new_EC, Range)

def study_Range(Range1):
    if Range1[0] == Range1[1]:
        return [Range1[0], Range1[1]]
    else:
        Deb = int(''.join(Range1[0].split(',')))
        Fin = int(''.join(Range1[1].split(',')))
        return [Deb, Fin]

def pack_Range(Rest):
    if not Rest:
        return []
    else:
        X, RRest = Rest[0], Rest[1:]
        V = [X[0]]
        packed, new_RRest = run(X, RRest, V, [])
        return [packed] + pack_Range(new_RRest)

def run(Fin, Rest, V, RRest):
    if not Rest:
        return [V, Fin], []
    else:
        Var, LRest = Rest[0], Rest[1:]
        if Fin != Var and Fin != Var + 1:
            return [V, Fin], [Var] + LRest
        elif Var == Fin + 1:
            return run(Var, LRest, V, RRest)
        else:
            return [Fin, Fin], [Var] + LRest

range_expand()