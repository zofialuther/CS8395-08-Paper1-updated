```python
import itertools

def makepowers():
    global pow5
    pow5 = {}
    for X in range(1, 250):
        Y = X * X * X * X * X
        pow5[X] = Y

def within(A, Bx, N):
    B = Bx - 1
    return range(A, B+1, N)

def solution():
    makepowers()
    X0_values = within(4, 250, 1)
    X1_values = within(3, X0_values[-1], 1)
    X2_values = within(2, X1_values[-1], 1)
    X3_values = within(1, X2_values[-1], 1)

    for combo in itertools.product(X0_values, X1_values, X2_values, X3_values):
        X0_5th = pow5[combo[0]]
        X1_5th = pow5[combo[1]]
        X2_5th = pow5[combo[2]]
        X3_5th = pow5[combo[3]]
        Y_5th = X0_5th + X1_5th + X2_5th + X3_5th
        for key, value in pow5.items():
            if value == Y_5th:
                print(combo[0], combo[1], combo[2], combo[3], key)

solution()
```