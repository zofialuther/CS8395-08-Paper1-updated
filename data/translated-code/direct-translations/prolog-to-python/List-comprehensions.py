```python
# We need operators
op(700, 'xfx', '<-')
op(450, 'xfx', '..')
op(1100, 'yfx', '&')

# use for explicit list usage
def my_bind(V, L):
    if L:
        V = L[0]
    else:
        my_bind(V, L[1:])

# we need to define the intervals of numbers
def interval(Vs, M, N):
    if isinstance(M, int) and isinstance(N, int) and M <= N:
        for i in range(M, N+1):
            Vs.append(i)

# for explicit list comprehension like Vs <- [1,2,3]
def list_comprehension(Vs, Xs):
    if isinstance(Xs, list):
        for x in Xs:
            Vs.append(x)

# finally we define list comprehension
# prototype is Vs <- {Var, Dec, Pred} where
# Var is the list of variables to output
# Dec is the list of intervals of the variables
# Pred is the list of predicates
def final_list_comprehension(Vs, Var, Dec, Pred):
    for d in Dec:
        for p in Pred:
            Vs.append(Var)

# for list comprehension without Pred
def list_comprehension_no_pred(Vs, Var, Dec):
    for d in Dec:
        Vs.append(Var)
```