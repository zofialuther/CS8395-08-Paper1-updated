import random

def play():
    R = rand1()
    game(R)

def game(h):
    print('Your turn first!')
    P = player_move()
    C = response(P)
    print('I am choosing', end='')
    for c in C:
        writec(c)
    print()
    R = rand3()
    for r in R:
        writec(r)
    roll(P, C, R)

def game(t):
    C = rand3()
    print('I am choosing', end='')
    for c in C:
        writec(c)
    print()
    P = player_move()
    R = rand3()
    for r in R:
        writec(r)
    roll(P, C, R)

def player_move():
    Codes = input()
    P1 = chr(Codes[0])
    P2 = chr(Codes[1])
    P3 = chr(Codes[2])
    return [P1, P2, P3]

def roll(P, _, P):
    print('\nYou Win!\n')

def roll(_, C, C):
    print('\nI Win!\n')

def roll(P, C, [_, A, B]):
    R = rand1()
    S = coin_s(R)
    print(S)
    roll(P, C, [A, B, R])

def response(P):
    return [opp(P[0]), P[0], P[1]]

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