```python
def count_digits(Number, Count):
    A = str(Number)
    Count = len(A)

def integer_to_atom(Number, Atom):
    A = str(Number)
    Count = len(A)
    if Count <= 20:
        Atom = A
    else:
        A1 = A[0:10]
        P = Count - 10
        A2 = A[P:10]
        A3 = A1 + '...'
        Atom = A3 + A2

def egyptian(X, Y, E):
    if X == 0:
        return
    else:
        Z = (Y + X - 1) // X
        X1 = -Y % X
        Y1 = Y * Z
        egyptian(X1, Y1, E)

def print_egyptian(E):
    if not E:
        return
    else:
        N = str(E[0])
        if len(E) == 1:
            print('1/' + N)
        else:
            print('1/' + N, end=' ')
            print_egyptian(E[1:])

def max_terms_and_denominator1(D, Max_terms, Max_denom, Max_terms1, Max_denom1):
    max_terms_and_denominator1(D, 1, Max_terms, Max_denom, Max_terms1, Max_denom1)

def max_terms_and_denominator1(D, D, Max_terms, Max_denom, Max_terms, Max_denom):
    return
def max_terms_and_denominator1(D, N, Max_terms, Max_denom, Max_terms1, Max_denom1):
    Max_terms1 = f(_, _, _, Len1)
    Max_denom1 = f(_, _, _, Max1)
    egyptian(N, D, E)
    Len = len(E)
    Max = E[-1]
    if Len > Len1:
        Max_terms2 = f(N, D, E, Len)
    else:
        Max_terms2 = Max_terms1
    if Max > Max1:
        Max_denom2 = f(N, D, E, Max)
    else:
        Max_denom2 = Max_denom1
    N1 = N + 1
    max_terms_and_denominator1(D, N1, Max_terms, Max_denom, Max_terms2, Max_denom2)

def max_terms_and_denominator(N, Max_terms, Max_denom):
    max_terms_and_denominator(N, 1, Max_terms, Max_denom, f(0, 0, [], 0), f(0, 0, [], 0))

def max_terms_and_denominator(N, N, Max_terms, Max_denom, Max_terms, Max_denom):
    return
def max_terms_and_denominator(N, N1, Max_terms, Max_denom, Max_terms1, Max_denom1):
    max_terms_and_denominator1(N1, Max_terms2, Max_denom2, Max_terms1, Max_denom1)
    N2 = N1 + 1
    max_terms_and_denominator(N, N2, Max_terms, Max_denom, Max_terms2, Max_denom2)

def show_max_terms_and_denominator(N):
    print('Proper fractions with most terms and largest denominator, limit =', N)
    max_terms_and_denominator(N, f(N_max_terms, D_max_terms, E_max_terms, Len), f(N_max_denom, D_max_denom, E_max_denom, Max))
    print('Most terms (Len): N_max_terms/D_max_terms = ', end='')
    print_egyptian(E_max_terms)
    count_digits(Max, Digits)
    print('Largest denominator (', Digits, ' digits): N_max_denom/D_max_denom = ', end='')
    print_egyptian(E_max_denom)

def main():
    print_egyptian(43, 48)
    print_egyptian(5, 121)
    print_egyptian(2014, 59)
    print()
    show_max_terms_and_denominator(100)
    print()
    show_max_terms_and_denominator(1000)

main()
```