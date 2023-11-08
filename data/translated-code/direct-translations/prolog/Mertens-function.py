```python
mertens_number_cache = {}

def mertens_number(N):
    if N == 1:
        return 1
    elif N in mertens_number_cache:
        return mertens_number_cache[N]
    else:
        M = 0
        for i in range(2, N + 1):
            M1 = mertens_number(N // i)
            M -= M1
        mertens_number_cache[N] = M
        return M

def print_mertens_numbers(Count):
    for i in range(Count):
        if i == 0:
            print('   ', end='')
        else:
            M = mertens_number(i)
            print(f'{M:3}', end='')
        if i > 0 and (i + 1) % 20 == 0:
            print()

def count_zeros(From, To):
    Z = 0
    C = 0
    for i in range(From, To + 1):
        M = mertens_number(i)
        if M == 0:
            Z += 1
            if M != 0:
                C += 1
    return Z, C

print('First 199 Mertens numbers:')
print_mertens_numbers(200)
Z, C = count_zeros(1, 1000)
print(f'M(n) is zero {Z} times for 1 <= n <= 1000.')
print(f'M(n) crosses zero {C} times for 1 <= n <= 1000.')
```