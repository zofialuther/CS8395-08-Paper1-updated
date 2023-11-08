def play24(Len, Range, Goal):
    L, S = game(Len, Range, Goal)
    for item in L:
        my_write(item)
    print(': ', S)

def game(Len, Range, Value):
    L = [choose(Range) for _ in range(Len)]
    S = compute(L, Value, [])
    return L, S

def choose(Range):
    import random
    return random.randint(1, Range)

def write_tree(M, S):
    # Implementation of write_tree function
    pass

def is_add(Op):
    # Implementation of is_add function
    pass

def compute(L, Value, CS):
    # Implementation of compute function
    pass

def next_value(M, N, R, CS, Expr):
    # Implementation of next_value function
    pass

def my_write(V):
    print(V, end=' ')