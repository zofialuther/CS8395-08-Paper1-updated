import random

def bogo_sort(L, Rl):
    Min = min(L)
    while not is_sorted(Rl, Min):
        Rl = random.sample(L, len(L))

def is_sorted(lst, prev):
    if not lst:
        return True
    else:
        if lst[0] >= prev:
            return is_sorted(lst[1:], lst[0])
        else:
            return False