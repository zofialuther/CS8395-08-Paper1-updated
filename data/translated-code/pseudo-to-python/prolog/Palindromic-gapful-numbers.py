```python
def init_palindrome(Digit, p):
    Next = Digit * 10 - 1
    p[0] = 10
    p[1] = Next
    p[2] = 0

def next_palindrome(Digit, p, p1, Palindrome):
    Power = p[0]
    Next = p[1]
    Even = p[2]
    Next1 = Next + 1
    if Next1 == Power * (Digit + 1):
        if Even == 1:
            Power1 = Power * 10
        else:
            Power1 = Power
        Next2 = Digit * Power1
        Even1 = 1 - Even
    else:
        Power1 = Power
        Next2 = Next1
        Even1 = Even
    if Even1 == 1:
        X = 10 * Power1
        Y = Next2
    else:
        X = Power1
        Y = Next2 // 10
    Z = reverse_number(Y)
    Palindrome = Next2 * X + Z

def reverse_number(N):
    return reverse_number_recursive(N, 0)

def reverse_number_recursive(N, R):
    if N == 0:
        return R
    else:
        R1 = R * 10 + N % 10
        N1 = N // 10
        return reverse_number_recursive(N1, R1)

def is_gapful(N):
    return is_gapful_recursive(N, N)

def is_gapful_recursive(N, M):
    if M < 10:
        return 0 == N % (N % 10 + 10 * (M % 10))
    else:
        M1 = M // 10
        return is_gapful_recursive(N, M1)

def find_palindromic_gapful_numbers(N, List):
    return find_palindromic_gapful_numbers_recursive(N, 1, List)

def find_palindromic_gapful_numbers_recursive(N, Digit, List):
    return find_palindromic_gapful_numbers1(Digit, N)

def find_palindromic_gapful_numbers1(Digit, N):
    P = [0, 0, 0]
    init_palindrome(Digit, P)
    return find_palindromic_gapful_numbers1(Digit, P, N, 0)

def find_palindromic_gapful_numbers1(Digit, P, N, Count):
    P_next = [0, 0, 0]
    Palindrome = next_palindrome(Digit, P, P_next)
    if is_gapful(Palindrome):
        Count1 = Count + 1
        List = [Palindrome]
    else:
        Count1 = Count
        List = []
    return find_palindromic_gapful_numbers1(Digit, P_next, N, Count1)

def print_numbers(First, Last, Numbers):
    if First == 1:
        print("First {} palindromic gapful numbers ending in:".format(Last))
    else:
        Count = Last - First + 1
        print("Last {} of first {} palindromic gapful numbers ending in:".format(Count, Last))
    print_numbers_recursive(First, Last, 1, Numbers)

def print_numbers_recursive(First, Last, Digit, Numbers):
    if Digit == 10:
        return
    else:
        print("{}:".format(Digit))
        print_numbers1(First, Last, 1, Numbers)
        Next_digit = Digit + 1
        print_numbers_recursive(First, Last, Next_digit, Numbers)

def print_numbers1(First, Last, I, Numbers):
    if I > Last:
        print("\n")
        return
    else:
        if I < First:
            J = I + 1
            print_numbers1(First, Last, J, Numbers)
        else:
            print(" {}".format(Numbers[I]))
            J = I + 1
            print_numbers1(First, Last, J, Numbers)

def main():
    Numbers = find_palindromic_gapful_numbers(1000)
    print_numbers(1, 20, Numbers)
    print_numbers(86, 100, Numbers)
    print_numbers(991, 1000, Numbers)
```