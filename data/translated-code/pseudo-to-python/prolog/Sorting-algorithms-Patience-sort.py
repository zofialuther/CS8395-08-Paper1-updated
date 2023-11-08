def patience_sort(UnSorted, Sorted):
    Piled = make_piles(UnSorted, [])
    return merge_piles(Piled, [])

def make_piles(T, P):
    if len(T) == 0:
        return P
    if len(P) == 0:
        return make_piles(T[1:], [[T[0]]], P)
    if T[0] <= P[0][0]:
        return make_piles(T[1:], [[T[0], P[0][0]] + P[0][1:]], P)
    else:
        return make_piles(T[1:], [[T[0]], P[0]], P)

def merge_piles(T, L):
    if len(T) == 0:
        return L
    else:
        Pl = merge_pile(T[0], L)
        return merge_piles(T[1:], Pl)

def merge_pile(T1, T2):
    if len(T1) == 0:
        return T2
    if len(T2) == 0:
        return T1
    if T1[0] == T2[0]:
        return [T1[0], T1[0]] + merge_pile(T1[1:], T2[1:])
    if T1[0] > T2[0]:
        return [T2[0]] + merge_pile(T1, T2[1:])
    if T1[0] < T2[0]:
        return [T1[0]] + merge_pile(T1[1:], T2)