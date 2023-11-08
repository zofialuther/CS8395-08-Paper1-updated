def remove_last(L, LR):
    LR = L[:-1]

def remove_first_last_chars():
    L = "Rosetta"
    L1 = L[1:]
    L2 = L[:-1]
    L3 = L[1:-1]
    print('Original string      : %s' % L)
    print('Without first char       : %s' % L1)
    print('Without last char        : %s' % L2)
    print('Without first/last chars : %s' % L3)