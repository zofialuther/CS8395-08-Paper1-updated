```python
mertens_number_cache = {}

def mertens_number(N, M):
    if N == 1:
        return 1
    if (N, M) in mertens_number_cache:
        return mertens_number_cache[(N, M)]
    if N >= 2:
        result = calculate_mertens_number(N, 2, M, 0)
        mertens_number_cache[(N, M)] = result
        return result

def calculate_mertens_number(N, K, M, S):
    if N == K:
        return M
    N1 = N // K
    M1 = mertens_number(N1, M)
    K1 = K + 1
    S1 = S - M1
    return calculate_mertens_number(N, K1, M, S1)

def print_mertens_numbers(Count):
    print_mertens_numbers_helper(Count, 0)

def print_mertens_numbers_helper(Count, N):
    if N == Count:
        return
    if N == 0:
        print(" ")
    else:
        M = mertens_number(N, M)
        print(f"{M} ", end="")
    N1 = N + 1
    Column = N1 % 20
    if N > 0 and Column == 0:
        print("\n")
    else:
        print_mertens_numbers_helper(Count, N1)

def count_zeros(From, To, Z, C):
    return count_zeros_helper(From, To, Z, C, 0, 0, 0)

def count_zeros_helper(From, To, Z, C, Z1, C1, P):
    if From > To:
        return Z, C
    M = mertens_number(From, M)
    if M == 0:
        Z2 = Z1 + 1
    else:
        Z2 = Z1
    if M == 0 and P != 0:
        C2 = C1 + 1
    else:
        C2 = C1
    Next = From + 1
    return count_zeros_helper(Next, To, Z, C, Z2, C2, M)

print("First 199 Mertens numbers:")
print_mertens_numbers(200)
Z, C = count_zeros(1, 1000, 0, 0)
print(f"Zeros: {Z}, Consecutive Zeros: {C}")
```