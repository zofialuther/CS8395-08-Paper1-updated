def count_digits(Number, Count):
    A = str(Number)
    Count = len(A)

def integer_to_atom(Number, Atom):
    A = str(Number)
    Count = len(A)
    if Count <= 20:
        Atom = A
    else:
        A1 = A[:10]
        P = Count - 10
        A2 = A[P:]
        A3 = A1 + '...' + A2
        Atom = A3

def egyptian(X, Y, result):
    if X == 0:
        return []
    else:
        Z = (Y + X - 1) // X
        X1 = -Y % X
        Y1 = Y * Z
        return [Z] + egyptian(X1, Y1, result)

def print_egyptian(List):
    for N in List:
        A = str(N)
        print(1/A, end='')
        if List[-1] != N:
            print(' + ', end='')

def print_egyptian(X, Y):
    print(f"Egyptian fraction for {X}/{Y}: ", end='')
    if X > Y:
        N = X // Y
        print(f"[{N}] ", end='')
        X1 = X % Y
    else:
        X1 = X
    E = egyptian(X1, Y, [])
    print_egyptian(E)
    print("\n")

def max_terms_and_denominator1(D, N, Max_terms, Max_denom, Max_terms1, Max_denom1):
    if D == N:
        return (Max_terms, Max_denom)
    else:
        E = egyptian(N, D, [])
        Len = len(E)
        Max = E[-1]
        if Len > Max_terms1[3]:
            Max_terms2 = (N, D, E, Len)
        else:
            Max_terms2 = Max_terms1
        if Max > Max_denom1[3]:
            Max_denom2 = (N, D, E, Max)
        else:
            Max_denom2 = Max_denom1
        N1 = N + 1
        return max_terms_and_denominator1(D, N1, Max_terms, Max_denom, Max_terms2, Max_denom2)

def max_terms_and_denominator(N, Max_terms, Max_denom):
    return max_terms_and_denominator1(N, 1, Max_terms, Max_denom, (0, 0, [], 0), (0, 0, [], 0))

def show_max_terms_and_denominator(N):
    print(f"Proper fractions with most terms and largest denominator, limit = {N}:")
    result = max_terms_and_denominator(N, (0, 0, [], 0), (0, 0, [], 0))
    (N_max_terms, D_max_terms, E_max_terms, Len) = result[0]
    (N_max_denom, D_max_denom, E_max_denom, Max) = result[1]
    print(f"Most terms ({Len}): {N_max_terms}/{D_max_terms} = ", end='')
    print_egyptian(E_max_terms)
    count_digits(Max, Digits)
    print(f"Largest denominator ({Digits} digits): {N_max_denom}/{D_max_denom} = ", end='')
    print_egyptian(E_max_denom)
    print("\n")

def main():
    print_egyptian(43, 48)
    print_egyptian(5, 121)
    print_egyptian(2014, 59)
    print("\n")
    show_max_terms_and_denominator(100)
    print("\n")
    show_max_terms_and_denominator(1000)

main()