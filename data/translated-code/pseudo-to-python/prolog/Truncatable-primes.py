def largest_left_truncatable_prime(N, P):
    if is_left_truncatable_prime(N):
        return
    N1 = N - 1
    largest_left_truncatable_prime(N1, P)

def is_left_truncatable_prime(P):
    if is_prime(P) and is_left_truncatable_prime(P, P, 10):
        return

def is_left_truncatable_prime(P, _, N):
    if P <= N:
        return
    Q1 = P % N
    if is_prime(Q1) and Q != Q1:
        N1 = N * 10
        is_left_truncatable_prime(P, Q1, N1)

def largest_right_truncatable_prime(N, P):
    if is_right_truncatable_prime(N):
        return
    N1 = N - 1
    largest_right_truncatable_prime(N1, P)

def is_right_truncatable_prime(P):
    if is_prime(P):
        Q = P // 10
        if Q == 0:
            return
        else:
            is_right_truncatable_prime(Q)

def main(N):
    find_prime_numbers(N)
    L = largest_left_truncatable_prime(N, N)
    print('Largest left-truncatable prime less than {}: {}'.format(N, L))
    R = largest_right_truncatable_prime(N, N)
    print('Largest right-truncatable prime less than {}: {}'.format(N, R))

def main():
    main(1000000)