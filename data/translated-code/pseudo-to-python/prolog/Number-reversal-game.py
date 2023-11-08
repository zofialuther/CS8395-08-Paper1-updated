```python
import random

def play():
    L = generate_random_numbers()
    take_turn(0, L)

def take_turn(N, L):
    print_list(L)
    F = determine_number_to_flip()
    NewList = flip(L, F, [])
    N1 = N + 1
    check_if_sorted(N1, NewList)

def determine_number_to_flip():
    F = int(input())
    while F not in range(1, 10):
        F = int(input())
    return F

def flip(L, N, C):
    if N == 0:
        return C + L
    else:
        return flip(L[1:], N-1, [L[0]]+C)

def check_if_sorted(N, L):
    if L == sorted(L):
        print_list(L)
        print(f'-> {N}')
    else:
        take_turn(N, L)

def generate_random_numbers():
    return random.sample(range(1, 10), 9)

def print_list(L):
    FormattedList = ' '.join(map(str, L))
    print(f'({FormattedList})', end=' ')

play()
```