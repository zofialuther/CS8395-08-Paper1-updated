```python
def fusc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return fusc(n/2)
    else:
        return fusc((n-1)/2) + fusc((n+1)/2)

def infiniteFusc():
    n = 0
    while True:
        yield fusc(n)
        n += 1

def firstFuscOfEachMagnitude():
    n = 1
    while True:
        yield fusc(2**n)
        n += 1

def main():
    fusc_sequence = take(61, infiniteFusc())
    first_fusc_magnitude = take(10, firstFuscOfEachMagnitude())
    showList(fusc_sequence)
    showList(first_fusc_magnitude)

def iterate(func, x):
    while True:
        yield x
        x = func(x)

def showList(lst):
    for item in lst:
        print(item, end=" ")
    print()

def take(n, iterable):
    return [next(iterable) for _ in range(n)]

if __name__ == "__main__":
    main()
```