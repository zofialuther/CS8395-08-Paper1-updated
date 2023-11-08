from functools import partial

def fun(X, Y):
    return Y == 2 * X

assert fun(1, 2) == True
assert fun(2, 4) == True
assert fun(3, 6) == True
assert fun(4, 8) == True
assert fun(5, 10) == True

L = list(map(partial(fun, Y=2), [1, 2, 3, 4, 5]))
print(L)