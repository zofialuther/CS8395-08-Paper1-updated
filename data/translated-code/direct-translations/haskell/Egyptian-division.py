```python
def egyptianQuotRem(m, n):
    def unfoldr(func, state):
        result = []
        while state is not None:
            state, val = func(state)
            if state is not None:
                result.append(val)
        return result

    def trace(message, value):
        print(message)
        return value

    rows = unfoldr(lambda state: (None, (state[0], state[1])) if state[1] > m else ((state[0] + state[0], state[1] + state[1]), (state[0], state[1])), (1, n))

    print("Number pair unfolded to series of doubling rows:")
    print(rows)
    print("\nRows refolded down to (quot, rem):")
    print((0, m))

    def foldr(func, acc, lst):
        for item in lst:
            acc = func(item, acc)
        return acc

    result = foldr(lambda item, acc: (acc[0] + item[0], acc[1] - item[1]) if item[1] < acc[1] else acc, (0, m), rows)
    return result

print(egyptianQuotRem(580, 34))
```