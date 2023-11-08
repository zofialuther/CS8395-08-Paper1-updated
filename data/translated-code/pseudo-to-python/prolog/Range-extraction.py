L = [0, 1, 2, 4, 6, 7, 8, 11, 12, 14,
         15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
         25, 27, 28, 29, 30, 31, 32, 33, 35, 36,
         37, 38, 39]
print(L)

def extract_Range(X, Y1):
    if not X:
        return []
    else:
        Range, X1 = get_Range(X, [], [])
        return [Range] + extract_Range(X1, Y1)

def get_Range(B, Range, R):
    if not B:
        return Range, [], R
    elif B[0] == ',':
        return Range, [], B[1:]
    else:
        return get_Range(B[1:], Range + [B[0]], R)

def study_Range(Range1):
    if '-' in Range1:
        Deb, Fin = map(int, Range1.split('-'))
        return [Deb, Fin]
    else:
        Deb = int(Range1)
        return [Deb, Deb]

def pack_Range(L):
    if not L:
        return []
    else:
        X = L[0]
        Rest = L[1:]
        V = [X]
        Packed = run(X, Rest, [X], [])
        return [[X] + V] + pack_Range(Packed)

def run(Var, LRest, Range, RRest):
    if not LRest:
        return [Var], []
    else:
        Var1 = LRest[0]
        if Var1 != Var and Var1 != Var + 1:
            return Range + [Var], LRest
        elif Var1 == Var + 1:
            return run(Var1, LRest[1:], Range, RRest)
        else:
            return Range + [Var], LRest[1:]