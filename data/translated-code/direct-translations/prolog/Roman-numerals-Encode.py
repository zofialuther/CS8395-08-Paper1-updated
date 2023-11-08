import clpfd

def roman():
    LA = [None, 2010, None, 1449, None]
    LR = ['MDCCLXXXIX', None, 'CX', None, 'MDCLXVI']
    for a, r in zip(LA, LR):
        roman(a, r)
        my_print(a, r)

def roman(A, R):
    if A > 0:
        LR = ['u', 't', 'h', 'th']
        parse_roman(CR, A, LR, [])
        clpfd.label([A])
        R = ''.join(CR)

def parse_roman(CR, 0, []) -> []:
    pass

def parse_roman(CR, N, [H | T]) -> None:
    N1 = N / 10
    N2 = N % 10
    parse_roman(T, N1, [])
    unity(N2, H)

def unity(1, 'u') -> ['I']
def unity(1, 't') -> ['X']
def unity(1, 'h') -> ['C']
def unity(1, 'th') -> ['M']
def unity(4, 'u') -> ['IV']
def unity(4, 't') -> ['XL']
def unity(4, 'h') -> ['CD']
def unity(4, 'th') -> ['MMMM']
def unity(5, 'u') -> ['V']
def unity(5, 't') -> ['L']
def unity(5, 'h') -> ['D']
def unity(5, 'th') -> ['MMMMM']
def unity(9, 'u') -> ['IX']
def unity(9, 't') -> ['XC']
def unity(9, 'h') -> ['CM']
def unity(9, 'th') -> ['MMMMMMMMM']
def unity(0, _) -> []

def unity(V, U):
    if V > 5:
        V1 = V - 5
        unity(U, 5)
        unity(U, V1)
    if 1 < V < 4:
        V1 = V - 1
        unity(1, U)
        unity(V1, U)

def parse_roman(['C', 'M' | T]) -> parse_roman(T)
def parse_roman(['C', 'D' | T]) -> parse_roman(T)
def parse_roman(['X', 'C' | T]) -> parse_roman(T)
def parse_roman(['X', 'L' | T]) -> parse_roman(T)
def parse_roman(['I', 'X' | T]) -> parse_roman(T)
def parse_roman(['I', 'V' | T]) -> parse_roman(T)
def parse_roman([H | T]) -> parse_roman(T)
def parse_roman([]) -> []

def my_print(A, R):
    print(f'{A} in roman is {R}')

roman()