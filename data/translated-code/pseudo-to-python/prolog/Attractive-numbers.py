def prime_factors(N, Factors):
    S = square_root(N)
    prime_factors_helper(N, Factors, S, 2)

def prime_factors_helper(1, [], _, _):
    return
def prime_factors_helper(N, [P|Factors], S, P):
    if P <= S and N % P == 0:
        M = N // P
        prime_factors_helper(M, Factors, S, P)
    else:
        Q = P + 1
        if Q <= S:
            prime_factors_helper(N, Factors, S, Q)
def prime_factors_helper(N, [N], _, _):
    return

def is_prime(2):
    return
def is_prime(N):
    if N % 2 == 0:
        return
    else:
        if N > 2 and not is_composite(N, square_root(N), 3):
            return

def is_composite(N, S, P):
    if P <= S and N % P == 0:
        return
    else:
        Q = P + 2
        if Q <= S:
            is_composite(N, S, Q)

def attractive_number(N):
    Factors = prime_factors(N)
    Len = length(Factors)
    return is_prime(Len)

def print_attractive_numbers(From, To, _):
    if From > To:
        return
    else:
        if attractive_number(From):
            print(From)
            if C % 20 == 0:
                print("\n")
            C = C + 1
        else:
            C = C
    Next = From + 1
    print_attractive_numbers(Next, To, C)

def main():
    print_attractive_numbers(1, 120, 1)