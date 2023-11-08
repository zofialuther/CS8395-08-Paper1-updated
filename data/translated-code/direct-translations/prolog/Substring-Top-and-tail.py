def remove_first_last_chars():
    L = "Rosetta"
    L1 = list(L)
    L2 = remove_last(L1)
    L3 = remove_last(L1[:-1])
    print('Original string      : %s' % L)
    print('Without first char       : %s' % ''.join(L1[1:]))
    print('Without last char        : %s' % ''.join(L2))
    print('Without first/last chars : %s' % ''.join(L3))

def remove_last(L):
    return L[:-1]