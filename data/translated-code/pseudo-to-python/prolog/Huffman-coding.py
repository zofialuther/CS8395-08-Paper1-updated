def huffman():
    L = 'this is an example for huffman encoding'
    LA = list(L)
    LS = sorted(LA)
    PL = packList(LS)
    PLS = sorted(PL)
    A = build_tree(PLS)
    C = coding(A, [])
    SC = sorted(C)
    print('Symbol   Weight                            Code')
    for element in SC:
        print_code(element)

def build_tree(T, AF):
    if len(T) >= 2:
        V1R1 = T[0]
        V2R2 = T[1]
        V = V1 + V2
        A = [V, V1R1, V2R2]
        if len(T) == 2:
            AF = A
        else:
            NT = sorted([A]+T)
            build_tree(NT, AF)

def coding(A, Code, CF):
    FG = A[1]
    FD = A[2]
    if is_node(FG):
        C1 = coding(FG, [0] + Code)
    else:
        C1 = leaf_coding(FG, [0] + Code)
    if is_node(FD):
        C2 = coding(FD, [1] + Code)
    else:
        C2 = leaf_coding(FD, [1] + Code)
    CF = C1 + C2

def leaf_coding(A, Code, CF):
    Code.reverse()
    CF = [[A[1], A[2], Code]]

def is_node(A):
    if A == 'node':
        return True
    else:
        return False

def print_code(N, Car, Code):
    print(Car + ' : ' + N + ' : ' + Code)

def packList(L):
    if not L:
        return []
    elif len(L) == 1:
        return [[1, L[0]]]
    else:
        X = L[0]
        Rest = L[1:]
        XRun, RRest = run(X, Rest)
        Packed = packList(Rest)
        return [XRun] + Packed

def run(V, L):
    if not L:
        XRun = [1, V]
        RRest = []
    elif V == L[0]:
        N1, RRest = run(V, L[1:])
        N1 = N1 + 1
        XRun = [N1, V]
    else:
        XRun = [1, V]
        RRest = L
    return XRun, RRest