def multiple_arrays(L1, L2, L3):
    for a, b, c in zip(L1, L2, L3):
        display(a, b, c)

def display(A, B, C):
    print('%s%s%s' % (A, B, C))