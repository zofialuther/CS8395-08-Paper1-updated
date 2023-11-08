```python
def makepowers():
    for i in range(1, 250):
        assert(fifth_power(i) == i**5)

def within(X, Y, Z):
    return X < Y < Z

def solution(X0, X1, X2, X3, Y):
    makepowers()
    within(X0, 250, X1)
    within(X1, 250, X2)
    within(X2, 250, X3)
    within(X3, 250, Y)
    assert(X0**5 + X1**5 + X2**5 + X3**5 == Y**5)
```