```python
from functools import reduce
from itertools import count

def ethMult(n, m):
    def unfoldr(f, x):
        if not f(x):
            return ()
        else:
            return (x,) + unfoldr(f, f(x))
    
    def iterate(f, x):
        return unfoldr(lambda y: True, x)  # using unfoldr as an infinite list
    
    def addedWhereOdd(d, x, a):
        if d % 2 != 0:
            return a + x
        else:
            return a
    
    def half(n):
        return divmod(n, 2)
    
    results = []
    for i in count():
        if i > n:
            break
        results.append(half(i))
    
    return reduce(lambda a, b: addedWhereOdd(b[0], b[1], a), results, m)

def main():
    params = [(3, 4), (5, 6), (7, 8)]
    for p in params:
        print(ethMult(*p))
    
    product_result = getProduct(ethMult(2, 3), ethMult(4, 5))
    sum_result = getSum(ethMult(2, 3), ethMult(4, 5))
    
    print(product_result)
    print(sum_result)
    
    print(ethMult(2, 3))
    print(ethMult(4.5, 6.7))

main()
```