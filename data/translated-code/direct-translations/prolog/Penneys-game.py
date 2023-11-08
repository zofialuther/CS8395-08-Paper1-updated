import random

def play():
    R = rand1()
    game(R)

def game(h):
    print('Your turn first!')
    P = player_move()
    C = response(P)
    print('I am choosing', end=' ')
    for item in C:
        writec(item)
    print()
    R = [rand1() for _ in range(3)]
    for item in R:
        writec(item)
    roll(P, C, R)

def game(t):
    C = [rand1() for _ in range(3)]
    print('I am choosing', end=' ')
    for item in C:
        writec(item)
    print()
    P = player_move()
    R = [rand1() for _ in range(3)]
    for item in R:
        writec(item)
    roll(P, C, R)

def player_move():
    Codes = input()
    P1,P2,P3 = map(char_code, Codes)
    return [P1,P2,P3]

def roll(P, _, P):
    print()
    print('You Win!')
    return
def roll(_, C, C):
    print()
    print('I Win!')
    return

def roll(P, C, [_,A,B]):
    R = rand1()
    S = coin_s(R)
    print(S, end='')
    roll(P, C, [A,B,R])

def response(P):
    A, B, _ = P
    C = [opp(A), A, B]
    return C

def writec(A):
    A1 = coin_s(A)
    print(A1, end='')

def rand1():
    V = random.random()
    I = round(V)
    return coin(I)

def rand3():
    R1 = rand1()
    R2 = rand1()
    R3 = rand1()
    return [R1, R2, R3]

def coin(I):
    if I == 0:
        return 'h'
    else:
        return 't'

def coin_s(A):
    if A == 'h':
        return 'H'
    else:
        return 'T'

def opp(A):
    if A == 'h':
        return 't'
    else:
        return 'h'