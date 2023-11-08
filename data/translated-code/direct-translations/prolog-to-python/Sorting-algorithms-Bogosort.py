import random

def bogo_sort(L):
    Min = min(L)
    while True:
        Rl = random.sample(L, len(L))
        if is_sorted(Rl, Min):
            return Rl

def is_sorted(L, P):
    if not L:
        return True
    if L[0] >= P:
        return is_sorted(L[1:], L[0])
    return False