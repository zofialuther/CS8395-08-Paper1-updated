def patience_sort(UnSorted, Sorted):
    piled = make_piles(UnSorted, [])
    merge_piles(piled, [], Sorted)

def make_piles([], P):
    return P
def make_piles([N|T], [], R):
    return make_piles(T, [[N]], R)
def make_piles([N|T], [[P|Pnt]|Tp], R):
    if N <= P:
        return make_piles(T, [[N, P|Pnt]|Tp], R)
    else:
        return make_piles(T, [[N], [P|Pnt]|Tp], R)

def merge_piles([], M, M):
    return M
def merge_piles([P|T], L, R):
    Pl = merge_pile(P, L)
    return merge_piles(T, Pl, R)

def merge_pile([], M, M):
    return M
def merge_pile(M, [], M):
    return M
def merge_pile([N|T1], [N|T2], [N, N|R]):
    return merge_pile(T1, T2, R)
def merge_pile([N|T1], [P|T2], [P|R]):
    if N > P:
        return merge_pile([N|T1], T2, R)
    else:
        return merge_pile(T1, [P|T2], R)