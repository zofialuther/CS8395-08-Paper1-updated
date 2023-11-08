def ncsubs(L, LNCSL):
    LNCSL = set(one_ncsubs(L, NCSL))

def one_ncsubs(L, NCSL):
    if extract_elem(L, NCSL):
        return True
    else:
        L1 = sublist(L)
        return one_ncsubs(L1, NCSL)

def extract_elem(L, NCSL):
    Len = len(L)
    Len1 = Len - 2
    for I in range(1, Len1 + 1):
        Elem = L[I]
        NCS1 = L.index(Elem)
        if NCSL == NCS1:
            return True
        else:
            extract_elem(NCS1, NCSL)

def sublist(L):
    if len(L) > 0:
        return L
    else:
        return list(reversed(L))