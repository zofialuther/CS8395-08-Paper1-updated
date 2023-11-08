```python
fusc_cache = {}

def fusc(N):
    if N in fusc_cache:
        return fusc_cache[N]
    if N == 0:
        fusc_cache[N] = 0
        return 0
    if N == 1:
        fusc_cache[N] = 1
        return 1
    if N % 2 == 0:
        M = N // 2
        f = fusc(M)
        fusc_cache[N] = f
        return f
    else:
        N1 = (N - 1) // 2
        N2 = (N + 1) // 2
        f1 = fusc(N1)
        f2 = fusc(N2)
        f = f1 + f2
        fusc_cache[N] = f
        return f

def print_fusc_sequence(N):
    print(f'First {N} fusc numbers:')
    for i in range(N):
        print(fusc(i), end=' ')
    print()

def print_max_fusc(N):
    Max = 0
    print(f'Fusc numbers up to {N} that are longer than any previous one:')
    for i in range(N):
        f = fusc(i)
        if f >= Max:
            print(f'n = {i}, fusc(n) = {f}')
            Max = max(10, f * 10)

def main():
    print_fusc_sequence(61)
    print_max_fusc(1000000)

if __name__ == "__main__":
    main()
```