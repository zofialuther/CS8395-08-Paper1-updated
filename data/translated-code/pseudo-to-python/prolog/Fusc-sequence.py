```python
fusc_cache = {}

def fusc(N, F):
    if (N, F) in fusc_cache:
        return fusc_cache[(N, F)]
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N % 2 == 0:
        M = N // 2
        fusc_cache[(N, F)] = fusc(M, F)
    else:
        N1 = (N - 1) // 2
        N2 = (N + 1) // 2
        F1 = fusc(N1, F)
        F2 = fusc(N2, F)
        F = F1 + F2
        fusc_cache[(N, F)] = F
    return fusc_cache[(N, F)]

def print_fusc_sequence(N):
    print("First N fusc numbers:")
    for i in range(N):
        print(fusc(i, 0), end=" ")
    print()

def print_max_fusc(N):
    print("Fusc numbers up to N that are longer than any previous one:")
    for i in range(N):
        F = fusc(i, 0)
        if F >= 10:
            print("n =", i, ", fusc(n) =", F)
        elif F >= 10 and F > Max:
            print("n =", i, ", fusc(n) =", F)
            Max = max(10, Max * 10)

def main():
    print_fusc_sequence(61)
    print_max_fusc(1000000)

main()
```