def loop(func, initial, lst):
    return functools.reduce(lambda acc, x: func(acc, x), lst, initial)

def example():
    x = 5
    y = -5
    z = -2
    one = 1
    three = 3
    seven = 7
    return loop(
        lambda sum_prod, j: (sum_prod[0] + abs(j), 
                             (sum_prod[1] * j) if abs(sum_prod[1]) < 2**27 and j != 0 else sum_prod[1]),
        (0, 1),
        [[-three, -three + three + 1, 3**3],
         [-seven, -seven + x, seven],
         [555, 554 - y],
         [22, 22 - three, -28],
         [1927, 1939],
         [x, x + z, y],
         [11**x, 11**x + one]]
    )