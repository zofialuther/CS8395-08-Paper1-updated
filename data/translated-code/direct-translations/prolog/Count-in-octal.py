def o(O):
    return O in [0,1,2,3,4,5,6,7]

def octal(O):
    return o(O)

def octal_list(A, B):
    O = octal(O)
    T = octal(O)
    return O + [T] == [A] + B and A != 0

def octalize():
    for X in range(0, 8):
        print(X)
        print("\n")