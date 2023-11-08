def proper_divisors(N, L):
    if N == 1:
        return []
    else:
        FSQRTN = int(N ** 0.5)
        return proper_divisors_helper(2, FSQRTN, N, [1])


def proper_divisors_helper(M, FSQRTN, N, L):
    if M > FSQRTN:
        return L
    elif N % M == 0:
        MO = N // M
        L.append(M)
        L.append(MO)
        return proper_divisors_helper(M + 1, FSQRTN, N, L)
    else:
        return proper_divisors_helper(M + 1, FSQRTN, N, L)


def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


def dpa(N):
    if N == 1:
        print("deficient: 0\nabundant: 0\nperfect: 0")
        print("took 0 seconds")
    else:
        T0 = time.process_time()
        D = proper_divisors(N, [])
        SPN = sum_list(D)
        if SPN < N:
            print(f"deficient: {len(D)}")
            print(f"abundant: 0")
            print(f"perfect: 1")
        elif SPN == N:
            print(f"deficient: {len(D)}")
            print(f"abundant: 0")
            print(f"perfect: 1")
        else:
            print(f"deficient: {len(D)}")
            print(f"abundant: 1")
            print(f"perfect: 0")
        Dur = time.process_time() - T0
        print(f"took {Dur} seconds")


# Example usage
dpa(12)