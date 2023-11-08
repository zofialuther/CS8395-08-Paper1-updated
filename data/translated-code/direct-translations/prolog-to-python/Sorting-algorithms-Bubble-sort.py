```python
def bubble_sort(Xs):
    print(Xs)
    Ys, changed = bubble_pass(Xs)
    if changed:
        return bubble_sort(Ys)
    else:
        return Xs

def bubble_pass(Xs):
    if len(Xs) < 2:
        return Xs, False
    else:
        X, Y = Xs[0], Xs[1]
        if X > Y:
            H, T, changed = Y, [X] + Xs[2:], True
        else:
            H, T, changed = X, Xs[1:], False
        R, changed = bubble_pass(T)
        return [H] + R, changed

def test():
    return [8,9,1,3,4,2,6,5,4]

def main():
    T = test()
    result = bubble_sort(T)
    print(result)

main()
```