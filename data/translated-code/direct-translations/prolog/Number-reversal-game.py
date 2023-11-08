import random
import itertools

def play():
    L = random_numbers()
    do_turn(0, L)

def do_turn(N, L):
    print_list(L)
    F = how_many_to_flip()
    Lnew = flip(L, F)
    N1 = N + 1
    sorted(N1, Lnew)

def how_many_to_flip():
    F = int(input())
    if F in range(1, 10):
        return F
    else:
        print("Please enter a number between 1 and 9")
        return how_many_to_flip()

def flip(L, F):
    return L[F:] + L[:F]

def sorted(N, L):
    if L == sorted(L):
        print_list(L)
        print(f'-> {N}')
    else:
        do_turn(N, L)

def random_numbers():
    return random.sample(range(1, 10), 9)

def print_list(L):
    Lf = ' '.join(map(str, L))
    print(f'({Lf}) ')

play()