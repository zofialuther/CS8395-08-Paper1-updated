```python
def happy_numbers(L, Nb):
    if len(L) == Nb:
        get_happy_number(L, 1)

def get_happy_number([], _):
    pass

def get_happy_number([H, *T], N):
    N1 = N+1
    if is_happy_number(N):
        H = N
        get_happy_number(T, N1)
    else:
        get_happy_number([H, *T], N1)

def is_happy_number(N):
    is_happy_number(N, [N])

def is_happy_number(N, _L):
    get_next_number(N, 1)

def is_happy_number(N, L):
    NN = get_next_number(N)
    if NN not in L:
        is_happy_number(NN, [NN, *L])

def get_next_number(N):
    LD = get_list_digits(N)
    L = map(square, LD)
    NewN = sum(L)
    return NewN

def get_list_digits(N):
    LCD = list(str(N))
    LD = map(int, LCD)
    return LD

def square(N):
    return N * N
```