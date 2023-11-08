from prologpy import *

def roman():
    LA = [_, 2010, _, 1449, _]
    LR = ['MDCCLXXXIX', _, 'CX', _, 'MDCLXVI']
    maplist(roman, LA, LR)
    maplist(my_print, LA, LR)

def roman(A, R):
    if A > 0:
        roman(A, ['u', 't', 'h', 'th'], LR, [])
        label([A])
        parse_roman(CR, LR, [])
        atom_chars(R, CR)

def roman_0():
    return []

def roman_N(N, [H | T]):
    N1 = N // 10
    N2 = N % 10
    roman(N1, T)
    unity(N2, H)

def unity_1(u):
    return ['I']

def unity_1(t):
    return ['X']

def unity_1(h):
    return ['C']

def unity_1(th):
    return ['M']

# ... (similar for other unity functions)

def parse_roman_CM(T):
    ['CM']
    parse_roman(T)

def parse_roman_CD(T):
    ['CD']
    parse_roman(T)

# ... (similar for other parse_Roman functions)

def my_print(A, R):
    format('~w in roman is ~w~n', [A, R])