```python
def memoize(func):
    cache = {}

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func

@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

@memoize
def catalan_direct(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n))

@memoize
def catalan_recursive_simple(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_recursive_simple(i) * catalan_recursive_simple(n-i-1)
    return res

@memoize
def catalan_recursive_efficient(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n)) // (n+1)

def main():
    for i in range(10):
        print(f"Direct Catalan ({i}): {catalan_direct(i)}")
        print(f"Recursive Catalan Simple ({i}): {catalan_recursive_simple(i)}")
        print(f"Recursive Catalan Efficient ({i}): {catalan_recursive_efficient(i)}")

if __name__ == "__main__":
    main()
```