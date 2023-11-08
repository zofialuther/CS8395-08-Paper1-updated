```python
go = 1

L = [1]

def print_niven(arr, N):
    if arr:
        X = arr[0]
        T = arr[1:]
        if isinstance(X, int):
            if go == 1 and N < 20:
                print(X)
                N1 = N + 1
                print_niven(T, N1)
            elif X > 1000:
                print(X)
                global go
                go = 0
            else:
                N1 = N + 1
                print_niven(T, N1)

def gen_niven(X, arr):
    if arr and go == 1:
        N = arr[0]
        T = arr[1:]
        X1 = X + 1
        S = sum_of_digit(X)
        if X % S == 0:
            N = X
            gen_niven(X1, T)
        else:
            gen_niven(X1, [N] + T)

def sum_of_digit(N):
    LC = list(str(N))
    LN = [int(x) for x in LC]
    return sum(LN)

print_niven(L, 1)
gen_niven(1, L)
```