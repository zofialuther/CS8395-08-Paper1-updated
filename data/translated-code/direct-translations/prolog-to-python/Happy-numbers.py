```python
def happy_numbers(L, Nb):
    # creation of the list
    L = [None] * Nb
    # Process of this list
    get_happy_number(L, 1)

# the game is over
def get_happy_number(L, _):
    pass

# querying the next happy_number
def get_happy_number(L, N):
    if not L:
        return
    else:
        N1 = N + 1
        if is_happy_number(N):
            L[0] = N
            get_happy_number(L[1:], N1)
        else:
            get_happy_number(L, N1)

# we must memorize the numbers reached
def is_happy_number(N, L=[N]):
    # a number is happy when we get 1
    if get_next_number(N, 1):
        return True
    # or when this number is not already reached !
    else:
        NN = get_next_number(N)
        if NN not in L:
            return is_happy_number(NN, [NN] + L)

# Process of the next number from N
def get_next_number(N, NewN):
    LD = get_list_digits(N)
    L = list(map(lambda x: square(x), LD))
    NewN = sum(L)

def get_list_digits(N):
    LCD = list(str(N))
    return list(map(lambda x: int(x), LCD))

def square(N):
    return N * N
```